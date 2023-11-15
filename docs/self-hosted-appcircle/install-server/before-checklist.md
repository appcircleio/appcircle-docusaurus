---
title: Before Installation Checklist
metaTitle: Before Installation Checklist
metaDescription: Before Installation Checklist
sidebar_position: 2
---

## Overview

This page provides a checklist to be followed before installing the Self-Hosted Appcircle.

It includes checks for the operating system, CPU core and architecture, RAM, disk, swappiness settings, DNS settings, SSL certificate, SMTP settings, Git server configuration, and necessary firewall rules.

Please ensure all the checks are completed for a smooth installation process.

## Self Hosted Appcircle Before Checklist

### Check the OS

- If you are using RHEL, it should be RHEL 8 or later.

```bash
cat /etc/redhat-release
```

- If you are using Ubuntu, it should be Ubuntu 20.04 or later.

```bash
cat /etc/os-release
```

- If you are using Debian, it should be Debian 11 or later.

```bash
cat /etc/os-release
```

- If you are using CentOS, it should be CentOS 8 or later.

```bash
cat /etc/centos-release
```

### Check the CPU Core

- Minimum CPU core count should be 8 core.
- Recommended and expected CPU core count is 32 core.

```bash
nproc --all
```

### Check the CPU Architecture.

- The CPU architecture must be x86_64.

```bash
uname -i
```

- If the command above 👆 doesn't work, you may try the command below 👇.

```bash
arch
```

### Check the Ram.

- Minimum Ram size should be 16GB.
- Recommended and expected Ram size is 64GB.

```bash
free -h
```

### Check the Disk.

- Minimum disk size should be 500GB.
- Recommended and expected disk size is 1TB.
- SSD is better and recommended choice for faster disk operations.

```bash
df -h
```

### Check the Swappiness Settings.

- The swappiness configuration should be 10.

```bash
sudo cat /proc/sys/vm/swappiness
```

- If the output is not 10, you can see the details [in here](docker.md#swappiness)

### Configure the DNS Settings.

- Create a subdomain name under your company's domain name.
- If your company name is "Spacetech", and your domain is `spacetech.com`, see the steps below 👇.
- You should determine a subdomain like `appcircle` or `appcircle-test` or `appctest` for Appcircle.
- This domain (`appcircle.spacetech.com`) will have 7 sub domains.
  - api
  - auth
  - dist
  - hook
  - my
  - resource
  - store
- [ ] Create the 7 domain name entries on your domain server.
  - [ ] api.appcircle.spacetech.com
  - [ ] auth.appcircle.spacetech.com
  - [ ] dist.appcircle.spacetech.com
  - [ ] hook.appcircle.spacetech.com
  - [ ] my.appcircle.spacetech.com
  - [ ] resource.appcircle.spacetech.com
  - [ ] store.appcircle.spacetech.com
- [ ] All of these subdomains should resolve to the same server IP address which is the Appcircle server.
- [ ] You can see details in the [DNS Settings](./docker.md#4-dns-settings) section.

### Obtain a SSL Certificate

- [ ] You should create only one SSL certificate.
- [ ] The SSL certificate should cover the all 7 domain names which you have seen in the [Configure DNS](#configure-the-dns-settings) section above.
- [ ] The SSL certificate should be in pem format.
- [ ] The SSL certificate private key must not have passphrase.
- [ ] Get the root CA certificate of your company.
- [ ] Get the intermediate CA certificate of your company if it exists.

### Obtain the SMTP Settings

- [ ] Get the IP address or host name of the SMTP server.
- [ ] Get the port number of the SMTP server.
- [ ] Learn if the SMTP server is using `SSL`.
- [ ] Learn if the SMTP server is using `STARTTLS`.
- Note: `SSL` and `STARTTLS` are **not** the same thing.
- If the SMTP server needs auth:
  - [ ] Create a user for Appcircle on the SMTP server.
  - [ ] Get the password of Appcircle user on the SMTP server.
- [ ] Contact to the System Admin get required permissions to send email with Appcircle user with the SMTP server.
- [ ] Create the firewall rules.
- [ ] Create a firewall rule from your Appcircle server to the SMTP server.

### Configure Git server

- [ ] Import Appcircle android and/or iOS sample repositories on your local git server.
  - [ ] [Android Sample Repo](https://github.com/appcircleio/appcircle-sample-android)
  - [ ] [iOS Sample Repo](https://github.com/appcircleio/appcircle-sample-ios)
- [ ] Create a Appcircle user on the git server (azure devops, gitlab, github, bitbucket).
- [ ] If you are using Gitlab, Azure Devops Server, Bitbucket:
  - [ ] Create a Appcircle user. Give it permissions for the repositories.
  - [ ] Create a personal access token that has sufficient permissions.
  - For details like token permissions, check the [Connect Your Repository Page](../../build/adding-a-build-profile#connect-your-repository).
- [ ] If you are using any other git server:
  - [ ] Create a public private ssh key pair.
  - [ ] Configure your Appcircle git user's public ssh keys and upload the public ssh key you created.
  - For details, you can check the [Connect via SSH Page](../../build/adding-a-build-profile/connecting-to-private-repository-via-ssh.md).

### Create necessary firewall rules for Appcircle server to install necessary dependencies

- [ ] You need a computer which has web browser and have access to the Appcircle server.
  - We will use Appcircle server from the web browser.
  - So the firewall rule should be from your computer to the Appcircle server machine.
- [ ] You must get other detailed URLs from [Network Access Page For an Appcircle Server](../configure-server/network-access.md)
  - You might install Appcircle server on RHEL or Ubuntu with docker or podman.
  - See titles for your scenario and get url from there.
- [ ] You need to create firewall rules from Appcircle server to your git repositories:
  - [ ] If you are using Gitlab, Azure Devops Server or Bitbucket, firewall rule should be:
    - from: Appcircle server
    - to: your Gitlab, Azure Devops Server or Bitbucket server
    - port: 443
    - test command: curl -v telnet://gitserver.spacetech.com:443
  - [ ] If you are using any another git repos:
    - from: Appcircle server
    - to: your git server (github, ...)
    - port 22
    - test command: curl -v telnet://gitserver.spacetech.com:22
- [ ] You need to create firewall rules from Appcircle server to your SMTP server:
  - from: Appcircle server
  - to: your SMTP server
  - port: your SMTP server's port (25 / 465 / 587)
  - test command: curl -v telnet://smtp.spacetech.com:587

### Create necessary firewall rules for Appcircle runner to build mobile applications

- [ ] You can get detailed urls from [Network Access Page For an Appcircle Runner](../configure-server/network-access.md#external-resources-access-when-running-build-pipeline)
- [ ] Appcircle Runner should be able to access to the Appcircle server. Create a firewall rule:
  - from: Appcircle runner
  - to: Appcircle server
  - port: 443
- [ ] Appcircle Runner should be able to access to the git server. Create a firewall rule:
  - [ ] If you are using Gitlab or Bitbucket, firewall rule should be:
    - from: Appcircle runner
    - to: your gitlab or bitbucket server
    - port: 443
  - [ ] If you are using any another git repos:
    - from: Appcircle runner
    - to: your git server (azure, github, ...)
    - port 22

```

```
