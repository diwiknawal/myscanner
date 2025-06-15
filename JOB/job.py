from stock_fetcher import fetch_stock_data
from db_utils import sqlHelper


# Define constants
DB_PATH = './DB/KA03SCANNER.db'
stock_tickers = ["RELIANCE.NS", "TCS.NS", "INFY.NS"]  # Add more tickers as needed

def main():
    sql_helper = sqlHelper(DB_PATH) 
    # Connect to the database
    #conn = sqlHelper.create_connection(DB_PATH)

    # Fetch and store data for each stock ticker
    for stock_ticker in stock_tickers:
        # Create a table for the stock ticker
        sql_helper.create_table_for_stock( stock_ticker)

        # Fetch stock data
        stock_data = fetch_stock_data(stock_ticker)
        print(stock_data)

        # Insert stock data into the table for the stock ticker
        sql_helper.insert_stock_data_for_stock( stock_data, stock_ticker)

    # Close the connection
    

    print("Stock data for all tickers has been stored in separate tables in the SQLite database.")

if __name__ == "__main__":
    main()