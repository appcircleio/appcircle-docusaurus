---
title: Adding CA Certificates
description: Learn how to configure CA license for the Appcircle Self Hosted server
tags: [self-hosted, helm, configuration, kubernetes]
sidebar_position: 50
---

import NeedHelp from '@site/docs/\_need-help.mdx';
import ApplyHelmConfigurationChanges from '@site/docs/self-hosted-appcircle/install-server/helm-chart/configuration/\_apply-helm-configuration-changes.mdx';

## Adding Trusted CA Certificates to the Appcircle Services

If any services that the Appcircle server needs to connect to, such as your Git provider, use a self-signed SSL/TLS certificate or a certificate issued by an untrusted root CA from your organization, Appcircle will refuse the connection by default.

:::tip
To prevent potential issues with untrusted certificates, it is recommended to add your organization's root certificate from the Certificate Authority (CA) to Appcircle. This ensures that the server can properly validate and trust SSL/TLS certificates issued by your organization’s CA.
:::

To add these certificates as trusted, you need to update the `.global.trustedCerts` key in the `values.yaml` file and import the certificates.

:::info
The `.global` key already exists in your `values.yaml` file. You just need to add the `trustedCerts` key.
:::

The trusted certificate names must conform to the regex pattern `[-._a-zA-Z0-9]+`. It is recommended to use descriptive names for your certificates, such as `spacetech-root` for the root certificate and `spacetech-intermediate` for the intermediate certificate.

Here is an example of how to update the `values.yaml` file:

```yaml
global:
  trustedCerts:
    - name: spacetech-root
      value: |
        -----BEGIN CERTIFICATE-----
        MIIGOTCCBCGgAwIBAgIUU5MNim6S8RDvILFbqSEEFJvqkUkwDQYJKoZIhvcNAQEL
        ...
        JBr5DP/2RTmkKFtc53xoSYXQCmg61T8vMycvrdxWX6eAa8VSDszAtl//QFJIrwY8
        ZmukIMGOIYPWDhsuJA==
        -----END CERTIFICATE-----
    - name: spacetech-intermediate
        -----BEGIN CERTIFICATE-----
        MIIGOTCCBCGgAwIBAgIUU5MNim6S8RDvILFbqSEEFJvqkUkwDQYJKoZIhvcNAQEL
        ...
        JBr5DP/2RTmkKFtc53xoSYXQCmg61T8vMycvrdxWX6eAa8VSDszAtl//QFJIrwY8
        ZmukIMGOIYPWDhsuJA==
        -----END CERTIFICATE-----
```

<ApplyHelmConfigurationChanges />

<NeedHelp />