---
title: Helm SSL Configuration
description: Learn how to configure SSL certificate for HTTPS connections
tags: [self-hosted, helm, configuration, kubernetes]
sidebar_position: 90
sidebar_label: SSL Configuration
---

import NeedHelp from '@site/docs/\_need-help.mdx';

# Overview

This guide provides detailed instructions for configuring an SSL certificate for HTTPS connections in the Appcircle Helm chart. 

By default, the Helm chart is configured for HTTP without an SSL certificate. If you use Appcircle with HTTP, you need to open port 6379 on the ingress controller for Redis the connection.

:::caution
Appcircle must be installed with HTTPS from the initial installation. If you initially installed Appcircle with HTTP, you will need to [uninstall](/self-hosted-appcircle/install-server/helm-chart/uninstallation) it and then reinstall it with HTTPS.
:::

## SSL Certificate Configuration

You have two options for configuring SSL certificates:

1. **Trial Purposes**: Define the SSL certificate directly in the `values.yaml` by following [this section](#define-the-ssl-certificate-in-valuesyaml).
2. **Production**: Create a Kubernetes secret for better security and manageability by following [this section](#create-the-tls-secret).

:::info
When configuring Appcircle with HTTPS, you have the option to use self-signed or untrusted root certificates. However, if you choose to do so, it is essential to add the certificate or the root CA certificate to the trusted certificates. Failure to do this may result in connection errors. For detailed instructions about adding trusted CA certificates, refer to the [Adding Trusted CA Certificates](/self-hosted-appcircle/install-server/helm-chart/configuration/ca-certificates.md) documentation.
:::

### Define the SSL Certificate in `values.yaml`

To configure the SSL certificate, update your `values.yaml` file with the following settings:

```yaml
global:
  urls:
    scheme: https
  tlsWildcard:
    # Public certificate - Fullchain including leaf (app), intermediate and root SSL certificates
    cert: |
      -----BEGIN CERTIFICATE-----
      MIIFzTCCBLWgAwIBAgISBMLn5uQI6Wmzku14xXUbbIbmMA0GCSqGSIb3DQEBCwUA
      ...
      SA==
      -----END CERTIFICATE-----
      -----BEGIN CERTIFICATE-----
      MIIFBjCCAu6gAwIBAgIRAIp9PhPWLzDvI4a9KQdrNPgwDQYJKoZIhvcNAQELBQAw
      ...
      uYkQ4omYCTX5ohy+knMjdOmdH9c7SpqEWBDC86fiNex+O0XOMEZSa8DA
      -----END CERTIFICATE-----
      -----BEGIN CERTIFICATE-----
      MIIFazCCA1OgAwIBAgIRAIIQz7DSQONZRGPgu2OCiwAwDQYJKoZIhvcNAQELBQAw
      ...
      emyPxgcYxn/eR44/KJ4EBs+lVDR3veyJm+kXQ99b21/+jh5Xos1AnX5iItreGCc=
      -----END CERTIFICATE-----
    # Private key for the SSL certificate
    key: |
      -----BEGIN PRIVATE KEY-----
      MIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQC3wS87baGONXjr
      ...
      oUcjMAu/mGJjtn9AS0S7rRa58Q==
      -----END PRIVATE KEY-----
    # Certificate Authority public key - Typically the bottom certificate of the fullchain SSL certificate
    caCert: |
      -----BEGIN CERTIFICATE-----
      MIIFazCCA1OgAwIBAgIRAIIQz7DSQONZRGPgu2OCiwAwDQYJKoZIhvcNAQELBQAw
      ...
      emyPxgcYxn/eR44/KJ4EBs+lVDR3veyJm+kXQ99b21/+jh5Xos1AnX5iItreGCc=
      -----END CERTIFICATE-----
```

#### Update the Certificate in `values.yaml`

To update the SSL certificate used on Appcircle server, perform the following steps to update the Helm chart and restart the required services:

1. Update the SSL certificate defined in the `values.yaml`.

2. Run the Helm upgrade command to apply the changes:

```bash
helm upgrade appcircle-server appcircle/appcircle -n appcircle -f values.yaml
```

3. To restart the Redis service after updating the SSL certificate, you need to first filter and find the names of the stateful sets, as the names might change according to the release name. Use the following command to get the stateful sets:

```bash
kubectl get statefulset -n appcircle | grep webeventredis
````

4. Restart the Redis StatefulSets to apply the changes:

```bash
kubectl rollout restart statefulset/appcircle-server-webeventredis-master -n appcircle
kubectl rollout restart statefulset/appcircle-server-webeventredis-replicas -n appcircle
```

### Create the TLS Secret

Create a secret with the name `appcircle-tls-wildcard` containing the `tls.crt`, `tls.key` and `ca.crt` keys.

:::info
The certificate (`cert`) should be in PEM format and include the full-chain (leaf, intermediate, and root certificates). 

The private key (`key`) should not be password-protected.
:::

:::caution
The name **`appcircle-tls-wildcard`** is **reserved** and **cannot be changed**.
:::

```bash
kubectl create secret generic appcircle-tls-wildcard \
  --from-file=tls.crt='fullchain.crt' \
  --from-file=tls.key='private.key' \
  --from-file=ca.crt='root-ca.crt' \
  --type=kubernetes.io/tls \
  -n appcircle
```

#### Update the Certificate in Secret

To update an existing SSL certificate, use the following commands

1. Update the secret with the new certificate.

```bash
kubectl create secret generic appcircle-tls-wildcard \
  -n appcircle \
  --from-file=tls.crt='fullchain.crt' \
  --from-file=tls.key='private.key' \
  --from-file=ca.crt='root-ca.crt' \
  --type=kubernetes.io/tls \
  --save-config --dry-run=client -o yaml | kubectl apply -f -
```

2. To restart the Redis service after updating the SSL certificate, you need to first filter and find the names of the stateful sets, as the names might change according to the release name. Use the following command to get the stateful sets:

```bash
kubectl get statefulset -n appcircle | grep webeventredis
````

3. Restart the Redis StatefulSets to apply the changes:

```bash
kubectl rollout restart statefulset/appcircle-server-webeventredis-master -n appcircle
kubectl rollout restart statefulset/appcircle-server-webeventredis-replicas -n appcircle
```

## Final Steps

Verify the SSL configuration by accessing the Appcircle server over HTTPS.

<NeedHelp />