---
title: iOS Build Infrastructure
metaTitle: iOS Build Infrastructure
metaDescription: iOS Build Infrastructure
sidebar_position: 1
---
# iOS Build Infrastructure

Depending on which Xcode version you select, Appcircle creates a brand new virtual machine running `macOS (v.10.15.7 Catalina)` or `macOS (v.12.4 Monterey)`

:::tip

For Xcode versions **14.0.x**, **13.4.x**, **13.3.x**, **13.2.x**, **13.1.x**, **13.0.x** and **12.5.x**, `macOS (v.12.4 Monterey)` is used. For every other versions, `macOS (v.10.15.7 Catalina)` is used.

:::

macOS images run on a fresh Docker environment for stability and performance. They are created just for your build and become ready within seconds.

During the build process, you can install any dependencies and run commands using "custom script" steps in the build workflow. This gives you complete control over your build and the virtual machine.

:::info

Please note that virtual machines are wiped off after a build is executed (no matter success or fail) and anything you installed in the virtual machine will be gone.

:::

### M1 Macs

We've started providing M1 Mac mini's to select enterprise customers starting from April 2022. We'll gradually enable M1 Macs to all enterprise customers first, and then to all plans.

If you'd like an M1 Mac for your builds, please request an invite:

https://www.appcircle.io/contact

### Using your own computer for build

Appcircle supports using a 3rd party computer to perform builds. You can create your own build environment by installing the operating system and other tools and dependencies you need to tell Appcircle to use that environment to perform builds.

[**Get in touch with Appcircle if you need enterprise features.**](https://appcircle.io/support)

### Available Xcode Versions

Our macOS build agents have Xcode versions 14.0.x, 13.4.x, 13.3.x, 13.2.x, 13.1.x, 13.0, 12.5, 12.4, 12.3, 12.2, 12.1, 12.0, 11.7, 11.6, 11.5, 11.4, 11.3, 11.2, 11.1 and 11.0 available.

### macOS Build Agent Stacks

There are many pre-installed packages in virtual machines. You can get a full list of pre-installed packages by running Bash commands in "custom script" steps.

Here are some of the most important packages installed in our macOS agents used for iOS builds:

`macOS Monterey v.12.4`

| Package            | Version    |
| ------------------ | ---------- |
| Bash               | 3.2.57     |
| Bundle             | 2.3.9      |
| Carthage           | 0.38.0     |
| Curl               | 7.79.1     |
| Homebrew           | 3.4.2      |
| Java (OpenJDK)     | 11.0.2     |
| Fastlane           | 2.204.3    |
| Gem                | 3.1.6      |
| Git                | 2.35.1     |
| Git LFS            | 3.1.2      |
| Gzip (Apple)       | 353.100.22 |
| LibreSSL (OpenSSL) | 2.8.3      |
| ImageMagick        | 7.1.0      |
| Maven              | 3.8.4      |
| N                  | 8.0.2      |
| Node               | 16.14.0    |
| Npm                | 8.3.1      |
| Perl               | 5.30.3     |
| Pod                | 1.11.2     |
| Pip                | 21.3.1     |
| Python             | 3.9.10     |
| Rake               | 13.0.1     |
| Ruby               | 2.7.5      |
| Rbenv              | 1.2.0      |
| Sdkman             | 5.14.0     |
| Slather            | 2.7.2      |
| Unzip              | 6.00       |
| Xcodeproj          | 1.21.0     |
| Yarn               | 1.22.17    |
| Zip                | 3.0        |
