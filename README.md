# Option Pricing Project

Ce projet permet de calculer le prix d'une option financière en utilisant trois méthodes principales : la simulation de Monte Carlo, la formule de Black-Scholes et un arbre binomial. Il inclut également une comparaison avec les prix du marché ainsi que le calcul des grecques (delta, gamma, theta, vega, rho).

Pour explorer la partie théorique, vous pouvez consulter le fichier [Report.ipynb](Report.ipynb).

## Méthodes de Pricing

- **Simulation de Monte Carlo** : Approche numérique utilisant des simulations pour estimer le prix de l'option.
- **Formule de Black-Scholes** : Calcul exact du prix d'une option européenne basé sur un modèle analytique.
- **Arbre Binomial** : Méthode discrète permettant d'estimer le prix d'une option en modélisant les évolutions de l'actif sous-jacent à chaque période.

## Optimisation des Performances

Le projet utilise **NumPy** pour les calculs numériques et **Numba** pour optimiser la simulation de Monte Carlo. **Numba** permet d'accélérer les calculs en compilant les fonctions Python en code machine, ce qui entraîne une réduction significative du temps d'exécution des simulations, en particulier pour des simulations avec un grand nombre de trajectoires.

### Estimation des gains de performance

Lors de l'implémentation initiale sans optimisation, le calcul pour 1 000 000 de simulations prenait environ **40 secondes**. Après l'optimisation avec **Numba**, le temps de calcul a été réduit à environ **10 secondes**.
Cette amélioration a un impact direct sur la vitesse de calcul des prix d'option, permettant d'effectuer des simulations avec une grande précision en un temps bien plus court, ce qui est essentiel pour des applications en temps réel ou des simulations nécessitant un grand nombre de répétitions.

## Résultats du Pricing

![Comparaison des méthodes de pricing](Img/Option%20Pricer%20Comparaison.png)

### Légende du graphique :
Le graphique ci-dessus montre une comparaison des prix des options obtenus à partir des trois méthodes de pricing : la simulation de Monte Carlo, la formule de Black-Scholes et l'arbre binomial. Le prix du marché est également représenté pour évaluer la précision des différentes méthodes.
