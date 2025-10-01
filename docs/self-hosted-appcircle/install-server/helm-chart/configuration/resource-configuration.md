---
title: Resource Configuration
description: Learn how to configure the resources of the Appcircle server using the Helm chart for production environments
tags: [self-hosted, helm, configuration, kubernetes, openshift]
sidebar_position: 120
---

import NeedHelp from '@site/docs/\_need-help.mdx';
import ApplyHelmConfigurationChanges from '@site/docs/self-hosted-appcircle/install-server/helm-chart/configuration/\_apply-helm-configuration-changes.mdx';

It's important that the Appcircle server services have enough resources to actually run in a Kubernetes or OpenShift cluster. Although the Appcircle server might work fine without setting any resource requests and limits using the default values, as a best practice, it's recommended to configure them for **production** workload and fine-tune the resources to fit your cluster resources when you need them.

Setting the `resources.requests` and `resources.limits` for each service will allow Kubernetes or OpenShift to better dispatch the pods across the nodes.

Following the guide here, you will learn how to configure "requests" and "limits" for the Appcircle server services to guarantee minimum resources for them in the **production** environment while preventing overconsumption with maximum thresholds.

:::tip
If you are not familiar with the resource configuration concepts, you can get a quick overview from [here](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-best-practices-resource-requests-and-limits).
:::

## Resource Requests and Limits

The "requests" and "limits" define how much CPU and memory an Appcircle server service is guaranteed and allowed to use.

- The "requests" ensures that the service always gets the minimum resources it needs.
- The "limits" covers the maximum usage to prevent overconsumption.

Below is the table of services with their recommended "requests" and "limits" for **production** environments.

Setting these, as guided below, improves the stability of production workloads while avoiding resource contention and keeping resource costs optimized, especially for shared clusters.

| Service | Requests CPU | Requests Memory | Limits CPU | Limits memory |
| ------- | -------------- | ----------------- | ------------ | --------------- |
| `agentcache` | 20m | 512Mi | 100m | 1000Mi |
| `agentcache-redis` | 10m | 25Mi | 50m | 100Mi |
| `apigateway` | 400m | 800Mi | 1500m | 1200Mi |
| `apigateway-redis` | 10m | 25Mi | 50m | 100Mi |

<!-- @TODO: Table should be complete. -->

:::tip
Using the table above, you can also find out the total resource requirements of the Appcircle server for the **production** environment.

Keep in mind that the "requests" and "limits" here are for one replica. When you have more than one replica, you need to **multiply them by the replica count** to see the whole picture.

For the recommended replica counts, please refer to the details in the [Increase the Replica Counts](/self-hosted-appcircle/install-server/helm-chart/configuration/advanced-configuration#increase-the-replica-counts) section.
:::

In the following section you can find the Helm chart details for the recommended configuration. You should update your `values.yaml` file using the relevant sections below.

<details>
    <summary>Click to view the Helm chart values for the **requests** and **limits**.</summary>

:::caution
Some keys might already exist in your `values.yaml` file that come from other configurations.

Make sure to update existing ones instead of adding new ones for them to avoid duplicate keys.
:::

```yaml
agentcache:
  resources:
    requests:
      cpu: 20m
      memory: 512Mi
    limits:
      cpu: 100m
      memory: 1000Mi
  agentcache-redis:
    master:
      resources:
        requests:
          cpu: 10m
          memory: 25Mi
        limits:
          cpu: 50m
          memory: 100Mi
```

<!-- @TODO: Values.yaml should be complete. -->

</details>

## Applying Configuration Changes

<ApplyHelmConfigurationChanges />

<NeedHelp />