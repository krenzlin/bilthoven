import numpy as np


def template(current_block, previous_block, random_parameter):
    """This is just a no-op transformation for you to see what interface you should provide."""
    return current_block


def reverse(current_block, *args):
    """Reverses the data of the current block."""
    return current_block[::-1]


def diff(current_block, previous_block, *args):
    """Subtracts the previous block from the current block."""
    return (current_block - previous_block[:len(current_block)])


def fft(current_block, *args):
    F = np.fft.rfft(current_block)
    f = np.fft.irfft(F)
    return np.real(f)


def reduce(current_block, *args):
    N = 4
    F = np.fft.fft(current_block)

    indexes_of_N_max_values = np.real(F).argsort()[::-1][:N]

    reduced_F = np.zeros(len(F)).astype(np.complex128)
    reduced_F[indexes_of_N_max_values] = F[indexes_of_N_max_values]

    return np.real(np.fft.ifft(reduced_F))


def random_frequency(current_block, previous_block, parameter):
    F = np.fft.rfft(current_block)

    index = np.floor((len(F)-1) * parameter / 4.0)

    reduced_F = np.zeros(len(F)).astype(np.complex128)
    reduced_F[index] = F[index]

    return np.real(np.fft.irfft(reduced_F))


def reverse_diff(current_block, *args):
    return diff(current_block, reverse(current_block))


def autocorr(x):
    result = np.correlate(x, x, mode='full')
    return result[result.size/2:]


def acf(current_block, *args):
    return autocorr(current_block)
