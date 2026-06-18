---
title: Installation Modes
description: Learn about the different installation modes for the Appcircle Helm chart — Full, Internal Zone, and External Zone — and how to configure split-cluster deployments.
tags: [self-hosted, helm, installation, configuration, kubernetes, openshift]
sidebar_position: 30
---

import NeedHelp from '@site/docs/\_need-help.mdx';

## Overview

Starting from server version **3.30.0**, the Appcircle Helm chart supports three deployment modes. These modes let you place Appcircle components across separate network zones — an **Internal Zone** for backend services and infrastructure, and an **External Zone** for publicly accessible web portals.

The active mode is controlled by two global Helm flags:

| Flag                   | Default | Zone          | Components deployed                                                                                                                                    |
| ---------------------- | ------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `global.tags.backend`  | `true`  | Internal Zone | All backend microservices, `web-app`, `web-event`, `apigateway`, and infrastructure (MongoDB, Kafka, Vault, MinIO, Redis, Keycloak, PostgreSQL)         |
| `global.tags.frontend` | `true`  | External Zone | Publicly accessible portals: `store-web`, `distribution-testerweb`, `codepush-proxy`, and optionally `auth-proxy`                                      |

:::info
The flag names `global.tags.frontend` and `global.tags.backend` reflect the original component grouping and do not indicate a UI vs. API tier split. Notably, `web-app` (the Appcircle Dashboard at `my.<domain>`) is a web application but deploys under `global.tags.backend=true` because it resides in the Internal Zone.
:::

## Mode Summary

| Mode                   | `global.tags.backend` | `global.tags.frontend` | Use Case                                                                   |
| ---------------------- | :-------------------: | :--------------------: | -------------------------------------------------------------------------- |
| **Full** (default)     | `true`                | `true`                 | All components in a single cluster and namespace.                          |
| **Internal Zone**      | `true`                | `false`                | Internal services only. Paired with a separate External Zone installation. |
| **External Zone**      | `false`               | `true`                 | Public-facing portals only. Requires an existing Internal Zone install.    |

## Mode 1 — Full Installation (Default)

The Full mode deploys all Appcircle components into a single cluster and namespace. This is the recommended starting point for trial deployments or environments where network zone separation is not required.

```yaml
global:
  tags:
    frontend: true
    backend: true
  rbac:
    create: true
  redis:
    everyModule: true   # Per-module Redis (default)
    enabled: false
```

:::tip
The Full installation is described in detail in the [Kubernetes](/self-hosted-appcircle/install-server/helm-chart/installation/kubernetes) and [OpenShift](/self-hosted-appcircle/install-server/helm-chart/installation/openshift) guides.
:::

## Mode 2 — Internal Zone Installation

The Internal Zone mode deploys all backend microservices, infrastructure (MongoDB, Kafka, Vault, MinIO, Redis, Keycloak, PostgreSQL), the Appcircle Dashboard (`web-app`), and `web-event` into your secured internal network. No external-facing web portals are deployed in this cluster.

This mode is typically paired with a separate External Zone installation that handles public traffic.

### Step 1 — Install Internal Zone Components

Create a `values.yaml` with the following configuration:

<details>
    <summary>Click to view the Internal Zone <code>values.yaml</code> example (per-module Redis).</summary>

```yaml
global:
  urls:
    domainName: .appcircle.spacetech.com

  tags:
    frontend: false
    backend: true
    singleRedisBackend: false
    redisBackendEveryModule: true

  rbac:
    create: true

  redis:
    enabled: false
    everyModule: true

auth:
  auth-keycloak:
    initialUsername: "admin@spacetech.com"
    initialPassword: "superSecretAppcirclePassword1234"

ingress-nginx:
  enabled: false
```

</details>

<details>
    <summary>Click to view the Internal Zone <code>values.yaml</code> example (shared Redis).</summary>

```yaml
global:
  urls:
    domainName: .appcircle.spacetech.com

  tags:
    frontend: false
    backend: true
    singleRedisBackend: true
    redisBackendEveryModule: false

  rbac:
    create: true

  redis:
    enabled: true
    everyModule: false

auth:
  auth-keycloak:
    initialUsername: "admin@spacetech.com"
    initialPassword: "superSecretAppcirclePassword1234"

ingress-nginx:
  enabled: false
```

</details>

Install the Appcircle server in Internal Zone mode:

```bash
helm install appcircle-server appcircle/appcircle \
  --timeout 1200s \
  -n appcircle \
  -f values.yaml
```

### Step 2 — Collect Output Values

After the Internal Zone installation completes, collect the following values from the Helm output. These are required for the External Zone installation:

- **`initialOrganizationId`** — The initial organization ID printed in the Helm output.
- **`distributionTesterWeb` client secret** — The Keycloak client secret for the distribution tester web portal.
- **`storeWeb` client secret** — The Keycloak client secret for the store web portal.

Retrieve the client secrets from the generated Kubernetes secret:

```bash
kubectl get secret -n appcircle appcircle-server-auth-keycloak-clients-secret \
  -o jsonpath='{.data.distributionTesterWeb}' | base64 --decode ; echo

kubectl get secret -n appcircle appcircle-server-auth-keycloak-clients-secret \
  -o jsonpath='{.data.storeWeb}' | base64 --decode ; echo
```

## Mode 3 — External Zone Installation

The External Zone mode deploys only the publicly accessible web portals: `store-web`, `distribution-testerweb`, and `codepush-proxy`. The External Zone cluster must be able to reach the Internal Zone cluster's `auth.<domain>` endpoint.

### Step 1 — Pre-create the Auth Client Secret

Before installing, create the Keycloak client secrets secret using the values collected from the Internal Zone installation:

```bash
kubectl create secret generic appcircle-server-auth-keycloak-clients-secret \
  -n appcircle \
  --from-literal=distributionTesterWeb='<from-internal-zone-install>' \
  --from-literal=storeWeb='<from-internal-zone-install>'
```

### Step 2 — Install External Zone Components

Create a `values.yaml` for the External Zone installation:

<details>
    <summary>Click to view the External Zone <code>values.yaml</code> example.</summary>

```yaml
global:
  urls:
    domainName: .appcircle.spacetech.com

  tags:
    frontend: true
    backend: false
    singleRedisBackend: false
    redisBackendEveryModule: false

  rbac:
    create: true

  redis:
    enabled: false
    everyModule: false

mongodb:
  enabled: false

codepush:
  codepush-redis:
    enabled: false
  codepush-postgresql:
    enabled: false

store:
  store-web:
    defaultOrganizationId: '<initialOrganizationId-from-internal-zone-install>'

ingress-nginx:
  enabled: true
```

</details>

If the External Zone cluster does not have DNS resolution for the Internal Zone's `auth.<domain>`, add `hostAliases` so the External Zone pods can reach Keycloak. The `<internal-zone-ingress-ip>` is the IP address of the Internal Zone cluster's Ingress controller (retrieve it with `kubectl get svc -n appcircle`):

```yaml
store:
  store-web:
    hostAliases:
      - ip: <internal-zone-ingress-ip>
        hostnames:
          - auth.appcircle.spacetech.com

distribution:
  distribution-testerweb:
    hostAliases:
      - ip: <internal-zone-ingress-ip>
        hostnames:
          - auth.appcircle.spacetech.com
```

Install the Appcircle server in External Zone mode:

```bash
helm install appcircle-server appcircle/appcircle \
  --timeout 1200s \
  -n appcircle \
  -f values.yaml
```

## Redis Configuration for Split Deployments

In Internal Zone and External Zone modes, Redis deployment is controlled by a combination of flags. You must choose exactly one Redis model per installation.

### Redis Flags Reference

| Flag                                  | Default | Mode          | Description                                                                    |
| ------------------------------------- | ------- | ------------- | ------------------------------------------------------------------------------ |
| `global.redis.enabled`                | `false` | Full          | Deploys a single shared Redis instance for all backend modules.                |
| `global.redis.everyModule`            | `true`  | Full          | Deploys one Redis instance per backend module (default).                       |
| `global.tags.singleRedisBackend`      | unset   | Internal Zone | Equivalent to `redis.enabled` for Internal Zone installations.                 |
| `global.tags.redisBackendEveryModule` | unset   | Internal Zone | Equivalent to `redis.everyModule` for Internal Zone installations.             |

:::caution
The shared Redis model (`redis.enabled=true`) and per-module Redis model (`redis.everyModule=true`) are mutually exclusive. The Helm chart will fail at render time if both are enabled simultaneously.

In External Zone mode, all Redis flags must be set to `false` since no Redis instances are deployed in the External Zone.
:::

## External API Gateway (External Zone Only)

In environments where traffic from the External Zone cluster to the Internal Zone cluster passes through a customer-managed API gateway, configure the gateway URL here. When enabled, External Zone services route their `auth` and `privateApi` calls through the gateway instead of directly to the Internal Zone subdomains.

```yaml
global:
  externalApiGateway:
    enabled: true
    url: 'https://apigw.spacetech.com'
```

:::info
This setting only takes effect in External Zone mode (`global.tags.frontend=true` and `global.tags.backend=false`). It has no effect in Full or Internal Zone installations.
:::

## Auth Proxy (External Zone Only)

When External Zone services must not have direct access to the authentication service, enable the bundled `auth-proxy` (an Nginx reverse proxy). This restricts External Zone → auth traffic through a controlled proxy.

```yaml
global:
  authProxy:
    enabled: true
```

:::caution
The `auth-proxy` must **not** be enabled in Full or Internal Zone installations. It is only applicable for External Zone deployments.
:::

## Common Validation Errors

The following errors are produced by the Helm chart's built-in validation (`check.yaml`) when the `values.yaml` configuration is inconsistent. The error messages reference the Helm flag names directly.

| Error Message                                                                    | Cause                                                                                                             |
| -------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `For backend-only installation, both ... must be defined`                        | `singleRedisBackend` and `redisBackendEveryModule` flags are missing from the Internal Zone `values.yaml`.        |
| `For frontend-only installation, all '...' must be disabled`                     | A Redis, MongoDB, or CodePush PostgreSQL flag is still enabled in an External Zone install.                       |
| `Secret '<release>-auth-keycloak-clients-secret' not found`                      | The client secrets secret was not pre-created before the External Zone installation.                              |
| `'store.store-web.defaultOrganizationId' must be set`                            | The `defaultOrganizationId` from the Internal Zone install was not provided to the External Zone `values.yaml`.   |
| `At least one Redis configuration must be enabled`                               | Neither `global.redis.everyModule` nor `global.redis.enabled` is set to `true` in Full mode.                     |

<NeedHelp />
