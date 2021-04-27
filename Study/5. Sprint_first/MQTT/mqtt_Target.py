import paho.mqtt.client as mqtt
import subprocess
import json

id = None

def do_connect(client, usrdata, flags, rc):
    if rc == 0:
        print("ok connect")
        client.subscribe("SODA/led/action") 
    else:
        print("not connect")

def do_message(client, usrdata, message):
    led_info = json.loads(message.payload)

    if id != led_info['id']:
        return
        
    if led_info['action'] == 'on':
        print('led on')
        # ref led_info['led']
    elif led_info['action'] == 'off':
        print('led off')
        # ref led_info['led']
        
    client.publish("SODA/led/state", "id:%d, led:%d, state:%s"%(id, led_info['led'], led_info['action']))

def main():
    global id

    id = int(input("input your id: "))

    client = mqtt.Client()
    client.on_connect = do_connect
    client.on_message = do_message
    client.connect("192.168.101.101") 
    client.loop_forever()

if __name__ == "__main__":
    main()