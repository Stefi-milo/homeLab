** HW Resources **

# lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 22.04.5 LTS
Release:	22.04
Codename:	jammy


# uname -a
Linux k8s-worker2 5.15.0-171-generic #181-Ubuntu SMP Fri Feb 6 22:44:50 UTC 2026 x86_64 x86_64 x86_64 GNU/Linux

# To see kernel version
# uname -r
5.15.0-171-generic


# CPU
uname -m                    # architecture
lscpu                       # full CPU details, cores, threads, cache
cat /proc/cpuinfo           # raw CPU info
nproc                       # number of CPU cores


# Memory
free -h                     # RAM usage human readable
cat /proc/meminfo           # detailed memory info


# Disk
lsblk                       # block devices, partitions, mount points
df -h                       # disk usage per filesystem
fdisk -l                    # partition table (needs sudo)
blkid                       # UUID and filesystem types


# Network
ip -br a                    # all interfaces and IPs
ip route show               # routing table
ss -tlnp                    # listening ports
ethtool eth0                # network interface details

# Hardware summary

lshw -short                 # full hardware list (needs sudo)
dmidecode -t system         # BIOS/system info (needs sudo)
hwinfo --short              # detailed hardware (if installed)

# OS info

cat /etc/os-release         # distro name and version
hostnamectl                 # hostname, OS, kernel, architecture
uptime                      # how long running, load average

# Running processes & resources

top                         # live process monitor
htop                        # better top (if installed)
ps aux                      # all running processes

# PCI/USB devices

lspci                       # PCI devices (GPU, network cards)
lsusb                       # USB devices

# Quick one liner system summary :

echo "=== SYSTEM ===" && hostnamectl && echo "=== CPU ===" && lscpu | grep -E "Architecture|CPU\(s\)|Model name" && 
echo "=== MEMORY ===" && free -h && echo "=== DISK ===" && df -h | grep -v tmpfs
