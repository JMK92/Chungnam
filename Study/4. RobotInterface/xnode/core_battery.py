from pop import Battery
from pop import time

b = Battery()

for _ in range(5):
    print('Battery: %.1f volt'%(b.read()))
    time.sleep(1)
    