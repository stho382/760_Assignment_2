import numpy as np
import matplotlib.pyplot as plt

def irls_median(x, tol, max_iter, init_guess):
    """
    Implementation of the IRLS function for finding the median of a set of N numbers
    :param x: array of numbers
    :param tol: error tolerance
    :param max_iter: maximum number of iterations
    :param init_guess: initial guess for median
    :return: array of median estimates calculate via the IRLS method
    """
    # Initialize median estimate
    median_est = list()
    median_est.append(init_guess)

    # Set a small numerical fudge parameter
    delta = 1e-6

    # Iterate until convergence or maximum iterations reached
    median_est_new = median_est[-1]
    for i in range(max_iter):
        # Update weights
        w = np.zeros(len(x))
        for j in range(len(x)):
            w[j] = 1 / np.maximum(np.abs(median_est_new - x[j]), delta)

        # Compute median estimate
        median_est_new = np.average(x, weights=w)

        # Check convergence
        if np.abs(median_est_new - median_est[-1]) < tol:
            break

        # Update median estimate
        median_est.append(median_est_new)

    return np.array(median_est)

# def irls_mean(x, tol, max_iter, init_guess):
#     # Initialize median estimate
#     mean_est = list()
#     mean_est.append(init_guess)
#
#     # Set a small numerical fudge parameter
#     delta = 1e-6
#
#     # Iterate until convergence or maximum iterations reached
#     mean_est_new = mean_est[-1]
#     for i in range(max_iter):
#         # Update weights
#
#         mean_est_new = np.average(x)
#
#         # Check convergence
#         if np.abs(mean_est_new - mean_est[i]) < tol:
#             break
#
#         # Update median estimate
#         mean_est.append(mean_est_new)
#
#     return np.array(mean_est)


def test_median(x, tol):
    """
    Function that takes a vector of numbers and user tolerances and
    checks answer from irls_median against the in-built
    function for the median
    :param x: array of numbers
    :param tol: error tolerance
    """
    # Check if input vector has odd length
    if len(x) % 2 == 0:
        print("Input vector must have odd length!")
        return

    # Iterate over tolerance values
    for t in tol:
        # Compute median using IRLS
        median_irls = irls_median(x, tol=t, max_iter=30, init_guess=1)[-1]

        # Compute median using np.median
        median_np = np.median(x)

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
    z = irls_median(x, tol, max_iter, init_guess)
    print(z[-1])
    print(np.mean(x))
    a = np.repeat(np.median(x),  len(z))
    b = np.repeat(np.mean(x),  len(z))


    plt.plot(range(1, len(z) + 1), z, marker='o', label='IRLS Median')
    plt.plot(range(1, len(a) + 1), a, marker='o', label='Built-in median function')
    plt.plot(range(1, len(b) + 1), b, marker='o', label='Built-in mean function')
    plt.xlabel('Iteration')
    plt.ylabel('Median Estimate')
    plt.title('IRLS Median Convergence')
    plt.legend()
    plt.show()

    test_median(x, [1e-3, 2e-3, 3e-3, 4e-3, 5e-3, 6e-3, 7e-3, 8e-3])
