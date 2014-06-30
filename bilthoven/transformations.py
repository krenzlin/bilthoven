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
    f = np.fft.irfft(F).astype(np.int16)
    return f


def reduce(current_block, *args):
    N = 4
    F = np.fft.fft(current_block)

    indexes_of_N_max_values = np.imag(F).argsort()[::-1][:N]

    reduced_F = np.zeros(len(F)).astype(np.complex128)
    reduced_F[indexes_of_N_max_values] = F[indexes_of_N_max_values]

    return np.abs(np.fft.ifft(reduced_F)).astype(np.int16)


def random_frequency(current_block, previous_block, parameter):
    F = np.fft.rfft(current_block)

    index = np.floor((len(F)-1) * parameter / 4.0)

    reduced_F = np.zeros(len(F)).astype(np.complex128)
    reduced_F[index] = F[index]

    return np.abs(np.fft.irfft(reduced_F)).astype(np.int16)


def reverse_diff(current_block, *args):
    return diff(current_block, reverse(current_block))


def autocorr(x):
    result = np.correlate(x, x, mode='full')
    return result[result.size/2:]


def acf(current_block, *args):
    return autocorr(current_block)


def speedx(current_block, previous_block, factor):
    """ Multiplies the sound's speed by some `factor` """
    # random parameter 0-1 -> 0.5-1.5
    factor += 0.5
    indices = np.round(np.arange(0, len(current_block), factor))
    indices = indices[indices < len(current_block)].astype(int)
    return current_block[indices.astype(int)]
