- KUBELET is a key component that runs on every node inside cluster
- acts as  a manager ensuring containers operate according to instructions from the control plane
- control plane sends commands via K8s API server to start,stop or restart containers


- also takes care of storage volumes and networking of containers

- KUBELET inetacts with CONTAINER RUNTIMES such as docker or containerd through the Container Runtime interface
- it reports the status of containers and the node back to the control plane for cluster overview

- KUBELET only manages containers created by Kubernetes ignoring external processes

- it runs as background process often managed by system tools like systemd
- provides HTTP endpoint for log streaming and troubleshooting commands inside containers

- understanding KUBELET is essential for troubleshooting and optimizing K8s cluster performance
