import sqlite3
import re
from typing import Dict, Any, List

# SQL keywords that should be blocked for safety
DANGEROUS_KEYWORDS = [
    'DROP', 'DELETE', 'TRUNCATE', 'UPDATE', 'INSERT', 'ALTER', 
    'CREATE', 'REPLACE', 'ATTACH', 'DETACH'
]

def execute_sql_safely(sql_query: str) -> Dict[str, Any]:
    """
    Execute SQL query with safety checks
    """
    try:
        # Basic SQL injection protection
        sql_upper = sql_query.upper()
        for keyword in DANGEROUS_KEYWORDS:
            if keyword in sql_upper:
                return {
                    'results': [],
                    'columns': [],
                    'error': f"Dangerous SQL keyword '{keyword}' detected. Only SELECT queries are allowed."
                }
        
        # Connect to database
        conn = sqlite3.connect("db/database.db")
        conn.row_factory = sqlite3.Row  # Enable column access by name
        cursor = conn.cursor()
        
        # Execute query
        cursor.execute(sql_query)
        
        # Get results
        rows = cursor.fetchall()
        
        # Convert rows to dictionaries
        results = []
        columns = []
        
        if rows:
            columns = list(rows[0].keys())
            for row in rows:
                results.append(dict(row))
        
        conn.close()
        
        return {
            'results': results,
            'columns': columns,
            'error': None
        }
        
    except Exception as e:
        return {
            'results': [],
            'columns': [],
            'error': str(e)
        }

def get_database_schema() -> Dict[str, Any]:
    """
    Get complete database schema information
    """
    try:
        conn = sqlite3.connect("db/database.db")
        cursor = conn.cursor()
        
        # Get all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        
        schema = {'tables': {}}
        
        for table in tables:
            table_name = table[0]
            
            # Get columns for each table
            cursor.execute(f"PRAGMA table_info({table_name})")
            columns_info = cursor.fetchall()
            
            columns = {}
            for col in columns_info:
                columns[col[1]] = col[2]  # column_name: data_type
            
            # Get row count
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            row_count = cursor.fetchone()[0]
            
            schema['tables'][table_name] = {
                'columns': columns,
                'row_count': row_count
            }
        
        conn.close()
        
        return schema
        
    except Exception as e:
        return {'tables': {}, 'error': str(e)}