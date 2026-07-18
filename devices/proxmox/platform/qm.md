qm config 100
qm start 100
qm status 100

# if VM is actually running
qm showcmd 100

# Stop VM
qm stop 100

# Remove serial and switch to VGA
qm set 100 --delete serial0
qm set 100 --vga std

# Start again
qm start 100

# Set worker1 resources
qm set 101 --memory 6144 --cores 2 --name k8s-worker1

# Set worker2 resources
qm set 102 --memory 6144 --cores 2 --name k8s-worker2

# Verify
qm config 101
qm config 102


# Resize containerd disk on both workers
qm resize 101 scsi1 60G
qm resize 102 scsi1 60G

# Verify
qm config 101 | grep scsi
qm config 102 | grep scsi

# Adding extra core to VM
qm stop 100
qm set 100 --cores 2
qm start 100

# Converting Template back to VM
qm set 100 --template 0

# qm stands for QEMU Manager ,breaking it down:
qm     → QEMU Manager (Proxmox CLI tool for managing VMs)
clone  → the action
100    → source VM ID (k8s-master)
101    → new VM ID (k8s-worker1)

It's the CLI tool for managing full virtual machines (KVM/QEMU based) in Proxmox.
Common commands:

# bashqm create   # create a new VM
qm start    # start a VM
qm stop     # stop a VM
qm reboot   # reboot a VM
qm clone    # clone a VM
qm snapshot # take a snapshot
qm rollback # restore a snapshot
qm destroy  # delete a VM
qm config   # show VM configuration
qm list     # list all VMs
qm status   # show VM status
qm migrate  # migrate VM to another node
```

**The difference between `qm` and `pvesm`:**
```
qm     → manages VMs (compute)
pvesm  → manages storage
pct    → manages LXC containers (not VMs)

Think of qm as the CLI equivalent of clicking on a VM in the Proxmox web UI. Everything you can do in the GUI with a VM, you can do with qm on the command line.
