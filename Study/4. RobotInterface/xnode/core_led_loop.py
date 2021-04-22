from pop import Led
from pop import time

l = Led()

for _ in range(10):
    l.on()
    print("Led on")
    time.sleep(.1)
    l.off()
    print("Led off")
    time.sleep(.1)