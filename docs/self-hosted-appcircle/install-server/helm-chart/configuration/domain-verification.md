---
title: Skipping Domain Verification  
description: Configure Appcircle server to bypass domain verification when adding domains to an organization.  
tags: [security, domain]  
sidebar_position: 95
---

import SpacetechExampleInfo from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/_spacetech-example-info.mdx';  
import RestartAppcircleServer from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/_restart-appcircle-server.mdx';  
import DowntimeCaution from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/_appcircle-server-downtime-caution.mdx';  
import ApplyHelmConfigurationChanges from '@site/docs/self-hosted-appcircle/install-server/helm-chart/configuration/\_apply-helm-configuration-changes.mdx';

## Overview

This document explains how to configure your Appcircle server to bypass domain verification when adding domains as trusted for Appcircle organizations. By skipping the domain verification process, domains will be automatically marked as verified without the need for TXT records.

Please note, this page does not cover the domain verification feature itself. For more detailed information on domain verification, please refer to the [Domain Verification Documentation](/account/my-organization/security/domain-verification/index.md).

By default, domain verification is disabled on the Appcircle server, meaning domains are automatically considered verified without the need to add a TXT record to your DNS configuration. 
However, if you change this option, Appcircle will require the addition of a TXT record to validate the domain.

## Configuring the Appcircle Server Chart

To enable or disable domain verification skipping, follow these steps to configure the Helm chart.

1. **Edit the `values.yaml` of Appcircle Server Helm Chart**  
   Open the `values.yaml` file in a text editor.

   ```bash
   vi values.yaml
   ```

2. **Modify the Keycloak Domain Verification Settings**  
   Locate the `auth` entry in the configuration file. Add or update the `domainVerification` key with the following settings, depending on your preference.

   :::caution  
   If the `keycloak` entry already exists in your `values.yaml` file, ensure you update the existing key instead of creating a new one.  
   :::

   ```yaml
   auth:
      auth-keycloak:
         domainVerification:
            enabled: true
   ```

   :::note  
   - **`enabled: true`**: Requires the addition of a TXT record for domain verification.  
   - **`enabled: false`**: Skips TXT record verification, and the domain is automatically considered verified.  
   :::

3. **Upgrade the Appcircle server release with new `values.yaml`**

   <ApplyHelmConfigurationChanges />