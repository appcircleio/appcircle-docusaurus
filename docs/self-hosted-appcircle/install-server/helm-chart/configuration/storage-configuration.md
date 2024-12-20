---
title: Storage Configuration
description: Learn how to configure the storage details of Appcircle server Helm chart for production environments
tags: [self-hosted, helm, configuration, kubernetes]
sidebar_position: 30
---

import NeedHelp from '@site/docs/\_need-help.mdx';

### Persistent Volume Configuration

Appcircle server Helm chart supports configuring storage classes and volume sizes for persistent volume claims (PVCs). If you don't specify any storage class or size, the PVCs will be created using the default storage class of your Kubernetes cluster with the default size. If you want to adjust these settings, you can specify them in the `values.yaml`.

:::caution
The configurations for storage classes should be **done before the first deployment** and **cannot be changed later**. To modify these settings, you should **[uninstall Appcircle](/self-hosted-appcircle/install-server/helm-chart/uninstallation)** and redeploy it.
:::

:::tip
You can check your **default storage class** by running the following command and check the output:

```bash
kubectl get storageclass
```

According to the sample output below, there is a `default` storage class.

```output
kubectl get storageclass
NAME                   PROVISIONER             RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
local-path (default)   rancher.io/local-path   Delete          WaitForFirstConsumer   false                  59d
```

If the Kubernetes cluster you are deploying Appcircle server **doesn't have a default** storage class, you can **set** the storage class from `values.yaml`.   

:::

:::caution
Some storage classes do not support **expanding volumes**. You should verify the capabilities of your own storage class. If volume expansion is needed, **manual operations**, such as moving data from the old volume to a new one, may be required.
:::

You can configure the `values.yaml` like in the example below. The storage values given in the example are recommended values for production usage.

```yaml
auth:
  auth-postgresql:
    primary:
      persistence:
        size: 40Gi
        storageClass: nfs-client
mongodb:
  persistence:
    size: 3Gi
    storageClass: nfs-client
kafka:
  controller:
    persistence:
      size: 8Gi
      storageClass: nfs-client
minio:
  persistence:
    storageClass: nfs-client
    size: 1Ti
vault:
  server:
    dataStorage:
      size: 20Gi
      storageClass: nfs-client
webeventredis:
  master:
    persistence:
      size: 2Gi
      storageClass: nfs-client
  replica:
    persistence:
      size: 2Gi
      storageClass: nfs-client
```

<NeedHelp />