import scipy.io.wavfile


def read_wave(file_name):
    return scipy.io.wavfile.read(file_name)


def write_wave(file_name, rate, data):
    scipy.io.wavfile.write(file_name, rate, data)

