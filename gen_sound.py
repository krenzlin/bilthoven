from bilthoven import write_wave
from bilthoven.random_functions import random_wave, normalize, random_walk_horizontal
from numpy import array, int16
import numpy as np
from pylab import plot, show

fs = 44100
f = 220

repeat_s = 20
repeat = f * repeat_s
#repeat = 10

sample_size = round(fs*1.0 / f)

sound = []

old_wave = random_wave(sample_size / 2)
ow = random_wave(sample_size / 2)

for i in range(repeat):
    new_wave = random_wave(sample_size / 2)

    #old_wave = old_wave - ow/2#new_wave
    old_wave = np.mean(array([[old_wave], [new_wave]]), axis=0)
    #old_wave /= np.max(np.abs(old_wave))
    sound += list(old_wave)
    #sound += 10*list(random_wave(sample_size / 2))


sound = normalize(sound, minus=True)*3276
#sound = array(sound)*3276
sound = array(sound).astype(int16)

write_wave('output/sound.wav', fs, sound)


#plot(sound)
#show()