import numpy as np


def random_walk(N, minus=False):
    """Returns a second order random walk from 0..1 of length N."""
    first_order = np.cumsum(np.random.randn(N))
    second_order = np.cumsum(first_order)
    second_order = second_order - np.min(second_order)
    second_order = second_order / np.max(second_order)
    if minus:
        second_order *= 2
        second_order -= 1
    return second_order


def random_walk_simple(N, minus=False):
    """Returns a second order random walk from 0..1 of length N."""
    first_order = np.cumsum(np.random.randn(N))
    first_order -= np.min(first_order)
    first_order /= np.max(first_order)
    if minus:
        first_order *= 2
        first_order -= 1

    return first_order


def normalize(xs, min=0, max=1, randomize=False):
    if randomize:
        min = np.random.randn()
        max = np.random.randn()
        if max < min:
            max, min = min, max
        min = np.max([-1, min])
        max = np.min([1, max])
        print min, max
    xs -= np.min(xs)
    xs /= np.max(xs)
    xs *= (max - min)
    xs += min
    return xs


def mirror_walk(N, lower_boundary=0, upper_boundary=1, factor=1):
    rw = np.zeros(N)
    current = 0
    for i in range(N):
        current += factor*(np.random.rand() - 0.5)

        if current > upper_boundary:
            current = upper_boundary - (current - upper_boundary)

        if current < lower_boundary:
            current = lower_boundary - (current - lower_boundary)

        rw[i] = current

    return rw