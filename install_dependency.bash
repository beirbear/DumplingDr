#!/bin/bash

# Please follow the installation below
# List the dependency here
# Download mongodb

echo "Install mongodb"
wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-amazon-3.2.5.tgz
tar -xvf mongodb-linux-x86_64-amazon-3.2.5
mv mongodb-linux-x86_64-amazon-3.2.5 mongodb
cd mongodb-linux-x86_64-amazon-3.2.5/
MONGO_PATH_PATH=`pwd`
echo "export PATH=${MONGO_PATH}/bin:$PATH"


# Then create a data folder
echo "Create mongodb data folder"
sudo mkdir /data
sudo mkdir /data/db
echo "Change mongodb data folder permission"
sudo chmod 777 /data
sudo chmod 777 /data/db

# Then, run the app and that's it

# Install python 3.5
echo "Install python 3.5"
sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt-get update
sudo apt-get install python3.5

# Install setup tool
echo "Install setup tool"
wget https://bootstrap.pypa.io/ez_setup.py -O - | sudo python3.5

# Install REST framework (Falcon)
echo "Install REST framework (Falcon)"
git clone https://github.com/falconry/falcon.git
install on python 3.5 (The one that you just has installed)
cd falcon
sudo python3.5 setup.py install

# Install pymongo api
echo "Install pymongo"
git clone git://github.com/mongodb/mongo-python-driver.git pymongo
cd pymongo/
sudo python3.5 setup.py install