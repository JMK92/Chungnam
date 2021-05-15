# Sprint 
## 팀명 : Tocar 
## 주제 : 주행 상태 모니터링

![설계](https://user-images.githubusercontent.com/81665620/118348138-2b7eb700-b583-11eb-97d6-48b3343b0f1c.jpg)


## 결과 UI  : 주행 상태에 따른 실기간 데이터값과 csv 파일 생성 및 위험 감지 알림
![blynk](https://user-images.githubusercontent.com/81665620/118348152-536e1a80-b583-11eb-9cd7-0387b44b20ab.jpg)


![simu](https://user-images.githubusercontent.com/81665620/118348158-5f59dc80-b583-11eb-82d8-eef7334f2065.jpg)


https://user-images.githubusercontent.com/81665620/118348163-67b21780-b583-11eb-9f0e-468f2162a8ae.mp4



### 기대효과 :
 1. 차량 이동 시 차량 간의 평균 거리 데이터를 수집해서 차량 정체 구간의 정도를 분석 및 도로 증설 제안의 기초 자료로 활용
 2. 자동차를 주행하면서 자신의 운전 패턴 실시간 데이터 차트를 통해 파악 할 수 있으며 각 csv 센서 값을 파악하여 향후 피드백 제어를 통해 안전하게 운행 할 수 있도록 도와 줌

### 향후 연구과제 :  
 DOB(Disturbance Of Observe)를 설치하여 각 센서의 외란 값을 측정 하여 필터로 제거 후 안전한 주행 피드백 제어 연구.

#### 참조 : 
https://woolbro.tistory.com/36 : pandas 사용  
https://hi098123.tistory.com/132#982a2a  : RGB 참조

## Code
<pre>
<code>
from pop import Psd, Leds, PixelDisplay, PiezoBuzzer
import time
import BlynkLib
import pandas as pd
import threading

#------------------ Pixel Varialbe ----------------------------- 

pixel =PixelDisplay()
psd = Psd()
dis = 0

R1 = 0
G1 = 0
B1 = 200

R2 = 139
G2 = 69
B2 = 255

#------------------ Pixel Car Shape ------------------- 

def pixel_car(R1,G1,B1,R2,G2,B2):
    
    #--------- car_body ----------
    
    pixel.setColor(2,1,[R1,G1,B1])
    pixel.setColor(2,2,[R1,G1,B1])
    pixel.setColor(3,1,[R1,G1,B1])
    pixel.setColor(3,2,[R1,G1,B1])
    pixel.setColor(4,1,[R1,G1,B1])
    pixel.setColor(4,2,[R1,G1,B1])
    pixel.setColor(5,1,[R1,G1,B1])
    pixel.setColor(5,2,[R1,G1,B1])
    pixel.setColor(0,3,[R1,G1,B1])
    pixel.setColor(0,4,[R1,G1,B1])
    pixel.setColor(1,3,[R1,G1,B1])
    pixel.setColor(1,4,[R1,G1,B1])
    pixel.setColor(2,3,[R1,G1,B1])
    pixel.setColor(2,4,[R1,G1,B1])
    pixel.setColor(3,3,[R1,G1,B1])
    pixel.setColor(3,4,[R1,G1,B1])
    pixel.setColor(4,3,[R1,G1,B1])
    pixel.setColor(4,4,[R1,G1,B1])
    pixel.setColor(5,3,[R1,G1,B1])
    pixel.setColor(5,4,[R1,G1,B1])
    pixel.setColor(6,3,[R1,G1,B1])
    pixel.setColor(6,4,[R1,G1,B1])
    pixel.setColor(7,3,[R1,G1,B1])
    pixel.setColor(7,4,[R1,G1,B1])
   
 #--------- wheel --------------
   
    pixel.setColor(1,6,[R2,G2,B2])
    pixel.setColor(2,5,[R2,G2,B2])
    pixel.setColor(2,6,[R2,G2,B2])
    pixel.setColor(2,7,[R2,G2,B2])
    pixel.setColor(3,6,[R2,G2,B2])
    pixel.setColor(4,6,[R2,G2,B2])
    pixel.setColor(5,5,[R2,G2,B2])
    pixel.setColor(5,6,[R2,G2,B2])
    pixel.setColor(5,7,[R2,G2,B2])
    pixel.setColor(6,6,[R2,G2,B2])

#------------------ Pixel Car Moving ------------------- 

def pixel_car_action(R1,G1,B1,R2,G2,B2,V): 

    pixel.clear()
    pixel_car(R1,G1,B1,R2,G2,B2)
    time.sleep(V)
    pixel.clear()
    time.sleep(V)
    
#------------------ Car Speed with Pixel------------------- 

def car_move(R1,G1,B1,R2,G2,B2):
    n =0
    while True :
        if n == 0 and dis < 20 :
            n = 1
            pixel.clear()
            pixel_car(R1,G1,B1,R2,G2,B2)

        if 20 <= dis < 80  :
            n = 0
            V = 0.4
            pixel_car_action(R1,G1,B1,R2,G2,B2,V)

        if dis >= 80  :
            n = 0
            V = 0.1
            pixel_car_action(R1,G1,B1,R2,G2,B2,V)

#--------------------- pixel func call ----------------------------

threading.Thread(target=car_move, args=(R1,G1,B1,R2,G2,B2)).start()

#------------------ connection with blynk -------------------------------------------------

blynk = BlynkLib.Blynk('EHMNNcBg45zgOR-NpFtcrtGmVe8FfIz1', server='127.0.0.1', port='8080')

 #------------------ Place to go with Dict -------------------------------

city = {'ulsan': 2000, 'seoul': 1000, 'Hwaii': 3000, 'cheonan':500, 'sejong':300 }
city_name_input = 0
leds = Leds()
pb = PiezoBuzzer()
K = 0

#------------ compre with input & dict ------------------------------------

def city_name_check(city_name_input, city):

    if city_name_input in city.keys():
        return city_name_input

    elif city_name_input not in city.keys():
        print('목적지를 다시 입력해 주세요')
        return 0

#------------ pds data get ----------------------------------------------

def data_read_and_leds_action(city, city_name_input):

    global K
    global dis
    

    if city_name_input :

        res = []

        for i in range(city[city_name_input]):
            
            val = psd.readAverage()
            dis = round(psd.calcDist(val), 2)
            blynk.virtual_write(1,dis)
                           
            if K == 0 :

                threading.Thread(target=leds_action).start()

            res.append(dis)
        
        return res

#---------pds state monitoring with led, buzzer---------------------------------

def leds_action():

    global K

    if dis < 20:

        K = 1            
        leds.allOn()
        pb.tone(5, 8, 1)
        time.sleep(0.1)
        K = 0
                    
    elif 20<= dis < 80:

        K = 1
        for _ in range(5):
            leds.allOn()
            pb.tone(4, 8, 4)
            time.sleep(0.1)
            leds.allOff()
            pb.tone(4, 8, 4)
            time.sleep(0.1)
        K = 0

    else:
        leds.allOff()

#---------------------- blynk input ----------------------------------------

@blynk.VIRTUAL_WRITE(0)
def text_input(n):

    global city_name_input
    global city

    city_name_input = n[0]
    city_name_input = city_name_check(city_name_input, city)

#--------------------- car monitoring --------------------------------------

@blynk.VIRTUAL_READ(1)
def car():

    global city_name_input
    global city
    global dis
       
    res = data_read_and_leds_action(city, city_name_input) 

    time.sleep(0.5)
        
    #------------------ cvs_file with Pandas--------------------------------------------- 

    if city_name_input in city.keys():

        data_frame = pd.DataFrame(res)
        data_frame.to_csv('/home/soda/Project/python/testSource/file101.csv', header= ['Psd_data'], index = False)
        
    #------------------ reset variable --------------------------------------------------

        print('운행 종료')
        print('편안한 운행 되셨습니까? 저희 운행사는 언제나 고객님을 위하여 최선을 다하겠습니다. 안녕히 가십쇼')

        dis = 0
        city_name_input = 0
            
#----------- Practical run ------------------

while True:
    blynk.run()
    car()
<pre>
<code>
