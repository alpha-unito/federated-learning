#!/bin/bash

echo "Starting Client in async mode"

~/anaconda3/bin/conda activate tff;
cd ~/federated-learning/Server/
nohup python3 -u main.py > ../log.txt &