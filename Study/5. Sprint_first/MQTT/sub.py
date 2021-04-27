import paho.mqtt.client as mqtt

def get_connection(client, userdata, flags, rc):
    if rc == 0:
        print('Perfect Way to Connect')
        client.subscribe("Soda/Hello")
    else:
        print('Wrong Way to Connect', rc)

def go_disconnect(client, userdata, flags, rc=0):
    print(str(rc))

def get_message(client, userdata, message):
    print("[%s] %s"%(message.topic, message.payload.decode()))

client = mqtt.Client()
client.on_connect = get_connection
client.on_disconnect = go_disconnect
client.on_message = get_message
client.connect("192.168.101.101")  

client.loop_forever()