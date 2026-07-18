# Check current status and leased info

ip addr show                    	# current IP
ip route                        	# default gateway
cat /var/lib/dhcp/dhclient.leases  	# full lease details (Ubuntu/Debian)

# Sends a DHCP RELEASE message to the server saying "I'm done with this IP, you can give it to someone else." Your interface loses its IP immediately.

sudo dhclient -r eth0

# Sends a DHCP DISCOVER message starting the full DHCP handshake (DISCOVER → OFFER → REQUEST → ACK) to get a new lease. 
# You may get the same IP or a different one depending on the server.
 
sudo dhclient eth0 

sudo dhclient -r eth0 && sudo dhclient eth0  	# release + renew in one line

# Check lease expity time

cat /var/lib/dhcp/dhclient.leases | grep -E "expire|renew|rebind|fixed-address"

# On Ubuntu

networkctl status               # shows lease info per interface
resolvectl status               # DNS from DHCP

# On Debian

nmcli device show eth0          # full DHCP info including expiry
nmcli con down eth0 && nmcli con up eth0  # renew

# Check what DHCP server assigned

journalctl -u networking        # Debian
journalctl -u systemd-networkd  # Ubuntu/netplan

**  TROUBLESHOOTING **

# Check if interface is up

ip link show eth0
ip link set eth0 up             # bring it up if down

# Manually trigger DHCP with verbose output

sudo dhclient -v eth0           # -v shows full DISCOVER/OFFER/REQUEST/ACK

# Check if DHCP packets are even leaving your machine: 

sudo tcpdump -i eth0 port 67 or port 68    # 67=server, 68=client

# Check system logs for DHCP errors :

journalctl -u networking -n 50
journalctl | grep -i dhcp
dmesg | grep -i eth0

# Check if interface has IP at all :

ip addr show eth0

# Force a fresh start :

sudo ip link set eth0 down
sudo ip link set eth0 up
sudo dhclient -v eth0


# dhcp relay vetsinou bezi na routrech
