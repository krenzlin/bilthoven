bilthoven
=========

bilthoven lets you generate electroacoustic music by transformation of existing audio material.



Why bilthoven?
--------------

Bilthoven is a village in the Netherlands where Gottfried Michael Koenig held courses (1961-65) on creating compositions by using transformation techniques on existing material over several iterations.

``bilthoven`` takes this approach and tries to combine it with more complex transformations and randomization.


What's bilthoven?
-----------------

``bilthoven`` consists of two parts. First a library that does all the processing of audio files and can be easily extended by your own transformation functions. Second an application that takes given audio material and generates a new composition for you.


Applying a transformation
-------------------------

``bilthoven`` gives you the tools to easily apply a transformation on piece of audio material.

```python
from bilthoven import process, read_wave, write_wave
from bilthoven.transformations import reverse

wave_data = read_wave('examples/example.wav')
processed_data = process(wave_data, reverse)
write_wave('output/example-reversed.wav')
```

What ``bilthoven`` does is that it cuts the audio data into little blocks which then are processed one by one.


Writing your own transformation
-------------------------------

``bilthoven`` provides a set of transformation, but you can easily write your own function. You only have to stick to the interface that ``bilthoven`` uses.

```python
def my_transformation(current_block, previous_block, random_parameter):
    # do your processing
    return processed_frame
```
* **current_block**: an array that holds that audio for the block currently processed
* **previous_block**: the same, but only the block before the current one
* **random_parameter**: this is parameter that the ``process`` function provides, you don't **have** to use it

..note::
   All blocks are numpy arrays.
   

Applying your own transformation is easy

```python
processed_data = process(wave_data, my_transformation)
```
