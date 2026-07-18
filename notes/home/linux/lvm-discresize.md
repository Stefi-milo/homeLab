# LVM (Logical Volume Manager). Here's the full picture of what we did:
# LVM components:
PV (Physical Volume) → the actual disk (e.g. /dev/sdc)
VG (Volume Group)    → pool of storage (e.g. containerd-vg)
LV (Logical Volume)  → usable partition (e.g. containerd-lv)

# The resize process we followed:

1. pvresize /dev/sdc        → tell LVM the PV (disk) got bigger
2. lvextend containerd-lv   → extend the LV to use new PV space
3. resize2fs containerd-lv  → extend the filesystem to fill the LV

# Think of it like:

Physical disk (sdc)     = land
Volume Group (VG)       = city built on that land
Logical Volume (LV)     = building in the city
Filesystem (ext4)       = rooms inside the building

pvresize  = annexing more land to the city
lvextend  = making the building bigger
resize2fs = adding more rooms inside


lvextend → extends an LV
lvreduce → shrinks an LV
lvresize → extends or shrinks an LV

# All are LVM commands. ZFS handles this differently — it resizes automatically without needing separate steps.

sudo pvresize /dev/sdc
sudo lvextend -l +100%FREE /dev/containerd-vg/containerd-lv
sudo resize2fs /dev/containerd-vg/containerd-lv
df -h /var/lib/containerd
