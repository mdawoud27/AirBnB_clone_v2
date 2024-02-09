#!/usr/bin/env bash
# Prepare the web servers

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
nginx_config="server {\n"
nginx_config+="\tlisten 80 default_server;\n"
nginx_config+="\tlisten [::]:80 default_server;\n"
nginx_config+="\tserver_name dawoud.tech;\n"
nginx_config+="\tlocation /hbnb_static/ {\n"
nginx_config+="\t\talias /data/web_static/current/;\n"
nginx_config+="\t}\n"
nginx_config+="}\n"

echo -e "$nginx_config" | sudo tee /etc/nginx/sites-available/default > /dev/null

# Restart and Reload Nginx
sudo service nginx restart
sudo nginx -s reload
