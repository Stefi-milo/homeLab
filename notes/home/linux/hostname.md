# milo@k8s-worker1:/etc/netplan$ cat /etc/hostname 
k8s-worker1

# milo@k8s-worker1:/etc/netplan$ hostname
k8s-worker1

# milo@k8s-worker1:/etc/netplan$ hostnamectl 
 Static hostname: k8s-worker1
       Icon name: computer-vm
         Chassis: vm
      Machine ID: 52c412bcd9ce4d67b290877cd13cc2c5
         Boot ID: 82f0c8c6acb64d069a1b240fb140232e
  Virtualization: kvm
Operating System: Ubuntu 22.04.5 LTS  
          Kernel: Linux 5.15.0-171-generic
    Architecture: x86-64
 Hardware Vendor: QEMU
  Hardware Model: Standard PC _Q35 + ICH9, 2009_

# Change hostname
sudo hostnamectl set-hostname NEW_HOSTNAME

# When changing hostname it is recommended to update it in /etc/hosts !!
# It’s recommended because of how Linux resolves the local hostname
