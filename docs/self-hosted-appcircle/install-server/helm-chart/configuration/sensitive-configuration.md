---
title: Sensitive Values
description: Learn how to configure the sensitive values for Appcircle server Helm chart
tags: [self-hosted, helm, configuration, kubernetes]
sidebar_position: 100
---

import NeedHelp from '@site/docs/\_need-help.mdx';

## Secrets for Sensitive Values

To manage sensitive information such as the Appcircle initial user password, SMTP password, SSL certificates, and other secrets, it is recommended to use Kubernetes secrets. This ensures that sensitive data is stored securely and can be accessed by applications running within the cluster in a controlled manner.

:::caution
The configurations for production readiness should be **done before the first deployment** and **cannot be changed later**. To modify these settings, you should **[uninstall Appcircle](/self-hosted-appcircle/install-server/helm-chart/uninstallation.md)** and redeploy it.
:::

:::info
The commands below assume you have already created a namespace for Appcircle. If you haven’t yet, you can create the Appcircle namespace using the following commands:

```bash
# Create the namespace
kubectl create namespace appcircle
```

Make sure to replace `appcircle` with your preferred namespace name if necessary.
:::

You can follow the steps below to create a secret for each sensitive value.

:::tip
If the `HISTCONTROL` environment variable is set to `ignoreboth`, commands with a leading space character will not be stored in the shell history. This allows you to create secrets safely without storing sensitive information in the shell history.
:::

#### Appcircle initial user password

- Create a secret with the name `${releaseName}-auth-keycloak-passwords` containing the `initialPassword` and `adminPassword` keys.

```bash
kubectl create secret generic appcircle-server-auth-keycloak-passwords \
  --from-literal=initialPassword=Test1234 \
  --from-literal=adminPassword=KeycloakAdminPassword1234 \
  -n appcircle
```

- Remove the `.auth.auth-keycloak.initialPassword` and `.auth.auth-keycloak.adminPassword` keys from the `values.yaml` file if they exist.

#### SMTP password

- Create a secret with the name `${releaseName}-smtp` containing the `password` key.

```bash
kubectl create secret generic appcircle-server-smtp \
  --from-literal=password="superSecretSMTPPassword" \
  -n appcircle
```

- Remove the `.global.mail.smtp.password` key from the `values.yaml` file if it exists.

#### SSL certificate

- Create a secret with the name `appcircle-tls-wildcard` containing the `tls.crt`, `tls.key` and `ca.crt` keys.

```bash
kubectl create secret generic appcircle-tls-wildcard \
  --from-file=tls.crt='fullchain.crt' \
  --from-file=tls.key='private.key' \
  --from-file=ca.crt='root.crt' \
  --type=kubernetes.io/tls \
  -n appcircle
```

- Remove the `.global.tlsWildcard` key from the `values.yaml` file if it exists.

<NeedHelp />