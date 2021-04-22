from pop import Led
import time

l = Led()

for _ in range(10):
    l.on()
    print('led on')
    time.sleep(0.5)
    l.off()
    print('led off')
    time.sleep(0.5)