#!/bin/bash

# 3) import dell ambiente conda
bash Anaconda3-2020.02-Linux-x86_64.sh -yml
source .bashrc
conda update conda

# 4) activate environment
cd federated-learning
conda create env -f tff.yml 
conda activate tff

# 5) lancio di un nuovo client eseguendo lo script in maniera indipente
#bash start_client.sh