---
title: Helm Configuration
description: Learn how to configure the Appcircle server Helm chart
tags: [self-hosted, helm, configuration, kubernetes]
sidebar_position: 1
---

## Secrets for Sensitive Values

To manage sensitive information such as the Appcircle initial user password, SMTP password, SSL certificates, and other secrets, it is recommended to use Kubernetes secrets. This ensures that sensitive data is stored securely and can be accessed by applications running within the cluster in a controlled manner.

:::info
The commands below assume you have already created a namespace for Appcircle. If you haven’t yet, you can create and switch to the Appcircle namespace using the following commands:

```bash
# Create the namespace
kubectl create namespace appcircle

# Switch to the newly created namespace
kubectl config set-context --current --namespace=appcircle
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
  --from-literal=adminPassword=KeycloakAdminPassword1234
```

#### SMTP password

Create a secret with the name `${releaseName}-smtp` containing the `password` key.

```bash
kubectl create secret generic appcircle-server-smtp \
  --from-file=password=/Users/berk/appcircle/helm-values/local-k8s/smtp-password
```

#### SSL certificate

Create a secret with the name `appcircle-tls-wildcard` containing the `tls.crt`, `tls.key` and `ca.crt` keys.

```bash
kubectl create secret generic appcircle-tls-wildcard \
  --from-file=tls.crt='/Users/berk/appcircle/helm-values/local-k8s/fullchain.crt' \
  --from-file=tls.key='/Users/berk/appcircle/helm-values/local-k8s/k8s-deployment.key' \
  --from-file=ca.crt='/Users/berk/appcircle/helm-values/local-k8s/ca.crt' \
  --type=kubernetes.io/tls
```

## Production Readiness

By default, the Appcircle Helm chart will deploy all the required services to the Kubernetes cluster for testing purposes. It is recommended that stateful applications, such as databases or object storage, be deployed outside the scope of the Helm chart. This allows you to have better control over their configuration and management.

If you wish to deploy these services within the Helm chart scope, you can use the default configuration provided by the Appcircle Helm chart.

:::info
The commands below assume you have already created a namespace for Appcircle. If you haven’t yet, you can create and switch to the Appcircle namespace using the following commands:

```bash
# Create the namespace
kubectl create namespace appcircle

# Switch to the newly created namespace
kubectl config set-context --current --namespace=appcircle
```

Make sure to replace `appcircle` with your preferred namespace name if necessary.
:::

### PostgreSQL

The Appcircle chart, by default, includes an in-cluster PostgreSQL deployment provided by `bitnami/PostgreSQL`.

If you are deploying the Appcircle server for testing purposes, you may use the built-in PostgreSQL deployment.

For a production-ready setup, it is recommended to configure an external PostgreSQL instance. The recommended version is PostgreSQL `12.x`, with a disk size of 40GB.

To use an external PostgreSQL database, you can follow the steps below:

- Create a secret for the PostgreSQL password. While you can choose your own secret name and key, it is recommended to use the format `${releaseName}-postgresql-connection` with the key `password`.

```bash
kubectl create secret generic appcircle-server-postgresql-connection \
  --from-literal=password=superSecretPostgresqlPassword
```

- Update the `values.yaml` accordingly.

```yaml
auth:
  auth-keycloak:
    database:
      hostname: "192.168.1.244"
      port: "5432"
      username: "ackeycloak"
      database: "ackeycloak"
      existingSecret: "appcircle-server-postgresql-connection"
      existingSecretKey: "password"
  auth-postgresql:
    enabled: false
```

### MongoDB

By default, the Appcircle chart includes an in-cluster MongoDB deployment provided by `bitnami/mongodb` by default.

If you are deploying the Appcircle server for testing purposes, the built-in MongoDB deployment can be used.

For production environments, it is recommended to set up an external, production-grade MongoDB instance. The recommended version is MongoDB `4.x`, with a disk size of 40GB.

To use an external MongoDB database, you can follow the steps below:

- Create individual users and passwords for each Appcircle service on the MongoDB instance. Each service should have its own user with distinct credentials to ensure proper access control and security. Below is an example of how to generate a secret with MongoDB connection strings for each service, where each user is assigned specific permissions for its corresponding service.

- Create a secret for the MongoDB connections. While you can choose your own secret name and key, it is recommended to use the format `${releaseName}-mongo-connections` with the multiple keys for each service.

```bash
kubectl create secret generic appcircle-server-mongo-connections \
  --from-literal=agentcache='mongodb://agentcachemongo:agentPassword@192.168.1.244:27017?retryWrites=true' \
  --from-literal=build='mongodb://buildmongo:buildPassword@192.168.1.244:27017?retryWrites=true' \
  --from-literal=distribution='mongodb://distributionmongo:distPassword@192.168.1.244:27017?retryWrites=true' \
  --from-literal=license='mongodb://licensemongo:licensePassword@192.168.1.244:27017?retryWrites=true' \
  --from-literal=notification='mongodb://notificationmongo:notificationPassword@192.168.1.244:27017?retryWrites=true' \
  --from-literal=publish='mongodb://publishmongo:publishPassword@192.168.1.244:27017?retryWrites=true' \
  --from-literal=reporting='mongodb://reportmongo:reportPassword@192.168.1.244:27017?retryWrites=true' \
  --from-literal=resign='mongodb://resignmongo:resignPassword@192.168.1.244:27017?retryWrites=true' \
  --from-literal=resource='mongodb://resourcemongo:resourcePassword@192.168.1.244:27017?retryWrites=true' \
  --from-literal=schedulemanager='mongodb://schedulemanagermongo:schedulerPassword@192.168.1.244:27017?retryWrites=true' \
  --from-literal=signingidentity='mongodb://signingmongo:signingPassword@192.168.1.244:27017?retryWrites=true' \
  --from-literal=store='mongodb://storemongo:storePassword@192.168.1.244:27017?retryWrites=true' \
  --from-literal=storesubmit='mongodb://storesubmitmongo:storeSubmitPassword@192.168.1.244:27017?retryWrites=true' \
  --from-literal=webhook='mongodb://webhookmongo:webhookPassword@192.168.1.244:27017?retryWrites=true'
```

- Update the `values.yaml` accordingly.

<details>
    <summary>Click to view example `values.yaml` file.</summary>

```yaml
agentcache:
  mongodb:
    external:
      enabled: true
      existingConnectionSecret: "appcircle-server-mongo-connections"
      existingConnectionSecretKey: "agentcache"
    database: agentCacheStore
build:
  mongodb:
    external:
      enabled: true
      existingConnectionSecret: "appcircle-server-mongo-connections"
      existingConnectionSecretKey: "build"
    database: buildStore
distribution:
  distribution-server:
    mongodb:
      external:
        enabled: true
        existingConnectionSecret: "appcircle-server-mongo-connections"
        existingConnectionSecretKey: "distribution"
      database: distributionStore
  distribution-testeradmin:
    mongodb:
      external:
        enabled: true
        existingConnectionSecret: "appcircle-server-mongo-connections"
        existingConnectionSecretKey: "distribution"
      database: distributionStore
  distribution-testerapi:
    mongodb:
      external:
        enabled: true
        existingConnectionSecret: "appcircle-server-mongo-connections"
        existingConnectionSecretKey: "distribution"
      database: distributionStore
  distribution-testerweb:
    mongodb:
      external:
        enabled: true
        existingConnectionSecret: "appcircle-server-mongo-connections"
        existingConnectionSecretKey: "distribution"
        database: distributionStore
  distribution-web:
    mongodb:
      external:
        enabled: true
        existingConnectionSecret: "appcircle-server-mongo-connections"
        existingConnectionSecretKey: "distribution"
      database: distributionStore
license:
  mongodb:
    external:
      enabled: true
      existingConnectionSecret: "appcircle-server-mongo-connections"
      existingConnectionSecretKey: "license"
    database: licenseStore
notification:
  mongodb:
    external:
      enabled: true
      existingConnectionSecret: "appcircle-server-mongo-connections"
      existingConnectionSecretKey: "notification"
    database: notificationStore
publish:
  mongodb:
    external:
      enabled: true
      existingConnectionSecret: "appcircle-server-mongo-connections"
      existingConnectionSecretKey: "publish"
    database: publishStore
reporting:
  mongodb:
    external:
      enabled: true
      existingConnectionSecret: "appcircle-server-mongo-connections"
      existingConnectionSecretKey: "reporting"
    database: reportingStore
resign:
  mongodb:
    external:
      enabled: true
      existingConnectionSecret: "appcircle-server-mongo-connections"
      existingConnectionSecretKey: "resign"
    database: resignStore
resource:
  mongodb:
    external:
      enabled: true
      existingConnectionSecret: "appcircle-server-mongo-connections"
      existingConnectionSecretKey: "resource"
    database: resourceStore
schedulemanager:
  mongodb:
    external:
      enabled: true
      existingConnectionSecret: "appcircle-server-mongo-connections"
      existingConnectionSecretKey: "schedulemanager"
    database: scheduleManagerStore
signingidentity:
  mongodb:
    external:
      enabled: true
      existingConnectionSecret: "appcircle-server-mongo-connections"
      existingConnectionSecretKey: "signingidentity"
    database: signingIdentityStore
store:
  store-web:
    mongodb:
      external:
        enabled: true
        existingConnectionSecret: "appcircle-server-mongo-connections"
        existingConnectionSecretKey: "store"
      database: enterpriseStore
  store-admin:
    mongodb:
      external:
        enabled: true
        existingConnectionSecret: "appcircle-server-mongo-connections"
        existingConnectionSecretKey: "store"
      database: enterpriseStore
  store-api:
    mongodb:
      external:
        enabled: true
        existingConnectionSecret: "appcircle-server-mongo-connections"
        existingConnectionSecretKey: "store"
      database: enterpriseStore
  store-profile:
    mongodb:
      external:
        enabled: true
        existingConnectionSecret: "appcircle-server-mongo-connections"
        existingConnectionSecretKey: "store"
      database: enterpriseStore
  store-report:
    mongodb:
      external:
        enabled: true
        existingConnectionSecret: "appcircle-server-mongo-connections"
        existingConnectionSecretKey: "store"
      database: enterpriseStore
storesubmit:
  mongodb:
    external:
      enabled: true
      existingConnectionSecret: "appcircle-server-mongo-connections"
      existingConnectionSecretKey: "storesubmit"
    database: storeSubmitStore
webhook:
  mongodb:
    external:
      enabled: true
      existingConnectionSecret: "appcircle-server-mongo-connections"
      existingConnectionSecretKey: "webhook"
    database: webhookStore

mongodb:
  enabled: false
```

</details>

### MinIO

By default, the Appcircle chart includes an in-cluster MinIO deployment provided by `bitnami/minio`.

If you are installing the Appcircle for testing purposes, you may use the built-in MinIO deployment.

For production environments, it is recommended to configure an external MinIO instance. The recommended version is MinIO `2024-03-15` or later, with a disk size of 1TB.

:::info
The recommended disk size for the MinIO instance may vary depending on your usage requirements. It can range from 500GB to 3-4TB.
:::

To use an external MinIO instance, you can follow the steps below:

- Create the following buckets for Appcircle to use on the MinIO instance:

  - appcircle-local-resource-temp
  - appcircle-local-resource-build
  - appcircle-local-resource-distribution
  - appcircle-local-resource-storesubmit
  - appcircle-local-resource-store
  - appcircle-local-resource-agent-cache
  - appcircle-local-resource-backup
  - appcircle-local-resource-publish

- Create a secret with the name `${releaseName}-minio-connection` containing the `accessKey` and `secretKey` keys.

```bash
kubectl create secret generic appcircle-server-minio-connection \
  --from-literal=accessKey='admin' \
  --from-literal=secretKey='superSecretAdminAccessKey'
```

- Update the `values.yaml` accordingly.

```yaml
global:
  minio:
    url: "http://10.33.167.78:9000"
minio:
  enabled: false
```

### HashiCorp Vault

By default, the Appcircle chart includes an in-cluster HashiCorp Vault deployment provided by `hashicorp/vault`.

If you are deploying the appcircle for testing purposes, the built-in Vault deployment can be used.

For production environments, it is recommended to configure an external Hashicorp Vault instance. The recommended version is Vault `v1.10.3`, with a disk size of 20GB.

To use an external Vault instance, you can follow the steps below:

- Create a secret with the name `${releaseName}-vault-seal` containing the `token` key.

```bash
kubectl create secret generic appcircle-server-vault-seal \
  --from-literal=token=hvs.superSecretVaultKey
```

- Update the `values.yaml` accordingly.

```yaml
global:
  vault:
    url: "http://10.33.167.78:8082/v1/local/"
vault:
  enabled: false
```

## Advanced Configuration

If there are any settings you want to configure, open the `values.yaml` with your favorite editor and follow the sections below.

### Persistent Volume Configuration

Appcircle server Helm chart supports configuring storage classes and volume sizes for persistent volume claims (PVCs). If you don't specify any storage class or size, the PVCs will be created using the default storage class of your Kubernetes cluster with the default size. If you want to adjust these settings, you can specify them in the `values.yaml`.

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

2. Run the following command in your **Linux/macOS** terminal to create/update a secret named **`${releaseName}-auth-license`** with the **`credentialJson`** key:

```bash
kubectl create secret generic appcircle-server-auth-license \
  -n appcircle \
  --from-literal=credentialJson=$(cat cred.json | base64) \
  --save-config --dry-run=client -o yaml | kubectl apply -f -
```

### Updating the License

If your organization’s Appcircle server license has been updated and you need to apply the new license, you can upgrade the Appcircle server deployment using Helm:

```bash
helm upgrade appcircle-server appcircle/appcircle-server \
  -n appcircle  \
  -f values.yaml
```

:::info
The license update might take ~30 minutes to take effect on the **UI** due to caches, but it will apply and be ready to use immediately.  
:::
