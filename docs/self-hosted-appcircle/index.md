---
title: Overview & Concepts
description: Overview of self-hosted Appcircle and related concepts
tags: [self-hosted, overview, concepts]
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';

Self-hosted Appcircle enables you to use your own systems and infrastructure for all cloud features.

By this way, you can build and test your apps on your choice of architectures. You have full control over the build environment. You can also customize your Appcircle installation with various options.

With the help of self-hosted runners as connected agents, you can have whole Appcircle in your own infrastructure and use all Appcircle features in your private cloud without any limitations.

Self-hosted Appcircle section in here, gives you detailed information about only server-side components installation and other related operations. For details about self-hosted runner concept, see [Self-hosted Runner](/self-hosted-appcircle/self-hosted-runner) section in docs.

:::caution

The only requirement for using self-hosted Appcircle is to be in `enterprise` plan.

See [pricing](https://appcircle.io/pricing) and feature comparison table for details.

:::

## Appcircle Standalone Architecture

We generally recommend a standalone approach by deploying a single node environment for the Appcircle server to reduce the complexity a little further.

When we look at self-hosted Appcircle deployment as a whole, we will see below architecture in execution for a basic installation.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3008-appcircle-topology.png' />

To see the topology diagram in greater detail, click [here](https://cdn.appcircle.io/docs/assets/be-3008-appcircle-topology.png). It will open the diagram in new browser tab.

:::tip
You can see all external network access details on the [Network Access](/self-hosted-appcircle/install-server/linux-package/configure-server/integrations-and-access/network-access) page.
:::

## Appcircle DMZ Architecture

If you plan to use Appcircle DMZ Architecture, the Appcircle DMZ Architecture follows this deployment structure:

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3008-appcircle-dmz-topology.png' />

For more information about the Appcircle DMZ architecture, you can check the [Enterprise App Store and Testing Distribution in DMZ](/self-hosted-appcircle/install-server/linux-package/configure-server/advanced-configuration/store-dist-dmz) document.

## Appcircle Distributed Architecture

In addition to the standalone and DMZ architectures, you can deploy Appcircle using the Helm chart for Kubernetes environments. This method allows for greater scalability and management flexibility.

For detailed instructions on installing and configuring Appcircle using the Helm chart, refer to the [Appcircle Helm Chart Documentation](/self-hosted-appcircle/install-server/helm-chart/installation/kubernetes). This documentation includes steps for setting up Helm, configuring `values.yaml`, and deploying the Appcircle server.

### Advantages

- **High Availability:** Deploying on Kubernetes ensures high availability through automated failover and load balancing.
- **Scalability:** Supports high traffic and large-scale applications with horizontal scaling based on load, ensuring optimal performance.
- **Fault Tolerance:** Kubernetes can handle node failures and automatically reschedule workloads to maintain application uptime.
- **Scalability:** Easily scale your deployment by adding or removing nodes in the Kubernetes cluster.

### Disadvantages

- **Complexity:** Requires familiarity with Kubernetes and Helm, which can be complex to learn and manage.
- **Resource Requirements:** May require more resources compared to a single-node deployment, including more compute power and storage.
- **Operational Overhead:** Maintaining and monitoring a Kubernetes cluster can add operational overhead.
