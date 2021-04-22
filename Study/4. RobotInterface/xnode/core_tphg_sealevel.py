from pop import Tphg
import time

tphg = Tphg()

for _ in range(5):
    sea_level, press = tphg.sealevel(90)
    print("Sea level: %.1f hpa, Pressure : %d hpa"%(sea_level, press))