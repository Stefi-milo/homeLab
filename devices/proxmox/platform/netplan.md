# On worker1 console
sudo nano /etc/netplan/00-installer-config.yaml

# Change it to DHCP:
network:
  version: 2
  ethernets:
    ens18:
      dhcp4: true

# Then apply:
sudo netplan apply
ip a

# Try out if the configuration of netplan is ok

sudo netplan try
