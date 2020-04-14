#!/bin/bash

echo "Starting Image Classification task"

~/anaconda3/bin/conda activate tff;
cd ~/federated-learning/ImageClassification/
nohup python3 -u task.py > ../log.txt &