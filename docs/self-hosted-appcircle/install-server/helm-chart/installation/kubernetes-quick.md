---
title: Kubernetes Quick Installation
description: Learn how to install and configure self-hosted Appcircle server with Helm chart to Kubernetes for testing purposes
tags: [self-hosted, helm, installation, configuration, kubernetes]
sidebar_position: 6
---

import NeedHelp from '@site/docs/\_need-help.mdx';

## Overview

This guide provides a concise yet comprehensive overview of how to install the Appcircle chart using **default values**. Please note that **default values** are intended for **trial purposes only** and are **not recommended** for use in **production environments**.

## Prerequisites

To complete this guide, you must have the following:
1. Domain Name
2. Kubernetes cluster
    - A cluster with a total of at least eight virtual CPUs and 16 GB of RAM is recommended. Kubernetes nodes should use the `x86_64` architecture.
3. kubectl.
4. Helm v3.
5. Appcircle License

## Install the Appcircle Server

### 1. Add the Appcircle Helm Repository

**Add the Appcircle Helm repository** to the configuration of Helm:

```bash
helm repo add appcircle https://helm-package.appcircle.io && \
helm repo update
```

### 2. Create Namespace

**Create a namespace** for the Appcircle server installation.

```bash
kubectl create namespace appcircle
```

### 3. Create Registry Secret

**Create a Kubernetes secret** named `containerregistry` to authenticate the Appcircle container image registry. You need a `cred.json` file you got from Appcircle with your license to access the container images. 

If you haven't got your `cred.json` already, you can [contact us](https://appcircle.io/support/).

```bash
kubectl create secret docker-registry containerregistry \
  -n appcircle \
  --docker-server='europe-west1-docker.pkg.dev' \
  --docker-username='_json_key' \
  --docker-password="$(cat cred.json)"
```

### 4. Create `values.yaml`

Below is a minimal `values.yaml` file that you should configure for your deployment.

**Please adjust these values** according to your environment requirements and **save your file**.

```yaml
global:
  urls:
    domainName: .appcircle.spacetech.com
  mail:
    smtp:
      host: 'smtp.spacetech.com'
      port: '587'
      from: 'appcircle@yandex.com'
      username: 'appcircle-smtp-user'
      password: 'superSecretSmtpPassword'
      ssl: 'false'
      tls: 'true'
auth:
  auth-keycloak:
     initialUsername: "admin@spacetech.com"
```

### 5. Install the Appcircle Server

**Run the following Helm command** to install the Appcircle server chart.

```bash
helm install appcircle-server appcircle/appcircle \
  --timeout 1200s \
  -n appcircle \
  -f values.yaml
```

You can watch the Appcircle server installation with any Kubernetes monitoring tool.

To make sure that the Appcircle server is installed successfully, you can run the command below and wait to finish:

```bash
kubectl wait --for=condition=ready pod \
  -l app.kubernetes.io/instance=appcircle-server \
  -n appcircle --timeout 1200s && \
  echo "Appcircle is ready to use. Happy building! "
```

### 6. Add DNS Records

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

### 7. Login to the Appcircle Dashboard

Check the output of the `Helm install` command to see login URL, initial username and command to get random created initial user password.

<NeedHelp />