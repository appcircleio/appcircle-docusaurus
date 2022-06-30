---
title: Installing Self-Hosted Runner
metaTitle: Installing Self-Hosted Runner
metaDescription: Installing Self-Hosted Runner
sidebar_position: 1
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Prerequisites

The following operating systems are supported for the self-hosted runner.

**Linux**

- Ubuntu 20.04 or later
- Debian 10 or later
  
**MacOS**

- MacOS 11 (Big Sur) or later

The following processor architectures are supported for operating systems.

- `x64` Linux, macOS
- `arm64` macOS only

## Installation

Adding a self-hosted runner requires that you download, register and configure Appcircle runner in your environment.

### 1. Download

@FIXME below dev bucket URLs in download section will replaced with prod cdn bucket.
( https://cdn.appcircle.io < https://storage.googleapis.com/appcircle-dev-common )

Download the latest self-hosted runner package.

<Tabs>
  <TabItem value="osx-x64" label="macOS x64" default>

   ```bash
curl -o appcircle-runner-osx-x64-1.0.0.zip -L https://storage.googleapis.com/appcircle-dev-common/self-hosted/runner/appcircle-runner-osx-x64-1.0.0.zip
```

Extract self-hosted runner package.

   ```bash
unzip -o -u appcircle-runner-osx-x64-1.0.0.zip
```

  </TabItem>
  <TabItem value="osx-arm64" label="macOS arm64">

   ```bash
curl -o appcircle-runner-osx-arm64-1.0.0.zip -L https://storage.googleapis.com/appcircle-dev-common/self-hosted/runner/appcircle-runner-osx-arm64-1.0.0.zip
```

Extract self-hosted runner package.

   ```bash
unzip -o -u appcircle-runner-osx-arm64-1.0.0.zip
```

  </TabItem>

  <TabItem value="linux-x64" label="Linux x64">

   ```bash
curl -o appcircle-runner-linux-x64-1.0.0.zip -L https://storage.googleapis.com/appcircle-dev-common/self-hosted/runner/appcircle-runner-linux-x64-1.0.0.zip
```

Extract self-hosted runner package.

   ```bash
unzip -o -u appcircle-runner-linux-x64-1.0.0.zip
```

  </TabItem>
</Tabs>

Change directory into extracted `appcircle-runner` folder for following steps.

```bash
cd appcircle-runner
```

### 2. Register

Go to your organization's **integration** settings and generate agent access token (AAT).

Using generated token, register self-hosted runner to your organization with desired name and pool.

```bash
./ac-runner register -t ${Access Token} -n ${Runner Name} -p ${Runner Pool}
```

Once you complete this step, you will see new added runner at "Build > Self-hosted Runners" list.

It's `enabled` by default but its state should be `Offline` by now.

### 3. Configure

You need to install some workflow required build tools once before executing any build pipeline.

You can install iOS platform tools, android platform tools or both of them for your requirements.

Below are some example configurations which shows you some sample runner configuration scenarios:

- Install only iOS platform tools with default Xcode (13.4.x)

```bash
./ac-runner install -o ios
```

- Install only iOS platform tools with Xcode versions 12.5.x and 13.3.x

```bash
./ac-runner install -o ios -x 12.5,13.3
```

- Install only android platform tools

```bash
./ac-runner install -o android
```

- Install both android and iOS platform tools with Xcode version 13.2.x

```bash
./ac-runner install -o ios,android -x 13.2
```

### 4. Run Service

Install and start self-hosted runner service.

```bash
./ac-runner service -c install
```

Once you complete this step, its state should be seen as `Online` Self-hosted Runners" list.

### 5. Build App

Now your runner is waiting for build jobs. In order to use your self-hosted runner pool;

- Find your app's build profile in "Build Profiles"
- Click on "Config" to open branch config details
- Select your runner's pool from "Config" tab
- Check also other settings for your runner capabilities
- Save settings and pool configuration
- Start Build :tada:
