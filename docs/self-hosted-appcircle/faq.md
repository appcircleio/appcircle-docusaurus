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

If you need to use a proxy on the Appcircle server, you should configure proxy settings according to the [Proxy Configuration](./configure-server/proxy-configuration.md) document.

### We are facing "manifest not found" error when we run the `up` command.

If you are using the Nexus registry and are facing a "manifest not found" error, this is an expected case to occur. Nexus proxy has a known bug while pulling multiple container images. You should pull images one by one as a workaround.

To pull images one by one, you can edit the script [here](./install-server/podman.md#mirroring-appcircle-images) and create a new shell script. Then you can pull images one by one with this script. So you won't face "manifest not found" error any more.

### Where should we download the zip package while we are updating?

Download the zip package of the appcircle server and extract it to the same folder as the already existing Appcircle server folder. Your data and configuration will be saved while updating.

### How do I change Docker or Podman's data location?

For more details on changing the location of Docker data, refer to the [Change the Docker Data Location](./install-server/docker.md#change-the-docker-data-location) page.

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

### How can we change the default sub-domains?

:::caution
This operation needs `reset` which deletes all your data like "Build Profiles", "Certificates" etc on Appcircle Server.
:::

You can change default subdomains as your needs at the first installation time of the Appcircle server.

If you have already installed the Appcircle server and want to change the subdomains, you can reset the data and move on.

For example, to change `my.appcircle.spacetech.com` to `my-appcircle.spacetech.com`, you can follow the step below:

- Go to the `appcircle-server` directory.

```bash
cd appcircle-server
```

:::info
`spacetech` is example project name. Please check your own project name from under the `./projects` directory.
:::

- If your server is up and running, down your project.

```bash
./ac-self-hosted.sh -n "spacetech" down
```

- Edit the `global.yaml` of your project for subdomains.

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
storeWeb:
  external:
    subdomain: store-appcircle
webEvent:
  external:
    subdomain: hook-appcircle
resource:
  domain: resource-appcircle
```

:::caution
If the keys are already exist in the `global.yaml`, you should just update or add the missing keys.

For example you must have `keycloak` key in the global.yaml already. You must just add the `keycloak.external.subdomain` section.
:::

- Edit the `global.yaml` of your project for the main domain.

```yaml
external:
  mainDomain: '.spacetech.com'
```

:::info

- After you change the main domain and the subdomains, you can merge them in your mind to find full domain.

- For example, in the example below:
  - Main domain: `.spacetech.com`
  - Web app domain: `my-appcircle`
  - So you will use `my-appcircle.spacetech.com` as full domain.

:::

- `reset`, `export` and `up` the Appcircle Server

The `reset` is optional, if you are installing for the first time (You must never have run the `up` command.), you don't the reset. You can continue with the `export` and the `up` commands.

For details, you can follow [Reset Configuration](./install-server/docker.md/#reset-configuration) section in the documentation.

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
