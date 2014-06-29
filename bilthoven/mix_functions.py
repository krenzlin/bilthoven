from pylab import plot, subplot, show
import numpy as np


def fade_out(xs, size):
    faded = np.array(xs)
    faded[-size:] *= np.linspace(1, 0, size)
    return faded


def fade_in(xs, size):
    faded = np.array(xs)
    faded[:size] *= np.linspace(0, 1, size)
    return faded


def mix(xs, ys, size):
    size = np.min([size, len(xs), len(ys)])
    faded_xs = np.append(fade_out(xs, size), np.zeros(len(ys) - size))
    faded_ys = np.append(np.zeros(len(xs) - size), fade_in(ys, size))
    return faded_xs + faded_ys
