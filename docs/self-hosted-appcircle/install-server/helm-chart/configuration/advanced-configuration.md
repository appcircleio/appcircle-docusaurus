---
title: Advanced Configuration
description: Learn how to fully configure the Appcircle server Helm chart
tags: [self-hosted, helm, configuration, kubernetes]
sidebar_position: 100
---

import NeedHelp from '@site/docs/\_need-help.mdx';

For advanced configuration options, open the `values.yaml` file with your preferred text editor and modify the settings as needed.

Once you have updated the `values.yaml` file, please proceed to the [Upgrade Appcircle Server](/self-hosted-appcircle/install-server/helm-chart/upgrades.md) section to apply the changes.


<!---
### Custom Testing Distribution Domain

TODO: Fill the post jobs after enabling the custom store domain.
-->

## Increase the Replica Counts

With the default Helm values, the Appcircle server services being deployed with one replica. If you want to increase this number for high availability, you can do so by updating your `values.yaml` file:

:::caution
Some keys might already exists in your `values.yaml` file, make sure to update the existing keys instead of adding new ones.
:::

```yaml
agentcache:
  replicaCount: 2
auth:
  auth-keycloak:
    replicas: 2
apigateway:
  replicaCount: 2
appparser:
  replicaCount: 2
build:
  replicaCount: 2
distribution:
  distribution-server:
    replicaCount: 2
  distribution-testeradmin:
    replicaCount: 2
  distribution-testerapi:
    replicaCount: 2
  distribution-testerweb:
    replicaCount: 2
  distribution-web:
    replicaCount: 2
license:
  replicaCount: 2
notification:
  replicaCount: 2
otp:
  replicaCount: 2
publish:
  replicaCount: 2
reporting:
  replicaCount: 2
resign:
  replicaCount: 2
resource:
  replicaCount: 2
schedulemanager:
  replicaCount: 2
signingidentity:
  replicaCount: 2
store:
  store-web:
    replicaCount: 2
  store-admin:
    replicaCount: 2
  store-api:
    replicaCount: 2
  store-profile:
    replicaCount: 2
  store-report:
    replicaCount: 2
storesubmit:
  replicaCount: 2
taskserver:
  replicaCount: 2
web:
  web-app:
    replicaCount: 2
  web-event:
    replicaCount: 2
webhook:
  replicaCount: 2
```

## Values Table

Users can view all available parameters of the Appcircle server Helm chart.

### Parameters

#### Global Parameters

Example usage:

```yaml
# Example usage:
global:
  imageRegistry: "myregistry.com"
```

| Key                                                 | Type               | Default Value | Description                                 |
| --------------------------------------------------- | ------------------ | ------------- | ------------------------------------------- |
| global                                              | object             | -             | Application global configuration            |
| global.appEnvironment                               | string             | Development   | Global app environment                      |
| global.appVersion                                   | string             | -             | Global app version                          |
| global.isSelfHosted                                 | boolean            | True          | Global Is self-hosted setup                 |
| global.imageRegistry                                | string             |               | Global Docker image registry                |
| global.imageRepositoryPath                          | string             |               | Global Docker image repository path         |
| global.imageTag                                     | string             |               | Global Docker image tag                     |
| global.imagePullSecrets                             | array              | []            | Image pull secrets                          |
| global.ingressClassName                             | string             | appcircle     | Global ingress class name for all ingresses |
| global.defaultStorageClass                          | string             | -             |                                             |
| global.urls                                         | object             | -             | Global URLs configuration                   |
| global.urls.domainName                              | string             | -             | Domain name for the app (.example.com)      |
| global.urls.scheme                                  | string             | http          | URL scheme                                  |
| global.urls.prefixSubdomain                         | ['string', 'null'] | -             | Prefix subdomain for the app                |
| global.urls.auth                                    | object             | -             |                                             |
| global.urls.auth.subdomain                          | string             | auth          | Auth subdomain                              |
| global.urls.privateApi                              | object             | -             |                                             |
| global.urls.privateApi.subdomain                    | string             | api           | Private API subdomain                       |
| global.urls.webApp                                  | object             | -             |                                             |
| global.urls.webApp.subdomain                        | string             | my            | Web app subdomain                           |
| global.urls.webEvent                                | object             | -             |                                             |
| global.urls.webEvent.subdomain                      | string             | hook          | Web event subdomain                         |
| global.urls.distributionTesterWeb                   | object             | -             |                                             |
| global.urls.distributionTesterWeb.subdomain         | string             | dist          | Distribution tester web subdomain           |
| global.urls.store                                   | object             | -             |                                             |
| global.urls.store.subdomain                         | string             | store         | Store subdomain                             |
| global.urls.webEventRedis                           | object             | -             |                                             |
| global.urls.webEventRedis.subdomain                 | string             | kvs           | Web event redis subdomain                   |
| global.urls.resource                                | object             | -             |                                             |
| global.urls.resource.subdomain                      | string             | resource      | Resource subdomain                          |
| global.keycloak                                     | object             | -             |                                             |
| global.keycloak.clients                             | object             | -             |                                             |
| global.keycloak.clients.appcircleWeb                | object             | -             |                                             |
| global.keycloak.clients.appcircleWeb.id             | string             | -             |                                             |
| global.keycloak.clients.reportingServer             | object             | -             |                                             |
| global.keycloak.clients.reportingServer.id          | string             | -             |                                             |
| global.keycloak.clients.licenseServer               | object             | -             |                                             |
| global.keycloak.clients.licenseServer.id            | string             | -             |                                             |
| global.keycloak.clients.storeServer                 | object             | -             |                                             |
| global.keycloak.clients.storeServer.id              | string             | -             |                                             |
| global.keycloak.clients.storeWeb                    | object             | -             |                                             |
| global.keycloak.clients.storeWeb.id                 | string             | -             |                                             |
| global.keycloak.clients.storeAdminService           | object             | -             |                                             |
| global.keycloak.clients.storeAdminService.id        | string             | -             |                                             |
| global.keycloak.clients.distributionServer          | object             | -             |                                             |
| global.keycloak.clients.distributionServer.id       | string             | -             |                                             |
| global.keycloak.clients.distributionAdminService    | object             | -             |                                             |
| global.keycloak.clients.distributionAdminService.id | string             | -             |                                             |
| global.keycloak.clients.distributionTesterWeb       | object             | -             |                                             |
| global.keycloak.clients.distributionTesterWeb.id    | string             | -             |                                             |
| global.keycloak.clients.publishServer               | object             | -             |                                             |
| global.keycloak.clients.publishServer.id            | string             | -             |                                             |
| global.keycloak.clients.buildServer                 | object             | -             |                                             |
| global.keycloak.clients.buildServer.id              | string             | -             |                                             |
| global.mail                                         | object             | -             | Global Mail configuration                   |
| global.mail.provider                                | string             | -             |                                             |
| global.mail.smtp                                    | object             | -             | SMTP configuration                          |
| global.mail.smtp.host                               | string             | -             |                                             |
| global.mail.smtp.username                           | string             | -             |                                             |
| global.mail.smtp.from                               | string             | -             |                                             |
| global.mail.smtp.fromDisplayName                    | string             | -             |                                             |
| global.mail.smtp.port                               | string             | -             |                                             |
| global.mail.smtp.password                           | string             | -             |                                             |
| global.mail.smtp.ssl                                | string             | -             |                                             |
| global.mail.smtp.auth                               | string             | -             |                                             |
| global.mail.smtp.starttls                           | string             | -             |                                             |
| global.tlsWildcard                                  | object             | -             | Global TLS wildcard configuration           |
| global.tlsWildcard.cert                             | string             | -             |                                             |
| global.tlsWildcard.caCert                           | string             | -             |                                             |
| global.tlsWildcard.key                              | string             | -             |                                             |
| global.trustedCerts                                 | array              | []            | Global Trusted certificates                 |
| global.minio                                        | object             | -             | Global Minio configuration                  |
| global.minio.url                                    | string             | -             | External Minio URL                          |
| global.minio.region                                 | string             | -             |                                             |
| global.minio.bucketPrefix                           | string             | -             |                                             |
| global.minio.buckets                                | string             | -             |                                             |
| global.containerRegistrySecret                      | string             | -             | Global container registry secret            |
| global.redis                                        | object             | -             | Global Redis configuration                  |
| global.redis.enabled                                | boolean            | -             | Enable common redis for all modules         |
| global.redis.everyModule                            | boolean            | -             | Enable redis instances for every module     |
| global.vault                                        | object             | -             | Global Vault configuration                  |
| global.vault.url                                    | string             | -             | External Vault URL                          |

#### General Parameters

```yaml
# Example usage:
redis:
  architecture: "standalone"
```

| Key                                                                           | Type    | Default Value | Description                 |
| ----------------------------------------------------------------------------- | ------- | ------------- | --------------------------- |
| redis.architecture                                                            | string  | -             |                             |
| redis.auth                                                                    | object  | -             |                             |
| redis.auth.sentinel                                                           | boolean | -             |                             |
| redis.auth.existingSecret                                                     | string  | -             |                             |
| redis.auth.existingSecretPasswordKey                                          | string  | -             |                             |
| redis.image                                                                   | object  | -             |                             |
| redis.image.name                                                              | string  | -             |                             |
| redis.master                                                                  | object  | -             |                             |
| redis.master.persistence                                                      | object  | -             |                             |
| redis.master.persistence.enabled                                              | boolean | -             |                             |
| redis.replica                                                                 | object  | -             |                             |
| redis.replica.persistence                                                     | object  | -             |                             |
| redis.replica.persistence.enabled                                             | boolean | -             |                             |
| redis.replica.replicaCount                                                    | integer | -             |                             |
| redis.replica.service                                                         | object  | -             |                             |
| redis.replica.service.resourcesPreset                                         | string  | -             |                             |
| vault                                                                         | object  | -             | Vault configuration         |
| vault.injector                                                                | object  | -             |                             |
| vault.injector.enabled                                                        | boolean | -             |                             |
| vault.server                                                                  | object  | -             |                             |
| vault.server.dataStorage                                                      | object  | -             |                             |
| vault.server.dataStorage.size                                                 | string  | -             |                             |
| vault.server.authDelegator                                                    | object  | -             |                             |
| vault.server.authDelegator.enabled                                            | boolean | -             |                             |
| vault.server.image                                                            | object  | -             |                             |
| vault.server.image.repository                                                 | string  | -             |                             |
| vault.server.image.tag                                                        | string  | -             |                             |
| vault.server.standalone                                                       | object  | -             |                             |
| vault.server.standalone.enabled                                               | boolean | -             |                             |
| vault.server.standalone.config                                                | string  | -             |                             |
| vault.server.extraVolumes                                                     | array   | -             |                             |
| vault.server.postStart                                                        | array   | -             |                             |
| vault.ui                                                                      | object  | -             |                             |
| vault.ui.enabled                                                              | boolean | -             |                             |
| vault.ui.externalPort                                                         | integer | -             |                             |
| kafka                                                                         | object  | -             | Kafka configuration         |
| kafka.image                                                                   | object  | -             |                             |
| kafka.image.name                                                              | string  | -             |                             |
| kafka.heapOpts                                                                | string  | -             |                             |
| kafka.controller                                                              | object  | -             |                             |
| kafka.controller.replicaCount                                                 | integer | -             |                             |
| kafka.controller.resourcesPreset                                              | string  | -             |                             |
| kafka.controller.persistence                                                  | object  | -             |                             |
| kafka.controller.persistence.enabled                                          | boolean | -             |                             |
| kafka.controller.persistence.size                                             | string  | -             |                             |
| kafka.listeners                                                               | object  | -             |                             |
| kafka.listeners.client                                                        | object  | -             |                             |
| kafka.listeners.client.protocol                                               | string  | -             |                             |
| kafka.listeners.controller                                                    | object  | -             |                             |
| kafka.listeners.controller.protocol                                           | string  | -             |                             |
| kafka.listeners.interbroker                                                   | object  | -             |                             |
| kafka.listeners.interbroker.protocol                                          | string  | -             |                             |
| kafka.metrics                                                                 | object  | -             |                             |
| kafka.metrics.kafka                                                           | object  | -             |                             |
| kafka.metrics.kafka.enabled                                                   | boolean | -             |                             |
| kafka.metrics.jmx                                                             | object  | -             |                             |
| kafka.metrics.jmx.enabled                                                     | boolean | -             |                             |
| kafka.zookeeper                                                               | object  | -             |                             |
| kafka.zookeeper.auth                                                          | object  | -             |                             |
| kafka.zookeeper.auth.enabled                                                  | boolean | -             |                             |
| kafka.zookeeper.metrics                                                       | object  | -             |                             |
| kafka.zookeeper.metrics.enabled                                               | boolean | -             |                             |
| kafka.client                                                                  | object  | -             |                             |
| kafka.client.protocol                                                         | string  | -             |                             |
| kafka.extraConfig                                                             | string  | -             |                             |
| webeventredis                                                                 | object  | -             | Webeventredis configuration |
| webeventredis.enabled                                                         | boolean | -             |                             |
| webeventredis.architecture                                                    | string  | -             |                             |
| webeventredis.image                                                           | object  | -             |                             |
| webeventredis.image.name                                                      | string  | -             |                             |
| webeventredis.commonLabels                                                    | object  | -             |                             |
| webeventredis.commonLabels.app                                                | string  | -             |                             |
| webeventredis.tls                                                             | object  | -             |                             |
| webeventredis.tls.enabled                                                     | boolean | -             |                             |
| webeventredis.tls.authClients                                                 | boolean | -             |                             |
| webeventredis.tls.existingSecret                                              | string  | -             |                             |
| webeventredis.tls.certCAFilename                                              | string  | -             |                             |
| webeventredis.tls.certFilename                                                | string  | -             |                             |
| webeventredis.tls.certKeyFilename                                             | string  | -             |                             |
| webeventredis.sentinel                                                        | object  | -             |                             |
| webeventredis.sentinel.enabled                                                | boolean | -             |                             |
| webeventredis.auth                                                            | object  | -             |                             |
| webeventredis.auth.sentinel                                                   | boolean | -             |                             |
| webeventredis.auth.existingSecret                                             | string  | -             |                             |
| webeventredis.auth.existingSecretPasswordKey                                  | string  | -             |                             |
| webeventredis.replica                                                         | object  | -             |                             |
| webeventredis.replica.persistence                                             | object  | -             |                             |
| webeventredis.replica.persistence.size                                        | string  | -             |                             |
| webeventredis.replica.replicaCount                                            | integer | -             |                             |
| webeventredis.replica.service                                                 | object  | -             |                             |
| webeventredis.replica.service.resourcesPreset                                 | string  | -             |                             |
| webeventredis.master                                                          | object  | -             |                             |
| webeventredis.master.persistence                                              | object  | -             |                             |
| webeventredis.master.persistence.size                                         | string  | -             |                             |
| webeventredis.master.service                                                  | object  | -             |                             |
| webeventredis.master.service.resourcesPreset                                  | string  | -             |                             |
| webeventredis.master.service.extraPorts                                       | array   | -             |                             |
| webeventredis.master.preExecCmds                                              | string  | -             |                             |
| webeventredis.ingress                                                         | object  | -             |                             |
| webeventredis.ingress.enabled                                                 | boolean | -             |                             |
| webeventredis.ingress.tls                                                     | boolean | -             |                             |
| webeventredis.ingress.selfSigned                                              | boolean | -             |                             |
| webeventredis.ingress.ingressClassName                                        | string  | -             |                             |
| webeventredis.ingress.annotations                                             | object  | -             |                             |
| webeventredis.ingress.annotations.nginx.ingress.kubernetes.io/ssl-passthrough | string  | -             |                             |
| minio                                                                         | object  | -             | Minio configuration         |
| minio.mode                                                                    | string  | -             |                             |
| minio.image                                                                   | object  | -             |                             |
| minio.image.name                                                              | string  | -             |                             |
| minio.image.pullPolicy                                                        | string  | -             |                             |
| minio.persistence                                                             | object  | -             |                             |
| minio.persistence.enabled                                                     | boolean | -             |                             |
| minio.persistence.size                                                        | string  | -             |                             |
| minio.resources                                                               | object  | -             |                             |
| minio.resources.requests                                                      | object  | -             |                             |
| minio.resources.requests.memory                                               | string  | -             |                             |
| minio.resources.requests.cpu                                                  | string  | -             |                             |
| minio.extraVolumes                                                            | string  | -             |                             |
| minio.extraVolumeMounts                                                       | string  | -             |                             |
| minio.lifecycleHooks                                                          | object  | -             |                             |
| minio.lifecycleHooks.postStart                                                | object  | -             |                             |
| minio.lifecycleHooks.postStart.exec                                           | object  | -             |                             |
| minio.lifecycleHooks.postStart.exec.command                                   | array   | -             |                             |
| minio.auth                                                                    | object  | -             |                             |
| minio.auth.existingSecret                                                     | string  | -             |                             |
| minio.auth.rootUserSecretKey                                                  | string  | -             |                             |
| minio.auth.rootPasswordSecretKey                                              | string  | -             |                             |
| auth                                                                          | object  | -             |                             |
| auth.auth-keycloak                                                            | object  | -             |                             |
| auth.auth-keycloak.image                                                      | object  | -             |                             |
| auth.auth-keycloak.image.repository                                           | string  | -             |                             |
| auth.auth-keycloak.imagePullSecrets                                           | array   | -             |                             |
| auth.auth-keycloak.adminUsername                                              | string  | -             |                             |
| auth.auth-keycloak.initialUsername                                            | string  | -             |                             |
| auth.auth-keycloak.organizationName                                           | string  | -             |                             |
| auth.ingress                                                                  | object  | -             |                             |
| auth.ingress.enabled                                                          | boolean | -             |                             |
| auth.migrations                                                               | object  | -             |                             |
| auth.migrations.enabled                                                       | string  | -             |                             |
| auth.migrations.extraFiles                                                    | array   | -             |                             |
| auth.auth-postgresql                                                          | object  | -             |                             |
| auth.auth-postgresql.image                                                    | object  | -             |                             |
| auth.auth-postgresql.image.name                                               | string  | -             |                             |
| auth.auth-postgresql.primary                                                  | object  | -             |                             |
| auth.auth-postgresql.primary.persistence                                      | object  | -             |                             |
| auth.auth-postgresql.primary.persistence.size                                 | string  | -             |                             |
| mongodb                                                                       | object  | -             |                             |
| mongodb.enabled                                                               | boolean | -             |                             |
| mongodb.architecture                                                          | string  | -             |                             |
| mongodb.replicaSetName                                                        | string  | -             |                             |
| mongodb.image                                                                 | object  | -             |                             |
| mongodb.image.name                                                            | string  | -             |                             |
| mongodb.replicaCount                                                          | integer | -             |                             |
| mongodb.persistence                                                           | object  | -             |                             |
| mongodb.persistence.size                                                      | string  | -             |                             |
| mongodb.annotations                                                           | object  | -             |                             |
| mongodb.annotations.helm.sh/hook-weight                                       | string  | -             |                             |
| mongodb.auth                                                                  | object  | -             |                             |
| mongodb.auth.rootPassword                                                     | string  | -             |                             |
| mongodb.auth.replicaSetKey                                                    | string  | -             |                             |
| mongodb.auth.usernames                                                        | array   | -             |                             |
| mongodb.auth.passwords                                                        | array   | -             |                             |
| mongodb.auth.databases                                                        | array   | -             |                             |
| ingress-nginx                                                                 | object  | -             |                             |
| ingress-nginx.enabled                                                         | boolean | True          | Enable ingress-nginx        |
| ingress-nginx.imagePullSecrets                                                | array   | -             |                             |
| ingress-nginx.tcp                                                             | object  | -             |                             |
| ingress-nginx.tcp.6379                                                        | string  | -             |                             |
| ingress-nginx.controller                                                      | object  | -             |                             |
| ingress-nginx.controller.kind                                                 | string  | -             |                             |
| ingress-nginx.controller.ingressClass                                         | string  | -             |                             |
| ingress-nginx.controller.extraArgs                                            | object  | -             |                             |
| ingress-nginx.controller.extraArgs.enable-ssl-passthrough                     | string  | -             |                             |
| ingress-nginx.controller.extraArgs.ingress-class                              | string  | -             |                             |
| ingress-nginx.controller.ingressClassResource                                 | object  | -             |                             |
| ingress-nginx.controller.ingressClassResource.name                            | string  | -             |                             |
| ingress-nginx.controller.ingressClassResource.enabled                         | boolean | -             |                             |
| ingress-nginx.controller.ingressClassResource.default                         | boolean | -             |                             |
| ingress-nginx.controller.ingressClassResource.controllerClass                 | string  | -             |                             |
| ingress-nginx.controller.ingressClassResource.parameters                      | object  | -             |                             |
| ingress-nginx.controller.image                                                | object  | -             |                             |
| ingress-nginx.controller.image.repository                                     | string  | -             |                             |
| ingress-nginx.controller.image.tag                                            | string  | -             |                             |
| ingress-nginx.controller.image.digest                                         | string  | -             |                             |
| ingress-nginx.controller.config                                               | object  | -             |                             |
| ingress-nginx.controller.config.proxy-body-size                               | string  | -             |                             |
| ingress-nginx.controller.config.proxy-connect-timeout                         | string  | -             |                             |
| ingress-nginx.controller.config.proxy-read-timeout                            | string  | -             |                             |
| ingress-nginx.controller.config.client-header-timeout                         | string  | -             |                             |
| ingress-nginx.controller.config.client-body-timeout                           | string  | -             |                             |
| ingress-nginx.controller.config.send-timeout                                  | string  | -             |                             |
| ingress-nginx.controller.config.keepalive-timeout                             | string  | -             |                             |
| ingress-nginx.controller.admissionWebhooks                                    | object  | -             |                             |
| ingress-nginx.controller.admissionWebhooks.enabled                            | boolean | -             |                             |
| ingress-nginx.controller.admissionWebhooks.patch                              | object  | -             |                             |
| ingress-nginx.controller.admissionWebhooks.patch.image                        | object  | -             |                             |
| ingress-nginx.controller.admissionWebhooks.patch.image.repository             | string  | -             |                             |
| ingress-nginx.controller.admissionWebhooks.patch.image.tag                    | string  | -             |                             |
| ingress-nginx.controller.admissionWebhooks.patch.image.pullPolicy             | string  | -             |                             |
| ingress-nginx.controller.admissionWebhooks.patch.image.digest                 | string  | -             |                             |
| ingress-nginx.defaultBackend                                                  | object  | -             |                             |
| ingress-nginx.defaultBackend.enabled                                          | boolean | -             |                             |
| ingress-nginx.defaultBackend.image                                            | object  | -             |                             |
| ingress-nginx.defaultBackend.image.repository                                 | string  | -             |                             |
| ingress-nginx.defaultBackend.image.tag                                        | string  | -             |                             |
| ingress-nginx.defaultBackend.image.pullPolicy                                 | string  | -             |                             |
| ingress-nginx.defaultBackend.image.digest                                     | string  | -             |                             |

#### Auth Parameters

Users can configure `auth.` values in `values.yaml`

```yaml
# Example usage:
auth:
  auth-keycloak:
    adminPassword: password
```

| Key                                                    | Type    | Default Value | Description                            |
| ------------------------------------------------------ | ------- | ------------- | -------------------------------------- |
| auth-keycloak.adminPassword                            | string  | -             | Admin password for keycloak            |
| auth-keycloak.adminUsername                            | string  | -             | Admin username for keycloak            |
| auth-keycloak.allowDisposableEmails                    | boolean | -             | Allow disposable emails                |
| auth-keycloak.annotations                              | object  | -             | Annotations for keycloak               |
| auth-keycloak.bruteForce                               | object  | -             | Brute force configuration for keycloak |
| auth-keycloak.bruteForce.bruteForceProtected           | string  | -             |                                        |
| auth-keycloak.bruteForce.failureFactor                 | string  | -             |                                        |
| auth-keycloak.bruteForce.maxDeltaTimeSeconds           | string  | -             |                                        |
| auth-keycloak.bruteForce.maxFailureWaitSeconds         | string  | -             |                                        |
| auth-keycloak.bruteForce.minimumQuickLoginWaitSeconds  | string  | -             |                                        |
| auth-keycloak.bruteForce.permanentLockout              | string  | -             |                                        |
| auth-keycloak.bruteForce.quickLoginCheckMilliSeconds   | string  | -             |                                        |
| auth-keycloak.bruteForce.waitIncrementSeconds          | string  | -             |                                        |
| auth-keycloak.cli                                      | object  | -             |                                        |
| auth-keycloak.cli.enabled                              | boolean | -             |                                        |
| auth-keycloak.database                                 | object  | -             | Database configuration for keycloak    |
| auth-keycloak.database.database                        | string  | -             |                                        |
| auth-keycloak.database.hostname                        | string  | -             |                                        |
| auth-keycloak.database.password                        | string  | -             |                                        |
| auth-keycloak.database.port                            | string  | -             |                                        |
| auth-keycloak.database.username                        | string  | -             |                                        |
| auth-keycloak.database.vendor                          | string  | -             |                                        |
| auth-keycloak.defaultUserGroupRoles                    | string  | -             |                                        |
| auth-keycloak.dmzCustomDomain                          | object  | -             |                                        |
| auth-keycloak.dmzCustomDomain.domain                   | null    | -             |                                        |
| auth-keycloak.dmzCustomDomain.enabled                  | boolean | -             |                                        |
| auth-keycloak.enabledOrganization                      | boolean | -             |                                        |
| auth-keycloak.enabledRegistration                      | boolean | -             |                                        |
| auth-keycloak.extraEnv                                 | string  | -             |                                        |
| auth-keycloak.extraInitContainers                      | string  | -             |                                        |
| auth-keycloak.extraVolumeMounts                        | string  | -             |                                        |
| auth-keycloak.extraVolumes                             | string  | -             |                                        |
| auth-keycloak.identityProviders                        | object  | -             |                                        |
| auth-keycloak.identityProviders.bitbucket              | object  | -             |                                        |
| auth-keycloak.identityProviders.bitbucket.clientId     | null    | -             |                                        |
| auth-keycloak.identityProviders.bitbucket.clientSecret | null    | -             |                                        |
| auth-keycloak.identityProviders.bitbucket.enabled      | boolean | -             |                                        |
| auth-keycloak.identityProviders.github                 | object  | -             |                                        |
| auth-keycloak.identityProviders.github.clientId        | null    | -             |                                        |
| auth-keycloak.identityProviders.github.clientSecret    | null    | -             |                                        |
| auth-keycloak.identityProviders.github.enabled         | boolean | -             |                                        |
| auth-keycloak.identityProviders.google                 | object  | -             |                                        |
| auth-keycloak.identityProviders.google.clientId        | null    | -             |                                        |
| auth-keycloak.identityProviders.google.clientSecret    | null    | -             |                                        |
| auth-keycloak.identityProviders.google.enabled         | boolean | -             |                                        |
| auth-keycloak.image                                    | object  | -             |                                        |
| auth-keycloak.image.pullPolicy                         | string  | -             |                                        |
| auth-keycloak.image.repository                         | string  | -             |                                        |
| auth-keycloak.image.tag                                | string  | -             |                                        |
| auth-keycloak.importRealm                              | boolean | -             |                                        |
| auth-keycloak.ingress                                  | object  | -             |                                        |
| auth-keycloak.ingress.enabled                          | boolean | -             |                                        |
| auth-keycloak.initialOrganizationId                    | string  | -             | Initial organization id                |
| auth-keycloak.initialPassword                          | string  | -             | Initial user password                  |
| auth-keycloak.initialUsername                          | string  | -             | Initial user name                      |
| auth-keycloak.organizationName                         | string  | -             | Initial organization name              |
| auth-keycloak.recaptcha                                | object  | -             | Recaptcha configuration for keycloak   |
| auth-keycloak.recaptcha.maxFailures                    | string  | 4             | Recaptcha max failures                 |
| auth-keycloak.recaptcha.requirement                    | string  | DISABLED      | Recaptcha requirement                  |
| auth-keycloak.recaptcha.secret                         | string  | -             |                                        |
| auth-keycloak.recaptcha.siteKey                        | string  | -             |                                        |
| auth-keycloak.userLookupDecisionStrategy               | string  | -             |                                        |
| auth-postgresql                                        | object  | -             |                                        |
| auth-postgresql.architecture                           | string  | standalone    | PostgreSQL Architecture                |
| auth-postgresql.enabled                                | boolean | -             | Enable PostgreSQL                      |

#### Common Module Parameters

Users can set values for `%MODULE_NAME%.` in `values.yaml`.

```yaml
# Example usage:
publish:
  extraEnvVars:
    - name: "EXAMPLE"
      value: "example"
```

| Key                                               | Type                 | Default Value | Description                                                                                                                                                                                                    |
| ------------------------------------------------- | -------------------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| affinity                                          | ['object', 'string'] | -             | Affinity for deployment pods assignment                                                                                                                                                                        |
| args                                              | array                | -             | Override default container args (useful when using custom images)                                                                                                                                              |
| automountServiceAccountToken                      | boolean              | -             | Mount Service Account token in pods                                                                                                                                                                            |
| autoscaling                                       | object               | -             | Autoscaling configuration                                                                                                                                                                                      |
| autoscaling.hpa                                   | object               | -             |                                                                                                                                                                                                                |
| autoscaling.hpa.enabled                           | boolean              | -             |                                                                                                                                                                                                                |
| autoscaling.hpa.maxReplicas                       | string               | -             |                                                                                                                                                                                                                |
| autoscaling.hpa.minReplicas                       | string               | -             |                                                                                                                                                                                                                |
| autoscaling.hpa.targetCPU                         | string               | -             |                                                                                                                                                                                                                |
| autoscaling.hpa.targetMemory                      | string               | -             |                                                                                                                                                                                                                |
| autoscaling.vpa                                   | object               | -             |                                                                                                                                                                                                                |
| autoscaling.vpa.annotations                       | ['object', 'string'] | -             |                                                                                                                                                                                                                |
| autoscaling.vpa.controlledResources               | array                | -             |                                                                                                                                                                                                                |
| autoscaling.vpa.enabled                           | boolean              | -             |                                                                                                                                                                                                                |
| autoscaling.vpa.maxAllowed                        | object               | -             |                                                                                                                                                                                                                |
| autoscaling.vpa.minAllowed                        | object               | -             |                                                                                                                                                                                                                |
| autoscaling.vpa.updatePolicy                      | object               | -             |                                                                                                                                                                                                                |
| autoscaling.vpa.updatePolicy.updateMode           | string               | Auto          | Specifies whether recommended updates are applied when a Pod is started and whether recommended updates are applied during the life of a Pod                                                                   |
| clusterDomain                                     | string               | cluster.local | clusterDomain Kubernetes cluster domain name                                                                                                                                                                   |
| command                                           | array                | -             | Override default container command (useful when using custom images)                                                                                                                                           |
| commonAnnotations                                 | ['object', 'string'] | -             | Annotations to add to all deployed objects                                                                                                                                                                     |
| commonLabels                                      | object               | -             | Labels to add to all deployed objects                                                                                                                                                                          |
| containerPorts                                    | object               | -             |                                                                                                                                                                                                                |
| containerPorts.http                               | integer              | -             | HTTP container port                                                                                                                                                                                            |
| containerPorts.https                              | integer              | -             | HTTPS container port                                                                                                                                                                                           |
| containerSecurityContext                          | object               | -             | Configure Container Security Context                                                                                                                                                                           |
| containerSecurityContext.allowPrivilegeEscalation | boolean              | False         | Set allowPrivilegeEscalation in container' Security Context                                                                                                                                                    |
| containerSecurityContext.capabilities             | object               | -             |                                                                                                                                                                                                                |
| containerSecurityContext.capabilities.drop        | array                | -             | List of capabilities to be dropped in container                                                                                                                                                                |
| containerSecurityContext.enabled                  | boolean              | False         | Enabled container' Security Context                                                                                                                                                                            |
| containerSecurityContext.privileged               | boolean              | False         | Set privileged in container' Security Context                                                                                                                                                                  |
| containerSecurityContext.readOnlyRootFilesystem   | boolean              | True          | Set readOnlyRootFilesystem in container' Security Context                                                                                                                                                      |
| containerSecurityContext.runAsGroup               | integer              | 1001          | Set runAsNonRoot in container' Security Context                                                                                                                                                                |
| containerSecurityContext.runAsNonRoot             | boolean              | True          | Set runAsNonRoot in container' Security Context                                                                                                                                                                |
| containerSecurityContext.runAsUser                | integer              | 1001          | Set runAsUser in container' Security Context                                                                                                                                                                   |
| containerSecurityContext.seLinuxOptions           | ['object', 'null']   | -             | [object,nullable] Set SELinux options in container                                                                                                                                                             |
| containerSecurityContext.seccompProfile           | object               | -             |                                                                                                                                                                                                                |
| containerSecurityContext.seccompProfile.type      | string               | -             | Set seccomp profile in container                                                                                                                                                                               |
| customLivenessProbe                               | ['object', 'string'] | -             | Custom livenessProbe that overrides the default one                                                                                                                                                            |
| customReadinessProbe                              | ['object', 'string'] | -             | Custom customReadinessProbe that overrides the default one                                                                                                                                                     |
| customStartupProbe                                | ['object', 'string'] | -             | Custom customStartupProbe that overrides the default one                                                                                                                                                       |
| daemonsetAnnotations                              | ['object', 'string'] | -             | Annotations for daemonset                                                                                                                                                                                      |
| deploymentAnnotations                             | ['object', 'string'] | -             | Annotations for deployment                                                                                                                                                                                     |
| diagnosticMode                                    | object               | -             | Diagnostic mode                                                                                                                                                                                                |
| diagnosticMode.args                               | array                | ['infinity']  | Args to override all containers in the chart release                                                                                                                                                           |
| diagnosticMode.command                            | array                | ['sleep']     | Command to override all containers in the chart release                                                                                                                                                        |
| diagnosticMode.enabled                            | boolean              | False         | Enable diagnostic mode (all probes will be disabled and the command will be overridden)                                                                                                                        |
| extraContainerPorts                               | array                | -             | Optionally specify extra list of additional ports for pod containers                                                                                                                                           |
| extraEnvVars                                      | ['array', 'string']  | -             | Array with extra environment variables to add to containers                                                                                                                                                    |
| secretVariables                                   | ['array', 'string']  | -             | Array with extra secret variables to add to container secret                                                                                                                                                   |
| extraEnvVarsCM                                    | string               | -             | Name of existing ConfigMap containing extra env vars for containers                                                                                                                                            |
| extraEnvVarsSecret                                | string               | -             | Name of existing Secret containing extra env vars for containers                                                                                                                                               |
| extraVolumeMounts                                 | array                | -             | Optionally specify extra list of additional volumes for the pods                                                                                                                                               |
| extraVolumes                                      | array                | -             | Optionally specify extra list of additional volumes for the pods                                                                                                                                               |
| hostAliases                                       | ['array', 'string']  | -             | Pods host aliases                                                                                                                                                                                              |
| image                                             | object               | -             |                                                                                                                                                                                                                |
| image.debug                                       | boolean              | -             |                                                                                                                                                                                                                |
| image.digest                                      | string               | -             | Container image digest in the way sha256:aa.... Please note this parameter, if set, will override the tag                                                                                                      |
| image.pullPolicy                                  | string               | -             | Container image pullPolicy                                                                                                                                                                                     |
| image.pullSecrets                                 | array                | -             | Specify image pull secrets                                                                                                                                                                                     |
| image.registry                                    | string               | -             | Container image registry                                                                                                                                                                                       |
| image.repository                                  | string               | -             | Container image repository                                                                                                                                                                                     |
| image.tag                                         | string               | -             | Container image tag (immutable tags are recommended)                                                                                                                                                           |
| importTrustedCerts                                | boolean              | True          | Import given trusted cetificates                                                                                                                                                                               |
| ingress                                           | object               | -             |                                                                                                                                                                                                                |
| ingress.annotations                               | ['object', 'string'] | -             | Additional annotations for the Ingress resource.                                                                                                                                                               |
| ingress.apiVersion                                | string               | -             | Force Ingress API version (automatically detected if not set)                                                                                                                                                  |
| ingress.enabled                                   | boolean              | -             | Enable ingress record generation                                                                                                                                                                               |
| ingress.extraHosts                                | array                | -             | An array with additional hostname(s) to be covered with the ingress record                                                                                                                                     |
| ingress.extraPaths                                | array                | -             | An array with additional arbitrary paths that may need to be added to the ingress under the main host                                                                                                          |
| ingress.extraRules                                | array                | -             | Additional rules to be covered with this ingress record                                                                                                                                                        |
| ingress.extraTls                                  | array                | -             | TLS configuration for additional hostname(s) to be covered with this ingress record                                                                                                                            |
| ingress.hostname                                  | string               | -             | Default host for the ingress record                                                                                                                                                                            |
| ingress.ingressClassName                          | string               | -             | IngressClass that will be be used to implement the Ingress (Kubernetes 1.18+)                                                                                                                                  |
| ingress.path                                      | string               | -             | Default path for the ingress record                                                                                                                                                                            |
| ingress.pathType                                  | string               | -             | Ingress path type                                                                                                                                                                                              |
| ingress.secrets                                   | array                | []            | Custom TLS certificates as secrets                                                                                                                                                                             |
| ingress.selfSigned                                | boolean              | False         | Create a TLS secret for this ingress record using self-signed certificates generated by Helm                                                                                                                   |
| ingress.tls                                       | boolean              | False         | Enable TLS configuration for the host defined at `ingress.hostname` parameter                                                                                                                                  |
| initContainers                                    | ['array', 'string']  | -             | Add additional init containers to the pods                                                                                                                                                                     |
| lifecycleHooks                                    | object               | -             | Container to automate configuration before or after startup                                                                                                                                                    |
| lifecycleHooks.postStart                          | object               | -             |                                                                                                                                                                                                                |
| lifecycleHooks.postStart.exec                     | object               | -             |                                                                                                                                                                                                                |
| lifecycleHooks.postStart.exec.command             | array                | -             |                                                                                                                                                                                                                |
| lifecycleHooks.preStop                            | object               | -             |                                                                                                                                                                                                                |
| lifecycleHooks.preStop.exec                       | object               | -             |                                                                                                                                                                                                                |
| lifecycleHooks.preStop.exec.command               | array                | -             |                                                                                                                                                                                                                |
| nodeAffinityPreset                                | ['object', 'string'] | -             |                                                                                                                                                                                                                |
| nodeSelector                                      | ['object', 'string'] | -             |                                                                                                                                                                                                                |
| pdb                                               | ['object', 'string'] | -             |                                                                                                                                                                                                                |
| persistence                                       | ['object', 'string'] | -             | Enable persistence using Persistent Volume Claims                                                                                                                                                              |
| podAffinityPreset                                 | string               |               | Pod affinity preset. Ignored if `affinity` is set. Allowed values: `soft` or `hard`                                                                                                                            |
| podAnnotations                                    | ['object', 'string'] | -             | Annotations for pods                                                                                                                                                                                           |
| podAntiAffinityPreset                             | string               | soft          | Pod anti-affinity preset. Ignored if `affinity` is set. Allowed values: `soft` or `hard`                                                                                                                       |
| podLabels                                         | ['object', 'string'] | -             | Extra labels for pods                                                                                                                                                                                          |
| podManagementPolicy                               | string               | -             |                                                                                                                                                                                                                |
| podSecurityContext                                | ['object', 'string'] | -             | Configure Pods Security Context                                                                                                                                                                                |
| priorityClassName                                 | string               | -             |                                                                                                                                                                                                                |
| replicaCount                                      | integer              | 1             | Number of replicas to deploy                                                                                                                                                                                   |
| resources                                         | ['object', 'string'] | {}            | Set container requests and limits for different resources like CPU or memory (essential for production workloads)                                                                                              |
| resourcesPreset                                   | string               | none          | Set container resources according to one common preset (allowed values: none, nano, small, medium, large, xlarge, 2xlarge). This is ignored if 'resources' is set ('resources' is recommended for production). |
| schedulerName                                     | string               |               | Name of the k8s scheduler (other than default) for pods                                                                                                                                                        |
| terminationGracePeriodSeconds                     | string               | -             | Seconds pods need to terminate gracefully                                                                                                                                                                      |
| tolerations                                       | array                | []            | Tolerations for pods assignment                                                                                                                                                                                |
| topologySpreadConstraints                         | array                | []            | Topology Spread Constraints for %%MAIN_CONTAINER_NAME%% pod assignment spread across your cluster among failure-domains                                                                                        |
| updateStrategy                                    | object               | -             | Deployment strategy type                                                                                                                                                                                       |
| updateStrategy.type                               | string               | RollingUpdate | Can be set to RollingUpdate or Recreate                                                                                                                                                                        |
| volumePermissions                                 | ['object', 'string'] | -             | 'volumePermissions' init container parameters                                                                                                                                                                  |

<NeedHelp />
