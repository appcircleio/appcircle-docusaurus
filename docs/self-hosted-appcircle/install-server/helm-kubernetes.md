---
title: Helm for Kubernetes
description: Learn how to install and configure self-hosted Appcircle server with Helm to Kubernetes
tags: [self-hosted, helm, installation, configuration]
sidebar_position: 6
---

import YamlGenerator from '@site/src/components/YamlGenerator';

## Overview

To install a cloud-native version of Appcircle, use the Appcircle Helm chart. This chart contains all the required components to get started and can scale to large deployments.

:::caution
The default Helm chart configuration is not intended for production. The default values create an implementation where all Appcircle services are deployed in the cluster, which is not suitable for production workloads.
:::

For a production deployment, you should have strong working knowledge of Kubernetes. This method of deployment has different management, observability, and concepts than traditional deployments.

## Prerequisites

### Kubernetes Cluster

To install the Appcircle server using Helm, a Kubernetes cluster with nodes based on the `x86_64` architecture is required. The cluster must meet the following hardware specifications:

**Minimum hardware requirements for an enterprise installation:**

- 500 GB SSD
- 8 CPUs
- 16 GB RAM

**Recommended hardware requirements for production environments:**

- 1 TB SSD
- 32 CPUs
- 64 GB RAM

### kubectl

Install `kubectl` by following the instructions provided in [the Kubernetes documentation](https://kubernetes.io/docs/tasks/tools/#kubectl). Ensure that the installed version is within one minor release of the version running on your cluster.

### Helm

Install Helm version 3.11.0 or later by following the instructions in [the Helm documentation](https://helm.sh/docs/intro/install/).

### PostgreSQL

The Appcircle chart, by default, includes an in-cluster PostgreSQL deployment provided by `bitnami/PostgreSQL`. This deployment is intended for testing and evaluation purposes only, and is not recommended for production environments.

For a production-ready setup, it is essential to configure an external PostgreSQL instance. The recommended version is PostgreSQL 16.

If you are deploying the Appcircle server for testing purposes, you may use the built-in PostgreSQL deployment.

### MongoDB

Similarly, the Appcircle chart includes an in-cluster MongoDB deployment provided by `bitnami/mongodb` by default. This is designed for trial use and is not suitable for production workloads.

To ensure optimal performance and reliability in a production environment, it is recommended to set up an external, production-grade MongoDB instance. The recommended version is MongoDB 7.0.

If you are deploying the Appcircle server for testing purposes, the built-in MongoDB deployment can be used.

### Create Values YAML

To configure Helm, you can create a `global.yaml` file by specifying your desired settings, which are commonly used across all deployments.

<YamlGenerator />

Click the `Generate YAML` button to create a ready-to-use configuration file. Once the YAML is generated, copy the content and save it as a file named `global.yaml`.

## Deploy Using Helm

Once you have gathered all the necessary configuration options, you can proceed with installing Helm dependencies and deploying the application. In this example, we will use the Helm release name `appcircle` and install the Appcircle server into the `appcircle-ns` namespace.

```bash
helm repo add appcircle https://charts.appcircle.io/ && \
helm repo update && \
helm upgrade --install appcircle appcircle/appcircle \
  --timeout 1200s \
  -n appcircle-ns --create-namespace \
  -f global.yaml
```

Please note that the release name must be 16 characters or fewer.

The installation process duration depends on factors such as network speed and the processing power of your Kubernetes nodes. Typically, the installation may take between 10 to 15 minutes.