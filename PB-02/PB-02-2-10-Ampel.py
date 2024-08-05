#==========================================================================
#
# PB-02-2-10-Ampel.py
#
# 3 LEDs, 3 Widerstände
#
#==========================================================================
#
import machine
import utime
gr = machine.Pin(11, machine.Pin.OUT, value=0)
ge = machine.Pin(13, machine.Pin.OUT, value=0)
ro = machine.Pin(15, machine.Pin.OUT, value=0)

while True:
    ro.value(1)
    utime.sleep(5)
    ge.value(1)
    utime.sleep(2)
    ro.value(0)
    ge.value(0)
    gr.value(1)
    utime.sleep(4)
    gr.value(0)
    ge.value(1)
    utime.sleep(2)
    ge.value(0)
   
   