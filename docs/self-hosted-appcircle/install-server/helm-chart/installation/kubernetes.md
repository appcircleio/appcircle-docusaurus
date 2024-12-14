---
title: Kubernetes Production Installation
description: Learn how to install and configure self-hosted Appcircle server with Helm chart to Kubernetes
tags: [self-hosted, helm, installation, configuration, kubernetes]
sidebar_position: 7
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import NeedHelp from '@site/docs/\_need-help.mdx';

## Overview

To deploy the Appcircle server on a Kubernetes cluster, use the Appcircle Helm chart. This chart includes all the necessary components for the initial setup and can scale to support larger deployments.

For a production deployment, a basic understanding of Kubernetes is sufficient. This knowledge will help you effectively manage and troubleshoot the cluster, optimize resource allocation, and maintain security.

Some example commands in this documentation are written for Linux and macOS terminals. You can use the appropriate alternatives for other operating systems.

:::warning
This Helm chart is currently in public beta. Please use it with caution and report any feedback or problems to help improve the chart.
:::

## Prerequisites

### Domain Name

A main **domain name**, which will have **subdomains**, is **required** for the Appcircle server. 

### SSL Certificate

An **SSL certificate** is **required** to deploy the Appcircle server for production environments.

Ensure the **one certificate** covers **all the subdomains** in the [domain name](#domain-name) section.

Currently, the self-hosted Appcircle does not support the use of password-protected private keys for SSL certificates. The SSL certificate should be in PEM format.

Additionally, configure the Appcircle server with a **fullchain certificate**, which should include the leaf (or app) certificate, intermediate certificates, and the root certificate, establishing a complete and trusted certificate chain.



:::tip
Appcircle **supports TLS 1.3**, the latest and most secure version of the TLS protocol, ensuring improved performance and stronger encryption for your connections.
:::

### Kubernetes cluster

A Kubernetes cluster is required to install the Appcircle server using Helm. The cluster should meet the following hardware specifications:

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

However, if you opt to use external services for components such as PostgreSQL or MinIO, the storage requirements for the cluster are significantly reduced to around 50GB.

:::info
Using SSD storage is highly recommended if stateful applications are installed within the Appcircle Helm chart scope. SSDs provide faster read/write speeds, improving the performance and responsiveness of your applications.
:::

:::tip
For stateful apps that should deployed out of scope this helm chart, you can check the [Production Readiness](/self-hosted-appcircle/install-server/helm-chart/configuration/production-readiness.md) document.

For storage details, you can check the [Storage Class Configuration](/self-hosted-appcircle/install-server/helm-chart/configuration/storage-configuration.md) section.
:::

Additionally, ensure that your Kubernetes version is 1.29.1 or later to maintain compatibility and support.

### `kubectl`

The `kubectl` CLI configured for the target Kubernetes cluster is required.

### Helm

Helm version `3.11.0` or later is required for deployment.

### Kubernetes Ingress Controller

The Kubernetes cluster should have **an Ingress controller** installed and configured since Appcircle exposes its services through **Ingress objects**.

Appcircle server supports Nginx Ingress controller by default. To install Nginx Ingress controller to the Kubernetes cluster, please check [the Nginx Ingress controller documentation](https://kubernetes.github.io/ingress-nginx/deploy/#installation-guide).

:::info
**Other Ingress controllers** like HAProxy Ingress controller are also **supported** by **modifying Helm values** accordingly.
:::

#### Enable SSL Passthrough

The Ingress controller **should have `ssl-passthrough` feature enabled**. The Ingress object named `kvs` for the Appcircle server, registered as part of [Appcircle domains](#domain-name), requires SSL passthrough to allow Appcircle runners to securely connect to the `kvs` service running within the Kubernetes cluster.

Enabling the SSL passthrough depends on the Ingress controller that is used in the Kubernetes cluster. For example:

- For Nginx Ingress controller, you can check [the Nginx documentation](https://kubernetes.github.io/ingress-nginx/user-guide/tls/#ssl-passthrough).

- For HAProxy Ingress controller, you can check [the HAProxy documentation](https://www.haproxy.com/documentation/kubernetes-ingress/community/configuration-reference/ingress/#ssl-passthrough).

:::info
Enabling the SSL passthrough option **does not** automatically allow all SSL traffic **from all Ingress objects** to pass through to the original service. Instead, it enables Ingress resources to leverage the SSL passthrough feature, allowing encrypted traffic to reach the backend service without being decrypted by the Ingress controller.
:::

## Pre-Installation Steps

### Create Configuration File

To configure Helm, you can create a `values.yaml` file by specifying your desired settings, which are commonly used by most users.

In the example values below, we used `spacetech` as an **example organization name**. You should **replace it** with your actual organization name or any other value you prefer.

:::caution
Please **review the comments for the `values.yaml`** below. If the values provided are incompatible, the installation may not complete successfully. Ensure that all configurations are correctly entered to avoid potential issues during the setup process.
:::

#### Example `values.yaml` File

Below is an example of a `values.yaml` file that you can use to configure the Appcircle Helm chart for your Kubernetes cluster. This configuration includes settings such as domain name, SSL/TLS configurations, and email settings.

Each key has a description of what it should be used for, and you can adjust these settings according to your needs.

:::tip
The example `values.yaml` below includes only the most commonly used configuration options.
:::

```yaml
# Global configurations for Appcircle deployment
global:
  # Defines the environment type
  appEnvironment: "Production"
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
      # Port 587 typically used for StartTLS
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

### Create Container Registry Secret

By default, Appcircle uses its own image registry that you should authenticate with the `cred.json` file you got from Appcircle.

You can create the registry secret on the `appcircle` namespace for pods to successfully pull the images by executing the following sections below:

1. Create the `appcircle` namespace if you haven't already created it:

:::info
In this documentation, we will deploy all the resources under the `appcircle` namespace. You can change this to any other namespace if you prefer.
:::

```bash
kubectl create namespace appcircle
```

:::info
If you are using your own container registry, you can follow the `Custom Registry` section below.

If the registry you are using doesn't require any authentication, you can skip this section.
:::

<Tabs groupId="Image Registry">

  <TabItem value="appcircle-registry" label="Appcircle Registry">

2. Save the `cred.json` file.

3. Create the container registry secret:

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


2. Update the `server`, `username`, and `password` fields for your own custom registry and create the container registry secret:

```bash
kubectl create secret docker-registry containerregistry \
  -n appcircle \
  --docker-server='registry.spacetech.com' \
  --docker-username='yourRegistryUsername' \
  --docker-password='superSecretRegistryPassword'
```

  </TabItem>
</Tabs>

### Secure Sensitive Data With Kubernetes Secrets (Optional)

To optionally remove sensitive data from the `values.yaml` file, you can create some secrets before you deploy the Appcircle server Helm chart. For more information, you can check the [Secrets for Sensitive Values section.](/docs/self-hosted-appcircle/install-server/helm-chart/configuration/sensitive-configuration.md)

### Production Readiness (Optional)

To optionally ensure your deployment is ready for production, follow the guidelines provided in the [Production Readiness](/self-hosted-appcircle/install-server/helm-chart/configuration/production-readiness.md) document. This section will help you adjust the settings in the `values.yaml` file, such as providing the external PostgreSQL, MongoDB, Vault, and MinIO connection settings.

### Appcircle Server Helm Chart Configurations (Optional)

Optionally, refer to the [Configuration Section](/self-hosted-appcircle/install-server/helm-chart/configuration/advanced-configuration.md) to customize the Appcircle server for various deployment scenarios. This section provides detailed instructions on configuring different aspects of the Appcircle server using the Helm chart.

## Deploy Using Helm

Once you have gathered all the necessary configuration options, you can proceed with getting the Helm repository of the Appcircle and deploying the Appcircle server. In this example, we deploy the Appcircle server to a single namespace, using **`appcircle`** as the **namespace** and **`appcircle-server`** as the Helm **release name**.

- Add the Appcircle Helm repository.

```bash
helm repo add appcircle https://helm-package.appcircle.io && \
helm repo update
```

- Use the [configured](#create-configuration-file) `values.yaml` file to install the Appcircle Helm chart to your Kubernetes cluster.

:::info
If you need or want to change the release name, please note that it should be 18 characters or fewer.
:::

```bash
helm upgrade --install appcircle-server appcircle/appcircle \
  --timeout 1200s \
  -n appcircle --create-namespace \
  -f values.yaml
```

The installation process duration depends on factors such as network speed and the processing power of your Kubernetes nodes. Typically, the installation may take up to **10 to 15 minutes**.

If you want to make sure that all containers are **ready to use**, you can use the **`kubectl wait`** command in another terminal window.

```bash
kubectl wait --for=condition=ready pod \
  -l app.kubernetes.io/instance=appcircle-server \
  -n appcircle --timeout 1200s && \
  echo "Appcircle is ready to use. Happy building! "
```

When all the pods are **ready**, the command will return with success, and you will see **"Appcircle is ready to use. Happy building!"** message. Now, you are ready to connect to the Appcircle UI and start to build, test and, publish!

## Post-installation Steps

### Add DNS Records

After the Appcircle server installation is finished, you can get the IP addresses of the Appcircle domains and configure the DNS.

You can list the Ingresses with `kubectl` to check the IP address of the Appcircle services domains.

```bash
kubectl get ingresses -n appcircle
```

```bash
NAME                               CLASS   HOSTS                                                          ADDRESS        PORTS      AGE
appcircle-apigateway               nginx   api.appcircle.spacetech.com,auth.appcircle.spacetech.com       10.45.140.78   80,443     24m
appcircle-distribution-testerweb   nginx   dist.appcircle.spacetech.com                                   10.45.140.78   80,443     24m
appcircle-resource                 nginx   resource.appcircle.spacetech.com                               10.45.140.78   80,443     24m
appcircle-store-web                nginx   *.store.appcircle.spacetech.com                                10.45.140.78   80,443     24m
appcircle-web-app                  nginx   my.appcircle.spacetech.com                                     10.45.140.78   80,443     24m
appcircle-web-event                nginx   hook.appcircle.spacetech.com                                   10.45.140.78   80,443     24m
appcircle-webeventredis            nginx   kvs.appcircle.spacetech.com                                    10.45.140.78   80,443     24m
```

You should configure your DNS records according to your DNS provider. For a best practice, create an **`A`** record for **`my.appcircle.spacetech.com`** and create **`CNAME`** records for other domains.

### Sign in to Appcircle

You can use the URL printed after the `helm` deployment command to access the Appcircle dashboard.

```bash
You can access the application dashboard at: ↴

https://my.appcircle.spacetech.com
```

After you see the login page of the Appcircle, you can now use the **initial username** and **password** to login to the Appcircle dashboard.

You can view the initial username printed after the `helm` deployment and view the initial password by running the `kubectl` secret command printed after the `helm` deployment:

```bash
kubectl get secret appcircle-server-auth-keycloak-passwords \
  -ojsonpath='{.data.initialPassword}' | base64 --decode ; echo
```

### License Configuration

When you deploy the Appcircle server using Helm, a default license is provided. You can explore the Appcircle with the default license.

To obtain the license you purchased, please share the initial organization ID, which is printed after the `helm` deployment command, with the Appcircle team and follow the detailed instructions available in the [Appcircle License Update](/self-hosted-appcircle/install-server/helm-chart/configuration/advanced-configuration.md#appcircle-license) section.

## Updating Appcircle Server

To update the Appcircle server deployment, follow the steps below:

### Check the Current Version

To check the current version of the Appcircle server, you can use the following `helm list` command:

```bash
helm list -n appcircle
```

This will show the currently deployed version of the Appcircle server in the `appcircle` namespace.

```bash
NAME            	NAMESPACE	REVISION	UPDATED                             	STATUS  	CHART          	APP VERSION
appcircle-server	appcircle	1       	2024-12-06 11:00:23.509105 +0300 +03	deployed	appcircle-0.1.0	3.21.0
```

In the example output, we see that Helm chart version `0.1.0` and Appcircle server version `3.21.0` are installed.

To list the available versions of the Appcircle chart, use the following command:

```bash
helm search repo appcircle --versions | head -n 10
```

This will display the top 10 available versions of the Appcircle Helm chart that you can upgrade to.

<NeedHelp />