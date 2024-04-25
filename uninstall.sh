echo "Removing systemctl service for web-server..."

systemctl stop webserver
systemctl disable webserver
rm -f /etc/systemd/system/webserver.service
systemctl daemon-reload

echo "Removing web-server..."

rm -rf /usr/local/bin/web-server

echo "Web-server removed successfully!"