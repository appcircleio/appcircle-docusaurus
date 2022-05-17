---
title: Android Build Infrastructure
metaTitle: Android Build Infrastructure
metaDescription: Android Build Infrastructure
sidebar_position: 2
---

# Android Build Infrastructure

For each Android build, Appcircle creates a brand new virtual machine running Debian Linux (v. 11).;

Virtual machines are created and they become ready for build within seconds.

During the build process, you can install any dependencies and run commands using custom scrip steps in the build workflow. This gives you complete control over your build and the virtual machine.

:::info

Please note that virtual machines are wiped off after a build is executed (no matter success or fail) and anything you installed in the virtual machine will be gone.

:::

### Using your own computer for build

Appcircle supports using a 3rd party computer to perform builds. You can create your own build environment by installing the operating system and other tools and dependencies you need to tell Appcircle to use that environment to perform builds.

[**Get in touch with Appcircle if you need enterprise features.**](https://appcircle.io/support)

### Linux image stacks

There are many pre-installed packages in virtual machines. You can get a full list of pre-installed packages by running Bash commands in custom script steps.;

Here are some most important packages installed in our Linux images used for Android builds:

| Package             | Version |
| ------------------- | ------- |
| Apt Package Manager | 2.2.4   |
| Bash                | 5.1.2   |
| GNU Binutils        | 2.35.2  |
| Bzip2               | 1.0.8   |
| Curl                | 7.74.0  |
| GCC                 | 10.2.1  |
| Git                 | 2.35.1  |
| Git LFS             | 2.13.2  |
| Gradle              | 4.4.1   |
| Gzip                | 1.10.4  |
| Java                | 11.0.12 |
| Maven               | 3.8.5   |
| Node JS             | 16.14.2 |
| OpenSSL             | 1.1.1   |
| Perl                | 5.32.1  |
| Python              | 3.9.2   |
| Rake                | 13.0.6  |
| Rbenv               | 1.2.0   |
| Ruby                | 2.7.5   |
| Unzip               | 6.00    |
| Wget                | 1.21    |
| Yarn                | 1.22.18 |
| Zip                 | 3.0     |
