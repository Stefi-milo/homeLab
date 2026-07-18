k8s-master:     2G RAM   2 core
k8s-worker1:    6G RAM   1 cores
k8s-worker2:    6G RAM   1 cores
postgresql:     4G RAM   1 core
oracle-db:      4G RAM   1 core
loki:           3G RAM   1 core
backup-agent:   1G RAM   1 core
game-server:    4G RAM   2 cores
vault:          1G RAM   1 core
─────────────────────────────────
Total:          31G RAM  13 cores


k8s-master:     
  scsi0  20G  /
  scsi1  20G  /var/lib/containerd
  scsi2  10G  /var/log
  Total: 50G of 60G quota

k8s-worker1/2:  
  scsi0  20G  /
  scsi1  60G  /var/lib/containerd
  scsi2  10G  /var/log
  Total: 90G of 100G quota

postgresql:     
  scsi0  20G  /
  scsi1  30G  /var/lib/postgresql
  scsi2  10G  /var/log
  Total: 60G quota ✓

oracle-db:   
  scsi0  20G  /
  scsi1  30G  /u01
  scsi2  10G  /var/log
  Total: 60G quota ✓

loki:           
  scsi0  20G  /
  scsi1  270G /var/lib/loki
  scsi2  10G  /var/log
  Total: 300G quota ✓

backup-agent:   
  scsi0  40G  /
  scsi1  10G  /var/log
  Total: 50G of 60G quota

game-server:    
  scsi0  20G  /
  scsi1  260G /opt/games
  scsi2  10G  /var/log
  Total: 290G of 300G quota

vault:          
  scsi0  15G  /
  scsi1  5G   /var/log
  Total: 20G quota ✓
