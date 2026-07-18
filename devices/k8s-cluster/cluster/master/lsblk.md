milo@master:~$ lsblk
NAME                            MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda                               8:0    0   20G  0 disk 
├─sda1                            8:1    0  953M  0 part /boot/efi
├─sda2                            8:2    0  1.8G  0 part /boot
└─sda3                            8:3    0 17.3G  0 part 
  └─ubuntu--vg-ubuntu--lv       253:2    0 17.3G  0 lvm  /
sdb                               8:16   0   10G  0 disk 
└─log--vg-log--lv               253:1    0   10G  0 lvm  /var/log
sdc                               8:32   0   20G  0 disk 
└─containerd--vg-containerd--lv 253:0    0   20G  0 lvm  /var/lib/containerd
sr0                              11:0    1 1024M  0 rom  
