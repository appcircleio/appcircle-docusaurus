---
title: Helm for Kubernetes
description: Learn how to install and configure self-hosted Appcircle server with Helm to Kubernetes
tags: [self-hosted, helm, installation, configuration]
sidebar_position: 6
---

import HelmYamlGenerator from '@site/src/components/HelmYamlGenerator';

## Overview

To deploy the Appcircle server on your Kubernetes cluster, use the Appcircle Helm chart. This chart includes all the necessary components for the initial setup and can scale to support larger deployments.

For a production deployment, a basic understanding of Kubernetes is sufficient. This knowledge will help you effectively manage and troubleshoot the cluster, optimize resource allocation, and maintain security.

## Prerequisites

### Domain Name

A main domain name, for which you can generate SSL/TLS certificates for several subdomains, is required for the Appcircle server. In this documentation, we will use `appcircle.spacetech.com` as an example main domain and `spacetech` as an example organization name.

By default, Appcircle uses eight subdomains. These subdomains are:

1. api.appcircle.spacetech.com
2. auth.appcircle.spacetech.com
3. dist.appcircle.spacetech.com
4. hook.appcircle.spacetech.com
5. resource.appcircle.spacetech.com
6. store.appcircle.spacetech.com
7. my.appcircle.spacetech.com
8. redis.appcircle.spacetech.com

TODO: Maybe add the monitor domain.

Upon completing the deployment of the Appcircle server, you will need to create DNS records based on the ingress objects defined in Kubernetes. This should be done through your DNS service provider to ensure proper routing and accessibility.

### SSL/TLS Certificate

Modern technologies and best practices require secure communication to protect data from potential threats and ensure user privacy. Therefore, deploying the Appcircle server with an SSL/TLS certificate is essential.

Ensure the certificate covers the main domain and all relevant subdomains outlined in the [domain name](#domain-name) section, safeguarding data integrity and confidentiality.

Additionally, configure the Appcircle server with a fullchain certificate, which should include the leaf (or app) certificate, intermediate certificates, and the root certificate, establishing a complete and trusted certificate chain.

### Kubernetes cluster

To install the Appcircle server using Helm, a Kubernetes cluster is required. The cluster must meet the following hardware specifications:

**Minimum hardware requirements for an enterprise installation:**

- Nodes with x86-64 architecture
- 8 CPUs
- 16 GB RAM
- TODO: Update 500 GB SSD

**Recommended hardware requirements for production environments:**

- Nodes with x86-64 architecture
- 32 CPUs
- 64 GB RAM
- TODO: Update 1 TB SSD

TODO: Define a kubernetes version

Kubernetes version must be x.x.x or later.

### kubectl

Install `kubectl` by following the instructions provided in [the Kubernetes documentation](https://kubernetes.io/docs/tasks/tools/#kubectl). Ensure that the installed version is within one minor release of the version running on your cluster.

The `kubectl` should be configured for the target Kubernetes cluster.

### Helm

Install Helm version 3.11.0 or later by following the instructions in [the Helm documentation](https://helm.sh/docs/intro/install/).

### Kubernetes Ingress Controller

By default, Appcircle exposes its services using name-based virtual servers, which are configured through Ingress objects. To ensure these Ingress objects function properly, your Kubernetes cluster must have an Ingress Controller installed and configured.

Appcircle server supports Nginx Ingress Controller by default. To install Nginx Ingress Controller to the Kubernetes cluster, please check [the Nginx Ingress Controller documentation](https://kubernetes.github.io/ingress-nginx/deploy/#installation-guide).

#### Enable SSL Passthrough

SSL passthrough allows SSL traffic to pass through a load balancer without decrypting it. The SSL/TLS termination is done at the backend server, not at the load balancer.

Redis ingress of the Appcircle server needs SSL passthrough so Appcircle runners can connect to the Redis service that is working on Kubernetes cluster securely.

Enabling the SSL passthrough depends on the ingress controller that is used in the Kubernetes cluster. For example:

- For Nginx Ingress Controller, check [the Nginx documentation](https://kubernetes.github.io/ingress-nginx/user-guide/tls/#ssl-passthrough).

  - In a summary, should edit the Nginx controller deployment and add the `--enable-ssl-passthrough` flag to the `args` section.

- @TODO: should be reviewed and tested to see if we support HAProxy-> For HAProxy Ingress Controller, check [the HAProxy documentation](https://www.haproxy.com/documentation/kubernetes-ingress/community/configuration-reference/ingress/#ssl-passthrough).
- @TODO: should be reviewed and tested to see if we support Traefik-> For Traefik Ingress Controller, check [the Traefik documentation](https://traefik.io/blog/https-on-kubernetes-using-traefik-proxy/).

:::info
Enabling the SSL passthrough option **does not** automatically allow all SSL traffic **from all ingress objects** to pass through to the original service. Instead, it enables Ingress resources to leverage the SSL passthrough feature, allowing encrypted traffic to reach the backend service without being decrypted by the Ingress Controller.
:::

### Create a Configuration File

To configure Helm, you can create a `global.yaml` file by specifying your desired settings, which are commonly used across all deployments.

We will reference this configuration file as `global.yaml` for the rest of this documentation.

:::caution
Please review the information for the input boxes below. If the values provided are incompatible, the installation may not complete successfully. Ensure that all configurations are correctly entered to avoid potential issues during the setup process.
:::

:::info
In the example values below, we used `spacetech` as an example organization name. You should replace it with your actual organization name or any other value you prefer.
:::

#### Appcircle General Settings

- `The Organization Name`: Enter your organization's name.
- `Appcircle Main Domain`: Specify the [domain name](#domain-name) that will host nine subdomains. Ensure the domain is properly configured and can handle subdomain creation as required.
- `Appcircle Initial User Email`: Provide the admin email address for the Appcircle server. It is recommended to use an email address that exists and can receive emails for password reset purposes.
- `Appcircle Initial User Password`: Set the password for the initial user. The password must adhere to the Appcircle password policy:
  - Minimum length of 6 characters.
  - At least one lowercase letter.
  - At least one uppercase letter.
  - At least one numeric digit.

---

#### Container Image Registry Settings

- `Container Registry Host`: Enter the domain or IP address of your container image registry, such as Harbor or Nexus, if using an external image registry.
- `Container Image Repository Path`: Specify the path of the container images. This is typically the segment between your registry host and the image name. For example, in the image path `registry.spacetech.com/appcircle-proxy/image:tag`, the repository path is `appcircle-proxy`.
- `Container Image Tag`: (Consider removing if unnecessary) Specify the version of the Appcircle server, such as `v3.23.1`, `latest`, or `beta-latest`.
- `Container Image Registry Requires Authentication`: Select this option if the container image registry requires authentication.
- `Container Image Registry Username`: For the default image registry, use `_json_key` as the username.
- `Container Image Registry Password`: Enter the content of the `cred.json` file, which you must obtain from Appcircle, for the default image registry.

:::tip
You don't need to change `Container Image Registry Host, Path and Tag` settings if you are not using an external container image registry.
:::

---

#### SMTP Settings

Appcircle needs an SMTP server to send emails for operations such as user authorization, Testing Distribution, notification emails.

- `SMTP Host`: Domain or IP address of the SMTP server.
- `SMTP Port`: Port number of the SMTP server.
- `SMTP SSL/TLS`: Set to 'true' if the SMTP server uses SSL/TLS protocol for secure communication, typically on port 465.
- `SMTP StartTLS`: Set to 'true' if the SMTP server uses StartTLS protocol for upgrading an unencrypted connection to a secure one, typically on port 587.
- `SMTP Send Emails From`: Email address that Appcircle will send emails from.
- `SMTP Server Requires Authentication`: Should be 'true' if the SMTP server requires authentication. False for otherwise.
- `SMTP Username`: SMTP username for authentication if the `auth` is set to 'true'. You can leave the value empty if the `auth` is false.
- `SMTP Password`: SMTP password for authentication if the `auth` is set to 'true'. You can leave the value empty if the `auth` is false.

:::tip
For most cases, `SMTP SSL/TLS` and `SMTP StartTLS` can't be `true` at the same time.
:::

:::info
If you are not using secure connections for SMTP communication, you should set both `SMTP SSL/TLS` and `SMTP StartTLS` to 'false'.
:::

---

#### Configure the SSL/TLS Certificates

With the example configuration, Appcircle configures the ingress objects with SSL/TLS certificates so the client that connect to Appcircle uses HTTPS instead of HTTP.

  - `Appcircle SSL/TLS Certificate File`: Should be the public certificate of the SSL/TLS certificate. It is best practice to use fullchain certificates (including intermediate certificates) instead of single certificates.
  - `Appcircle SSL/TLS Private Key File`: Should be the private key of the SSL/TLS certificate.
  - `Appcircle CA Certificate File`: Should be the Certificate Authority public key. Typically the bottom certificate of your fullchain certificate. If you are using a single certificate instead of a full chain certificate, `Appcircle CA Certificate File` should be that single certificate.

---

#### Generate the Configuration File

<HelmYamlGenerator />

Click the `Generate YAML` button to create a pre-configured YAML file. After the YAML is generated, copy its content and save it as a file named `global.yaml` in the directory where you will execute the Helm commands.

## Deploy Using Helm

Once you have gathered all the necessary configuration options, you can proceed with getting the Helm repository of the Appcircle and deploying the Appcircle server. In this example, we will use `appcircle-server` as Helm release name and install the Appcircle server into the `appcircle` namespace.

TODO: The repository is not working for now. You should package the helm repository manually, or get it from Appcircle team. The `helm upgrade --install` commands works with the helm package from a local file.
- Add the Appcircle Helm repository.

```bash
helm repo add appcircle https://charts.appcircle.io/ && \
helm repo update
```

- Use the configured `global.yaml` file to install the Appcircle Helm chart to your Kubernetes cluster.

```bash
helm upgrade --install appcircle-server appcircle/appcircle-server \
  --timeout 1200s \
  -n appcircle --create-namespace \
  -f global.yaml
```

Please note that the release name must be 18 characters or fewer.

The installation process duration depends on factors such as network speed and the processing power of your Kubernetes nodes. Typically, the installation may take between 10 to 15 minutes.

You can use `watch` command on a second terminal on Linux/MacOS systems to watch the pod creation process by running:

```bash
watch kubectl get pods -n appcircle
```

If you want to make sure that all containers are ready to use, you can the `kubectl wait` command on a third terminal window. The `appcircle` in the command is the Helm release name. So if you have changed the release name in the installation process, change the command according to your release name.

```bash
kubectl wait --for=condition=ready pod -l app.kubernetes.io/instance=appcircle-server -n appcircle --timeout 1200s
```

When all the pods are ready, the command will return with success. You are ready to connect to the Appcircle UI and start to discover.

## Create DNS Records

After the Appcircle server installation is finished, you can get the IP addresses of the Appcircle domains and configure the DNS.

You can list the ingresses with `kubectl` to check the IP address of the Appcircle services domains.

```bash
kubectl get ingresses -n appcircle
```

```bash
NAME                               CLASS   HOSTS                                                          ADDRESS                                     PORTS   AGE
appcircle-apigateway               nginx   api.appcircle.spacetech.com,auth.appcircle.spacetech.com       192.168.1.245,192.168.1.246,192.168.1.247   80      24m
appcircle-distribution-testerweb   nginx   dist.appcircle.spacetech.com                                   192.168.1.245,192.168.1.246,192.168.1.247   80      24m
appcircle-resource                 nginx   resource.appcircle.spacetech.com                               192.168.1.245,192.168.1.246,192.168.1.247   80      24m
appcircle-store-web                nginx   *.store.appcircle.spacetech.com                                192.168.1.245,192.168.1.246,192.168.1.247   80      24m
appcircle-web-app                  nginx   my.appcircle.spacetech.com                                     192.168.1.245,192.168.1.246,192.168.1.247   80      24m
appcircle-web-event                nginx   hook.appcircle.spacetech.com                                   192.168.1.245,192.168.1.246,192.168.1.247   80      24m
appcircle-webeventredis            nginx   redis.appcircle.spacetech.com                                  192.168.1.245,192.168.1.246,192.168.1.247   80      24m
```

You should configure your DNS records according to your DNS provider. For a best practice, create a `A` record for the `my.appcircle.spacetech.com` and create `CNAME` records for other domains.

## Sign in to Appcircle

You can use the `my` prefixed domain name to access Appcircle dashboard. For example, if you set `global.urls.domainName` to `.appcircle.spacetech.com` then you should use `my.appcircle.spacetech.com` address.

After you see the login page of the Appcircle, you can now use the initial username and password to login to the Appcircle dashboard. You can check the initial username and password from the `global.yaml` file that you have used to install Appcircle server. The values you should look for are under `auth.auth-keycloak.initialUsername` and `auth.auth-keycloak.initialPassword` keys.

## Uninstall the Appcircle Server

If you want to uninstall the Appcircle server, you can just remove the Helm release from the Kubernetes cluster.

If you haven't changed the release name and namespace name while following the [Deploy Using Helm](#deploy-using-helm) section, you can run the command below to uninstall the Appcircle server.

```bash
helm uninstall -n appcircle appcircle-server
```

## Deleting the Appcircle Server Data

(TODO: Validate the information. Uninstall and install then check if the data still exists.) [Uninstalling the Appcircle Server](#uninstall-the-appcircle-server) doesn't delete the Appcircle server data. If you want to delete all the data of the Appcircle server for a reason, you can simple delete the namespace.

If you haven't changed the namespace name while following the [Deploy Using Helm](#deploy-using-helm) section, you can run the command below to delete the all data of the Appcircle server.

```bash
kubectl delete namespace appcircle
```

## Production Readiness

By default, Appcircle Helm chart will deploy all the required services to the Kubernetes cluster for testing purposes. It is recommended that stateful applications, such as databases or object storage, be deployed outside the scope of the Helm chart. This allows you to have better control over their configuration and management.

If you wish to deploy these services within the Helm chart scope, you can use the default configuration provided by the Appcircle Helm chart.

### PostgreSQL

The Appcircle chart, by default, includes an in-cluster PostgreSQL deployment provided by `bitnami/PostgreSQL`. This deployment is intended for testing and evaluation purposes only, and is not recommended for production environments.

For a production-ready setup, it is essential to configure an external PostgreSQL instance. The recommended version is PostgreSQL 16.

If you are deploying the Appcircle server for testing purposes, you may use the built-in PostgreSQL deployment.

### MongoDB

By default, the Appcircle chart includes an in-cluster MongoDB deployment provided by `bitnami/mongodb` by default. This deployment is intended for testing and evaluation purposes only, and is not recommended for production environments.

To ensure optimal performance and reliability in a production environment, it is recommended to set up an external, production-grade MongoDB instance. The recommended version is MongoDB 7.0.

If you are deploying the Appcircle server for testing purposes, the built-in MongoDB deployment can be used.

### MinIO

By default, the Appcircle chart includes an in-cluster MinIO deployment provided by @TODO: change -> `stable/minio`. This deployment is intended for testing and evaluation purposes only, and is not recommended for production environments.

For production environments, it is highly recommended to configure an external, production-grade MinIO instance to ensure scalability, high availability, and data durability. TODO: Add minimum MinIO version.

If you are installing the Appcircle for testing purposes, you may use the built-in MinIO deployment.

### Kafka

By default, the Appcircle chart includes an in-cluster Kafka deployment provided by `bitnami/kafka`. This deployment is intended for testing and evaluation purposes only, and is not recommended for production environments.

For production deployments, you should set up an external, production-ready Kafka cluster to handle high-throughput messaging and ensure proper fault tolerance and scaling. TODO: Add minimum Kafka version.

If you are installing the Appcircle for testing purposes, you may use the built-in Kafka deployment.

#### HashiCorp Vault

By default, the Appcircle chart includes an in-cluster HashiCorp Vault deployment provided by `hashicorp/vault`. This deployment is intended for testing and evaluation purposes only, and is not recommended for production environments.

For production, you should configure an external, production-grade Vault instance to ensure robust secret management, scalability, and high availability. TODO: Add minimum HashiCorp Vault version.

If you are deploying the appcircle for testing purposes, the built-in Vault deployment can be used.

## Update the Configuration File

Although the `Generate YAML` button above generates a `yaml` file that you can use when deploying the Appcircle server to Kubernetes, there are some configurations in this file that you may want to add manually.

If there are any settings you want to configure, open the `global.yaml` with your favorite editor like `vi`, `VS Code` or `notepad` and follow the sections below.

```bash
vi global.yaml
```

TODO: Move to another page
### Configure External Stateful Apps

If you are deploying the Appcircle server for production, you should have stateful apps outside of the Kubernetes cluster. You can skip this section if you are deploying the Appcircle server for test environments.

@TODO: Fill here.


### Adding Trusted CA Certificates to the Appcircle Services

If any services that the Appcircle server needs to connect to, such as your Git provider, use a self-signed SSL/TLS certificate or a certificate issued by an untrusted root CA from your organization, Appcircle will refuse the connection by default.

:::tip
To prevent potential issues with untrusted certificates, it is recommended to add your organization's root certificate from the Certificate Authority (CA) to Appcircle. This ensures that the server can properly validate and trust SSL/TLS certificates issued by your organization’s CA.
:::

To add this certificates as trusted, you need to update the `.global.trustedCerts` key in the `global.yaml` file and import the certificates.

:::info
The `.global` key already exists in your `global.yaml` file. You just need to add the `trustedCerts` key.
:::

The trusted certificate names must conform to the regex pattern `[-._a-zA-Z0-9]+`. It is recommended to use descriptive names for your certificates, such as `spacetech-root` for the root certificate and `spacetech-intermediate` for the intermediate certificate.

Here is an example of how to update the `global.yaml` file:

(TODO: Multiple certificate should be tested.)

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
TODO: Move to another page
### Configure Max Body Size

In Appcircle, there are scenarios where the client upload size might exceed the default limit of 4096MB for a single request body size. To accommodate larger file uploads or if you wish to adjust this setting according to your needs, you can configure the maximum allowed body size in your `global.yaml` file.

```yaml
# For APK, IPA, build artifact uploads from browsers and Appcircle runners
apigateway:
  ingress:
    annotations:
      nginx.ingress.kubernetes.io/proxy-body-size: 1024m

# For build cache uploads from Appcircle runners
resource:
  ingress:
    annotations: 
      nginx.ingress.kubernetes.io/proxy-body-size: 1024m
```

### Git Providers

With default installation, self-hosted Appcircle comes with the connection options below:

- Bitbucket
- Azure
- GitLab
- Connect via SSH
- Connect via URL

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2031-git-providers-v2.png' />

If you want to enable or disable any of these providers, you can do so by updating your `global.yaml` file.

In the example below, there are enabled git providers list with comma separated:

```yaml
web:
  web-app:
    selfHostedGitProviders: "bitbucketServer,azureDevopsServer,gitlabSelfHosted,ssh,publicRepository"
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

To configure LDAP lookup decision settings, you can edit the `global.yaml` file and add the following settings under `auth`:

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

TODO: Get overview from the [original document](/docs/self-hosted-appcircle/configure-server/advanced-configuration/ldap-brutefore.md).

To configure LDAP brute force protection, you can edit the `global.yaml` file and add the following settings under `auth`:

```yaml
auth:
  auth-keycloak:
    bruteForce:
      distribution: 
        maxFailureCount: '5'
        maxLockDuration: '600'
      store: 
        maxFailureCount: '5'
        maxLockDuration: '600'
```

### Increase the Replica Counts

With the default Helm values, the Appcircle server services being deployed with one replica. If you want to increase this number for high availability, you can do so by updating your `global.yaml` file:

:::caution
Some keys might already exists in your `global.yaml` file, make sure to update the existing keys instead of adding new ones.
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

## Troubleshooting & FAQ

### When we try to login to the Appcircle server, we see `too many redirects` error from browser

This error usually happens when the pods can't resolve some of [the Appcircle server domains](#domain-name).

For the solution, please make sure that the domain name server of the worker nodes of the Kubernetes cluster can resolve the Appcircle server domain names.

### When we deploy the Helm chart, the `appcircle-server-webeventredis-master-0` pod is stuck in `CrashLoopBackOff` state

This error usually happens when you select a non-valid `Appcircle CA Certificate File` while [generating the configuration file](#generate-the-configuration-file). Please make sure that the certificate you choose is the **root** certificate of the full-chain certificate.

:::tip

If you created the SSL/TLS certificate with LetsEncrypt, you should know that the `fullchain.pem` file doesn't include the root CA certificate by default. 

:::

To fix the problem, you can edit the `global.yaml` file and upgrade the Helm chart. 

```bash
helm upgrade appcircle-server appcircle/appcircle-server \
  --timeout 1200s \
  -n appcircle \
  -f global.yaml
```

:::caution
The `stateful` pods won't be recreated from a error state. This is known issue of Kubernetes.

You should delete the pods manually to fix this problem. The new updated pods will be created automatically. You can use the example commands below to delete the pods:

```bash
kubectl delete pods appcircle-server-webeventredis-master-0 -n appcircle && \
kubectl delete pods appcircle-server-webeventredis-replicas-0 -n appcircle && \
kubectl delete pods appcircle-server-webeventredis-replicas-1 -n appcircle
```
:::

