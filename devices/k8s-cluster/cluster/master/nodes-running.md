milo@master:~$ kubectl get nodes
NAME          STATUS   ROLES           AGE   VERSION
k8s-master    Ready    control-plane   11d   v1.29.15
k8s-worker1   Ready    <none>          10d   v1.29.15
k8s-worker2   Ready    <none>          10d   v1.29.15

milo@master:~$ kubectl get namespaces
NAME              STATUS   AGE
default           Active   11d
kube-flannel      Active   11d
kube-node-lease   Active   11d
kube-public       Active   11d
kube-system       Active   11d

