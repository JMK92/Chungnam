from pop import Led
from pop import time

l = Led()
l.on()
print("Led %d"%(l.stat()))
time.sleep(2)
l.off()
print("Led %d"%(l.stat()))
time.sleep(2)