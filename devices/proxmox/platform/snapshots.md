# On Proxmox SSH
zfs snapshot rpool/k8s-master/vm-100-disk-0@base
zfs snapshot rpool/k8s-master/vm-100-disk-1@base
zfs snapshot rpool/k8s-master/vm-100-disk-2@base
zfs snapshot rpool/k8s-master/vm-100-disk-3@base

# Verify
zfs list -t snapshot

# What you can do with snapshots:
1. Rollback — go back to a previous state: If k8s installation breaks everything
- qm stop 100
- zfs rollback rpool/k8s-master/vm-100-disk-1@base
- qm start 100
# VM is back to clean Ubuntu, no k8s
2. See what changed since snapshot:
- zfs diff rpool/k8s-master/vm-100-disk-1@base
Shows every file added/changed/deleted since snapshot
3. Clone from snapshot — create new VM from this exact state:
# Create another VM from the clean base
- qm clone 100 103 --name k8s-worker3
# Instantly gets clean Ubuntu with correct disk layout

**Think of snapshots like this:**
@base          → clean Ubuntu, no k8s (NOW)
@k8s-ready     → after k8s installed and working
@app-deployed  → after apps deployed

# Real world scenarios: k8s upgrade goes wrong → rollback to @k8s-ready
# App deployment breaks cluster → rollback to @k8s-ready
# Want to test something risky → snapshot first, test, rollback if needed

** Important: Snapshots are not backups — if the disk fails, snapshots are lost too. That's what your backup-agent VM will be for later. **


