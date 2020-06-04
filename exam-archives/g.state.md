### Create a Persistent Volume called log-volume. It should make use of a storage class name manual. It should use RWX as the access mode and have a size of 1Gi. The volume should use the hostPath /opt/volume/nginx Next, create a PVC called log-claim requesting a minimum of 200Mi of storage. This PVC should bind to log-volume.Mount this in a pod called logger at the location /var/www/nginx. This pod should use the image nginx:alpine.

<details><summary>show</summary>
<p>

create a pv with the given requirements: 

```bash
vim pv.yaml 
```

```YAML
apiVersion: v1
kind: PersistentVolume
metadata:
  name: log-volume
spec:
  storageClassName: manual
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteMany
  hostPath:
    path: "/opt/volume/nginx"
```

```bash
kubectl create -f pv.yaml
```

create a pvc with the given requirements:

```bash
vim pvc.yaml 
```

```YAML
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: log-volume-claim
spec:
  storageClassName: manual
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 200Mi
```

```bash
kubectl create -f pvc.yaml
```

ensure that the pvc is bound to the pv created : 

```bash
kubectl get pvc | grep -i log-volume-claim
```

create a pod using the above pvc as a volume mount with the details mentioned in the question

```bash
vim pod.yaml 
```

```YAML
apiVersion: v1
kind: Pod
metadata:
  name: logger
spec:
  volumes:
    - name: pv-storage
      persistentVolumeClaim:
        claimName: log-volume-claim
  containers:
    - name: task-pv-container
      image: nginx:alpine
      volumeMounts:
        - mountPath: "/var/www/nginx"
          name: pv-storage
```

```bash
kubectl create -f pod.yaml
```

ensure that pod is up and running 

```bash
kubectl get pods
```

</p>
</details>
