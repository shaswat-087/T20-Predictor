
# 🏏 T20 Match Predictor

A Python-based tool to estimate **projected scores** and **winning probabilities** in T20 cricket matches (both **T20 Internationals** and **IPL**) using mathematical models, tier-based team strength, and Monte Carlo simulations.

---

## 📌 Features
- Supports **T20I** and **IPL** tournaments.
- Classifies teams into **tiers** based on relative strength.
- Calculates:
  - Current run rate
  - Projected score at the end of innings
  - Winning probability for batting and bowling teams
- Uses multiple projection methods:
  - Run rate extrapolation
  - Wickets-based scoring
  - Momentum from last 3 overs
  - Capacitor-like slowdown model when wickets fall
- Monte Carlo simulation for **close chase scenarios** (last overs).

---

## ⚙️ How It Works
1. **Select Innings**:  
   - `1` → First innings projection  
   - `2` → Second innings chase probability
2. **Provide Match Data**:
   - Batting team, Bowling team
   - Runs, Wickets, Overs (in format `Ovs.balls`)
   - Fall of wicket score (if applicable)
   - Ground average score
   - Last 3 overs performance (optional, improves accuracy)
3. **Output**:
   - Projected score at the end of innings
   - Winning probability (%) for both teams

---

## 🧮 Key Concepts
- **Tier System**: Teams grouped into Tier 1, 2, 3 based on strength.  
- **Chasing Factor (cf)**: Adjusts probability depending on team tiers.  
- **Projection Models**:
  - `pro1`: Current run rate extrapolation  
  - `pro2`: Wickets-based scoring potential  
  - `pro3`: Momentum from last 3 overs  
  - `pro4`: Slowdown model if wickets fall  
- **Monte Carlo Simulation**: Randomized ball-by-ball outcomes to estimate win probability in tight finishes.

---

## * Updated Feature *:
- Visualize win probabilities with a piechart using Matplotlib.


## 📂 Future Improvements
- Add live data integration (e.g., from CricAPI).

- Extend to ODI formats.

---

