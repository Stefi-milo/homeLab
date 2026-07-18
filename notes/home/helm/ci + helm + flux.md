s

```sh
CI responsibility :
build --> test --> package it (but not deploy)

CI OUTPUT is a container image, a chart package, a versioned artifact

DO NOT use kubectl apply / helm upgrade
```

```sh
CI updates git
flux notices changes
cluster converges
```

```sh
HELM used for helm charts to render a k8s manifest
- describing how application should look like in k8s cluster
- but not to do deployment scheduling, not responsible for orchestrartion
```

```sh
- FLUX a gitops control plane for kubernetes
- flux turns git into living control system, not just a storage
- runs inside k8s cluster
- decides when and how are changes applied
- treats git as a source of truth
- watches git for declarative changes 
```

```sh
ARTIFACT vs. MANIFEST
Artifact = packaged input (what you install from)  
Manifest = rendered output (what Kubernetes runs)

|Stage        |Object|

|Recipe book   |Artifact|
|Cooked meal   |Manifest|
You don’t eat the recipe — you eat the cooked result.

# Pipeline view
`Artifact (chart package)         ↓ render/template Manifest (plain YAML)         ↓ apply Running resources`
Artifact = input  
Manifest = output


# Where rendering happens
Depends on tool:
- Helm CLI → renders templates
- Flux helm-controller → renders during install
- Argo CD → renders before apply
But manifests always come after artifacts.

# Key differences table
|Aspect             |Artifact                |Manifest

|Format             |Packaged archive        |Plain YAML
|Purpose            |Installation source     |Cluster state definition
|Readable by K8s    |❌ No                   |✅ Yes
|Contains templates |Often yes               |No
|Versioned          |Yes                     |Indirectly via Git
|Produced by        |Source-controller       |Helm/Kustomize/render step


Helm repo
   ↓
Chart.tgz  ← Artifact
   ↓ helm render
Deployment.yaml ← Manifest
   ↓
kubectl apply



|Flux object       |Produces|

|HelmChart         |Artifact|
|GitRepository     |Artifact|
|Kustomization     |Manifests|
|HelmRelease       |Manifests (via Helm render)|



Helm charts don’t store ready-to-apply Kubernetes manifests.  
They contain templates (parameterized YAML files) plus values.

When Helm renders a chart, it:

1. Takes the chart templates (`templates/*.yaml`)
2. Applies your values (`values.yaml`, overrides, HelmRelease spec, etc.)
3. Produces final plain YAML manifests
    
Those output files are what Kubernetes actually understands.
```