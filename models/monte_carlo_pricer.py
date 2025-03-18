import numpy as np
from numba import njit

# Fonction statique optimisée pour générer les marches aléatoires
@njit
def generate_random_walks(current_price, volatility, risk_free_rate, time_to_maturity, num_simulations):
    dt = time_to_maturity / 252  # Nombre de jours de trading par an
    num_steps = int(time_to_maturity * 252)  # Nombre de pas dans la simulation
    
    # Générer des variables aléatoires normales (simulations de l'évolution du prix)
    Z = np.random.standard_normal((num_simulations, num_steps))  
    paths = np.zeros((num_simulations, num_steps + 1))  # Matrice pour les trajectoires
    paths[:, 0] = current_price  # Initialiser les prix au temps t=0

    # Calcul des trajectoires
    drift = (risk_free_rate - 0.5 * volatility**2) * dt
    diffusion = volatility * np.sqrt(dt)

    print(f"Initial current price: {current_price}")
    print(f"Volatility: {volatility}, Risk-Free Rate: {risk_free_rate}, Time to Maturity: {time_to_maturity}")
    
    # Calcul de chaque marche aléatoire
    for t in range(1, num_steps + 1):
        paths[:, t] = paths[:, t-1] * np.exp(drift + diffusion * Z[:, t-1])
        if t % 100 == 0:  # Affiche un message tous les 100 pas
            print(f"Step {t}/{num_steps} completed")
    
    print(f"Generated paths for {num_simulations} simulations.")
    return paths

class MonteCarloPricer:
    def __init__(self, option, stock_data, num_simulations):
        self.option = option
        self.stock_data = stock_data
        self.num_simulations = num_simulations

    def price_call(self):
        # Pré-calculs des valeurs constantes
        current_price = self.stock_data.current_price
        volatility = self.stock_data.volatility
        risk_free_rate = self.option.risk_free_rate
        time_to_maturity = self.option.time_to_maturity
        
        # Appeler la méthode optimisée de simulation
        print(f"Pricing call option...")
        paths = generate_random_walks(current_price, volatility, risk_free_rate, time_to_maturity, self.num_simulations)
        
        # Calculer le payoff
        final_prices = paths[:, -1]
        payoffs = np.maximum(final_prices - self.option.strike_price, 0)
        
        # Vérification de la moyenne des payoffs
        print(f"Average payoff for call option: {np.mean(payoffs)}")
        
        # Retourner le prix actualisé de l'option Call
        call_price = np.exp(-risk_free_rate * time_to_maturity) * np.mean(payoffs)
        print(f"Call option price: {call_price}")
        return call_price

    def price_put(self):
        # Pré-calculs des valeurs constantes
        current_price = self.stock_data.current_price
        volatility = self.stock_data.volatility
        risk_free_rate = self.option.risk_free_rate
        time_to_maturity = self.option.time_to_maturity
        
        # Appeler la méthode optimisée de simulation
        print(f"Pricing put option...")
        paths = generate_random_walks(current_price, volatility, risk_free_rate, time_to_maturity, self.num_simulations)
        
        # Calculer le payoff
        final_prices = paths[:, -1]
        payoffs = np.maximum(self.option.strike_price - final_prices, 0)
        
        # Vérification de la moyenne des payoffs
        print(f"Average payoff for put option: {np.mean(payoffs)}")
        
        # Retourner le prix actualisé de l'option Put
        put_price = np.exp(-risk_free_rate * time_to_maturity) * np.mean(payoffs)
        print(f"Put option price: {put_price}")
        return put_price
