import nidaqmx

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
    task.read()

# example of writing to daq
# https://nidaqmx-python.readthedocs.io/en/latest/
'''
import nidaqmx
from nidaqmx.types import CtrTime
with nidaqmx.Task() as task:
    task.co_channels.add_co_pulse_chan_time("Dev1/ctr0")
    sample = CtrTime(high_time=0.001, low_time=0.001)
    task.write(sample)

1
with nidaqmx.Task() as task:
    task.ao_channels.add_ao_voltage_chan("Dev1/ao0")
    task.write([1.1, 2.2, 3.3, 4.4, 5.5], auto_start=True)
'''