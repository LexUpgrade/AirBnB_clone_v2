#!/usr/bin/env bash
# Sets up a web server (Nginx) for deployment of web_static.

# Install Nginx if it not already installed.
apt-get update &&
	apt-get install -y nginx

# Creates the folder /data/ if it doesn’t already exist
# Creates the folder /data/web_static/ if it doesn’t already exist
# Creates the folder /data/web_static/releases/ if it doesn’t already exist
# Creates the folder /data/web_static/shared/ if it doesn’t already exist
# Creates the folder /data/web_static/releases/test/ if it doesn’t already exist
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Creates a fake HTML file /data/web_static/releases/test/index.html (with simple content, to test your Nginx configuration)
printf %s "<html>
	<head>
	</head>
	<body>
		Holberton School
	</body>
</html>
" > /data/web_static/releases/test/index.html
# Creates a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder. If the symbolic link already exists, it should be deleted and recreated every time the script is ran.
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group (you can assume this user and group exist). This should be recursive; everything inside should be created/owned by this user/group.
chown -hR ubuntu:ubuntu /data/
chmod -R 755 /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static).
printf %s "server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root /var/www/html;
	index index.html index.htm;
	add_header X-Served-By $HOSTNAME;

	location /hbnb_static {
		alias /data/web_static/current;
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

# Restart Nginx after updating the configuration
service nginx restart
