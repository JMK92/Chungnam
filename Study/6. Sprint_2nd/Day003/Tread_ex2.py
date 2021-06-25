import multiprocessing as mp
import time
import os

start_time = time.time()

def count(n):
    proc = os.getpid()
    for i in range(n):
        print("PIDL %d, -- %d"%(proc, i))

nums = [2500, 2500, 2500, 2550]   # map 4개
pool = mp.Pool(processes=4)
pool.map(count, nums)
pool.close()
pool.join()

#pool을 사용하면서 밑에 있는 join을 for문을 사용하지 않아도 됨.
#pt =[]

# for _ in range(4):
#     pt.append(mp.Process(target=count, args=(2500,)))
#     pt[-1].start()

# p2 = mp.Process(target=count, args=(2500,))
# p3 = mp.Process(target=count, args=(2500,))
# p4 = mp.Process(target=count, args=(2500,))

# p1.start()
# p2.start()
# p3.start()
# p4.start()

# for p in pt:
#     p.join()

# p1.join()
# p2.join()
# p3.join()
# p4.join()

count(10000)
print("time : %f"%(time.time() - start_time))