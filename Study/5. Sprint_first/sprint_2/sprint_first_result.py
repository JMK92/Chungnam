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

#------------ compre with input & dict ------------------------------------
def city_name_check(city_name_input, city):

    if city_name_input in city.keys():
        return city_name_input

    elif city_name_input not in city.keys():
        print('목적지를 다시 입력해 주세요')
        return 0

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
    global dis
    global psd
    global city_name_input
    global city
    
    leds = Leds()
    pb = PiezoBuzzer()
       
    res = [] # -> for append

    #------------------ dis with Led, buzzer--------------------------------- 
    if city_name_input :

        for i in range(city[city_name_input]):
            
            val = psd.readAverage()
            dis = round(psd.calcDist(val), 2)
            blynk.virtual_write(1,dis)

            if dis < 20:            
                leds.allOn()
                #pb.tone(5, 8, 1)
                time.sleep(0.1)
                    
            elif 20<= dis < 80:
                for _ in range(5):
                    leds.allOn()
                    #pb.tone(4, 8, 4)
                    time.sleep(0.1)
                    leds.allOff()
                    #pb.tone(4, 8, 4)
                    time.sleep(0.1)
            else:
                leds.allOff()
                
            #-------- each dis_data in list ----------------------
            res.append(dis)
    
        time.sleep(0.5)
        
        #------------------ cvs_file with Pandas--------------------------------------------- 
        data_frame = pd.DataFrame(res)
        data_frame.to_csv('/home/soda/Project/python/testSource/file101.csv', header= ['Psd_data'], index = False)
        
        #------------------ reset variable --------------------------------------------------
        dis = 0
        city_name_input = 0

        print('운행 종료')
        print('편안한 운행 되셨습니까? 저희 운행사는 언제나 고객님을 위하여 최선을 다하겠습니다. 안녕히 가십쇼')
            
#----------- Practical run ------------------
while True:
    blynk.run()
    car()