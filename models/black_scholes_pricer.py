import numpy as np
from scipy.stats import norm
import pandas as pd

class BlackScholesPricer:
    def __init__(self, option, stock_data):
        self.option = option
        self.stock_data = stock_data

    def price(self):
        d1 = (np.log(self.stock_data.current_price / self.option.strike_price) + 
              (self.option.risk_free_rate + 0.5 * self.stock_data.volatility**2) * self.option.time_to_maturity) / \
             (self.stock_data.volatility * np.sqrt(self.option.time_to_maturity))
        d2 = d1 - self.stock_data.volatility * np.sqrt(self.option.time_to_maturity)
        return self.stock_data.current_price * norm.cdf(d1) - \
               self.option.strike_price * np.exp(-self.option.risk_free_rate * self.option.time_to_maturity) * norm.cdf(d2)