milo@pi:~ $ docker ps
CONTAINER ID   IMAGE                                    COMMAND                  CREATED          STATUS                  PORTS                                         NAMES
626ca4ec9911   ghcr.io/stefi-milo/game:4b0761b7         "/docker-entrypoint.…"   30 minutes ago   Up 30 minutes           0.0.0.0:8080->80/tcp, [::]:8080->80/tcp       home-arcade
c1e6feae4bd1   prom/prometheus:v2.54.1                  "/bin/prometheus --c…"   8 weeks ago      Up 26 hours             0.0.0.0:9090->9090/tcp, [::]:9090->9090/tcp   prometheus
c2538bcaf547   grafana/grafana:11.1.0                   "/run.sh"                8 weeks ago      Up 26 hours             0.0.0.0:3000->3000/tcp, [::]:3000->3000/tcp   grafana
a1326ab076d2   prom/node-exporter:v1.8.2                "/bin/node_exporter …"   8 weeks ago      Up 26 hours             9100/tcp                                      node-exporter
2cbee8445369   prompve/prometheus-pve-exporter:latest   "/opt/prometheus-pve…"   8 weeks ago      Up 26 hours             0.0.0.0:9221->9221/tcp, [::]:9221->9221/tcp   proxmox-exporter
9610889f9cf7   prom/mysqld-exporter:v0.15.1             "/bin/mysqld_exporte…"   8 weeks ago      Up 26 hours             0.0.0.0:9104->9104/tcp, [::]:9104->9104/tcp   mysqld-exporter
7bd6d080441d   prom/snmp-exporter:v0.27.0               "/bin/snmp_exporter …"   8 weeks ago      Up 26 hours             9116/tcp                                      snmp-exporter
d9e7d62f035d   ghcr.io/gethomepage/homepage:latest      "docker-entrypoint.s…"   2 months ago     Up 26 hours (healthy)   0.0.0.0:3002->3000/tcp, [::]:3002->3000/tcp   homepage
