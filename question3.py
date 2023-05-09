import numpy as np
import matplotlib.pyplot as plt

def irls_median(x, tol, max_iter, init_guess):
    # Initialize median estimate
    median_est = list()
    median_est.append(init_guess)

    # Set a small numerical fudge parameter
    delta = 1e-6

    # Iterate until convergence or maximum iterations reached
    for i in range(max_iter):
        # Update weights
        w = np.zeros(len(x))
        for j in range(len(x)):
            w[j] = 1 / np.maximum(np.abs(median_est[i] - x[j]), delta)

        # Compute median estimate
        median_est_new = np.median(np.multiply(x, w))

        # Check convergence
        if np.abs(median_est_new - median_est[i]) < tol:
            break

        # Update median estimate
        median_est.append(median_est_new)

    return np.array(median_est)

def irls_mean(x, tol, max_iter, init_guess):
    # Initialize median estimate
    mean_est = list()
    mean_est.append(init_guess)

    # Set a small numerical fudge parameter
    delta = 1e-6

    # Iterate until convergence or maximum iterations reached
    for i in range(max_iter):
        # Update weights
        w = np.zeros(len(x))
        for j in range(len(x)):
            w[j] = 1 / np.maximum(np.abs(mean_est[i] - x[j]), delta)

        # Compute median estimate
        mean_est_new = np.dot(w, x) / np.sum(w)

        # Check convergence
        if np.abs(mean_est_new - mean_est[i]) < tol:
            break

        # Update median estimate
        mean_est.append(mean_est_new)

    return np.array(mean_est)


import numpy as np


def test_median(x, tol):
    # Check if input vector has odd length
    if len(x) % 2 == 0:
        print("Input vector must have odd length!")
        return

    # Iterate over tolerance values
    for t in tol:
        # Compute median using IRLS
        median_irls = irls_mean(x, tol=t, max_iter=30, init_guess=1)[-1]

        # Compute median using np.median
        median_np = irls_median(x, tol=t, max_iter=30, init_guess=1)[-1]

        # Check if difference between medians is within tolerance
        if np.abs(median_irls - median_np) < t:
            print("IRLS and np.median agree (tol={}): {}".format(t, median_irls))
        else:
            print("IRLS and np.median do not agree (tol={}): {}".format(t, median_irls))


if __name__ == "__main__":
    x = [1.1, 4.5, 2.1, 10.2, 16.1, 5.8, 900, 11, 15.6]
    tol = 1e-3
    max_iter = 30
    init_guess = 1
    y = irls_mean(x, tol, max_iter, init_guess)
    z = irls_median(x, tol, max_iter, init_guess)
    test_median(x, [1e-3, 1e-3, 1e-3, 1e-3, 1e-3, 1e-3, 1e-3, 1e-3])

    plt.plot(range(1, len(z) + 1), z, marker='o', label='IRLS Median')
    plt.plot(range(1, len(y) + 1), y, marker='o', label='IRLS Mean')
    plt.xlabel('Iteration')
    plt.ylabel('Median Estimate')
    plt.title('IRLS Median Convergence')
    plt.legend()
    plt.show()