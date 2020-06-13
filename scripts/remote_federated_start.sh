## !! NOT WORKING !!

PROXY="lmancuso@130.192.137.199"
CERT_PATH="/home/lore/Scaricati/mancuso_federated"

# node01
echo "start node01"
ssh -i $CERT_PATH -J $PROXY lmancuso@node01 "bash ~/federated-learning/scripts/client_start.sh"

# node02
echo "start node02"
ssh -i $CERT_PATH -J $PROXY lmancuso@node02 "bash ~/federated-learning/scripts/client_start.sh"

# node03
echo "start node03"
ssh -i $CERT_PATH -J $PROXY lmancuso@node03 "bash ~/federated-learning/scripts/client_start.sh"

# node04
echo "start node04"
ssh -i $CERT_PATH -J $PROXY lmancuso@node04 "bash ~/federated-learning/scripts/client_start.sh"

# coordinator
#echo "start coordinator"
#ssh -i $CERT_PATH -J $PROXY lmancuso@coordinator "bash ~/federated-learning/scripts/server_start.sh"


ssh -i "/home/lore/Scaricati/mancuso_federated" -J "lmancuso@130.192.137.199" lmancuso@device12 "bash ~/federated-learning/scripts/client_start.sh"


ssh -i "/home/lore/Scaricati/mancuso_federated" -J "lmancuso@130.192.137.199" lmancuso@device12 ". ~/.bashrc; conda activate tff; cd ~/federated-learning/Client; nohup python3 -u app.py > ../log.txt &"

