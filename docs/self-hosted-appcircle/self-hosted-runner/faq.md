---
title: Troubleshooting & FAQ for Appcircle Runner
description: Troubleshooting and FAQ for Appcircle runner
tags: [troubleshooting, faq, self-hosted]
sidebar_position: 60
sidebar_label: Troubleshooting & FAQ
---


## Appcircle Runner FAQ

### We are facing a self-signed certificate error on builds.

The certificate of your organization should be trusted on the Appcircle runner virtual machines.

You should refer to the [Custom Certificates](/self-hosted-appcircle/self-hosted-runner/configure-runner/custom-certificates) page for more details.

### We are facing an "SSL certificate is not valid yet" error on builds.

The runner VMs cannot connect to the servers to update their date and time due to network restrictions.

You should configure NTP server settings in the runner VMs. For updating base runners, please refer to the [Update Base Images](/self-hosted-appcircle/self-hosted-runner/runner-vm-setup#update-base-images) section.

For details on configuring NTP settings, you can refer to the [NTP Configuration](/self-hosted-appcircle/self-hosted-runner/runner-vm-setup#2-configure-base-runners-ntp-settings) section and follow the steps.

### We can't register Appcircle runner to the server.

First, you should check if your Appcircle runner can access the Appcircle server. You can run the command below to test this. You should change the example Appcircle URL for yourself.

```bash
curl -v https://api.appcircle.spacetech.com
```

You should check if there is a self-signed certificate problem. You can refer to the [Custom Certificates](/self-hosted-appcircle/self-hosted-runner/configure-runner/custom-certificates) page to trust the root CA certificate of your organization.

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
