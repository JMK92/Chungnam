from pop import time
from pop import Battery

b = Battery()

max = 4.2
min = 3.2

block = 10

step = (max-min) / block # 0.1 이됨
#block_table = { i*10 : (min+step*i) for i in range(block+1)}

block_table = {i*10:(min+step*i) for i in range(block+1)}
#block_table = {0:3.2, 10:3.3, 20:3.4 ...}

for _ in range(10):
    vol = b.read()
    print('Battery : %.1f volt'% (vol), end=",")
    if vol >= block_table[80]:
        print('HIGH')
    elif vol >= block_table[30]:
        print('MIDDLE') 
    else:
        print('LOW')
    time.sleep(1)   