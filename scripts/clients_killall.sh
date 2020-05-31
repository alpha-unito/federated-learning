PROXY="lmancuso@130.192.137.199"
CERT_PATH="/home/lore/Scaricati/mancuso_federated"

REMOVE_COMMAND="pkill python3"

#ssh -i $CERT_PATH -J $PROXY lmancuso@coordinator $REMOVE_COMMAND

ssh -i $CERT_PATH -J $PROXY lmancuso@node01 $REMOVE_COMMAND
ssh -i $CERT_PATH -J $PROXY lmancuso@node02 $REMOVE_COMMAND
ssh -i $CERT_PATH -J $PROXY lmancuso@node03 $REMOVE_COMMAND
ssh -i $CERT_PATH -J $PROXY lmancuso@node04 $REMOVE_COMMAND

ssh -i $CERT_PATH -J $PROXY lmancuso@device1 $REMOVE_COMMAND
ssh -i $CERT_PATH -J $PROXY lmancuso@device2 $REMOVE_COMMAND
ssh -i $CERT_PATH -J $PROXY lmancuso@device3 $REMOVE_COMMAND
ssh -i $CERT_PATH -J $PROXY lmancuso@device4 $REMOVE_COMMAND
ssh -i $CERT_PATH -J $PROXY lmancuso@device5 $REMOVE_COMMAND
ssh -i $CERT_PATH -J $PROXY lmancuso@device6 $REMOVE_COMMAND
ssh -i $CERT_PATH -J $PROXY lmancuso@device7 $REMOVE_COMMAND
ssh -i $CERT_PATH -J $PROXY lmancuso@device8 $REMOVE_COMMAND
ssh -i $CERT_PATH -J $PROXY lmancuso@device9 $REMOVE_COMMAND
ssh -i $CERT_PATH -J $PROXY lmancuso@device10 $REMOVE_COMMAND
ssh -i $CERT_PATH -J $PROXY lmancuso@device11 $REMOVE_COMMAND
ssh -i $CERT_PATH -J $PROXY lmancuso@device12 $REMOVE_COMMAND
ssh -i $CERT_PATH -J $PROXY lmancuso@device13 $REMOVE_COMMAND
ssh -i $CERT_PATH -J $PROXY lmancuso@device14 $REMOVE_COMMAND
ssh -i $CERT_PATH -J $PROXY lmancuso@device15 $REMOVE_COMMAND
ssh -i $CERT_PATH -J $PROXY lmancuso@device16 $REMOVE_COMMAND
ssh -i $CERT_PATH -J $PROXY lmancuso@device17 $REMOVE_COMMAND
ssh -i $CERT_PATH -J $PROXY lmancuso@device18 $REMOVE_COMMAND
ssh -i $CERT_PATH -J $PROXY lmancuso@device19 $REMOVE_COMMAND
ssh -i $CERT_PATH -J $PROXY lmancuso@device20 $REMOVE_COMMAND
