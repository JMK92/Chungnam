from pop import Light
from pop import time

l = Light()

for _ in range(10):
    val = l.read()
    print('light = %d lx' %(val))
    time.sleep(1)
    
    