PROXY="lmancuso@130.192.137.199"
CERT_PATH="/home/lore/Scaricati/mancuso_federated"

# coordinator
ssh -i $CERT_PATH -J $PROXY lmancuso@coordinator "cd federated-learning; bash scripts/conda_install.sh"
ssh -i $CERT_PATH -J $PROXY lmancuso@coordinator "cd federated-learning; bash scripts/mosquitto_install.sh"

# node01
ssh -i $CERT_PATH -J $PROXY lmancuso@node01 "cd federated-learning; bash scripts/conda_install.sh"
ssh -i $CERT_PATH -J $PROXY lmancuso@node01 "cd federated-learning; bash scripts/mosquitto_install.sh"

# node02
ssh -i $CERT_PATH -J $PROXY lmancuso@node02 "cd federated-learning; bash scripts/conda_install.sh"
ssh -i $CERT_PATH -J $PROXY lmancuso@node02 "cd federated-learning; bash scripts/mosquitto_install.sh"

# node03
ssh -i $CERT_PATH -J $PROXY lmancuso@node03 "cd federated-learning; bash scripts/conda_install.sh"
ssh -i $CERT_PATH -J $PROXY lmancuso@node03 "cd federated-learning; bash scripts/mosquitto_install.sh"

# node04
ssh -i $CERT_PATH -J $PROXY lmancuso@node04 "cd federated-learning; bash scripts/conda_install.sh"
ssh -i $CERT_PATH -J $PROXY lmancuso@node04 "cd federated-learning; bash scripts/mosquitto_install.sh"
