import scipy.io.wavfile
import numpy as np


def read_wave(file_name):
    rate, data = scipy.io.wavfile.read(file_name)
    data = data.astype(np.float64)
    data /= np.iinfo(np.int16).max
    return rate, data


def write_wave(file_name, rate, data):
    data *= np.iinfo(np.int16).max
    data = data.astype(np.int16)
    scipy.io.wavfile.write(file_name, rate, data)

