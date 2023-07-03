---
title: Android Emulators
metaTitle: Android Emulators
metaDescription: Android Emulators
sidebar_position: 4
---

# Overview

On build pipeline, you can use android emulators for UI testing of android apps. Self-hosted runner supports this use case and installs below android emulator for general purpose usage by default.

For example, on `macOS arm64` installation default emulator on self-hosted runner will be:

```txt
    Name: Pixel_3a
  Device: pixel_3a (Google)
    Path: $HOME/.android/avd/Pixel_3a.avd
  Target: Google Play (Google Inc.)
Based on: Android 9.0 (Pie)
 Tag/ABI: google_apis_playstore/arm64-v8a
```

Self-hosted runner chooses emulator ABI according to host architecture. So, android emulator ABI will be always compatible with host architecture for better optimization.

For all types of platforms, whether linux or macOS, other properties of default emulator and its device name are same. You don't need any conditional steps on your workflow while using default installed emulator.

If default emulator does not satisfy your requirements, you can install any additional emulators to self-hosted runner for your own usage.

For example, in order to install Android 11 (API 30) emulator to arm64 macOS you can take below steps:

**1.** Install emulator system image if not exists. (If it exists, command will return quickly with success.)

```bash
sdkmanager "system-images;android-30;google_apis;arm64-v8a"
```

You can see list of available system images with below command:

```bash
sdkmanager --list | grep "system-images;android"
```

**2.** Create new pixel_3a device with "Pixel_Custom" emulator name.

```bash
avdmanager create avd -n Pixel_Custom -k "system-images;android-30;google_apis;arm64-v8a" -c 512M -d pixel_3a
```

When completed with success, you should see below device with `avdmanager list avd`:

```txt
    Name: Pixel_Custom
  Device: pixel_3a (Google)
    Path: /Users/onur/.android/avd/Pixel_Custom.avd
  Target: Google APIs (Google Inc.)
Based on: Android 11.0 (R)
 Tag/ABI: google_apis/arm64-v8a
  Sdcard: 512 MB
```

## Emulators on Linux

For linux hosts, there are some preconditions to run android emulator. These are not preventing installation of default android emulator on self-hosted runner but you won't be able to start or use emulator on pipeline. So, you should check and satisfy them.

Although we summarize key points on below sections, you can get more detailed information about configuring hardware acceleration for the android emulator from [here](https://developer.android.com/studio/run/emulator-acceleration#dependencies-gpu).

### Check the capability of running KVM

To run KVM, you need a processor that supports hardware virtualization.

```bash
grep -cw ".*\(vmx\|svm\).*" /proc/cpuinfo
# or
egrep -c '(vmx|svm)' /proc/cpuinfo
```

A non-zero result means the host CPU supports hardware virtualization.

Alternatively, you can use below command to check capability:

```bash
sudo apt install -y cpu-checker >/dev/null 2>&1 && sudo kvm-ok
```

If virtualization is not enabled, be sure to enable the virtualization feature in your system.

If you're using cloud computing services, you can take a look at below resources:

- [Amazon Web Services](https://aws.amazon.com/blogs/compute/running-hyper-v-on-amazon-ec2-bare-metal-instances/)
- [Google Cloud Computing](https://cloud.google.com/compute/docs/instances/enable-nested-virtualization-vm-instances)
- [Microsoft Azure](https://azure.microsoft.com/en-us/blog/nested-virtualization-in-azure)

### Check if KVM module is loaded

```bash
lsmod | grep kvm
```

If you don't see any output, most probably you don't have KVM installed and running. So, follow below steps for Ubuntu based linux distributions.

**1.** Run the command below to install KVM and additional virtualization packages.

```bash
sudo apt install -y qemu-kvm virt-manager libvirt-daemon-system virtinst libvirt-clients bridge-utils
```

**2.** After all the packages installed, enable and start the Libvirt daemon.

```bash
sudo systemctl enable --now libvirtd
```

```bash
sudo systemctl start libvirtd
```

You can check virtualization daemon is status as shown.

```bash
sudo systemctl status libvirtd
```

**3.** Add the currently logged-in user to the kvm and libvirt groups so that they can create and manage virtual machines.

```bash
sudo usermod -aG kvm $USER
```

```bash
sudo usermod -aG libvirt $USER
```

To apply this change, you may need to log out and log in back again.

## Emulators on MacOS

If your GPU hardware and drivers are compatible, the emulator uses the GPU for graphics acceleration. You may get an error message like below, if your user is not logged in. (mostly on reboot cases)

> ... FATAL: Could not compile shader for guest framebuffer blit. There may be an issue with the GPU drivers on your machine. ...

So, take following steps to enable auto-login for the currently logged-in user.

1. Click the **Apple** logo.
2. Select **System Preferences** from the menu.
3. Click **Users & Groups.** (In earlier versions of OS X, this is called **Accounts**.)
4. Click the **lock** to make changes, and enter your administrator password when prompted.
5. Click **Login Options**.
6. Select the **Automatic login** username that you want to configure.

For more details, see [here](https://support.apple.com/en-us/HT201476).
