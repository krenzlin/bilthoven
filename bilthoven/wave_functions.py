import scipy.io.wavfile


def read_wave(file_name):
    rate, data = scipy.io.wavfile.read(file_name)
    return rate, data


def write_wave(file_name, rate, data):
    scipy.io.wavfile.write(file_name, rate, data)

