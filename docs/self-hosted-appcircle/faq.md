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
