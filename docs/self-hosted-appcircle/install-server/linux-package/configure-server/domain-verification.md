---
title: Domain Verification
description: Configure the Appcircle server to bypass domain verification when adding domains to an organization or verify them using DNS records on Docker/Podman architecture.
tags: [security, domain, verify]
sidebar_position: 30
---

import SpacetechExampleInfo from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/_spacetech-example-info.mdx';  
import RestartAppcircleServer from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/_restart-appcircle-server.mdx';  
import DowntimeCaution from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/_appcircle-server-downtime-caution.mdx';  

## Overview

This document explains how to configure your Appcircle server's domain verification option when adding domains as trusted for Appcircle organizations. By skipping the domain verification process, domains will be automatically marked as verified without the need for TXT records.

Please note, this page does not cover the domain verification feature itself. For more detailed information on domain verification, please refer to the [Domain Verification](/account/my-organization/security/domain-verification) documentation.

By default, domain verification is **disabled** on the Appcircle server, meaning domains are automatically considered verified without the need to add a TXT record to your DNS configuration. However, if you change this option, Appcircle will require the addition of a TXT record to validate the domain.

## Configuring the Appcircle Server

To enable or disable domain verification, follow these steps:

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

4. Locate the `keycloak` entry in the configuration file. Add or update the `domainVerification` key with the following settings, depending on your preference.

   :::caution  
   If the `keycloak` entry already exists in your `global.yaml` file, ensure you update the existing key instead of creating a new one.
   :::

   ```yaml
   keycloak:
     domainVerification:
       enabled: true
   ```

   :::note  
   - **`enabled`**: If this variable is set to `true`, it requires the addition of a TXT record for domain verification. If you want to skip TXT record verification and make the domain automatically considered as verified, then this variable should be set to `false`.
   :::

5. After saving the configuration changes, restart your Appcircle server to apply the new settings.

   <RestartAppcircleServer />
