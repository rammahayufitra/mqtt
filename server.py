import base64 
import cv2 
import numpy as np
import json
import paho.mqtt.client as mqtt 

MQTT_BROKER = "0.0.0.0"
MQTT_RECEIVE1 = "/streaming"
MQTT_RECEIVE2 = "/data"

frame = np.zeros((640, 320, 3), np.uint8)


def on_connect1(client,userdata, flags, rc):
    print("terkoneksi "+str(rc))
    client.subscribe(MQTT_RECEIVE1)

def on_message1(client,userdata, msg):
    global frame
    img = base64.b64decode(msg.payload)
    npimg = np.frombuffer(img, dtype=np.uint8)
    frame = cv2.imdecode(npimg, 1)
    

def on_connect2(client,userdata, flags, rc):
    print("terkoneksi "+str(rc))
    client.subscribe(MQTT_RECEIVE2)

def on_message2(client,userdata, msg):
    print(msg.payload.decode())
    
client1 = mqtt.Client()
client1.on_connect = on_connect1 
client1.on_message = on_message1

client2 = mqtt.Client()
client2.on_connect = on_connect2 
client2.on_message = on_message2

client1.connect(MQTT_BROKER)
client2.connect(MQTT_BROKER)
client1.loop_start()
client2.loop_start()

while True:
    cv2.imshow("from client", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 

client1.loop_stop()
client2.loop_stop()