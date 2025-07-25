---
title: Database and Vault Configurations
description: Learn how to configure the Appcircle server Helm chart for production environments
tags: [self-hosted, helm, configuration, kubernetes]
sidebar_position: 20
---

import NeedHelp from '@site/docs/\_need-help.mdx';

By default, the Appcircle Helm chart will deploy all the required services to the Kubernetes cluster for testing purposes. It is recommended that stateful applications, such as databases or object storage, be deployed outside the scope of the Helm chart. This allows you to have better control over their configuration and management.

If you wish to deploy these services within the Helm chart scope, you can use the default configuration provided by the Appcircle Helm chart.

:::caution
The configurations for production readiness should be **done before the first deployment** and **cannot be changed later**. To modify these settings, you should **[uninstall Appcircle](/self-hosted-appcircle/install-server/helm-chart/uninstallation)** and redeploy it.
:::

:::info
The commands below assume you have already created a namespace for Appcircle. If you haven’t yet, you can create and switch to the Appcircle namespace using the following commands:

```bash
# Create the namespace
kubectl create namespace appcircle
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
  -n appcircle \
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

For production environments, it is recommended to set up an external, production-grade MongoDB instance. The recommended version is MongoDB `4.2` or later, with a disk size of 40GB.

:::info
The Appcircle server supports MongoDB versions between `4.2` and `8.0`.

Later versions of the Appcircle server may deprecate `4.x` versions and might remove support for MongoDB EOL (end-of-life) [releases](https://www.mongodb.com/docs/manual/release-notes/).

For this reason, it will be better to choose a recent stable version of MongoDB instead of an EOL release, which can prevent future migration efforts as much as possible.
:::

To use an external MongoDB database, you can follow the steps below:

- Create individual users and passwords for each Appcircle service on the MongoDB instance. Each service should have its own user with distinct credentials to ensure proper access control and security. Below is an example of how to generate a secret with MongoDB connection strings for each service, where each user is assigned specific permissions for its corresponding service.

- Create a secret for the MongoDB connections. While you can choose your own secret name and key, it is recommended to use the format `${releaseName}-mongo-connections` with the multiple keys for each service.

```bash
kubectl create secret generic appcircle-server-mongo-connections \
  -n appcircle \
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

### HashiCorp Vault

By default, the Appcircle chart includes an in-cluster HashiCorp Vault deployment provided by `hashicorp/vault`.

#### Test (or Trial) Environments

For testing purposes, the built-in Vault deployment can be used. In this setup, the storage is kept in Kubernetes.

If the Kubernetes cluster has multiple nodes, it should be configured to guarantee that all Vault replicas reach the same storage for consistency.

#### Production Environments

For production environments, it is recommended to configure an external HashiCorp Vault instance instead of using the built-in deployment. There are two approaches for this:

##### External Vault Service

In this setup, Appcircle connects to an externally managed Vault service. Vault operates independently from Kubernetes, ensuring better availability and scalability. The recommended Vault version is `v1.10.3` with a disk size of at least 20GB.

To use an external Vault instance, follow these steps:

- Create a Kubernetes secret with the name `${releaseName}-vault-seal` containing the Vault access token:

```bash
kubectl create secret generic appcircle-server-vault-seal \
  -n appcircle \
  --from-literal=token=hvs.superSecretVaultKey
```

- Update the `values.yaml` file accordingly:

```yaml
global:
  vault:
    url: "http://10.33.167.78:8082/v1/local/"
vault:
  enabled: false
```

##### External Data Store (e.g., MSSQL)

As an alternative to using an external Vault service, you can configure Vault to use an external database such as MSSQL for storage while keeping the Vault instance inside Kubernetes.

You can find more storage configurations on the official HashiCorp documentation: [HashiCorp Vault Database Capabilities](https://developer.hashicorp.com/vault/docs/v1.10.x/secrets/databases#database-capabilities).

To use MSSQL as the storage backend:

- Ensure that your MSSQL database is accessible and properly configured.

- Update the `values.yaml` file to configure Vault with MSSQL as the backend:

```yaml
# Third party charts
vault:
  server:
    standalone:
      config: |
        ui = true

        listener "tcp" {
          tls_disable = 1
          address = "[::]:8200"
          cluster_address = "[::]:8201"
        }

        storage "mssql" {
          server = "10.10.117.67"
          port = 1433
          username = "sqlserveruser"
          password = "supersecretpassword"
          database = "appcircle-vault"
          table = "vault"
          appname = "vault"
          schema = "dbo"
          connectionTimeout = 30
          logLevel = 0
        }
    dataStorage:
      enabled: false
```

#### Choosing the Right Setup

- If you have an **existing Vault service**, configure Appcircle to connect to it (**recommended for production**).
- If you prefer **running Vault inside Kubernetes** but want persistent storage, use an **external data store (e.g., MSSQL)** as the storage backend.
- For testing (or trial) purposes, the built-in Vault deployment **can be used but is not recommended for production workloads**. Also, it should be configured to guarantee that all Vault replicas reach the same storage for consistency when the cluster has multiple nodes.

<NeedHelp />