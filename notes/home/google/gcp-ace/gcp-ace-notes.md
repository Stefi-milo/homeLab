```sh
## Role example

Custom roles require a YAML or JSON definition file. Example custom_role.yaml:

title: "Custom Role Example"
description: "A sample custom IAM role"
stage: "GA"
includedPermissions:
  - resourcemanager.projects.get
  - resourcemanager.projects.list
```

```sh
## Pub Sub

  - Pub/Sub is **asynchronous, event-driven messaging**
- Decouples producers and consumers
- Supports **push and pull subscriptions**
- Messages must be **acknowledged**
- Schema enforcement is optional
- Pub/Sub Lite is **not the same** as standard Pub/Sub
```

```sh
## Kubernetes

**Kubernetes** is an **open-source container orchestration system** for automating **deployment, scaling, and management** of containers.

Originally created by Google and now maintained by the **Cloud Native Computing Foundation (CNCF) as a CNCF Project**

Kubernetes is commonly called **K8s** The 8 represent the remaining letters “ubernete”

**The advantage of Kubernetes over Docker is the ability to run “container apps” distributed across multiple VMs

A unique component of Kubernetes are **Pods**.

A pod is a group of one or more containers with shared storage, network resources, and other shared settings.

Kubernetes is ideally for micro-service architectures where a company has tens to **hundreds of services** they need to manage
```

```sh
  **Manifest (not technical description)**

A Manifest file is a document that is commonly used for customs to list the contents of cargo, or passengers. Its an itemized list of things.

**Manifest File (in the context of Kubernetes)**

A Manifest file is a generalized name **for any Kubernetes Configuration File** that define the configuration of various K8s components.

These are all Manifest files with specific purposes:

- Deployment File
- PodSpec File
- Network Policy File

Manifest Files can be written in either:

- YAML
- JSON

A manifest can contain **multiple** K8s component definitions/configurations.

In YAML you can see the **three hyphens ---** is used to defined multiple components.

**kubectl apply** command is generally used to deploy manifest files

**Resource Configuration file** is sometimes used to describe multiple resources in a manifest.
```

```sh
## Kubernetes Components Overview

### Cluster

- A logical grouping of all Kubernetes components.
- Encompasses **control plane** and **worker nodes**.

### Namespace

- Logical grouping of components within a cluster.
- Used to isolate workloads and manage resources efficiently.

### Node

- A **virtual or physical machine** hosting workloads.
- **Control Plane Node:** Manages cluster state.
- **Worker Node:** Runs applications and workloads.

### Pod

- The smallest deployable unit in Kubernetes.
- An **abstraction over a container**.
- Each pod runs one or more containers that share resources and networking.

### Service

- Provides a **stable IP and DNS name** for a set of pods.
- Ensures connectivity even if pods restart.
- Can act as a **load balancer**.

### Ingress

- Manages **HTTP/S routing** to services from outside the cluster.
- Can include TLS termination.

### API Server

- Entry point for all K8s commands via **kubectl** or HTTP API.
- Handles communication between components.

### Kubelet

- Agent running on each node.
- Ensures containers are running as defined in Pod specs.
- Communicates with **API Server**.

### Kubectl

- Command Line Interface (CLI) for managing the cluster.
- Sends commands to the **API Server**.

### Cloud Controller Manager

- Connects Kubernetes to cloud provider APIs (e.g., **AWS, Azure, GCP**).

### Controller Manager

- Watches cluster state and reconciles desired vs. current state.
- Manages controllers like Node, Replication, and Endpoint controllers.

### Scheduler

- Assigns pods to nodes based on available resources and constraints.

### Kube Proxy

- Maintains network rules on nodes for routing and load balancing of pods.

### Network Policy

- Acts as a virtual firewall at **pod** or **namespace** level.

### ConfigMap

- Stores **non-confidential configuration data** in key-value pairs.
- Decouples configuration from container images.

### Secret

- Stores **sensitive data** (e.g., passwords, tokens, keys).
- Base64-encoded but should be encrypted in production.

### Volumes

- Provides **persistent storage** for pods.
- Can be local or remote (e.g., cloud storage).

### StatefulSet

- Manages **stateful applications** requiring stable IDs and storage.
- Used for databases or apps needing ordered deployment.

### ReplicaSet

- Ensures a specified number of pod replicas are running.
- Provides high availability and fault tolerance.

### Deployment

- Defines **blueprints for pods**.
- Automates rolling updates and rollbacks.
```

```sh
## Control Plane and Worker Nodes

**Control Plane Node** (Formally known as Master Node)

Manages processes like scheduling, restarting nodes, maintaining the overall state of the cluster

- **API Server** – the backbone of communication
- **Scheduler** – determines where to start a pod on worker node
- **Controller Manager** – detect state changes (if pod crashes, restart it)
- **etcd** – A Key/Value Store that stores the state of the cluster
- ~~Kubelet – Allows user to interact with the node via KubeCTL~~
- **Cloud Control Manager (optional)** – Integrates with the cloud provider

**Worker Node**

Does the work of running your app in pods and containers

**Components:**

- Kubelet
- Kube Proxy
- Container Runtime
- Pods and Containers
```

```sh
## Pods

Pods are the smallest unit in Kubernetes.

Pods abstract away the container layer so you can directly interact with the Kubernetes Layer.

A Pod is intended to run one application in multiple containers

- Database Pod, Job Pod, Frontend App Pod, Backend App Pod
- You can run multiple apps in a pod but those containers will tightly dependent.

Each Pod gets its own private IP address

- Containers will run on different ports
- Containers can talk to each other via localhost

Each Pod can have a shared storage volume attached.

- All containers will share the same volume

When the last remaining container dies (maybe crashes) in a pod so does the pod

- When a replacement pod is created, the pod will have an IP address will be assigned.
    - IP addresses are Ephemeral, (temporary) for pods, they don’t by default persist.

Get pods and show their IP addresses

kubectl get pod -o wide
```

```sh
## API Server

The core of the Kubernetes control plane is the API server.

The API server exposes an HTTP API that lets end-users, different parts of your cluster, and external components communicate with one another.

The Kubernetes API lets you query and manipulates the state of API objects in Kubernetes (for example: Pods, Namespaces, ConfigMaps, and Events).

The API server is a component of the Kubernetes control plane that exposes the Kubernetes API. The API server is the front end for the Kubernetes control plane.

The main implementation of a Kubernetes API server is kube-apiserver.

kube-apiserver is designed to scale horizontally—that is, it scales by deploying more instances.

You can run several instances of kube-apiserver and balance traffic between those instances.

Everything has to **go through the API Server**.

You can interact with the API Server in three ways:

- UI*
- API
- CLI KubeCTL
```

```sh
## Deployment

A Deployment provides declarative updates for Pods and ReplicaSets.

A Deployment Controller changes the actual state to the desired state at a controlled rate.

- The default Deployment Controller can be swapped out for other deployments tools eg:
    - Argo CD, Flux, Jenkin X…..

A Deployment define the desired state of ReplicaSets and Pods.

A deployment will create and manage a ReplicaSet.

A ReplicaSet will manage replicas of pod.
```