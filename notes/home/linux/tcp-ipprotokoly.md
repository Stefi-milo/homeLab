ARP

iEEE 802.xx / spanning tree / LACP

ipv4 , ipv6, ICMPv4, IGMP (multicast), RARP ,...

TCP / UDP --> dns dotazy, synchronizace casu, voice, real time protokoly ...

HTTP, DNS (pouziva oboji tcp/udp), DHCP, SNMP, SMB, FTP ....

APLIKACE DATA STREAM vrstva Transport - data payload


 | TCP HEADER | (tcp,udp,port,velikost segmentu,sekvencni cisla,..) | DATA | SEGMENT |
 | IP HEADER | | PACKET |
 | MAC HEADER| 1500 bitu po linkove vrstve ( nebo jumbo ramec 9000 bitu) | FRAME |