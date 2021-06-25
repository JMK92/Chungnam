import multiprocessing as mp
#import  threading as th

x = None

def boo(d):
    # global x
    # x = 10
    d.value = 10

def foo(d):
    # global x          # boo의 x랑은 전역변수는 맞는데 다른 전역변수이다.
    #print(x)
    # x = 100
    d.value = 3.14

d= None

def show():
    print(d.value)


def main():
    global d
    d = mp.Manager().Value('d', None) 
    p1 = mp.Process(target=boo, args=(d,))
    p2 = mp.Process(target=foo, args=(d,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    show()
    #print(d.value)

    #foo()
    #boo()
if __name__ == '__main__':
    main()