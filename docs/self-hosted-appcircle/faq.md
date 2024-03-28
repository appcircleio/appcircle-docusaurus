---
title: Troubleshooting & FAQ
metaTitle: Troubleshooting & FAQ
metaDescription: Troubleshooting & FAQ
sidebar_position: 4
---

# Overview

This section is designed to help you quickly find answers to common questions and provide you with a better understanding of Appcircle server and runner.

## Appcircle Server FAQ

### Can I change the password of the initial user?

For now, you shouldn't change the initial user password you defined in the `global.yaml`.

### Does Appcircle support LDAP login?

Appcircle supports LDAP login on the Testing Distribution and Enterprise App Store modules.

Appcircle doesn't support LDAP login on the Appcircle dashboard, where you login to create build profiles and other developer-related jobs.

### We can't send mail to outside domains.

Let's say your company's domain is `spacetech.com`. And you can send mail from Appcircle to `user@spacetech.com`, but you can't send mail to `user@gmail.com`.

You should check the SMTP configuration and allow SMTP server to send mail to outside domains.

### While installing the Appcircle server with Podman, `minio` containers can't get healthy status.

The podman network backend should be `netavark`. You can check the current settings with the command below:

```bash
podman info | grep -i networkBackend
```

If you need to use a proxy on the Appcircle server, you should configure proxy settings according to the [Proxy Configuration](/self-hosted-appcircle/configure-server/integrations-and-access/proxy-configuration) document.

### We are facing "manifest not found" error when we run the `up` command.

If you are using the Nexus registry and are facing a "manifest not found" error, this is an expected case to occur. Nexus proxy has a known bug while pulling multiple container images. You should pull images one by one as a workaround.

To pull images one by one, you can see the [Pulling Image One By One](./configure-server/external-image-registry.md#pulling-images-one-by-one) document. Then you can pull images one by one with this script. So you won't face "manifest not found" error any more.

### Where should we download the zip package while we are updating?

Download the zip package of the appcircle server and extract it to the same folder as the already existing Appcircle server folder. Your data and configuration will be saved while updating.

### How do I change Docker or Podman's data location?

For more details on changing the location of Docker data, refer to the [Change the Docker Data Location](/self-hosted-appcircle/install-server/docker.md#change-the-docker-data-location) page.

For more details on changing the location of Podman data, refer to the [Change the Podman Data Location](./install-server/podman.md#change-the-podman-data-location) page.

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
This operation needs **[reset](https://docs.appcircle.io/self-hosted-appcircle/install-server/docker#reset-configuration)** which deletes all your data like "Build Profiles", "Signing Identities", etc on the Appcircle server.
:::

:::tip
If you only want to change the URL of the **Testing Distribution** or **Enterprise App Store**, you should follow the [custom domain](/self-hosted-appcircle/configure-server/integrations-and-access/ssl-configuration#custom-domain) configuration document to assign a custom domain without resetting the Appcircle server.
:::

You can change the default subdomains as per your needs at the first installation time of the Appcircle server.

If you have already installed the Appcircle server and want to change the subdomains, you must **[reset](https://docs.appcircle.io/self-hosted-appcircle/install-server/docker#reset-configuration)** the server before applying a new configuration.

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

:::warning
If you have configured the Appcircle server as HTTPS, as an extra step, it may be required to change the SSL certificates in the `global.yaml` if they are not compatible with your new subdomains.

See the **[SSL configuration](/self-hosted-appcircle/configure-server/integrations-and-access/ssl-configuration)** document for details.
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

For details, you can see the [reset configuration](./install-server/docker.md/#reset-configuration) section in the documentation.
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

## Appcircle Runner FAQ

### We are facing a self-signed certificate error on builds.

The certificate of your organization should be trusted on the Appcircle runner virtual machines.

You should refer to the [Custom Certificates](./self-hosted-runner/configure-runner/custom-certificates.md) page for more details.

### We are facing an "SSL certificate is not valid yet" error on builds.

The runner VMs cannot connect to the servers to update their date and time due to network restrictions.

You should configure NTP server settings in the runner VMs. For updating base runners, please refer to the [Update Base Images](./self-hosted-runner/runner-vm-setup.md#update-base-images) section.

For details on configuring NTP settings, you can refer to the [NTP Configuration](./self-hosted-runner/runner-vm-setup.md#2-configure-base-runners-ntp-settings) section and follow the steps.

### We can't register Appcircle runner to the server.

First, you should check if your Appcircle runner can access the Appcircle server. You can run the command below to test this. You should change the example Appcircle URL for yourself.

```bash
curl -v https://api.appcircle.spacetech.com
```

You should check if there is a self-signed certificate problem. You can refer to the [Custom Certificates](./self-hosted-runner/configure-runner/custom-certificates.md) page to trust the root CA certificate of your organization.

If you already trusted the root CA cert, you should check the Appcircle server's certificate. If it is too long, like 5 years, it should be trusted using the graphical user interface. You should open the Keychain Access application from the GUI and add the Appcircle server's certificate. After that, you should click on the certificate and select "Always trust".

### We are facing "LoginName too long" error while running the `screen` command.

The `screen` command has a bug with long usernames which has been fixed in the new versions.

If you are facing this error while trying to run Appcircle runner VMs on a macOS host, you should update the `screen` tool on the host machine with `brew`.

You should follow the steps below to update the `screen` tool:

- Check the current version before updating.

```bash
screen --version
```

- Install the up-to-date version using Homebrew.

```bash
brew install screen
```

- Open a new terminal session to use the new `screen`.

:::caution
If you don't open a new terminal session, you cannot use the up-to-date `screen` since the current shell session has access to the older version.
:::

- Re-check the version to see if the update was done successfully.

```bash
screen --version
```
