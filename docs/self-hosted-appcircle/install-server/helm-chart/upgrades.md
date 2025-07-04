---
title: Upgrades
description: Learn how to upgrade the Appcircle server Helm chart deployment
tags: [self-hosted, helm, configuration, kubernetes]
sidebar_position: 30
---

import NeedHelp from '@site/docs/\_need-help.mdx';

To **upgrade** the Appcircle server to the **latest** version and apply any configuration changes, you can follow the sections below.

## Updating to the Latest Version

To update the Appcircle server to the latest version, follow these steps:

1. Check the installed Helm chart and Appcircle server version.

```bash
helm list -n appcircle
```

2. Update the Appcircle Helm chart repository.

```bash
helm repo update
```

3. Update the Appcircle server

```bash
helm upgrade appcircle-server appcircle/appcircle \
  --timeout 1200s \
  -n appcircle \
  -f values.yaml
```

By following these steps, you can ensure that your Appcircle server is updated to the latest version with all the latest features.

## Version History

Below is the version history of the self-hosted Appcircle server and the Helm chart. This table helps you track the latest updates and releases since your current version.

:::tip

To keep the below table brief, we are adding only versions for Helm chart upgrades along with the bundled Appcircle server version.

You can also check Docker/Podman architecture [version history](https://docs.appcircle.io/self-hosted-appcircle/install-server/linux-package/update#version-history) to see all released self-hosted versions.
:::

<details>
    <summary>Click to view version history.</summary>

        Since the cloud and self-hosted versions are released asynchronously, the release dates listed in the table may differ from those on the **[Release Notes](https://docs.appcircle.io/release-notes)** page.

        | Appcircle Server Version | Helm Chart Version | Release Date |
        | ------------------------ | ------------------ | ------------ |
        | 3.27.3                   | 0.3.19             | 28/05/2025   |
        | 3.25.1                   | 0.2.8              | 05/02/2025   |
        | 3.23.2                   | 0.1.1              | 23/12/2024   |
        | 3.23.2                   | 0.1.0              | 20/12/2024   |

</details>

## Updating to a Specific Version

You can specify a **specific version** of the Appcircle Helm chart by adding the `--version` flag to the Helm upgrade command.

For instance, to upgrade the **Appcircle Helm chart** to a **specific version** and view the Appcircle server Helm chart versions that are available:

**1.** Check the list of available versions.

```bash
helm search repo appcircle/appcircle -l
```

The output should look like the following:

```txt
NAME                    CHART VERSION   APP VERSION     DESCRIPTION
appcircle/appcircle     0.3.19          3.27.3          Official Appcircle Chart | Enterprise-Grade Ful...
appcircle/appcircle     0.2.8           3.25.1          A Helm chart for Kubernetes                       
appcircle/appcircle     0.1.1           3.23.2          A Helm chart for Kubernetes                       
appcircle/appcircle     0.1.0           3.23.2          A Helm chart for Kubernetes
```

:::caution

### OpenShift Support

`0.2.x` and older versions are deprecated. They are not getting maintenance updates, and they do not support [OpenShift](/self-hosted-appcircle/install-server/helm-chart/installation/openshift) installation.

We strongly recommend you use `0.3.x` or later versions, which are actively maintained and have new features like supporting installation on [OpenShift](/self-hosted-appcircle/install-server/helm-chart/installation/openshift).

:::

**2.** Update the Appcircle Helm chart to a specific version.

```bash
helm upgrade appcircle-server appcircle/appcircle \
  --version 0.2.8 \
  --timeout 1200s \
  -n appcircle \
  -f values.yaml
```

By following these steps, you can upgrade your Appcircle server to a specific version of the Helm chart.

### Why is my Helm chart not updating to the latest version?

If your Helm chart is not updating to the latest version, it could be due to several reasons such as an outdated repository, local cache issues, or network problems. Follow the steps below to troubleshoot and resolve the issue:

1. **Update the Helm Repository:** Make sure your Helm repository is up to date by running the following command:

   ```sh
   helm repo update
   ```

2. **Clear the Local Cache:** Sometimes, clearing the local cache can help in fetching the latest charts.

- For Linux, delete `$HOME/.cache/helm` directory.
  ```sh
  rm -rf "$HOME/.cache/helm"
  ```
- For MacOS, delete `$HOME/Library/Caches/helm` directory.
  ```sh
  rm -rf "$HOME/Library/Caches/helm"
  ```
- For Windows, delete `%TEMP%\helm` folder.

3. **Re-add the Repository:** If the update doesn't resolve the issue, try removing and re-adding the repository:

   ```sh
   helm repo remove appcircle
   helm repo add appcircle https://helm-package.appcircle.io
   helm repo update
   ```

4. **Verify the Index:** After updating, you can check the repository index to ensure that the latest version is available.

   ```sh
   curl -fsSL https://helm-package.appcircle.io/index.yaml | grep -A 5 'appcircle'
   ```

5. **Check for Errors:** Ensure there are no issues with your internet connection or any firewall rules that might be blocking the update.

<NeedHelp />
