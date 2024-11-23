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

A main domain name, which will have subdomains, is required for the Appcircle server. In this documentation, we will use `appcircle.spacetech.com` as an example main domain and `spacetech` as an example organization name.

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

Upon completing the deployment of the Appcircle server, you will need to create DNS records based on the ingress objects defined in Kubernetes. This should be done through your DNS service provider to ensure proper routing and accessibility.

### SSL Certificate

Modern technologies and best practices require secure communication to protect data from potential threats and ensure user privacy. Therefore, deploying the Appcircle server with an SSL/TLS certificate is essential.

Ensure the **one certificate** covers **the all subdomains** in the [domain name](#domain-name) section.

Additionally, configure the Appcircle server with a **fullchain certificate**, which should include the leaf (or app) certificate, intermediate certificates, and the root certificate, establishing a complete and trusted certificate chain.

:::tip
You can use a **wildcard certificate** to cover the all subdomains, simplifying the certificate management process. For example, a wildcard certificate for **`*.appcircle.spacetech.com`** will be enough.
:::

:::caution
If you use a domain like `appcircle.spacetech.com`, it will have **two levels of subdomains**. Ensure that both your DNS provider and SSL certificate provider support multi-level subdomains for proper configuration.
:::

:::tip
Appcircle supports TLS 1.3, the latest and most secure version of the TLS protocol, ensuring improved performance and stronger encryption for your connections.
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

By default, Appcircle exposes its services using name-based virtual servers, which are configured through Ingress objects. To ensure these Ingress objects function properly, your Kubernetes cluster must have an Ingress Controller installed and configured.

Appcircle server supports Nginx Ingress Controller by default. To install Nginx Ingress Controller to the Kubernetes cluster, please check [the Nginx Ingress Controller documentation](https://kubernetes.github.io/ingress-nginx/deploy/#installation-guide).

#### Enable SSL Passthrough

SSL passthrough allows SSL traffic to pass through a load balancer without decrypting it. The SSL/TLS termination is done at the backend server, not at the load balancer.

Redis ingress of the Appcircle server needs SSL passthrough so Appcircle runners can connect to the Redis service that is working on Kubernetes cluster securely.

Enabling the SSL passthrough depends on the ingress controller that is used in the Kubernetes cluster. For example:

- For Nginx Ingress Controller, check [the Nginx documentation](https://kubernetes.github.io/ingress-nginx/user-guide/tls/#ssl-passthrough).

  - In a summary, should edit the Nginx controller deployment and add the `--enable-ssl-passthrough` flag to the `args` section.

- @TODO: should be reviewed and tested to see if we support HAProxy-> For HAProxy Ingress Controller, check [the HAProxy documentation](https://www.haproxy.com/documentation/kubernetes-ingress/community/configuration-reference/ingress/#ssl-passthrough).

:::info
Enabling the SSL passthrough option **does not** automatically allow all SSL traffic **from all ingress objects** to pass through to the original service. Instead, it enables Ingress resources to leverage the SSL passthrough feature, allowing encrypted traffic to reach the backend service without being decrypted by the Ingress Controller.
:::

### Create a Configuration File

To configure Helm, you can create a `values.yaml` file by specifying your desired settings, which are commonly used across all deployments.

We will reference this configuration file as `values.yaml` for the rest of this documentation.

:::caution
Please review the information for the input boxes below. If the values provided are incompatible, the installation may not complete successfully. Ensure that all configurations are correctly entered to avoid potential issues during the setup process.
:::

:::info
In the example values below, we used `spacetech` as an example organization name. You should replace it with your actual organization name or any other value you prefer.
:::

#### Appcircle General Settings

- `The Organization Name`: Enter your organization's name.
- `Appcircle Main Domain`: Specify the [domain name](#domain-name) that will host nine subdomains. Ensure the domain is properly configured and can handle subdomain creation as required.
- `Appcircle Initial User Email`: Provide the admin email address for the Appcircle server. It is recommended to use an email address that exists and can receive emails for password reset purposes.
- `Appcircle Initial User Password`: Set the password for the initial user. The password must adhere to the Appcircle password policy:
  - Minimum length of 6 characters.
  - At least one lowercase letter.
  - At least one uppercase letter.
  - At least one numeric digit.

---

#### Container Image Registry Settings

- `Container Registry Host`: Enter the domain or IP address of your container image registry, such as Harbor or Nexus, if using an external image registry.
- `Container Image Repository Path`: Specify the path of the container images. This is typically the segment between your registry host and the image name. For example, in the image path `registry.spacetech.com/appcircle-proxy/image:tag`, the repository path is `appcircle-proxy`.
- `Container Image Tag`: (Consider removing if unnecessary) Specify the version of the Appcircle server, such as `v3.23.1`, `latest`, or `beta-latest`.
- `Container Image Registry Requires Authentication`: Select this option if the container image registry requires authentication.
- `Container Image Registry Username`: For the default image registry, use `_json_key` as the username.
- `Container Image Registry Password`: Enter the content of the `cred.json` file, which you must obtain from Appcircle, for the default image registry.

:::tip
You don't need to change `Container Image Registry Host, Path and Tag` settings if you are not using an external container image registry.
:::

---

#### SMTP Settings

Appcircle needs an SMTP server to send emails for operations such as user authorization, Testing Distribution, notification emails.

- `SMTP Host`: Domain or IP address of the SMTP server.
- `SMTP Port`: Port number of the SMTP server.
- `SMTP SSL/TLS`: Set to 'true' if the SMTP server uses SSL/TLS protocol for secure communication, typically on port 465.
- `SMTP StartTLS`: Set to 'true' if the SMTP server uses StartTLS protocol for upgrading an unencrypted connection to a secure one, typically on port 587.
- `SMTP Send Emails From`: Email address that Appcircle will send emails from.
- `SMTP Server Requires Authentication`: Should be 'true' if the SMTP server requires authentication. False for otherwise.
- `SMTP Username`: SMTP username for authentication if the `auth` is set to 'true'. You can leave the value empty if the `auth` is false.
- `SMTP Password`: SMTP password for authentication if the `auth` is set to 'true'. You can leave the value empty if the `auth` is false.

:::tip
For most cases, `SMTP SSL/TLS` and `SMTP StartTLS` can't be `true` at the same time.
:::

:::info
If you are not using secure connections for SMTP communication, you should set both `SMTP SSL/TLS` and `SMTP StartTLS` to 'false'.
:::

---

#### Configure the SSL/TLS Certificates

With the example configuration, Appcircle configures the ingress objects with SSL/TLS certificates so the client that connect to Appcircle uses HTTPS instead of HTTP.

  - `Appcircle SSL/TLS Certificate File`: Should be the public certificate of the SSL/TLS certificate. It is best practice to use fullchain certificates (including intermediate certificates) instead of single certificates.
  - `Appcircle SSL/TLS Private Key File`: Should be the private key of the SSL/TLS certificate.
  - `Appcircle CA Certificate File`: Should be the Certificate Authority public key. Typically the bottom certificate of your fullchain certificate. If you are using a single certificate instead of a full chain certificate, `Appcircle CA Certificate File` should be that single certificate.

---

#### Generate the Configuration File

<HelmYamlGenerator />

Click the `Generate YAML` button to create a pre-configured YAML file. After the YAML is generated, copy its content and save it as a file named `values.yaml` in the directory where you will execute the Helm commands.

### Update the Configuration File

#### Production Readiness

To ensure your deployment is ready for production, follow the guidelines provided in the [Production Readiness](/self-hosted-appcircle/configure-server/kubernetes/helm-configuration.md#production-readiness) section. This section will help you adjust the settings in the `values.yaml` file to meet production standards and requirements.

#### Appcircle Server Helm Chart Configurations

Refer to the [Configuration Section](/docs/self-hosted-appcircle/configure-server/kubernetes/helm-configuration.md#update-the-configuration-file) to customize the Appcircle server for various deployment scenarios. This section provides detailed instructions on configuring different aspects of the Appcircle server using the Helm chart.

## Deploy Using Helm

Once you have gathered all the necessary configuration options, you can proceed with getting the Helm repository of the Appcircle and deploying the Appcircle server. In this example, we deploy the Appcircle server to a single namespace, using `appcircle` as the namespace and `appcircle-server` as the Helm release name.

TODO: The repository is not working for now. You should package the helm repository manually, or get it from Appcircle team. The `helm upgrade --install` commands works with the helm package from a local file.
- Add the Appcircle Helm repository.

```bash
helm repo add appcircle https://charts.appcircle.io/ && \
helm repo update
```

- Use the [configured](#create-a-configuration-file) `values.yaml` file to install the Appcircle Helm chart to your Kubernetes cluster.

:::caution
Please note that the release name must be 18 characters or fewer.
:::

```bash
helm upgrade --install appcircle-server appcircle/appcircle-server \
  --timeout 1200s \
  -n appcircle --create-namespace \
  -f values.yaml
```



The installation process duration depends on factors such as network speed and the processing power of your Kubernetes nodes. Typically, the installation may take between 10 to 15 minutes.

You can use `watch` command on a second terminal on **Linux/MacOS** terminals to watch the pod creation process by running:

```bash
watch kubectl get pods -n appcircle
```

If you want to make sure that all containers are ready to use, you can the `kubectl wait` command on another terminal window. The `appcircle` in the command is the Helm release name. So if you have changed the release name in the installation process, change the command according to your release name.

```bash
kubectl wait --for=condition=ready pod -l app.kubernetes.io/instance=appcircle-server -n appcircle --timeout 1200s
```

When all the pods are ready, the command will return with success. You are ready to connect to the Appcircle UI and start to discover.

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

You should configure your DNS records according to your DNS provider. For a best practice, create a `A` record for the `my.appcircle.spacetech.com` and create `CNAME` records for other domains.

## Sign in to Appcircle

You can use the `my` prefixed domain name to access Appcircle dashboard. For example, if you set `global.urls.domainName` to `.appcircle.spacetech.com` then you should use `my.appcircle.spacetech.com` address.

After you see the login page of the Appcircle, you can now use the initial username and password to login to the Appcircle dashboard. You can check the initial username and password from the `values.yaml` file that you have used to install Appcircle server. The values you should look for are under `auth.auth-keycloak.initialUsername` and `auth.auth-keycloak.initialPassword` keys.

## Uninstall the Appcircle Server

If you want to uninstall the Appcircle server, you can just remove the Helm release from the Kubernetes cluster.

If you haven't changed the release name and namespace name while following the [Deploy Using Helm](#deploy-using-helm) section, you can run the command below to uninstall the Appcircle server.

```bash
helm uninstall -n appcircle appcircle-server
```

## Deleting the Appcircle Server Data

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

