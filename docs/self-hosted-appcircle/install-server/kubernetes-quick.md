---
title: Kubernetes Express Install
description: Learn how to install and configure self-hosted Appcircle server with Helm chart to Kubernetes
tags: [self-hosted, helm, installation, configuration, kubernetes, express]
sidebar_position: 6
---

## Overview

This guide serves as a concise but complete documentation about how to install the Appcircle chart with **default values**. **The default values** for **trial purposes** only and **not recommended** for use in **production environments**.

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

**Add the Appcircle Helm repository** to configuration of the Helm:

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

**Create a Kubernetes secret** named `containerregistry` to authenticate Appcircle container image registry. You need a `cred.json` file you got from Appcircle with your license to access the container images. 

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
    domainName: .k8s-appcircle.burakberk.com
  mail:
    smtp:
      host: 'smtp.yandex.com'
      username: 'alexismokar@yandex.com'
      domain: 'smtp.yandex.com'
      from: 'alexismokar@yandex.com'
      port: '465'
      password: 'gfvodgkvewgsnakj'
      ssl: 'true'
      tls: 'false'
auth:
  auth-keycloak:
     initialUsername: "berk@appcircle.io"
webeventredis:
  master:
    preExecCmds: ''
```

### 5. Install the Appcircle Server

**Run the following Helm command** to install the Appcircle server chart.

```bash
helm install appcircle-server appcircle/appcircle \
  --timeout 1200s \
  -n appcircle \
  -f values.yaml
```

## Update the Appcircle Server

**To update** the Appcircle server chart, run the following Helm command.

```bash
helm upgrade appcircle-server appcircle/appcircle \
  -n appcircle \
  -f values.yaml
```

## Uninstall the Appcircle Server

**To uninstall** the Appcircle server chart, run the following the Helm command.

```bash
helm uninstall appcircle-server -n appcircle
```