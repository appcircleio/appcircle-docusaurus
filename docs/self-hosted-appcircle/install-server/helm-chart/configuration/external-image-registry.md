---
title: External Image Registries
description: Learn how to configure external image registries for Appcircle server when installing using a Helm chart
tags:
  [
    self-hosted,
    external image registry,
    registry,
    quay,
    mirror images,
    insecure registry,
  ]
sidebar_position: 100
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import NeedHelp from '@site/docs/\_need-help.mdx';

# Overview

In Appcircle's orchestrated application ecosystem, users have the flexibility to access container images through various external image registries.

These external repositories serve as integral components, offering users different avenues to retrieve and manage container images based on their preferences and infrastructure requirements.

These services act as intermediaries, facilitating seamless image retrieval, caching frequently accessed images, and providing enhanced security measures for image distribution.

## Quay Configuration

Red Hat Quay provides a robust container registry solution that integrates well with Kubernetes and OpenShift environments. To configure Quay as your proxy registry, follow these steps:

- Enable the proxy cache feature by following one of these docs: [Project Quay Proxy Cache](https://docs.projectquay.io/config_quay.html#config-fields-proxy-cache), or [Red Hat Quay Proxy Cache](https://docs.redhat.com/en/documentation/red_hat_quay/3.13/html/use_red_hat_quay/quay-as-cache-proxy#red-hat-quay-proxy-cache-procedure).

- Create a new organization in Quay (e.g., named `appcircle`).

- Go to the organization settings and configure **Proxy Cache** section:
  - Set **Remote Registry** as `europe-west1-docker.pkg.dev/appcircle/docker-registry`.
  - Set **Remote Registry Username** as `_json_key`.
  - Copy the content of your `cred.json` and paste into **Remote Registry Password** field.
  - Save the configuration.

In the end, the configuration page should look like this:

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-5592-quay-proxy-cache.png' />

## Appcircle Configuration

For the Appcircle server to work with your own container image registry, you should add additional settings to the `values.yaml` file of your deployment.

:::info
In this documentation, we will use `registry.spacetech.com` as an **example registry domain**, `spacetech` as an **example organization name** and `appcircle` as an **example namespace name**.

To see name and namespace of your existing Helm deployment, you can use the command below.

```bash
helm list --all-namespaces
```

:::

:::caution
If your registry uses a non-standard port (anything other than 443 for HTTPS or 80 for HTTP), you must specify it in the configuration as shown in the examples below with port `8083`.
:::

- Add or find the `imageRegistry` and `imageRepositoryPath` keys under `global` mapping in your `values.yaml` file.

- Additionally, you need to configure `vault`, `cert-utils-operator`, and `kube_rbac_proxy` images separately due to Helm restrictions that prevent automatic inheritance from the global registry settings.

Your configuration should be set as follows:

```yaml
global:
...
  # Container image registry host for container images
  imageRegistry: registry.spacetech.com:8083
  # Container image repository path between registry host and image name (for Quay it is the organization name)
  imageRepositoryPath: appcircle

...

# Appcircle vault configuration
vault:
  server:
    image:
      # Appcircle vault image repository path
      repository: registry.spacetech.com:8083/appcircle/appcircle-vault

cert-utils-operator:
  image:
    # Container image repository path for the cert-utils-operator
    repository: registry.spacetech.com:8083/appcircle/cert-utils-operator
  kube_rbac_proxy:
    image:
      # Container image repository path for the kube-rbac-proxy
      repository: registry.spacetech.com:8083/appcircle/kube-rbac-proxy

...
```

Be careful with the indentation and the structure of the `values.yaml` file.

- Create a secret with credentials for the external container image registry.

<Tabs groupId="kubernetes-selection">

  <TabItem value="kubernetes" label="Kubernetes" default>

```bash
kubectl create secret docker-registry containerregistry \
  -n appcircle \
  --docker-server='registry.spacetech.com:8083' \
  --docker-username='yourRegistryUsername' \
  --docker-password='superSecretRegistryPassword' \
  --dry-run=client -o yaml | kubectl apply -f -
```

  </TabItem>

  <TabItem value="openshift" label="Openshift">

```bash
oc create secret docker-registry containerregistry \
  -n appcircle \
  --docker-server='registry.spacetech.com:8083' \
  --docker-username='yourRegistryUsername' \
  --docker-password='superSecretRegistryPassword' \
  --dry-run=client -o yaml | oc apply -f -
```

  </TabItem>

</Tabs>

Configuration is completed; now you can continue to the installation using the external container image registry.

:::tip
If the Appcircle server is already installed, you can test the container image registry connection using the command below.

```bash
helm upgrade appcircle-server appcircle/appcircle \
  -n appcircle \
  -f values.yaml
```

It will try to pull all the required images from the external registry and result in an images already exist message, since the application version is not changed.

:::

## Mirroring Images

If a proxy registry with pull-through cache ability is not available in your setup, you can mirror images manually with your preferred method using the following image list.

### Retrieving the Image List

A list of all container images is given below; image versions may vary depending on the Helm chart version.

<details>
    <summary>Click to view the image list.</summary>

:::tip

The below container image list is based on the **`latest`** Helm chart version. See others in the [version history](https://docs.appcircle.io/self-hosted-appcircle/install-server/helm-chart/upgrades#version-history) page.

:::

    <Tabs groupId="kubernetes-selection">

  <TabItem value="kubernetes" label="Kubernetes" default>

```txt
europe-west1-docker.pkg.dev/appcircle/docker-registry/agentcacheservice:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/appcircle-keycloak:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/appcircle-vault:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/appparserserver:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/buildserver:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/dashboardserver:1.8.92-beta1196
europe-west1-docker.pkg.dev/appcircle/docker-registry/distributionserver:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/disttesterweb:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/kafkab:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/keycloakversioning:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/licenseserver:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/minio/miniob:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/mongodb:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/notificationserver:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/otpservice:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/postgresqlb:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/privateapigateway:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/publishserver:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/redisb:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/reportserver:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/resignservice:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/resourceserver:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/schedulemanagerservice:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/signingidentityserver:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/storeadminservice:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/storeapiservice:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/storeprofileservice:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/storereportservice:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/storesubmitserver:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/storeweb:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/taskserver:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/testeradminservice:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/testerapiservice:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/toolbox:1.5.1
europe-west1-docker.pkg.dev/appcircle/docker-registry/uiserver:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/webhookservice:v3.27.3
```

  </TabItem>

  <TabItem value="openshift" label="Openshift">

```txt
europe-west1-docker.pkg.dev/appcircle/docker-registry/agentcacheservice:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/appcircle-keycloak:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/appcircle-vault:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/appparserserver:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/buildserver:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/cert-utils-operator:v1.3.12
europe-west1-docker.pkg.dev/appcircle/docker-registry/dashboardserver:1.8.92-beta1196
europe-west1-docker.pkg.dev/appcircle/docker-registry/distributionserver:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/disttesterweb:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/kafkab:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/keycloakversioning:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/kube-rbac-proxy:v0.11.0
europe-west1-docker.pkg.dev/appcircle/docker-registry/licenseserver:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/minio/miniob:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/mongodb:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/notificationserver:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/otpservice:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/postgresqlb:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/privateapigateway:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/publishserver:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/redisb:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/reportserver:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/resignservice:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/resourceserver:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/schedulemanagerservice:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/signingidentityserver:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/storeadminservice:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/storeapiservice:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/storeprofileservice:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/storereportservice:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/storesubmitserver:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/storeweb:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/taskserver:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/testeradminservice:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/testerapiservice:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/toolbox:1.5.1
europe-west1-docker.pkg.dev/appcircle/docker-registry/uiserver:v3.27.3
europe-west1-docker.pkg.dev/appcircle/docker-registry/webhookservice:v3.27.3
```

  </TabItem>
  </Tabs>
</details>

:::tip
You can also use the following command to get up-to-date image list required during `helm install`:

```bash
helm template appcircle appcircle/appcircle -f values.yaml | grep image: | sed 's/\s*image:\s*//; s/"//g' | sort -u
```

:::

## Insecure Registry

By default, Kubernetes and OpenShift require HTTPS connections to image registries. To use a registry over HTTP, you must configure it as an insecure registry.

### Kubernetes

Setting up a private container registry for Kubernetes clusters requires different approaches depending on the container runtime and Kubernetes distribution. While Docker was previously the default runtime, Kubernetes has transitioned to `containerd` and other CRI-compliant runtimes, which require different configurations.

#### Challenges with Kubernetes Distributions

Different Kubernetes distributions use various container runtimes, each requiring unique configurations:

- **General Kubernetes with Docker runtimes**: Might require configuring the Docker daemon, but some managed distributions restrict access to this file.
- **General Kubernetes nodes with `containerd` runtimes**: Might require modifying `/etc/containerd/config.toml`, but some managed distributions restrict access to this file.
- **Managed Kubernetes (GKE, EKS, AKS, Rancher, K3s, etc.)**: Configuration methods depend on the specific provider or service. For instance, managed Kubernetes services may restrict node-level configurations and instead use IAM-based authentication with cloud artifact registries. For self-managed services like Rancher or K3s, the configuration will vary, so it's important to consult the official documentation for each.

Because of these variations, it's important to consult the specific Kubernetes distribution’s documentation when configuring **insecure** private registries.

:::tip

##### Use HTTPS-based registries

Instead of configuring insecure HTTP registries, we strongly recommend using **HTTPS-based** artifact registries.

Using an HTTPS registry eliminates the need for complex `containerd`, `docker` or K8s related configurations and improves security.
:::

#### Sample K3s Configuration

For K3s clusters, the registry must be configured on each node using the `registries.yaml` file. The more detailed steps are located in the [official documentation](https://docs.k3s.io/installation/private-registry#without-tls).

1. Create the `registries.yaml` file on all nodes:

```sh
sudo vi /etc/rancher/k3s/registries.yaml
```

2. Add the private registry configuration:

```yaml
mirrors:
  registry.spacetech.com:8083:
    endpoint:
      - "http://registry.spacetech.com:8083"
configs:
  "registry.spacetech.com:8083":
    auth:
      username: "yourRegistryUsername"
      password: "superSecretRegistryPassword"
```

3. Restart K3s to apply changes per its type:

- For control-plane nodes;

```sh
sudo systemctl restart k3s
```

- For worker nodes;

```sh
sudo systemctl restart k3s-agent
```

After configuring the registry on all nodes, Kubernetes will be able to pull images without requiring a separate Kubernetes secret.

For instructions on changing the image repository in your Helm `values.yaml`, refer to the [Appcircle configuration](#appcircle-configuration) section. Keep in mind that you can skip creating a secret with credentials step since it's already been done above for each node.

### OpenShift

Edit the cluster's image configuration:

```bash
oc edit image.config cluster
```

Add your registry address to the `insecureRegistries` section:

```yaml
...
spec:
...
  registrySources:
    insecureRegistries:
    - registry.spacetech.com:8083
```

Save the file and exit.

:::caution
If your registry uses a non-standard port (anything other than 80 for HTTP), you must specify it in the configuration as shown in the example above with port `8083`.
:::

The Machine Config operator will apply the changes and reboot the nodes. Wait until the nodes are up and running.

:::info

- You can check the status of the nodes with the following command:

```bash
oc get nodes
```

Nodes should be in the `Ready` state.

- You can check the status of the configuration update with the command below:

```bash
oc get mcp
```

When the update is done successfully, the state fields look like this:

```bash
... UPDATED   UPDATING   DEGRADED ...
... True      False      False    ...
```

:::

<NeedHelp />
