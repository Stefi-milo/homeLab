Kubernetes Cluster Troubleshooting Summary
Environment

Cluster setup:

k8s-master
k8s-worker1
k8s-worker2

Runtime stack:

Kubernetes: v1.29.15

Container runtime: containerd

CNI plugin: Flannel

Pod network: 10.244.0.0/16

1️⃣ Initial Problem

After reinstalling Flannel, the Kubernetes node stayed in:

STATUS: NotReady

Running:

kubectl get nodes

Output:

k8s-master   NotReady   control-plane

The kubelet logs showed:

NetworkPluginNotReady
cni plugin not initialized
container runtime network not ready

This means:

Kubernetes could not initialize the CNI network

Pods could not attach to a network

Node remained NotReady

2️⃣ Investigation

Several checks were performed.

Flannel environment file
/run/flannel/subnet.env

Confirmed values:

FLANNEL_NETWORK=10.244.0.0/16
FLANNEL_SUBNET=10.244.0.1/24

So Flannel itself was running correctly.

CNI configuration

Checked:

/etc/cni/net.d/10-flannel.conflist

Configuration existed and referenced:

"type": "flannel"

Also verified that CNI binaries existed:

/opt/cni/bin

All plugins were present.

So the problem was not missing CNI plugins.

3️⃣ Kubelet Configuration Fix

The kubelet configuration was verified:

/var/lib/kubelet/config.yaml

Added explicit CNI configuration:

cniConfDir: /etc/cni/net.d
cniBinDir: /opt/cni/bin

Restarted kubelet:

systemctl daemon-reload
systemctl restart kubelet

However the node still remained:

NotReady
4️⃣ Clearing CNI State

Old CNI state was removed:

systemctl stop kubelet

rm -rf /var/lib/cni/*
rm -rf /var/run/flannel/subnet.env

systemctl start kubelet

But the problem still remained.

Logs still showed:

NetworkPluginNotReady
cni plugin not initialized
5️⃣ Root Cause Discovery

The actual issue was that containerd still held stale network state.

Even though:

Flannel was reinstalled

CNI configs were correct

kubelet restarted

containerd had not reloaded the new CNI configuration.

This caused Kubernetes to think:

CNI plugin not initialized
6️⃣ Final Fix

Restarting the container runtime fixed the problem:

systemctl restart containerd

Immediately after that:

kubectl get nodes

returned:

k8s-master   Ready   control-plane

The network initialized correctly and Kubernetes became healthy.

7️⃣ Worker Join Issue

When rejoining workers, the following error occurred:

FileAvailable--etc-kubernetes-kubelet.conf already exists
Port 10250 is in use
/etc/kubernetes/pki/ca.crt already exists

Cause:

Workers had partial previous join state.

Solution:

sudo kubeadm reset -f
sudo rm -rf /etc/cni/net.d
sudo rm -rf /var/lib/kubelet
sudo rm -rf /etc/kubernetes
sudo systemctl restart containerd

Then rejoin:

kubeadm join <master-ip>:6443 --token ...
8️⃣ Root Cause Summary

Primary root cause:

containerd was not restarted after Flannel reinstall

This caused:

container runtime network not ready
NetworkPluginNotReady
CNI plugin not initialized

Kubernetes could not attach pod networks until containerd restarted.

9️⃣ Correct Recovery Procedure (Future)

If reinstalling CNI (Flannel, Calico, etc):

systemctl restart containerd
systemctl restart kubelet

Optional cleanup:

rm -rf /var/lib/cni/*
rm -rf /var/run/flannel/*

Then verify:

kubectl get nodes
kubectl get pods -A
🔟 Key Lesson

Kubernetes networking involves three components:

Kubelet
CNI plugin (Flannel)
Container runtime (containerd)

If the runtime doesn't reload the CNI config, the cluster cannot initialize networking.

✅ Final status

Cluster working:

k8s-master   Ready
k8s-worker1  Ready
k8s-worker2  Ready

If you want, I can also show you a much faster recovery method that avoids rebuilding the cluster when Flannel breaks (takes ~30 seconds instead of a full reset).

show me

Here is the fast recovery procedure you can use next time when Flannel/CNI breaks so you don’t have to rebuild the cluster.
This usually fixes the cluster in 30–60 seconds.

⚡ Fast Kubernetes Network Recovery (Flannel / CNI)

This procedure fixes the most common problem:

Node NotReady
NetworkPluginNotReady
CNI plugin not initialized
1️⃣ Check cluster state
kubectl get nodes
kubectl get pods -A

Typical symptom:

k8s-master   NotReady

Flannel pods may be restarting or stuck.

2️⃣ Restart container runtime

Most common fix:

sudo systemctl restart containerd

Then:

kubectl get nodes

Often the node becomes Ready immediately.

3️⃣ Restart kubelet (if still broken)
sudo systemctl restart kubelet

Then check again:

kubectl get nodes
4️⃣ Clear CNI cache (if still broken)

Sometimes old CNI state remains.

sudo systemctl stop kubelet
sudo rm -rf /var/lib/cni/*
sudo rm -rf /var/run/flannel/*
sudo systemctl start kubelet

Then restart container runtime again:

sudo systemctl restart containerd
5️⃣ Restart Flannel pods

If Flannel itself got stuck:

kubectl delete pod -n kube-flannel -l app=flannel

Kubernetes will recreate them automatically.

Check:

kubectl get pods -n kube-flannel
6️⃣ Verify network
kubectl get nodes
kubectl get pods -A

Node should now show:

Ready
🔎 Why this works

Networking stack in Kubernetes:

kubelet
   ↓
containerd
   ↓
CNI plugin (Flannel)
   ↓
Pod networking

If containerd keeps old CNI state, Kubernetes reports:

NetworkPluginNotReady
cni plugin not initialized

Restarting containerd forces it to reload the CNI configuration.

🧠 Pro Tip (very useful)

When debugging cluster networking:

sudo journalctl -u kubelet -f

Look for:

cni plugin not initialized
NetworkPluginNotReady
container runtime network not ready

These almost always point to CNI or container runtime state issues.

🧰 Even Faster Debug Command

When nodes go NotReady, try this immediately:

sudo systemctl restart containerd kubelet

This alone fixes ~80% of Kubernetes CNI failures.
