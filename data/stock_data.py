import yfinance as yf
import numpy as np

class StockData:
    def __init__(self, ticker):
        self.ticker = ticker
        self.stock = yf.Ticker(ticker)
        self.current_price = self.stock.history(period="1d")['Close'].iloc[-1]
        self.volatility = self.calculate_volatility()

    def calculate_volatility(self):
        historical_data = self.stock.history(period="1y")
        return np.sqrt(252) * historical_data['Close'].pct_change().std()