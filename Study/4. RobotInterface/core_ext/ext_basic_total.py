from pop import Buzzer, Leds, Buttons, rand
from pop import time

buzzer = Buzzer()
leds = Leds()
buttons = Buttons()

bt0 = bt1 = False

print('Start')

while True:
    if buttons[0] != bt0:
        bt0 = not bt0
        if bt0 == True:
            t0 = time.ticks_ms()
            buzzer.beep(5)
        else:
            if time.ticks_ms() - t0 > 2000:
                break
    
    if buttons[1] != bt1:
        bt1 = not bt1
        if bt1:
            n = rand() % 255 +1
            leds.write(n)
            print(n)
        else:
            leds.clear()
    time.sleep(.5)
    
print('The End')    