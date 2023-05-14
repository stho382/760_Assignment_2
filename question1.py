import numpy as np
investments = np.array([[200000, 80000, -30000],
                        [150000, 100000, 10000],
                        [0, 0, 0]])
investments_2 = np.array([[3, 5],
                        [1, 7]])
investments_3 = np.array([[7, 11],
                        [3, 16]])
investments_4 = np.array([[7, 11],
                        [3, 15]])
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
    :return: Decision with the minimum regret
    """
    max_regret_for_each_decision = np.max(np.max(profit_values, axis=0) -
                                          profit_values, axis=1)
    optimal_decision = f"Decision {np.where(max_regret_for_each_decision == np.min(max_regret_for_each_decision))[0][0] + 1}"
    return optimal_decision

def test_2(profit_values,probabilities):
    pass

if __name__ == "__main__":
    x = expected_utility(investments, np.array([0.5, 0.3, 0.2]))
    print('Expected utility for investing in A: {:.2f}'.format(x[0]))
    print('Expected utility for investing in B: {:.2f}'.format(x[1]))
    print('Expected utility for not investing: {:.2f}'.format(x[2]))
    print(f"Optimal decision with the minimum regret is: "
          f"{minimax_regret_decision(investments)}")
    print(f"Optimal decision with the minimum regret is: "
          f"{minimax_regret_decision(investments_2)}")
    print(f"Optimal decision with the minimum regret is: "
          f"{minimax_regret_decision(investments_3)}")
    print(f"Optimal decision with the minimum regret is: "
          f"{minimax_regret_decision(investments_4)}")

