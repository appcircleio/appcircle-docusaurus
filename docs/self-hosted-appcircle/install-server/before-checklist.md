---
title: Before Installation Checklist
metaTitle: Before Installation Checklist
metaDescription: Before Installation Checklist
sidebar_position: 4
---

## Overview

This page provides a checklist to be followed before installing the Self-Hosted Appcircle.

It includes checks for the operating system, CPU core and architecture, RAM, disk, swappiness settings, DNS settings, SSL certificate, SMTP settings, Git server configuration, and necessary firewall rules.

Please ensure all the checks are completed for a smooth installation process.

## Self Hosted Appcircle Before Checklist

### Check the OS

- RHEL 8 or later.

```bash
cat /etc/redhat-release
```

- Ubuntu 20.04 or later.

```bash
cat /etc/os-release
```

- Debian 11 or later.

```bash
cat /etc/os-release
```

- CentOS 8 or later.

```bash
cat /etc/centos-release
```

### Check the CPU Core

- Minimum 8 core.
- Recommended 32 core.

```bash
nproc --all
```

### Check the CPU Architechture.

- must be x86_64.

```bash
uname -i
```

### Check the Ram.

- Minimum 16GB.
- Recommended 64GB.

```bash
free -h
```

### Check the Disk.

- Minimum 500GB.
- Recommended 1TB.
- SSD is a better choice.

```bash
df -h
```

### Check the Swappines Settings.

- Should be 10

```
sudo cat /proc/sys/vm/swappiness
sudo sysctl vm.swappiness=10
sudo vim /etc/sysctl.conf
vm.swappiness=10
```

### Configure the DNS Settings.

- Create a subdomain name from your companies domain name.
- If your company name is "Spacetech", and your domain is spacetech.local, see the steps below 👇.
- You should determine a subdomain like `appcircle` or `appcircle-test` or `appctest`.
- This domain (appcircle.spacetech.local) will have 7 sub domains.
  - api
  - auth
  - dist
  - hook
  - my
  - resource
  - store
- [ ] Create the 7 domain name entries on your domain server.
  - [ ] api.appcircle.spacetech.local
  - [ ] auth.appcircle.spacetech.local
  - [ ] dist.appcircle.spacetech.local
  - [ ] hook.appcircle.spacetech.local
  - [ ] my.appcircle.spacetech.local
  - [ ] resource.appcircle.spacetech.local
  - [ ] store.appcircle.spacetech.local
- [ ] All of these subdomains should resolve to the same server IP address which is Appcircle server.
- [ ] See details in [here.](https://docs.appcircle.io/self-hosted-appcircle/install-server/docker#4-dns-settings)
- [ ] Obtain a SSL cert.
  - [ ] You should create only one SSL certificate.
  - [ ] The SSL certificate should cover the all 7 domain names which you have seen in the previous step.
  - [ ] The SSL certificate should be in pem format.
  - [ ] The SSL certificate private key must not have passphrase.
  - [ ] Get the root CA certificate of your company.
  - [ ] Get the intermediate CA certificate of your company if it exists.
- [ ] Obtain SMTP Settings.
  - [ ] Get the ip address or host name of the smtp server.
  - [ ] Get the port number of the smtp server.
  - [ ] Learn if the SMTP server is using SSL.
  - [ ] Learn if the SMTP server is using STARTTLS.
  - Note: SSL and STARTTLS are _not_ the same thing.
  - If the SMTP server needs auth:
    - [ ] Create a user for Appcircle on the smtp server.
    - [ ] Get the password of Appcircle user on the smtp server.
  - [ ] Contact to the System Admin get required permissions to send email with Appcircle user with the SMTP server.
  - [ ] Create the firewall rules.
  - [ ] Create a firewall rule from your Appcircle server to the SMTP server.
- [ ] Configure Git server.
  - [ ] Import Appcircle android and/or iOS sample repositories on your local git server.
    - [ ] [Android Sample Repo](https://github.com/appcircleio/appcircle-sample-android)
    - [ ] [iOS Sample Repo](https://github.com/appcircleio/appcircle-sample-ios)
  - [ ] Create a Appcircle user on the git server (azure devops, gitlab, github, bitbucket).
  - [ ] If you are using Gitlab, Azure Devops Server, Bitbucket:
    - [ ] Create a Appcircle user. Give it permissions for the repositories.
    - [ ] Create a personal access token that has sufficient permissions.
    - For details like token permissions, check the [Appcircle documentation](https://docs.appcircle.io/build/adding-a-build-profile/#connect-your-repository).
  - [ ] If you are using any other git server:
    - [ ] Create a public private ssh key pair.
    - [ ] Configure your Appcircle git user's public ssh keys and upload the public ssh key you created.
    - For details, you can check the [Appcircle documentation](https://docs.appcircle.io/build/adding-a-build-profile/connecting-to-private-repository-via-ssh).
- [ ] Create necessary firewall rules for Appcircle server to install necessary dependencies.
  - [ ] You need a computer which has web browser and have access to the Appcircle server.
    - We will use Appcircle server from the web browser.
    - So the firewall rule should be from your computer to the Appcircle server machine.
  - [ ] You must get other detailed URLs from [Network Access Page](https://docs.appcircle.io/self-hosted-appcircle/configure-server/network-access)
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
  - [ ] You need to create firewall rules from Appcircle server to your smtp server:
    - from: Appcircle server
    - to: your smtp server
    - port: your smtp server's port (25 / 465 / 587)
    - test command: curl -v telnet://smtp.spacetech.com:587
- [ ] Create necessary firewall rules for Appcircle runner to build mobile applications.
  - [ ] You can get detailed urls from [Network Access Page](https://docs.appcircle.io/self-hosted-appcircle/configure-server/network-access/#external-resources-access-when-running-build-pipeline)
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
