---
title: Android Build Infrastructure
metaTitle: Android Build Infrastructure
metaDescription: Android Build Infrastructure
sidebar_position: 2
---

# Android Build Infrastructure

For each Android build, Appcircle creates a brand new virtual machine;

- If you select "Default Intel Pool", virtual machine will be Debian 11 Bullseye.
- If you select "Default M1 Pool", virtual machine will be macOS Ventura `13.4.1` or macOS Monterey `12.6`.

:::info

If you select M1 Pool, you can not choose macOS version. It will be automatically selected by Appcircle.

The chance is equal for both macOS Ventura and macOS Monterey for your android build because it does not effect your build.

:::

Virtual machines are created and they become ready for build within seconds.

During the build process, you can install any dependencies and run commands using custom scrip steps in the build workflow. This gives you complete control over your build and the virtual machine.

:::info

Please note that virtual machines are wiped off after a build is executed (no matter success or fail) and anything you installed in the virtual machine will be gone.

:::

### Java Version

Build agents have Java 8, 11, and 17 installed. Java 11 is set as the default version. If you want to use a different Java version. please follow [this document](../integrations/working-with-custom-scripts/custom-script-samples.md#changing-java-version)

### Emulator

Build agents have Pixel_3a Android 9.0 emulator pre-installed. You may add or remove other emulators by using `sdkmanager`.
For example, in order to install Android 11 (API 30) emulator to x86_64 Linux, you can take the below steps:

**1.** Install emulator system image if not exists. (If it exists, the command will return quickly with success.)

```bash
sdkmanager "system-images;android-30;google_apis;x86_64"
```

You can see a list of available system images with the below command:

```bash
sdkmanager --list | grep "system-images;android"
```

**2.** Create new pixel_3a device with "Pixel_Custom" emulator name.

```bash
avdmanager create avd -n Pixel_Custom -k "system-images;android-30;google_apis;x86_64" -c 512M -d pixel_3a
```

When completed with success, you should see below the device with `avdmanager list avd`:

```txt
    Name: Pixel_Custom
  Device: pixel_3a (Google)
    Path: /users/appcircle/.android/avd/Pixel_Custom.avd
  Target: Google APIs (Google Inc.)
Based on: Android 11.0 (R)
 Tag/ABI: google_apis/x86_64
  Sdcard: 512 MB
```

### Using your own computer for build

Appcircle supports using a 3rd party computer to perform builds. You can create your own build environment by installing the operating system and other tools and dependencies you need to tell Appcircle to use that environment to perform builds.

[**You can find more information about using your own infrastructure for build here.**](../self-hosted-appcircle/self-hosted-runner/overview.md)

### Android Build Agent Stacks

There are many pre-installed packages in virtual machines. You can get a full list of pre-installed packages by running Bash commands in custom script steps.

Here are some most important packages installed in our Linux and macOS images used for Android builds:

| Package             | Debian Bullseye | M1 Pool Ventura |  M1 Pool Monterey |
| ------------------- | --------------- | --------------- | ----------------- |
| Apt Package Manager | 2.2.4           | n/A             | n/A               |
| Bash                | 5.1.4           | 3.2.57          | 3.2.57            |
| GNU Binutils        | 2.35.2          | 2.39            | 2.39              |
| Bzip2               | 1.0.8           | n/A             | n/A               |
| Curl                | 7.74.0          | 7.88.1          | 7.79.1            |
| GCC                 | 10.2.1          | 15.0.0          | 14.0.0            |
| Git                 | 2.35.1          | 2.39.0          | 2.38.1            |
| Git LFS             | 2.13.2          | 3.3.0           | 3.2.0             |
| Gradle              | 4.4.1           | 7.6             | 7.5.1             |
| Gzip                | 1.10.4          | 403.100.6       | 353.100.22        |
| Java                | 11.0.12         | 11.0.14         | 11.0.14           |
| Maven               | 3.8.6           | 3.9.3           | 3.8.6             |
| Node JS             | 16.18.1         | 16.20.1         | 16.18.1           |
| OpenSSL             | 1.1.1           | 3.3.6           | 2.8.3             |
| Perl                | 5.32.1          | 5.30.3          | 5.30.3            |
| Python              | 3.9.2           | 3.10.9          | 3.10.8            |
| Rake                | 13.0.6          | 13.0.1          | 13.0.1            |
| Rbenv               | 1.2.0           | 1.2.0           | 1.2.0             |
| Ruby                | 2.7.5           | 2.7.5           | 2.7.5             |
| Unzip               | 6.00            | 6.00            | 6.00              |
| Wget                | 1.21            | 1.21            | 1.21              |
| Yarn                | 1.22.19         | 1.22.19         | 1.22.19           |
| Zip                 | 3.0             | 3.0             | 3.0               |
