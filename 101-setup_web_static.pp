# Configures a web server for deployment of web_static.

# Nginx configuration file
$nginx_conf = @("EOF")
server {
	listen 80 default_server;
	listen [::]:80 default_server;
	
	root   /var/www/html;
	index  index.html index.htm;

	add_header X-Served-By ${hostname};
	location /hbnb_static {
		alias /data/web_static/current;
	}

	location /redirect_me {
		return 301 http://cuberule.com/;
	}

	error_page 404 /404.html;
	location /404 {
		root /var/www/html;
		internal;
	}
}
EOF

# Fake HTML file
$html = @("EOF")
<html>
	<head>
	</head>
	<body>
		Holberton School
	</body>
</html>
EOF

package { 'nginx':
  ensure   => 'present',
  provider => 'apt',
}

file { '/data':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

file { '/data/web_static':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => File['/data']
}

file { '/data/web_static/releases':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => File['/data/web_static']
}

file { '/data/web_static/releases/test':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => File['/data/web_static/releases']
}

file { '/data/web_static/shared':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => File['/data/web_static/releases/test']
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => $html,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => File['/data/web_static/shared']
}

file { '/data/web_static/current':
  ensure  => 'link',
  target  => '/data/web_static/releases/test',
  require => File['/data/web_static/releases/test']
}

file { '/var/www':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

file { '/var/www/html':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => File['/var/www']
}

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => "Hello World!\n",
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => File['/var/www/html']
}

file { '/var/www/html/404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page\n",
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => File['/var/www/html/index.html']
}

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $nginx_conf,
  owner   => 'root',
  group   => 'root',
  notify  => Service['nginx']
}

service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
