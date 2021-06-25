from pop import Pilot
from pop import LiDAR
from gtts import gTTS

import subprocess
import math
import random

text = "운행을 시작합니다."
filename = "start.mp3"

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
        angle = math.atan(tan) * (180 / math.pi)
        return angle

    def collisonDetect(self, length):
        detect = [0] * len(self.degrees)
        angle = self.calcAngle(length)
        ret = self.lidar.getVectors()
        for degree, distance, _ in ret:
            for i, detect_direction in enumerate(self.degrees):
                min_degree = (detect_direction - angle) % 360
                if (degree + (360 - min_degree)) % 360 <= (angle * 2):
                    if distance < length:
                        detect[i] = 1
                        break
        return detect
 
print("Start Serbot!!!")

def main():
    serbot_width = 500
    direction_count = 8
    speed = 50

    bot = Pilot.SerBot()
    lidar = Lidar(serbot_width, direction_count)
    current_direction = 0
    
    tts = gTTS(text, lang="ko") # tts = gTTs(text, lang='ko')
    tts.save(filename)
    # with subprocess.Popen(['play', 'start.mp3']) as p: #Popen([리눅스 명령어, filename])
    #     p.wait()
    flag = True
    
    while flag:
        try:
            if lidar.collisonDetect(300)[current_direction]:
                bot.stop()
                continue

            detect = lidar.collisonDetect(800)

            if sum(detect) == direction_count:
                bot.stop()
                continue
                        
            if detect[current_direction]:
                #detect[curent_directi               
                open_directions = [i for i, val in enumerate(detect) if not val]
                current_direction = random.choice(open_directions)

            bot.move(lidar.degrees[current_direction], speed)
            print(detect[current_direction])
            print(detect)

        except (KeyboardInterrupt, SystemError):            
            flag = False
    
    bot.stop()
    print('Stopped Serbot!')

if __name__ == '__main__':
    main()
    