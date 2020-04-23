#!/bin/bash

# 3) import dell ambiente conda
curl -O https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
bash Anaconda3-2020.02-Linux-x86_64.sh -b -p $HOME/anaconda3

rm -rf Anaconda3-2020.02-Linux-x86_64.sh

~/anaconda3/bin/conda init bash

# 4) activate environment
~/anaconda3/bin/conda update conda -y
~/anaconda3/bin/conda env create -f tff.yml 
~/anaconda3/bin/conda activate tff

# 5) lancio di un nuovo client eseguendo lo script in maniera indipente
#bash start_client.sh