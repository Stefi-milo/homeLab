[myservers]
switch ansible_host=192.168.88.2 ansible_user=admin ansible_password=secret ansible_network_os=routeros ansible_connection=network_cli
router ansible_host=192.168.88.1 ansible_user=admin ansible_password=secret ansible_network_os=routeros ansible_connection=network_cli
raspberri ansible_host=192.168.100.253 ansible_port=2200 ansible_python_interpreter=/usr/bin/python3
synology ansible_host=192.168.10.10 ansible_port=2200 ansible_user=Stefi-milo ansible_python_interpreter=/usr/bin/python3
k8smaster ansible_host=192.168.100.235 ansible_port=2200 ansible_python_interpreter=/usr/bin/python3
k8sworker1 ansible_host=192.168.100.233 ansible_port=2200 ansible_python_interpreter=/usr/bin/python3
k8sworker2 ansible_host=192.168.100.234 ansible_port=2200 ansible_python_interpreter=/usr/bin/python3
dbmaster ansible_host=192.168.100.248 ansible_port=2200 ansible_python_interpreter=/usr/bin/python3
dbslave ansible_host=192.168.100.236 ansible_port=2200 ansible_python_interpreter=/usr/bin/python3

