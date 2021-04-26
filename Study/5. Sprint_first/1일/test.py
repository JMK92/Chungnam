# xpop.py


# LED

from pop import Leds 

class xLeds(leds):
    def __init__(self, ...):
        Leds.__init__(...)
        #....
    
    def caller(self, ...):
        pass
    
    @caller    
    def on(self):
        pass
    
    @caller
    def off(self):
        pass
    
#----------------------------------------    
from xpop import xLeds

l = xLeds()
l(0).on()
l(0).off()

#------------------------------------------

# 바이트, 파이썬 문자열 사이 변환.

a = "python String" # 파이썬 문자열 
# a, b는 변경 불가능한 객체 -> 읽기 전용 객체
b = b"system string" # 바이트 문자열 -> 파일로 읽어오거나 보낼때, 저장.

bb = a.encode() # 파이썬을 바이트 문자열로 바꾸어줌
# aa : str ncode()
aa = b.decode() # 바이트 문자를 파이썬으로

# bbb는 변경가능한 객체 -> 읽기 전용만 할거면 필요X
bbb = bytearray(s)

# 변경가능한 객체의 특성( 얕은 복사, 깊은복사 ).
from copy import copy, deepcopy# deepcopy 메모리 할당이 큼. 염두해 두어서 사용

# 제너레이터 
com_l = =[i for i in range(1, 10+1)]

x = (i for i in range(1, 10+1)) # 튜플은 listcompre가 아닌 제너레이터임. 호출하면  10이 나옴.

def xrange(start, end = None, step=1.0, digit = 5): # 제너레이터
    if end == None:
        end = float(start)
        start = 0.0
        
    while float(round(start, digit)) < end:
        yield float(round(start, digit))
        start += step
        

for i in range(1, 10, 1.7): # 제너레이터는 range도 포함.
    print(i)
    
# 일급 함수

def fibonacci(n):
    if n < 2:
        return 1
    else:
        fibonacci(n-2) + fibonacci(n-1)
    return # 1 if n < 2 else fibonacci(n-2) + fibonacci(n-1)

fibo = fibonacci # 동적함수

print(fibo(6)) # 동적함수 사용

# 일급함수는 고차함수 일때 사용

# 고차 함수
def getter(func, *args):
    ret = []
    end = len(args)
    i = 0
    while i < end:
        if func[arg[i]]:
            ret.append(args[i])
            i += 1
    return 1

def isodd(n):
    return n % 2 == 1 # 홀수 판별
a = getter(isodd, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# 고참 함수2 -> 클로저
def adder(n):
    def sencond_adder(m):
        return n +m
    
    return sencond_adder

to_addr = adder(10)
ret = to_addr(20)

# 클로저
def make_adder(n):
    total = n # total은 지역변수
    
    def adder(m):
        nonlocal total # total을 받아 들인다.
        total += m
        return total
    
    return adder

adder = make_adder(10)
adder(20)
adder(30)
ret = adder(40)

# 데커레이터
def caller(func):
    def wrapper(*args, **kawrgs):
        # todo...
        ret = func(*args, **kawrgs)
        # todo....
        return ret
    
    return wrapper

@caller # caller func에 foo가 들어감.
def foo(n, m):
    return n-m

ret = foo(2, 6) # caller의 반환값(wrapper)임. 위의 foo가 아님

# file로 저장.(binary code로)
# read에서 볼 수 있게끔.
# 장비 제어하는 함수. (최소 5개)
# 데커레이터 
# 응용예제 1개.
# pop소스 고치기X, xpop으로 새로 만들기. 

def caller(func):
    
    def wrapper(*args, **kawrgs):
        # todo..기록을 남길 수 있음.(profile)
        ret = func(*args, **kawrgs)
        # todo.. 기록을 남길 수 있음.(profile)
        return ret
    
    return wrapper

@caller
def factorial(n):
    return 1 if n < 2 else: n * factorial(n-1)

#factorial = caller(factorial) # 위에 @caller추가함으로 이 명령을 안쓸수 있다. 
ret = factorial(4)

#---------------------------------------------------------------------------
import time

def perform_clock(func):
    
    def wrapper(*args):
        
        start = time.perf_counter()# todo..기록을 남길 수 있음.(profile)
        ret = func(*args) # 키워드 인자 없어도 됨.
        elapsed = time.perf_counter() - start# todo.. 기록을 남길 수 있음.(profile)
        print("[%.8fs]%(%s)->%r"%(elapsed, func.__name__, ','.join(repr(arg) for in args), ret))
        return ret
    
    return wrapper

@caller
def factorial(n):
    return 1 if n < 2 else: n * factorial(n-1)

#factorial = caller(factorial) # 위에 @caller추가함으로 이 명령을 안쓸수 있다. 
ret = factorial(4)