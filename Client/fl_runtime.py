import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("topic/fl-broadcast")


def on_message(client, userdata, msg):
    print("received")
    if msg.payload.decode() == "Hello world!":
        print("Yes!")
        client.disconnect()

# MQTT CLIENT CONNECTION TO MESSAGE BROKER
client = mqtt.Client()
client.connect("localhost", 1883, 60)

client.on_connect = on_connect
client.on_message = on_message

def device_connection_to_server():
    client.publish("topic/fl-broadcast", "Hello world!");
    print("published message to 'topic/fl-broadcast'")
    # client.loop_forever()
