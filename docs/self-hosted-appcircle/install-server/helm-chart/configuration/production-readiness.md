---
title: Production Readiness
description: Learn how to configure the Appcircle server Helm chart for production environments
tags: [self-hosted, helm, configuration, kubernetes]
sidebar_position: 20
---

import NeedHelp from '@site/docs/\_need-help.mdx';

By default, the Appcircle Helm chart will deploy all the required services to the Kubernetes cluster for testing purposes. It is recommended that stateful applications, such as databases or object storage, be deployed outside the scope of the Helm chart. This allows you to have better control over their configuration and management.

If you wish to deploy these services within the Helm chart scope, you can use the default configuration provided by the Appcircle Helm chart.

:::caution
The configurations for production readiness should be **done before the first deployment** and **cannot be changed later**. To modify these settings, you should **[uninstall Appcircle](/self-hosted-appcircle/install-server/helm-chart/uninstallation.md)** and redeploy it.
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

For production environments, it is recommended to set up an external, production-grade MongoDB instance. The recommended version is MongoDB `4.x`, with a disk size of 40GB.

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
  -n appcircle \
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
  -n appcircle \
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

<NeedHelp />