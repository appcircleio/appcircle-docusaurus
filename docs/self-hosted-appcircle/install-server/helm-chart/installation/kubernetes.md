---
title: Kubernetes
description: Learn how to install and configure self-hosted Appcircle server with Helm chart to Kubernetes
tags: [self-hosted, helm, installation, configuration, kubernetes]
sidebar_position: 20
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import NeedHelp from '@site/docs/\_need-help.mdx';

## Overview

This guide offers a comprehensive overview of installing the Appcircle chart. While the provided **default values** are suitable **for initial trials**, they are not recommended for production environments.

**For production deployments**, it is essential to **review the detailed descriptions** and **optional sections** to ensure a secure and reliable setup. **This document supports both trial and production installations**.

## Prerequisites

To complete this guide, you must have the following:

### 1. Domain Name

A main **domain name**, which will have **subdomains**, is **required** for the Appcircle server.

<details>
    <summary>Click to view more details about domain name prerequisite.</summary>

In this documentation, we will use `appcircle.spacetech.com` as an **example main domain** and `spacetech` as an **example organization name**.

By default, Appcircle uses seven subdomains. These subdomains are:

1. api.appcircle.spacetech.com
2. auth.appcircle.spacetech.com
3. dist.appcircle.spacetech.com
4. hook.appcircle.spacetech.com
5. resource.appcircle.spacetech.com
6. my.appcircle.spacetech.com
7. kvs.appcircle.spacetech.com

**Upon completing the deployment** of the Appcircle server, you will need to create DNS records based on the Ingress objects created in Kubernetes.

</details>

### 2. SSL Certificate

An **SSL certificate** is **required** to deploy the Appcircle server for **production** environments.

You **can skip** SSL certificate if you are deploying Appcircle server **for trial purposes**.

<details>
    <summary>Click to view more details about SSL certificate prerequisite.</summary>

- The SSL certificate private key shouldn't be password protected.

- The SSL certificate should be in PEM format.

- Ensure the **one certificate** covers **all the subdomains** in the [domain name](#1-domain-name) section.

- Make sure to configure the Appcircle server with a **fullchain certificate**, which should include the leaf (or app) certificate, intermediate certificates, and the root certificate.

:::tip
You can use a **wildcard certificate** to cover all the subdomains, simplifying the certificate management process. For example, a wildcard certificate for **`*.appcircle.spacetech.com`** will be enough.
:::

:::caution
If you use a domain like `appcircle.spacetech.com`, it will have **two levels of subdomains**. Ensure that both your DNS provider and SSL certificate provider support multi-level subdomains for proper configuration.
:::

</details>

### 3. Kubernetes Cluster

A **Kubernetes cluster** is **required** to install the Appcircle server using Helm.

<details>
    <summary>Click to view more details about Kubernetes cluster prerequisite.</summary>

**Minimum hardware requirements for enterprise installation:**

- Nodes with `x86_64` architecture
- 8 CPUs
- 16 GB RAM
- 500 GB Disk

**Recommended hardware requirements for enterprise installation:**

- Nodes with `x86_64` architecture
- 32 CPUs
- 64 GB RAM
- 1 TB Disk

For production environments, if you deploy stateful applications with the Appcircle Helm chart, you will need significant storage capacity, as specified above. You can configure disk resource allocations through Helm values according to your needs.

However, if you opt to use external services for components such as PostgreSQL or MinIO, the storage requirements for the cluster are significantly reduced to around 50GB. It is **highly recommended** to deploy stateful apps outside of the Appcircle Helm chart configuration.

:::tip
For stateful apps that should deployed out of scope this helm chart, you can check the [Production Readiness](/self-hosted-appcircle/install-server/helm-chart/configuration/production-readiness.md) document.

For storage details, you can check the [Storage Class Configuration](/self-hosted-appcircle/install-server/helm-chart/configuration/storage-configuration.md) section.
:::

:::info
Using SSD storage is highly recommended if stateful applications are installed within the Appcircle Helm chart scope. SSDs provide faster read/write speeds, improving the performance and responsiveness of your applications.
:::

Additionally, ensure that your Kubernetes version is 1.29.1 or later to maintain compatibility and support.

</details>

### 4. `kubectl`

The **`kubectl`** CLI is **required**.

### 5. Helm v3

**Helm version `3.11.0`** or later is **required**.

## Pre-installation Steps

### 1. Ingress Controller

The Kubernetes cluster should have **an Ingress controller** installed and configured since Appcircle exposes its services through **Ingress objects**.

For **trial** purposes, you can **use** the default **Ingress-Nginx** controller deployed **within the Helm chart** scope.

For **production** environments, it's recommended to use **your own Ingress controller**.

Appcircle server supports Ingress-Nginx controller by default. To install Ingress-Nginx controller to the Kubernetes cluster, please check [the Ingress-Nginx controller documentation](https://kubernetes.github.io/ingress-nginx/deploy/#installation-guide).

:::info
**Other Ingress controllers** like HAProxy Ingress controller are also **supported** by **modifying Helm values** accordingly.
:::

#### Enable SSL Passthrough

You can **skip** this section **if you use the default** Ingress-Nginx controller deployed **within the Helm chart scope**.

Enable **`ssl-passthrough`** feature on your ingress-controller Enabling the SSL passthrough depends on the Ingress controller that is used in the Kubernetes cluster. For example:

- For Nginx Ingress controller, you can check [the Nginx documentation](https://kubernetes.github.io/ingress-nginx/user-guide/tls/#ssl-passthrough).

- For HAProxy Ingress controller, you can check [the HAProxy documentation](https://www.haproxy.com/documentation/kubernetes-ingress/community/configuration-reference/ingress/#ssl-passthrough).

:::info
Enabling the SSL passthrough option **does not** automatically allow all SSL traffic **from all Ingress objects** to pass through to the original service. Instead, it enables Ingress resources to leverage the SSL passthrough feature, allowing encrypted traffic to reach the backend service without being decrypted by the Ingress controller.
:::

### 2. Production Readiness

If you are deploying the Appcircle server for a production environment, it is recommended that stateful applications, such as databases or object storage, be deployed outside the scope of the Appcircle server Helm chart.

For more information, you can check the [Production Readiness](self-hosted-appcircle/install-server/helm-chart/configuration/production-readiness.md) documentation.

### 3. Create Namespace

**Create a namespace** for the Appcircle server deployment. In this documentation, we will use `appcircle` as the example namespace.

```bash
kubectl create namespace appcircle
```

### 4. Create Container Registry Secret

By default, Appcircle uses its own image registry, which requires authentication with the `cred.json` file provided by Appcircle.

If you are using your own container image registry to access Appcircle container images, you can either skip authentication if your registry doesn't require it or create a secret for your custom registry.

Follow the steps below to create the registry secret in the `appcircle` namespace for pods to successfully pull images:

:::info
If you are using your own container registry, follow the `Custom Registry` section below.

If your registry doesn't require authentication, you can skip this section.
:::

<Tabs groupId="Image Registry">

  <TabItem value="appcircle-registry" label="Appcircle Registry">

- Save the `cred.json` file.

- Create the container registry secret:

```bash
kubectl create secret docker-registry containerregistry \
  -n appcircle \
  --docker-server='europe-west1-docker.pkg.dev' \
  --docker-username='_json_key' \
  --docker-password="$(cat cred.json)"
```

  </TabItem>
  <TabItem value="custom-registry" label="Custom Registry">

:::tip
If the `HISTCONTROL` environment variable is set to `ignoreboth`, commands with a leading space character will not be stored in the shell history. This allows you to create secrets safely without storing sensitive information in the shell history.
:::

- Update the `server`, `username`, and `password` fields for your own custom registry and create the container registry secret:

```bash
kubectl create secret docker-registry containerregistry \
  -n appcircle \
  --docker-server='registry.spacetech.com' \
  --docker-username='yourRegistryUsername' \
  --docker-password='superSecretRegistryPassword'
```

  </TabItem>
</Tabs>

## Installation

### 1. Create `values.yaml`

Below is a minimal `values.yaml` file that you should configure for your deployment.

**Please adjust these values** according to your environment requirements and **save your file**.

In the example values below, we used `spacetech` as an **example organization name**. You should **replace it** with your actual organization name or any other value you prefer.

:::caution
Please **review the comments for the `values.yaml`** below. If the values provided are incompatible, the installation may not complete successfully. Ensure that all configurations are correctly entered to avoid potential issues during the setup process.
:::

<Tabs groupId="Example Values">

  <TabItem value="minimal" label="Minimal Configuration">
  
<details>
    <summary>Click to view example `values.yaml` file.</summary>

```yaml
# Global configurations for Appcircle deployment
global:
  urls:
    # Main domain configuration - All Appcircle services will be subdomains of this domain
    domainName: .appcircle.spacetech.com
  # SMTP server configuration for sending emails (Authentication, Notifications, Testing Distribution)
  mail:
    smtp:
      # SMTP server host
      host: "smtp.spacetech.com"
      # SMTP Server port, 587 typically used for StartTLS
      port: "587"
      # Email address that will be used as sender
      from: "appcircle@yandex.com"
      # SSL configuration - Set to 'true' if the SMTP server uses SSL/TLS protocol for secure communication, typically on port 465.
      ssl: "false"
      # StartTLS configuration - Set to 'true' if the SMTP server uses StartTLS protocol, typically on port 587.
      tls: "true"
      # SMTP authentication settings
      auth: true
      username: "appcircle-smtp-user"
      password: "superSecretSmtpPassword"

# Authentication configuration
auth:
  auth-keycloak:
    # Initial admin user email for Appcircle server
    initialUsername: "admin@spacetech.com"
```

</details>

  </TabItem>
  <TabItem value="production" label="Production Configuration">

<details>
    <summary>Click to view example `values.yaml` file.</summary>

```yaml
# Global configurations for Appcircle deployment
global:
  urls:
    # Main domain configuration - All Appcircle services will be subdomains of this domain
    domainName: .appcircle.spacetech.com
    # Protocol to be used for connections
    scheme: https

  # SMTP server configuration for sending emails (Authentication, Notifications, Testing Distribution)
  mail:
    smtp:
      # SMTP server host
      host: smtp.spacetech.com
      # SMTP Server port, 587 typically used for StartTLS
      port: 587
      # Email address that will be used as sender
      from: appcircle@spacetech.com
      # SSL configuration - Set to 'true' if the SMTP server uses SSL/TLS protocol for secure communication, typically on port 465.
      ssl: false
      # StartTLS configuration - Set to 'true' if the SMTP server uses StartTLS protocol, typically on port 587.
      tls: true
      # SMTP authentication settings
      auth: true
      username: smtpUserName
      # You can create a secret with the password or directly enter the password here.
      password: superSecretSmtpPassword

  # If the K8s cluster access the container images from a private container image registry, you can configure it here.
  # Container Image Registry host for container images
  imageRegistry: europe-west1-docker.pkg.dev
  # Container Image Repository path between registry host and image name
  imageRepositoryPath: appcircle/docker-registry

  # Kubernetes Ingress controller class
  ingressClassName: "nginx"

  # SSL/TLS certificate configuration for HTTPS
  # You can create a secret with the certificate and key or directly enter them here.
  tlsWildcard:
    # Public certificate - Fullchain including leaf (app), intermediate and root SSL certificates
    cert: |
      -----BEGIN CERTIFICATE-----
      MIIFzTCCBLWgAwIBAgISBMLn5uQI6Wmzku14xXUbbIbmMA0GCSqGSIb3DQEBCwUA
      ...
      SA==
      -----END CERTIFICATE-----
      -----BEGIN CERTIFICATE-----
      MIIFBjCCAu6gAwIBAgIRAIp9PhPWLzDvI4a9KQdrNPgwDQYJKoZIhvcNAQELBQAw
      ...
      uYkQ4omYCTX5ohy+knMjdOmdH9c7SpqEWBDC86fiNex+O0XOMEZSa8DA
      -----END CERTIFICATE-----
      -----BEGIN CERTIFICATE-----
      MIIFazCCA1OgAwIBAgIRAIIQz7DSQONZRGPgu2OCiwAwDQYJKoZIhvcNAQELBQAw
      ...
      emyPxgcYxn/eR44/KJ4EBs+lVDR3veyJm+kXQ99b21/+jh5Xos1AnX5iItreGCc=
      -----END CERTIFICATE-----
    # Private key for the SSL certificate
    key: |
      -----BEGIN PRIVATE KEY-----
      MIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQC3wS87baGONXjr
      ...
      oUcjMAu/mGJjtn9AS0S7rRa58Q==
      -----END PRIVATE KEY-----
    # Certificate Authority public key - Typically the bottom certificate of the fullchain SSL certificate
    caCert: |
      -----BEGIN CERTIFICATE-----
      MIIFazCCA1OgAwIBAgIRAIIQz7DSQONZRGPgu2OCiwAwDQYJKoZIhvcNAQELBQAw
      ...
      emyPxgcYxn/eR44/KJ4EBs+lVDR3veyJm+kXQ99b21/+jh5Xos1AnX5iItreGCc=
      -----END CERTIFICATE-----
# Authentication configuration
auth:
  auth-keycloak:
    # Organization name for Appcircle server
    organizationName: spacetech
    # Initial admin user email for Appcircle server
    initialUsername: "admin@example.com"
    # Initial admin password - Should contain: min 6 chars, 1 lowercase, 1 uppercase, 1 number
    # You can create a secret with the password or directly enter the password here
    initialPassword: "superSecretAppcirclePassword1234"
    image:
      # Appcircle keycloak image repository path
      repository: europe-west1-docker.pkg.dev/appcircle/docker-registry/appcircle-keycloak

# Internal Ingress controller configuration
ingress-nginx:
  enabled: false

# Appcircle vault configuration
vault:
  server:
    image:
      # Appcircle vault image repository path
      repository: europe-west1-docker.pkg.dev/appcircle/docker-registry/appcircle-vault

# Web event Redis configuration
webeventredis:
  # Enable TLS for Redis connections
  tls:
    enabled: true
  # Ingress configuration for Redis
  ingress:
    enabled: true
    tls: true
```

</details>

  </TabItem>
</Tabs>

### 2. Remove Sensitive Information From `values.yaml`

**Remove sensitive information** such as Appcircle initial user password, SMTP password, SSL certificates, and other secrets from the `values.yaml` **for production environments**, by checking the [Sensitive Values](self-hosted-appcircle/install-server/helm-chart/configuration/sensitive-configuration.md) documentation.

### 3. Add the Appcircle Helm Repository

**Add the Appcircle Helm repository** to the configuration of Helm:

```bash
helm repo add appcircle https://helm-package.appcircle.io && \
helm repo update
```

### 4. Install the Appcircle Server

**Run the following Helm command** to install the Appcircle server chart.

In this example, we deploy the Appcircle server to a single namespace, using **`appcircle`** as the **namespace** and **`appcircle-server`** as the Helm **release name**.

```bash
helm install appcircle-server appcircle/appcircle \
  --timeout 1200s \
  -n appcircle \
  -f values.yaml
```

:::warning
If you need or want to change the release name, please note that it should be 18 characters or fewer.
:::

You can watch the Appcircle server installation with any Kubernetes monitoring tool. The installation process duration depends on factors such as network speed and the processing power of your Kubernetes nodes. Typically, the installation may take up to **10 to 15 minutes**.

To make sure that the Appcircle server is installed successfully, you can run the command below and wait to finish:

```bash
kubectl wait --for=condition=ready pod \
  -l app.kubernetes.io/instance=appcircle-server \
  -n appcircle --timeout 1200s && \
  echo "Appcircle is ready to use. Happy building! "
```

## Post-installation Steps

### 1. Add DNS Records

List the Ingresses with `kubectl` to check the IP address of the Appcircle services domains.

```bash
kubectl get ingresses -n appcircle
```

According to the example output below, you need to configure your DNS as follows:

```bash
NAME                               CLASS   HOSTS                                                          ADDRESS        PORTS      AGE
appcircle-apigateway               nginx   api.appcircle.spacetech.com,auth.appcircle.spacetech.com       10.45.140.78   80,443     24m
appcircle-distribution-testerweb   nginx   dist.appcircle.spacetech.com                                   10.45.140.78   80,443     24m
appcircle-resource                 nginx   resource.appcircle.spacetech.com                               10.45.140.78   80,443     24m
appcircle-store-web                nginx   *.store.appcircle.spacetech.com                                10.45.140.78   80,443     24m
appcircle-web-app                  nginx   my.appcircle.spacetech.com                                     10.45.140.78   80,443     24m
appcircle-web-event                nginx   hook.appcircle.spacetech.com                                   10.45.140.78   80,443     24m
appcircle-webeventredis            nginx   redis.appcircle.spacetech.com                                  10.45.140.78   80,443     24m
```

1. **Create an A Record for the `api` domain:**

   - `api.appcircle.spacetech.com` → **10.45.140.78**

2. **Create CNAME Records for the other domains:**
   - `auth.appcircle.spacetech.com` → **api.appcircle.spacetech.com**
   - `dist.appcircle.spacetech.com` → **api.appcircle.spacetech.com**
   - `resource.appcircle.spacetech.com` → **api.appcircle.spacetech.com**
   - `*.store.appcircle.spacetech.com` → You can skip this domain and use a [Custom Enterprise App Store Domain](https://docs.appcircle.io/enterprise-app-store/portal-settings#store-domain).
   - `my.appcircle.spacetech.com` → **api.appcircle.spacetech.com**
   - `hook.appcircle.spacetech.com` → **api.appcircle.spacetech.com**
   - `redis.appcircle.spacetech.com` → **api.appcircle.spacetech.com**

### 2. Login to the Appcircle Dashboard

Check the output of the `Helm install` command to see login URL, initial username and command to get initial user password.

```bash
You can access the application dashboard at: ↴

https://my.appcircle.spacetech.com
```

### 3. Apply the Appcircle License

When you deploy the Appcircle server using Helm, a default license is provided. You can explore the Appcircle with the default license.

To obtain the license you purchased, please share the initial organization ID, which is printed after the `helm` deployment command, with the Appcircle team and follow the detailed instructions available in the [Appcircle License Update](/self-hosted-appcircle/install-server/helm-chart/configuration/license-configuration.md) section.

<NeedHelp />
