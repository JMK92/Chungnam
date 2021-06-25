from pop import Pilot
from pop import LiDAR
from gtts import gTTS

import subprocess
import math
import random
from popAssist import *
from pop import Pilot
import multiprocessing as mp

bot = Pilot.SerBot()
def userAction(text): 
    action = False
    
    print(text)

    if text.find("전진") != -1:
        bot.forward()
        action = True
    elif text.find("후진") != -1:
        bot.backward()
        action = True
    elif text.find("정지") != -1:
        bot.stop()
        action = True

    return action

stream = create_conversation_stream()
ga = GAssistant(stream, local_device_handler=userAction) 
    
def onStart():
    print(">>> Start recording...")

while True:
    ga.assist(onStart)

print("Start Serbot!!!")

def calcAngle(length):
    tan = (self.serbot_width / 2) / length
    angle = math.atan2(tan) * (180 / math.pi)
    return angle

def main():
    SPEED = 50
    direction = 0
    
    lidar = LiDAR.Rplidar()
    bot = Pilot.SerBot()

    lidar.connect()
    lidar.startMotor()

    bot.setSpeed(SPEED)
    p1 = mp.Process(target=boo, args=(d,))
    # with subprocess.Popen(['play', 'start.mp3']) as p: #Popen([리눅스 명령어, filename])
    #     p.wait()

    while True:
        vectors = lidar.getVectors()        
        for deg, dis, _ in vectors:
            
            
        #bot.move(direction, 50)            
            

# if __name__ == '__main__':   
#     main()
#     ga.assist(onStart)
