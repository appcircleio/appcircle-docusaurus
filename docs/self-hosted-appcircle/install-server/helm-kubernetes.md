---
title: Helm for Kubernetes
description: Learn how to install and configure self-hosted Appcircle server with Helm to Kubernetes
tags: [self-hosted, helm, installation, configuration]
sidebar_position: 6
---

import YamlGenerator from '@site/src/components/YamlGenerator';

## Overview

To install Appcircle server on a Kubernetes cluster, use the Appcircle Helm chart. This chart contains all the required components to get started and can scale to large deployments.

:::caution
The default Helm chart configuration is not intended for production. The default values create an implementation where all Appcircle services are deployed in the cluster, which is not suitable for production workloads.
:::

For a production deployment, you should have strong working knowledge of Kubernetes. This method of deployment has different management, observability, and concepts than traditional deployments.

## Prerequisites

### Domain Name

A domain name that you can create SSL/TLS certificate for a couple of subdomain under it is required for Appcircle server. In this document, we will use `spacetech.com` as an example domain and `spacetech` as an organization name.

Appcircle uses 6 domain names by default. These domain names are:

1. api.spacetech.com
2. auth.spacetech.com
3. dist.spacetech.com
4. hook.spacetech.com
5. resource.spacetech.com
6. store.spacetech.com
7. my.spacetech.com
8. redis.spacetech.com

TODO: Maybe add the monitor domain.

At the end of the deploying the Appcircle server, you will create DNS record according to the ingress objects of the Kubernetes on your DNS service provider.

### SSL/TLS Certificate

You should deploy the Appcircle server with a SSL/TLS certificate for security reasons.

Create an SSL/TLS certificate that covers all @TODO: Update if required -> nine domain names mentioned in the [Domain Name](#domain-name) section in the alternative subject name extension of the certificate.

You should configure Appcircle server with a fullchain certificate.

### Kubernetes cluster

To install the Appcircle server using Helm, a Kubernetes cluster with nodes based on the `x86_64` architecture is required. The cluster must meet the following hardware specifications:

**Minimum hardware requirements for an enterprise installation:**

- TODO: Update 500 GB SSD
- 8 CPUs
- 16 GB RAM

**Recommended hardware requirements for production environments:**

- TODO: Update 1 TB SSD
- 32 CPUs
- 64 GB RAM

Currently supported Kubernetes versions:

- @TODO: Define supported Kubernetes versions.

### kubectl

Install `kubectl` by following the instructions provided in [the Kubernetes documentation](https://kubernetes.io/docs/tasks/tools/#kubectl). Ensure that the installed version is within one minor release of the version running on your cluster.

### Helm

Install Helm version 3.11.0 or later by following the instructions in [the Helm documentation](https://helm.sh/docs/intro/install/).

### PostgreSQL

The Appcircle chart, by default, includes an in-cluster PostgreSQL deployment provided by `bitnami/PostgreSQL`. This deployment is intended for testing and evaluation purposes only, and is not recommended for production environments.

For a production-ready setup, it is essential to configure an external PostgreSQL instance. The recommended version is PostgreSQL 16.

If you are deploying the Appcircle server for testing purposes, you may use the built-in PostgreSQL deployment.

### MongoDB

Similarly, the Appcircle chart includes an in-cluster MongoDB deployment provided by `bitnami/mongodb` by default. This deployment is intended for testing and evaluation purposes only, and is not recommended for production environments.

To ensure optimal performance and reliability in a production environment, it is recommended to set up an external, production-grade MongoDB instance. The recommended version is MongoDB 7.0.

If you are deploying the Appcircle server for testing purposes, the built-in MongoDB deployment can be used.

### MinIO

By default, the Appcircle chart includes an in-cluster MinIO deployment provided by @TODO: change -> `stable/minio`. This deployment is intended for testing and evaluation purposes only, and is not recommended for production environments.

For production environments, it is highly recommended to configure an external, production-grade MinIO instance to ensure scalability, high availability, and data durability.

If you are installing the Appcircle for testing purposes, you may use the built-in MinIO deployment.

### Kafka

By default, the Appcircle chart includes an in-cluster Kafka deployment provided by `bitnami/kafka`. This deployment is intended for testing and evaluation purposes only, and is not recommended for production environments.

For production deployments, you should set up an external, production-ready Kafka cluster to handle high-throughput messaging and ensure proper fault tolerance and scaling.

For testing environments, the built-in Kafka deployment can be used.

### HashiCorp Vault

By default, the Appcircle chart includes an in-cluster HashiCorp Vault deployment provided by `hashicorp/vault`. This deployment is intended for testing and evaluation purposes only, and is not recommended for production environments.

For production, you should configure an external, production-grade Vault instance to ensure robust secret management, scalability, and high availability.

If you are deploying the appcircle for testing purposes, the built-in Vault deployment can be used.

### Kubernetes Ingress Controller

By default, to expose services, Appcircle uses name-based virtual servers that are configured with Ingress objects. For the Ingress objects works, the Kubernetes cluster should have a Ingress Controller.

Appcircle server supports Nginx Ingress Controller by default.

To install Nginx Ingress Controller to the Kubernetes cluster, please check [the Nginx documentation](https://kubernetes.github.io/ingress-nginx/deploy/#installation-guide).

#### Enable SSL Passthrough

SSL passthrough allows SSL traffic to pass through a load balancer without decrypting it. The SSL/TLS termination is done at the backend server, not at the load balancer.

Redis ingress of the Appcircle server needs SSL passthrough so Appcircle runners can connect to the Redis service that is working on Kubernetes cluster securely.

Enabling the SSL passthrough depends on the ingress controller that is used in the Kubernetes cluster. For example:

- For Nginx Ingress Controller, check [the Nginx documentation](https://kubernetes.github.io/ingress-nginx/user-guide/tls/#ssl-passthrough).

  - In a summary, should edit the Nginx controller deployment and add the `--enable-ssl-passthrough` flag to the `args` section.

- @TODO: should be reviewed and tested to see if we support HAProxy-> For HAProxy Ingress Controller, check [the HAProxy documentation](https://www.haproxy.com/documentation/kubernetes-ingress/community/configuration-reference/ingress/#ssl-passthrough).
- @TODO: should be reviewed and tested to see if we support Traefik-> For Traefik Ingress Controller, check [the Traefik documentation](https://traefik.io/blog/https-on-kubernetes-using-traefik-proxy/).

### Create Configuration File

To configure Helm, you can create a `global.yaml` file by specifying your desired settings, which are commonly used across all deployments.

<YamlGenerator />

Click the `Generate YAML` button to create a ready-to-use configuration file. Once the YAML is generated, copy the content and save it as a file named `global.yaml`.

We will reference this configuration file as `global.yaml` for the rest of this documentation.

### Update the Configuration File

Although the `Generate YAML` button above generates a `yaml` file that you can use when deploying the Appcircle server to Kubernetes, there are some points in this file that you need to configure manually.

Open the `global.yaml` with your favorite editor.

```bash
vi global.yaml
```

#### Edit the SMTP Settings

Appcircle needs an SMTP server to send emails for operations such as user authorization, Testing Distribution, notification emails.

The `global.yaml` configuration file contains `.global.smtp` key to store the SMTP settings that the Appcircle will use.

- `auth`: Should be 'true' if the SMTP server requires authentication. False for otherwise.
- `username`: SMTP username for authentication if the `auth` is set to 'true'. You can leave the value empty if the `auth` is false.
- `password`: SMTP password for authentication if the `auth` is set to 'true'. You can leave the value empty if the `auth` is false.
  @TODO: deprecate this
- `domain`: SMTP server domain name.
- `host`: Domain or IP address of the SMTP server.
- `port`: Port number of the SMTP server.
- `from`: Email address that Appcircle will send emails from.
- `ssl`: Set to 'true' if the SMTP server uses SSL/TLS protocol for secure communication, typically on port 465.
- `tls`: Set to 'true' if the SMTP server uses StartTLS protocol for upgrading an unencrypted connection to a secure one, typically on port 587.

:::tip
For most cases, `ssl` and `tls` can't be 'true' at the same time.
:::

:::info
If you are not using secure connections for SMTP communication, you should set both `ssl` and `tls` to 'false'.
:::

```yaml
global:
  mail:
    smtp:
      auth: "true"
      username: "appcircle-smtp-user"
      password: "super-secret-smtp-password"
      # @TODO: deprecate this
      domain: "smtp.spacetech.com"
      host: "smtp.spacetech.com"
      port: "587"
      from: "appcircle@spacetech.com"
      ssl: "false"
      tls: "true"
```

#### Configure the SSL/TLS Certificates

You can follow the steps below to configure the SSL/TLS certificates in your `global.yaml`:

- Add your fullchain certificate and private key under the `.global.tlsWildcard` key.

  - `cert`: Should be the public certificate of the SSL/TLS certificate.
  - `key`: Should be the private key of the SSL/TLS certificate.
  - `caCert`: Should be the Certificate Authority public key. Typically the bottom certificate of your fullchain certificate. If you are using a single certificate instead of a full chain certificate, `caCert` should be that single certificate.

:::info
The `.global` key already exists in your `global.yaml` file. You should just add the `tlsWildcard` key.
:::

```yaml
global:
  tlsWildcard:
    cert: |
      -----BEGIN CERTIFICATE-----
      MIIE7zCCA9egAwIBAgIRAMuL6km3baPC7pQC2G0FCZ0wDQYJKoZIhvcNAQELBQAw
      ...
      lxvhabfGso2n9ppuEAFwMZSdDkhFX6FRvXJAldlpFh4v5Ul1VEjaMHAe/go70NLm
      uTTH2V/Zq/L6T6Sz+R06ZJywSA==
      -----END CERTIFICATE-----
      -----BEGIN CERTIFICATE-----
      MIIFHTCCAwWgAwIBAgICEAAwDQYJKoZIhvcNAQELBQAwgaMxCzAJBgNVBAYTAlRS
      ...
      FiMVxtvuaWheLrKDNpD80TGnizYXFQlmWBGRQSv1juCIx/c3JWElda3AWLf9KomB
      dFBVrpgXba7IinYmwobBlHk=
      -----END CERTIFICATE-----
      -----BEGIN CERTIFICATE-----
      MIIGOTCCBCGgAwIBAgIUU5MNim6S8RDvILFbqSEEFJvqkUkwDQYJKoZIhvcNAQEL
      JBr5DP/2RTmkKFtc53xoSYXQCmg61T8vMycvrdxWX6eAa8VSDszAtl//QFJIrwY8
      ...
      ZmukIMGOIYPWDhsuJA==
      -----END CERTIFICATE-----
    key: |
      -----BEGIN RSA PRIVATE KEY-----
      MIIEpAIBAAKCAQEA4MtI/9wqs44tCtf6XgACSzNCxHfoajBRnic+OvCPXpacfFWw
      ...
      wMu/IaqM2mIIvQLI90D/ea1JOUrR3m8HK/faGFVz1+I/3GgkoZnYIA==
      -----END RSA PRIVATE KEY-----
    caCert: |
      -----BEGIN CERTIFICATE-----
      MIIGOTCCBCGgAwIBAgIUU5MNim6S8RDvILFbqSEEFJvqkUkwDQYJKoZIhvcNAQEL
      JBr5DP/2RTmkKFtc53xoSYXQCmg61T8vMycvrdxWX6eAa8VSDszAtl//QFJIrwY8
      ...
      ZmukIMGOIYPWDhsuJA==
      -----END CERTIFICATE-----
```

#### Configure External Stateful Apps

If you are deploying the Appcircle server for production, you should have stateful apps outside of the Kubernetes cluster. You can skip this section if you are deploying the Appcircle server for test environments.

@TODO: Fill here.

## Deploy Using Helm

Once you have gathered all the necessary configuration options, you can proceed with getting the Helm repository of the Appcircle and deploying the Appcircle server. In this example, we will use `appcircle` as Helm release name and install the Appcircle server into the `appcircle-ns` namespace.

- Add the Appcircle Helm repository.

```bash
helm repo add appcircle https://charts.appcircle.io/ && \
helm repo update
```

- Use the configured `global.yaml` file to install the Appcircle Helm chart to your Kubernetes cluster.

```bash
helm upgrade --install appcircle appcircle/appcircle-server \
  --timeout 1200s \
  -n appcircle-ns --create-namespace \
  -f global.yaml
```

Please note that the release name must be 16 characters or fewer.

The installation process duration depends on factors such as network speed and the processing power of your Kubernetes nodes. Typically, the installation may take between 10 to 15 minutes.

You can use `watch` command on a second terminal on Linux/MacOS systems to watch the pod creation process by running:

```bash
watch kubectl get pods -n appcircle-ns
```

If you want to make sure that all containers are ready to use, you can the `kubectl wait` command on a third terminal window. The `appcircle` in the command is the Helm release name. So if you have changed the release name in the installation process, change the command according to your release name.

```bash
kubectl wait --for=condition=ready pod -l app.kubernetes.io/instance=appcircle --timeout 1200s
```

When all the pods are ready, the command will return with success. You are ready to connect to the Appcircle UI and start to discover.

## Create DNS Records

After the Appcircle server installation is finished, you can get the IP addresses of the Appcircle domains and configure the DNS.

You can list the ingresses with `kubectl` to check the IP address of the Appcircle services domains.

```bash
kubectl get ingresses -n appcircle-ns
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

After you see the login page of the Appcircle, you can now use the initial username and password to login to the Appcircle dashboard. You can check the initial username and password from the `global.yaml` file that you have used to install Appcircle server. The values you should look for are under `auth.auth-keycloak.initialUsername` and `auth.auth-keycloak.initialPassword` keys.

## Troubleshooting & FAQ

### When we try to login to the Appcircle server, we see `too many redirects` error from browser

This error usually happens when the pods can't resolve some of [the Appcircle server domains](#domain-name).

For the solution, please make sure that the domain name server of the worker nodes of the Kubernetes cluster can resolve the Appcircle server domain names.
