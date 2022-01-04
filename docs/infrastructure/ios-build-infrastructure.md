---
title: iOS Build Infrastructure
metaTitle: iOS Build Infrastructure
metaDescription: iOS Build Infrastructure
sidebar_position: 1
---
# iOS Build Infrastructure

Depending on which Xcode version you select, Appcircle creates a brand new virtual machine running `macOS X (v.10.15 Catalina)` or `macOS X (v.10.16 Big Sur)`

:::tip

For Xcode version **13.0.x** and **12.5.x**, `macOS X (v.10.16 Big Sur)` is used. For every other versions, `macOS X (v.10.15 Catalina)` is used.

:::

macOS X images run on a fresh Vagrant environment for stability and performance. They are created just for your build and become ready within seconds.

During the build process, you can install any dependencies and run commands using custom scrip steps in the build workflow. This gives you complete control over your build and the virtual machine.

:::info


Please note that virtual machines are wiped off after a build is executed (no matter success or fail) and anything you installed in the virtual machine will be gone.

:::

### Using your own computer for build

Appcircle supports using a 3rd party computer to perform builds. You can create your own build environment by installing the operating system and other tools and dependencies you need to tell Appcircle to use that environment to perform builds.

[**Get in touch with Appcircle if you need enterprise features.**](https://appcircle.io/support)

### Available Xcode Versions

Our macOS build agents have Xcode versions 13.2.x, 13.1.x, 13.0, 12.5, 12.4, 12.3, 12.2, 12.1, 12.0, 11.7, 11.6, 11.5, 11.4, 11.3, 11.2, 11.1 and 11.0 available.;

### macOS Build Agent Stacks

There are many pre-installed packages in virtual machines. You can get a full list of pre-installed packages by running Bash commands in custom script steps.;

Here are some of the most important packages installed in our macOS agents used for iOS builds:

| Package            | Version   |
| ------------------ | --------- |
| Bash               | 3.2.57    |
| Homebrew           | 2.3.0     |
| Git                | 2.24.3    |
| Gzip (Apple)       | 287.100.2 |
| LibreSSL (OpenSSL) | 2.8.3     |
| Node               | 14.3.0    |
| Perl               | 5.18.4    |
| Python             | 2.7.16    |
| Rake               | 12.3.2    |
| Ruby               | 2.6.3     |
| RVM                | 1.29.10   |
