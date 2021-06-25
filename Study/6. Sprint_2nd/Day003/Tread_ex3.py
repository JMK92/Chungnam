#import multiprocessing as mp
import  threading as th

x = None

def boo():#d):
    global x
    x = 10
    #d.append(1)

def foo():#d):
    # global x          # boo의 x랑은 전역변수는 맞는데 다른 전역변수이다.
    print(x)
    # x = 100
    #d.append(2)

def main():
    #d = mp.Manager().list()  # thread는 매니저 객체가 없다
    p1 = th.Thread(target=boo)#, args=(d,))
    p2 = th.Thread(target=foo)#, args=(d,))
    # p1 = mp.Process(target=boo, args=(d,))
    # p2 = mp.Process(target=foo, args=(d,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    #print(d)

    #foo()
    #boo()
if __name__ == '__main__':
    main()