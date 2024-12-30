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
You can specify a **particular version** of the Appcircle Helm chart by adding the `--version` flag. For example, to upgrade **Helm chart version** to **`0.2.0`**, use the following command:

```bash
helm upgrade appcircle-server appcircle/appcircle \
  --timeout 1200s \
  -n appcircle \
  -f values.yaml \
  --version 0.2.0
```
:::

<NeedHelp />
