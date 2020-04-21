PROXY="lmancuso@130.192.137.199"
CERT_PATH="/home/lore/Scaricati/mancuso_federated"

# coordinator
ssh -i $CERT_PATH -J $PROXY lmancuso@coordinator "bash ~/federated-learning/scripts/server_start.sh"

# node01
ssh -i $CERT_PATH -J $PROXY lmancuso@node01 "bash ~/federated-learning/scripts/client_start.sh"

# node02
ssh -i $CERT_PATH -J $PROXY lmancuso@node02 "bash ~/federated-learning/scripts/client_start.sh"

# node03
ssh -i $CERT_PATH -J $PROXY lmancuso@node03 "bash ~/federated-learning/scripts/client_start.sh"

# node04
ssh -i $CERT_PATH -J $PROXY lmancuso@node04 "bash ~/federated-learning/scripts/client_start.sh"
