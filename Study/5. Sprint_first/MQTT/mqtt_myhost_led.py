import paho.mqtt.client as mqtt
import threading
import json
import Xpop


def say_pulish(client): # 따로 만들어 줘도 됨.
    led_info = {'id': None, 'led':None, 'action':None}

    led_info['id'] = int(input("Select Id : "))    
    led_info['led'] = int(input('LED : '))   
    led_info['action'] = input('Action : ')
    client.publish("Soda/led/action", json.dumps(led_info))
    
def go_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Perfect Way to Connect")
        client.subscribe("SODA/led/state")
        threading.Thread(target=say_pulish, args=(client,)).start()
       
    else:
        print("Wrong Way to Connect")
    
def go_disconnect(client, userdata, flags, rc=0):
    print(str(rc))

def go_publish(client, userdata, mid):
    threading.Thread(target=say_pulish, args=(client,)).start()
    
def do_message(client, usrdata, message):
    print(' ' * 20, "<<<", message.payload.decode())


def main():
    client = mqtt.Client()
    client.on_connect = go_connect
    client.on_disconnect = go_disconnect
    client.on_publish = go_publish
    client.on_message = do_message
    client.connect("192.168.101.101")  #실제 브로커 주소 사용
    client.loop_forever()
#client.loop_stop() # 스크립트를 빠져나갈 때 loop의 사1

if __name__ == "__main__":
    main()
