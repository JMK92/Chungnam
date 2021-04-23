from pop import Pir
from pop import time

pir = Pir()
t = time.ticks_ms()

count = 0
print('Start')

while True:
    if pir.read():
        count += 1
        if not count % 100:
            print('#', end= '') 
        
    if time.ticks_ms() - t > 10 * 1000:
        break
print("\nYour are moving power: %d"%(count))