#!/usr/bin/env bash
#Write a Bash script that sets up your web servers for the deployment of web_static. It must:
sudo apt update
sudo apt-get -y install nginx
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch -p /data/web_static/releases/test/index.html
echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" > sudo /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "55i location /hbnb_static/ {\nalias /data/web_static/current/;\n}\n" /etc/nginx/sites-enabled/default
sudo service nginx restart