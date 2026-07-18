```sh
helm show values podinfo/podinfo | head -60
```

```sh
HELM REPOSITORY = chart source
```

```sh
az version
kubectl version --client
flux version
helm version
```

```sh

NO RELEASE = NO ROLLBACK

HELM is not connected to your cluster but to YOUR MACHINE

When you deploy chart with values, it becomes a RELEASE
	my-app (chart)
		my-app-non (release)
		my-app-prod (release)

TEMPLATES should be statis and whatever needed to be changed use values.yaml

- HELM renders templates into k8s manifest
- Templates + values are combined locally
- output is plain K8s YAML
- Helm takes chart templates + values → produces YAML manifests that K8s understands      
  
HELM adds: versioned history, separation of env, standard packaging format

KUBERNETES is declarative, declaring to API what state the cluster should be
(everything is built on control loop)

WITHOUT HELM: many YAML files, manual changes, hard rollbacks

HELM sits between K8s cluster and developer      

HELM is not CI/CD, no replacement for kubectl, not GitOps = building BLOG, not PLATFORM

HELM CHART - template without values, blue print of the app
	- same chart can be reused across environments
HELM RELEASE - deployed instance of the chart exists in a namespace
HELM REPOSITORY - public/privite, storage for charts (the same as GIT)
	- provides chart bineries (.bnz), metadata and indexes 
HELM VALUES - configuration input, override chart defaults
	- abstraction that separate what app is from and how it should run
	  
WORKFLOW STEPS: pick a chart, configure values, install, upgrade, rollback 

```

```sh
helm create demo (creates demo with my-chart)
helm lint ./demo (check the syntax of the chart)
helm install demo ./demo
helm upgrade demo ./demo (upgrade changes of the k8s files, dry)
helm upgrade demo ./demo --dry-run --debug
helm template demo ./demo 
helm list
helm list -A (list all releases across namespaces)
helm status demo
helm get values demo
helm get manifest demo
helm history demo
helm rollback demo
helm uninstall demo ./demo
```

```sh
my-chart
	- chart.yaml
	- values.yaml
	- templates
		- helpers.tpl 
		- deployments.yaml
		- ingress.yaml
		- different kubernetes files.yaml
	-  charts
```

```sh
HELPERS.TPL 
- is used to define reusable template functions/snippets that you can call from other templates in the chart.
  
- to avoid duplicates inside the templates (names,labels,..)

```

```sh
helm install podinfo/podinfo -n demo --set replicaCount=1
helm status podinfo -n tmobile
kubectl -n tmobile port-forward deploy/podinfo 8080:9898
kubectl get all -n tmobile
helm get values podinfo -n tmobile --all | head -n 60
```

```sh
echo "Visit http://127.0.0.1:8080 to use your app" kubectl -n tmobile port-forward deploy/podinfo 8080:9898

watch kubectl get -n tmobile get deploy podinfo
kubectl -n tmobile get svc podinfo -w
helm history podinfo -n tmobile 
helm rollback podinfo 1 -n tmobile 
kubectl rollout status
```

```sh
LABELS and SELECTORS (templating)
labels:
app.kubernetes.io/name: {{include "my-app.name" .}}
app.kubernetes.io/instance: {{ .Release.name }}
```

```sh
VALUES
- are the runtime input to a chart
- templates decribe structur and values describe behaviour
- values can come from :
	  - values.yaml
	  - external values files (-f)
	  - CLI overrides (--set)  
```

```sh
VALUES PRECEDENCE ORDER --> last write wins
- values.yaml (default)
- -f values.yaml
- -f values-dev.yaml (recommended)
- --set key = value (long run avoid)
```

```sh
helm template demo . -s templates/demo-configmap.yaml -f values.prod.yaml
(-s means only this specific template demo-config will be rendered)
```

```sh
MENTAL MODEL
chart = code
value = runtime inout
release = state
```

```sh
ROLLBACK FLOW -->
value change -> upgrade -> failure -> rollback -> recovery
```

```sh

```