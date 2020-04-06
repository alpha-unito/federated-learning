import paho.mqtt.client as mqtt
import threading
import json


def on_connect(client, userdata, flags, rc):
    print("\nConnected with result code {code} to topic 'topic/fl-update' \n".format(code = rc))
    print('subscribe', client.subscribe("topic/fl-update"))


def on_message(client, userdata, msg):
    print("\nNew message received ")



print('Init client update MQTT listener')

# MQTT CLIENT CONNECTION TO MESSAGE BROKER
client = mqtt.Client(userdata = {})

client.connect('localhost', 1883, 60)

client.on_connect = on_connect
client.on_message = on_message

print("Start listening on MQTT channel ...")
client.loop_forever()
print("End listening on MQTT channel.")
