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

### kubectl
Install `kubectl` by following [the Kubernetes documentation](https://kubernetes.io/docs/tasks/tools/#kubectl). The version you install must be within one minor release of the version running in your cluster.

### Helm
Install Helm v3.10.3 or later by following the Helm documentation.

### PostgreSQL
By default, the Appcircle chart includes an in-cluster PostgreSQL deployment that is provided by `bitnami/PostgreSQL`. This deployment is for trial purposes only and not recommended for use in production.

You should set up an external, production-ready PostgreSQL instance. Recommended default version is PostgreSQL 16.

### MongoDB
By default, the Appcircle chart includes an in-cluster MongoDB deployment that is provided by `bitnami/mongodb`. This deployment is for trial purposes only and not recommended for use in production.

You should set up an external, production-ready MongoDB instance. Recommended default version is MongoDB `7.0`.

### Create Values Yaml

You can create a `values.yaml` file for helm by entering your settings, which are usually configured by everyone

<YamlGenerator />

Click the `Generate YAML` button to generate some ready to use configuration file. Copy content of the yaml output and save it as a file named  `global.yaml` or anything you wish.

## Deploy using Helm

Once you have all of your configuration options collected, we can get any dependencies and run Helm. In this example, we’ve named our Helm release `appcircle` and we will install the Appcircle server into the `appcircle-ns` namespace.

```bash
helm repo add appcircle https://charts.appcircle.io/ && \
helm repo update && \
helm upgrade --install appcircle appcircle/appcircle \
  --timeout 1200s \
  -n appcircle-ns --create-namespace \
  -f global.yaml
```

Please keep in mind that the release name should be maximum 16 or less character.

Installation time heavily depends on the network speed and process power of the Kubernetes nodes and usually takes 10-15 minutes. 
