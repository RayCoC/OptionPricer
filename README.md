# Option Pricing Project

Ce projet permet de calculer le prix d'une option financière en utilisant deux méthodes principales : la simulation de Monte Carlo et la formule de Black-Scholes. Il inclut également une comparaison avec les prix du marché et le calcul des grecques (delta, gamma, theta, vega, rho).

---

## Table des matières

1. [Fonctionnalités](#fonctionnalités)
2. [Théorie et calculs](#théorie-et-calculs)
   - [Modèle de Black-Scholes](#modèle-de-black-scholes)
   - [Simulation de Monte Carlo](#simulation-de-monte-carlo)
   - [Calcul des grecques](#calcul-des-grecques)
3. [Utilisation](#utilisation)

---

## Fonctionnalités

- **Pricing d'options** :
  - Simulation de Monte Carlo.
  - Formule de Black-Scholes.
- **Comparaison avec les prix du marché**.
- **Calcul des grecques** :
  - Delta, Gamma, Theta, Vega, Rho.
- **Visualisation des résultats** :
  - Graphique comparant les prix calculés et le prix du marché.

---

## Théorie et calculs

### Modèle de Black-Scholes

Le modèle de Black-Scholes est une méthode analytique pour calculer le prix d'une option européenne. La formule pour le prix d'une option d'achat (call) est :

$$
C = S_0 N(d_1) - K e^{-rT} N(d_2)
$$

Où :
- $C$ : Prix de l'option d'achat.
- $S_0$ : Prix actuel de l'actif sous-jacent.
- $K$ : Prix d'exercice de l'option.
- $r$ : Taux d'intérêt sans risque.
- $T$ : Temps jusqu'à l'expiration de l'option.
- $N(\cdot)$ : Fonction de répartition de la loi normale centrée réduite.
- $d_1$ et $d_2$ sont donnés par :

$$
d_1 = \frac{\ln(S_0 / K) + (r + \sigma^2 / 2) T}{\sigma \sqrt{T}}
$$
$$
d_2 = d_1 - \sigma \sqrt{T}
$$

Où $\sigma$ est la volatilité de l'actif sous-jacent.

---

### Simulation de Monte Carlo

La simulation de Monte Carlo est une méthode numérique pour estimer le prix d'une option en simulant des trajectoires possibles du prix de l'actif sous-jacent. Les étapes sont les suivantes :

1. **Simuler des trajectoires** :
   - Le prix de l'actif suit un mouvement brownien géométrique :
     $$
     S_t = S_0 \exp\left( \left(r - \frac{\sigma^2}{2}\right) t + \sigma \sqrt{t} Z \right)
     $$
     Où $Z$ est une variable aléatoire normale standard.

2. **Calculer le payoff** :
   - Pour chaque trajectoire, calculer le payoff de l'option à l'expiration :
     $$
     \text{Payoff} = \max(S_T - K, 0)
     $$

3. **Moyenne des payoffs** :
   - Le prix de l'option est la moyenne des payoffs actualisés :
     $$
     C = e^{-rT} \cdot \frac{1}{N} \sum_{i=1}^N \text{Payoff}_i
     $$

---

### Calcul des grecques

Les grecques mesurent la sensibilité du prix de l'option à différents facteurs. Voici les formules utilisées dans ce projet :

- **Delta** :
  $$
  \Delta = N(d_1)
  $$
  Mesure la sensibilité du prix de l'option par rapport au prix de l'actif sous-jacent.

- **Gamma** :
  $$
  \Gamma = \frac{N'(d_1)}{S_0 \sigma \sqrt{T}}
  $$
  Mesure la sensibilité du delta par rapport au prix de l'actif sous-jacent.

- **Theta** :
  $$
  \Theta = -\frac{S_0 N'(d_1) \sigma}{2 \sqrt{T}} - r K e^{-rT} N(d_2)
  $$
  Mesure la sensibilité du prix de l'option par rapport au temps.

- **Vega** :
  $$
  \text{Vega} = S_0 N'(d_1) \sqrt{T}
  $$
  Mesure la sensibilité du prix de l'option par rapport à la volatilité.

- **Rho** :
  $$
  \rho = K T e^{-rT} N(d_2)
  $$
  Mesure la sensibilité du prix de l'option par rapport au taux d'intérêt.

---

## Utilisation

Exécutez le programme principal :
```bash
python src/main.py
# Option Pricing Project

Ce projet permet de calculer le prix d'une option financière en utilisant deux méthodes principales : la simulation de Monte Carlo et la formule de Black-Scholes. Il inclut également une comparaison avec les prix du marché et le calcul des grecques (delta, gamma, theta, vega, rho).

---

## Table des matières

1. [Fonctionnalités](#fonctionnalités)
2. [Théorie et calculs](#théorie-et-calculs)
   - [Modèle de Black-Scholes](#modèle-de-black-scholes)
   - [Simulation de Monte Carlo](#simulation-de-monte-carlo)
   - [Calcul des grecques](#calcul-des-grecques)
3. [Utilisation](#utilisation)

---

## Fonctionnalités

- **Pricing d'options** :
  - Simulation de Monte Carlo.
  - Formule de Black-Scholes.
- **Comparaison avec les prix du marché**.
- **Calcul des grecques** :
  - Delta, Gamma, Theta, Vega, Rho.
- **Visualisation des résultats** :
  - Graphique comparant les prix calculés et le prix du marché.

---

## Théorie et calculs

### Modèle de Black-Scholes

Le modèle de Black-Scholes est une méthode analytique pour calculer le prix d'une option européenne. La formule pour le prix d'une option d'achat (call) est :

$$
C = S_0 N(d_1) - K e^{-rT} N(d_2)
$$

Où :
- $C$ : Prix de l'option d'achat.
- $S_0$ : Prix actuel de l'actif sous-jacent.
- $K$ : Prix d'exercice de l'option.
- $r$ : Taux d'intérêt sans risque.
- $T$ : Temps jusqu'à l'expiration de l'option.
- $N(\cdot)$ : Fonction de répartition de la loi normale centrée réduite.
- $d_1$ et $d_2$ sont donnés par :

$$
d_1 = \frac{\ln(S_0 / K) + (r + \sigma^2 / 2) T}{\sigma \sqrt{T}}
$$
$$
d_2 = d_1 - \sigma \sqrt{T}
$$

Où $\sigma$ est la volatilité de l'actif sous-jacent.

---

### Simulation de Monte Carlo

La simulation de Monte Carlo est une méthode numérique pour estimer le prix d'une option en simulant des trajectoires possibles du prix de l'actif sous-jacent. Les étapes sont les suivantes :

1. **Simuler des trajectoires** :
   - Le prix de l'actif suit un mouvement brownien géométrique :
     $$
     S_t = S_0 \exp\left( \left(r - \frac{\sigma^2}{2}\right) t + \sigma \sqrt{t} Z \right)
     $$
     Où $Z$ est une variable aléatoire normale standard.

2. **Calculer le payoff** :
   - Pour chaque trajectoire, calculer le payoff de l'option à l'expiration :
     $$
     \text{Payoff} = \max(S_T - K, 0)
     $$

3. **Moyenne des payoffs** :
   - Le prix de l'option est la moyenne des payoffs actualisés :
     $$
     C = e^{-rT} \cdot \frac{1}{N} \sum_{i=1}^N \text{Payoff}_i
     $$

---

### Calcul des grecques

Les grecques mesurent la sensibilité du prix de l'option à différents facteurs. Voici les formules utilisées dans ce projet :

- **Delta** :
  $$
  \Delta = N(d_1)
  $$
  Mesure la sensibilité du prix de l'option par rapport au prix de l'actif sous-jacent.

- **Gamma** :
  $$
  \Gamma = \frac{N'(d_1)}{S_0 \sigma \sqrt{T}}
  $$
  Mesure la sensibilité du delta par rapport au prix de l'actif sous-jacent.

- **Theta** :
  $$
  \Theta = -\frac{S_0 N'(d_1) \sigma}{2 \sqrt{T}} - r K e^{-rT} N(d_2)
  $$
  Mesure la sensibilité du prix de l'option par rapport au temps.

- **Vega** :
  $$
  \text{Vega} = S_0 N'(d_1) \sqrt{T}
  $$
  Mesure la sensibilité du prix de l'option par rapport à la volatilité.

- **Rho** :
  $$
  \rho = K T e^{-rT} N(d_2)
  $$
  Mesure la sensibilité du prix de l'option par rapport au taux d'intérêt.

---

## Utilisation

Exécutez le programme principal :
```bash
python src/main.py
