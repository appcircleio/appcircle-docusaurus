---
title: Installing Self-Hosted Runner
metaTitle: Installing Self-Hosted Runner
metaDescription: Installing Self-Hosted Runner
sidebar_position: 1
---

# Prerequisites

todo

## Installation

Adding a self-hosted runner requires that you download, register and configure Appcircle runner in your environment.

### 1. Download

Download the latest self-hosted runner package.

```bash
curl -o appcircle-runner-osx-x64-1.0.0.zip -L https://cdn.appcircle.io/self-hosted/runner/appcircle-runner-osx-x64-1.0.0.zip
```

Extract self-hosted runner package.

```bash
unzip -o -u appcircle-runner-osx-x64-1.0.0.zip
```

Change directory into extracted folder for following steps.

```bash
cd appcircle-runner
```

### 2. Register

Go to your organization's **integration** settings and generate agent access token (AAT).

Using generated token (AAT), register self-hosted runner to your organization with desired name and pool.

```bash
./ac-runner register -t ${AAT} -n ${Runner Name} -p {Runner Pool}
```

### 3. Configure

For build pipeline, you need to install some workflow required build tools.

You can install iOS platform tools, android platform tools or both of them.

```bash
./ac-runner install -o ios -x 13.3
```

### 4. Run Service

Install and start self-hosted runner service.

```bash
./ac-runner service -i
```
