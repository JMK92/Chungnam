from pop import Leds
from pop import time

leds = Leds()

for led in leds:
    led.on()
    time.sleep(.5)
    led.off()
    time.sleep(.5)