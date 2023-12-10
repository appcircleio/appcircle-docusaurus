---
title: Pre-Installation Checklist
metaTitle: Pre-Installation Checklist
metaDescription: Pre-Installation Checklist
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

If you don't have any swap space or it's insufficient, you can find the configuration details [here](docker.md#swap).

### Check the Swappiness

- [ ] The swappiness configuration should be **10**.

```bash
sudo cat /proc/sys/vm/swappiness
```

If the output is not 10, you can find the configuration details [here](docker.md#swappiness).

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

- [ ] All of these subdomains should resolve to the same server IP address, which is the Appcircle server.

You can see details in the [DNS Settings](./docker.md#4-dns-settings) section.

### Obtain an SSL Certificate

- [ ] You should create only one SSL certificate that covers all 7 domain names which you have seen in the [Configure DNS](#configure-the-dns-settings) section above.
- [ ] The SSL certificate should be in PEM format.
- [ ] The SSL certificate private key must not have a passphrase.
- [ ] Obtain the root CA certificate of your company.
- [ ] Obtain the intermediate CA certificate of your company if it exists.

### Obtain the SMTP Settings

- [ ] Obtain the IP address or host name of the SMTP server.
- [ ] Obtain the port number of the SMTP server.
- [ ] Determine if the SMTP server is using `SSL`.
- [ ] Determine if the SMTP server is using `STARTTLS`.
- Note: `SSL` and `STARTTLS` are **not** the same thing.
- If the SMTP server requires authentication:
  - [ ] Create a user for Appcircle on the SMTP server.
  - [ ] Obtain the password of the Appcircle user on the SMTP server.
- [ ] Contact the System Admin to get required permissions to send email with the Appcircle user via the SMTP server.
- [ ] Create a firewall rule from the Appcircle server to the SMTP server.

### Configure the Git Server

- [ ] Import Appcircle Android and/or iOS sample repositories on your local git server.
  - [ ] [Android Sample Repo](https://github.com/appcircleio/appcircle-sample-android)
  - [ ] [iOS Sample Repo](https://github.com/appcircleio/appcircle-sample-ios)
- [ ] Create an Appcircle user on the git server (Azure DevOps, GitLab, GitHub, Bitbucket).
- [ ] Give the required permissions to the Appcircle user to clone and edit the repositories.
- [ ] If you are using GitLab, Azure DevOps Server, Bitbucket:
  - [ ] Create an Appcircle user. Give it permissions for the repositories.
  - [ ] Create a personal access token that has sufficient permissions.
  - For details like token permissions, check the [Connect Your Repository Page](../../build/adding-a-build-profile#connect-your-repository).
- [ ] If you are using any other git server:
  - [ ] Create a public-private SSH key pair.
  - [ ] Configure your Appcircle git user's public SSH keys and upload the public SSH key you created.
  - For details, you can check the [Connect via SSH Page](../../build/adding-a-build-profile/connecting-to-private-repository-via-ssh.md).
  - [ ] Create a firewall rule from the Appcircle server to the git server.

### Create Necessary Firewall Rules for Appcircle Server to Install Necessary Dependencies

- [ ] You need a computer which has a web browser and has access to the Appcircle server.
  - You will use the Appcircle from a web browser.
  - [ ] Create a firewall rule should be from your computer to the Appcircle server machine.
    - from: A computer with a web browser
    - to: The Appcircle server
    - port: 80 & 443
- [ ] You need to create firewall rules from the Appcircle server to your git repositories:
  - [ ] If you are using GitLab, Azure DevOps Server or Bitbucket, the firewall rule should be:
    - from: The Appcircle server
    - to: The GitLab, Azure DevOps Server or Bitbucket server
    - port: 80 & 443
    - test command: curl -v telnet://gitserver.spacetech.com:443
  - [ ] If you are using any other git repos:
    - from: Appcircle server
    - to: The git server (GitHub, ...)
    - port: 22
    - test command: curl -v telnet://gitserver.spacetech.com:22
- [ ] You need to create firewall rules from the Appcircle server to your SMTP server:
  - from: The Appcircle server
  - to: The SMTP server
  - port: The SMTP server's port (25 / 465 / 587)
  - test command: curl -v telnet://smtp.spacetech.com:587
- [ ] You must obtain the rest of detailed URLs from [Network Access Page For an Appcircle Server](../configure-server/network-access.md)
  - You might install the Appcircle server on RHEL or Ubuntu with Docker or Podman.
  - See titles for your scenario and get the URL from there.

### Create Necessary Firewall Rules for Appcircle Runner to Build Mobile Applications

- [ ] The Appcircle Runner should be able to access the Appcircle server. Create a firewall rule:
  - from: Appcircle runner
  - to: Appcircle server
  - port: 443
- [ ] The Appcircle Runner should be able to access the git server. Create a firewall rule:

  - [ ] If you are using GitLab or Bitbucket, the firewall rule should be:
    - from: Appcircle runner
    - to: your GitLab or Bitbucket server
    - port: 443
  - [ ] If you are using any other git repos:
    - from: Appcircle runner
    - to: your git server (Azure, GitHub, ...)
    - port: 22

- [ ] You can get detailed URLs from [Network Access Page For an Appcircle Runner](../configure-server/network-access.md#appcircle-runner-runtime)
