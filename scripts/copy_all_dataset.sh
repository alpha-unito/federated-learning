PROXY="lmancuso@130.192.137.199"
CERT_PATH="/home/lore/Scaricati/mancuso_federated"

# 2) copia dei file richiesti tramite sync
COMMAND="ssh -i $CERT_PATH -J $PROXY"

# dataset node01
rsync -azv --append-verify --stats --human-readable --info=progress2 -e "$COMMAND" /home/lore/Projects/res/subset01/ lmancuso@node01:/home/lmancuso/federated-learning/res
# dataset node02
rsync -azv --append-verify --stats --human-readable --info=progress2 -e "$COMMAND" /home/lore/Projects/res/subset02/ lmancuso@node02:/home/lmancuso/federated-learning/res
# dataset node03
rsync -azv --append-verify --stats --human-readable --info=progress2 -e "$COMMAND" /home/lore/Projects/res/subset03/ lmancuso@node03:/home/lmancuso/federated-learning/res
# dataset node04
rsync -azv --append-verify --stats --human-readable --info=progress2 -e "$COMMAND" /home/lore/Projects/res/subset04/ lmancuso@node04:/home/lmancuso/federated-learning/res
