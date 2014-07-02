from bilthoven.random_functions import random_walk_simple, random_walk, normalize
from bilthoven import write_wave
import numpy as np
from itertools import izip

import pylab




def gendy(segments, iterations, duration_factor=32.0):
    durations = []
    for segment in xrange(segments):
        durations += [list(random_walk_simple(iterations))]
    durations = np.array(durations)

    amplitudes = []
    for segment in xrange(segments):
        rw = normalize(random_walk_simple(iterations), min=-1, max=1)
        amplitudes += [list(rw)]
    amplitudes = np.array(amplitudes)

    for iteration in xrange(iterations):
        wave = []
        for segment in xrange(segments):
            start_point = amplitudes[segment, iteration]
            duration = durations[segment, iteration] * duration_factor
            if segment == segments - 1:
                end_point = amplitudes[0, iteration]
            else:
                end_point = amplitudes[segment+1, iteration]
            wave += list(np.linspace(start_point, end_point, duration))
        yield np.array(wave)


wave = []
for i,j in izip(gendy(72, 1000), gendy(10, 1000)):
    wave += list(i) #+ list(j)
#print wave
write_wave('output/gendy.wav', 44100, np.array(wave))

#pylab.plot(wave)
#pylab.show()
