# What filesystem is your OS
sudo df -T /volume1

# identify USB device
lsblk

# Unmounting
sudo umount /dev/sdb3

# Creating boot drive
sudo dd if=proxmox-ve_9.1-1.iso of=/dev/sdb bs=1M status=progress conv=fsync
sync

# Verify the flash matches the ISO
sudo cmp proxmox-ve_9.1-1.iso /dev/sdb


# If installation goes wrong, after pressing CTRL+ALT+F2
cat /tmp/install.log | tail -50
# or
dmesg | tail -30

# On Ubuntu, verify ISO integrity first and compare on website with the checksum
md5sum proxmox-ve_9.1-1.iso


