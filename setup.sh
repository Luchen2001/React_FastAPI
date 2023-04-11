#!/usr/bin/env bash

# Install required packages
sudo apt update
sudo apt install nginx -y
sudo apt-get install curl
sudo apt install nodejs
sudo apt install npm

# Set up React app
cd ~/React_FastAPI/fastapi-react/frontend
npm install
npm run build

# Set up PM2
sudo npm install pm2@latest -g
pm2 start npm --name "React" -- start
pm2 startup systemd

# Copy Nginx configuration
nginx_config_file="/etc/nginx/sites-available/react"
sudo cp nginx_react_config "$nginx_config_file"

# Create symbolic link for Nginx configuration
sudo ln -s /etc/nginx/sites-available/react /etc/nginx/sites-enabled/

# Restart Nginx
sudo systemctl restart nginx

pm2 restart "React"

# install library for backend
sudo apt install python3-pip
pip install fastapi 
pip install --user uvicorn
pip install decorator
export PATH="/home/ubuntu/.local/lib/python3.10/site-packages:$PATH"


