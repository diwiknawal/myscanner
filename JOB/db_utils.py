import sqlite3
import pandas as pd

class sqlHelper:
    def __init__(self, db_path):
        """Initialize the sqlHelper with a database path."""
        self.db_path = db_path
        self.conn = self.create_connection()
        self.cursor = self.conn.cursor()
        self.delete_table()
        

    def create_connection(self):
        """Create a connection to the SQLite database."""
        return sqlite3.connect(self.db_path)

    def delete_table(self):
        """Delete a table from the database."""
        self.cursor.execute(f"DROP TABLE IF EXISTS stock_data;")
        self.conn.commit()

    def create_table_for_stock(self, stock_ticker):
        """Create a table for storing stock data for a specific stock ticker."""
        table_name = stock_ticker.replace('.', '_')
        self.cursor.execute(f'''
       CREATE TABLE IF NOT EXISTS stock_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                open REAL,
                high REAL,
                low REAL,
                close REAL,
                volume INTEGER,
                ticker TEXT
            )
        ''')
        self.conn.commit()

    def insert_stock_data_for_stock(self, stock_data, stock_ticker):
        """Insert stock data into the table for a specific stock ticker."""
        table_name = stock_ticker.replace('.', '_')
        for index, row in stock_data.iterrows():
            date = index.strftime("%Y-%m-%d")
            open_price = round(float(row["Open"]),2)
            high_price = round(float(row["High"]),2)
            low_price = round(float(row["Low"]),2)
            close_price = round(float(row["Close"]),2)
            volume = int(row["Volume"])
        
            print(date, open_price, high_price, low_price, close_price, volume, table_name)
        
            self.cursor.execute("""
                INSERT INTO stock_data (date, open, high, low, close, volume, ticker)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (date, open_price, high_price, low_price, close_price, volume, table_name))
            
        self.conn.commit()
    