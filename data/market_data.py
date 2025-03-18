import yfinance as yf

class MarketData:
    def __init__(self, option):
        self.option = option

    def get_market_price(self, call=True):
        options = yf.Ticker(self.option.ticker).option_chain(self.option.maturity_date)
        if call:
            option_type = options.calls
        else:
            option_type = options.puts

        closest_strike_idx = (option_type['strike'] - self.option.strike_price).abs().idxmin()
        return option_type.iloc[closest_strike_idx]['lastPrice']