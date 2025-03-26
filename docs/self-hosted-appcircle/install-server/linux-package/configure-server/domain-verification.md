---
title: Skipping Domain Verification  
description: Configure Appcircle server to bypass domain verification when adding domains to an organization.  
tags: [security, domain, verification]  
sidebar_position: 30  
---

import SpacetechExampleInfo from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/_spacetech-example-info.mdx';  
import RestartAppcircleServer from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/_restart-appcircle-server.mdx';  
import DowntimeCaution from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/_appcircle-server-downtime-caution.mdx';  

## Overview

This document explains how to configure your Appcircle server to bypass domain verification when adding domains as trusted for Appcircle organizations. By skipping the domain verification process, domains will be automatically marked as verified without the need for TXT records.

Please note, this page does not cover the domain verification feature itself. For more detailed information on domain verification, please refer to the [Domain Verification Documentation](/docs/account/my-organization/security/domain-verification/index.md).

By default, domain verification is disabled on the Appcircle server, meaning domains are automatically considered verified without the need to add a TXT record to your DNS configuration. 
However, if you change this option, Appcircle will require the addition of a TXT record to validate the domain.

## Configuring the Appcircle Server

To enable or disable domain verification skipping, follow these steps:

<DowntimeCaution />

1. **Access the Appcircle Server**  
   Log in to your Appcircle server via SSH or a remote connection.

2. **Navigate to the Appcircle Server Directory**  
   Change to the directory containing the Appcircle server configuration.

   ```bash
   cd appcircle-server
   ```

3. **Edit the Global Configuration File**  
   Open the `global.yaml` file in a text editor.

   <SpacetechExampleInfo />

   ```bash
   vi ./projects/spacetech/global.yaml
   ```

4. **Modify the Keycloak Domain Verification Settings**  
   Locate the `keycloak` entry in the configuration file. Add or update the `domainVerification` key with the following settings, depending on your preference.

   :::caution  
   If the `keycloak` entry already exists in your `values.yaml` file, ensure you update the existing key instead of creating a new one.  
   :::

   ```yaml
   keycloak:
     domainVerification:
       enabled: false
   ```

   :::note  
   - **`enabled: true`**: Requires the addition of a TXT record for domain verification.  
   - **`enabled: false`**: Skips TXT record verification, and the domain is automatically considered verified.  
   :::

5. **Restart the Appcircle Server**  
   After saving the configuration changes, restart your Appcircle server to apply the new settings.

   <RestartAppcircleServer />
