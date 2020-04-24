#!/bin/bash

echo "Starting Client in async mode"

eval "$(conda shell.bash hook)"

conda activate tff;
cd ~/federated-learning/Server/
nohup python3 -u main.py > ../log.txt &