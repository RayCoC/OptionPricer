# Option Pricing Project

Ce projet permet de calculer le prix d'une option financière en utilisant trois méthodes principales : la simulation de Monte Carlo, la formule de Black-Scholes et un arbre binomial. Il inclut également une comparaison avec les prix du marché ainsi que le calcul des grecques (delta, gamma, theta, vega, rho).

Pour explorer la partie théorique, vous pouvez consulter le fichier [Report.ipynb](Report.ipynb).

## Méthodes de Pricing

- **Simulation de Monte Carlo** : Approche numérique utilisant des simulations pour estimer le prix de l'option.
- **Formule de Black-Scholes** : Calcul exact du prix d'une option européenne basé sur un modèle analytique.
- **Arbre Binomial** : Méthode discrète permettant d'estimer le prix d'une option en modélisant les évolutions de l'actif sous-jacent à chaque période.

## Résultats du Pricing (1k simulations MC et Arbre Binomial)

![Comparaison des méthodes de pricing](Img/Option%20Pricer%20Comparaison.png)

### Légende du graphique :
Le graphique ci-dessus montre une comparaison des prix des options obtenus à partir des trois méthodes de pricing : la simulation de Monte Carlo, la formule de Black-Scholes et l'arbre binomial, en utilisant 1000 simulations pour Monte Carlo. Le prix du marché est également représenté pour évaluer la précision des différentes méthodes.
