---
title: Update Runner
metaTitle: Update Runner
metaDescription: Update Runner
sidebar_position: 6
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Update Self-hosted Runner

When a new version of self-hosted runner is released, you can update runner with below steps.

## 1. Update Runner

Download and extract the latest self-hosted runner package.

<Tabs>
  <TabItem value="osx-x64" label="macOS x64" default>

```bash
curl -O -L https://cdn.appcircle.io/self-hosted/runner/appcircle-runner-osx-x64-1.3.11.zip
```

Extract self-hosted runner package.

```bash
unzip -o -u appcircle-runner-osx-x64-1.3.11.zip
```

  </TabItem>
  <TabItem value="osx-arm64" label="macOS arm64">

```bash
curl -O -L https://cdn.appcircle.io/self-hosted/runner/appcircle-runner-osx-arm64-1.3.11.zip
```

Extract self-hosted runner package.

```bash
unzip -o -u appcircle-runner-osx-arm64-1.3.11.zip
```

  </TabItem>

  <TabItem value="linux-x64" label="Linux x64">

```bash
curl -O -L https://cdn.appcircle.io/self-hosted/runner/appcircle-runner-linux-x64-1.3.11.zip
```

Extract self-hosted runner package.

```bash
unzip -o -u appcircle-runner-linux-x64-1.3.11.zip
```

  </TabItem>
</Tabs>

Change directory into extracted `appcircle-runner` folder for following steps.

```bash
cd appcircle-runner
```

## 2. Reconfigure Runner

Self-hosted runner updates may include tool upgrades or introduce new required tools for build pipeline. So we need to rerun configuration step same as before. It will check installed tools quickly, and will update only required tools.

To remember what configuration step was, please refer to [this](../self-hosted-runner/installation.md#3-configure) page.

## 3. Reinstall Service

Although we change self-hosted runner files with above steps, we need to restart runner service in order to activate latest updates.

Some updates may also contain systemd or launchd service updates. For this reason, on every update, reinstalling service is suggested.

Reinstalling service also contains runner restart operations and doesn't affect self-hosted runner logs or produced artifacts.

In order to reinstall systemd or launchd service, first uninstall and then install service with below commands.

```bash
./ac-runner service -c uninstall
```

```bash
./ac-runner service -c install
```

:::info

When you complete update successfully, you will see updated **version** in "Self-hosted Runners" list in [here](../self-hosted-runner/manage-runners.md#monitoring-self-hosted-runners).

```bash
./ac-runner --version
```

:::
