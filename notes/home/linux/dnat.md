firewall-cmd --add-rich-rule='rule family="ipv4" destination address="192.168.201.143" forward-port="12022" protocol="tcp" to-port="22" to-addr="10.100.2.10"' --zone-external

iptables -L

iptables -t nat -L

nft list ruleset