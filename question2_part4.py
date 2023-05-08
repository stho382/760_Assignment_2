import numpy
import numpy as np
from question1 import expected_utility
from question2 import sim_eco_conditions

profit_vals = np.array([[200000, 80000, -30000], [150000, 100000, 10000], [0, 0, 0]])

demand_probs = {
    'Good': np.array([0.6, 0.3, 0.1]),
    'Moderate':  np.array([0.3, 0.5, 0.2]),
    'Poor': np.array([0.1, 0.4, 0.5])
}

def compute_expec_utility(profit_vals, demand_probs):
    x = sim_eco_conditions(1000)
    y = {
        "Invest in A": list(),
        "Invest in B": list(),
        "Do not invest": list()
    }
    for sample in x:
        expec_util = expected_utility(profit_vals, demand_probs.get(sample))
        y.get("Invest in A").append(expec_util[0])
        y.get("Invest in B").append(expec_util[1])
        y.get("Do not invest").append(expec_util[2])

    return y

def determine_optimal_decision(expec_util):
    best_decision = max(max(expec_util.get("Invest in A")),  max(expec_util.get("Invest in B")), max(expec_util.get("Do not invest")))
    if best_decision == max(expec_util.get("Invest in A")):
        return "Invest in A"
    elif best_decision == max(expec_util.get("Invest in B")):
        return "Invest in B"
    else:
        return "Do not invest"

if __name__ == '__main__':
    x = compute_expec_utility(profit_vals, demand_probs)
    y = determine_optimal_decision(x)
    print(y)