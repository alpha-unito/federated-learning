PROXY="lmancuso@130.192.137.199"
CERT_PATH="/home/lore/Scaricati/mancuso_federated"

REMOVE_COMMAND="rm -rf ~/federated-learning"
COMMAND="ssh -o StrictHostKeyChecking=no -i $CERT_PATH -J $PROXY"

# coordinator
#rsync -azv --append-verify --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" -e "$COMMAND" /home/lore/Projects/federated-learning lmancuso@coordinator:/home/lmancuso/



rsync -azv -I --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning/Client/ lmancuso@node01:/home/lmancuso/federated-learning/Client/
rsync -azv -I --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning/Client/ lmancuso@node02:/home/lmancuso/federated-learning/Client/
rsync -azv -I --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning/Client/ lmancuso@node03:/home/lmancuso/federated-learning/Client/
rsync -azv -I --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning/Client/ lmancuso@node04:/home/lmancuso/federated-learning/Client/
rsync -azv -I --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning/Client/ lmancuso@device1:/home/lmancuso/federated-learning/Client/
rsync -azv -I --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning/Client/ lmancuso@device2:/home/lmancuso/federated-learning/Client/
rsync -azv -I --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning/Client/ lmancuso@device3:/home/lmancuso/federated-learning/Client/
rsync -azv -I --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning/Client/ lmancuso@device4:/home/lmancuso/federated-learning/Client/
rsync -azv -I --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning/Client/ lmancuso@device5:/home/lmancuso/federated-learning/Client/
rsync -azv -I --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning/Client/ lmancuso@device6:/home/lmancuso/federated-learning/Client/
rsync -azv -I --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning/Client/ lmancuso@device7:/home/lmancuso/federated-learning/Client/
rsync -azv -I --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning/Client/ lmancuso@device8:/home/lmancuso/federated-learning/Client/
rsync -azv -I --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning/Client/ lmancuso@device9:/home/lmancuso/federated-learning/Client/
rsync -azv -I --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning/Client/ lmancuso@device10:/home/lmancuso/federated-learning/Client/
rsync -azv -I --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning/Client/ lmancuso@device11:/home/lmancuso/federated-learning/Client/
rsync -azv -I --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning/Client/ lmancuso@device12:/home/lmancuso/federated-learning/Client/
rsync -azv -I --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning/Client/ lmancuso@device13:/home/lmancuso/federated-learning/Client/
rsync -azv -I --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning/Client/ lmancuso@device14:/home/lmancuso/federated-learning/Client/
rsync -azv -I --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning/Client/ lmancuso@device15:/home/lmancuso/federated-learning/Client/
rsync -azv -I --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning/Client/ lmancuso@device16:/home/lmancuso/federated-learning/Client/
rsync -azv -I --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning/Client/ lmancuso@device17:/home/lmancuso/federated-learning/Client/
rsync -azv -I --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning/Client/ lmancuso@device18:/home/lmancuso/federated-learning/Client/
rsync -azv -I --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning/Client/ lmancuso@device19:/home/lmancuso/federated-learning/Client/
rsync -azv -I --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning/Client/ lmancuso@device20:/home/lmancuso/federated-learning/Client