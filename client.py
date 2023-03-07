import cv2 
import paho.mqtt.client as mqtt 
import base64 
from components.detector import Detector
from components.draw import Draw
from components.bbox import BBOX
import json


MQTT_BROKER = "0.0.0.0"
MQTT_SEND1 = "/streaming"
MQTT_SEND2 = "/data"

cap = cv2.VideoCapture(0)

client1 = mqtt.Client()
client2 = mqtt.Client()
client1.connect(MQTT_BROKER)
client2.connect(MQTT_BROKER)

try:
    while True:
        ret, frame = cap.read()
        results = Detector(frame)
        for object in results:
            box = BBOX(object)
            frame = Draw(frame, box)
        name = "ramma"

        dictionary = {
            "name":str(name),
            "x": str(box.xywh[0]),
            "y": str(box.xywh[1]),
            "w": str(box.xywh[2]),
            "h": str(box.xywh[3])
        }
        data = json.dumps(dictionary)
        print(data)

        _, buffer = cv2.imencode('.jpg', frame)
        jpg_as_text = base64.b64encode(buffer)
        client1.publish(MQTT_SEND1, jpg_as_text)
        client2.publish(MQTT_SEND2, data)
except:
    cap.release()
    client1.disconnect()
    client2.disconnect()