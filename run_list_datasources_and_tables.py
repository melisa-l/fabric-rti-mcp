"""
Run this locally to list external data sources and tables in the Fabric Lakehouse SQL endpoint.

Usage (PowerShell):
    $env:FABRIC_SQL_ENDPOINT = "your-sql-endpoint.fabric.windows.net"
    $env:FABRIC_LAKEHOUSE_NAME = "YourLakehouseDatabaseName"
    az login
    python run_list_datasources_and_tables.py

This script uses DefaultAzureCredential (which will pick up `az login` for local dev).
It encodes the Azure AD access token as UTF-16-LE bytes before passing to the ODBC driver
(which is required on Windows for SQL Server token auth).

Make sure you have:
    pip install pyodbc azure-identity
    ODBC Driver 18 for SQL Server installed (matching your Python bitness)

Security: the token is handled briefly in memory and then deleted/overwritten where practical.
"""

import os
import sys
import traceback
import pyodbc
from azure.identity import DefaultAzureCredential

SQL_DATASOURCES_QUERY = """
SELECT name, data_source_type, location
FROM sys.external_data_sources
ORDER BY name
"""

SQL_TABLES_QUERY = """
SELECT TABLE_SCHEMA, TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE'
ORDER BY TABLE_SCHEMA, TABLE_NAME
"""


def get_token_bytes(scope: str = "https://database.windows.net/.default") -> bytearray:
    cred = DefaultAzureCredential()
    token = cred.get_token(scope).token
    # Encode as UTF-16-LE bytes for the Microsoft ODBC driver on Windows
    tb = bytearray(token.encode("utf-16-le"))
    # Remove plain token reference quickly
    try:
        del token
    except Exception:
        pass
    return tb


def connect_with_token(sql_endpoint: str, database: str, token_bytes: bytearray):
    conn_str = (
        f"Driver={{ODBC Driver 18 for SQL Server}};"
        f"Server=tcp:{sql_endpoint},1433;"
        f"Database={database};"
        f"Encrypt=yes;TrustServerCertificate=no;"
        "Authentication=ActiveDirectoryAccessToken"
    )
    # The SQL_COPT_SS_ACCESS_TOKEN option id is 1256
    conn = pyodbc.connect(conn_str, attrs_before={1256: bytes(token_bytes)})
    return conn


def list_rows(conn, sql: str):
    with conn.cursor() as cur:
        cur.execute(sql)
        return cur.fetchall()


def main():
    sql_endpoint = os.getenv("FABRIC_SQL_ENDPOINT")
    database = os.getenv("FABRIC_LAKEHOUSE_NAME")
    if not sql_endpoint or not database:
        print("FABRIC_SQL_ENDPOINT and FABRIC_LAKEHOUSE_NAME must be set in the environment.")
        sys.exit(1)

    print(f"Using endpoint: {sql_endpoint}  database: {database}")

    token_bytes = None
    conn = None
    try:
        print("Acquiring Azure AD token... (DefaultAzureCredential)")
        token_bytes = get_token_bytes()
        print("Connecting to the SQL endpoint via ODBC...")
        conn = connect_with_token(sql_endpoint, database, token_bytes)
        print("Connected. Querying external data sources...")
        datasources = list_rows(conn, SQL_DATASOURCES_QUERY)
        if datasources:
            print("External data sources:")
            for row in datasources:
                # row columns: name, data_source_type, location (may vary)
                print(" - ", tuple(row))
        else:
            print("No external data sources found or query returned no rows.")

        print("\nQuerying tables...")
        tables = list_rows(conn, SQL_TABLES_QUERY)
        if tables:
            print("Tables:")
            for schema, name in tables:
                print(f" - {schema}.{name}")
        else:
            print("No tables found or query returned no rows.")

    except Exception as e:
        print("Error while querying the lakehouse:")
        traceback.print_exc()
        sys.exit(2)

    finally:
        # Close connection
        try:
            if conn:
                conn.close()
        except Exception:
            pass
        # Zero and delete token bytes to reduce lifetime in memory
        try:
            if token_bytes is not None:
                for i in range(len(token_bytes)):
                    token_bytes[i] = 0
                del token_bytes
        except Exception:
            pass

    print("Done.")


if __name__ == "__main__":
    main()
