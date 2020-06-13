#!/bin/bash

echo "Starting Client in async mode"

eval "$(conda shell.bash hook)"

conda activate tff;
cd ~/federated-learning/Client/
nohup python3 -u app.py > ../log.txt &