from pop import Psd, Leds
import time
import BlynkLib
import numpy as np
import pandas as pd




blynk = BlynkLib.Blynk('EHMNNcBg45zgOR-NpFtcrtGmVe8FfIz1', server='127.0.0.1', port='8080')

# 
@blynk.VIRTUAL_READ(1)
def car():
    
    dis= Psd()
    leds = Leds()
    res = []
 
    city = {'ulsan': 30, 'Seoul':15}
    x = input('도시는 : ')
       
    for i in range(city[x]):
        val = dis.readAverage()
        ret = round(dis.calcDist(val), 2)
        blynk.virtual_write(1,ret)

        print(ret) 
        time.sleep(0.1)

        if ret < 20:            
            a = leds.allOn()
            a
        elif 20<= ret < 80:
            for _ in range(5):
                leds.allOn()
                time.sleep(0.1)
                leds.allOff()
                time.sleep(0.1)
        else:
            b = leds.allOff()
            b
        
        res.append(ret)
    print(len(res), res)
    time.sleep(0.5)
    
    data_frame = pd.DataFrame(res)
    print(data_frame)
    data_frame.to_csv('/home/soda/Project/python/testSource/file101.csv', header= False, index = False)
      
i = 0
while i < 1:
    blynk.run()
    car()
    i += 1

