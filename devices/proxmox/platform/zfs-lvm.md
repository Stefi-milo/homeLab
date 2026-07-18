# LVM on k8s VMs:

Lower memory overhead — ZFS is memory hungry (needs ~1G RAM minimum)
Better performance for container workloads
containerd and kubelet work natively with LVM
Simpler to manage thin provisioning for container storage
Less CPU overhead

# ZFS on Proxmox host:

Perfect for VM disk management (snapshots, clones, compression)
ZFS handles the underlying storage efficiently
Proxmox snapshots work at ZFS level — so you get VM-level snapshots for free

# So the stack looks like:

Proxmox (ZFS)
└── VM disk stored as ZFS dataset
    └── Inside VM: LVM
        ├── / (root)
        ├── /var/lib/containerd
        └── /var/log

# Best of both worlds:

ZFS gives you VM snapshots, compression, data integrity at Proxmox level
LVM gives k8s lightweight, fast local storage inside the VM
You can snapshot the entire VM at ZFS level before k8s upgrades

