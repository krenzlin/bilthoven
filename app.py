from bilthoven import process, read_wave, write_wave
from bilthoven.transformations import reverse

rate, wave_data = read_wave('examples/example.wav')
processed_data = process(wave_data, reverse)
write_wave('output/example-reversed.wav', rate, processed_data)