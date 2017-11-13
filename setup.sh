#!/bin/sh
apt-get update 
apt-get install -y python 
apt-get update
apt-get install -y python-pip
pip install pexpect
mkdir ht_change_offset
cp -r /mnt/c/Users/ivos/Desktop/ht_change_offset ~/
scp -r ~/ht_change_offset root@192.168.7.2:~/