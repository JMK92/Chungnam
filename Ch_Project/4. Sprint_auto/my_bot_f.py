from pop import Pilot
from pop import LiDAR
from gtts import gTTS
import BlynkLib
from popAssist import *

import subprocess
import math
import time
import random
import threading

BLYNK_AUTH = 'Z9rZjLjIkSz63o1zvuFtyfJapf7L4afq'
blynk = BlynkLib.Blynk(BLYNK_AUTH)  

bot = Pilot.SerBot()
lidar = LiDAR.Rplidar()
lidar.connect()

class Lidar:
    def __init__(self, width, directions):
        self.serbot_width = width
        self.degrees = list(range(0, 360, 360 // directions))

        self.lidar = LiDAR.Rplidar()
        self.lidar.connect()
        self.lidar.startMotor()

    def __del__(self):
        self.bot.stop()
        self.lidar.stopMotor()

    def calcAngle(self, length):
        tan = (self.serbot_width / 2) / length
        angle = math.atan2(length, (self.serbot_width / 2)) * (180 / math.pi)
        return angle

    def collisonDetect(self, length):
        detect = [0] * len(self.degrees)         
        angle = self.calcAngle(length)
        ret = self.lidar.getVectors()
        for deg, dis, _ in ret:
            for i, detect_direction in enumerate(self.degrees):
                min_degree = (detect_direction - angle) % 360
                if (deg + (360 - min_degree)) % 360 <= (angle * 2):
                    if dis < length:
                        detect[i] = 1
                        break
        return detect

n = None
# text = None
auto = False

@blynk.VIRTUAL_WRITE(0)
def go_button(n):
    global auto

    if int(n[0])== 1:
        auto = True
        auto_car()
        print(n)
    else:
        bot.stop()
        lidar.stopMotor()       
        auto = False
        print(n)
        
def auto_car():
    serbot_width = 500
    direction_count = 8
    speed = 50
    
    lidar = Lidar(serbot_width, direction_count)
    current_direction = 0
            
    with subprocess.Popen(['play', 'start.mp3']) as p: #Popen([리눅스 명령어, filename])
        p.wait()
        
    flag = True
    
    while flag:
        try:
            if lidar.collisonDetect(400)[current_direction]:
                with subprocess.Popen(['play', 'say.mp3']) as p: 
                    p.wait()
                bot.stop()
                continue

            detect = lidar.collisonDetect(800) 

            if sum(detect) == direction_count:
                bot.stop()
                continue
                        
            if detect[current_direction]:                                                        
                open_directions = [i for i, val in enumerate(detect) if not val]
                current_direction = random.choice(open_directions)                    

            bot.move(lidar.degrees[current_direction], speed)                    
            print(detect)

        except (KeyboardInterrupt, SystemError):            
            flag = False                             

@blynk.VIRTUAL_WRITE(1)
def go_button2(n):      
    if n[0] == '0'or n[0] == '1':
        
        bot.stop()
        lidar.stopMotor()
        print("정지")

@blynk.VIRTUAL_WRITE(2)
def say(n):
    if int(n[0]) == 1:
        with subprocess.Popen(['play', 'hey.mp3']) as p: 
            p.wait()

@blynk.VIRTUAL_WRITE(3)
def left(n):
    if int(n[0]) == 1:        
        bot.move(270,50)
        time.sleep(1)
    else:
        bot.stop()

@blynk.VIRTUAL_WRITE(4)    
def right(n):
    if int(n[0]) == 1:        
        bot.move(90,50)
        time.sleep(1)
    else:
        bot.stop()    

@blynk.VIRTUAL_WRITE(5)    
def front(n):
    if int(n[0]) == 1:        
        bot.move(0,50)
        time.sleep(1)
    else:
        bot.stop()
@blynk.VIRTUAL_WRITE(6)    
def back(n):
    if int(n[0]) == 1:        
        bot.move(180,50)
        time.sleep(1)
    else:
        bot.stop()

def userAction(text):
    if '그만' in text:        
        bot.stop()
        lidar.stopMotor()
        bot.stop()
        return True
    return False

def onStart():
    print(">>> Start recording...")

def assist():
    steam = create_conversation_stream()
    ga = GAssistant(steam, local_device_handler=userAction) 
    while True:
        ga.assist(onStart)



def main():
    global n
    #n = mp.Manager().Value('n', None) 
    # text = mp.Manager().Value('text', None) 
    
    # steam = create_conversation_stream()
    # ga = GAssistant(steam, local_device_handler=userAction) 
    #b = threading.Thread(target=go_button2, args=(n,))
    a = threading.Thread(target=assist)
    #b.start()
    a.start()   
    while True:    
        blynk.run()
        #ga.assist(onStart)

if __name__ == '__main__':
    main()
    # p1 = mp.Process(target=go_button, args=(n,))
    # p2 = mp.Process(target=go_button2, args=(n,))
    # p3 = mp.Process(target=say, args=(n,))

    # p1.start()
    # p2.start()
    # p3.start()

    # p1.join()
    # p2.join()
    # p3.join()

        
