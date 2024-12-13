---
title: Configuration
description: Learn how to configure the Appcircle server Helm chart
tags: [self-hosted, helm, configuration, kubernetes]
sidebar_position: 100
---

import NeedHelp from '@site/docs/\_need-help.mdx';

## Overview

In this section, you will learn how to configure Helm values for Kubernetes installations. These configurations will guide you through setting up various parameters and options to ensure a successful deployment of the Appcircle server. 

By customizing the `values.yaml` file, you can tailor the installation to meet your specific requirements, including external database connections, storage options, and other critical settings. This documentation provides detailed instructions and examples to help you optimize your Kubernetes deployment using Helm.

Some example commands in this documentation are written for Linux and macOS terminals. You can use the appropriate alternatives for other operating systems.

:::info
When using the example `values.yaml` files provided in this document, please ensure that you check your own `values.yaml` keys. Do not add keys multiple times; simply update the existing keys with the appropriate values.
:::

