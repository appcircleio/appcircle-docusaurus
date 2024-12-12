---
title: Advanced Configuration
description: Learn how to fully configure the Appcircle server Helm chart
tags: [self-hosted, helm, configuration, kubernetes]
sidebar_position: 100
---

import NeedHelp from '@site/docs/\_need-help.mdx';

For advanced configuration options, open the `values.yaml` file with your preferred text editor and modify the settings as needed.

Once you have updated the `values.yaml` file, please proceed to the [Upgrade Appcircle Server](/self-hosted-appcircle/install-server/helm-chart/upgrades.md) section to apply the changes.

### Persistent Volume Configuration

Appcircle server Helm chart supports configuring storage classes and volume sizes for persistent volume claims (PVCs). If you don't specify any storage class or size, the PVCs will be created using the default storage class of your Kubernetes cluster with the default size. If you want to adjust these settings, you can specify them in the `values.yaml`.

:::caution
The configurations for storage classes should be **done before the first deployment** and **cannot be changed later**. To modify these settings, you should **[uninstall Appcircle](/self-hosted-appcircle/install-server/helm-chart/uninstallation.md)** and redeploy it.

Additionally, some storage classes do not support **expanding volumes**. You should verify the capabilities of your own storage class. If volume expansion is needed, **manual operations**, such as moving data from the old volume to a new one, may be required.
:::

You can configure the `values.yaml` like in the example below. The storage values given in the example are recommended values for production usage.

```yaml
auth:
  auth-postgresql:
    primary:
      persistence:
        size: 40Gi
        storageClass: nfs-client
mongodb:
  persistence:
    size: 3Gi
    storageClass: nfs-client
kafka:
  controller:
    persistence:
      size: 8Gi
      storageClass: nfs-client
minio:
  persistence:
    storageClass: nfs-client
    size: 1Ti
vault:
  server:
    dataStorage:
      size: 20Gi
      storageClass: nfs-client
webeventredis:
  master:
    persistence:
      size: 2Gi
      storageClass: nfs-client
  replica:
    persistence:
      size: 2Gi
      storageClass: nfs-client
```

### Adding Trusted CA Certificates to the Appcircle Services

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

### Configure Max Body Size

In Appcircle, there are scenarios where the client upload size might exceed the default limit of `4096MB` for the Nginx Ingress controller for a single request body size. To accommodate larger file uploads or if you wish to adjust this setting according to your needs, you can configure the maximum allowed body size in your `values.yaml` file.

```yaml
# For APK, IPA, build artifact uploads from browsers and Appcircle runners
apigateway:
  ingress:
    annotations:
      # For Nginx Ingress Controller
      nginx.ingress.kubernetes.io/proxy-body-size: 1024m
      # For HAProxy Kubernetes Ingress Controller
      haproxy.ingress.kubernetes.io/body-size: 1024m

# For build cache uploads from Appcircle runners
resource:
  ingress:
    annotations:
      # For Nginx Ingress Controller
      nginx.ingress.kubernetes.io/proxy-body-size: 1024m
      # For HAProxy Kubernetes Ingress Controller
      haproxy.ingress.kubernetes.io/body-size: 1024m
```

### Git Providers

With default installation, self-hosted Appcircle comes with the connection options below:

- Bitbucket
- Azure
- GitLab
- Connect via SSH
- Connect via URL

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2031-git-providers-v2.png' />

If you want to enable or disable any of these providers, you can do so by updating your `values.yaml` file.

In the example below, there are enabled git providers list with comma separated:

```yaml
web:
  web-app:
    selfHostedGitProviders:
      - "bitbucketServer"
      - "azureDevopsServer"
      - "gitlabSelfHosted"
      - "ssh"
      - "publicRepository"
```

You can delete the providers you do not need by removing them from `selfHostedGitProviders` list above.

### Customize Enterprise App Store

You can change the Enterprise App Store tab title according to the language selected on the self-hosted Appcircle server.

For example, you can set a title for **TR** and a different title for **EN** language selection on browsers.

```yaml
store:
  store-web:
    extraEnvVars:
      - name: TR_STORE_TITLE
        value: "Uygulama Mağazası"
      - name: EN_STORE_TITLE
        value: "App Store"
```

### User Lookup Decision Strategy

The LDAP (Lightweight Directory Access Protocol) user lookup decision strategy is a crucial aspect of user authentication in applications that utilize LDAP for user management.

When Appcircle receives a user login request from the Enterprise App Store or Testing Distribution, it needs to determine which LDAP configuration to use for the user lookup and authentication process.

In scenarios where a user exists in multiple LDAP configurations, a decision must be made on which configuration to use for authentication.

This documentation provides insights into the LDAP user lookup decision strategy and how it can be configured to handle scenarios where a user has multiple usernames and passwords across different LDAP configurations.

To configure LDAP lookup decision settings, you can edit the `values.yaml` file and add the following settings under `auth`:

```yaml
auth:
  auth-keycloak:
    userLookupDecisionStrategy: decisive
```

The `userLookupDecisionStrategy` variable can have three options: `affirmative` , `decisive` or `tolerant`.

If you don't define it or it has an unknown value, it is assumed to be `decisive` by default.

- `Affirmative`

When `userLookupDecisionStrategy` is set to "affirmative", the LDAP authentication process will check all LDAP settings, even if the user is found on a particular LDAP configuration. This means that if a user has multiple accounts on different LDAP configurations with different passwords, they will be able to login successfully. The authentication system will search across all LDAP configurations to find a matching username or email and validate the user's password, allowing the user to access the system.

- `Decisive`

On the other hand, when `userLookupDecisionStrategy` is set to "decisive", the LDAP authentication process will check a specific LDAP configuration for the user's username or email. If the authentication system finds the username on a particular LDAP, it will verify the user's password only on that specific LDAP configuration. If the provided password is incorrect, the authentication system will not check other LDAP configurations and will immediately return invalid credentials, denying access to the user.

- `Tolerant`

When `userLookupDecisionStrategy` is set to "tolerant", similar to the "affirmative" strategy, it retrieves the list of LDAP providers where the user is found and checks the password sequentially. If the password is correct, the process ends. If it is incorrect, the search continues until the last LDAP provider. Unlike "affirmative", if an LDAP provider is unreachable or an error occurs, the process continues, and the faulty provider is ignored.

### LDAP Brute Force Protection

To configure LDAP brute force protection, you can edit the `values.yaml` file and add the following settings under `auth`:

```yaml
auth:
  auth-keycloak:
    bruteForce:
      distribution:
        maxFailureCount: "5"
        maxLockDuration: "600"
      store:
        maxFailureCount: "5"
        maxLockDuration: "600"
```

### Custom Enterprise App Store Domain

To configure a custom domain for the Enterprise App Store of your organization, you can refer to the [Portal Settings](https://docs.appcircle.io/enterprise-app-store/portal-settings#custom-domain) of the Enterprise App Store documentation.

<!---
### Custom Testing Distribution Domain

TODO: Fill the post jobs after enabling the custom store domain.
-->
### Increase the Replica Counts

With the default Helm values, the Appcircle server services being deployed with one replica. If you want to increase this number for high availability, you can do so by updating your `values.yaml` file:

:::caution
Some keys might already exists in your `values.yaml` file, make sure to update the existing keys instead of adding new ones.
:::

```yaml
agentcache:
  replicaCount: 3
auth:
  auth-keycloak:
    replicas: 3
apigateway:
  replicaCount: 2
appparser:
  replicaCount: 3
build:
  replicaCount: 3
distribution:
  distribution-server:
    replicaCount: 3
  distribution-testeradmin:
    replicaCount: 3
  distribution-testerapi:
    replicaCount: 3
  distribution-testerweb:
    replicaCount: 3
  distribution-web:
    replicaCount: 3
license:
  replicaCount: 3
notification:
  replicaCount: 3
otp:
  replicaCount: 3
publish:
  replicaCount: 3
reporting:
  replicaCount: 3
resign:
  replicaCount: 3
resource:
  replicaCount: 3
schedulemanager:
  replicaCount: 3
signingidentity:
  replicaCount: 3
store:
  store-web:
    replicaCount: 3
  store-admin:
    replicaCount: 3
  store-api:
    replicaCount: 3
  store-profile:
    replicaCount: 3
  store-report:
    replicaCount: 3
storesubmit:
  replicaCount: 3
taskserver:
  replicaCount: 3
web:
  web-app:
    replicaCount: 3
  web-event:
    replicaCount: 3
webhook:
  replicaCount: 3
```

## Appcircle License

### Creating a Secret for License Authentication

To authenticate the Appcircle license, you need to create a secret that contains the `cred.json` file you received from Appcircle.

1. Save the `cred.json` file to your local system.

2. Create/update the secret named **`${releaseName}-auth-license`** with the **`credentialJson`** key:

```bash
kubectl create secret generic appcircle-server-auth-license \
  -n appcircle \
  --from-literal=credentialJson=$(cat cred.json | base64) \
  --save-config --dry-run=client -o yaml | kubectl apply -f -
```

### Updating the License

If your organization’s Appcircle server license has been updated and you need to apply the new license, you can upgrade the Appcircle server deployment using Helm:

```bash
helm upgrade appcircle-server appcircle/appcircle \
  -n appcircle  \
  -f values.yaml
```

:::info
The license update might take ~30 minutes to take effect on the **UI** due to caches, but it will apply and be ready to use immediately.  
:::

<NeedHelp />