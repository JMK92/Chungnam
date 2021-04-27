import paho.mqtt.client as mqtt
import subprocess
import json
import Xpop

id = None

def get_connection(client, userdata, flags, rc):
    if rc == 0:
        print('Perfect Way to Connect')
        client.subscribe("Soda/led/action")
    else:
        print('Wrong Way to Connect')

def go_disconnect(client, userdata, flags, rc=0):
    print(str(rc))

def get_message(client, userdata, message):
    led_info = json.loads(message.payload)
    
    if id != led_info['id']:
        return
          
    if led_info['action'] == 'on':
        print('led on')
        Xpop.light(led_info['led'], 'on')
    elif led_info['action'] == 'off':
        print('led off')
        Xpop.light(led_info['led'], 'off')
    client.publish("SODA/led/state","id:%d, led:%d, state:%s"%(id, led_info['led'], led_info['action']))

def main():
    global id
    id = int(input('input your id : '))
    
    client = mqtt.Client()
    client.on_connect = get_connection
    client.on_disconnect = go_disconnect
    client.on_message = get_message
    client.connect("192.168.101.101")  

    client.loop_forever()
if __name__ == "__main__":
    main()