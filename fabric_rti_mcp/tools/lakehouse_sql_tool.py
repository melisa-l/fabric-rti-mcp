
import os
import pyodbc

def lakehouse_sql_query(query: str):
    """Run SQL queries against Fabric Lakehouse using SQL endpoint."""
    sql_endpoint = os.getenv("FABRIC_SQL_ENDPOINT")
    database = os.getenv("FABRIC_LAKEHOUSE_NAME")

    print(f"Connecting to {database} at {sql_endpoint}")
    
    # Use direct interactive authentication
    conn_str = (
        f"Driver={{ODBC Driver 18 for SQL Server}};"
        f"Server={sql_endpoint};"
        f"Database={database};"
        "Authentication=ActiveDirectoryInteractive;"
        "Encrypt=yes;TrustServerCertificate=no"
    )
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return [tuple(row) for row in rows]