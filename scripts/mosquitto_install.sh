#!/bin/bash

sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa -y
sudo apt-get update
sudo apt-get install mosquitto -y
sudo apt-get install mosquitto-clients -y
