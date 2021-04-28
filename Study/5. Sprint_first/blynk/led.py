from pop import Leds
import time
import BlynkLib
blynk = BlynkLib.Blynk('wDpqfJFPawGuN4qnGek85S5XpJI5VBIh', server='127.0.0.1', port='8080')

leds = Leds()

@blynk.VIRTUAL_WRITE(1)
def led_on_off(n):
    for i in n:
        if i == '0':
            leds.allOff()
        elif i == '1':
            leds.allOn()

@blynk.VIRTUAL_WRITE(2)
def led_on_off(n):
    for i in n:
        if i == '0':
            leds.allOff()
        elif i == '1':
            leds.allOn()

# @blynk.VIRTUAL_WRITE(3)       
# def led_step(n):
#     for i in n:
#         for j in range(8):
#             if i == '0':
#                 leds[j].on()
#                 time.sleep(0.5)
#                 j += 1
#                 if i == '1':
#                     leds[j].off()


while True:
    blynk.run()
