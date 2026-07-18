# -c here means "container name", e.g.:
kubectl logs slupws-68b6986dd-k5gbf -c <container-name>

# watch the state of the pod:
kubectl get pods slupws-68b6986dd-k5gbf -w

# run a command inside the pod:
kubectl exec slupws-68b6986dd-k5gbf -c <container-name> -- date
kubectl exec slupws-68b6986dd-k5gbf -- date

# find the pod, exec inside and kill a process
kubectl exec $(kubectl get pod --namespace slupws-test --no-headers --output name) --namespace slupws-test -- bash -c "ps -C slup2soap -o pid --noheader | xargs kill"
