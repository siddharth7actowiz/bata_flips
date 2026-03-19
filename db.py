import mysql.connector
from config import *

def make_connection():
    return mysql.connector.connect(**DB_CONFIG)

def create_table(cursor):
    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {TABLE_NAME}(
        id INT AUTO_INCREMENT PRIMARY KEY,
        Urls TEXT
    
    )
    """)

def insert_into_db(cursor, con, data):

    if not data:
        return

    cols = "Urls"
    
    placeholders = "%s"

    query = f"INSERT INTO {TABLE_NAME} ({cols}) VALUES ({placeholders}) ON DUPLICATE KEY UPDATE id=id"

    values=[(url,)for url in data]

    try:
        cursor.executemany(query, values)
        con.commit()

    except Exception as e:
        con.rollback()
