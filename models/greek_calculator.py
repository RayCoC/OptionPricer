import numpy as np
import pandas as pd
from scipy.stats import norm

class GreekCalculator:
    def __init__(self, option, stock_data):
        self.option = option
        self.stock_data = stock_data

    def calculate_greeks(self):
        d1 = (np.log(self.stock_data.current_price / self.option.strike_price) + 
              (self.option.risk_free_rate + 0.5 * self.stock_data.volatility**2) * self.option.time_to_maturity) / \
             (self.stock_data.volatility * np.sqrt(self.option.time_to_maturity))
        d2 = d1 - self.stock_data.volatility * np.sqrt(self.option.time_to_maturity)

        delta = norm.cdf(d1)
        gamma = norm.pdf(d1) / (self.stock_data.current_price * self.stock_data.volatility * np.sqrt(self.option.time_to_maturity))
        theta = (-self.stock_data.current_price * norm.pdf(d1) * self.stock_data.volatility) / (2 * np.sqrt(self.option.time_to_maturity)) - \
                self.option.risk_free_rate * self.option.strike_price * np.exp(-self.option.risk_free_rate * self.option.time_to_maturity) * norm.cdf(d2)
        vega = self.stock_data.current_price * norm.pdf(d1) * np.sqrt(self.option.time_to_maturity)
        rho = self.option.strike_price * self.option.time_to_maturity * np.exp(-self.option.risk_free_rate * self.option.time_to_maturity) * norm.cdf(d2)

        return delta, gamma, theta, vega, rho