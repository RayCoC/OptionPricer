import numpy as np
from scipy.stats import norm
import pandas as pd
from scipy.stats import norm

class BlackScholesPricer:
    def __init__(self, option, stock_data):
        self.option = option
        self.stock_data = stock_data

    def calculate_d1_d2(self):
        S0 = self.stock_data.current_price
        K = self.option.strike_price
        r = self.option.risk_free_rate
        T = self.option.time_to_maturity
        sigma = self.stock_data.volatility

        d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)
        return d1, d2

    def price_call(self):
        d1, d2 = self.calculate_d1_d2()
        S0 = self.stock_data.current_price
        K = self.option.strike_price
        r = self.option.risk_free_rate
        T = self.option.time_to_maturity

        call_price = S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
        return call_price

    def price_put(self):
        d1, d2 = self.calculate_d1_d2()
        S0 = self.stock_data.current_price
        K = self.option.strike_price
        r = self.option.risk_free_rate
        T = self.option.time_to_maturity

        put_price = K * np.exp(-r * T) * norm.cdf(-d2) - S0 * norm.cdf(-d1)
        return put_price