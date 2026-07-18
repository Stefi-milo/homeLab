# Check MAC of the interface

ip link show enp6s18

# Restart interface down and back up

sudo ifdown enp6s18 && sudo ifup enp6s18

# Describes the network interfaces available on your system

cat /etc/network/interfaces
