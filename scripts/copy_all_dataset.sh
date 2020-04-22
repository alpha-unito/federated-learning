PROXY="lmancuso@130.192.137.199"
CERT_PATH="/home/lore/Scaricati/mancuso_federated"

# 2) copia dei file richiesti tramite sync
COMMAND="ssh -i $CERT_PATH -J $PROXY"

# validation set coordinator
rsync -azv --append-verify --stats --human-readable --info=progress2 -e "$COMMAND" /media/lore/EA72A48772A459D9/ILSVRC2012/ILSVRC2012_img_val lmancuso@coordinator:~/federated-learning/Server/res/

# dataset node01
rsync -azv --append-verify --stats --human-readable --info=progress2 -e "$COMMAND" /media/lore/EA72A48772A459D9/ILSVRC2012/ILSVRC2012_img_train/subset01 lmancuso@node01:/mnt/dataset/
# dataset node02
rsync -azv --append-verify --stats --human-readable --info=progress2 -e "$COMMAND" /media/lore/EA72A48772A459D9/ILSVRC2012/ILSVRC2012_img_train/subset02 lmancuso@node02:/mnt/dataset/
# dataset node03
rsync -azv --append-verify --stats --human-readable --info=progress2 -e "$COMMAND" /media/lore/EA72A48772A459D9/ILSVRC2012/ILSVRC2012_img_train/subset03 lmancuso@node03:/mnt/dataset/
# dataset node04
rsync -azv --append-verify --stats --human-readable --info=progress2 -e "$COMMAND" /media/lore/EA72A48772A459D9/ILSVRC2012/ILSVRC2012_img_train/subset04 lmancuso@node04:/mnt/dataset/
