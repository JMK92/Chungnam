import time
import struct

from machine import Pin, ADC

#----------------------------------------------------------------------------------
#Core
#----------------------------------------------------------------------------------

from sys import stdin
from sys import stdout 

class Uart:            
    def read(self, size=None):
        if size is None:
            return stdin.buffer.read()
        else:
            return stdin.buffer.read(size)            
    
    def write(self, n):
        stdout.buffer.write(n)      

class Led:
    def __init__(self):
        self._pin = Pin("D9", Pin.OUT, value=1)

    def on(self):
        self._pin(0)

    def off(self):
        self._pin(1)
    
    def stat(self):
        return self._pin() == 0      

class Battery:
    def __init__(self):
        self.adc = ADC("D2")

    def read(self):
        return round(((self.adc.read() * 3.3 / 4095) * (3.2/2)), 1)