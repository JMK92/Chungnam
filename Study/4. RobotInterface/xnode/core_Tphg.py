from pop import Tphg
import time

tphg = Tphg()

# for _ in range(5):
#     val = tphg.read()
#     print('temp : %.1f, Press : %.1f hpa, Humi : %.1f RH, Gas : %d ohm'%(val))
#     time.sleep(1)

for _ in range(5):
    temp, _, humi, _, = tphg.read()
    print('temp : %.1f C, Humi : %.1f RH'%(temp, humi))
    time.sleep(1)