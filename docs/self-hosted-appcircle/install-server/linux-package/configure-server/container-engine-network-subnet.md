---
title: Configure Container Engine Network Subnet
sidebar_label: Configure Container Engine Network Subnet
description: Configure the Appcircle server to use a specific network subnets for the containers.
tags: [docker, self-hosted, network]
sidebar_position: 50
---

import SpacetechExampleInfo from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/_spacetech-example-info.mdx';  
import RestartAppcircleServer from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/_restart-appcircle-server.mdx';  
import DowntimeCaution from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/_appcircle-server-downtime-caution.mdx';  
import DowntimeCautionDMZ from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/_appcircle-server-downtime-caution-dmz.mdx';  
import NeedHelp from '@site/docs/\_need-help.mdx';

## Overview

This document explains how to configure your Appcircle server's network subnets of the containers if the existing subnets are conflicting with other networks or not suitable for the you use case.

:::info
This feature is included in the Appcircle Server package version **`3.28.0` or later**.
:::

## Configuring the Subnets for Appcircle Server

To configure the network subnets of the containers of the Appcircle server, follow these steps:

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
      subnet: 10.0.0.0/16
    ```
    :::tip
    The `subnet` will be used to configure the network subnets of the Appcircle server containers.
    :::

5. After saving the configuration changes, restart your Appcircle server to apply the new settings.

   <RestartAppcircleServer />

## Configuring the Subnets for Appcircle DMZ Server

To configure the network subnets of the containers of the DMZ server, follow these steps:

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
      subnet: 10.0.0.0/16
    ```
    :::tip
    The `subnet` will be used to configure the network subnets of the Appcircle DMZ server containers.
    :::

5. After saving the configuration changes, restart the Appcircle server and Appcircle DMZ server with the new settings.

    :::info
    For more information about updating the Appcircle server and Appcircle DMZ server, please refer to the [Upgrading Appcircle DMZ and Appcircle Server](/self-hosted-appcircle/install-server/linux-package/configure-server/advanced-configuration/store-dist-dmz.md#upgrading-appcircle-dmz-and-appcircle-server) document.
    :::


<NeedHelp />