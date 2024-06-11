import numpy
import sycomore
from sycomore.units import *

species = sycomore.Species(1000*ms, 100*ms)
TE = 4*ms
train_length = 40

model = sycomore.epg.Regular(species)
signal = numpy.zeros(train_length, dtype=complex)

model.apply_pulse(90*deg)
for echo in range(train_length):
    model.apply_time_interval(TE/2)
    model.apply_pulse(180*deg)
    model.apply_time_interval(TE/2)
    
    signal[echo] = model.echo

print(signal-echo)