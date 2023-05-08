import numpy as np
investments = np.array([[200000, 80000, -30000], [150000, 100000, 10000], [0, 0, 0]])
def expected_utility(profit_values,probabilities):
    """
    computes the expected utility of each investment
    :param profit_values: numpy array of profits for each investment
    :param probabilities: list of probabilities for each investment
    :return: a numpy array of expected utility of each investment
    """
    return np.dot(profit_values, probabilities)

# computing the regret of each investment
def minimax_regret_decision(profit_values):
    """
    computes the regret of each investment
    :param profit_values: numpy array of profits for each investment
    :return: decision with the minimum regret
    """
    return np.min(np.max(np.max(profit_values, axis=0) - profit_values, axis=1))

if __name__ == "__main__":
    print(expected_utility(investments, np.array([0.5, 0.3, 0.2])))
    print(minimax_regret_decision(investments))