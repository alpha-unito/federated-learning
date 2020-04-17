#!/usr/bin/env python3

import paho.mqtt.client as mqtt

# This is the Publisher
if __name__ == "__main__":
    client = mqtt.Client()
    client.connect("localhost",1883,60)
    client.publish("topic/fl-update", "Hello world!", 0);
    client.disconnect();