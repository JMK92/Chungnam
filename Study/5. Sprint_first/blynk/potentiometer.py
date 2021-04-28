from pop import Potentiometer
import time
import BlynkLib

blynk = BlynkLib.Blynk('wDpqfJFPawGuN4qnGek85S5XpJI5VBIh', server='127.0.0.1', port='8080')

@blynk.VIRTUAL_READ(5)
def on_poten():
    poten = Potentiometer()
    val = int(poten.readAverage()*0.95)
    if val>9: val=10
    blynk.virtual_write(5,val)
       
while True:
    blynk.run()