PROXY="lmancuso@130.192.137.199"
CERT_PATH="/home/lore/Scaricati/mancuso_federated"

REMOVE_COMMAND="rm -rf ~/federated-learning"
COMMAND="ssh -o StrictHostKeyChecking=no -i $CERT_PATH -J $PROXY"

# coordinator
#ssh -i $CERT_PATH -J $PROXY lmancuso@coordinator $REMOVE_COMMAND
#rsync -azv --append-verify --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" -e "$COMMAND" /home/lore/Projects/federated-learning lmancuso@coordinator:/home/lmancuso/



# node01
#ssh -i $CERT_PATH -J $PROXY lmancuso@node01 $REMOVE_COMMAND
#rsync -azv -I --ignore-times --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning lmancuso@node01:/home/lmancuso/

# node02
#ssh -i $CERT_PATH -J $PROXY lmancuso@node02 $REMOVE_COMMAND
#rsync -azv -I --ignore-times --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning lmancuso@node02:/home/lmancuso/

# node03
#ssh -i $CERT_PATH -J $PROXY lmancuso@node03 $REMOVE_COMMAND
#rsync -azv -I --ignore-times --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning lmancuso@node03:/home/lmancuso/

# node04
#ssh -i $CERT_PATH -J $PROXY lmancuso@node04 $REMOVE_COMMAND
#rsync -azv -I --ignore-times --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning lmancuso@node04:/home/lmancuso/


#rsync -azv -I --ignore-times --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "ssh -i /home/lore/Scaricati/mancuso_federated -J lmancuso@130.192.137.199" /home/lore/Projects/federated-learning/tff.yml lmancuso@device1:/home/lmancuso/federated-learning/


## device01
#ssh -i $CERT_PATH -J $PROXY lmancuso@device01 $REMOVE_COMMAND
#rsync -azv -I --ignore-times --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning lmancuso@device1:/home/lmancuso/
#
## device02
#ssh -i $CERT_PATH -J $PROXY lmancuso@device02 $REMOVE_COMMAND
#rsync -azv -I --ignore-times --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning lmancuso@device2:/home/lmancuso/
#
## device03
#ssh -i $CERT_PATH -J $PROXY lmancuso@device03 $REMOVE_COMMAND
#rsync -azv -I --ignore-times --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning lmancuso@device3:/home/lmancuso/
#
## device04
#ssh -i $CERT_PATH -J $PROXY lmancuso@device04 $REMOVE_COMMAND
#rsync -azv -I --ignore-times --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning lmancuso@device4:/home/lmancuso/




#rsync -azv -I --ignore-times --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning lmancuso@device5:/home/lmancuso/
#rsync -azv -I --ignore-times --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning lmancuso@device6:/home/lmancuso/
#rsync -azv -I --ignore-times --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning lmancuso@device7:/home/lmancuso/
#rsync -azv -I --ignore-times --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning lmancuso@device8:/home/lmancuso/
#rsync -azv -I --ignore-times --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning lmancuso@device9:/home/lmancuso/
#rsync -azv -I --ignore-times --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning lmancuso@device10:/home/lmancuso/
#rsync -azv -I --ignore-times --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning lmancuso@device11:/home/lmancuso/
#rsync -azv -I --ignore-times --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning lmancuso@device12:/home/lmancuso/
#rsync -azv -I --ignore-times --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning lmancuso@device13:/home/lmancuso/
#rsync -azv -I --ignore-times --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning lmancuso@device14:/home/lmancuso/
#rsync -azv -I --ignore-times --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning lmancuso@device15:/home/lmancuso/
#rsync -azv -I --ignore-times --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning lmancuso@device16:/home/lmancuso/
#rsync -azv -I --ignore-times --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning lmancuso@device17:/home/lmancuso/
#rsync -azv -I --ignore-times --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning lmancuso@device18:/home/lmancuso/
#rsync -azv -I --ignore-times --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning lmancuso@device19:/home/lmancuso/
#rsync -azv -I --ignore-times --stats --human-readable --info=progress2 --exclude=".*" --exclude="res" --exclude="__pycache__" -e "$COMMAND" /home/lore/Projects/federated-learning lmancuso@device20:/home/lmancuso/
