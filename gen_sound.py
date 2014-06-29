from bilthoven import write_wave
from bilthoven.random_functions import random_wave, normalize, random_walk_horizontal
from numpy import array, int16
import numpy as np
from pylab import plot, show

fs = 44100
f = 220

repeat_s = 20
repeat = f * repeat_s


sample_size = round(fs*1.0 / f)

sound = []

old_wave = random_walk_horizontal(sample_size)
for i in range(repeat):
    #new_wave = normalize(old_wave - random_walk_horizontal(sample_size)/10.0)
    new_wave = old_wave - random_walk_horizontal(sample_size)/2.0
    #new_wave = normalize(wave, minus=True)
    new_wave -= new_wave[0] - old_wave[-1]
    sound += list(new_wave)
    old_wave = new_wave

sound = array(sound)
sound /= np.max(sound)
write_wave('output/sound.wav', fs, sound)
