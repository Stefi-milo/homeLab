IANNA.ORG

CZ.NIC

prevod na ip adresu A zaznam

AAAA zaznam : domena prekladana na IPv6

CNAME :alias

NS :ktery dns server obsluhuje danou domeny vystupem je hostname

MX :pro postu

SPF : textovy komentar pro mail servery

SOA ZAZNAMY { TTL doba zaznamu se obvykle bede od tud

DOPREDNE ZAZNAMY ,databaze, zaznamy hlavne typu A

rotovska domena = .

 www.tmo.cz. (domena 3 radu)(domena 2 radu)(domena 1 radu)

REVERZNI ZONY, ZAZNAMY

ol-100-1.team100.edu. 3600 A 10.100.1.10 (3600 TTL, doba zaznamu v kesi v databazi/dns)

10.100.1.10 PTR ol-100-1.team100.edu.

1.100.10.in-addr.arpa. (nazev domeny pro .10 hosts )

-client kdyz se dotazuje DNS serveru na preklad tak DNS nevi IP adresu DNS co je nad nim z pohledu hiearchie

-prvni DNS server na ktery se DNS bude ptat je ROOT DNS takze hledani domeny "od konce zaznamu"

root.servers.org (zde najdu vsechny root servery, celkem 13 titan serveru na svete)

dnf install bind bind-utils

systemctl enable --now named.service

vi /etc/named.conf (recursion yes) znamena ze dns ma povoleno se ptat jinyho dns

(allow-recursion) uvedte site pro ktere je dns potreba

--definuji logging, ale i "zony" --> je pro konfigurace pro forward dns hlavne

zone "." IN

type hint

file "named.ca"

cat /var/named/name.ca

/etc/resolv.conf (konfigurace clienta)

nmcli connection down PUBLIC;nmcli connection up PUBLIC

nslookup google.com

nslookup -q=A google.com

nslookup -q=NS google.com (jaky nameserver google.com pouziva)

nslookup -q=MX google.com

nslookup -q=SOA google.com

nslookup -q=TXT google.com

nslookup -q=PTR google.com

nslookup -q=PTR 222.77.75.77.in-addr.arpa.

dig nfs.team109.edu

dig MX team109.edu

dig @8.8.8.8 ibm.com

dig @8.8.8.8 MX ibm.com

-- BIND ZONE file generator

; BIND db file for team109.edu

--> vytvoreni vlastni zony:

$TTL 600

@ IN SOA ns.team109.edu. hostmaster.team109.edu. (

2025111301 ; serial number YYMMDDNN

28800 ; Refresh

7200 ; Retry

864000 ; Expire

600 ; Min TTL

NS ns.team109.edu.

MX 10 mx1.team109.edu.

MX 20 mx2.team109.edu.

$ORIGIN team109.edu.

ol-100-3 IN A 192.168.201.143

ol-100-2 IN A 10.109.2.1

ol-100-1 IN A 10.109.1.1