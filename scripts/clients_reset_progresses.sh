PROXY="lmancuso@130.192.137.199"
CERT_PATH="/home/lore/Scaricati/mancuso_federated"


echo 'coordinator'
ssh -i $CERT_PATH -J $PROXY lmancuso@coordinator "cd federated-learning/Server/snapshots/ ; rm -rfv ./*"
echo 'node01'
ssh -i $CERT_PATH -J $PROXY lmancuso@node01 "cd federated-learning/Client/snapshots; rm -rfv ./*"
echo 'node02'
ssh -i $CERT_PATH -J $PROXY lmancuso@node02 "cd federated-learning/Client/snapshots; rm -rfv ./*"
echo 'node03'
ssh -i $CERT_PATH -J $PROXY lmancuso@node03 "cd federated-learning/Client/snapshots; rm -rfv ./*"
echo 'node04'
ssh -i $CERT_PATH -J $PROXY lmancuso@node04 "cd federated-learning/Client/snapshots; rm -rfv ./*"

echo 'device1'
ssh -i $CERT_PATH -J $PROXY lmancuso@device1 "cd federated-learning/Client/snapshots; rm -rfv ./*"
echo 'device2'
ssh -i $CERT_PATH -J $PROXY lmancuso@device2 "cd federated-learning/Client/snapshots; rm -rfv ./*"
echo 'device3'
ssh -i $CERT_PATH -J $PROXY lmancuso@device3 "cd federated-learning/Client/snapshots; rm -rfv ./*"
echo 'device4'
ssh -i $CERT_PATH -J $PROXY lmancuso@device4 "cd federated-learning/Client/snapshots; rm -rfv ./*"
echo 'device5'
ssh -i $CERT_PATH -J $PROXY lmancuso@device5 "cd federated-learning/Client/snapshots; rm -rfv ./*"
echo 'device6'
ssh -i $CERT_PATH -J $PROXY lmancuso@device6 "cd federated-learning/Client/snapshots; rm -rfv ./*"
echo 'device7'
ssh -i $CERT_PATH -J $PROXY lmancuso@device7 "cd federated-learning/Client/snapshots; rm -rfv ./*"
echo 'device8'
ssh -i $CERT_PATH -J $PROXY lmancuso@device8 "cd federated-learning/Client/snapshots; rm -rfv ./*"
echo 'device9'
ssh -i $CERT_PATH -J $PROXY lmancuso@device9 "cd federated-learning/Client/snapshots; rm -rfv ./*"
echo 'device10'
ssh -i $CERT_PATH -J $PROXY lmancuso@device10 "cd federated-learning/Client/snapshots; rm -rfv ./*"
echo 'device11'
ssh -i $CERT_PATH -J $PROXY lmancuso@device11 "cd federated-learning/Client/snapshots; rm -rfv ./*"
echo 'device12'
ssh -i $CERT_PATH -J $PROXY lmancuso@device12 "cd federated-learning/Client/snapshots; rm -rfv ./*"
#echo 'device13'
#ssh -i $CERT_PATH -J $PROXY lmancuso@device13 "cd federated-learning/Client/snapshots; rm -rfv ./*"
#echo 'device14'
#ssh -i $CERT_PATH -J $PROXY lmancuso@device14 "cd federated-learning/Client/snapshots; rm -rfv ./*"
#echo 'device15'
#ssh -i $CERT_PATH -J $PROXY lmancuso@device15 "cd federated-learning/Client/snapshots; rm -rfv ./*"
#echo 'device16'
#ssh -i $CERT_PATH -J $PROXY lmancuso@device16 "cd federated-learning/Client/snapshots; rm -rfv ./*"
#echo 'device17'
#ssh -i $CERT_PATH -J $PROXY lmancuso@device17 "cd federated-learning/Client/snapshots; rm -rfv ./*"
#echo 'device18'
#ssh -i $CERT_PATH -J $PROXY lmancuso@device18 "cd federated-learning/Client/snapshots; rm -rfv ./*"
#echo 'device19'
#ssh -i $CERT_PATH -J $PROXY lmancuso@device19 "cd federated-learning/Client/snapshots; rm -rfv ./*"
#echo 'device20'
#ssh -i $CERT_PATH -J $PROXY lmancuso@device20 "cd federated-learning/Client/snapshots; rm -rfv ./*"