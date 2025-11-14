"""
Lakehouse SQL tools for querying and exploring Fabric Lakehouse data.
"""

import os
from typing import List, Tuple
import pyodbc


def _get_connection():
    """Get a connection to the lakehouse SQL endpoint."""
    sql_endpoint = os.getenv("FABRIC_SQL_ENDPOINT")
    database = os.getenv("FABRIC_LAKEHOUSE_NAME")
    
    if not sql_endpoint or not database:
        raise ValueError("FABRIC_SQL_ENDPOINT and FABRIC_LAKEHOUSE_NAME must be set")
    
    conn_str = (
        f"Driver={{ODBC Driver 18 for SQL Server}};"
        f"Server={sql_endpoint};"
        f"Database={database};"
        "Authentication=ActiveDirectoryInteractive;"
        "Encrypt=yes;TrustServerCertificate=no"
    )
    return pyodbc.connect(conn_str)


def lakehouse_sql_query(query: str) -> List[Tuple]:
    """
    Execute a SQL query against Fabric Lakehouse using the SQL endpoint.
    
    Args:
        query: T-SQL query to execute
        
    Returns:
        List of tuples containing query results
    """
    conn = _get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        return [tuple(row) for row in cursor.fetchall()]
    finally:
        conn.close()


def lakehouse_list_tables() -> List[Tuple[str, str, int]]:
    """
    List all tables in the lakehouse with their schemas and row counts.
    
    Returns:
        List of tuples: (schema_name, table_name, row_count)
    """
    query = """
        SELECT 
            s.name AS schema_name,
            t.name AS table_name,
            SUM(p.rows) AS row_count
        FROM sys.tables t
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        INNER JOIN sys.partitions p ON t.object_id = p.object_id
        WHERE p.index_id IN (0, 1)  -- heap or clustered index
        GROUP BY s.name, t.name
        ORDER BY s.name, t.name
    """
    return lakehouse_sql_query(query)


def lakehouse_describe_table(schema_name: str, table_name: str) -> List[Tuple]:
    """
    Get detailed schema information for a specific table.
    
    Args:
        schema_name: Name of the schema
        table_name: Name of the table
        
    Returns:
        List of tuples with column information: 
        (column_name, data_type, max_length, precision, scale, is_nullable, is_identity)
    """
    query = """
        SELECT 
            c.COLUMN_NAME,
            c.DATA_TYPE,
            c.CHARACTER_MAXIMUM_LENGTH,
            c.NUMERIC_PRECISION,
            c.NUMERIC_SCALE,
            c.IS_NULLABLE,
            COLUMNPROPERTY(OBJECT_ID(c.TABLE_SCHEMA + '.' + c.TABLE_NAME), c.COLUMN_NAME, 'IsIdentity') as IS_IDENTITY
        FROM INFORMATION_SCHEMA.COLUMNS c
        WHERE c.TABLE_SCHEMA = ? AND c.TABLE_NAME = ?
        ORDER BY c.ORDINAL_POSITION
    """
    conn = _get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(query, (schema_name, table_name))
        return [tuple(row) for row in cursor.fetchall()]
    finally:
        conn.close()


def lakehouse_sample_table(schema_name: str, table_name: str, limit: int = 10) -> List[Tuple]:
    """
    Get sample rows from a table to preview the data.
    
    Args:
        schema_name: Name of the schema
        table_name: Name of the table
        limit: Number of rows to return (default: 10, max: 1000)
        
    Returns:
        List of tuples containing sample data rows
    """
    # Limit to reasonable max to avoid memory issues
    limit = min(limit, 1000)
    
    query = f"""
        SELECT TOP {limit} *
        FROM [{schema_name}].[{table_name}]
    """
    return lakehouse_sql_query(query)


def lakehouse_find_relationships() -> List[Tuple[str, str, str, str, str, str]]:
    """
    Find foreign key relationships between tables in the lakehouse.
    This is useful for understanding the semantic model structure and how tables relate to each other.
    
    Note: Many lakehouses don't have formal FK constraints defined. If this returns empty,
    use lakehouse_find_potential_relationships() to discover relationships by naming patterns.
    
    Returns:
        List of tuples with relationship information:
        (parent_schema, parent_table, parent_column, child_schema, child_table, child_column)
    """
    query = """
        SELECT 
            OBJECT_SCHEMA_NAME(fk.referenced_object_id) AS parent_schema,
            OBJECT_NAME(fk.referenced_object_id) AS parent_table,
            COL_NAME(fk.referenced_object_id, fkc.referenced_column_id) AS parent_column,
            OBJECT_SCHEMA_NAME(fk.parent_object_id) AS child_schema,
            OBJECT_NAME(fk.parent_object_id) AS child_table,
            COL_NAME(fk.parent_object_id, fkc.parent_column_id) AS child_column
        FROM sys.foreign_keys AS fk
        INNER JOIN sys.foreign_key_columns AS fkc 
            ON fk.object_id = fkc.constraint_object_id
        ORDER BY parent_schema, parent_table, child_schema, child_table
    """
    return lakehouse_sql_query(query)


def lakehouse_find_potential_relationships() -> List[Tuple[str, str, str, str, str]]:
    """
    Find potential relationships between tables based on column naming patterns.
    This is useful when formal foreign keys aren't defined (common in lakehouses).
    
    Looks for columns that end with common suffixes like: Id, ID, Key, Ref, Code, etc.
    and match between tables.
    
    Returns:
        List of tuples: (table1_schema, table1_name, table2_schema, table2_name, matching_column)
    """
    query = """
        WITH ColumnNames AS (
            SELECT 
                s.name AS schema_name,
                t.name AS table_name,
                c.name AS column_name
            FROM sys.tables t
            INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
            INNER JOIN sys.columns c ON t.object_id = c.object_id
            WHERE c.name LIKE '%Id' 
               OR c.name LIKE '%ID' 
               OR c.name LIKE '%Key'
               OR c.name LIKE '%Code'
               OR c.name LIKE '%Ref'
        )
        SELECT DISTINCT
            c1.schema_name AS table1_schema,
            c1.table_name AS table1_name,
            c2.schema_name AS table2_schema,
            c2.table_name AS table2_name,
            c1.column_name AS matching_column
        FROM ColumnNames c1
        INNER JOIN ColumnNames c2 
            ON c1.column_name = c2.column_name
            AND (c1.schema_name != c2.schema_name OR c1.table_name != c2.table_name)
        WHERE c1.table_name < c2.table_name  -- Avoid duplicates
        ORDER BY c1.schema_name, c1.table_name, c2.schema_name, c2.table_name
    """
    return lakehouse_sql_query(query)


def lakehouse_find_primary_keys() -> List[Tuple[str, str, str, int]]:
    """
    Find all primary key columns across all tables.
    Useful for understanding unique identifiers in the semantic model.
    
    Returns:
        List of tuples: (schema_name, table_name, column_name, ordinal_position)
    """
    query = """
        SELECT 
            s.name AS schema_name,
            t.name AS table_name,
            c.name AS column_name,
            ic.key_ordinal AS ordinal_position
        FROM sys.indexes i
        INNER JOIN sys.index_columns ic 
            ON i.object_id = ic.object_id AND i.index_id = ic.index_id
        INNER JOIN sys.columns c 
            ON ic.object_id = c.object_id AND ic.column_id = c.column_id
        INNER JOIN sys.tables t 
            ON i.object_id = t.object_id
        INNER JOIN sys.schemas s 
            ON t.schema_id = s.schema_id
        WHERE i.is_primary_key = 1
        ORDER BY s.name, t.name, ic.key_ordinal
    """
    return lakehouse_sql_query(query)