** Kubelet TLS Authentication **

# What is Kubelet and Why Scrape It?

- Kubelet runs on every k8s node and exposes cAdvisor metrics at :10250/metrics/cadvisor. 
- These give you per-container/per-pod CPU, memory, network metrics — things node-exporter can't provide since node-exporter only sees the host level. 
- Without kubelet scraping you can't answer "which pod is eating all the RAM?"

# Why Authentication is Required

Kubelet's API is protected by two layers:

1. TLS (Transport Security) — ensures you're talking to the real kubelet, not an imposter. Kubelet presents a certificate; Prometheus verifies it against a CA.
2. Bearer Token (Authentication) — proves to kubelet that Prometheus is allowed to read metrics. Without a valid token, kubelet returns 401.

Both must work together. TLS without auth = encrypted but unauthorized. Auth without TLS = credentials sent in cleartext.

# What We Did Step by Step

1. Created a Service Account & Token

kubectl create serviceaccount prometheus -n monitoring
kubectl create clusterrolebinding prometheus --clusterrole=cluster-admin --serviceaccount=monitoring:prometheus

- This gives Prometheus an identity inside k8s with permissions to scrape kubelet.

kubectl apply -f - <<EOF
apiVersion: v1
kind: Secret
metadata:
  name: prometheus-token
  namespace: monitoring
  annotations:
    kubernetes.io/service-account.name: prometheus
type: kubernetes.io/service-account-token
EOF

- This creates a long-lived token (newer k8s versions use short-lived tokens by default, so we explicitly created a permanent one).

2. Extracted Token and CA Cert

kubectl get secret prometheus-token -n monitoring -o jsonpath='{.data.token}' | base64 -d > prometheus-token

- The token is a JWT that kubelet validates against the k8s API server.

3. Mounted Into Prometheus Container

- In docker-compose.yml:

volumes:
  - ./prometheus-token:/etc/prometheus/prometheus-token:ro
  - ./ca.crt:/etc/prometheus/ca.crt:ro

- And in prometheus.yml:

authorization:
  credentials_file: /etc/prometheus/prometheus-token
tls_config:
  ca_file: /etc/prometheus/ca.crt

4. Fixed the TLS Certificate Problem

# Problem 1 — IP SAN mismatch: Kubelet's cert only had DNS:master not the IP 192.168.100.249. 
- Fixed by using hostnames in prometheus.yml and adding extra_hosts to docker-compose.yml.

# Problem 2 — Unknown CA: Kubelet was using a self-generated CA (master-ca@1774451202) stored only in memory — impossible to trust externally.
- Fix — serverTLSBootstrap: Added to /var/lib/kubelet/config.yaml on all nodes:
- yamlserverTLSBootstrap: true

- This tells kubelet to request a serving certificate from the k8s API server (signed by the cluster CA) instead of generating its own self-signed one.

5. Approved the CSRs

- When kubelet requests a new cert, it creates a Certificate Signing Request in k8s:

kubectl get csr

kubectl certificate approve csr-297nr csr-df7zr csr-zzvkk

# After approval, kubelet gets a cert signed by /etc/kubernetes/pki/ca.crt — the same CA Prometheus now trusts.

6. Copied the Correct CA to Pi

scp -P 2200 /etc/kubernetes/pki/ca.crt milo@192.168.100.253:~/Docker/ca.crt

# How to Troubleshoot If It Breaks
# Symptom: x509: certificate signed by unknown authority

# CA cert on Pi doesn't match what signed kubelet's cert
- Check: sudo openssl x509 -in /var/lib/kubelet/pki/kubelet.crt -noout -text | grep Issuer
- Fix: re-copy /etc/kubernetes/pki/ca.crt to Pi

# Symptom: x509: cannot validate certificate for IP because it doesn't contain any IP SANs
- Prometheus is connecting via IP but cert only has DNS names
- Fix: use hostnames in prometheus.yml + extra_hosts in docker-compose.yml

# Symptom: 401 Unauthorized

# Token is expired, wrong, or service account was deleted
- Check: kubectl get secret prometheus-token -n monitoring
- Fix: recreate the secret and re-copy the token to Pi

# Symptom: 403 Forbidden
# Service account exists but lacks permissions
- Check: kubectl get clusterrolebinding prometheus
- Fix: recreate the clusterrolebinding

# Symptom: CSRs stuck in Approved but not Issued
- Workers haven't restarted kubelet with serverTLSBootstrap: true
- Fix: add the config to all nodes and sudo systemctl restart kubelet

# Symptom: New node added, kubelet target DOWN

New node needs serverTLSBootstrap: true in its kubelet config
Its CSR needs manual approval: kubectl get csr then kubectl certificate approve <name>
Add hostname to extra_hosts in docker-compose.yml and target to prometheus.yml


** Certificate Renewal **

- Kubelet certs rotate automatically before expiry when rotateCertificates: true is set (already in your config). 
- New CSRs will appear and need approval. To auto-approve future CSRs install the approver:

kubectl apply -f https://raw.githubusercontent.com/postfinance/kubelet-csr-approver/main/deploy/k8s/deploy.yaml

# This approves valid kubelet serving CSRs automatically so you never need to manually approve again.
