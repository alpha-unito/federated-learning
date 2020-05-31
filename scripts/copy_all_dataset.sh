PROXY="lmancuso@130.192.137.199"
CERT_PATH="/home/lore/Scaricati/mancuso_federated"

# 2) copia dei file richiesti tramite sync
COMMAND="ssh -i $CERT_PATH -J $PROXY"

# validation set coordinator
#rsync -azv --append-verify --stats --human-readable --info=progress2 -e "$COMMAND" /media/lore/EA72A48772A459D9/ILSVRC2012/ILSVRC2012_img_val lmancuso@coordinator:~/federated-learning/Server/res/
#rsync -azv --append-verify --stats --human-readable --info=progress2 -e "$COMMAND" /home/lore/Projects/ILSVRC2012_devkit_t12 lmancuso@coordinator:~/federated-learning/Server/res/

# GPU NODES
# dataset node01
echo 'node01'
ssh -i $CERT_PATH -J $PROXY lmancuso@node01 "rm -rf /mnt/dataset/subset*"
rsync -azv --append-verify --stats --human-readable --info=progress2 -e "$COMMAND" /media/lore/EA72A48772A459D9/ILSVRC2012/ILSVRC2012_img_train/subset01 lmancuso@node01:/mnt/dataset/
# dataset node02
echo 'node02'
ssh -i $CERT_PATH -J $PROXY lmancuso@node02 "rm -rf /mnt/dataset/subset*"
rsync -azv --append-verify --stats --human-readable --info=progress2 -e "$COMMAND" /media/lore/EA72A48772A459D9/ILSVRC2012/ILSVRC2012_img_train/subset02 lmancuso@node02:/mnt/dataset/
# dataset node03
echo 'node03'
ssh -i $CERT_PATH -J $PROXY lmancuso@node03 "rm -rf /mnt/dataset/subset*"
rsync -azv --append-verify --stats --human-readable --info=progress2 -e "$COMMAND" /media/lore/EA72A48772A459D9/ILSVRC2012/ILSVRC2012_img_train/subset03 lmancuso@node03:/mnt/dataset/
# dataset node04
echo 'node04'
ssh -i $CERT_PATH -J $PROXY lmancuso@node04 "rm -rf /mnt/dataset/subset*"
rsync -azv --append-verify --stats --human-readable --info=progress2 -e "$COMMAND" /media/lore/EA72A48772A459D9/ILSVRC2012/ILSVRC2012_img_train/subset04 lmancuso@node04:/mnt/dataset/

# CPU DEVICES
# dataset device1
echo 'device1'
ssh -i $CERT_PATH -J $PROXY lmancuso@device1 "rm -rf /home/lmancuso/dataset/subset*"
rsync -azv --append-verify --stats --human-readable --info=progress2 -e "$COMMAND" /media/lore/EA72A48772A459D9/ILSVRC2012/ILSVRC2012_img_train/subset05 lmancuso@device1:/home/lmancuso/dataset/
# dataset device2
echo 'device2'
ssh -i $CERT_PATH -J $PROXY lmancuso@device2 "rm -rf /home/lmancuso/dataset/subset*"
rsync -azv --append-verify --stats --human-readable --info=progress2 -e "$COMMAND" /media/lore/EA72A48772A459D9/ILSVRC2012/ILSVRC2012_img_train/subset06 lmancuso@device2:/home/lmancuso/dataset/
# dataset device3
echo 'device3'
ssh -i $CERT_PATH -J $PROXY lmancuso@device3 "rm -rf /home/lmancuso/dataset/subset*"
rsync -azv --append-verify --stats --human-readable --info=progress2 -e "$COMMAND" /media/lore/EA72A48772A459D9/ILSVRC2012/ILSVRC2012_img_train/subset07 lmancuso@device3:/home/lmancuso/dataset/
# dataset device4
echo 'device4'
ssh -i $CERT_PATH -J $PROXY lmancuso@device4 "rm -rf /home/lmancuso/dataset/subset*"
rsync -azv --append-verify --stats --human-readable --info=progress2 -e "$COMMAND" /media/lore/EA72A48772A459D9/ILSVRC2012/ILSVRC2012_img_train/subset08 lmancuso@device4:/home/lmancuso/dataset/



# dataset device5
echo 'device5'
#ssh -i $CERT_PATH -J $PROXY lmancuso@device4 "rm -rf /home/lmancuso/dataset/subset*"
rsync -azv --append-verify --stats --human-readable --info=progress2 -e "$COMMAND" /media/lore/EA72A48772A459D9/ILSVRC2012/ILSVRC2012_img_train/subset09 lmancuso@device5:/home/lmancuso/dataset/

# dataset device6
echo 'device6'
#ssh -i $CERT_PATH -J $PROXY lmancuso@device4 "rm -rf /home/lmancuso/dataset/subset*"
rsync -azv --append-verify --stats --human-readable --info=progress2 -e "$COMMAND" /media/lore/EA72A48772A459D9/ILSVRC2012/ILSVRC2012_img_train/subset10 lmancuso@device6:/home/lmancuso/dataset/

# dataset device7
echo 'device7'
#ssh -i $CERT_PATH -J $PROXY lmancuso@device4 "rm -rf /home/lmancuso/dataset/subset*"
rsync -azv --append-verify --stats --human-readable --info=progress2 -e "$COMMAND" /media/lore/EA72A48772A459D9/ILSVRC2012/ILSVRC2012_img_train/subset11 lmancuso@device7:/home/lmancuso/dataset/

# dataset device8
echo 'device8'
#ssh -i $CERT_PATH -J $PROXY lmancuso@device4 "rm -rf /home/lmancuso/dataset/subset*"
rsync -azv --append-verify --stats --human-readable --info=progress2 -e "$COMMAND" /media/lore/EA72A48772A459D9/ILSVRC2012/ILSVRC2012_img_train/subset12 lmancuso@device8:/home/lmancuso/dataset/

# dataset device9
echo 'device9'
#ssh -i $CERT_PATH -J $PROXY lmancuso@device4 "rm -rf /home/lmancuso/dataset/subset*"
rsync -azv --append-verify --stats --human-readable --info=progress2 -e "$COMMAND" /media/lore/EA72A48772A459D9/ILSVRC2012/ILSVRC2012_img_train/subset13 lmancuso@device9:/home/lmancuso/dataset/

# dataset device10
echo 'device10'
#ssh -i $CERT_PATH -J $PROXY lmancuso@device4 "rm -rf /home/lmancuso/dataset/subset*"
rsync -azv --append-verify --stats --human-readable --info=progress2 -e "$COMMAND" /media/lore/EA72A48772A459D9/ILSVRC2012/ILSVRC2012_img_train/subset14 lmancuso@device10:/home/lmancuso/dataset/

# dataset device11
echo 'device11'
#ssh -i $CERT_PATH -J $PROXY lmancuso@device4 "rm -rf /home/lmancuso/dataset/subset*"
rsync -azv --append-verify --stats --human-readable --info=progress2 -e "$COMMAND" /media/lore/EA72A48772A459D9/ILSVRC2012/ILSVRC2012_img_train/subset15 lmancuso@device11:/home/lmancuso/dataset/

# dataset device12
echo 'device12'
#ssh -i $CERT_PATH -J $PROXY lmancuso@device4 "rm -rf /home/lmancuso/dataset/subset*"
rsync -azv --append-verify --stats --human-readable --info=progress2 -e "$COMMAND" /media/lore/EA72A48772A459D9/ILSVRC2012/ILSVRC2012_img_train/subset16 lmancuso@device12:/home/lmancuso/dataset/

# dataset device13
echo 'device13'
#ssh -i $CERT_PATH -J $PROXY lmancuso@device4 "rm -rf /home/lmancuso/dataset/subset*"
rsync -azv --append-verify --stats --human-readable --info=progress2 -e "$COMMAND" /media/lore/EA72A48772A459D9/ILSVRC2012/ILSVRC2012_img_train/subset17 lmancuso@device13:/home/lmancuso/dataset/

# dataset device14
echo 'device14'
#ssh -i $CERT_PATH -J $PROXY lmancuso@device4 "rm -rf /home/lmancuso/dataset/subset*"
rsync -azv --append-verify --stats --human-readable --info=progress2 -e "$COMMAND" /media/lore/EA72A48772A459D9/ILSVRC2012/ILSVRC2012_img_train/subset18 lmancuso@device14:/home/lmancuso/dataset/

# dataset device15
echo 'device15'
#ssh -i $CERT_PATH -J $PROXY lmancuso@device4 "rm -rf /home/lmancuso/dataset/subset*"
rsync -azv --append-verify --stats --human-readable --info=progress2 -e "$COMMAND" /media/lore/EA72A48772A459D9/ILSVRC2012/ILSVRC2012_img_train/subset19 lmancuso@device15:/home/lmancuso/dataset/

# dataset device16
echo 'device16'
#ssh -i $CERT_PATH -J $PROXY lmancuso@device4 "rm -rf /home/lmancuso/dataset/subset*"
rsync -azv --append-verify --stats --human-readable --info=progress2 -e "$COMMAND" /media/lore/EA72A48772A459D9/ILSVRC2012/ILSVRC2012_img_train/subset20 lmancuso@device16:/home/lmancuso/dataset/

# dataset device17
echo 'device17'
#ssh -i $CERT_PATH -J $PROXY lmancuso@device4 "rm -rf /home/lmancuso/dataset/subset*"
rsync -azv --append-verify --stats --human-readable --info=progress2 -e "$COMMAND" /media/lore/EA72A48772A459D9/ILSVRC2012/ILSVRC2012_img_train/subset21 lmancuso@device17:/home/lmancuso/dataset/

# dataset device18
echo 'device18'
#ssh -i $CERT_PATH -J $PROXY lmancuso@device4 "rm -rf /home/lmancuso/dataset/subset*"
rsync -azv --append-verify --stats --human-readable --info=progress2 -e "$COMMAND" /media/lore/EA72A48772A459D9/ILSVRC2012/ILSVRC2012_img_train/subset22 lmancuso@device18:/home/lmancuso/dataset/

# dataset device19
echo 'device19'
#ssh -i $CERT_PATH -J $PROXY lmancuso@device4 "rm -rf /home/lmancuso/dataset/subset*"
rsync -azv --append-verify --stats --human-readable --info=progress2 -e "$COMMAND" /media/lore/EA72A48772A459D9/ILSVRC2012/ILSVRC2012_img_train/subset23 lmancuso@device19:/home/lmancuso/dataset/

# dataset device20
echo 'device20'
#ssh -i $CERT_PATH -J $PROXY lmancuso@device4 "rm -rf /home/lmancuso/dataset/subset*"
rsync -azv --append-verify --stats --human-readable --info=progress2 -e "$COMMAND" /media/lore/EA72A48772A459D9/ILSVRC2012/ILSVRC2012_img_train/subset24 lmancuso@device20:/home/lmancuso/dataset/
