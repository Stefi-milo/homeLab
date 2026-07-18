* NMAP

IPv4 vs IPv6 (128 bit, objevuje se zde IPSEC, vnorovani hlavicek)

UNICAST A --> B one-to-one ip resolution

BROADCAT ALL x.x.x.225

MULTITASK GMP protocol 224.0.0.1

ANYCAST napr DNS - nektere ilove adresy v ramci IP DNSka budou pristupne jen z urcitych segmentu, REGIONU

lspci

dmesg | less

/etc/sysconfig/network-scripts/ (redhat pozuiva Network manager)

nmcli (parametry VELKYM pismenem jsou RUNTIME parametry)

nmcli device show

nmcli connection show

nmtui

/etc/Networkmanager/system-connections/ens192.nmconnections (staci vytvorit file pro vytvoreni noveho interfacu a obratit network manager)

ip addr add / del (smaze aresu) / flush (smaze cely interface) / show / change VSE JE JEN STATICKY po REBOOT se hodnoty vrati

ip addr add 10.109.1.2 dev ens234

nmcli connection reload

* BOND interface \[jedna MAC] (mode 802.3ad LACP protokol)

(mode ROUND-ROBIN distribuce na interface 1, pak 2, 3 ,4 ...a zase 1,2,3,4)

- proto i na interface pri 1,2 projde vzdy druhy ping!

* BRIDGE interface (na L2 vrstve propojeni 2 zarizeni, napriklad u VM kdy VM potrebuje sitovku fyzickeho zarizeni)

* VLAN interface

sysctl net.ipv4.ip\_forward=1

echo 0 /proc/sys/net/ipv4/ip\_forward (tim forward vypnu, pouze RUNTIME hodnota kvuli PROC adresari)

vi 10.forward.conf (a zapsat to dovnitr: net.ipv4.ip\_forward=1 ,tim uz to neni runtime)

/usr/lib/sysctl.d/

/USR/==> soubory do USR se dostanou pomoci instalaci (jsou zde knihovny, prikazy atd ...) sem s NESAHA, piste pouze do /ETC/

/etc/sysctl.d/

/run/sysctl.d/ ==> vylozene RUNTIME zalezitost, neprezije REBOOT

sysctl -a | less

cp /usr/lib/systemd/system/sshd.service /etc/lib/systemd/system/sshd.service (diky uprave v etc jsem si vytvoril vlastni customized servisu)

LOGIKA FRAMEWORKU : prvne hleda v RUN adresari, pak v ETC a jinak v USR

mount | grep run (tmpfs filesystem)

/usr/sbin/ system binaries

/usr/bin/ uzivatele nebo bezne

* pod DEBIAN se pod uzivatelem ROOT neprihlasime (debian muze a nemusi pouzivat Networkmanager)

* vychozi GW je z principu vzdy jen 1