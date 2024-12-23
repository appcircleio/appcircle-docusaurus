---
title: Advanced Configuration
description: Learn how to fully configure the Appcircle server Helm chart
tags: [self-hosted, helm, configuration, kubernetes]
sidebar_position: 100
---

import NeedHelp from '@site/docs/\_need-help.mdx';

For advanced configuration options, open the `values.yaml` file with your preferred text editor and modify the settings as needed.

Once you have updated the `values.yaml` file, please proceed to the [Upgrade Appcircle Server](/self-hosted-appcircle/install-server/helm-chart/upgrades) section to apply the changes.

## Custom Testing Distribution Domain

To configure a custom domain for the Appcircle Testing Distribution, update your `values.yaml` file with the custom domain settings. Below is an example configuration for a custom Testing Distribution domain usage:

```yaml
global:
  distribution:
    distribution-testerweb:
      url: https://dist.spacetech.com
distribution:
  distribution-testerweb:
    ingress:
      extraHosts:
        - name: dist.spacetech.com
          path: /
      extraTls:
        - secretName: k8s-dist-spacetech-com-tls
          hosts:
            - dist.spacetech.com
```

:::caution
The emails related to the Testing Distribution will now include the new domain in the links. Please note that old links associated with the previous domain will no longer work.
:::

After updating the `values.yaml` file, create a TLS secret for the custom domain using the following command:

:::info

- The certificate (`cert`) should be in **PEM format** and it's recommended to include the leaf (app), intermediate, and root (CA) certificates to form a **full-chain** certificate.
- The private key (`key`) **should not be password-protected**.
  :::

```bash
kubectl create secret tls k8s-dist-spacetech-com-tls \
--cert=fullchain.crt \
--key=private.key
```

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

To deploy the Appcircle server with customized parameters, refer to the basic values.yaml configuration table below.

### Parameters

| Parameter                                                     | Description                                                               | Default Value                 |
| ------------------------------------------------------------- | ------------------------------------------------------------------------- | ----------------------------- |
| `global.appEnvironment`                                       | Specifies the application environment (e.g., Development, Production).    | 'Development'                 |
| `global.imageRegistry`                                        | The Docker registry where container images are stored.                    | 'europe-west1-docker.pkg.dev' |
| `global.imageRepositoryPath`                                  | The path within the Docker registry for the application's images.         | 'appcircle/docker-registry'   |
| `global.imageTag`                                             | The specific tag of the Docker image to use.                              | 'v3.23.2'                     |
| `global.imagePullSecrets`                                     | Secrets used to authenticate with private Docker registries.              | [ 'containerregistry' ]       |
| `global.ingressClassName`                                     | Specifies the ingress class name used for all application ingresses.      | 'appcircle'                   |
| `global.defaultStorageClass`                                  | The default storage class used for persistent volumes in the application. | -                             |
| `global.urls.domainName`                                      | The domain name used for the application (e.g., .example.com).            | -                             |
| `global.urls.scheme`                                          | The URL scheme used for the application (e.g., http or https).            | 'http'                        |
| `global.urls.auth.subdomain`                                  | Subdomain used for the authentication service.                            | 'auth'                        |
| `global.urls.privateApi.subdomain`                            | Subdomain used for the private API service.                               | 'api'                         |
| `global.urls.webApp.subdomain`                                | Subdomain used for the web application.                                   | 'my'                          |
| `global.urls.webEvent.subdomain`                              | Subdomain used for the web event service.                                 | 'hook'                        |
| `global.urls.distributionTesterWeb.subdomain`                 | Subdomain used for the distribution tester web.                           | 'dist'                        |
| `global.urls.store.subdomain`                                 | Subdomain used for the store service.                                     | 'store'                       |
| `global.urls.webEventRedis.subdomain`                         | Subdomain used for the web event Redis service.                           | 'kvs'                         |
| `global.urls.resource.subdomain`                              | Subdomain used for the resource service.                                  | 'resource'                    |
| `global.mail.provider`                                        | Mail provider to use (e.g., MailKitSMTP, SMTP ).                          | 'MailKitSMTP'                 |
| `global.mail.smtp`                                            | SMTP configuration details.                                               | -                             |
| `global.mail.smtp.host`                                       | SMTP server hostname.                                                     | -                             |
| `global.mail.smtp.username`                                   | SMTP username.                                                            | -                             |
| `global.mail.smtp.from`                                       | The "From" address used for emails.                                       | -                             |
| `global.mail.smtp.fromDisplayName`                            | The display name for the sender of emails.                                | -                             |
| `global.mail.smtp.port`                                       | Port number for the SMTP server.                                          | -                             |
| `global.mail.smtp.password`                                   | Password for the SMTP account.                                            | -                             |
| `global.mail.smtp.ssl`                                        | Whether SSL is enabled for SMTP.                                          | 'false'                       |
| `global.mail.smtp.auth`                                       | Whether Authentication is enabled for SMTP.                               | 'true'                        |
| `global.mail.smtp.starttls`                                   | Whether STARTTLS is enabled for SMTP.                                     | 'true'                        |
| `global.distribution.distribution-testerweb.url`              | The external URL for the distribution tester web module.                  | -                             |
| `global.tlsWildcard.cert`                                     | The wildcard TLS certificate.                                             | -                             |
| `global.tlsWildcard.caCert`                                   | The Certificate Authority (CA) for the wildcard certificate.              | -                             |
| `global.tlsWildcard.key`                                      | The private key for the wildcard certificate.                             | -                             |
| `global.trustedCerts`                                         | List of trusted certificates.                                             | []                            |
| `global.minio.url`                                            | External Minio URL.                                                       | -                             |
| `global.minio.region`                                         | The region for Minio.                                                     | `local`                       |
| `global.minio.bucketPrefix`                                   | Prefix for Minio buckets.                                                 | `appcircle-local-resource-`   |
| `global.containerRegistrySecret`                              | Secret used for accessing the container registry.                         | -                             |
| `global.redis.enabled`                                        | Whether a common Redis instance is enabled for all modules.               | `false`                       |
| `global.redis.everyModule`                                    | Whether separate Redis instances are enabled for each module.             | `true`                        |
| `global.vault.url`                                            | External URL for Vault.                                                   | -                             |
| `auth.auth-keycloak.adminUsername`                            | Admin username for Keycloak.                                              | 'admin'                       |
| `auth.auth-keycloak.initialUsername`                          | Initial username for the default user.                                    | 'admin@myappcircle.io'        |
| `auth.auth-keycloak.organizationName`                         | Initial organization name in Keycloak.                                    | 'myappcircle'                 |
| `auth.auth-keycloak.allowDisposableEmails`                    | Determines whether disposable emails are allowed for registration.        | false                         |
| `auth.auth-keycloak.bruteForce.bruteForceProtected`           | Enables brute force protection for Keycloak.                              | 'true'                        |
| `auth.auth-keycloak.bruteForce.failureFactor`                 | Number of failed login attempts before action is taken.                   | '30'                          |
| `auth.auth-keycloak.bruteForce.maxDeltaTimeSeconds`           | Maximum time in seconds to consider failed login attempts.                | '43200'                       |
| `auth.auth-keycloak.bruteForce.maxFailureWaitSeconds`         | Maximum wait time in seconds after consecutive failures.                  | '900'                         |
| `auth.auth-keycloak.bruteForce.minimumQuickLoginWaitSeconds`  | Minimum wait time in seconds for quick login attempts.                    | '60'                          |
| `auth.auth-keycloak.bruteForce.permanentLockout`              | Enables permanent account lockout after repeated failures.                | 'false'                       |
| `auth.auth-keycloak.bruteForce.quickLoginCheckMilliSeconds`   | Time in milliseconds to check quick login attempts.                       | '1000'                        |
| `auth.auth-keycloak.bruteForce.waitIncrementSeconds`          | Time increment in seconds for wait periods after failures.                | '60'                          |
| `auth.auth-keycloak.cli.enabled`                              | Enables the Keycloak CLI for custom commands.                             | false                         |
| `auth.auth-keycloak.database.database`                        | Name of the Keycloak database.                                            | -                             |
| `auth.auth-keycloak.database.hostname`                        | Hostname of the Keycloak database.                                        | -                             |
| `auth.auth-keycloak.database.password`                        | Password for the Keycloak database.                                       | -                             |
| `auth.auth-keycloak.database.port`                            | Port number for the Keycloak database.                                    | -                             |
| `auth.auth-keycloak.database.username`                        | Username for the Keycloak database.                                       | -                             |
| `auth.auth-keycloak.database.vendor`                          | Database vendor for Keycloak (e.g., postgres, mysql).                     | 'postgres'                    |
| `auth.auth-keycloak.defaultUserGroupRoles`                    | Default roles assigned to new users in Keycloak.                          | -                             |
| `auth.auth-keycloak.dmzCustomDomain.domain`                   | Domain name for the DMZ custom configuration.                             | -                             |
| `auth.auth-keycloak.dmzCustomDomain.enabled`                  | Enables custom domain for DMZ.                                            | false                         |
| `auth.auth-keycloak.enabledOrganization`                      | Enables the organization feature in Keycloak.                             | -                             |
| `auth.auth-keycloak.enabledRegistration`                      | Enables user registration in Keycloak.                                    | -                             |
| `auth.auth-keycloak.extraEnv`                                 | Additional environment variables for the Keycloak deployment.             | []                            |
| `auth.auth-keycloak.extraInitContainers`                      | Additional init containers for the Keycloak deployment.                   | []                            |
| `auth.auth-keycloak.extraVolumeMounts`                        | Extra volume mounts for the Keycloak deployment.                          | []                            |
| `auth.auth-keycloak.extraVolumes`                             | Extra volumes for the Keycloak deployment.                                | []                            |
| `auth.auth-keycloak.identityProviders.bitbucket.clientId`     | Client ID for Bitbucket integration.                                      | -                             |
| `auth.auth-keycloak.identityProviders.bitbucket.clientSecret` | Client secret for Bitbucket integration.                                  | -                             |
| `auth.auth-keycloak.identityProviders.bitbucket.enabled`      | Enables Bitbucket as an identity provider.                                | false                         |
| `auth.auth-keycloak.identityProviders.github.clientId`        | Client ID for GitHub integration.                                         | -                             |
| `auth.auth-keycloak.identityProviders.github.clientSecret`    | Client secret for GitHub integration.                                     | -                             |
| `auth.auth-keycloak.identityProviders.github.enabled`         | Enables GitHub as an identity provider.                                   | false                         |
| `auth.auth-keycloak.identityProviders.google.clientId`        | Client ID for Google integration.                                         | -                             |
| `auth.auth-keycloak.identityProviders.google.clientSecret`    | Client secret for Google integration.                                     | -                             |
| `auth.auth-keycloak.identityProviders.google.enabled`         | Enables Google as an identity provider.                                   | false                         |
| `auth.auth-keycloak.image.pullPolicy`                         | Image pull policy for Keycloak.                                           | -                             |
| `auth.auth-keycloak.image.repository`                         | Repository for the Keycloak image.                                        | -                             |
| `auth.auth-keycloak.image.tag`                                | Tag of the Keycloak image.                                                | -                             |
| `auth.auth-keycloak.importRealm`                              | Enables importing of realms during startup.                               | false                         |
| `auth.auth-keycloak.ingress`                                  | Ingress configuration for Keycloak.                                       | -                             |
| `auth.auth-keycloak.ingress.enabled`                          | Enables ingress for Keycloak.                                             | false                         |
| `auth.auth-keycloak.initialOrganizationId`                    | Initial organization ID for Keycloak.                                     | -                             |
| `auth.auth-keycloak.initialPassword`                          | Initial password for the default user.                                    | -                             |
| `auth.auth-keycloak.initialUsername`                          | Initial username for the default user.                                    | 'admin@myappcircle.io'        |
| `auth.auth-keycloak.organizationName`                         | Initial organization name in Keycloak.                                    | 'myappcircle'                 |
| `auth.auth-keycloak.recaptcha.maxFailures`                    | Maximum failed attempts before requiring a Recaptcha.                     | '4'                           |
| `auth.auth-keycloak.recaptcha.requirement`                    | Recaptcha requirement level (e.g., DISABLED, OPTIONAL, REQUIRED).         | 'DISABLED'                    |
| `auth.auth-keycloak.recaptcha.secret`                         | Secret key for Recaptcha integration.                                     | -                             |
| `auth.auth-keycloak.recaptcha.siteKey`                        | Site key for Recaptcha integration.                                       | -                             |
| `auth.auth-keycloak.userLookupDecisionStrategy`               | Strategy for user lookup decisions in Keycloak.                           | -                             |
| `auth.auth-postgresql.architecture`                           | Defines the architecture of PostgreSQL (e.g., standalone, replication).   | standalone                    |
| `auth.auth-postgresql.enabled`                                | Enables PostgreSQL for Keycloak.                                          | true                          |
| `auth.auth-postgresql.auth.username`                          | Username for the PostgreSQL database.                                     | 'keycloak'                    |
| `auth.auth-postgresql.auth.database`                          | The name of the PostgreSQL database to create.                            | 'keycloak'                    |
| `kafka.heapOpts`                                              | JVM heap options for Kafka.                                               | '-Xmx1408m -Xms512m'          |
| `kafka.controller.replicaCount`                               | Number of Kafka controller replicas.                                      | 3                             |
| `kafka.controller.resourcesPreset`                            | Resource preset for the Kafka controller.                                 | 'medium'                      |
| `kafka.controller.persistence.enabled`                        | Enables persistence for Kafka controller.                                 | true                          |
| `kafka.controller.persistence.size`                           | Size of persistence storage for Kafka controller.                         | '8Gi'                         |
| `kafka.listeners.client.protocol`                             | Protocol used for Kafka client listener.                                  | 'PLAINTEXT'                   |
| `kafka.listeners.controller.protocol`                         | Protocol used for Kafka controller listener.                              | 'PLAINTEXT'                   |
| `kafka.listeners.interbroker.protocol`                        | Protocol used for Kafka inter-broker communication.                       | 'PLAINTEXT'                   |
| `kafka.metrics.kafka.enabled`                                 | Enables Kafka metrics.                                                    | false                         |
| `kafka.metrics.jmx.enabled`                                   | Enables JMX metrics for Kafka.                                            | false                         |
| `kafka.zookeeper.auth.enabled`                                | Enables authentication for Zookeeper.                                     | false                         |
| `kafka.zookeeper.metrics.enabled`                             | Enables metrics for Zookeeper.                                            | false                         |
| `kafka.client.protocol`                                       | Protocol used by Kafka clients.                                           | 'PLAINTEXT'                   |
| `kafka.extraConfig`                                           | Additional configuration file for Kafka.                                  | -                             |
| `webeventredis.enabled`                                       | Enables Web Event Redis.                                                  | true                          |
| `webeventredis.tls.enabled`                                   | Enables TLS for Web Event Redis.                                          | false                         |
| `webeventredis.tls.existingSecret`                            | References an existing TLS secret for Web Event Redis.                    | 'appcircle-tls-wildcard'      |
| `webeventredis.tls.certCAFilename`                            | Filename for the CA certificate in TLS.                                   | 'ca.crt'                      |
| `webeventredis.tls.certFilename`                              | Filename for the server certificate in TLS.                               | 'tls.crt'                     |
| `webeventredis.tls.certKeyFilename`                           | Filename for the private key in TLS.                                      | 'tls.key'                     |
| `webeventredis.ingress.enabled`                               | Enables ingress for Web Event Redis.                                      | false                         |
| `webeventredis.ingress.tls`                                   | Enables TLS for Web Event Redis ingress.                                  | false                         |
| `webeventredis.ingress.ingressClassName`                      | Specifies the ingress class name for Web Event Redis.                     | `appcircle`                   |
| `webeventredis.ingress.annotations`                           | Annotations for Web Event Redis ingress.                                  | -                             |
| `minio.enabled`                                               | Enables Minio.                                                            | true                          |
| `minio.mode`                                                  | Minio mode (standalone, distributed, etc.).                               | 'standalone'                  |
| `minio.persistence.enabled`                                   | Enables persistence for Minio.                                            | true                          |
| `minio.persistence.size`                                      | Size of persistence storage for Minio.                                    | '8Gi'                         |
| `mongodb.enabled`                                             | Enables MongodB.                                                          | true                          |
| `mongodb.persistence.enabled`                                 | Enables persistence for MongodB.                                          | true                          |
| `mongodb.persistence.size`                                    | Size of persistence storage for MongodB.                                  | '5Gi'                         |
| `ingress-nginx.enabled`                                       | Specifies whether ingress-nginx is enabled.                               | true                          |
| `ingress-nginx.controller.ingressClassResource.name`          | Name of the IngressClass resource.                                        | appcircle                     |
| `ingress-nginx.controller.ingressClassResource.enabled`       | Specifies whether the IngressClass resource is enabled.                   | true                          |
| `ingress-nginx.controller.config.proxy-body-size`             | Maximum allowed size of the client request body.                          | "4096m"                       |
| `ingress-nginx.controller.config.proxy-connect-timeout`       | Timeout for establishing a connection to the backend server.              | "600"                         |
| `ingress-nginx.controller.config.proxy-read-timeout`          | Timeout for reading a response from the backend server.                   | "600"                         |
| `ingress-nginx.controller.config.client-header-timeout`       | Timeout for reading the client request headers.                           | "180"                         |
| `ingress-nginx.controller.config.client-body-timeout`         | Timeout for reading the client request body.                              | "180"                         |
| `ingress-nginx.controller.config.send-timeout`                | Timeout for sending data to the client.                                   | "180"                         |
| `ingress-nginx.controller.config.keepalive-timeout`           | Timeout for idle keep-alive connections.                                  | "75"                          |
| `ingress-nginx.defaultBackend.enabled`                        | Specifies whether the default backend is enabled.                         | false                         |
| `vault.injector.enabled`                                      | Enables the Vault sidecar injector.                                       | false                         |
| `vault.server.dataStorage.size`                               | Size of the data storage for Vault.                                       | '1Gi'                         |
| `vault.server.authDelegator.enabled`                          | Enables the auth delegator for Vault.                                     | false                         |
| `vault.server.image.repository`                               | Repository of the Vault server image.                                     | -                             |
| `vault.server.image.tag`                                      | Tag of the Vault server image.                                            | -                             |
| `vault.server.standalone.enabled`                             | Enables standalone mode for Vault.                                        | true                          |
| `vault.server.standalone.config`                              | Configuration file for standalone Vault.                                  | -                             |
| `vault.ui.enabled`                                            | Enables the Vault UI.                                                     | true                          |

<NeedHelp />
