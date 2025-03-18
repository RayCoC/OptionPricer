import yfinance as yf

class MarketData:
    def __init__(self, option):
        self.option = option

    def get_market_price(self):
        options = yf.Ticker(self.option.ticker).option_chain(self.option.maturity_date)
        calls = options.calls
        closest_strike_idx = (calls['strike'] - self.option.strike_price).abs().idxmin()
        return calls.iloc[closest_strike_idx]['lastPrice']