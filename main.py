from data.stock_data import StockData
from models.option import Option
from services.option_pricer import OptionPricer

if __name__ == "__main__":
    # Paramètres de l'option
    ticker = "AAPL"
    strike_price = 180
    risk_free_rate = 0.05
    num_simulations = 10000

    # Récupération des données de l'action
    stock_data = StockData(ticker)

    # Création de l'option
    option = Option(ticker, strike_price, None, risk_free_rate)

    # Initialisation du pricer
    pricer = OptionPricer(option, stock_data, num_simulations)

    # Comparaison des prix et calcul des grecques
    pricer.compare_prices()