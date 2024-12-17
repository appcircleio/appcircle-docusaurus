---
title: Pre-Installation Checklist
description: Checklist to be followed before installing the self-hosted Appcircle
tags: [self-hosted, installation, checklist]
sidebar_position: 2
---

This page provides a checklist to be followed before installing the self-hosted Appcircle.

Please ensure all the checks are completed for a smooth installation process.

## Server Checklist

### Check the Operating System

- [ ] If you are using RHEL, it should be **RHEL 8 or later**.

```bash
cat /etc/redhat-release
```

- [ ] If you are using Ubuntu, it should be **Ubuntu 20.04 or later**.

```bash
cat /etc/os-release
```

- [ ] If you are using Debian, it should be **Debian 11 or later**.

```bash
cat /etc/os-release
```

- [ ] If you are using CentOS, it should be **CentOS 8 or later**.

```bash
cat /etc/centos-release
```

### Check the CPU Cores

- [ ] Minimum CPU core count should be **8 cores**.
  - For enterprise installations and production environments, **16 or 32 CPU cores** are recommended.

```bash
nproc --all
```

### Check the CPU Architecture

- [ ] The CPU architecture must be **x86_64**.

```bash
uname -i
```

If the command above doesn't work, you can try the command below.

```bash
arch
```

### Check the RAM Size

- [ ] Minimum RAM size should be **16 GB**.
  - For enterprise installations and production environments, **32 GB or 64 GB of RAM** is recommended.

```bash
free -h
```

### Check the Disk Size

- [ ] Minimum disk size should be **500 GB**.
  - For enterprise installations and production environments, **1 TB of disk space** is recommended.

```bash
df -h
```

:::info
Keep in mind that **SSDs** are a better and **recommended** choice for faster disk operations.
:::

### Check the Swap Size

- [ ] The swap size should be minimum half of the RAM size.

```bash
free -h
```

If you don't have any swap space or it's insufficient, you can find the configuration details [here](docker#swap).

### Check the Swappiness

- [ ] The swappiness configuration should be **10**.

```bash
sudo cat /proc/sys/vm/swappiness
```

If the output is not 10, you can find the configuration details [here](docker#swappiness).

### Configure the DNS Settings

- [ ] Create a subdomain under your company's primary domain name.

For example, if your company is "Spacetech" with the domain `spacetech.com`, you can create a subdomain like `appcircle.spacetech.com` or `appcircle-test.spacetech.com` to assign to the Appcircle server.

It will be the **main domain** for the self-hosted Appcircle server.

The main domain (`appcircle.spacetech.com`, for instance.) should have seven subdomains which should resolve to the IP address of the Appcircle server.

These subdomains are **api**, **auth**, **dist**, **hook**, **my**, **resource** and **store**.

- [ ] Create these seven domain name entries on your DNS.

  - [ ] `api.appcircle.spacetech.com`
  - [ ] `auth.appcircle.spacetech.com`
  - [ ] `dist.appcircle.spacetech.com`
  - [ ] `hook.appcircle.spacetech.com`
  - [ ] `my.appcircle.spacetech.com`
  - [ ] `resource.appcircle.spacetech.com`
  - [ ] `store.appcircle.spacetech.com`
  - [ ] `monitor.appcircle.spacetech.com`
  - [ ] `redis.appcircle.spacetech.com`

- [ ] All of these domain names should resolve to the same server IP address, which is the Appcircle server.

You can see details in the [DNS Settings](/self-hosted-appcircle/install-server/docker#4-dns-settings) section.

### Obtain an SSL Certificate

- [ ] You should create only one SSL certificate that covers all seven domain names which you have seen in the [Configure DNS](#configure-the-dns-settings) section above.
- [ ] The SSL certificate should be in PEM format.
- [ ] The SSL certificate private key must not have a passphrase.
- [ ] Obtain the root CA certificate of your company.
- [ ] Obtain the intermediate CA certificate of your company if it exists.

### Obtain the SMTP Settings

- [ ] Obtain the IP address or host name of the SMTP server.
- [ ] Obtain the port number of the SMTP server.
- [ ] Determine if the SMTP server is using `SSL`.
- [ ] Determine if the SMTP server is using `STARTTLS`.
  - :warning: `SSL` and `STARTTLS` are **not** the same thing.
- [ ] Determine if the SMTP server requires SSL certificate verification.
  - ✨ Appcircle server version `3.23.1` or later supports disabling the certificate verification if you have problems with the SMTP server certificate and need a workaround for certificate errors while troubleshooting.
  - ⚠️ It's **not recommended to disable** the SSL certificate verification in production environments.
- If the SMTP server requires authentication:
  - [ ] Create a user for Appcircle on the SMTP server.
  - [ ] Obtain the password of the Appcircle user on the SMTP server.
- [ ] Contact the system admin to get required permissions to send email with the Appcircle user via the SMTP server.
- [ ] Create a firewall rule (or permission) from the Appcircle server to the SMTP server.

### Configure the Git Server

- [ ] Import Appcircle Android and/or iOS sample repositories on your local git server.
  - [ ] [Android Sample Repo](https://github.com/appcircleio/appcircle-sample-android)
  - [ ] [iOS Sample Repo](https://github.com/appcircleio/appcircle-sample-ios)
- [ ] Create an Appcircle user on the git server (GitLab, Azure DevOps, Bitbucket).
- [ ] Give the required permissions to the Appcircle user to clone and edit the repositories.
- If you are using GitLab, Azure DevOps, Bitbucket:
  - [ ] Create an Appcircle user. Give it permissions for the repositories.
  - [ ] Create a personal access token that has sufficient permissions.
    - For details like token permissions, check the [connect your repository](/build/manage-the-connections/adding-a-build-profile#connect-your-repository) section.
- If you are using any other git server:
  - [ ] Create a public-private SSH key pair.
  - [ ] Configure your Appcircle git user's public SSH keys and upload the public SSH key you created.
    - For details, you can check the [connect via SSH](/build/manage-the-connections/adding-a-build-profile/connecting-to-private-repository-via-ssh) section.
- [ ] Create a firewall rule (or permission) between the Appcircle server and the git server in both directions.

### Network Access for Installation

According to the selected Linux distribution and installation method, you need to configure firewall rules (or permissions) for the Appcircle server. All required domains that are used for installation are detailed in the [network access](/self-hosted-appcircle/configure-server/integrations-and-access/network-access) section.

- [ ] Review the [network access](/self-hosted-appcircle/configure-server/integrations-and-access/network-access#appcircle-server-install-and-update) section and be sure that the listed domains are reachable from the Appcircle server.

## Runner Checklist

### Network Access for Installation

The Appcircle runner should be able to access the Appcircle server.

- [ ] Create a firewall rule (or permission) from the Appcircle runner to the Appcircle server.

:::info
Port depends on the configured `external.scheme` in the `global.yaml`.

- Port `443` must be allowed if the Appcircle server is configured as HTTPS.
- Ports `80` and `6379` must be allowed if the Appcircle server is configured as HTTP.

:::

The Appcircle runner should be able to access to the git provider

- [ ] Create a firewall rule (or permission) from the Appcircle runner to the git server.

:::info
Port depends on the selected connection method. Default values can be:

- HTTP(s): `80` or `443`
- SSH: `22`

If your git server has a custom port for git servcies, then you should use that port.
:::

- [ ] Review the [network access](/self-hosted-appcircle/configure-server/integrations-and-access/network-access#appcircle-runner-install-as-ready-to-use-macos-virtual-machine) section and be sure that the listed domains are reachable from the Appcircle runner.
