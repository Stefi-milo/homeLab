
sudo btrfs filesystem show

# Check disk
lsblk

# Create ZFS pool named rpool
zpool create -f rpool /dev/sdb

# Verify if zpool is online and has no data errors (rpool)
zpool status
zfs list

# ZFS quota check
zfs get quota,used rpool/retro-gaming


# Retro Gaming VM
zfs create rpool/retro-gaming

# Retro Gaming VM: max 50GB
zfs set quota=50G rpool/retro-gaming

# Enable compression (lz4)
zfs set compression=lz4 rpool/retro-gaming

zpool status
zfs list

# to register created datasets as a proxmox storage so we can create VMs later
pvesm add zfspool retro-gaming --pool rpool/retro-gaming --content images,rootdir

# Verify
pvesm status
pvesm add zfspool retro-gaming --pool rpool/retro-gaming --content images,rootdir

# Verify
pvesm status


# pve   → Proxmox Virtual Environment
# sm    → Storage Manager
# status → show current status of all storage

pvesm status          # list all storage and their usage
pvesm list <storage>  # list contents of a storage
pvesm add             # add new storage
pvesm remove          # remove storage
pvesm set             # modify storage settings

# Check zfs snapshots

zfs list -t snapshot



