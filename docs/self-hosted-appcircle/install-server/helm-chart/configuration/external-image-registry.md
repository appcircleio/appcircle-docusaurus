---
title: External Image Registries
description: Learn how to configure external image registries in Appcircle
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

## Overview

In the Appcircle's orchestrated application ecosystem, users have the flexibility to access container images through various external image registries.

These external repositories serve as integral components, offering users different avenues to retrieve and manage container images based on their preferences and infrastructure requirements.

These services act as intermediaries, facilitating seamless image retrieval, caching frequently accessed images, and providing enhanced security measures for image distribution.

## Quay Configuration

Red Hat Quay provides a robust container registry solution that integrates well with Kubernetes and OpenShift environments. To configure Quay as your proxy registry, follow these steps:

- Enable Proxy Cache feature by following one of these docs: [Project Quay Proxy Cache](https://docs.projectquay.io/config_quay.html#config-fields-proxy-cache), or [Redhat Quay Proxy Cache](https://docs.redhat.com/en/documentation/red_hat_quay/3.13/html/use_red_hat_quay/quay-as-cache-proxy#red-hat-quay-proxy-cache-procedure).

- Create a new organization in Quay (e.g., named `appcircle`).

- Go to the organization settings and configure Proxy Cache section:
  - Set _Remote Registry_ as `europe-west1-docker.pkg.dev/appcircle/docker-registry`.
  - Set _Remote Registry username_ as `_json_key`.
  - Copy the content of your `cred.json` and paste into _Remote Registry password_ field.
  - Save the configuration.

- Configuration page should look like this:

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-5592-quay-proxy-cache.png' />

## Appcircle Registry Configuration

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

- Additionally, you need to configure `appcircle-vault`, `cert-utils-operator` and `kube_rbac_proxy` images separately due to Helm restrictions that prevent automatic inheritance from the global registry settings.

Your configuration should be set as follows:

```yaml
global:
...
  # Container Image Registry host for container images
  imageRegistry: registry.spacetech.com:8083
  # Container Image Repository path between registry host and image name (for Quay it is the organization name)
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
    # Container image repository for the cert-utils-operator
    repository: registry.spacetech.com:8083/appcircle/cert-utils-operator
  kube_rbac_proxy:
    image:
      # Container image repository for the kube-rbac-proxy
      repository: registry.spacetech.com:8083/appcircle/kube-rbac-proxy

...
```

Be careful with the indentation and the structure of the `values.yaml` file.

- Create a secret with credentials for the external registry.

<Tabs>

  <TabItem value="kubernetes" label="Kubernetes" default>

```bash
kubectl create secret docker-registry containerregistry \
  -n appcircle \
  --docker-server='registry.spacetech.com:8083' \
  --docker-username='yourRegistryUsername' \
  --docker-password='superSecretRegistryPassword'
```

  </TabItem>

  <TabItem value="openshift" label="Openshift">

```bash
oc create secret docker-registry containerregistry \
  -n appcircle \
  --docker-server='registry.spacetech.com:8083' \
  --docker-username='yourRegistryUsername' \
  --docker-password='superSecretRegistryPassword'
```

  </TabItem>

</Tabs>

Configuration is completed, you can continue to the installation using the external registry.

:::tip
If Appcircle is already installed, you can test the registry connection using the command below. It will try to pull the all required images from the external registry and result with images already exists message, since the application version is not changed.

```bash
helm upgrade appcircle-server appcircle/appcircle \
  -n appcircle \
  -f values.yaml
```

:::

## Mirroring Images

If a proxy registry with pull-through cache ability is not available in your setup, you can mirror images manually with your preferred method using the following image list.

### Retrieving the Image List

List of the all container images given below, image versions may vary depending on the Helm chart version.

<details>
    <summary>Click to view the image list.</summary>
```
europe-west1-docker.pkg.dev/appcircle/docker-registry/agentcacheservice:latest
europe-west1-docker.pkg.dev/appcircle/docker-registry/appcircle-keycloak:latest
europe-west1-docker.pkg.dev/appcircle/docker-registry/appcircle-vault:latest
europe-west1-docker.pkg.dev/appcircle/docker-registry/appparserserver:latest
europe-west1-docker.pkg.dev/appcircle/docker-registry/buildserver:latest
europe-west1-docker.pkg.dev/appcircle/docker-registry/cert-utils-operator:v1.3.12
europe-west1-docker.pkg.dev/appcircle/docker-registry/dashboardserver:latest
europe-west1-docker.pkg.dev/appcircle/docker-registry/distributionserver:latest
europe-west1-docker.pkg.dev/appcircle/docker-registry/disttesterweb:latest
europe-west1-docker.pkg.dev/appcircle/docker-registry/kafkab:latest
europe-west1-docker.pkg.dev/appcircle/docker-registry/keycloakversioning:latest
europe-west1-docker.pkg.dev/appcircle/docker-registry/kube-rbac-proxy:v0.11.0
europe-west1-docker.pkg.dev/appcircle/docker-registry/licenseserver:latest
europe-west1-docker.pkg.dev/appcircle/docker-registry/minio/miniob:latest
europe-west1-docker.pkg.dev/appcircle/docker-registry/mongodb:latest
europe-west1-docker.pkg.dev/appcircle/docker-registry/notificationserver:latest
europe-west1-docker.pkg.dev/appcircle/docker-registry/otpservice:latest
europe-west1-docker.pkg.dev/appcircle/docker-registry/postgresqlb:latest
europe-west1-docker.pkg.dev/appcircle/docker-registry/privateapigateway:latest
europe-west1-docker.pkg.dev/appcircle/docker-registry/publishserver:latest
europe-west1-docker.pkg.dev/appcircle/docker-registry/redisb:latest
europe-west1-docker.pkg.dev/appcircle/docker-registry/reportserver:latest
europe-west1-docker.pkg.dev/appcircle/docker-registry/resignservice:latest
europe-west1-docker.pkg.dev/appcircle/docker-registry/resourceserver:latest
europe-west1-docker.pkg.dev/appcircle/docker-registry/schedulemanagerservice:latest
europe-west1-docker.pkg.dev/appcircle/docker-registry/signingidentityserver:latest
europe-west1-docker.pkg.dev/appcircle/docker-registry/storeadminservice:latest
europe-west1-docker.pkg.dev/appcircle/docker-registry/storeapiservice:latest
europe-west1-docker.pkg.dev/appcircle/docker-registry/storeprofileservice:latest
europe-west1-docker.pkg.dev/appcircle/docker-registry/storereportservice:latest
europe-west1-docker.pkg.dev/appcircle/docker-registry/storesubmitserver:latest
europe-west1-docker.pkg.dev/appcircle/docker-registry/storeweb:latest
europe-west1-docker.pkg.dev/appcircle/docker-registry/taskserver:latest
europe-west1-docker.pkg.dev/appcircle/docker-registry/testeradminservice:latest
europe-west1-docker.pkg.dev/appcircle/docker-registry/testerapiservice:latest
europe-west1-docker.pkg.dev/appcircle/docker-registry/toolbox:1.5.0
europe-west1-docker.pkg.dev/appcircle/docker-registry/uiserver:latest
europe-west1-docker.pkg.dev/appcircle/docker-registry/webhookservice:latest
```
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

Save the file and exit. The Machine Config Operator will apply the changes and reboot the nodes. Wait until the nodes are up and running.

:::info

- You can check the status of the nodes with the following command:

```bash
oc get nodes
```

Nodes should be in the `Ready` state.

- And you can check the status of configuration update with the command below:

```bash
oc get mcp
```

Update is done successfully when the state fields look like this:

```bash
... UPDATED   UPDATING   DEGRADED ...
... True      False      False    ...
```

:::

:::caution
If your registry uses a non-standard port (anything other than 80 for HTTP), you must specify it in the configuration as shown in the example above with port `8083`.
:::
