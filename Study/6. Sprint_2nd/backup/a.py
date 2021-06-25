from pop import LiDAR, Pilot
import time
from gtts import gTTS
import subprocess
import threading
import random

SPEED = 20
disrection = 0  # 현재각
k = 0
q = 4


lidar = LiDAR.Rplidar()
bot = Pilot.SerBot()

lidar.connect()
lidar.startMotor()

bot.setSpeed(SPEED)

def talk():

    global k
    global q

    q = int(input("종료 0"))

    k = 0

        
while True:
    collision = True
    if q==3:
        break

    while collision:
        

        if k == 0 :

            k = 1

            a=threading.Thread(target=talk)  # 1누르면 일시정지 2누르면 재시작 3누르면 프로그램 종료
            a.start()

        if q==1:
            bot.stop()
            while True:

                if q==2:
                    q=4 
                    break

        if q==2:
            break

        

        collision = False
        vectors = lidar.getVectors()

        
        if q == 0:
            bot.stop()
            break    
        
        for v in vectors:
            degree = v[0] 
            distance = v[1]

            if 340<=disrection<360 or 0 <= disrection <20:

                if (disrection-20)%360<degree<360 or 0<=degree<(disrection+20)%360:
                    
                    if distance <= 600:

                        collision = True
                        bot.stop()
                        
                        break


            if 20<= disrection < 340:

                if disrection-20 <= degree < disrection+20:

                    if distance <= 600:
                        collision = True
                        bot.stop()
                        
                        break
        
        
        
        if collision :
                
            disrection = random.randint(0, 359)
            print(disrection)
            #disrection %= 360

        
       
        bot.move(disrection, 50)
print("프로그램을 종료합니다")
lidar.stopMotor()
bot.stop()


            

            
            

       