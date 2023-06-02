# inductive_sensing_offshelf
## Code for NI DAQ &amp; ESCON driver phase of inductive sensing project. NOT the repo for the custom boards we're designing.

A## lso contains the code for the data processing (format is: date_experiment-number.

Part of this experiment consists of asking what our reasonable range of operation is. 
Can we calculate the inductance of our electromagnet? If so, does it change in the present of the magnetic leg implant? 
If it does change, can we characterize that change and infer the position from the inductance?

Experiment 2 suggests that we operate within 15-25 mm. 
It's noisy until then and after that. I'd also believe this, because the test bench displayed abnormal flex especially starting around 6 mm of gap distance, going until near 15 mm (I observed the lower limit more rigorously than the upper, though).

My proposed steps for experiment 3: focus on half mm increments from 15 mm to 20 mm (+/- 3mm) of gap distance. We’ll have to take more trials to get a better sense of the relationship between the two and what the noise is. 
