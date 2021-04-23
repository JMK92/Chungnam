from pop import Battery, Light, Tphg
from pop import time
import os

battery = Battery()
light = Light()
tphg = Tphg()

if 'sensors.dat' in os.listdir():
    os.remove("sensors.dat") 
    
f = open("sensors.dat", "w")
f.write("BATTERY, LIGHT, TPHG, PRESS, HUMI, GAS\n")

for _ in range(10):
    v = battery.read()
    l = light.read()
    t, p, h, g = tphg.read()

    data = "%.2f, %d, %.2f, %.2f, %.2f, %d" %(v, l, t, p, h, g)
    print(data)
    f.write(data + "\n")
    time.sleep(1)
    
f.close()
    