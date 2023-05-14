import numpy as np

def sim_eco_conditions(N):
    """
    two-step simulation to generate n samples of a market demand scenario based on economic conditions
    :param N: Number of samples
    :return: a list of market demand scenarios (strings)
    """

    # Define the probability distributions
    economic_probs = {'Good': 0.5, 'Moderate': 0.3, 'Poor': 0.2}

    # Step 1: Simulate economic conditions
    economic_conditions = np.random.choice(list(economic_probs.keys()), size=N, p=list(economic_probs.values()))

    return economic_conditions

def sim_demand_scenarios(economic_conditions, N):
    """
    two-step simulation to generate n samples of a market demand scenario based on economic conditions
    :param eco_conditions: a list of economic conditions (strings)
    :param N: Number of samples
    :return: a list of market demand scenarios (strings)
    """
    demand_probs = {
        'Good': {'High': 0.6, 'Medium': 0.3, 'Low': 0.1},
        'Moderate': {'High': 0.3, 'Medium': 0.5, 'Low': 0.2},
        'Poor': {'High': 0.1, 'Medium': 0.4, 'Low': 0.5}
    }

    # Step 2: Simulate market demand scenarios based on economic condition
    demand_probs_given_eco = np.array([demand_probs[condition] for condition in economic_conditions])
    demand_scenarios = np.array(
        [np.random.choice(list(demand_probs_given_eco[i].keys()), p=list(demand_probs_given_eco[i].values())) for i in
         range(N)])

    return demand_scenarios

if __name__ == "__main__":
    # Storing the simulated outcomes in a vector
    x = sim_eco_conditions(1000)
    y = sim_demand_scenarios(x, 1000)

