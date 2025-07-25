---
title: iOS Build Stacks
description: Learn about the iOS build stacks in Appcircle
tags: [ios, build, build stacks, ios build stacks]
sidebar_position: 1
---

import ContentRef from '@site/src/components/ContentRef';

# iOS Build Stacks

Depending on which Xcode version you select, Appcircle creates a brand new virtual machine running.

If your selected pool from config is "Appcircle Standard macOS Pool (arm64)", there are several options for the virtual machine as listed below:

| Xcode Selection | macOS Version |
| ------- | ----- |
| 16.3.x or later | Sequoia `15.4.1` |
| 16.0.x - 16.2.x | Sequoia `15.4.1` or Sonoma `14.5` |
| 14.3.x - 15.4.x | Sonoma `14.5` |
| 14.2.x or earlier | Monterey `12.6` |

MacOS images run on fresh virtual machines for stability and performance. They are created just for your build and become ready within seconds.

During the build process, you can install any dependencies and run commands using [custom script](/workflows/common-workflow-steps/custom-script) steps in the build workflow. This gives you complete control over your build and the virtual machine.

:::info

Please note that virtual machines are wiped off after a build is executed (no matter success or fail) and anything you installed in the virtual machine will be gone.

:::

## Available Xcode Versions

Our macOS build agents have Xcode versions 26.0.x, 16.4.x, 16.3.x, 16.2.x, 16.1.x, 16.0.x, 15.4.x, 15.3.x, 15.2.x, 15.1.x, 15.0.x, 14.3.x, 14.2.x, 14.1.x, 14.0.x, 13.4.x, 13.3.x, 13.2.x, 13.1.x, 13.0.x, 12.5.x available.

The "Appcircle Standard macOS Pool (arm64)" macOS **Sequoia** (`15.4.1`) stack has the Xcode versions below:

| Version | Build |
| ------- | ----- |
| 26.0 | `17A5241e` |
| 16.4 | `16F6` |
| 16.3 | `16E140` |
| 16.2 | `16C5032a` |
| 16.1 | `16B40` |
| 16.0 | `16A242d` |

The "Appcircle Standard macOS Pool (arm64)" macOS **Sonoma** (`14.5`) stack has the Xcode versions below:

| Version | Build |
| ------- | ----- |
| 16.2 | `16C5032a` |
| 16.1 | `16B40` |
| 16.0 | `16A242d` |
| 15.4 | `15F31d` |
| 15.3 | `15E204a` |
| 15.2 | `15C500b` |
| 15.1 | `15C65` |
| 15.0.1 | `15A507` |
| 14.3.1 | `14E300c` |

The "Appcircle Standard macOS Pool (arm64)" macOS **Monterey** (`12.6`) stack has the Xcode versions below:

| Version | Build |
| ------- | ----- |
| 14.2 | `14C18` |
| 14.1 | `14B47b` |
| 14.0.1 | `14A400` |
| 13.4 | `13F17a` |
| 13.3 | `13E113` |
| 13.2.1 | `13C100` |
| 13.1 | `13A1030d` |
| 13.0 | `13A233` |
| 12.5.1 | `12E507` |

## iOS Build Agent Stacks

There are many pre-installed packages on virtual machines. You can get a full list of pre-installed packages by running Bash commands in the [custom script](/workflows/common-workflow-steps/custom-script) steps.

Here are some of the most important packages installed in our iOS build agents used for iOS builds:

| Package            | macOS Monterey | macOS Sonoma | macOS Sequoia |
| ------------------ | ---------------- | -------------- | -------------- |
| Bash               | 3.2.57           | 3.2.57         | 3.2.57 |
| Bundle             | 2.1.4            | 2.4.19         | 2.4.19 |
| Carthage           | 0.38.0           | 0.39.1         | 0.40.0 |
| Curl               | 7.79.1           | 8.6.0          | 8.7.1 |
| Homebrew           | 3.6.11           | 4.3.5          | 4.5.1 |
| Java (OpenJDK)     | 17.0.9           | 17.0.9         | 17.0.9 |
| Gem                | 3.1.6            | 3.4.19         | 3.4.19 |
| Fastlane           | 2.211.0          | 2.220.0        | 2.227.2 |
| Git                | 2.38.1           | 2.45.2         | 2.49.0 |
| Git LFS            | 3.2.0            | 3.5.1          | 3.6.1 |
| Gzip (Apple)       | 353.100.22       | 430.100.5      | 457.100.3 |
| LibreSSL (OpenSSL) | 2.8.3            | 3.3.6          | 3.3.6 |
| ImageMagick        | 7.1.0            | 7.1.1-33       | 7.1.1-47 |
| Maven              | 3.8.6            | 3.9.7          | 3.9.9 |
| N                  | 9.0.1            | 9.2.3          | 10.1.0 |
| Node               | 18.19.1          | 18.20.3        | 18.20.8 |
| Npm                | 10.2.4           | 10.7.0         | 10.8.2 |
| Perl               | 5.30.3           | 5.34.1         | 5.34.1 |
| Pod                | 1.11.3           | 1.15.2         | 1.16.2 |
| Pip                | 22.2.2           | 24.0           | 25.0.1 |
| Python             | 3.10.8           | 3.12.3         | 3.13.3 |
| Rake               | 13.0.1           | 13.0.6         | 13.0.6 |
| Ruby               | 2.7.5            | 3.2.3          | 3.2.3 |
| Rbenv              | 1.2.0            | 1.2.0          | 1.3.2 |
| Sdkman             | 5.16.0           | 5.18.2         | 5.19.0 |
| Slather            | 2.7.2            | 2.8.0          | 2.8.5 |
| Unzip              | 6.00             | 6.00           | 6.00 |
| Xcodeproj          | 1.22.0           | 1.27.0         | 1.27.0 |
| Yarn               | 1.22.19          | 1.22.22        | 1.22.22 |
| Zip                | 3.0              | 3.0            | 3.0 |

### Using your own computer for build

Appcircle supports using a third-party computer to perform builds. You can create your own build environment by installing the operating system and other tools and dependencies you need to tell Appcircle to use that environment to perform builds.

<ContentRef url="/self-hosted-appcircle/self-hosted-runner">
Appcircle Self-hosted Runner
</ContentRef>
