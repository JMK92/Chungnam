import paho.mqtt.client as mqtt

def say_pulish(): # 따로 만들어 줘도 됨.
    mes = input('Talk : ')
    client.publish("Soda/Hello", mes)
    
def go_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Perfect Way to Connect")
        say_pulish()
    else:
        print("Wrong Way to Connect", rc)
    
def go_disconnect(client, userdata, flags, rc=0):
    print(str(rc))

def go_publish(client, userdata, mid):
    print("Welcome")
    say_pulish()


client = mqtt.Client()

client.on_connect = go_connect
client.on_disconnect = go_disconnect
client.on_publish = go_publish
client.connect("192.168.101.101")  #실제 브로커 주소 사용
client.loop_forever()
#client.loop_stop() # 스크립트를 빠져나갈 때 loop의 사용을 멈춰야 한다.