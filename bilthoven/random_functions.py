import numpy as np


def random_walk(N):
    """Returns a second order random walk from 0..1 of length N."""
    first_order = np.cumsum(np.random.randn(N))
    second_order = np.cumsum(first_order)
    second_order = second_order - np.min(second_order)
    second_order = second_order / np.max(second_order)
    return second_order
