A **Linux filesystem** is the method and data structure the Linux kernel uses to **organize, store, retrieve, and manage data on storage devices** (HDDs, SSDs, NVMe, USB drives, etc.).

It defines:

- How files and directories are structured
    
- How metadata (permissions, ownership, timestamps) is stored
    
- How free/used space is tracked
    
- How data integrity is handled
    

Without a filesystem, your disk is just raw blocks of data.

---

# What a Filesystem Is For

A Linux filesystem provides:

### 1️⃣ File organization

Hierarchical directory structure (`/home`, `/var`, `/etc`, etc.)

### 2️⃣ Metadata management

- Ownership (user/group)
- Permissions (rwx)
- Timestamps
- File size
- Inodes
    

### 3️⃣ Data integrity

- Journaling
- Checksums (in modern filesystems)
    

### 4️⃣ Advanced features (depending on FS)

- Snapshots
- Compression
- Encryption
- RAID
- Deduplication
- Self-healing
    

---

# Common Linux Filesystems

## 🟢 ext4 (Fourth Extended Filesystem)

**Most common Linux filesystem.**

### Pros:

- Very stable
- Fast
- Mature
- Excellent compatibility
- Low overhead
- Good performance on SSDs
    

### Cons:

- No built-in snapshots
- No native compression
- No built-in RAID
- No data checksumming for file contents
    

### Best for:

- Servers
- General Linux systems
- Simplicity and reliability
    

---

## 🔵 ZFS (OpenZFS)

Modern advanced filesystem + volume manager in one.

Main project: OpenZFS

Originally from Sun Microsystems.

### Pros:

- Built-in snapshots
- Built-in compression
- Built-in RAID (RAID-Z)
- End-to-end checksumming
- Self-healing
- Very high data integrity
- Copy-on-write (CoW)
- Excellent for large storage systems
    

### Cons:

- Higher RAM usage (rule of thumb: 1GB per TB for optimal performance)
- More complex
- Not built into Linux kernel (licensed separately)
- Can be heavy for small systems
    

### Best for:

- NAS systems
- Backup servers
- Virtualization storage
- Data integrity critical systems
    

---

## 🟣 Btrfs (B-Tree Filesystem)

Developed by Oracle Corporation, now community maintained.

### Pros:

- Snapshots
- Compression (zstd, lzo, zlib)
- Built-in RAID
- Checksumming
- Subvolumes
- Lighter than ZFS
- Integrated in Linux kernel
    

### Cons:

- RAID5/6 still considered risky
- Slightly less mature than ext4
- Can fragment over time
    

### Best for:

- Desktop systems
- Rolling distros (like openSUSE default)
- Systems needing snapshots but lighter than ZFS