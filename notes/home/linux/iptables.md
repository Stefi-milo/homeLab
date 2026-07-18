\- 1 NAT ma tabulku pro prichozi, odchozi nebo jen prochazejici packety, coz je soucasti NAT tabulky IPTABLES

\- 2 filtrovani packetu

\- 3 packet MANGLING ("vynuceni" napr zmena TTL packetu)

lsmod | less (vypise aktualni moduly)

cat /etc/firewalld/firewalld.conf (muzu zde prepnout pravidla na IPTABLES ci NFTABLES - je vykonnejsi, nizka latence!)

firewall-cmd --list-all-zones | less

firewall-cmd --change-interface=ecs167 --zone=internal --permanent

firewall-cmd --runtime-to-permanent / firewall-cmd --reload (rollback)

firewall-cmd --info-service=ssh

\- zony BLOCK, DMZ, DROP, EXTERNAL, HOME, INTERNAL, TRUSTED, NM-SHARED, WORK, PUBLIC : jaka pravidla se pro zonu zobrazuji, zona = trida PRAVIDEL

\- zona external predpoklada ze masquarade je ZAPLA

\- pridany novy adapter ma vzdy default zonu public

\- staci jen priradit interface do urcitych zone na ktere jsou jiz nastavena pravidla

target: %%REJECT%%

interfaces:

sources:

systemctl status httpd.socket

systemctl enable --now httpd.socket (pri NOW neni treba uz startovat servisu)

ss -lntf

curl 127.0.0.1 (zjistim si zda muj web server ja aktivni, dostupna)

firewall-cmd --add-service=http --zone-external

dnf search webmin

webmin (sprava weboveho serveru)

cockpit (pro redhat)