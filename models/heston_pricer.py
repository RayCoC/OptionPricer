import numpy as np
import matplotlib.pyplot as plt

class HestonPricer:
    def __init__(self, option, stock_data, kappa, theta, xi, rho, v0):
        """
        Initialise le pricer Heston.

        :param option: L'option à pricer (classe Option).
        :param stock_data: Les données de l'actif sous-jacent (classe StockData).
        :param kappa: Vitesse de retour à la moyenne de la volatilité.
        :param theta: Niveau de long terme de la volatilité.
        :param xi: Volatilité de la volatilité (vol of vol).
        :param rho: Corrélation entre le prix de l'actif et sa volatilité.
        :param v0: Volatilité initiale.
        """
        self.option = option
        self.stock_data = stock_data
        self.kappa = kappa
        self.theta = theta
        self.xi = xi
        self.rho = rho
        self.v0 = v0

    def simulate_heston_paths(self, num_simulations, num_steps):
        """
        Simule des trajectoires de prix et de volatilité selon le modèle de Heston.

        :param num_simulations: Nombre de simulations.
        :param num_steps: Nombre de pas de temps.
        :return: Tuple (S, V) où S est un array de prix et V un array de volatilités.
        """
        S0 = self.stock_data.current_price
        r = self.option.risk_free_rate
        T = self.option.time_to_maturity
        dt = T / num_steps

        # Initialisation des arrays
        S = np.zeros((num_simulations, num_steps + 1))
        V = np.zeros((num_simulations, num_steps + 1))
        S[:, 0] = S0
        V[:, 0] = self.v0

        # Simulation des trajectoires
        for t in range(1, num_steps + 1):
            Z1 = np.random.standard_normal(num_simulations)
            Z2 = np.random.standard_normal(num_simulations)
            Z2 = self.rho * Z1 + np.sqrt(1 - self.rho**2) * Z2  # Corrélation entre S et V

            # Mise à jour de la volatilité
            V[:, t] = np.maximum(V[:, t-1] + self.kappa * (self.theta - V[:, t-1]) * dt + 
                       self.xi * np.sqrt(V[:, t-1]) * np.sqrt(dt) * Z2, 0)

            # Mise à jour du prix de l'actif
            S[:, t] = S[:, t-1] * np.exp(
                (r - 0.5 * V[:, t-1]) * dt + 
                np.sqrt(V[:, t-1]) * np.sqrt(dt) * Z1
            )

        return S, V

    def price_call(self, num_simulations=10000, num_steps=252):
        """
        Calcule le prix d'une option d'achat (call) en utilisant le modèle de Heston.
        """
        S, _ = self.simulate_heston_paths(num_simulations, num_steps)
        K = self.option.strike_price
        r = self.option.risk_free_rate
        T = self.option.time_to_maturity

        final_prices = S[:, -1]
        payoffs = np.maximum(final_prices - K, 0)
        return np.exp(-r * T) * np.mean(payoffs)

    def price_put(self, num_simulations=10000, num_steps=252):
        """
        Calcule le prix d'une option de vente (put) en utilisant le modèle de Heston.
        """
        S, _ = self.simulate_heston_paths(num_simulations, num_steps)
        K = self.option.strike_price
        r = self.option.risk_free_rate
        T = self.option.time_to_maturity

        final_prices = S[:, -1]
        payoffs = np.maximum(K - final_prices, 0)
        return np.exp(-r * T) * np.mean(payoffs)

    def plot_trajectories(self, num_simulations=10, num_steps=252):
        """
        Affiche des trajectoires simulées de prix et de volatilité.
        """
        S, V = self.simulate_heston_paths(num_simulations, num_steps)
        T = self.option.time_to_maturity
        time = np.linspace(0, T, num_steps + 1)

        plt.figure(figsize=(14, 6))

        # Graphique des trajectoires de prix
        plt.subplot(1, 2, 1)
        for i in range(num_simulations):
            plt.plot(time, S[i], lw=1)
        plt.title("Trajectoires de prix (Heston)")
        plt.xlabel("Temps (années)")
        plt.ylabel("Prix de l'actif ($)")
        plt.grid(True, alpha=0.3)

        # Graphique des trajectoires de volatilité
        plt.subplot(1, 2, 2)
        for i in range(num_simulations):
            plt.plot(time, V[i], lw=1)
        plt.title("Trajectoires de volatilité (Heston)")
        plt.xlabel("Temps (années)")
        plt.ylabel("Volatilité")
        plt.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.show()