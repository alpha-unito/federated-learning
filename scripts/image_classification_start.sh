#!/bin/bash

echo "Starting Image Classification task in async mode"

eval "$(conda shell.bash hook)"

conda activate tff;
cd ~/federated-learning/ImageClassification/
nohup python3 -u task.py > ../log.txt &