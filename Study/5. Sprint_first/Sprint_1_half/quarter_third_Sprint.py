from pop import Psd, Leds, PixelDisplay, PiezoBuzzer
import time
import BlynkLib
import pandas as pd
import threading
#------------------ Pixel V----------------------------- 
pixel =PixelDisplay()
dis = Psd()
ret = 0

R = 0
G = 0
B = 255

#------------------ Pixel Car Shape ------------------- 
def pixel_car(R ,G ,B):
    
    pixel.setColor(1,6,[139,69,19])
    pixel.setColor(2,5,[139,69,19])
    pixel.setColor(2,6,[139,69,19])
    pixel.setColor(2,7,[139,69,19])
    pixel.setColor(3,6,[139,69,19])
    pixel.setColor(4,6,[139,69,19])
    pixel.setColor(5,5,[139,69,19])
    pixel.setColor(5,6,[139,69,19])
    pixel.setColor(5,7,[139,69,19])
    pixel.setColor(6,6,[139,69,19])
    pixel.setColor(2,1,[R,G,B])
    pixel.setColor(2,2,[R,G,B])
    pixel.setColor(3,1,[R,G,B])
    pixel.setColor(3,2,[R,G,B])
    pixel.setColor(4,1,[R,G,B])
    pixel.setColor(4,2,[R,G,B])
    pixel.setColor(5,1,[R,G,B])
    pixel.setColor(5,2,[R,G,B])
    pixel.setColor(0,3,[R,G,B])
    pixel.setColor(0,4,[R,G,B])
    pixel.setColor(1,3,[R,G,B])
    pixel.setColor(1,4,[R,G,B])
    pixel.setColor(2,3,[R,G,B])
    pixel.setColor(2,4,[R,G,B])
    pixel.setColor(3,3,[R,G,B])
    pixel.setColor(3,4,[R,G,B])
    pixel.setColor(4,3,[R,G,B])
    pixel.setColor(4,4,[R,G,B])
    pixel.setColor(5,3,[R,G,B])
    pixel.setColor(5,4,[R,G,B])
    pixel.setColor(6,3,[R,G,B])
    pixel.setColor(6,4,[R,G,B])
    pixel.setColor(7,3,[R,G,B])
    pixel.setColor(7,4,[R,G,B])

#------------------ Pixel Car Moving ------------------- 
def pixel_car_action(R,G,B,V): 

    pixel.clear()
    pixel_car(R,G,B)
    time.sleep(V)
    pixel.clear()
    time.sleep(V)
    
#------------------ Car Speed with Pixel------------------- 
def car_move(R, G, B):

    n =0

    while True :
        
        if n == 0 and ret < 20 :

            n = 1

            pixel.clear()
            pixel_car(R, G, B)

        if 20 <= ret < 80  :

            n = 0
            V = 0.4

            pixel_car_action(R, G, B, V)

        if ret >= 80  :

            n = 0
            V = 0.1

            pixel_car_action(R, G, B, V)


threading.Thread(target=car_move, args=(R,G,B)).start()

blynk = BlynkLib.Blynk('EHMNNcBg45zgOR-NpFtcrtGmVe8FfIz1', server='127.0.0.1', port='8080')

# blynk와 
@blynk.VIRTUAL_READ(1)
def car():
    global ret
    global dis
    leds = Leds()
    pb = PiezoBuzzer()
    
    #------------------ Place to go with Dict -------------------------
    city = {'ulsan': 1000, 'Seoul': 500, 'Hwaii': 2000 }
    x = input('도시는 : ')
    res = []
    #------------------ Led with Speed--------------------------------- 
    for i in range(city[x]):
        
        val = dis.readAverage()
        ret = round(dis.calcDist(val), 2)
        blynk.virtual_write(1,ret)

        if ret < 20:            
            leds.allOn()
            #pb.
                  
        elif 20<= ret < 80:
            for _ in range(5):
                leds.allOn()
                time.sleep(0.1)
                leds.allOff()
                time.sleep(0.1)
        else:
            leds.allOff()
            
        
        res.append(ret)
    #print(len(res), res)
    time.sleep(0.5)
    #------------------ cvs_file with Pandas--------------------------------------------- 
    data_frame = pd.DataFrame(res)
    #print(data_frame)
    data_frame.to_csv('/home/soda/Project/python/testSource/file101.csv', header= ['Psd_data'], index = False)
    ret = 0
    print('운행 종료')
    print('편안한 운행 되셨습니까? 저희 운행사는 언제나 고객님을 위하여 최선을 다하겠습니다. 안녕히 가십쇼')
              
i = 0
while i < 1:
    blynk.run()
    car()
    i += 1