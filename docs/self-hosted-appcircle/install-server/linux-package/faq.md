---
title: Troubleshooting & FAQ for Appcircle Server and Runner
description: Troubleshooting and FAQ for Appcircle server and runner
tags: [troubleshooting, faq, self-hosted]
sidebar_position: 80
sidebar_label: Troubleshooting & FAQ
---

import DowntimeCaution from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/\_appcircle-server-downtime-caution.mdx';
import SpacetechExampleInfo from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/\_spacetech-example-info.mdx';
import RestartAppcircleServer from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/\_restart-appcircle-server.mdx';

# Overview

This section is designed to help you quickly find answers to common questions and provide you with a better understanding of Appcircle server and runner.

## Appcircle Server FAQ

### Can I change the password of the initial user?

For now, you shouldn't change the initial user password you defined in the `global.yaml`.

### Does Appcircle support LDAP login?

Appcircle supports LDAP login on the Testing Distribution and Enterprise App Store modules. For more details about enabling the LDAP, you can head over to the [Enterprise App Store](/account/my-organization/security/authentications/store-ldap-authentication) and [Testing Distribution](/account/my-organization/security/authentications/distribution-ldap-authentication) LDAP settings documents.

Appcircle also supports LDAP login on the Appcircle dashboard, where you log in to create build profiles and other developer-related jobs. For more details about enabling LDAP on the Appcircle dashboard, you can head over to the [Appcircle Login with LDAP](/self-hosted-appcircle/install-server/linux-package/configure-server/integrations-and-access/ldap-settings) document.

### We can't send mail to outside domains.

Let's say your company's domain is `spacetech.com`. And you can send mail from Appcircle to `user@spacetech.com`, but you can't send mail to `user@gmail.com`.

You should check the SMTP configuration and allow SMTP server to send mail to outside domains.

### While installing the Appcircle server with Podman, `minio` containers can't get healthy status.

The podman network backend should be `netavark`. You can check the current settings with the command below:

```bash
podman info | grep -i networkBackend
```

If you need to use a proxy on the Appcircle server, you should configure proxy settings according to the [Proxy Configuration](/self-hosted-appcircle/install-server/linux-package/configure-server/integrations-and-access/proxy-configuration) document.

### We are facing "manifest not found" error when we run the `up` command.

If you are using the Nexus registry and are facing a "manifest not found" error, this is an expected case to occur. Nexus proxy has a known bug while pulling multiple container images. You should pull images one by one as a workaround.

To pull images one by one, you can see the [Pulling Image One By One](./configure-server/external-image-registry#pulling-images-one-by-one) document. Then you can pull images one by one with this script. So you won't face "manifest not found" error any more.

### Where should we download the zip package while we are updating?

Download the zip package of the appcircle server and extract it to the same folder as the already existing Appcircle server folder. Your data and configuration will be saved while updating.

### How do I change Docker or Podman's data location?

For more details on changing the location of Docker data, refer to the [Change the Docker Data Location](/self-hosted-appcircle/install-server/linux-package/installation/docker#change-the-docker-data-location) page.

For more details on changing the location of Podman data, refer to the [Change the Podman Data Location](./installation/podman#change-the-podman-data-location) page.

### I'm offline on the Appcircle dashboard on my browser.

You should trust the Appcircle's or your organization's root CA certificate on your computer.

### We are getting the "potentially insufficient UIDs or GIDs" error while using Podman.

You should check the user ID and group ID of your current account.

```bash
id
```

The user ID and group ID should be four-digit numbers. (For example, 1000, 1002, etc.)

If your user ID and group ID are very large, you may get this error. In this case, you should create a new user and group with regular IDs.

### We want to change the Enterprise App Store custom domain. What should we do?

You can change the custom domain settings of Enterprise App Store from the `global.yaml` configuration file.

:::caution
We are assuming that you have installed the Appcircle server with version `3.11.0` or later for this operation.
:::

- Log in to the Appcircle server with SSH or a remote connection.

- Go to the `appcircle-server` directory.

```bash
cd appcircle-server
```

:::info

The `spacetech` in the example codes below are example project name.

Please find your own project name and replace `spacetech` with your project name.

To see projects, you can check the `projects` directory.

```bash
ls -l ./projects
```

:::

- Shutdown Appcircle server. Keep in mind that, this will cause downtime.

```bash
./ac-self-hosted.sh -n "spacetech" down
```

- Edit the `global.yaml` file of your project.

```bash
vi ./projects/spacetech/global.yaml
```

```yaml
storeWeb:
  customDomain:
    enabled: true
    domain: store.spacetech.com
```

:::caution
If the certificate of the custom store domain is not defined in the `global.yaml` file, the Enterprise App Store will listen on HTTP by default. It will not use the server-wide certificate defined in `.nginx.sslCertificate` for the Enterprise App Store.

To enable HTTPS for the Enterprise App Store, you must provide `.storeWeb.customDomain.publicKey` and `.storeWeb.customDomain.privateKey` values. For details, refer to the [SSL Configuration](/self-hosted-appcircle/install-server/linux-package/configure-server/integrations-and-access/ssl-configuration#custom-domain) docs.
:::

- Apply configuration changes.

```bash
./ac-self-hosted.sh -n "spacetech" export
```

- Boot Appcircle server.

```bash
./ac-self-hosted.sh -n "spacetech" up
```

:::tip
You should check the status of the Appcircle server after boot for any possible errors.

```bash
./ac-self-hosted.sh -n "spacetech" check
```

:::

Now you can access the Enterprise App Store with the new store domain settings.

### How can we change the default sub-domains?

:::caution
This operation needs **[reset](https://docs.appcircle.io/self-hosted-appcircle/install-server/linux-package/installation/docker#reset-configuration)** which deletes all your data like "Build Profiles", "Signing Identities", etc on the Appcircle server.
:::

:::tip
If you only want to change the URL of the **Testing Distribution** or **Enterprise App Store**, you should follow the [custom domain](/self-hosted-appcircle/install-server/linux-package/configure-server/integrations-and-access/ssl-configuration#custom-domain) configuration document to assign a custom domain without resetting the Appcircle server.
:::

You can change the default subdomains as per your needs at the first installation time of the Appcircle server.

If you have already installed the Appcircle server and want to change the subdomains, you must **[reset](https://docs.appcircle.io/self-hosted-appcircle/install-server/linux-package/installation/docker#reset-configuration)** the server before applying a new configuration.

For example, to change `my.appcircle.spacetech.com` to `my-appcircle.spacetech.com` along with other subdomains, you should follow the steps below:

- Go to the `appcircle-server` directory.

```bash
cd appcircle-server
```

:::info
The `spacetech` in the example codes below is an example project name.

Please find your own project name and replace `spacetech` with your project name.

To see projects, you can check the `projects` directory.

```bash
ls -l ./projects
```

:::

- Edit the `global.yaml` of your project for subdomain changes.

```bash
vi ./projects/spacetech/global.yaml
```

```yaml
keycloak:
  external:
    subdomain: auth-appcircle
webApp:
  external:
    subdomain: my-appcircle
apiGateway:
  external:
    subdomain: api-appcircle
testerWeb:
  external:
    subdomain: dist-appcircle
webEvent:
  external:
    subdomain: hook-appcircle
minio:
  external:
    subdomain: resource-appcircle
storeWeb:
  external:
    subdomain: store-appcircle
webEventRedis:
  external:
    subdomain: redis-appcircle
grafana:
  external:
    subdomain: monitor-appcircle
```

:::caution
If the keys already exist in the `global.yaml`, you should just update or add the missing keys.

For example, if you already have the `keycloak` key in global.yaml, you must just add the `keycloak.external.subdomain` section there.
:::

- Edit the `mainDomain` of your project in the `global.yaml` file.

```yaml
external:
  mainDomain: ".spacetech.com"
```

:::caution
The subdomains will be concatenated to the **`mainDomain`**.

For this reason, `external.mainDomain` in the configuration file must always begin with a `.` character as a prefix.
:::

:::tip

After you change the main domain and the subdomains, you can merge them yourself to see the up-to-date URLs for Appcircle modules.

For example;

- when `mainDomain` is `.spacetech.com`
- and `webApp` `subdomain` is `my-appcircle`

then the Appcircle dashboard URL will be `my-appcircle.spacetech.com`.
:::

:::danger
If you have configured the Appcircle server as HTTPS, as an extra step, it may be required to change the SSL certificates in the `global.yaml` if they are not compatible with your new subdomains.

See the **[SSL configuration](/self-hosted-appcircle/install-server/linux-package/configure-server/integrations-and-access/ssl-configuration)** document for details.
:::

When the `global.yaml` changes are ready to apply, follow the below steps:

- Stop the server.

```bash
./ac-self-hosted.sh -n "spacetech" down
```

- Cleanup server data.

```bash
./ac-self-hosted.sh -n "spacetech" reset
```

:::info
The `reset` step is optional. If you are installing for the first time, which means that you have never run the `up` command and used the system, then you don't need to cleanup anything.

For details, you can see the [reset configuration](./installation/docker#reset-configuration) section in the documentation.
:::

- Apply the configuration changes.

```bash
./ac-self-hosted.sh -n "spacetech" export
```

- Start the server.

```bash
./ac-self-hosted.sh -n "spacetech" up
```

- Check the health of the services.

```bash
./ac-self-hosted.sh -n "spacetech" check
```

You should see the message: _"All services are running successfully."_

### While connecting to a repository from GitLab, we can list the projects, but binding is failing.

The first thing you should check is **PAT** permissions.

If you are sure that **PAT** has the required permissions, you should check the **Outbound Requests** configuration of your GitLab server.

For more details about configuring the outbound requests, you can refer to the [Outbound Requests](/build/manage-the-connections/adding-a-build-profile/connecting-to-gitlab#outbound-requests) section.

### What should be done after upgrading the hardware resources (CPU & memory) of the Appcircle server?

When you upgrade the hardware resources (CPU & memory) of the Appcircle server, it's important to update the **resource limits** accordingly.

Appcircle sets these limitations with the `export` command and configures CPU and memory limits for the services. If you don't run the `export` command again after updating the CPU and memory of the Appcircle host machine, the Appcircle services will continue to use the old resource limits.

To ensure the new resource limits are applied, follow these steps:

<DowntimeCaution />

- Log in to the Appcircle server with SSH or a remote connection.

- Go to the `appcircle-server` directory.

```bash
cd appcircle-server
```

<SpacetechExampleInfo/>

<RestartAppcircleServer />

### How can we restrict the TLS versions used by the Appcircle server?

To restrict the TLS versions used by the Appcircle server, you can follow the [Configure TLS Versions](/self-hosted-appcircle/install-server/linux-package/configure-server/integrations-and-access/ssl-configuration#configure-tls-versions) section in the **SSL Configuration** documentation.
