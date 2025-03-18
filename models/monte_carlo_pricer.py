import numpy as np

class MonteCarloPricer:
    def __init__(self, option, stock_data, num_simulations=10000):
        self.option = option
        self.stock_data = stock_data
        self.num_simulations = num_simulations

    def generate_random_walks(self):
        dt = self.option.time_to_maturity / 252
        num_steps = max(1, int(self.option.time_to_maturity * 252))
        Z = np.random.standard_normal((self.num_simulations, num_steps))
        paths = np.zeros((self.num_simulations, num_steps + 1))
        paths[:, 0] = self.stock_data.current_price
        
        for t in range(1, num_steps + 1):
            paths[:, t] = paths[:, t-1] * np.exp(
                (self.option.risk_free_rate - 0.5 * self.stock_data.volatility**2) * dt + 
                self.stock_data.volatility * np.sqrt(dt) * Z[:, t-1]
            )
        return paths

    def price_call(self):
        paths = self.generate_random_walks()
        final_prices = paths[:, -1]
        payoffs = np.maximum(final_prices - self.option.strike_price, 0)
        return np.exp(-self.option.risk_free_rate * self.option.time_to_maturity) * np.mean(payoffs)

    def price_put(self):
        paths = self.generate_random_walks()
        final_prices = paths[:, -1]
        payoffs = np.maximum(self.option.strike_price - final_prices, 0)
        return np.exp(-self.option.risk_free_rate * self.option.time_to_maturity) * np.mean(payoffs)