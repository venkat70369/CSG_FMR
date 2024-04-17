import time
import paho.mqtt.client as mqtt
import ssl
import json
import threading

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

client = mqtt.Client()
client.on_connect = on_connect
client.tls_set(
    ca_certs='./rootCA.pem',
    certfile='./certificate.pem.crt',
    keyfile='./private.pem.key',
    tls_version=ssl.PROTOCOL_SSLv23
)
client.tls_insecure_set(True)
client.connect("a3l8nxwg4yj1h6-ats.iot.ap-south-1.amazonaws.com", 8883, 60)  # Taken from REST API endpoint - Use your own.

while True:
    print('Published Successfully')
    integer_values = [1, 2, 3, 4]
    for value in integer_values:
        data = str(value)
        client.publish("aws_1", payload=data, qos=0, retain=False)
        time.sleep(2)
