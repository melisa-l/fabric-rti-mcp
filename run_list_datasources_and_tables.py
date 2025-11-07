#!/usr/bin/env python3#!/usr/bin/env python3

""""""

Run this locally to list tables in the Fabric Lakehouse SQL endpoint.Run this locally to list external data sources and tables in the Fabric Lakehouse SQL endpoint.



Usage (PowerShell):Usage (PowerShell):

    $env:FABRIC_SQL_ENDPOINT = "your-sql-endpoint.fabric.windows.net"    $env:FABRIC_SQL_ENDPOINT = "your-sql-endpoint.fabric.windows.net"

    $env:FABRIC_LAKEHOUSE_NAME = "YourLakehouseDatabaseName"    $env:FABRIC_LAKEHOUSE_NAME = "YourLakehouseDatabaseName"

    python run_list_datasources_and_tables.py    python run_list_datasources_and_tables.py



This script uses ActiveDirectoryInteractive authentication which will prompt for credentialsThis script uses ActiveDirectoryInteractive authentication which will prompt for credentials

in your default web browser.in your default web browser.



Make sure you have:Make sure you have:

    pip install pyodbc    pip install pyodbc

    ODBC Driver 18 for SQL Server installed (matching your Python bitness)    ODBC Driver 18 for SQL Server installed (matching your Python bitness)

""""""



import osimport os

import sysimport sys

from typing import List, Tuplefrom typing import List, Tuple

import pyodbcimport pyodbc



SQL_TABLES_QUERY = """SQL_DATASOURCES_QUERY = """

SELECT TABLE_SCHEMA, TABLE_NAMESELECT name, data_source_type, location

FROM INFORMATION_SCHEMA.TABLESFROM sys.external_data_sources

WHERE TABLE_TYPE = 'BASE TABLE'ORDER BY name

ORDER BY TABLE_SCHEMA, TABLE_NAME"""

"""

SQL_TABLES_QUERY = """

def list_rows(conn: pyodbc.Connection, sql: str) -> List[Tuple[str, ...]]:SELECT TABLE_SCHEMA, TABLE_NAME

    with conn.cursor() as cur:FROM INFORMATION_SCHEMA.TABLES

        cur.execute(sql)WHERE TABLE_TYPE = 'BASE TABLE'

        return [tuple(row) for row in cur.fetchall()]ORDER BY TABLE_SCHEMA, TABLE_NAME

"""

def main() -> None:

    conn = Nonedef list_rows(conn: pyodbc.Connection, sql: str) -> List[Tuple[str, ...]]:

    try:    with conn.cursor() as cur:

        sql_endpoint = os.getenv("FABRIC_SQL_ENDPOINT")        cur.execute(sql)

        database = os.getenv("FABRIC_LAKEHOUSE_NAME")        return [tuple(row) for row in cur.fetchall()]

        if not sql_endpoint or not database:

            print("FABRIC_SQL_ENDPOINT and FABRIC_LAKEHOUSE_NAME must be set in the environment.", file=sys.stderr)def main() -> None:

            sys.exit(1)    conn = None

    try:

        print(f"Using endpoint: {sql_endpoint}  database: {database}")        sql_endpoint = os.getenv("FABRIC_SQL_ENDPOINT")

        database = os.getenv("FABRIC_LAKEHOUSE_NAME")

        conn_str = (        if not sql_endpoint or not database:

            f"Driver={{ODBC Driver 18 for SQL Server}};"            print("FABRIC_SQL_ENDPOINT and FABRIC_LAKEHOUSE_NAME must be set in the environment.", file=sys.stderr)

            f"Server={sql_endpoint};"            sys.exit(1)

            f"Database={database};"

            "Authentication=ActiveDirectoryInteractive;"        print(f"Using endpoint: {sql_endpoint}  database: {database}")

            "Encrypt=yes;TrustServerCertificate=no"

        )        conn_str = (

            f"Driver={{ODBC Driver 18 for SQL Server}};"

        print("Connecting to the SQL endpoint via ODBC (browser authentication will open)...")            f"Server={sql_endpoint};"

        conn = pyodbc.connect(conn_str)            f"Database={database};"

            "Authentication=ActiveDirectoryInteractive;"

        print("\nQuerying tables...")            "Encrypt=yes;TrustServerCertificate=no"

        tables = list_rows(conn, SQL_TABLES_QUERY)        )

        if tables:

            print("\nTables found:")        print("Connecting to the SQL endpoint via ODBC (browser authentication will open)...")

            for schema, name in tables:        conn = pyodbc.connect(conn_str)

                print(f" - {schema}.{name}")

        else:        print("Connected. Querying external data sources...")

            print("\nNo tables found in the lakehouse.")        datasources = list_rows(conn, SQL_DATASOURCES_QUERY)

        if datasources:

    except Exception as e:            print("External data sources:")

        print("Error while querying the lakehouse:", file=sys.stderr)            for row in datasources:

        print(str(e), file=sys.stderr)                print(f" - {', '.join(str(x) for x in row)}")

        sys.exit(1)        else:

    finally:            print("No external data sources found or query returned no rows.")

        if conn:

            conn.close()        print("\nQuerying tables...")

        tables = list_rows(conn, SQL_TABLES_QUERY)

if __name__ == "__main__":        if tables:

    main()            print("Tables:")
            for schema, name in tables:
                print(f" - {schema}.{name}")
        else:
            print("No tables found or query returned no rows.")

    except Exception as e:
        print("Error while querying the lakehouse:", file=sys.stderr)
        print(str(e), file=sys.stderr)
        sys.exit(1)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()