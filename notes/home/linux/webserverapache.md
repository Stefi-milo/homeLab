--nepotrebuje bezet pod rootem! (apache:apache) - jediny coneumi je otevrit SITOVY SOCKET to muze jen ROOT !

dnf install httpd

systemctl enable --now httpd

systemctl enable httpd.service

--reverzni proxy musi na webserver videt!

/etc/httpd/conf/httpd.conf

/etc/httpd/httpd.conf/ - tenhle adresar modifikujeme vic, zacneme zde vytvaret virtualni weby

&nbsp; welcome.conf - vzdy odstranit

userdir.conf

httpd -M (seznam modulu co webserver pouziva)

/etc/httpd/black.conf : zde vyrvarit virtualni web

<Virtualhost \*:80> (\* znamena ze posloucha na vsech IP)

ServerName black.team109.edu

ServerAlias black.team109.lan

DocumentRoot "/var/www/black.team109.edu/"

CostumLog

ErrorLog

semanage fcontext -a -t httpd\_sys\_content\_t "/srv/example.com(/.\*)" (pozor na SE LINUX kdy umoznuji Apache prava)

echo "MAN in BLACK" > /var/www/black.team109.edu/index.html

apachectl -v configtest

curl -H 'Host:black.team109.edu' http://127.0.0.1

dnf install php

dnf list | grep release (nejedna se o release software ale repository)

vi /var/www/gree.team109.edu/index.php (nezapomen nainstalovat a rozjet handler)

<?php  
  
phpinfo();  
  
