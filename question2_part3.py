import numpy as np
import matplotlib.pyplot as plt
from question1 import expected_utility

def sim_eco_conditions(N):
    """
    Simulate the economic conditions for N samples and return the appropriate
    cumulative emperical proportions.
    :param N: number of samples
    :return:
        high_demand_cum_freqs: array containing the emperical proportions for
                               high market demand
        medium_demand_cum_freqs: array containing the emperical proportions for
                                 medium market demand
        low_demand_cum_freqs: array containing the emperical proportions for
                              low market demand
    """
    # Define the probability distributions
    economic_probs = {'Good': 0.5, 'Moderate': 0.3, 'Poor': 0.2}

    demand_probs = {
        'Good': {'High': 0.6, 'Medium': 0.3, 'Low': 0.1},
        'Moderate': {'High': 0.3, 'Medium': 0.5, 'Low': 0.2},
        'Poor': {'High': 0.1, 'Medium': 0.4, 'Low': 0.5}
    }

    # Step 1: Simulate economic conditions
    economic_conditions = np.random.choice(list(economic_probs.keys()),
                                           size=N, p=list(economic_probs.values()))

    # Step 2: Simulate market demand scenarios based on economic condition
    demand_probs_given_eco = np.array([demand_probs[condition]
                                       for condition in economic_conditions])
    demand_scenarios = np.array(
        [np.random.choice(list(demand_probs_given_eco[a].keys()),
                          p=list(demand_probs_given_eco[a].values())) for a in
         range(N)])

    # Initialize counters for each market demand outcome
    demand_counters = {'High': 0, 'Medium': 0, 'Low': 0}

    # Initialize arrays to store the cumulative empirical frequencies for each outcome
    high_demand_cum_freqs = np.zeros(N)
    medium_demand_cum_freqs = np.zeros(N)
    low_demand_cum_freqs = np.zeros(N)

    # Update the counters and compute the empirical frequencies for each outcome
    for i in range(1, N+1):
        demand_counters['High'] += np.sum(demand_scenarios[:i] == 'High')
        demand_counters['Medium'] += np.sum(demand_scenarios[:i] == 'Medium')
        demand_counters['Low'] += np.sum(demand_scenarios[:i] == 'Low')

        # demand_sum = np.sum(demand_scenarios[:i] == 'High') + np.sum(demand_scenarios[:i] == 'Medium') \
        #              + np.sum(demand_scenarios[:i] == 'Low')


        high_demand_emp_freq = demand_counters['High'] / \
                               sum(demand_counters.values())
        medium_demand_emp_freq = demand_counters['Medium'] / \
                                 sum(demand_counters.values())
        low_demand_emp_freq = demand_counters['Low'] / \
                              sum(demand_counters.values())

        # Update the cumulative empirical frequencies
        high_demand_cum_freqs[i - 1] = high_demand_emp_freq
        medium_demand_cum_freqs[i - 1] = medium_demand_emp_freq
        low_demand_cum_freqs[i - 1] = low_demand_emp_freq

    # Plot the cumulative empirical frequencies
    x = np.arange(1, N+1)
    plt.plot(x, high_demand_cum_freqs, label='High Demand')
    plt.plot(x, medium_demand_cum_freqs, label='Medium Demand')
    plt.plot(x, low_demand_cum_freqs, label='Low Demand')
    plt.legend()
    plt.xlabel('Number of samples')
    plt.ylabel('Cumulative empirical frequency')
    plt.title('Cumulative empirical frequencies for each market demand outcome')
    plt.show()

    return high_demand_cum_freqs, medium_demand_cum_freqs, low_demand_cum_freqs

if __name__ == "__main__":
    high, med, low = sim_eco_conditions(1000)
    investments = np.array([[200000, 80000, -30000],
                            [150000, 100000, 10000],
                            [0, 0, 0]])
    x = expected_utility(investments, np.array([high[-1], med[-1], low[-1]]))
    print('Expected utility for investing in A: {:.2f}'.format(x[0]))
    print('Expected utility for investing in B: {:.2f}'.format(x[1]))
    print('Expected utility for not investing: {:.2f}'.format(x[2]))