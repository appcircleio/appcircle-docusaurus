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
| Apt Package Manager | 1.8.2   |
| Bash                | 5.0.4   |
| GNU Binutils        | 2.31.1  |
| Bzip2               | 1.0.6   |
| Curl                | 7.64.0  |
| GCC                 | 8.3.0   |
| Git                 | 2.20.1  |
| Gradle              | 4.4.1   |
| Gzip                | 1.9.3   |
| Java-common         | 0.71    |
| OpenSSL             | 1.1.1   |
| Perl                | 5.28    |
| Python              | 2.7.16  |
| Rake                | 12.3.1  |
| Ruby                | 2.5.1   |
