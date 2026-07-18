# Check that heartbeat is on Loki server rnning

cat /etc/cron.d/loki-heartbeat

# Check it's firing:

sudo grep heartbeat /var/log/syslog | tail -5

# Check all cron jobs running on the system:

**  System cron jobs **
ls /etc/cron.d/
cat /etc/crontab

** User cron jobs **

crontab -l
sudo crontab -l


**Cron schedule syntax explained:**


* * * * * root /usr/bin/logger -t heartbeat 'loki-server alive'
│ │ │ │ │
│ │ │ │ └── day of week (0-7, 0=Sunday)
│ │ │ └──── month (1-12)
│ │ └────── day of month (1-31)
│ └──────── hour (0-23)
└────────── minute (0-59)

* = every

# Common cron examples:

* * * * *        # every minute
0 * * * *        # every hour
0 0 * * *        # every day at midnight
0 0 * * 0        # every Sunday at midnight
0 0 1 * *        # first day of every month
*/5 * * * *      # every 5 minutes
0 9-17 * * 1-5   # every hour 9am-5pm Monday-Friday

# Why heartbeats matter in monitoring:

- Keeps labels alive in Loki's ingester memory
- Confirms the server is actually up and running
- Timestamps prove when a server was last seen alive
- If heartbeat stops → server is down or cron is broken
