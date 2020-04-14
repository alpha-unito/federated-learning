NODE="lmancuso@coordinator"
PROXY="lmancuso@130.192.137.199"
CERT_PATH="/home/lore/Scaricati/mancuso_federated"
SUBSET_FOLDER="subfolder"

# 2) copia dei file richiesti tramite sync
COMMAND="ssh -i $CERT_PATH -J $PROXY"
# project
rsync -azv --append-verify --stats --human-readable --info=progress2 --exclude=".*" -e "$COMMAND" /home/lore/Projects/federated-learning $NODE:/home/lmancuso/

# dataset
#rsync -azv --append-verify --stats --human-readable --info=progress2 -e 'ssh -i $CERT_PATH -J $PROXY' /home/lore/Projects/res/$SUBSET_FOLDER/ $NODE:/home/lmancuso/federated-learning/res

# 1) connessione ssh alla macchina virtuale
ssh -i $CERT_PATH -J $PROXY $NODE "cd federated-learning; bash scripts/conda_install.sh"
