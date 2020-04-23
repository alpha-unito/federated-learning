PROXY="lmancuso@130.192.137.199"
CERT_PATH="/home/lore/Scaricati/mancuso_federated"

REMOVE_COMMAND="rm -rf ~/federated-learning"
COMMAND="ssh -i $CERT_PATH -J $PROXY"

# coordinator
ssh -i $CERT_PATH -J $PROXY lmancuso@coordinator $REMOVE_COMMAND
rsync -azv --append-verify --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" -e "$COMMAND" /home/lore/Projects/federated-learning lmancuso@coordinator:/home/lmancuso/

# node01
ssh -i $CERT_PATH -J $PROXY lmancuso@node01 $REMOVE_COMMAND
rsync -azv --append-verify --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" -e "$COMMAND" /home/lore/Projects/federated-learning lmancuso@node01:/home/lmancuso/

# node02
ssh -i $CERT_PATH -J $PROXY lmancuso@node02 $REMOVE_COMMAND
rsync -azv --append-verify --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" -e "$COMMAND" /home/lore/Projects/federated-learning lmancuso@node02:/home/lmancuso/

# node03
ssh -i $CERT_PATH -J $PROXY lmancuso@node03 $REMOVE_COMMAND
rsync -azv --append-verify --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" -e "$COMMAND" /home/lore/Projects/federated-learning lmancuso@node03:/home/lmancuso/

# node04
ssh -i $CERT_PATH -J $PROXY lmancuso@node04 $REMOVE_COMMAND
rsync -azv --append-verify --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" -e "$COMMAND" /home/lore/Projects/federated-learning lmancuso@node04:/home/lmancuso/
