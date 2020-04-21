#!/bin/bash

echo "Starting Client in async mode"

~/anaconda3/bin/conda activate tff;
cd ~/federated-learning/Client/
nohup python3 -u app.py > ../log.txt &