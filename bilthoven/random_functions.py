import numpy as np
import pylab

def random_walk(N):
    """Returns a second order random walk from 0..1 of length N."""
    first_order = np.cumsum(np.random.randn(N))
    second_order = np.cumsum(first_order)
    second_order = second_order - np.min(second_order)
    second_order = second_order / np.max(second_order)
    return second_order


def normalize(xs, minus=False):
    xs -= np.min(xs)
    xs /= np.max(xs)
    if minus:
        xs *= 2
        xs -= 1
    return xs


def random_walk_horizontal(N):
    rw = random_walk(N)
    line = np.linspace(rw[0], rw[-1], N)

    horizontal = rw - line

    return horizontal / np.max(np.abs(horizontal))


def random_wave(N1, N2=None):
    if N2 is None:
        N2 = N1
    rw_first = random_walk_horizontal(N1)
    rw_second = random_walk_horizontal(N2)
    wave = np.append(rw_first, rw_second)

    return wave
