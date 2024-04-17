import time
import json
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

myMQTTClient = AWSIoTMQTTClient("Data")
myMQTTClient.configureEndpoint("a3l8nxwg4yj1h6-ats.iot.ap-south-1.amazonaws.com", 8883)
myMQTTClient.configureCredentials("rootCA.pem", "private.pem.key", "certificate.pem.crt")

print("Initiating IoT Core Topic...")
print("Subscribing to topic")
myMQTTClient.connect()

def callback(self, params, packet):
    payload = packet.payload.decode('utf-8')
    print("Payload:", payload)



myMQTTClient.subscribe("aws_csg", 1,callback)

while True:
     time.sleep(2)