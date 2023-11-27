---
title: Runner Virtual Machine Setup
metaTitle: Runner Virtual Machine Setup
metaDescription: Runner Virtual Machine Setup
sidebar_class_name: hidden
---

# Self-hosted Runner as MacOS VM Image

Self-hosted runner installation is explained at Appcircle [docs](installation.md) in detail. You can install runner in your self-hosted environment by yourself, following instructions on there.

We're also providing ready-to-use runner VM image that you can download from Appcircle CDN. Especially for enterprise installation, it might be more practical than installing from scratch.

Here are some reasons for choosing VM image for self-hosted runner;

- It's more quick and easy way of deploying runner. Just download VM image and make some minor configurations for your environment.
- While installing runner, we need several packages from various sources on internet and runner installation requires to be online. Since all iOS and android build pipeline tools are included in VM image, you don't need complex firewall rules while deploying runner.
- It minimizes effects of strict macOS policies applied to host, especially at enterprise environments. Your runner environment will be same as used in Appcircle cloud.
- Since we use virtual machine for runner, it provides a clean, isolated instance for every build job. It means, known and more stable runner environment. Your runner won't persist any macOS changes done in build pipeline which can make runner unstable in time.
- You can install and run only one instance of self-hosted runner on a physical machine. On the other hand, using virtualization infrastructure brings us concurrency. We can run multiple instances of runner on the same host.

## Requirements

In order to use macOS VM, we need to install some dependencies on macOS host.

### 1. Install Homebrew

Script explains what it will do, follow instructions on there.

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

When installation complete, test:

```bash
brew doctor
```

```bash
brew --version
```

### 2. Install Tart

Tap Appcircle repository and install tart.

```bash
brew tap appcircleio/cli
```

```bash
brew install appcircleio/cli/tart
```

When installation complete, test:

```bash
tart --version
```

Run `tart` to touch initial folders.

```bash
tart list
```

Create VMs root folder in tart home.

```bash
mkdir $HOME/.tart/vms
```

### 3. Configure Power Settings

Configuring power settings on macOS to prevent the system from entering sleep mode is vital when deploying it as an Appcircle runner.

By keeping the system awake, you ensure uninterrupted accessibility to your Appcircle runners, preventing any potential offline cases caused by the system going to sleep.

This continuous availability is critical for running builds, as it guarantees that your builds can find runners online.

We suggest disabling those power settings to make it behave like a server station.

```bash
sudo pmset -a sleep 0
sudo pmset -a powernap 0
sudo pmset -a disksleep 0
sudo pmset -a displaysleep 0
```

## Download MacOS VM

### Download the macOS VM Image Manually

Download macOS VM from Appcircle bucket.

```bash
curl -L -O -C - https://storage.googleapis.com/appcircle-dev-common/self-hosted/macOS_230921.tar.gz
```

If you encounter network interruption, just run the same command again. It should continue download for remaining part. It will result in saving both time and bandwidth.

---

**Note:** You can check the integrity of downloaded file by comparing the MD5 checksum.

```bash
md5 macOS_230921.tar.gz
```

After a couple of minutes later you should see the output below.

```bash
MD5 (macOS_230921.tar.gz) = a86e96952bf538a086d1f35f67c4bc00
```

---

Create folder for VM.

```bash
mkdir $HOME/.tart/vms/macOS_230921
```

Extract archive into VMs folder.

```bash
tar -zxf macOS_230921.tar.gz --directory $HOME/.tart/vms/macOS_230921
```

It may take a little to complete. Be patient and wait return of command.

You can track progress of extraction by monitoring VM folder size.

```bash
du -sh $HOME/.tart/vms/macOS_230921
```

### Download the macOS VM Image With Script

To download and extract the Appcircle runner vm image on the background automatically, you can run the command below.

```bash
curl -O -L https://raw.githubusercontent.com/appcircleio/appcircle-self-hosted-scripts/main/install_vm.sh && \
chmod +x install_vm.sh && \
nohup ./install_vm.sh &
```

It may take a little to complete. You can see the logs with the command below.

```bash
tail -f nohup.out
```

:::info
You can close the ssh session while the script is running. The download and extract process will go on in the background.

But be aware that there might be some errors while downloading and extracting the VM image. Please keep an eye on the logs.
:::

:::info
If you face any error while downloading the VM image, please delete the corrupted VM image file and run the `curl` command block above 👆.
:::

### MacOS VM Information

This macOS VM image contains the same tools as in the "Default M1 Pool" in Appcircle Cloud. The only difference is the bundled Xcode versions. It comes with the Xcode versions below:

- `15.0.x`
- `14.3.x`
- `14.2.x`
- `14.1.x`

In order to keep free disk space sufficient for build pipelines, we're packaging the latest and most frequently used Xcode versions. But you can also install other Xcode versions yourself if required.

You can find more information about the build infrastructure in the documents below:

- [iOS Build Infrastructure](../../infrastructure/ios-build-infrastructure.md)
- [Android Build Infrastructure](../../infrastructure/android-build-infrastructure.md)

:::caution
We're bumping the VM macOS version according to Xcode requirements. So the latest VM image,`macOS_230921`, includes Ventura `13.5.2` pre-installed and needs Ventura host to run. It doesn't support running on older hosts like Monterey, Big Sur, etc.

If you don't need the latest Xcode and you want to run an older version of the macOS VM image that supports running on a Monterey host, contact us through our support channels.
:::

## Create Base Images

### Create Base Runner VMs

Apple's virtualization framework allows us to run up to two macOS VMs on host.

Each runner must register to the self-hosted Appcircle server with a unique name and configuration. So we will need two VM base images.

When you list VMs with `tart list`, you should see our extracted VM image in list.

In the steps below, we will create 2 base images named vm01 and vm02.

:::tip
The `vm01` base image is derived from our base image, and subsequently, the `vm02` base image will be created from the `vm01` base image.

This approach eliminates the need to redo all the configurations applied to `vm01` when setting up `vm02`, ensuring efficiency and consistency across both virtual machines.
:::

```txt
Source Name         Size
local  macOS_230921 167
```

Create VM image for runner1.

```bash
tart clone macOS_230921 vm01
```

In docker terminology, `vm01` and `vm02` will be our docker images. We will configure them separately, persist our changes and then create containers to execute build pipelines. On every build, fresh containers will be used for both runners.

### Configure Base Runner VMs

#### Configure Runner 1

Start runner1 VM image for configuration.

```bash
screen -d -m tart run vm01 --no-graphics
```

SSH login into running macOS VM.

```bash
ssh -o StrictHostKeyChecking=no appcircle@$(tart ip vm01)
```

---

**Note:** You should use "cicd" as SSH login password.

---

In the macOS VM, `/Volumes/agent-disk/appcircle-runner` is the root folder of runner.

```bash
cd /Volumes/agent-disk/appcircle-runner
```

So, the following commands will assume that current working directory is `/Volumes/agent-disk/appcircle-runner`.

##### 1. Check the Runner Version

You may have installed the latest Appcircle runner VM image, but the Appcircle runner may not be up-to-date.

You can follow the steps below to check the Appcircle runner version and upgrade if it isn't the latest version.

- Check the version of the current installation.

```bash
./ac-runner --version
```

- Check the latest version from the [Upgrade Runner](./update.md#1-update-runner) page.

- If your version is not up to date, please follow the [Update Runner](./update.md#1-update-runner) section in the page.

:::caution

You should run the `curl` and `unzip` commands on the `/Volumes/agent-disk/` path.

Since you're in the `appcircle-runner` directory now, please change the directory one level up.

:::

You don't need to apply the `Reconfigure Runner` section. But the `Reinstall Service` section is necessary since the latest version may also have some service updates.

When you complete update successfully, you should see the updated version in `--version` output.

Go to the `appcircle-runner` directory.

```bash
cd appcircle-runner
```

Check the version of the runner.

```bash
./ac-runner --version
```

##### 2. Configure Base Runner's NTP Settings

MacOS VMs try to update their date and time using the network time protocol (NTP) by default.

If your organization has limited network access for the Appcircle runner machine, the VM may be unable to reach the servers responsible for updating its date and time settings.

In a situation like that, your organization might have an NTP server for internal usage.

You can configure your macOS runner VM to use your organization's own NTP server.

You can use the helper script named `configure_ntp.sh` that comes with the runner package to configure the NTP settings.

To configure NTP settings:

- The IP address or URL of the NTP server should be known.

- Network access should be allowed from the Appcircle runner to the NTP server.

- You will find a script named `configure_ntp.sh` in the `scripts` folder inside the `appcircle-runner` directory.

- Run the script and give the NTP server IP (or URL) as an argument, like the example below:

```bash
./scripts/configure_ntp.sh "10.10.1.50"
```

:::caution
You should change "10.10.1.50" to the NTP server address of your organization in the example above.
:::

##### 3. Trust The Root Certificates of Your Organization

If the resources you want to connect use a self-signed certificate, you should also trust the root certificate of your organization in your Appcircle runner VMs. These resources can be:

- Git providers (GitLab, Bitbucket, Azure DevOps, etc.)
- Self-hosted Appcircle server
- Proxy server for network access

Trusting your organization's root certificate on the OS is crucial.

Because the runner will try to connect to these resources over HTTPS and the SSL certificate will be signed with your organization's root certificate.

Furthermore, if the runner attempts to access external web sites, the requests will most likely be intercepted by the proxy and re-signed with a self-issued certificate that is also signed by the root certificate.

You can use the helper script named `install_cert.sh` that comes with your runner package to configure the certificates.

- You will find a script named `install_cert.sh` in the `scripts` folder inside the `appcircle-runner` directory.

- Run the script like the example below:

```bash
./scripts/install_cert.sh
```

- The script will ask you to enter a URL. Please give the URL of the resource that you need to connect to from the runner.

- Hit "enter" and check the results.

- Your organization's root CA certificate is now trusted on the OS, Java, Ruby, and Node.js.

:::info
For more detailed usage, you can check the [Self-signed Certificates](./configure-runner/custom-certificates.md#adding-certificates) page.
:::

##### 4. Configure Runner Service

---

**Note:** Runner logs are kept in `$HOME/appcircle-runner` folder.

---

Stop runner service.

```bash
./ac-runner service -c stop
```

Edit `appsettings.json` with your favorite editor. (nano, vi etc.)

```json
{
  ...
  "ASPNETCORE_NOSHUTDOWN": "false",
  ...
  "ASPNETCORE_BASE_API_URL": "https://api.test-appcircle.tool.zb/build/v1"
}
```

- ASPNETCORE_NOSHUTDOWN: It should be `false`. So, it will shutdown VM when build complete.
- ASPNETCORE_BASE_API_URL: It should be your self-hosted appcircle server URL.

Runner will register to server defined in `ASPNETCORE_BASE_API_URL` and take build jobs from there.

Create runner access token from appcircle server and register runner to server. See details in [here](../self-hosted-runner/installation.md#2-register).

For example,

```bash
./ac-runner register -t aat_eev4NQdG_7F2jodmMShBFhh_DgabOJSsWSMojX5_lo4 -n runner1 -p macOS_pool
```

It won't print anything to CLI on success. You can also check its exit value with `echo $?`. It should be `0` on success.

```bash
./ac-runner service -c start
```

Now you should see "runner1" in "Build > Self-hosted Runners" list. It may take a couple of seconds to become online.

If "runner1" is online, we can shutdown VM since configuration is done with success.

```bash
sudo shutdown -h now
```

#### Configure Runner 2

As we configured the runner1 (vm01), we can clone vm01 to vm02.

So we won't need to reconfigure NTP settings, self-signed SSL certificates, or other configurations that we made for vm01.

Create VM image for runner2 from runner1.

```bash
tart clone vm01 vm02
```

Start runner2 image for configuration.

```bash
screen -d -m tart run vm02 --no-graphics
```

SSH login into running macOS VM.

```bash
ssh -o StrictHostKeyChecking=no appcircle@$(tart ip vm02)
```

After login, configuration steps for Appcircle runner service are the same as "runner1". So, we don't need to repeat same commands again.

The only difference should be runner naming. It must be unique. For the second runner, just give a different name. For example, "runner2".

Refer to the [Configure Runner Service](#3-configure-runner-service) for detailed Appcircle runner service configuration.

After shutdown, we're ready to run instances from `vm01` and `vm02` base VM images.

At this stage your VM list returned by `tart list` should be like below.

```txt
Source Name         Size
local  macOS_230921 167
local  vm01         130
local  vm02         130
```

## Operating MacOS VMs

### Prerequisites

We need to create two seperate folders for two runners. These will be their working directories on runtime.

Create folder for "runner1".

```bash
mkdir $HOME/runner1
```

Create folder for "runner2".

```bash
mkdir $HOME/runner2
```

We have a simple bash script that will be used to run VM instances in loop.

Download the script into runner folders you created and make script executable.

For "runner1" use below commands.

```bash
curl -L -o $HOME/runner1/run.sh https://storage.googleapis.com/appcircle-dev-common/self-hosted/run.sh
chmod u+x $HOME/runner1/run.sh
```

For "runner2" use below commands.

```bash
curl -L -o $HOME/runner2/run.sh https://storage.googleapis.com/appcircle-dev-common/self-hosted/run.sh
chmod u+x $HOME/runner2/run.sh
```

### Start VM

In order to start "runner1", use below command.

```bash
screen -d -m $HOME/runner1/run.sh vm01
```

It will start "runner1" in detached mode and will manage VM lifecycle continuously.

In a couple of minutes, you should see "runner1" as online in self-hosted runners list.

We can also start "runner2" with below command.

```bash
screen -d -m $HOME/runner2/run.sh vm02
```

In docker terminology, we're creating container from docker image at this stage. On build complete, runner will be shutdown automatically and `run.sh` will create a fresh one from macOS image. It continuously does the same operation until stopped.

We can see running instances on macOS host with `tart list`.

```txt
Source Name                                      Size
local  macOS_230921                              167
local  vm01                                      130
local  vm01-4f496549-cfe8-462c-ba55-774f01c03b4f 130
local  vm02                                      130
local  vm02-9f1fc62a-f43c-40f3-98d0-523ed9a67042 130
```

As you can see in list, we have new VMs with long unique name. Those are actually online VMs that we started.

`vm01` and `vm02` are immutable VM images. On the other hand, others are instances created from VM images.

### Stop VM

In order to stop VM, we need to mark runner as stopped and shutdown online runner over SSH.

Touch `.stop` file at runner's working directory.

```bash
touch $HOME/runner1/.stop
```

Creating `.stop` file prevents creating new instance by `run.sh` on shutdown.

If runner is executing build pipeline, you may prefer waiting completion of the build job. See [stop](../self-hosted-runner/configure-runner/runner-service.md#stop) section at self-hosted runner docs. When executing build pipeline completes, runner will be shutdown automatically.

On the other hand if you want to stop runner immediately for whatever reason or it's in idle state, you can SSH into runner and run shutdown command.

First you need to have to find out online runner's VM name from `tart list`.

```txt
Source Name                                      Size
local  macOS_230921                              167
local  vm01                                      130
local  vm01-4f496549-cfe8-462c-ba55-774f01c03b4f 130
local  vm02                                      130
local  vm02-9f1fc62a-f43c-40f3-98d0-523ed9a67042 130
```

In above list, "vm01-4f496549-cfe8-462c-ba55-774f01c03b4f" is the name of runner that we will shutdown.

SSH login into that runner.

```bash
ssh -o StrictHostKeyChecking=no appcircle@$(tart ip vm01-4f496549-cfe8-462c-ba55-774f01c03b4f)
```

---

**Note:** You should use "cicd" as SSH login password.

---

Execute shutdown command.

```bash
sudo shutdown -h now
```

Shutdown process may take a couple of seconds.

After shutdown, you won't see anymore instance from `vm01` on `tart list`.

```txt
Source Name                                      Size
local  macOS_230921                              167
local  vm01                                      130
local  vm02                                      130
local  vm02-9f1fc62a-f43c-40f3-98d0-523ed9a67042 130
```

After a couple of minutes later, "runner1" will also become offline at self-hosted runners list.

Steps are also similar for "runner2". You need to touch `.stop` file in its working directory and after getting its VM name from `tart list`, you can shutdown "runner2" over SSH.

## Update Base Images

On some cases, you may need to update to your macOS base images in order to make your changes permanent.

Below are the ones that frequently occur, but not limited to them.

- Your team might use a tool frequently in build pipeline, that's not included in Appcircle macOS image. Installing that tool into the image once will save build time. Your build pipeline will be more efficient and optimized.
- You may prefer to get iOS and android tool updates by using [self-hosted runner update](../self-hosted-runner/update.md) method instead of getting fresh macOS VM image. When you get fresh macOS image you may need to make your custom configurations again.
- You may need to make persistent proxy configuration for your internal network requirements.
- You may need to add your corporate's self-signed root CAs to macOS VM image in order to succeed SSL connections.

Steps, that we need to take, are technically similar as in [Create Base Images](#create-base-images) section. So, a conceptual overview of the steps will be sufficient.

1. Stop all online runners as explained in [Stop VM](#stop-vm) section.
2. Run `vm01` base image. `screen -d -m tart run vm01 --no-graphics`
3. SSH into `vm01`. `ssh -o StrictHostKeyChecking=no appcircle@$(tart ip vm01)`
4. Make your modifications, configurations or updates in macOS.
5. Shutdown `vm01`
6. Run `vm02` base image. `screen -d -m tart run vm02 --no-graphics`
7. SSH into `vm02`. `ssh -o StrictHostKeyChecking=no appcircle@$(tart ip vm02)`
8. Make your modifications, configurations or updates in macOS.
9. Shutdown `vm02`.
10. Start offline runners as explained in [Start VM](#start-vm) section.

## Troubleshooting

### Tart list has runner instance in list but I can not SSH into the runner

Rarely your runner might hang or might become offline for some reason.

- You can get its IP with `tart ip` but might not connect.
- Although it's in `tart list` you might not get its IP.
- Detached `screen` session might be terminated because of an error.

You need to check your macOS host for possible system issues. (disk space, network connectivity, OS reboot etc.)

You can also check runner's working directory for any error that might happen at virtualization. (`stderr.log`, `stdout.log`)

In this case, you can make your runners operational again by following below steps.

1- Make sure detached screen session and all its child processes terminated for the runner.

For instance, you can find list of PIDs for "runner2" as seen below.

```bash
% ps aux | grep vm02 | grep -v grep
appcircle        35640   0.0  0.1 408653856  18320 s002  S+    2:35PM   0:00.68 tart run vm02-3a003bce-a2ee-4ae7-9500-7754e181c314 --no-graphics
appcircle        35174   0.0  0.0 408628512   2352 s002  S+    2:20PM   0:00.01 bash /Users/appcircle/runner2/run.sh vm02
root             35173   0.0  0.0 408515456   6848 s002  Ss+   2:20PM   0:00.01 login -pflq appcircle /Users/appcircle/runner2/run.sh vm02
appcircle        35172   0.0  0.0 408654848   1264   ??  Ss    2:20PM   0:00.00 SCREEN -d -m /Users/appcircle/runner2/run.sh vm02
```

2- Make sure there is no active virtualization framework process for the runner.

For instance, you can filter like this.

```bash
% ps aux | grep -i virtualmachine | grep -v grep
appcircle        35641   0.3 31.9 503225216 10699872   ??  Ss    2:35PM  42:07.38 /System/Library/Frameworks/Virtualization.framework/Versions/A/XPCServices/com.apple.Virtualization.VirtualMachine.xpc/Contents/MacOS/com.apple.Virtualization.VirtualMachine
```

3- Make sure there is no instance for the runner at VM list. If exists, remove it.

For instance, we have an instance for "runner2" seen below.

```bash
% tart list
Source Name                                      Size
local  macOS_230309                              187
local  vm01                                      140
local  vm02                                      140
local  vm02-3a003bce-a2ee-4ae7-9500-7754e181c314 125
```

Remove dangling "runner2".

```bash
tart delete vm02-3a003bce-a2ee-4ae7-9500-7754e181c314
```

4- Start VM for the runner as usual by following steps at [start VM](#start-vm).

For instance, start "runner2" with command below.

```bash
screen -d -m $HOME/runner2/run.sh vm02
```

### I can SSH into runner but runner is offline at self-hosted runners list

In this case, you need to focus on self-hosted runner issues inside macOS VM (guest).

In order to be able to investigate root cause, you should learn the basics of self-hosted runner. Check our [online docs](./overview.md) details.

- You can check your macOS guest for possible system issues. (disk space, network connectivity etc.)
- If you have custom proxy settings on macOS guest, check these settings.
- If you added custom root CAs to macOS guest, verify their validity for SSL connection errors.
- You can check runner launchd service and its logs. (`stdout.log`, `stderr.log`, `logs` etc.)
- You should check network access from self-hosted runner to server. (firewall, open ports etc.)

### Datetime I see in build logs is not correct

This case is related with broken datetime synchronization between runner and server.

Both server and runner should synchronize their times with relevant NTP services. Timezone difference is not important. Datetime must be correct in their timezones.

If runner doesn't have network access to an NTP server on the internet, you can also configure it to use your internal NTP server.

For updating macOS base image see [related section](#update-base-images) above.

For configuring NTP settings, see [Configure Base Runner's NTP Settings](#1-configure-base-runners-ntp-settings) section above.

### I am facing "SSL cert is not valid yet" error in our builds

This problem is again related to your macOS VM date and time being out of date.

To fix that, you should sync the VMs' date and time with your organization's NTP server.

For updating macOS base image see [related section](#update-base-images) above.

For configuring NTP settings, see [Configure Base Runner's NTP Settings](#1-configure-base-runners-ntp-settings) section above.

### Runners are offline and I noticed that macOS host has been reboot

If there is no system crash, one reason for an unintentional reboot may be caused by automatic updates.

We suggest disabling automatic updates on macOS host, and get them manually when required.

Below are the CLI commands to disable all automatic updates on macOS.

```bash
sudo defaults write /Library/Preferences/com.apple.SoftwareUpdate AutomaticDownload -bool false
sudo defaults write /Library/Preferences/com.apple.SoftwareUpdate CriticalUpdateInstall -int 0
sudo defaults write /Library/Preferences/com.apple.SoftwareUpdate AutomaticCheckEnabled -bool false
sudo defaults write /Library/Preferences/com.apple.SoftwareUpdate AutomaticallyInstallMacOSUpdates -int 0
sudo defaults write /Library/Preferences/com.apple.commerce AutoUpdate -int 0
```

### Runners are offline but when I SSH into host, it suddenly becomes online

When you install a fresh macOS on a mac device, it comes with predefined power settings which makes it energy efficient.

So, most probably, your macOS host sleeps when there is no UI interaction, and awakes on SSH login.

To do that, please configure your power settings on the host machine.

You can re-check the [Configure Power Settings](#3-configure-power-settings) title for power management on the host.

### I want to make some configurations to macOS base image but need desktop UI for them

If you're not comfortable with CLI, you can also make your customizations using macOS desktop.

For this purpose, remove `--no-graphics` argument from `tart run` commands.

Below step in [update base images](#update-base-images) section,

> 2- Run `vm01` base image. `screen -d -m tart run vm01 --no-graphics`

should be like this in this case.

> 2- Run `vm01` base image. `screen -d -m tart run vm01`
