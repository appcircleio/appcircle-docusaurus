---
title: Kubernetes
description: Learn how to install and configure self-hosted Appcircle server with Helm chart to Kubernetes
tags: [self-hosted, helm, installation, configuration, kubernetes]
sidebar_position: 6
---

import HelmYamlGenerator from '@site/src/components/HelmYamlGenerator';

## Overview

To deploy the Appcircle server on your Kubernetes cluster, use the Appcircle Helm chart. This chart includes all the necessary components for the initial setup and can scale to support larger deployments.

For a production deployment, a basic understanding of Kubernetes is sufficient. This knowledge will help you effectively manage and troubleshoot the cluster, optimize resource allocation, and maintain security.

## Prerequisites

### Domain Name

A main **domain name**, which will have **subdomains**, is required for the Appcircle server. In this documentation, we will use `appcircle.spacetech.com` as an example main domain and `spacetech` as an example organization name.

By default, Appcircle uses eight subdomains. These subdomains are:

1. api.appcircle.spacetech.com
2. auth.appcircle.spacetech.com
3. dist.appcircle.spacetech.com
4. hook.appcircle.spacetech.com
5. resource.appcircle.spacetech.com
6. store.appcircle.spacetech.com
7. my.appcircle.spacetech.com
8. redis.appcircle.spacetech.com

TODO: Maybe add the monitor domain.

**Upon completing the deployment** of the Appcircle server, you will need to create DNS records based on the ingress objects defined in Kubernetes. This should be done through your DNS service provider to ensure proper routing and accessibility.

### SSL Certificate

Modern technologies and best practices require secure communication to protect data from potential threats and ensure user privacy. Therefore, deploying the Appcircle server with an SSL certificate is essential.

Ensure the **one certificate** covers **the all subdomains** in the [domain name](#domain-name) section.

Additionally, configure the Appcircle server with a **fullchain certificate**, which should include the leaf (or app) certificate, intermediate certificates, and the root certificate, establishing a complete and trusted certificate chain.

:::tip
You can use a **wildcard certificate** to cover the all subdomains, simplifying the certificate management process. For example, a wildcard certificate for **`*.appcircle.spacetech.com`** will be enough.
:::

:::caution
If you use a domain like `appcircle.spacetech.com`, it will have **two levels of subdomains**. Ensure that both your DNS provider and SSL certificate provider support multi-level subdomains for proper configuration.
:::

:::tip
Appcircle **supports TLS 1.3**, the latest and most secure version of the TLS protocol, ensuring improved performance and stronger encryption for your connections.
:::

### Kubernetes cluster

To install the Appcircle server using Helm, a Kubernetes cluster is required. The cluster should meet the following hardware specifications:

**Minimum** hardware requirements for **enterprise installation**:

- Nodes with x86-64 architecture
- 8 CPUs
- 16 GB RAM
- TODO: Update 500 GB SSD

**Recommended** hardware requirements for **enterprise installation**:

- Nodes with x86-64 architecture
- 32 CPUs
- 64 GB RAM
- TODO: Update 1 TB SSD

TODO: Define a kubernetes version

Kubernetes version must be x.x.x or later.

### Install `kubectl`

The `kubectl` CLI configured for the target Kubernetes cluster is required.

### Install Helm

Helm version `3.11.0` or later is required for deployment.

### Kubernetes Ingress Controller

By default, Appcircle exposes its services through **Ingress objects**. To ensure these Ingress objects function properly, your Kubernetes cluster should have **an Ingress Controller** installed and configured.

Appcircle server supports Nginx Ingress Controller by default. To install Nginx Ingress Controller to the Kubernetes cluster, please check [the Nginx Ingress Controller documentation](https://kubernetes.github.io/ingress-nginx/deploy/#installation-guide).

:::info
**Other Ingress Controllers** like HAProxy Ingress Controller are also **supported** by **modifying Helm values** accordingly.
:::

#### Enable SSL Passthrough

**Redis ingress** of the Appcircle server needs **SSL passthrough** so Appcircle **runners** can connect to the Redis service that is working on Kubernetes cluster **securely**.

Enabling the SSL passthrough depends on the ingress controller that is used in the Kubernetes cluster. For example:

- For Nginx Ingress Controller, you can check [the Nginx documentation](https://kubernetes.github.io/ingress-nginx/user-guide/tls/#ssl-passthrough).

- For HAProxy Ingress Controller, you can check [the HAProxy documentation](https://www.haproxy.com/documentation/kubernetes-ingress/community/configuration-reference/ingress/#ssl-passthrough).

:::info
Enabling the SSL passthrough option **does not** automatically allow all SSL traffic **from all ingress objects** to pass through to the original service. Instead, it enables Ingress resources to leverage the SSL passthrough feature, allowing encrypted traffic to reach the backend service without being decrypted by the Ingress Controller.
:::

## Create a Configuration File

To configure Helm, you can create a `values.yaml` file by specifying your desired settings, which are commonly used across all deployments.

In the example values below, we used `spacetech` as an **example organization name**. You should **replace it** with your actual organization name or any other value you prefer.

:::caution
Please **review the comments for the `values.yaml`** below. If the values provided are incompatible, the installation may not complete successfully. Ensure that all configurations are correctly entered to avoid potential issues during the setup process.
:::

### Example `values.yaml` File

Below is an example of a `values.yaml` file that you can use to configure the Appcircle Helm chart for your Kubernetes cluster. This configuration includes settings such as domain name, SSL/TLS configurations, and email settings.

Each key has a description of what it should be used for, and you can adjust these settings according to your needs.

:::tip
You can check the [Create Container Registry Secret](#create-container-registry-secret) section to learn how to create a secret for your container registry.
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

  # SMTP server configuration for sending emails (auth, notifications, Testing Distribution)
  mail:
    smtp:
      domain: smtp.spacetech.com
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
      password: superSecretSmtpPassword

  # If the K8s cluster access the images from a private container image registry, you can configure it here.
  # For example, if the url of an image is 'europe-west1-docker.pkg.dev/appcircle/docker-registry/nginx', you can set it as follows:
  # Container Image Registry host for container images
  imageRegistry: europe-west1-docker.pkg.dev
  # Container Image Repository path between registry host and image name
  imageRepositoryPath: appcircle/docker-registry
  # Version tag for Appcircle server
  imageTag: alpha-latest
  # Container registry authentication secret
  # Contains authentication details for the container registry in JSON format
  # Check the next section below on how to create this secret
  containerRegistrySecret: '{"auths":{"europe-west1-docker.pkg.dev":{"auth": "X2pzb25fa2V5OkNvbnRlbnQgb2YgdGhlIGNyZWQuanNvbiBmaWxl"}}}'

  # Kubernetes ingress controller class
  ingressClassName: "nginx"

  # SSL/TLS certificate configuration for HTTPS
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
    initialPassword: "superSecretAppcirclePassword1234"
    image:
      # Appcircle keycloak image repository path
      repository: europe-west1-docker.pkg.dev/appcircle/docker-registry/appcircle-keycloak

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

### Update the Configuration File

#### Create Container Registry Secret

By default, Appcircle uses its own image registry that you should authenticate with the `cred.json` file you got from Appcircle.

You can create this secret on the `appcircle` namespace for Appcircle image registry by executing the following command:

:::tip
If you are using your own container registry, make sure to update the `server`, `username`, and `password` variables accordingly.
:::

1. Create the `appcircle` namespace:

```bash
kubectl create namespace appcircle
```

2. Save the `cred.json` file or your own registry password into a file named `registry-password`.

3. Run the following command on your **Linux / MacOS** terminal to create the container registry secret on the Kubernetes cluster:

```bash
kubectl create secret docker-registry containerregistry \
  --docker-server='europe-west1-docker.pkg.dev' \
  --docker-username='_json_key' \
  --docker-password="$(cat registry-password)"
```

#### Production Readiness

To ensure your deployment is ready for production, follow the guidelines provided in the [Production Readiness](/self-hosted-appcircle/configure-server/kubernetes/helm-configuration.md#production-readiness) section. This section will help you adjust the settings in the `values.yaml` file, such as providing the external PostgreSQL, MongoDB, Vault and MinIO connection strings.

#### Appcircle Server Helm Chart Configurations

Refer to the [Configuration Section](/docs/self-hosted-appcircle/configure-server/kubernetes/helm-configuration.md#update-the-configuration-file) to customize the Appcircle server for various deployment scenarios. This section provides detailed instructions on configuring different aspects of the Appcircle server using the Helm chart.

## Deploy Using Helm

Once you have gathered all the necessary configuration options, you can proceed with getting the Helm repository of the Appcircle and deploying the Appcircle server. In this example, we deploy the Appcircle server to a single namespace, using **`appcircle`** as the **namespace** and **`appcircle-server`** as the Helm **release name**.

TODO: The repository is not working for now. You should package the helm repository manually, or get it from Appcircle team. The `helm upgrade --install` commands works with the helm package from a local file.

- Add the Appcircle Helm repository.

```bash
helm repo add appcircle https://charts.appcircle.io/ && \
helm repo update
```

- Use the [configured](#create-a-configuration-file) `values.yaml` file to install the Appcircle Helm chart to your Kubernetes cluster.

:::caution
Please note that the **release name should be 18 characters or fewer**.
:::

```bash
helm upgrade --install appcircle-server appcircle/appcircle-server \
  --timeout 1200s \
  -n appcircle --create-namespace \
  -f values.yaml
```

The installation process duration depends on factors such as network speed and the processing power of your Kubernetes nodes. Typically, the installation may take up to **10 to 15 minutes**.

You can use **`watch`** command on a second terminal on **Linux/MacOS** terminals to watch the pod creation process by running:

```bash
watch kubectl get pods -n appcircle
```

If you want to make sure that all containers are **ready to use**, you can the **`kubectl wait`** command on another terminal window.

```bash
kubectl wait --for=condition=ready pod -l app.kubernetes.io/instance=appcircle-server -n appcircle --timeout 1200s && echo "Appcircle is ready to use. Happy building! "
```

When all the pods are **ready**, the command will return with success and you will see **"Appcircle is ready to use. Happy building!"** message. Now, you are ready to connect to the Appcircle UI and start to build, test and publish!

## Create DNS Records

After the Appcircle server installation is finished, you can get the IP addresses of the Appcircle domains and configure the DNS.

You can list the ingresses with `kubectl` to check the IP address of the Appcircle services domains.

```bash
kubectl get ingresses -n appcircle
```

```bash
NAME                               CLASS   HOSTS                                                          ADDRESS                                     PORTS   AGE
appcircle-apigateway               nginx   api.appcircle.spacetech.com,auth.appcircle.spacetech.com       192.168.1.245,192.168.1.246,192.168.1.247   80      24m
appcircle-distribution-testerweb   nginx   dist.appcircle.spacetech.com                                   192.168.1.245,192.168.1.246,192.168.1.247   80      24m
appcircle-resource                 nginx   resource.appcircle.spacetech.com                               192.168.1.245,192.168.1.246,192.168.1.247   80      24m
appcircle-store-web                nginx   *.store.appcircle.spacetech.com                                192.168.1.245,192.168.1.246,192.168.1.247   80      24m
appcircle-web-app                  nginx   my.appcircle.spacetech.com                                     192.168.1.245,192.168.1.246,192.168.1.247   80      24m
appcircle-web-event                nginx   hook.appcircle.spacetech.com                                   192.168.1.245,192.168.1.246,192.168.1.247   80      24m
appcircle-webeventredis            nginx   redis.appcircle.spacetech.com                                  192.168.1.245,192.168.1.246,192.168.1.247   80      24m
```

You should configure your DNS records according to your DNS provider. For a best practice, create a **`A`** record for the **`my.appcircle.spacetech.com`** and create **`CNAME`** records for other domains.

## Sign in to Appcircle

You can use the `my` prefixed domain name to access Appcircle dashboard.

For example, if you set `global.urls.domainName` to `.appcircle.spacetech.com` and deployed the Appcircle server with SSL certificates then you can use `https://my.appcircle.spacetech.com` address to access the Appcircle dashboard.

After you see the login page of the Appcircle, you can now use the **initial username** and **password** to login to the Appcircle dashboard. You can check the initial username and password from the `values.yaml` file that you have used to install Appcircle server. The values you should look for are under `auth.auth-keycloak.initialUsername` and `auth.auth-keycloak.initialPassword` keys.

## Uninstall the Appcircle Server

If you want to uninstall the Appcircle server, you can just remove the Helm release from the Kubernetes cluster.

If you haven't changed the release name and namespace name while following the [Deploy Using Helm](#deploy-using-helm) section, you can run the command below to uninstall the Appcircle server.

```bash
helm uninstall -n appcircle appcircle-server
```

### Deleting the Appcircle Server Data

(TODO: Validate the information. Uninstall and install then check if the data still exists.) [Uninstalling the Appcircle Server](#uninstall-the-appcircle-server) doesn't delete the Appcircle server data. If you want to delete all the data of the Appcircle server for a reason, you can simple delete the namespace.

If you haven't changed the namespace name while following the [Deploy Using Helm](#deploy-using-helm) section, you can run the command below to delete the all data of the Appcircle server.

```bash
kubectl delete namespace appcircle
```

## Troubleshooting & FAQ

### When we try to login to the Appcircle server, we see `too many redirects` error from browser

This error usually happens when the pods can't resolve some of [the Appcircle server domains](#domain-name).

For the solution, please make sure that the domain name server of the worker nodes of the Kubernetes cluster can resolve the Appcircle server domain names.

### When we deploy the Helm chart, the `appcircle-server-webeventredis-master-0` pod is stuck in `CrashLoopBackOff` state

This error usually happens when you select a non-valid `Appcircle CA Certificate File` while [generating the configuration file](#generate-the-configuration-file). Please make sure that the certificate you choose is the **root** certificate of the full-chain certificate.

:::tip

If you created the SSL/TLS certificate with LetsEncrypt, you should know that the `fullchain.pem` file doesn't include the root CA certificate by default.

:::

To fix the problem, you can edit the `values.yaml` file and upgrade the Helm chart.

```bash
helm upgrade appcircle-server appcircle/appcircle-server \
  --timeout 1200s \
  -n appcircle \
  -f values.yaml
```

:::caution
The `stateful` pods won't be recreated from a error state. This is known issue of Kubernetes.

You should delete the pods manually to fix this problem. The new updated pods will be created automatically. You can use the example commands below to delete the pods:

```bash
kubectl delete pods appcircle-server-webeventredis-master-0 -n appcircle && \
kubectl delete pods appcircle-server-webeventredis-replicas-0 -n appcircle && \
kubectl delete pods appcircle-server-webeventredis-replicas-1 -n appcircle
```

:::