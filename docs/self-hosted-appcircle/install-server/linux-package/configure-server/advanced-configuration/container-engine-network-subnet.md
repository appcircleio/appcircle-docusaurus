---
title: Configure Container Engine Network Subnet
sidebar_label: Configure Container Engine Network Subnet
description: Configure the Appcircle server to use a specific network subnet for the containers.
tags: [docker, podman, self-hosted, network, subnet]
sidebar_position: 40
---

import SpacetechExampleInfo from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/\_spacetech-example-info.mdx';  
import RestartAppcircleServer from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/\_restart-appcircle-server.mdx';  
import DowntimeCaution from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/\_appcircle-server-downtime-caution.mdx';  
import DowntimeCautionDMZ from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/\_appcircle-server-downtime-caution-dmz.mdx';  
import NeedHelp from '@site/docs/\_need-help.mdx';

## Overview

This document explains how to configure your Appcircle server's and Appcircle DMZ server's network subnet of the containers if the existing subnet is conflicting with other networks or not suitable for your use case.

:::info
This feature is included in the Appcircle server package version **`3.28.0` or later**.
:::

## Configuring the Subnet for Appcircle Server

To configure the network subnet of the containers of the Appcircle server, follow these steps:

<DowntimeCaution />

1. Log in to your Appcircle server via SSH or a remote connection.

2. Change to the directory containing the Appcircle server configuration.

   ```bash
   cd appcircle-server
   ```

3. Open the `global.yaml` file in a text editor.

   <SpacetechExampleInfo />

   ```bash
   vi ./projects/spacetech/global.yaml
   ```

4. Create or update the `networkSettings` entry in the `global.yaml` configuration file.

   :::caution  
   If the `networkSettings` entry already exists in your `global.yaml` file, ensure you update the existing key instead of creating a new one.
   :::

   ```yaml
   networkSettings:
     enabled: true
     networkSubnet: 10.0.0.0/16
   ```

   :::tip
   The `subnet` will be used to configure the network subnet of the Appcircle server containers.
   :::

5. After saving the configuration changes, restart your Appcircle server to apply the new settings.

   <RestartAppcircleServer />

## Configuring the Subnet for Appcircle DMZ Server

To configure the network subnet of the containers of the DMZ server, follow these steps:

<DowntimeCautionDMZ />

1. Log in to your Appcircle server via SSH or a remote connection.

2. Change to the directory containing the Appcircle server configuration.

   ```bash
   cd appcircle-server
   ```

3. Open the `global.yaml` file in a text editor.

   <SpacetechExampleInfo />

   ```bash
   vi ./projects/spacetech/global.yaml
   ```

4. Create or update the `dmzNetworkSettings` entry in the `global.yaml` configuration file.

   :::caution  
   If the `dmzNetworkSettings` entry already exists in your `global.yaml` file, ensure you update the existing key instead of creating a new one.
   :::

   ```yaml
   dmzNetworkSettings:
     enabled: true
     networkSubnet: 10.0.0.0/16
   ```

   :::tip
   The `networkSubnet` will be used to configure the network subnet of the Appcircle DMZ server containers.
   :::

   :::info
   Although the Appcircle server and Appcircle DMZ server have the same subnet configuration as the sample above, they are not required to have the same subnet values or to be configured to custom subnet both.
   :::

5. Apply the new configuration changes.

   ```bash
   ./ac-self-hosted.sh -n spacetech export --dmz
   ```

6. Compress the Appcircle DMZ server directory into a tarball.

   ```bash
   tar -czf dmz.tar.gz -C projects/spacetech/export/dmz/ .
   ```

7. Transfer the `dmz.tar.gz` file to the Appcircle DMZ server with a file transfer protocol like `scp` or `ftp`.

8. Log in to your Appcircle DMZ server via SSH or a remote connection.

9. Change to the directory containing the Appcircle DMZ server configuration.

   ```bash
   cd appcircle-server-dmz
   ```

10. Stop the Appcircle DMZ server.

    ```bash
    ./ac-self-hosted-dmz.sh down
    ```

11. Delete the old Appcircle DMZ server directory.

    ```bash
    cd .. && rm -rf appcircle-dmz-server
    ```

12. Extract the `dmz.tar.gz` file into a new Appcircle DMZ server directory.

    ```bash
    mkdir -p appcircle-server-dmz && \
    tar -xzf dmz.tar.gz -C appcircle-server-dmz
    ```

13. Change directory into the new directory.

    ```bash
    cd appcircle-server-dmz
    ```

14. Reconfigure the Appcircle DMZ server.

    ```bash
    ./ac-self-hosted-dmz.sh -i
    ```

15. Start the Appcircle DMZ server.

    ```bash
    ./ac-self-hosted-dmz.sh up
    ```

16. Check the Appcircle DMZ server status.

    ```bash
    ./ac-self-hosted-dmz.sh check
    ```

## Disabling Custom Subnet Configuration

To allow Docker or Podman to automatically manage subnet configurations for your Appcircle server and/or Appcircle DMZ server containers, you can disable the custom subnet settings.

To disable custom subnet configuration:

1. Follow the steps in either:

   - [Configuring the Subnet for Appcircle Server](#configuring-the-subnet-for-appcircle-server)
   - [Configuring the Subnet for Appcircle DMZ Server](#configuring-the-subnet-for-appcircle-dmz-server)

2. Set the `enabled` parameter to `false` or delete the `networkSettings` or `dmzNetworkSettings` entry in the appropriate configuration section:

   - For the Appcircle server:

     ```yaml
     networkSettings:
       enabled: false
     ```

   - For the Appcircle DMZ server:

     ```yaml
     dmzNetworkSettings:
       enabled: false
     ```

3. After saving the configuration changes, restart the Appcircle server and/or Appcircle DMZ server to apply the new settings by following the steps in the [Configuring the Subnet for Appcircle Server](#configuring-the-subnet-for-appcircle-server) or [Configuring the Subnet for Appcircle DMZ Server](#configuring-the-subnet-for-appcircle-dmz-server) section.

<NeedHelp />
