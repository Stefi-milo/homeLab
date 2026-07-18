# You can see three jobs for k8s-master:

syslog — system logs from /var/log/syslog
auth — SSH logins, sudo usage from /var/log/auth.log
kubernetes — logs from all Kubernetes pods running on this node from /var/log/pods/*/*/*.log

# The kubernetes job is the most valuable one. It scrapes logs from every pod running on the node — so you can see:

kube-scheduler logs
kube-controller-manager logs
etcd logs
coredns logs
Any application pods you deploy

The path /var/log/pods/*/*/*.log follows Kubernetes' standard log structure:
/var/log/pods/
  └── kube-system_kube-scheduler-k8s-master_xxx/
        └── kube-scheduler/
              └── 0.log, 1.log, 2.log...
