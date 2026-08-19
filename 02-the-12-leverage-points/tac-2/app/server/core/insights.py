import sqlite3
from typing import List, Optional, Dict, Any
from core.data_models import ColumnInsight

def generate_insights(table_name: str, column_names: Optional[List[str]] = None) -> List[ColumnInsight]:
    """
    Generate statistical insights for table columns
    """
    try:
        conn = sqlite3.connect("db/database.db")
        cursor = conn.cursor()
        
        # Get table schema
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns_info = cursor.fetchall()
        
        # If no specific columns requested, analyze all
        if not column_names:
            column_names = [col[1] for col in columns_info]
        
        insights = []
        
        for col_info in columns_info:
            col_name = col_info[1]
            col_type = col_info[2]
            
            if col_name not in column_names:
                continue
            
            # Basic statistics
            cursor.execute(f"SELECT COUNT(DISTINCT {col_name}) FROM {table_name}")
            unique_values = cursor.fetchone()[0]
            
            cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE {col_name} IS NULL")
            null_count = cursor.fetchone()[0]
            
            insight = ColumnInsight(
                column_name=col_name,
                data_type=col_type,
                unique_values=unique_values,
                null_count=null_count
            )
            
            # Type-specific insights
            if col_type in ['INTEGER', 'REAL', 'NUMERIC']:
                # Numeric insights
                cursor.execute(f"""
                    SELECT 
                        MIN({col_name}) as min_val,
                        MAX({col_name}) as max_val,
                        AVG({col_name}) as avg_val
                    FROM {table_name}
                    WHERE {col_name} IS NOT NULL
                """)
                result = cursor.fetchone()
                if result:
                    insight.min_value = result[0]
                    insight.max_value = result[1]
                    insight.avg_value = result[2]
            
            # Most common values (for all types)
            cursor.execute(f"""
                SELECT {col_name}, COUNT(*) as count
                FROM {table_name}
                WHERE {col_name} IS NOT NULL
                GROUP BY {col_name}
                ORDER BY count DESC
                LIMIT 5
            """)
            most_common = cursor.fetchall()
            if most_common:
                insight.most_common = [
                    {"value": val, "count": count} 
                    for val, count in most_common
                ]
            
            insights.append(insight)
        
        conn.close()
        return insights
        
    except Exception as e:
        raise Exception(f"Error generating insights: {str(e)}")