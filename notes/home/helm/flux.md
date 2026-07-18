
```sh
flux get helmchart 
	- Downloaded installers
	- Chart artifacts cached by source-controller

Which chart packages Flux has downloaded and cached from Helm repositories.
Whether the source-controller downloaded chart package and made an artifact
	- Chart name   
	- Version 
	- Whether it was downloaded successfully 
	- The artifact file created
```

```sh
flux get helmrelease
	- Installed apps
	- Helm releases managed by helm-controller

Shows Helm releases installed and managed by Flux (running apps + their Helm state)
It’s not the artifact itself — it’s what was installed from the artifact.
	- Release name
    - Ready status
    - Last applied revision
    - Chart version
    - Last reconciliation time
      
When Flux fetches a chart, it creates an Artifact: downloaded, versioned, cached chart package
```

```sh
ARTIFACT relationship :

HelmRepository (storage for helmrelease)
     ↓
HelmChart
     ↓ (produces artifact)
Chart artifact (.tgz cached)
     ↓
HelmRelease uses it
     ↓
Helm install/upgrade
```

```sh
|Flux object         | Human analogy             |What it does|

1|HelmRepository     |App Store                  |Where apps live|
2|HelmChart          |Downloaded installer file  |The app package on disk|
3|HelmRelease        |Installed app              |Running app on your phone|

1: You tell Flux:
> “Charts are in this Helm repo URL.”

2: You tell Flux:
> “Download nginx chart version 1.2.3.”
Flux then:
- Connects to repo   
- Downloads chart `.tgz`  
- Stores it inside cluster  
- Versions it  
- Verifies checksum
This stored package = artifact

3: Now you tell Flux:
> “Take that downloaded chart and install it with these values.”
Flux (helm-controller) then runs Helm lifecycle:
- `helm install` 
- or `helm upgrade`
This creates real Kubernetes resources:
- Deployments
- Services
- ConfigMaps 
- etc.
Now the app is running.
```

```sh
- system install on the CLUSTER, not locally!
- flux system needs to be a part of git for the loop to happen 
```

```sh
flux --version

```

```sh
- cluster becomes an execution engine not a cluster decision maker 
- decisions need to be made outside the cluster
  
- GIT does not match the cluster state !
  
- deployments rely on manual kubectl apply, ad-hoc helm upgrades, undocumented hotfixes
  
```

```sh
IMPERATIVE vs. DECLARATIVE

Declarative: 
- describe the end result
- let the system converge 
- state is explicit and reviewable
- the system is smart
  
Imperative:
- step by step command
- explicit instructions
- state is an indirect result
- hard to replay reliably    
- the system is stupid
```

```sh
GIT AS THE CONTROL PLANE
GITOPS :
- authoritative source of truth
- the interface for a change
GIT :
- git that already provide : diff, history, review workflow, versioning
```

```sh
DESIRED STATE VS ACTUAL STATE repeatedly
desired state <--> RECONCILIATION LOOP (observe) <--> current state
```

```sh
PUSH git model (cluster fetches from git)
PULL git 
model (CI has cluster access)
```

```sh
From Helm to FLux
- FLUX control layer
- CLUSTER execution layer
- HELM definition layer
  
- Flux triggers Helm at the right time
- HELM decribes, FLUX decides, K8s executes !
```

```sh
- CI builds artifacts
- HELM packages intent
- FLUX enforces state
```

```sh
FLUX ARCHITECTURE

- flux is glued to the cluster not a pod
- each controller watches specific CRDs and reconciles them using K8s control loop
  
source --> reconciliation --> cluster

Workflow:
- source become artifact (image,binary,... packed and shipped)
- workload controllers apply it
- status vs events tell you what happened
```

```sh
flux bootstrap github (chosing github as a source code)
```

```sh
FLUX is split by RESPONSIBILITY
- in flux you debug by controller boundary (logs separated by controllers)
  
- "source-controller" (fetches sources on an interval, verify and authenticate, produces artifact from git)
  
- "kustomize-controller" (konzume artifact and turnes it to the k8s objects)
  (apply phase ; dry-run failed,...)
  
- "helm-controller" (watches HelmRelease objects CRDs)
  
- "notification-controller" 
  
- "image-reflector-controller" (nice add-on)
  
EACH controller owns one API surface CRDs !!
- why controller : separation, easy find failure
```

```sh
HEM is a package manager that creates release with the use of values.yaml 
```

```sh
Flux first turns git into an artifact than reconciles from the artifact

ARTIFACT : a versioned snapshot of the source
```

```sh
HOW TO FIND HELM RELEASE FROM THE CLUSTER
flux get helmreleases -A
kubectl -n demo get helmreleases  (both are the same)
```

```sh
flux get sources -A
flux get kustomizations -A (see repo where flux connect)
kubectl -n flux-system describe kustomization apps-demo
flux get all -A

kubectl get gitrepositories,helmrepositories,kustomizations,helmreleases -A
```

```sh
- if something not defined in git flux will not correct it !

- typical failure points:
source phase (repo not ready), apply phase (validation or dry-run failed), release phase (helm chart not found, values.yaml errors,..)
```

```sh
flux bootstrap !!!
- use the command once only, most important one
- creates cluster runtime and git contract
- installs flux controllers, sets up authentication
- commits initial sync manifests into git (DO git pull first!)
- BEFORE decide which git path represents the cluster 
  
fluxbootstrap --owner --path --repository --branch 

flux check --pre (checks the flux is set up corrctly)
flux check (if all flux controllers are healthy)

kubectl get pods -n flux-system (should see all ready controllers in cluster)
```

```sh
- AUDIT TRAIL becomes git history not terminal history

```

```sh
!!!

KEEP changes small and observable (one intent per PR)
PROTECT flux system folder with reviews and approvals
ROLLBACK means revert commit, not rerun pipelines
```

```sh
WHAT WE NEED FOR THE FLUX
- authenticate to github (or add personal access token)
- neew write permissions to repository as flux writes into it
	- kubectl cluster
	- git available
	- flux cli
	- github access
```

```sh
TO RECONCILE (speed up reconcile loop)
1 flux reconcile source git flux-system -n flux-system
2 flux reconcile kustomization flux-system -n flux-system
```

```sh
MANUALLY SCALING PODS/REPLICAS
kubectl -n demo scale deploy/podinfo --replicas=3

- flux will override the state!
- better to update helmrelease to do it properly! 
```

```sh
TROUBLESHOOTING
flux get sources -A         (if it fetched helm repository)
flux get kustomizations -A  (to see reconciliation status)
flux get helmreleases -A
```

```sh
FIXING BROKEN app/HelmRelease

1 flux suspend helmrelease podinfo -n demo-gitops (pause)
2 - fix changes
3 flux resume helmrelease podinfo -n demo-gitops (play)
```

```sh
REMOVING FLUX FROM CLUSTER
flux uninstall --silent
```

```sh

MINIMAL 4 FILES NEEDED FOR FLUX :
- kustomization.yaml
- namespace.yaml
- hemlrelease.yaml
- helmrepo.yaml
```

```sh
GIT : environmental vs. app centric structure approach

1 Environmental : prod, non-prod, test, ... git file/project separation
2 more apps seperated with apps they individual team manages
```

```sh
gitops rollback 
- ONLY1! dont use helm rollback (will be overwritten)
```

```sh
flux events -A
- everything in flux stored as an event 
```

```sh
DETAILED TROUBLESHOOTING OF COMPONENTS

flux logs -n flux-system deploy/source-controller | tail -200
```

```sh
kubectl -n demo-gitops rollout status deploy/podinfo
kubectl -n demo-gitops get pods -w
```









