from bilthoven import write_wave
from bilthoven.random_functions import random_walk_horizontal, normalize
from numpy import array, int16
from pylab import plot, show

fs = 44100
f = 440

repeat_s = 10
repeat = f * repeat_s
repeat = 100

sample_size = round(fs*1.0 / f)

sound = []
old_wave = random_walk_horizontal(sample_size)
for i in range(repeat):
    #new_wave = normalize(old_wave - random_walk_horizontal(sample_size)/10.0)
    new_wave = old_wave - random_walk_horizontal(sample_size)/1.0
    #new_wave = normalize(wave, minus=True)
    new_wave -= new_wave[0] - old_wave[-1]
    sound += list(new_wave)
    old_wave = new_wave

#sound = normalize(sound, minus=True)*3276
sound = array(sound)*3276
sound = array(sound).astype(int16)

write_wave('output/sound.wav', fs, sound)


plot(sound)
show()