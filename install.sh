#!/bin/bash

CERT_PATH="/root/cert"
mkdir $CERT_PATH
openssl req -new -newkey rsa:4096 -days 3600 -nodes -x509 -subj '/C=UK/ST=Denial/L=String/O=Dis/CN=www.ray.uk' -keyout $CERT_PATH/host.key -out $CERT_PATH/host.crt
docker-compose build
docker-compose -f /root/v2ray-traffic-manager-slave-node/docker-compose.yaml up -d
sleep 10
