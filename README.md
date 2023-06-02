# inductive_sensing_offshelf
## Code for NI DAQ &amp; ESCON driver phase of inductive sensing project. NOT the repo for the custom boards we're designing.

## Also contains the code for the data processing (format is: date_experiment-number.

Part of this experiment consists of asking what our reasonable range of operation is. 
Can we calculate the inductance of our electromagnet? If so, does it change in the present of the magnetic leg implant? 
If it does change, can we characterize that change and infer the position from the inductance?

Experiment 2 suggests that we operate within 15-25 mm. 
It's noisy until then and after that. I'd also believe this, because the test bench displayed abnormal flex especially starting around 6 mm of gap distance, going until near 15 mm (I observed the lower limit more rigorously than the upper, though).

My proposed steps for experiment 3: focus on half mm increments from 15 mm to 20 mm (+/- 3mm) of gap distance. We’ll have to take more trials to get a better sense of the relationship between the two and what the noise is. 

# Challenges we've encountered so far:
1. Broke the NiDaq, so we're forced to use the oscilloscope for data collection.
2. Experiments 1 and 2 consist of DC voltage input, where we assume the voltage to be steady with neglibible transient. This is a safe bet as we measured this, and found that the voltage transient is 1/30 of the current transient, so we assume it to reach steady state instantly. But, We're forced to use DC voltage because we can't read the battery voltage on the oscilloscope. The o-scope channel ground would short the motor driver battery voltage (bidirectional motor, where motor B = -40v) to the analog output voltage (range = 0 - 4 v). We also can't divide down the voltage because the resistor tolerances are too high and thus unreliable. We'd like to use a sinusoidal input around 1 HZ, since that would accurately simulate how the voltage commanded by the magnet would fluctuate along with the wearer's walking speed. 
3. The aluminum test bench literally flexes due to the sheer magnitude of force exerted by the electromagnet on the implant. We fixed this by clamping the base down to the table, but it still flexes in the stem that actually holds the electromagnet. 
