---
title: iOS Build Stacks
description: Learn about the iOS build stacks in Appcircle
tags: [ios, build, build stacks, iOS build stacks]
sidebar_position: 1
---

import ContentRef from '@site/src/components/ContentRef';

# iOS Build Stacks

Depending on which Xcode version you select, Appcircle creates a brand new virtual machine running.

- If your selected pool from config is "Default Intel Pool", virtual machine will be macOS Monterey `12.5.1`.

- If your selected pool from config is "Default M1 Pool", there are two options for virtual machine.
  - If you select Xcode 14.3 or later, virtual machine will be macOS Sonoma `14.5`.
  - If you select Xcode 14.2 or earlier, virtual machine will be macOS Monterey `12.6`.

:::caution

If you select Xcode 14.3 or later and "Default Intel Pool", your build will not start. Because Xcode 14.3 or later requires a Mac running macOS Ventura 13.0 or later.

:::

MacOS images run on fresh virtual machines for stability and performance. They are created just for your build and become ready within seconds.

During the build process, you can install any dependencies and run commands using "custom script" steps in the build workflow. This gives you complete control over your build and the virtual machine.

:::info

Please note that virtual machines are wiped off after a build is executed (no matter success or fail) and anything you installed in the virtual machine will be gone.

:::

## Available Xcode Versions

Our macOS build agents have Xcode versions 16.1.x, 16.0.x, 15.4.x, 15.3.x, 15.2.x, 15.1.x, 15.0.x, 14.3.x, 14.2.x, 14.1.x, 14.0.x, 13.4.x, 13.3.x, 13.2.x, 13.1.x, 13.0.x, 12.5.x available.

:::caution
Xcode `14.3.x` or higher Xcode versions require a Mac running macOS Ventura 13.0 or later.
:::

The "Default M1 Pool" macOS **Sonoma** (`14.5`) stack has the Xcode versions below:

| Version | Build |
| ------- | ----- |
| 16.1 | `16B5001e` |
| 16.0 | `16A242` |
| 15.4 | `15F31d` |
| 15.3 | `15E204a` |
| 15.2 | `15C500b` |
| 15.1 | `15C65` |
| 15.0.1 | `15A507` |
| 14.3.1 | `14E300c` |

The "Default M1 Pool" macOS **Monterey** (`12.5.1`) stack has the Xcode versions below:

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

There are many pre-installed packages on virtual machines. You can get a full list of pre-installed packages by running Bash commands in "custom script" steps.

Here are some of the most important packages installed in our iOS build agents used for iOS builds:

- For "Default M1 Pool" Xcode `14.3.x` or later macOS Sonoma `14.5`
- For "Default M1 Pool" Xcode `14.2.x` or earlier macOS Monterey `12.6`
- For "Default Intel Pool" macOS Monterey `12.5.1`
  - :memo: Supports Xcode versions up to `14.2.x`

| Package            | M1 Pool Monterey | M1 Pool Sonoma | Intel Pool |
| ------------------ | ---------------- | -------------- | ---------- |
| Bash               | 3.2.57           | 3.2.57         | 3.2.57     |
| Bundle             | 2.1.4            | 2.4.19         | 2.3.9      |
| Carthage           | 0.38.0           | 0.39.1         | 0.38.0     |
| Curl               | 7.79.1           | 8.6.0          | 7.79.1     |
| Homebrew           | 3.6.11           | 4.3.5          | 3.4.2      |
| Java (OpenJDK)     | 11.0.21          | 11.0.21        | 11.0.2     |
| Gem                | 3.1.6            | 3.4.19         | 3.1.6      |
| Fastlane           | 2.211.0          | 2.220.0        | 2.204.3    |
| Git                | 2.38.1           | 2.45.2         | 2.35.1     |
| Git LFS            | 3.2.0            | 3.5.1          | 3.1.2      |
| Gzip (Apple)       | 353.100.22       | 430.100.5      | 353.100.22 |
| LibreSSL (OpenSSL) | 2.8.3            | 3.3.6          | 2.8.3      |
| ImageMagick        | 7.1.0            | 7.1.1-33       | 7.1.0      |
| Maven              | 3.8.6            | 3.9.7          | 3.8.4      |
| N                  | 9.0.1            | 9.2.3          | 8.0.2      |
| Node               | 18.19.1          | 18.20.3        | 16.14.0    |
| Npm                | 10.2.4           | 10.7.0         | 8.3.1      |
| Perl               | 5.30.3           | 5.34.1         | 5.30.3     |
| Pod                | 1.11.3           | 1.15.2         | 1.11.2     |
| Pip                | 22.2.2           | 24.0           | 21.3.1     |
| Python             | 3.10.8           | 3.12.3         | 3.9.10     |
| Rake               | 13.0.1           | 13.0.6         | 13.0.1     |
| Ruby               | 2.7.5            | 3.2.3          | 2.7.5      |
| Rbenv              | 1.2.0            | 1.2.0          | 1.2.0      |
| Sdkman             | 5.16.0           | 5.18.2         | 5.14.0     |
| Slather            | 2.7.2            | 2.8.0          | 2.7.2      |
| Unzip              | 6.00             | 6.00           | 6.00       |
| Xcodeproj          | 1.22.0           | 1.24.0         | 1.21.0     |
| Yarn               | 1.22.19          | 1.22.22        | 1.22.17    |
| Zip                | 3.0              | 3.0            | 3.0        |

### Using your own computer for build

Appcircle supports using a third-party computer to perform builds. You can create your own build environment by installing the operating system and other tools and dependencies you need to tell Appcircle to use that environment to perform builds.

<ContentRef url="/self-hosted-appcircle/self-hosted-runner">
Appcircle Self-hosted Runner
</ContentRef>
