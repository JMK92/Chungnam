from pop import Pilot
from pop import LiDAR
from gtts import gTTS
import BlynkLib

import subprocess
import math
import time
import random
from pop import Pilot

BLYNK_AUTH = 'Z9rZjLjIkSz63o1zvuFtyfJapf7L4afq'
blynk = BlynkLib.Blynk(BLYNK_AUTH)  

bot = Pilot.SerBot()

def search():
    lidar = LiDAR.Rplidar()
    lidar.connect()
    lidar.startMotor()
    time.sleep(1)
    for deg, dis, _ in getVectors():
        print(dis)
    # for deg, dis, _ in getVectors():
    #     for i in deg:        

@blynk.VIRTUAL_WRITE(0)
def go_button(n):
    print(n)
    for i in n:
        if i == '0'or i== '1':
            bot.move(0, 40)
            #search()
            print("이동")
           # if search() 
            


@blynk.VIRTUAL_WRITE(1)
def go_button2(n):
    print(n)
    for i in n:
        if i == '0'or i== '1':
            bot.stop()
            print("정지")


@blynk.VIRTUAL_WRITE(2)
def say(n):
    if int(n[0]) == 1:
        with subprocess.Popen(['play', 'start.mp3']) as p: 
            p.wait()

def calcAngle(length):
    tan = (self.serbot_width / 2) / length
    angle = math.atan2(length, tan * length) * (180 / math.pi)
    return angle

def main():
    print("Start Serbot!!!")
    SPEED = 50
    direction = 0
    
    lidar = LiDAR.Rplidar()
    bot = Pilot.SerBot()

    lidar.connect()
    lidar.startMotor()

    bot.setSpeed(SPEED)
  
    # with subprocess.Popen(['play', 'start.mp3']) as p: #Popen([리눅스 명령어, filename])
    #     p.wait()

    # while True:
    #     vectors = lidar.getVectors()        
    #     for deg, dis, _ in vectors:
            
            
        #bot.move(direction, 50)            
    
while True:    
    blynk.run()


# serbot_width = 500
# directions = 4
# degrees = list(range(0, 360, 360 // directions))
# print(degrees)
# detect = [0] * len(degrees)
# print(detect)

# tan = (serbot_width / 2) / length
# angle = math.atan(tan) * (180 / math.pi)
        
