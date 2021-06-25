import multiprocessing as mp
import time

print(mp.cpu_count())

def worker1(): 
    time.sleep(2)   
    print("run SubProcess1")

def worker2(): 
    time.sleep(2)   
    print("run SubProcess2")
    

p1 = mp.Process(target=worker1) # 서브프로세스로 만들어짐
p2 = mp.Process(target=worker2)
p1.start()                     # 이때 복제가 됨.
p2.start()                     
#time.sleep(2)

#p.join()                      # join 없으면 join전에 끝이남          -> end, run
print("The end MainProcess")  # join은 자식이 종료 될때까지 blocking함 -> run, end