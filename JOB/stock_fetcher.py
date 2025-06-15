import yfinance as yf
from datetime import datetime, timedelta

def fetch_stock_data(stock_ticker, days=900):
    """Fetch stock data for the given ticker and date range."""
    end_date = datetime.today()
    start_date = end_date - timedelta(days=days)
    stock_data = yf.download(stock_ticker, start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))
    return stock_data