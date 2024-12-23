---
title: Upgrades
description: Learn how to upgrade the Appcircle server Helm chart deployment
tags: [self-hosted, helm, configuration, kubernetes]
sidebar_position: 30
---

import NeedHelp from '@site/docs/\_need-help.mdx';

To **upgrade** the Appcircle server to the **latest** version and apply any configuration changes, use the following `helm upgrade` command. 

```bash
helm upgrade appcircle-server appcircle/appcircle \
  --timeout 1200s \
  -n appcircle \
  -f values.yaml
```

:::tip
You can specify a **particular version** of the Appcircle Helm chart by adding the `--version` flag. 

For instance, to upgrade **Appcircle Helm chart** to **specific version** and view the Appcircle server Helm chart versions that are available:

- Check the list of available versions.

```bash
helm search repo appcircle
```

- The output should look like the following:

```bash
NAME               	CHART VERSION	APP VERSION	DESCRIPTION                
appcircle/appcircle	0.1.0        	3.23.2     	A Helm chart for Kubernetes
appcircle/appcircle	0.2.0        	3.23.3     	A Helm chart for Kubernetes
```

- Update the Appcircle Helm chart version to `0.2.0`.

```bash
helm upgrade appcircle-server appcircle/appcircle \
  --timeout 1200s \
  -n appcircle \
  -f values.yaml \
  --version 0.2.0
```
:::

<NeedHelp />
