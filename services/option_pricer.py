import matplotlib.pyplot as plt
from models.monte_carlo_pricer import MonteCarloPricer
from models.black_scholes_pricer import BlackScholesPricer 
from data.market_data import MarketData 
from models.greek_calculator import GreekCalculator

class OptionPricer:
    def __init__(self, option, stock_data, num_simulations=10000):
        self.option = option
        self.stock_data = stock_data
        self.num_simulations = num_simulations
        self.monte_carlo_pricer = MonteCarloPricer(option, stock_data, num_simulations)
        self.black_scholes_pricer = BlackScholesPricer(option, stock_data)
        self.market_data = MarketData(option)
        self.greek_calculator = GreekCalculator(option, stock_data)

    def compare_prices(self):
        mc_price = self.monte_carlo_pricer.price()
        bs_price = self.black_scholes_pricer.price()
        market_price = self.market_data.get_market_price()
        
        delta, gamma, theta, vega, rho = self.greek_calculator.calculate_greeks()
        
        print(f"\nOption Pricing Analysis - {self.option.ticker}")
        print(f"Strike Price: {self.option.strike_price:.2f} $")
        print(f"Current Stock Price: {self.stock_data.current_price:.2f} $")
        print(f"Days to Maturity: {self.option.time_to_maturity*365:.0f}")
        
        print(f"\nPricing Results:")
        print(f"{'Method':<20} {'Price':>10}")
        print("-" * 30)
        
        if market_price is not None:
            print(f"{'Market':<15} ${market_price:>9.2f}")
            avg_model_price = (mc_price + bs_price) / 2
            if market_price > avg_model_price * 1.05:
                print("\nAnalysis: Option appears OVERVALUED in the market")
            elif market_price < avg_model_price * 0.95:
                print("\nAnalysis: Option appears UNDERVALUED in the market")
            else:
                print("\nAnalysis: Option appears FAIRLY PRICED in the market")
        
        print(f"{'Monte Carlo':<20} {mc_price:>9.2f} $")
        print(f"{'Black-Scholes':<20} {bs_price:>9.2f} $")
        
        print(f"\nGreeks:")
        print(f"{'Delta':<10} {delta:.4f}")
        print(f"{'Gamma':<10} {gamma:.4f}")
        print(f"{'Theta':<10} {theta:.4f}")
        print(f"{'Vega':<10} {vega:.4f}")
        print(f"{'Rho':<10} {rho:.4f}")
        
        self.plot_price_comparison(mc_price, bs_price, market_price)
        return mc_price, bs_price, market_price, delta, gamma, theta, vega, rho

    def plot_price_comparison(self, mc_price, bs_price, market_price):
        if market_price is not None:
            methods = ['Market Price', 'Monte Carlo', 'Black-Scholes']
            prices = [market_price, mc_price, bs_price]
        else:
            methods = ['Monte Carlo', 'Black-Scholes']
            prices = [mc_price, bs_price]
        
        plt.figure(figsize=(10, 6))
        bars = plt.bar(methods, prices)
        plt.title(f'Option Price Comparison - {self.option.ticker} Strike ${self.option.strike_price}')
        plt.ylabel('Option Price ($)')
        plt.grid(True, alpha=0.3)
        
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'${height:.2f}',
                    ha='center', va='bottom')
        plt.show()