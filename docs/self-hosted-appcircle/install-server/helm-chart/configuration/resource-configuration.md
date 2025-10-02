---
title: Resource Configuration
description: Learn how to configure the resources of the Appcircle server using the Helm chart for production environments
tags: [self-hosted, helm, configuration, kubernetes, openshift]
sidebar_position: 120
---

import NeedHelp from '@site/docs/\_need-help.mdx';
import ApplyHelmConfigurationChanges from '@site/docs/self-hosted-appcircle/install-server/helm-chart/configuration/\_apply-helm-configuration-changes.mdx';

It's important that the Appcircle services have enough resources to actually run in a Kubernetes or OpenShift cluster. Although the Appcircle server might work fine without setting any resource "requests" and "limits" using the default values, as a best practice, it's recommended to configure them for **production** workload and fine-tune the resources to fit your cluster resources when you need them.

Setting the `resources.requests` and `resources.limits` for each Appcircle service will allow Kubernetes or OpenShift to better dispatch the pods across the nodes.

Following the guide here, you will learn how to configure "requests" and "limits" for the Appcircle server to guarantee minimum resources for the services in the **production** environment while preventing overconsumption with maximum thresholds.

:::tip
If you are not familiar with the resource configuration concepts, you can get a quick overview from [here](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-best-practices-resource-requests-and-limits).
:::

:::info

This document contains the Appcircle services, which are included in the "**Appcircle Server**" box in the [Kubernetes/OpenShift Architecture Using Helm Chart](/self-hosted-appcircle/install-server/helm-chart/configuration/production-readiness) diagram, and it is based on a **[production readiness](/self-hosted-appcircle/install-server/helm-chart/configuration/production-readiness)** setup.

Therefore, it does not include resource requirements for the **[external services](/self-hosted-appcircle#kubernetesopenshift-architecture-using-helm-chart)** since they are documented in their own sections in detail considering the **production** requirements.

When you install the Appcircle Helm chart with the default configuration and deploy all the required services to the cluster for testing or trial purposes, there will be some other services that are not within the scope of this document. These are recommended to be outside of the "**Appcircle Server**" box.

- `auth-postgresql`
- `minio`
- `mongodb`

One exception for that is the [HashiCorp Vault](/self-hosted-appcircle/install-server/helm-chart/configuration/production-readiness/database-and-vault#hashicorp-vault) service. Since it has a recommended **production** option as [External Data Store](/self-hosted-appcircle/install-server/helm-chart/configuration/production-readiness/database-and-vault#external-data-store-eg-mssql), you have an option to deploy the `vault` service to the cluster within the "**Appcircle Server**" box. You can find its resource requirements for this kind of setup in the following sections.

:::

## Resource Requests and Limits

The "requests" and "limits" define how much CPU and memory an Appcircle service is guaranteed and allowed to use.

- The "requests" ensures that the service always gets the minimum resources it needs.
- The "limits" covers the maximum usage to prevent overconsumption.

Below is the table of Appcircle services with their recommended "requests" and "limits" for **production** environments.

Setting these, as guided below, improves the stability of production workloads while avoiding resource contention and keeping resource costs optimized, especially for shared clusters.

|  | Requests CPU | Requests Memory | Limits CPU | Limits Memory |
| ------- | -------------- | ----------------- | ------------ | --------------- |
| `agentcache` | 20m | 512Mi | 100m | 1000Mi |
| `agentcache-redis` | 10m | 25Mi | 50m | 100Mi |
| `apigateway` | 400m | 800Mi | 1500m | 1200Mi |
| `apigateway-redis` | 10m | 25Mi | 50m | 100Mi |
| `appparser` | 50m | 650Mi | 200m | 1500Mi |
| `auth-keycloak` | 250m | 1280Mi | 600m | 2000Mi |
| `build` | 100m | 850Mi | 300m | 1500Mi |
| `build-redis` | 10m | 25Mi | 50m | 100Mi |
| `distribution-server` | 100m | 720Mi | 250m | 1200Mi |
| `distribution-server-redis` | 10m | 25Mi | 50m | 100Mi |
| `distribution-testeradmin` | 50m | 410Mi | 200m | 600Mi |
| `distribution-testerapi` | 50m | 750Mi | 200m | 1300Mi |
| `distribution-testerapi-redis` | 10m | 25Mi | 50m | 100Mi |
| `distribution-testerweb` | 50m | 300Mi | 200m | 400Mi |
| `distribution-testerweb-redis` | 10m | 25Mi | 50m | 100Mi |
| `kafka` | 300m | 2000Mi | 1500m | 3000Mi |
| `license` | 50m | 260Mi | 200m | 320Mi |
| `license-redis` | 10m | 25Mi | 50m | 100Mi |
| `notification` | 50m | 300Mi | 200m | 450Mi |
| `otp` | 50m | 75Mi | 200m | 120Mi |
| `otp-redis` | 10m | 25Mi | 50m | 100Mi |
| `publish` | 50m | 380Mi | 200m | 720Mi |
| `publish-redis` | 10m | 25Mi | 50m | 100Mi |
| `reporting` | 50m | 320Mi | 200m | 400Mi |
| `resign` | 50m | 150Mi | 200m | 220Mi |
| `resource` | 50m | 1000Mi | 200m | 1500Mi |
| `resource-redis` | 10m | 25Mi |  50m | 100Mi |
| `schedulemanager` | 50m | 270Mi | 200m | 350Mi |
| `schedulemanager-redis` | 10m | 25Mi | 50m | 100Mi |
| `signingidentity` | 50m | 460Mi | 200m | 600Mi |
| `signingidentity-redis` | 10m | 25Mi | 50m | 100Mi |
| `store-admin` | 50m | 240Mi | 200m | 350Mi |
| `store-api` | 50m | 330Mi | 200m | 420Mi |
| `store-api-redis` | 10m | 25Mi | 50m | 100Mi |
| `store-profile` | 50m | 380Mi | 200m | 450Mi |
| `store-report` | 50m | 300Mi | 200m | 400Mi |
| `store-web` | 50m | 340Mi | 200m | 450Mi |
| `store-web-redis` | 10m | 25Mi | 50m | 100Mi |
| `storesubmit` | 50m | 265Mi | 200m | 350Mi |
| `storesubmit-redis` | 10m | 25Mi | 50m | 100Mi |
| `taskserver` | 50m | 135Mi | 200m | 200Mi |
| `taskserver-redis` | 10m | 25Mi | 50m | 100Mi |
| `vault` | 40m | 200Mi | 200m | 650Mi |
| `web-app` | 8m | 80Mi | 60m | 150Mi |
| `web-event` | 50m | 110Mi | 200m | 300Mi |
| `web-redis` | 10m | 25Mi | 50m | 100Mi |
| `webeventredis-master` | 100m | 1000Mi | 500m | 2000Mi |
| `webeventredis-replica` | 100m | 1000Mi | 500m | 2000Mi |
| `webhook` | 50m | 210Mi | 200m | 350Mi |

<!-- @TODO: Add exception fro vault -->

<!-- @TODO: mention services that do not have replicas -->

:::tip
Using the table above, you can also find out the total resource requirements of the Appcircle server for the **production** environment.

Keep in mind that the "requests" and "limits" here are for **one replica**. When you have more than one replica, you need to **multiply them by the replica count** to see the whole picture.

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

apigateway:
  resources:
    requests:
      cpu: 400m
      memory: 800Mi
    limits:
      cpu: 1500m
      memory: 1200Mi
  apigateway-redis:
    master:
      resources:
        requests:
          cpu: 10m
          memory: 25Mi
        limits:
          cpu: 50m
          memory: 100Mi

appparser:
  resources:
    requests:
      cpu: 50m
      memory: 650Mi
    limits:
      cpu: 200m
      memory: 1500Mi

auth:
  auth-keycloak:
    resources:
      requests:
        cpu: 250m
        memory: 1280Mi
      limits:
        cpu: 600m
        memory: 2000Mi

build:
  resources:
    requests:
      cpu: 100m
      memory: 850Mi
    limits:
      cpu: 300m
      memory: 1500Mi
  build-redis:
    master:
      resources:
        requests:
          cpu: 10m
          memory: 25Mi
        limits:
          cpu: 50m
          memory: 100Mi

distribution:
  distribution-server:
    resources:
      requests:
        cpu: 100m
        memory: 720Mi
      limits:
        cpu: 250m
        memory: 1200Mi
  distribution-server-redis:
    master:
      resources:
        requests:
          cpu: 10m
          memory: 25Mi
        limits:
          cpu: 50m
          memory: 100Mi
  distribution-testeradmin:
    resources:
      requests:
        cpu: 50m
        memory: 410Mi
      limits:
        cpu: 200m
        memory: 600Mi
  distribution-testerapi:
    resources:
      requests:
        cpu: 50m
        memory: 750Mi
      limits:
        cpu: 200m
        memory: 1300Mi
  distribution-testerapi-redis:
    master:
      resources:
        requests:
          cpu: 10m
          memory: 25Mi
        limits:
          cpu: 50m
          memory: 100Mi
  distribution-testerweb:
    resources:
      requests:
        cpu: 50m
        memory: 300Mi
      limits:
        cpu: 200m
        memory: 400Mi
  distribution-testerweb-redis:
    master:
      resources:
        requests:
          cpu: 10m
          memory: 25Mi
        limits:
          cpu: 50m
          memory: 100Mi

kafka:
  controller:
    resources:
      requests:
        cpu: 300m
        memory: 2000Mi
      limits:
        cpu: 1500m
        memory: 3000Mi

license:
  resources:
    requests:
      cpu: 50m
      memory: 260Mi
    limits:
      cpu: 200m
      memory: 320Mi
  license-redis:
    master:
      resources:
        requests:
          cpu: 10m
          memory: 25Mi
        limits:
          cpu: 50m
          memory: 100Mi

notification:
  resources:
    requests:
      cpu: 50m
      memory: 300Mi
    limits:
      cpu: 200m
      memory: 450Mi

otp:
  resources:
    requests:
      cpu: 50m
      memory: 75Mi
    limits:
      cpu: 200m
      memory: 120Mi
  otp-redis:
    master:
      resources:
        requests:
          cpu: 10m
          memory: 25Mi
        limits:
          cpu: 50m
          memory: 100Mi

publish:
  resources:
    requests:
      cpu: 50m
      memory: 380Mi
    limits:
      cpu: 200m
      memory: 720Mi
  publish-redis:
    master:
      resources:
        requests:
          cpu: 10m
          memory: 25Mi
        limits:
          cpu: 50m
          memory: 100Mi

reporting:
 resources:
   requests:
     cpu: 50m
     memory: 320Mi
   limits:
     cpu: 200m
     memory: 400Mi

resign:
  resources:
    requests:
      cpu: 50m
      memory: 150Mi
    limits:
      cpu: 200m
      memory: 220Mi

resource:
  resources:
    requests:
      cpu: 50m
      memory: 1000Mi
    limits:
      cpu: 200m
      memory: 1500Mi
  resource-redis:
    master:
      resources:
        requests:
          cpu: 10m
          memory: 25Mi
        limits:
          cpu: 50m
          memory: 100Mi

schedulemanager:
  resources:
    requests:
      cpu: 50m
      memory: 270Mi
    limits:
      cpu: 200m
      memory: 350Mi
  schedulemanager-redis:
    master:
      resources:
        requests:
          cpu: 10m
          memory: 25Mi
        limits:
          cpu: 50m
          memory: 100Mi

signingidentity:
  resources:
    requests:
      cpu: 50m
      memory: 460Mi
    limits:
      cpu: 200m
      memory: 600Mi
  signingidentity-redis:
    master:
      resources:
        requests:
          cpu: 10m
          memory: 25Mi
        limits:
          cpu: 50m
          memory: 100Mi

store:
  store-web:
    resources:
      requests:
        cpu: 50m
        memory: 340Mi
      limits:
        cpu: 200m
        memory: 450Mi
  store-web-redis:
    master:
      resources:
        requests:
          cpu: 10m
          memory: 25Mi
        limits:
          cpu: 50m
          memory: 100Mi
  store-admin:
    resources:
      requests:
        cpu: 50m
        memory: 240Mi
      limits:
        cpu: 200m
        memory: 350Mi
  store-api:
    resources:
      requests:
        cpu: 50m
        memory: 330Mi
      limits:
        cpu: 200m
        memory: 420Mi
  store-api-redis:
    master:
      resources:
        requests:
          cpu: 10m
          memory: 25Mi
        limits:
          cpu: 50m
          memory: 100Mi
  store-profile:
    resources:
      requests:
        cpu: 50m
        memory: 380Mi
      limits:
        cpu: 200m
        memory: 450Mi
  store-report:
    resources:
      requests:
        cpu: 50m
        memory: 300Mi
      limits:
        cpu: 200m
        memory: 400Mi

storesubmit:
  resources:
    requests:
      cpu: 50m
      memory: 265Mi
    limits:
      cpu: 200m
      memory: 350Mi
  storesubmit-redis:
    master:
      resources:
        requests:
          cpu: 10m
          memory: 25Mi
        limits:
          cpu: 50m
          memory: 100Mi

taskserver:
  resources:
    requests:
      cpu: 50m
      memory: 135Mi
    limits:
      cpu: 200m
      memory: 200Mi
  taskserver-redis:
    master:
      resources:
        requests:
          cpu: 10m
          memory: 25Mi
        limits:
          cpu: 50m
          memory: 100Mi

vault:
  server:
    resources:
      requests:
        cpu: 40m
        memory: 200Mi
      limits:
        cpu: 200m
        memory: 650Mi

web:
  web-app:
    resources:
      requests:
        cpu: 8m
        memory: 80Mi
      limits:
        cpu: 60m
        memory: 150Mi
  web-event:
    resources:
      requests:
        cpu: 50m
        memory: 110Mi
      limits:
        cpu: 200m
        memory: 300Mi
  web-redis:
    master:
      resources:
        requests:
          cpu: 10m
          memory: 25Mi
        limits:
          cpu: 50m
          memory: 100Mi

webeventredis:
  master:
    resources:
      requests:
        cpu: 100m
        memory: 1000Mi
      limits:
        cpu: 500m
        memory: 2000Mi
  replica:
    resources:
      requests:
        cpu: 100m
        memory: 1000Mi
      limits:
        cpu: 500m
        memory: 2000Mi

webhook:
  resources:
    requests:
      cpu: 50m
      memory: 210Mi
    limits:
      cpu: 200m
      memory: 350Mi
```

<!-- @TODO: Values.yaml should be complete. -->

</details>

## Applying Configuration Changes

<ApplyHelmConfigurationChanges />

<NeedHelp />