# Stop logging services temporarily
sudo systemctl stop rsyslog systemd-journald

# Copy existing logs to new disk
sudo mkdir /mnt/newlog
sudo mount /dev/log-vg/log-lv /mnt/newlog
sudo cp -a /var/log/. /mnt/newlog/
sudo umount /mnt/newlog

# Add to fstab
echo '/dev/log-vg/log-lv /var/log ext4 defaults 0 2' | sudo tee -a /etc/fstab

# Mount new log disk
sudo mount /var/log

# Restart logging
sudo systemctl start systemd-journald rsyslog

# Verify
lsblk
df -h
