#!/bin/bash

echo "Starting Image Classification task in async mode"

~/anaconda3/bin/conda activate tff;
cd ~/federated-learning/ImageClassification/
nohup python3 -u task.py > ../log.txt &