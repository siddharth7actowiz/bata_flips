import mysql.connector
from config import *

def make_connection():
    return mysql.connector.connect(**DB_CONFIG)


def create_table(cursor,TABLE_NAME):
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS {TABLE_NAME}(
        id INT AUTO_INCREMENT PRIMARY KEY,
        Brand VARCHAR(255),
        Color VARCHAR(255),
        Size VARCHAR(50),
        Discount VARCHAR(255),
        Urls TEXT
       
    )
    """)


def insert_into_db( cursor, con,data):
    if not data:
        print("No data to insert.")
        return

    try:
        # Ensure consistent column order
        columns = ["Brand", "Color", "Size", "Discount", "Urls"]

        cols = ",".join(columns)
        vals = ",".join(["%s"] * len(columns))

        insert_query = f"""
        INSERT INTO `{TABLE_NAME}` ({cols})
        VALUES ({vals})
        ;
        """

        rows = [
            tuple(item[col] for col in columns)
            for item in data
        ]

        cursor.executemany(insert_query, rows)
        con.commit()

        print(f"{cursor.rowcount} rows inserted.")

    except Exception as e:
        # con.rollback()
        print("Error in insert_into_db:", e)