                    Synology NAS

        WD30EFRX 3TB                 WD20EFPX 2TB
        /dev/sata2                   /dev/sata1
             |                            |
             |                            |
       Existing pool                 New pool
             |                            |
          /volume1                    /volume2
             |                            |
     +-------+-------+              +------+
     |               |              |
 Docker          Grafana/Loki    Hyper Backup
