import matplotlib.pyplot as plt
from models.monte_carlo_pricer import MonteCarloPricer
from models.black_scholes_pricer import BlackScholesPricer
from data.market_data import MarketData
from models.greek_calculator import GreekCalculator

class OptionPricer:
    def __init__(self, option, stock_data, num_simulations=10000):
        """
        Initialise le pricer d'options.

        :param option: L'option à pricer (classe Option).
        :param stock_data: Les données de l'actif sous-jacent (classe StockData).
        :param num_simulations: Nombre de simulations pour la méthode Monte Carlo (par défaut 10 000).
        """
        self.option = option
        self.stock_data = stock_data
        self.num_simulations = num_simulations
        self.monte_carlo_pricer = MonteCarloPricer(option, stock_data, num_simulations)
        self.black_scholes_pricer = BlackScholesPricer(option, stock_data)
        self.market_data = MarketData(option)
        self.greek_calculator = GreekCalculator(option, stock_data)

    def compare_prices(self):
        """
        Compare les prix des options (call et put) calculés par Monte Carlo, Black-Scholes et le marché.
        Affiche également les grecques.
        """
        # Calcul des prix pour les calls
        mc_call_price = self.monte_carlo_pricer.price_call()
        bs_call_price = self.black_scholes_pricer.price_call()
        market_call_price = self.market_data.get_market_price(call=True)

        # Calcul des prix pour les puts
        mc_put_price = self.monte_carlo_pricer.price_put()
        bs_put_price = self.black_scholes_pricer.price_put()
        market_put_price = self.market_data.get_market_price(call=False)

        # Calcul des grecques
        delta, gamma, theta, vega, rho = self.greek_calculator.calculate_greeks()

        # Affichage des résultats
        print(f"\nOption Pricing Analysis - {self.option.ticker}")
        print(f"Strike Price: {self.option.strike_price:.2f} $")
        print(f"Current Stock Price: {self.stock_data.current_price:.2f} $")
        print(f"Days to Maturity: {self.option.time_to_maturity * 365:.0f}")

        # Résultats pour les calls
        print(f"\nPricing Results for Calls:")
        print(f"{'Method':<20} {'Price':>10}")
        print("-" * 30)
        if market_call_price is not None:
            print(f"{'Market':<15} ${market_call_price:>9.2f}")
        print(f"{'Monte Carlo':<20} {mc_call_price:>9.2f} $")
        print(f"{'Black-Scholes':<20} {bs_call_price:>9.2f} $")

        # Résultats pour les puts
        print(f"\nPricing Results for Puts:")
        print(f"{'Method':<20} {'Price':>10}")
        print("-" * 30)
        if market_put_price is not None:
            print(f"{'Market':<15} ${market_put_price:>9.2f}")
        print(f"{'Monte Carlo':<20} {mc_put_price:>9.2f} $")
        print(f"{'Black-Scholes':<20} {bs_put_price:>9.2f} $")

        # Affichage des grecques
        print(f"\nGreeks:")
        print(f"{'Delta':<10} {delta:.4f}")
        print(f"{'Gamma':<10} {gamma:.4f}")
        print(f"{'Theta':<10} {theta:.4f}")
        print(f"{'Vega':<10} {vega:.4f}")
        print(f"{'Rho':<10} {rho:.4f}")

        # Visualisation des résultats
        self.plot_price_comparison(mc_call_price, bs_call_price, market_call_price, mc_put_price, bs_put_price, market_put_price)

    def plot_price_comparison(self, mc_call_price, bs_call_price, market_call_price, mc_put_price, bs_put_price, market_put_price):
        """
        Affiche un graphique comparant les prix des options (call et put) calculés par Monte Carlo, Black-Scholes et le marché.

        :param mc_call_price: Prix du call calculé par Monte Carlo.
        :param bs_call_price: Prix du call calculé par Black-Scholes.
        :param market_call_price: Prix du call sur le marché.
        :param mc_put_price: Prix du put calculé par Monte Carlo.
        :param bs_put_price: Prix du put calculé par Black-Scholes.
        :param market_put_price: Prix du put sur le marché.
        """
        # Données pour les calls
        call_methods = ['Monte Carlo', 'Black-Scholes']
        call_prices = [mc_call_price, bs_call_price]
        if market_call_price is not None:
            call_methods.insert(0, 'Market')
            call_prices.insert(0, market_call_price)

        # Données pour les puts
        put_methods = ['Monte Carlo', 'Black-Scholes']
        put_prices = [mc_put_price, bs_put_price]
        if market_put_price is not None:
            put_methods.insert(0, 'Market')
            put_prices.insert(0, market_put_price)

        # Création du graphique
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

        # Graphique pour les calls
        bars1 = ax1.bar(call_methods, call_prices)
        ax1.set_title(f'Call Option Price Comparison - {self.option.ticker} Strike ${self.option.strike_price}')
        ax1.set_ylabel('Option Price ($)')
        ax1.grid(True, alpha=0.3)
        for bar in bars1:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width() / 2, height, f'${height:.2f}', ha='center', va='bottom')

        # Graphique pour les puts
        bars2 = ax2.bar(put_methods, put_prices)
        ax2.set_title(f'Put Option Price Comparison - {self.option.ticker} Strike ${self.option.strike_price}')
        ax2.set_ylabel('Option Price ($)')
        ax2.grid(True, alpha=0.3)
        for bar in bars2:
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width() / 2, height, f'${height:.2f}', ha='center', va='bottom')

        plt.tight_layout()
        plt.show()