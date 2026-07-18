** What is logging and why use it? **
- Logging is the automatic recording of system events, errors, and activities over time. 
- It's your system's black box — when something goes wrong, breaks, or gets hacked, logs tell you exactly what happened, when, and who did it. 
- Without logs you're completely blind.

** The /var/log directory **
The most important files you'll find there:

# Security & Access

syslog — the main system log, catches almost everything
auth.log — all authentication events: SSH logins, sudo usage, failed passwords
kern.log — kernel messages, hardware errors, driver issues

# Package Management

dpkg.log — every package installed, removed, or updated
apt/history.log — apt command history

# Services & Boot

boot.log — what happened during system startup
cron.log — scheduled job executions and failures
daemon.log — background service events

# Applications

nginx/access.log — every HTTP request to your web server
nginx/error.log — web server errors
mysql/error.log — database errors
php8.2-fpm.log — PHP errors

** Essential log commands**

# Reading logs:

bashtail /var/log/syslog              	# last 10 lines
tail -f /var/log/syslog           	# follow live in real time
tail -n 100 /var/log/syslog       	# last 100 lines
cat /var/log/auth.log             	# entire file
less /var/log/syslog              	# paginated reading, q to quit

# Searching logs:

bashgrep "error" /var/log/syslog              	# find errors
grep "Failed" /var/log/auth.log           	# failed logins
grep "sudo" /var/log/auth.log             	# sudo usage
grep -i "warn\|error\|fail" /var/log/syslog  	# multiple keywords

# journalctl — systemd logs:

bashjournalctl                        			# all logs
journalctl -f                     			# follow live
journalctl -u nginx               			# logs for specific service
journalctl -u ssh --since "1 hour ago"
journalctl -p err                 			# only errors
journalctl --since "2026-03-21" --until "2026-03-22"

** The logger command: **

bashlogger "something happened"                    	# write to syslog
logger -t myapp "application started"          		# with tag
logger -p auth.info "manual auth event"        		# specific facility
logger -p user.error "something broke"         		# as error level

- Useful for testing, scripts, and manually marking events in logs.

** Common troubleshooting scenarios **

# Who logged into my server?

bashlast                              	# all logins
lastb                             	# failed login attempts
grep "Accepted" /var/log/auth.log
grep "Failed" /var/log/auth.log

# Why did a service crash?

bashjournalctl -u servicename -n 50
journalctl -u servicename --since "10 minutes ago"
systemctl status servicename

# Is someone brute forcing my SSH?

bashgrep "Failed password" /var/log/auth.log | awk '{print $11}' | sort | uniq -c | sort -rn

# What happened at 3am?

bashgrep "Mar 22 03:" /var/log/syslog
journalctl --since "2026-03-22 03:00" --until "2026-03-22 04:00"

# Disk full investigation:

bashdu -sh /var/log/*                 	# what's eating disk space in logs
ls -lhS /var/log/                 	# largest files first

** Log rotation ** 

- logs don't grow forever, logrotate compresses and archives them automatically. 
- Config is in /etc/logrotate.d/. This is also why you'll see files like syslog.1, syslog.2.gz — those are older rotated logs.
