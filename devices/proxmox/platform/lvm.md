# Expand root LVM to full 20G sda:

sudo lvextend -l +100%FREE /dev/ubuntu-vg/ubuntu-lv
sudo resize2fs /dev/ubuntu-vg/ubuntu-lv
df -h /


# Create LVM on sdc (20G) for containerd:

sudo pvcreate /dev/sdc
sudo vgcreate containerd-vg /dev/sdc
sudo lvcreate -l 100%FREE -n containerd-lv containerd-vg
sudo mkfs.ext4 /dev/containerd-vg/containerd-lv
sudo mkdir -p /var/lib/containerd
echo '/dev/containerd-vg/containerd-lv /var/lib/containerd ext4 defaults 0 2' | sudo tee -a /etc/fstab
sudo mount /var/lib/containerd

# Create LVM on sdb (10G) for logs:

sudo pvcreate /dev/sdb
sudo vgcreate log-vg /dev/sdb
sudo lvcreate -l 100%FREE -n log-lv log-vg
sudo mkfs.ext4 /dev/log-vg/log-lv 
