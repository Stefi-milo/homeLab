
kubectl apply -f https://raw.githubusercontent.com/flannel-io/flannel/master/ Documentation/kube-flannel.yml

#This command installs Flannel — the network plugin for your k8s cluster.
# What it does:

Downloads the Flannel configuration YAML from GitHub
Applies it to your cluster (kubectl apply)
Creates DaemonSets, ClusterRoles, ConfigMaps needed for networking

# Why you need it:
Kubernetes doesn't come with networking built in — it requires a CNI (Container Network Interface) plugin. Without it:
pods can't communicate with each other
pods can't communicate with services
cluster stays in NotReady state

# Flannel specifically:

Creates a virtual network overlay across all nodes
Assigns each node a subnet from your --pod-network-cidr=10.244.0.0/16
Routes traffic between pods on different nodes

# Think of it like:
k8s cluster = office building
pods        = people in the building
Flannel     = internal phone/network system
             without it people can't call each other
Other CNI alternatives to Flannel:

Calico — more features, network policies
Cilium — modern, eBPF based, best performance
Weave — simple, good for small clusters

For your homelab Flannel is the simplest choice. Calico or Cilium would be better if you need network policies between your apps later.
