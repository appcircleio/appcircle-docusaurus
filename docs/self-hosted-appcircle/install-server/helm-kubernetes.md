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

### Create Values YAML

To configure Helm, you can create a `global.yaml` file by specifying your desired settings, which are commonly used across all deployments.

<YamlGenerator />

Click the `Generate YAML` button to create a ready-to-use configuration file. Once the YAML is generated, copy the content and save it as a file named `global.yaml`.

## Deploy Using Helm

Once you have gathered all the necessary configuration options, you can proceed with installing Helm dependencies and deploying the application. In this example, we will use `appcircle` as Helm release name and install the Appcircle server into the `appcircle-ns` namespace.

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

You can use `watch` command on Linux/MacOS to watch the pod creation process by running:

```bash
watch kubectl get pods -n appcircle-ns
```

If you want to make sure that all containers are ready to use, you can the `kubectl wait` command. The `appcircle` in the command is the Helm release name. So if you have changed the release name in the installation process, change the command according to your release name. 

```bash
kubectl wait --for=condition=ready pod -l app.kubernetes.io/instance=appcircle --timeout 1200s
```

When all the pods are ready, the command will return with success. You are ready to connect to the Appcircle UI and start to discover.


## Sign in to Appcircle

After the installation is finished, you can connect to the Appcircle UI with the URL you configured.

To check the IP address of the domains, you can list the ingresses:

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

You can use the `my` prefixed domain name to access Appcircle dashboard. For example, if you set `global.urls.domainName` to `.appcircle.spacetech.com` then you should use `my.appcircle.spacetech.com` address. 

You should configure your DNS records according to your DNS provider. For a best practice, create a `A` record for the `my.appcircle.spacetech.com` and create `CNAME` records for other domains.

After you see the login page of the Appcircle, you can now use the initial username and password to login to the Appcircle dashboard. You can check the initial username and password from the `global.yaml` file that you have used to install Appcircle server. The values you should look for are under `auth.auth-keycloak.initialUsername` and `auth.auth-keycloak.initialPassword` keys.