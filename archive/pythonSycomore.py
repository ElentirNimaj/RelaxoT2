import numpy
import sycomore
from sycomore.units import *

species = sycomore.Species(1000*ms, 200*ms)

# Sequence parameters
flip_angle=180*deg
TE = 10*ms
TR = 1000*ms
phase_steps = [0*deg, 90*deg, 117*deg, 180*deg]
slice_thickness = 1*mm
tau_readout = 1*ms
repetitions = int((5*species.T1/TR))

# Motion to k-space extremity and its associated gradient amplitude
k_max = 0.5 * 2*numpy.pi/slice_thickness
G = k_max / sycomore.gamma / (tau_readout/2)

models = [
    sycomore.epg.Regular(species, unit_dephasing=k_max) for _ in phase_steps]

print([sycomore.epg.Regular(species, unit_dephasing=k_max) for _ in phase_steps])

signals = numpy.zeros((len(models), repetitions), dtype=complex)
for r in range(0, repetitions):
    for index, (phase_step, model) in enumerate(zip(phase_steps, models)):
        phase = (phase_step * 1/2*(r+1)*r)
        
        # RF-pulse and idle until the readout
        model.apply_pulse(flip_angle, phase)
        model.apply_time_interval(TE-tau_readout)
        
        # Readout prephasing and first half of the readout
        model.apply_time_interval(-G, tau_readout/2)
        model.apply_time_interval(+G, tau_readout/2)
        
        # Echo at the center of the readout, cancel the phase imparted by the
        # RF-spoiling
        signals[index, r] = model.echo * numpy.exp(-1j*phase.convert_to(rad))
        
        # Second half of the readout, idle until the end of the TR
        model.apply_time_interval(+G, tau_readout/2)
        model.apply_time_interval(TR-TE-tau_readout/2)

print(signals.shape)