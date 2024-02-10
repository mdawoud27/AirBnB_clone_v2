#!/usr/bin/env bash
# Prepare the web servers
#
# Install Nginx if not installed
sudo apt update
sudo apt install nginx -y

# Create directories
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/

# Create the fake html file
sudo echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tMohamed Dawoud\n\t</body>\n</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null


# Create symbolic link (rm if already exists)
sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test /data/web_static/current

# Give the ownership to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sudo sh -c 'echo "server {
     listen 80;
     listen [::]:80 default_server;
     server_name dawoud.tech
     location /hbnb_static {
        alias /data/web_static/current/;
     }
}" >> /etc/nginx/sites-available/default'

# Restart and Reload Nginx
sudo service nginx restart
sudo nginx -s reload
