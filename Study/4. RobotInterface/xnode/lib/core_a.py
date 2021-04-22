import time
import struct
import pycom

from machine import ADC

#----------------------------------------------------------------------------------
#Core
#----------------------------------------------------------------------------------

from sys import stdin
from sys import stdout 

class Uart:            
    def read(self, size=None):
        if size is None:
            return stdin.read().encode()
        else:
            return stdin.read(size).encode()            
    
    def write(self, n):
        stdout.write(n)      

class RgbLed:
    def __init__(self):
        self.color = 0
        pycom.heartbeat(False)
        self._stat=False        

    def setColor(self,color):
        self.color = color

    def getColor(self):
        return self.color

    def on(self):
        pycom.rgbled(self.color)
        self._stat=True
    
    def off(self):
        pycom.rgbled(0)
        self._stat=False 
        
    def stat(self):
        return self._stat       

class Battery:
    def __init__(self):
        self._adc = ADC()
        self.adc = self._adc.channel(pin='P16')

    def read(self):
        return ((self.adc.value() * 1.1 / 4095))*(13.3/3.3)