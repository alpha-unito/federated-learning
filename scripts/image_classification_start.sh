#!/bin/bash

echo "Starting Image Classification task"

eval "$(conda shell.bash hook)"

conda activate tff;
cd /home/lmancuso/federated-learning/ImageClassification/
nohup python3 -u task.py > ../log.txt &