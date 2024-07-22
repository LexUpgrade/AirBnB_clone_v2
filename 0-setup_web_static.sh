#!/usr/bin/env bash
# Sets up a web server (Nginx) for deployment of web_static.

# Installs Nginx and root directories
apt-get update &&
	apt-get install nginx -y
ufw allow 'Nginx HTTP'
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
chown -R ubuntu /data/
chgrp -R ubuntu /data/

# Creates an HTML file
printf %s "<html>
	<head>
	</head>
	<body>
		<h1>ALX - The Best School Ever... \o/ yhhh!</h1>
	</body>
</html>
" > /data/web_static/releases/test/index.html
ln -fs /data/web_static/releases/test /data/web_static/current

# Nginx configuration
printf %s "server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root /var/www/html;
	index index.html index.htm;

	server_name _;
	add_header X-Served-By $HOSTNAME;

	location /hbnb_static {
		alias /data/web_static/current/test;
		index index.html index.htm;
	}

	location /redirect_me {
		return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
	}

	error_page 404 /404.html;
	location /404 {
		root /var/www/html;
		internal;
	}
}" > /etc/nginx/sites-available/default
service nginx restart
