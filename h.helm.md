# Managing Kubernetes with Helm

- Note: Helm is part of the new CKAD syllabus. Here are a few examples of using Helm to manage Kubernetes.

## Helm in K8s

### Creating a basic Helm chart

<details><summary>show</summary>
<p>

```bash
helm create chart-test ## this creates a basic helm chart
```

</p>
</details>

### Add the Bitnami repo at https://charts.bitnami.com/bitnami to Helm
<details><summary>show</summary>
<p>

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
```

Show the list of installed repositories:
```bash
helm repo list
```

</p>
</details>

### Using Helm repo

<details><summary>show</summary>
<p>

Add, list, remove, update and index chart repos

```bash
helm repo add [NAME] [URL] [flags]

helm repo list / helm repo ls

helm repo remove [REPO1] [flags]

helm repo update / helm repo up

helm repo update [REPO1] [flags]

helm repo index [DIR] [flags]
```

</p>
</details>

### Search Repositories for a Chart
<details><summary>show</summary>
<p>

Search all installed repositories for a chart

```bash
helm search repo [keyword]
```

</p>
</details>

### Download a Helm chart from a repository

<details><summary>show</summary>
<p>

```bash
helm pull [chart URL | repo/chartname] [...] [flags] ## this would download a chart, but not install it
helm pull --untar [repo/chartname] # untar the chart after downloading it (does not create a release)
```

</p>
</details>

### Create a Release

<details><summary>show</summary>
<p>

Create a release, creating the resources defined in the chart

```bash
helm install -f myvalues.yaml myredis ./redis # creates a release from a local chart
helm install [releasename] [repo/chartname] # creates a release from a chart in a repo
# Example: helm install my-app bitnami/nginx
```

</p>
</details>

### Find pending Helm deployments on all namespaces

<details><summary>show</summary>
<p>

```bash
helm list --pending -A
```

</p>
</details>

### Uninstall a Helm release

<details><summary>show</summary>
<p>

```bash
helm uninstall -n namespace releasename
```

</p>
</details>

### Upgrading a Helm chart

<details><summary>show</summary>
<p>

```bash
helm upgrade [releasename] [repo/chartname] # Upgrade a chart from a repository
helm upgrade -f myvalues.yaml -f override.yaml redis ./redis # Upgrade a local chart from a file
```

</p>
</details>

### Write the contents of the values.yaml of a chart to standard output
<details><summary>show</summary>
<p>

```bash
helm show values [repo/chartname]
```

</p>
</details>

### Install the `bitnami/node` chart setting the number of replicas to 5
<details><summary>show</summary>
<p>

To achieve this, we need two key pieces of information:
- The name of the attribute in values.yaml which controls replica count
- A simple way to set the value of this attribute during installation

To identify the name of the attribute in the values.yaml file, we could get all the values, as in the previous task, and then grep to find attributes matching the pattern `replica`
```bash
helm show values bitnami/node | grep -i replica
```
which returns
```bash
## @param replicaCount Specify the number of replicas for the application
replicaCount: 1
```

We can use the `--set` argument during installation to override attribute values. Hence, to set the replica count to 5, we need to run
```bash
helm install mynode bitnami/node --set replicaCount=5
```

</p>
</details>


