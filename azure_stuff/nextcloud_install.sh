#!/bin/bash
PORT=${1}
cd $HOME
mkdir -p gitrepos
cd gitrepos
git clone https://github.com/docker/awesome-compose
cd awesome-compose/nextcloud-redis-mariadb
sed -i -e "s/80:80/${PORT}:80/" docker-compose.yaml
grep "${PORT}:80" docker-compose.yaml
docker-compose up -d
