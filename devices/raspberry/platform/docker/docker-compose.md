milo@pi:~/Docker $ cat docker-compose.yml 
services:
  homepage:
    image: ghcr.io/gethomepage/homepage:latest
    container_name: homepage
    ports:
      - "3002:3000"
    volumes:
      - ./homepage:/app/config
      - /var/run/docker.sock:/var/run/docker.sock
    group_add:
      - "991"
    environment:
      - HOMEPAGE_ALLOWED_HOSTS=*
    restart: unless-stopped
    networks:
      - monitoring

  proxmox-exporter:
    image: prompve/prometheus-pve-exporter:latest
    container_name: proxmox-exporter
    ports:
      - "9221:9221"
    environment:
      PVE_HOST: "https://192.168.100.254:8006"
      PVE_USER: "prometheus@pve"
      PVE_TOKEN_NAME: "exporter"
      PVE_TOKEN_VALUE: "${PVE_TOKEN_VALUE}"
      PVE_VERIFY_SSL: "false"
    networks:
      - monitoring
    restart: unless-stopped

  prometheus:
    image: prom/prometheus:v2.54.1
    container_name: prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml:ro
      - ./prometheus-token:/etc/prometheus/prometheus-token:ro
      - ./ca.crt:/etc/prometheus/ca.crt:ro
    extra_hosts:
      - "master:192.168.100.249"
      - "worker1:192.168.100.248"
      - "worker2:192.168.100.243"
    networks:
      - monitoring
    restart: unless-stopped

  snmp-exporter:
    image: prom/snmp-exporter:v0.27.0
    container_name: snmp-exporter
    networks:
      - monitoring
    restart: unless-stopped
    volumes:
      - /home/milo/Docker/snmp.yml:/etc/snmp_exporter/snmp.yml:ro

  node-exporter:
    image: prom/node-exporter:v1.8.2
    container_name: node-exporter
    hostname: pi
    restart: unless-stopped
    networks:
      - monitoring
    pid: host
    volumes:
      - "/:/host:ro,rslave"
    command:
      - '--path.rootfs=/host'

  mysqld-exporter:
    image: prom/mysqld-exporter:v0.15.1
    container_name: mysqld-exporter
    ports:
      - "9104:9104"
    command:
      - "--config.my-cnf=/etc/mysql/my.cnf"
    volumes:
      - ./my.cnf:/etc/mysql/my.cnf:ro
    restart: unless-stopped
    networks:
      - monitoring

  grafana:
    image: grafana/grafana:11.1.0
    container_name: grafana
    ports:
      - "3000:3000"
    volumes:
      - ./grafana-data:/var/lib/grafana
      - ./grafana/provisioning:/etc/grafana/provisioning:ro
    environment:
      - GF_AUTH_ANONYMOUS_ENABLED=true
      - GF_AUTH_ANONYMOUS_ORG_ROLE=Viewer
      - GF_AUTH_ANONYMOUS_ORG_NAME=Main Org.
      - GF_USERS_ALLOW_SIGN_UP=false
      - GF_EXPLORE_ENABLED=false
      - GF_SECURITY_ADMIN_USER=xxxx
      - GF_SECURITY_ADMIN_PASSWORD: xxxx
    extra_hosts:
      - "host.docker.internal:host-gateway"
    networks:
      - monitoring
    restart: unless-stopped

  promtail:
    image: grafana/promtail:3.6.0
    container_name: promtail
    user: root
    group_add:
      - "991"
    volumes:
      - ./promtail-config.yaml:/mnt/config/promtail-config.yaml:ro
      - /var/log:/var/log
      - /var/lib/docker/containers:/var/lib/docker/containers:ro
      - /var/run/docker.sock:/var/run/docker.sock
    command: -config.file=/mnt/config/promtail-config.yaml
    networks:
      - monitoring
    restart: unless-stopped

networks:
  monitoring:
    driver: bridge
