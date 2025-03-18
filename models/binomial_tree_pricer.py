import numpy as np


class BinomialTreePricer:

    def __init__(self, option, stock_data, num_steps=100):
        """
        Initialise le pricer d'options avec un arbre binomial.

        :param option: L'option à pricer (classe Option).
        :param stock_data: Les données de l'actif sous-jacent (classe StockData).
        :param num_steps: Nombre de pas de temps dans l'arbre binomial (par défaut 100).
        """
        self.option = option
        self.stock_data = stock_data
        self.num_steps = num_steps

    def calculate_tree_parameters(self):
        """
        Calcule les paramètres de l'arbre binomial : u, d, p.
        """
        T = self.option.time_to_maturity
        dt = T / self.num_steps
        sigma = self.stock_data.volatility
        r = self.option.risk_free_rate

        u = np.exp(sigma * np.sqrt(dt))  # Facteur de hausse
        d = 1 / u  # Facteur de baisse
        p = (np.exp(r * dt) - d) / (u - d)  # Probabilité risque-neutre

        return u, d, p
    
    def price_call(self):
        """
        Calcule le prix d'une option d'achat (call) en utilisant un arbre binomial.
        """
        u, d, p = self.calculate_tree_parameters()
        S0 = self.stock_data.current_price
        K = self.option.strike_price
        T = self.option.time_to_maturity
        r = self.option.risk_free_rate
        dt = T / self.num_steps

        # Calcul des prix à l'échéance
        prices_at_maturity = S0 * (u ** np.arange(self.num_steps, -1, -1)) * (d ** np.arange(0, self.num_steps + 1))
        payoffs = np.maximum(prices_at_maturity - K, 0)

        # Calcul du prix de l'option en remontant l'arbre
        for step in range(self.num_steps, 0, -1):
            payoffs = np.exp(-r * dt) * (p * payoffs[:-1] + (1 - p) * payoffs[1:])
        return payoffs[0]

    def price_put(self):
        """
        Calcule le prix d'une option de vente (put) en utilisant un arbre binomial.
        """
        u, d, p = self.calculate_tree_parameters()
        S0 = self.stock_data.current_price
        K = self.option.strike_price
        T = self.option.time_to_maturity
        r = self.option.risk_free_rate
        dt = T / self.num_steps

        # Calcul des prix à l'échéance
        prices_at_maturity = S0 * (u ** np.arange(self.num_steps, -1, -1)) * (d ** np.arange(0, self.num_steps + 1))
        payoffs = np.maximum(K - prices_at_maturity, 0)

        # Calcul du prix de l'option en remontant l'arbre
        for step in range(self.num_steps, 0, -1):
            payoffs = np.exp(-r * dt) * (p * payoffs[:-1] + (1 - p) * payoffs[1:])

        return payoffs[0]