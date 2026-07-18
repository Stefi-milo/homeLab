CERTBOT TROUBLESHOOTING WHEN CERT EXPIRE


1. Check all installed certificates
Shows all certificates Certbot knows about:

sudo certbot certificates

Use this to:

see active certs
see expiry dates
detect duplicates like -0001



2. Check which certificate NGINX is using
Find all references to Let’s Encrypt certs in your web server configs:

grep -R "/etc/letsencrypt/live/" /etc/nginx /etc/apache2 2>/dev/null

Use this to:

confirm active cert in production
detect unused / old certs
avoid deleting active certs by mistake



3. Delete an old / expired certificate (Certbot safe method)
sudo certbot delete --cert-name karatemilo.com

Use this to:

remove unused or expired certificates
clean Certbot certificate list

Certbot may refuse if internal metadata is already gone.



4. Check certificate files on disk
sudo ls /etc/letsencrypt/live/

Shows:

currently active certificate folders
what NGINX can actually use



5. Check deeper Certbot storage (advanced cleanup)
sudo ls /etc/letsencrypt/archive/
sudo ls /etc/letsencrypt/renewal/

Use this to:

detect leftover orphan certificates
confirm full cleanup after deletion



6. Manual cleanup (ONLY if leftovers exist)
sudo rm -rf /etc/letsencrypt/archive/karatemilo.com
sudo rm -f /etc/letsencrypt/renewal/karatemilo.com.conf

Use only when:

Certbot delete partially failed
orphan files remain


NGINX CERT CHECK / MAINTENANCE COMMANDS



7. Find SSL cert used in NGINX configs
grep -R "ssl_certificate" /etc/nginx/sites-available /etc/nginx/sites-enabled

Shows:

which cert each domain uses
ensures no expired cert is active


8. Reload NGINX after cert changes
sudo systemctl reload nginx

Use after:

deleting certs
switching cert paths
renewing certificates

(no downtime reload)



9. Restart NGINX (full restart)
sudo systemctl restart nginx

Use when:

reload is not enough
SSL changes don’t apply correctly


10. Test NGINX configuration before reload
sudo nginx -t

Use to:

verify config is valid
prevent breaking HTTPS before reload


SUMMARY FLOW (HOW YOU USED IT)

Typical cleanup flow:

certbot certificates
        ↓
grep nginx config
        ↓
verify active cert
        ↓
certbot delete old cert
        ↓
certbot certificates (confirm)
        ↓
sudo systemctl reload nginx
