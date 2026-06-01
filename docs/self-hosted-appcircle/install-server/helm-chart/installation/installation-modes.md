---
title: Installation Modes
description: Learn about the different installation modes available for the Appcircle Helm chart, including Full, DMZ-LAN, and DMZ-DMZ deployments.
tags: [self-hosted, helm, installation, configuration, kubernetes, openshift, dmz]
sidebar_position: 30
---

import NeedHelp from '@site/docs/\_need-help.mdx';

## Overview

Starting from server version **3.30.0**, the Appcircle Helm chart supports three distinct installation modes. These modes allow you to deploy Appcircle components across different network zones, enabling architectures that separate externally-facing (DMZ-DMZ) services from internally-facing (DMZ-LAN) services.

The installation mode is controlled by two global flags:

| Flag                   | Default | Description                                                                                                                   |
| ---------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `global.tags.frontend` | `true`  | Deploys DMZ-DMZ facing components: `store-web`, `distribution-testerweb`, `codepush-proxy`, and optionally `auth-proxy`.     |
| `global.tags.backend`  | `true`  | Deploys DMZ-LAN components: all backend microservices, `web-app`, `web-event`, `apigateway`, and all infrastructure services. |

:::info
The naming of these tags (`frontend`/`backend`) predates the current DMZ terminology and may be counterintuitive. Think of them as "DMZ-DMZ zone" and "DMZ-LAN zone" respectively, not as UI vs API tiers.

Note that `web-app` (the Appcircle Dashboard at `my.<domain>`) is a UI application but it deploys under `global.tags.backend=true` because it resides in the DMZ-LAN zone.
:::

## Mode Summary

| Mode                         | `global.tags.frontend` | `global.tags.backend` | Use Case                                                                   |
| ---------------------------- | :--------------------: | :-------------------: | -------------------------------------------------------------------------- |
| **Full** (default)           | `true`                 | `true`                | Single-cluster deployment with all components in one namespace.            |
| **DMZ-LAN** (backend-only)   | `false`                | `true`                | Secure zone with all backend services. Paired with a DMZ-DMZ install.     |
| **DMZ-DMZ** (frontend-only)  | `true`                 | `false`               | Externally accessible zone with only public-facing services.               |

## Mode 1 — Full Installation (Default)

The default mode deploys all Appcircle components into a single cluster and namespace. This is suitable for trial deployments or environments where network zone separation is not required.

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
The Full installation is the simplest deployment option and is described in the [Kubernetes](/self-hosted-appcircle/install-server/helm-chart/installation/kubernetes) and [OpenShift](/self-hosted-appcircle/install-server/helm-chart/installation/openshift) installation guides.
:::

## Mode 2 — DMZ-LAN Installation (Backend-Only)

The DMZ-LAN mode deploys all backend microservices, infrastructure (MongoDB, Kafka, Vault, MinIO, Redis, Keycloak, PostgreSQL), and the Appcircle Dashboard (`web-app`) into a secured internal zone. No externally-facing web portals are deployed.

### Step 1 — Install the Backend

Create a `values.yaml` with the following configuration:

<details>
    <summary>Click to view the DMZ-LAN <code>values.yaml</code> example (per-module Redis).</summary>

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
    <summary>Click to view the DMZ-LAN <code>values.yaml</code> example (shared Redis).</summary>

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

Install the Appcircle server in backend-only mode:

```bash
helm install appcircle-server appcircle/appcircle \
  --timeout 1200s \
  -n appcircle \
  -f values.yaml
```

### Step 2 — Collect Output Values

After the backend installation, collect the following values from the Helm install output. These are required for the DMZ-DMZ installation:

- **`initialOrganizationId`** — The initial organization ID printed in the Helm output.
- **`distributionTesterWeb` client secret** — The Keycloak client secret for the distribution tester web.
- **`storeWeb` client secret** — The Keycloak client secret for the store web.

You can retrieve the client secrets from the generated Kubernetes secret:

```bash
kubectl get secret -n appcircle appcircle-server-auth-keycloak-clients-secret \
  -o jsonpath='{.data.distributionTesterWeb}' | base64 --decode ; echo

kubectl get secret -n appcircle appcircle-server-auth-keycloak-clients-secret \
  -o jsonpath='{.data.storeWeb}' | base64 --decode ; echo
```

## Mode 3 — DMZ-DMZ Installation (Frontend-Only)

The DMZ-DMZ mode deploys only the externally-accessible web portals: `store-web`, `distribution-testerweb`, and `codepush-proxy`. This cluster must be able to reach the DMZ-LAN cluster's `auth.<domain>` endpoint.

### Step 1 — Pre-create the Auth Client Secret

Before installing, create the Keycloak client secrets secret using the values collected from the DMZ-LAN installation:

```bash
kubectl create secret generic appcircle-server-auth-keycloak-clients-secret \
  -n appcircle \
  --from-literal=distributionTesterWeb='<from-backend-install>' \
  --from-literal=storeWeb='<from-backend-install>'
```

### Step 2 — Install the Frontend

Create a `values.yaml` for the DMZ-DMZ installation:

<details>
    <summary>Click to view the DMZ-DMZ <code>values.yaml</code> example.</summary>

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
    defaultOrganizationId: '<initialOrganizationId-from-backend-install>'

ingress-nginx:
  enabled: true
```

</details>

If the DMZ-DMZ cluster does not have DNS resolution for the backend's `auth.<domain>`, add `hostAliases` so the frontend pods can reach Keycloak:

```yaml
store:
  store-web:
    hostAliases:
      - ip: <backend-ingress-ip>
        hostnames:
          - auth.appcircle.spacetech.com

distribution:
  distribution-testerweb:
    hostAliases:
      - ip: <backend-ingress-ip>
        hostnames:
          - auth.appcircle.spacetech.com
```

Install the Appcircle server in frontend-only mode:

```bash
helm install appcircle-server appcircle/appcircle \
  --timeout 1200s \
  -n appcircle \
  -f values.yaml
```

## Redis Configuration for DMZ Modes

Redis deployment is controlled by a combination of flags. You must choose exactly one Redis model per installation.

### Redis Flags Reference

| Flag                                  | Default | Mode         | Description                                                                   |
| ------------------------------------- | ------- | ------------ | ----------------------------------------------------------------------------- |
| `global.redis.enabled`                | `false` | Full         | Deploys a single shared Redis instance for all backend modules.               |
| `global.redis.everyModule`            | `true`  | Full         | Deploys one Redis instance per backend module (default).                      |
| `global.tags.singleRedisBackend`      | unset   | DMZ-LAN      | Equivalent to `redis.enabled` for backend-only installations.                 |
| `global.tags.redisBackendEveryModule` | unset   | DMZ-LAN      | Equivalent to `redis.everyModule` for backend-only installations.             |

:::caution
The shared Redis model (`redis.enabled=true`) and per-module Redis model (`redis.everyModule=true`) are mutually exclusive. The Helm chart will fail at render time if both are enabled simultaneously.

In DMZ-DMZ mode, all Redis flags must be set to `false` since no Redis instances are deployed in the frontend zone.
:::

## External API Gateway (DMZ-DMZ Only)

In environments where traffic from the DMZ-DMZ cluster to the DMZ-LAN cluster is mediated by a customer-managed API gateway, you can configure the external gateway URL. When enabled, DMZ-DMZ frontend services route their `auth` and `privateApi` calls through the gateway instead of directly to the backend subdomains.

```yaml
global:
  externalApiGateway:
    enabled: true
    url: 'https://apigw.spacetech.com'
```

:::info
This setting only takes effect when `global.tags.frontend=true` and `global.tags.backend=false` (DMZ-DMZ mode). It has no effect in Full or DMZ-LAN installations.
:::

## Auth Proxy (DMZ-DMZ Only)

When the DMZ-DMZ cluster must not have direct access to the authentication service, you can enable the bundled `auth-proxy` (an Nginx reverse proxy). This restricts DMZ-DMZ→auth access through a controlled proxy.

```yaml
global:
  authProxy:
    enabled: true
```

:::caution
The `auth-proxy` must **not** be enabled in Full or DMZ-LAN installations. It is only applicable for DMZ-DMZ deployments.
:::

## Common Validation Errors

| Error Message                                                                    | Cause                                                                                    |
| -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `For backend-only installation, both ... must be defined`                        | `singleRedisBackend` and `redisBackendEveryModule` flags are missing from the values.    |
| `For frontend-only installation, all '...' must be disabled`                     | A Redis, MongoDB, or CodePush PostgreSQL flag is still enabled in a DMZ-DMZ install.     |
| `Secret '<release>-auth-keycloak-clients-secret' not found`                      | The client secrets secret was not pre-created before the DMZ-DMZ installation.           |
| `'store.store-web.defaultOrganizationId' must be set`                            | The `defaultOrganizationId` from the DMZ-LAN install was not provided.                  |
| `At least one Redis configuration must be enabled`                               | Neither `global.redis.everyModule` nor `global.redis.enabled` is set to `true` in Full mode. |

<NeedHelp />
