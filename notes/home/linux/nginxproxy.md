systemctl disable httpd

systemctl mask httpd (pozastavim kompletne sluzbu pak pomoci UNMUSK zase muzu nastartovat, pouziju kdyz mam 2 servisi na stejnem portu)

--odhesovat https pro port 443

server {

listen 443 ssl http2;

}

cd /conf.d cat web.conf

vi revproxy.conf

mkdir -p /var/www/black

systemctl reload nginx

REVERZNI PROXY :

server {

server\_name team109.edu;

location / {

root /var/www/html/;

}

location /black/ {

proxy\_pass http://black.team109.edu/;

}

CERTBOT pro automatizaci certifikatu a musi cert byt videt z internetu

certbot zkontroluje ze webserver existuje a ze je cert muj