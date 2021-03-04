#!/bin/bash
# Install Docker
sudo apt-get --assume-yes update
sudo apt-get --assume-yes install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
sudo apt-get --assume-yes update
apt-cache policy docker-ce
sudo apt-get --assume-yes install docker-ce

exit 0