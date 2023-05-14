import numpy as np
import matplotlib.pyplot as plt

def geometric_median(x, tol, max_iter, init_guess):
    """
    Function for finding the geometric median vector for a set of 𝑁 vectors
    :param x: array of numbers
    :param tol: error tolerance
    :param max_iter: maximum number of iterations
    :param init_guess: initial guess for median
    :return: array of median estimates calculate via the geometric median method
    """

    # Set a small numerical fudge parameter
    delta = 1e-6

    # Iterate until convergence or maximum iterations reached
    median_est_new = init_guess
    for i in range(max_iter):
        # Update weights
        distances = np.maximum(np.sqrt(np.sum((median_est_new - x)**2, axis=1)), delta)
        w = 1.0 / distances

        w /= np.sum(w)

        median_est_new_2 = np.average(x, axis=0, weights=w)

        # Check convergence
        if np.all(distances < tol):
            break

        # Update median estimate
        median_est_new = median_est_new_2

    return np.array(median_est_new)


if __name__ == '__main__':
    x = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9,10], [11,12], [13,14]])
    tol = 1e-3
    max_iter = 30
    init_guess = [1,2]

    median_estimates = geometric_median(x, tol, max_iter, init_guess)
    print(median_estimates)

    # plot the input vectors and the geometric median estimate
    plt.scatter(x[:, 0], x[:, 1], c='blue')
    plt.scatter(median_estimates[0], median_estimates[1], c='red')
    plt.title("Geometric Median")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

    x_2 = np.array([[1.1], [4.5], [2.1], [10.2], [16.1], [5.8], [900], [11], [15.6]])
    tol_2 = 1e-3
    max_iter_2 = 30
    init_guess_2 = [1]

    median_estimates_2 = geometric_median(x_2, tol_2, max_iter_2, init_guess_2)
    print(median_estimates_2)