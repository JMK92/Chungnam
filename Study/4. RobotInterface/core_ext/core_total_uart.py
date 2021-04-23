from pop import Battery, Light, Tphg
from pop import time
from pop import Uart

battery = Battery()
light = Light()
tphg = Tphg()

uart = Uart()

uart.write('start...\n')

while True:
    cmd = uart.read(1).decode()
    if cmd == 'q' or cmd == 'Q': # 대소문자 가리지 않고 처리
        break
    elif cmd == 'b' or cmd == 'B':
        uart.write("\nbattery: %.2f volt \n" %(battery.read()))
    
    elif cmd == 'l' or cmd == 'L':
        uart.write("\nlight: %d lx \n" %(light.read()))    
    elif cmd == 't' or cmd == 'T':
        uart.write("\nTemp: %.2f degree, Press : %2f hPa, Humi : %.2f RH, Gas : %d ohm \n" %(tphg.read())) 
    
    else: 
        uart.write("\nUnknown command")

uart.write("\n The end...\n")