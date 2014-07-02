from bilthoven.random_functions import random_walk_simple, random_walk, normalize, mirror_walk
from bilthoven import write_wave
import numpy as np
from itertools import izip

import pylab


def create_random_limits(lower_boundary, upper_boundary):
    min, max = np.random.uniform(lower_boundary, upper_boundary, 2)
    if min > max:
        min, max = max, min
    return min, max


def gendy(segments, iterations, duration_factor=12.0):
    duration_limits = create_random_limits(0.9, 1)
    amplitude_limits = create_random_limits(-1, 1)
    print 'segments:', segments
    print 'durations:', duration_limits
    print 'duration factor:', duration_factor
    print 'amplitudes:', amplitude_limits

    durations = []
    for segment in xrange(segments):
        durations += [list(mirror_walk(iterations, duration_limits[0], duration_limits[1]))]
    durations = np.array(durations)


    amplitudes = []
    for segment in xrange(segments):
        rw = mirror_walk(iterations, amplitude_limits[0], amplitude_limits[1])
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
for i in gendy(10, 1000):
    wave += list(i) #+ list(j)
#print wave
write_wave('output/gendy.wav', 44100, np.array(wave))

#pylab.plot(wave)
#pylab.show()
