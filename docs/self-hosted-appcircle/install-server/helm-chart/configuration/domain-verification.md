---
title: Domain Verification
description: Configure the Appcircle server to bypass domain verification when adding domains to an organization or verify them using DNS records on Kubernetes/OpenShift architecture.
tags: [security, domain, verify]
sidebar_position: 95
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

import SpacetechExampleInfo from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/_spacetech-example-info.mdx';  
import RestartAppcircleServer from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/_restart-appcircle-server.mdx';  
import DowntimeCaution from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/_appcircle-server-downtime-caution.mdx';  
import ApplyHelmConfigurationChanges from '@site/docs/self-hosted-appcircle/install-server/helm-chart/configuration/\_apply-helm-configuration-changes.mdx';

## Overview

This document explains how to configure your Appcircle server's domain verification option when adding domains as trusted for Appcircle organizations. By skipping the domain verification process, domains will be automatically marked as verified without the need for TXT records.

Please note, this page does not cover the domain verification feature itself. For more detailed information on domain verification, please refer to the [Domain Verification](/account/my-organization/security/domain-verification) documentation.

By default, domain verification is **disabled** on the Appcircle server, meaning domains are automatically considered verified without the need to add a TXT record to your DNS configuration. However, if you change this option, Appcircle will require the addition of a TXT record to validate the domain.

## Configuring the Appcircle Server Chart

To enable or disable domain verification, follow these steps:

1. Open the `values.yaml` file in a text editor.

   ```bash
   vi values.yaml
   ```

2. Locate the `auth` entry in the configuration file. Add or update the `domainVerification` key with the following settings, depending on your preference.

   :::caution  
   If the `auth-keycloak` entry already exists in your `values.yaml` file, ensure you update the existing key instead of creating a new one.  
   :::

   ```yaml
   auth:
     auth-keycloak:
       domainVerification:
         enabled: true
   ```

   :::note  
   - **`enabled`**: If this variable is set to `true`, it requires the addition of a TXT record for domain verification. If you want to skip TXT record verification and make the domain automatically considered as verified, then this variable should be set to `false`.
   :::

3. Upgrade the Appcircle server release with new `values.yaml` settings.

   <ApplyHelmConfigurationChanges />

4. Restart the Keycloak stateful set to apply new changes.

<Tabs>
  <TabItem value="kubernetes" label="Kubernetes" default>
   ```bash
   kubectl rollout restart statefulset appcircle-server-auth-keycloak -n appcircle
   ```
  </TabItem>
  <TabItem value="openshift" label="OpenShift">
   ```bash
   oc rollout restart statefulset appcircle-server-auth-keycloak -n appcircle
   ```
  </TabItem>
</Tabs>

:::caution
Restarting the Keycloak stateful set affects active sessions and causes a redirection to the login page for the end-users to log in again. After re-login, the users can go on with their operations as usual from where they left off.
:::
