
import os
import pyodbc
from azure.identity import AzureCliCredential

def lakehouse_sql_query(query: str):
    """Run SQL queries against Fabric Lakehouse using SQL endpoint."""
    sql_endpoint = os.getenv("FABRIC_SQL_ENDPOINT")
    database = os.getenv("FABRIC_LAKEHOUSE_NAME")

    credential = AzureCliCredential()
    token = credential.get_token("https://database.windows.net/.default").token

    conn_str = f"Driver={{ODBC Driver 18 for SQL Server}};Server=tcp:{sql_endpoint},1433;Database={database};Encrypt=yes;TrustServerCertificate=no;Authentication=ActiveDirectoryAccessToken"
    conn = pyodbc.connect(conn_str, attrs_before={1256: token})
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return [tuple(row) for row in rows]
