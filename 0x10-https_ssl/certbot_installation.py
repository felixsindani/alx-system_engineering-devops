#!/usr/bin/env bash
#install certbot
sudo apt update
sudo apt install snapd
sudo apt-get remove certbot
sudo apt-get install certbot
sudo service haproxy stop
sudo certbot certonly --standalone --preferred-challenges http --http-01-port 80 -d www.sindani.tech
sudo ls /etc/letsencrypt/live/www.sindani.tech
sudo mkdir -p /etc/haproxy/certs
DOMAIN='www.sindani.tech' sudo -E bash -c 'cat /etc/letsencrypt/live/$DOMAIN/fullchain.pem /etc/letsencrypt/live/$DOMAIN/privkey.pem > /etc/haproxy/certs/$DOMAIN.pem'
sudo chmod -R go-rwx /etc/haproxy/certs
sudo nano /etc/haproxy/haproxy.cfg
