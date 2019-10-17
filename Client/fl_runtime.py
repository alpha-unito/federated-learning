import requests 
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("topic/fl")

def on_message(client, userdata, msg):
  if msg.payload.decode() == "Hello world!":
    print("Yes!")
    client.disconnect()

# MQTT CLIENT CONNECTION TO MESSAGE BROKER
client = mqtt.Client()
client.connect("localhost", 1883, 60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
# client.disconnect()

# api-endpoint 
URL = "http://127.0.0.1:5002/selector"

def device_connection_to_server():
    client.publish("topic/fl", "Hello world!");
