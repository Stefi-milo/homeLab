**Prerequisites**
#To follow along with this tutorial, you’ll need:

- At least two Ubuntu Server 22.04 instances (one for the controller, one for at least one node)
- A static IP address or DHCP reservation on those instances, so their IP addresses cannot change
- The controller node should have at least 2GB of RAM and 2 cores
- The node instances can have a single gigabyte of RAM and a single CPU core (or more if you prefer)
- Note: This tutorial utilizes Ubuntu Server 22.04. If you choose to use a different distribution or a different version of Ubuntu, these commands may not work.

# Setting up the cluster
The following commands are to be run on the controller node (unless otherwise stated).

# Setting up a static IP
Note, a static lease is preferred, but you can use the following Netplan config example to serve as a basis of yours if you need to set up a static IP.

network:
    version: 2
    ethernets:
        eth0:
            addresses: [10.10.10.213/24]
            nameservers:
                addresses: [10.10.10.1]
            routes:
                - to: default
                  via: 10.10.10.1
# Installing containerd
# This Kubernetes cluster will utilize the containerd runtime. To set that up, we’ll first need to install the required package:

sudo apt install containerd
# Create the initial configuration:

sudo mkdir /etc/containerd
containerd config default | sudo tee /etc/containerd/config.toml
# For this cluster to work properly, we’ll need to enable SystemdCgroup within the configuration. To do that, we’ll need to edit the config we’ve just created:

sudo nano /etc/containerd/config.toml
# Within that file, find the following line of text:

[plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc.options]
Underneath that, find the SystemdCgroup option and change it to true, which should look like this:

SystemdCgroup = true
Disable swap
# Kubernetes requires swap to be disabled. To turn off swap, we can run the following command:

sudo swapoff -a
# Next, edit the /etc/fstab file and comment out the line that corresponds to swap (if present). This will help ensure swap doesn’t end up getting turned back on after reboot.

Enable bridging
# To enable bridging, we only need to edit one config file:

sudo nano /etc/sysctl.conf
Within that file, look for the following line:

#net.ipv4.ip_forward=1
Uncomment that line by removing the # symbol in front of it, which should make it look like this:

net.ipv4.ip_forward=1
Enable br_netfilter
#The next step is to enable br_netfilter by editing yet another config file:

sudo nano /etc/modules-load.d/k8s.conf
# Add the following to that file (the file should actually be empty at first):

br_netfilter
# Reboot your servers
Reboot each of your instances to ensure all of our changes so far are in place:

sudo reboot
**Installing Kubernetes**
The next step is to install the packages that are required for Kubernetes. First, we’ll add the required GPG key:

sudo curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://
packages.cloud.google.com/apt/doc/apt-key.gpg
After that, install the packages that are required for Kubernetes:

sudo apt install kubeadm kubectl kubelet
# Controller node only: Initialize our Kubernetes cluster
So long as you have everything complete so far, you can initialize the Kubernetes cluster now. Be sure to customize the first IP address shown here (not the second) and also change the name to match the name of your controller.

sudo kubeadm init --control-plane-endpoint=172.16.250.216 --node-name
controller --pod-network-cidr=10.244.0.0/16
# After the initialization finishes, you should see at least four commands printed within the output.

Setting up our user account to manage the cluster
# Three commands will be shown in the output from the previous command, and these commands will give our user account access to manage our cluster. Here are those related commands to save you from having to search the output for them:

mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
suod chown $(id -u):$(id -g) $HOME/.kube/config
Those commands should allow you to manage the cluster, without needing to use the root account to do so.

**Install an Overlay Network**

# The following command will install the Flannel overlay network (an overlay network is required for this to function).

kubectl apply -f https://raw.githubusercontent.com/flannel-io/flannel/master/
Documentation/kube-flannel.yml
# Adding Nodes
The join command, which you will receive from the output once you initialize the cluster, can be ran on your node instances now to get them joined to the cluster. The following command will help you monitor which nodes have been added to the controller (it can take several minutes for them to appear):

kubectl get nodes
# If for some reason the join command has expired, the following command will provide you with a new one:

kubeadm token create --print-join-command
Deploying a container within our cluster
# Create the file pod.yml with the following contents:

apiVersion: v1
kind: Pod
metadata:
Chapter 18 25
 
name: nginx-example
  labels:
    app: nginx
spec:
  containers:
    - name: nginx
      image: linuxserver/nginx
      ports:
        - containerPort: 80
          name: "nginx-http"
Apply the file with the following command:

kubectl apply -f pod.yml
You can check the status of this deployment with the following command:

kubectl get pods
# Creating a NodePort Service
# Setting up a NodePort service is one of the methods we can use to be able to access the container from outside the pod network. To set this up, first create the following file as service-nodeport.yml:

apiVersion: v1
kind: Service
metadata:
  name: nginx-example
spec:
  type: NodePort
  ports:
    - name: http
      port: 80
      nodePort: 30080
      targetPort: nginx-http
  selector:
app: nginx
You can apply that file with the following command:

kubectl apply -f service-nodeport.yml
# To check the status of the service deployment, you can use the following command:

kubectl get service



