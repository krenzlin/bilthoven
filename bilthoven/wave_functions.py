import scipy.io.wavfile
import numpy as np


def read_wave(file_name):
    rate, data = scipy.io.wavfile.read(file_name)
    data = data.astype(np.float64)
    data /= np.iinfo(np.int16).max
    return rate, data


def write_wave(file_name, rate, data):
    data *= np.iinfo(np.int16).max - 1
    if data.dtype == np.object:
        # need to make every channel the same length
        new_data = np.zeros((len(max(data, key=len)), data.shape[0]))
        for i in range(data.shape[0]):
            new_data[:len(data[i]), i] = data[:][i]
        data = new_data
    data = data.astype(np.int16)
    scipy.io.wavfile.write(file_name, rate, data)

