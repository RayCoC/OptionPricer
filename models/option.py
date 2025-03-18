import numpy as np
import pandas as pd
import yfinance as yf
from scipy.stats import norm
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

class Option:
    def __init__(self, ticker, strike_price, maturity_date, risk_free_rate):
        self.ticker = ticker
        self.strike_price = strike_price
        self.maturity_date = self.validate_maturity_date(maturity_date)
        self.risk_free_rate = risk_free_rate
        self.time_to_maturity = self.calculate_time_to_maturity()

    def validate_maturity_date(self, maturity_date):
        if maturity_date is None:
            target_date = datetime.now() + timedelta(days=180)
        else:
            target_date = datetime.strptime(maturity_date, "%Y-%m-%d")
        
        expirations = yf.Ticker(self.ticker).options
        closest_date = min(expirations, key=lambda x: abs(datetime.strptime(x, "%Y-%m-%d") - target_date))
        return closest_date

    def calculate_time_to_maturity(self):
        maturity_datetime = datetime.strptime(self.maturity_date, "%Y-%m-%d")
        current_datetime = datetime.now()
        if maturity_datetime <= current_datetime:
            raise ValueError(f"Maturity date {self.maturity_date} must be in the future")
        return (maturity_datetime - current_datetime).days / 365.0