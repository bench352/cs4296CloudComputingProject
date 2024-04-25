#!/bin/bash

echo "This is an automated script that install the web-server and start it as a systemctl service."

echo "Installing web-server..."

CURRENT_DIR=$(pwd)

cp -r web-server /usr/local/bin/web-server
chmod +x /usr/local/bin/web-server
cd /usr/local/bin/web-server || exit

echo "Creating virtual environment..."

python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

cd "$CURRENT_DIR" || exit

echo "Initializing web-server service..."

cp webserver.service /etc/systemd/system/webserver.service
sed -i "s|<your_username>|$(whoami)|g" /etc/systemd/system/webserver.service

systemctl daemon-reload
systemctl enable webserver
systemctl start webserver

echo "Web-server installed and run successfully!"