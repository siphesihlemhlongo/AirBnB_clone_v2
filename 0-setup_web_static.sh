#!/bin/bash
# Install Nginx if not installed
sudo apt-get -y update
sudo apt-get -y install nginx

# Create required directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file
echo -e "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>"
| sudo tee /data/web_static/releases/test/index.html

# Create or recreate symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sudo sed -i '/^\tlocation \/ {$/a\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n'
/etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
