from pop import Light
import time

ks_light =   {'A':(3, 6),'B':(6, 15), 'C':(15, 30), 'D':(30, 60), 'E':(60, 150), 'F':(150, 300), 
              'G':(300, 600), 'H':(600, 1500), 'I':(1500, 3000), 'J':(3000, 6000), 'K':(6000, 15000)}

l = Light()

for _ in range(10):
    val = l.read()
    ret = None
    
    for k, v in ks_light.items():
        if val >= v[0] and val <= v[1]:
            ret = k
            
    print('light = {} lx level = {}'.format(val, ret))
    time.sleep(1)
