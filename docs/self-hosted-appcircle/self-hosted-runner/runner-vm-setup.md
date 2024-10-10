---
title: Runner Virtual Machine Setup
description: Learn how to set up a self-hosted runner as a macOS VM image
tags: [self-hosted runner, runner, vm, virtual machine, setup]
sidebar_class_name: hidden
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import NewRunnerOldServerRedisCaution from '@site/docs/self-hosted-appcircle/self-hosted-runner/\_new_runner-old_server-redis-caution.mdx';
import HostCaution512GB from '@site/docs/self-hosted-appcircle/self-hosted-runner/\_512GB_host_warning.mdx';

# Self-hosted Runner as MacOS VM Image

Self-hosted runner installation is explained at Appcircle [docs](installation) in detail. You can install runner in your self-hosted environment by yourself, following instructions on there.

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

Tap Appcircle repository and install `tart` (Tart is a registered trademark of Cirrus Labs, Inc.).

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

### 4. Configure Power Failure Settings

Power failure settings allow a Mac to restart automatically after a power outage or failure. Activating this on a Mac ensures the host comes back online automatically if power is lost, avoiding downtime.

:::info
For now, Appcircle runners don't support auto-start when the macOS host restarts.

You should connect to host with SSH and [start the VMs](#start-vm) manually.
:::

To configure power failure settings, you can run the command below.

```bash
sudo /usr/sbin/systemsetup -setrestartpowerfailure on
```

You should see "setrestartpowerfailure: On" in the command output after successful execution.

:::info
If your host doesn't support this feature, you will get the message below.

> Restart After Power Failure: Not supported on this machine.

You can ignore power failure settings if they are not supported.
:::

## Download MacOS VM

You have two options to obtain the Appcircle runner images: manual or automated.

To perform these tasks manually, you can follow our step-by-step guide on [downloading the macOS VM image manually](#download-the-macos-vm-image-manually).

Alternatively, you can automate this process in the background by following our instructions on [downloading the macOS VM and Xcode images automatically](#download-the-macos-vm-and-xcode-images-automatically).

### Download the macOS VM Image Manually

:::tip

MacOS VM image has a versioning convention based on release date instead of arbitrary numbers. This date-based approach is called calendar versioning, or CalVer for short.

Our calendar versioning scheme for the macOS image is `YY0M0D`. For example, a macOS image that's released on March 6, 2024, should have version `240306`.

The versions are listed in chronological order, from the earliest to the most recent, in the tabs below.

:::

<HostCaution512GB/>

Download macOS VM from Appcircle bucket.

<Tabs groupId="macos-image">

  <TabItem value="240306" label="240306">

```bash
curl -L -O -C - https://storage.googleapis.com/appcircle-dev-common/self-hosted/macOS_240306.tar.gz
```

  </TabItem>
  <TabItem value="240514" label="240514">

```bash
curl -L -O -C - https://storage.googleapis.com/appcircle-dev-common/self-hosted/macOS_240514.tar.gz
```

  </TabItem>
  <TabItem value="240918" label="240918" default>

```bash
curl -L -O -C - https://storage.googleapis.com/appcircle-dev-common/self-hosted/macOS_240918.tar.gz
```

  </TabItem>
</Tabs>

If you encounter network interruption, just run the same command again. It should continue download for remaining part. It will result in saving both time and bandwidth.

---

**Note:** You can check the integrity of downloaded file by comparing the MD5 checksum.

<Tabs groupId="macos-image">

  <TabItem value="240306" label="240306">

```bash
md5 macOS_240306.tar.gz
```

  </TabItem>
  <TabItem value="240514" label="240514">

```bash
md5 macOS_240514.tar.gz
```

  </TabItem>
  <TabItem value="240918" label="240918" default>

```bash
md5 macOS_240918.tar.gz
```

  </TabItem>

</Tabs>

After a couple of minutes later you should see the output below.

<Tabs groupId="macos-image">

  <TabItem value="240306" label="240306">

```bash
MD5 (macOS_240306.tar.gz) = 084a9221075ed5453aceba6a3438b134
```

  </TabItem>
  <TabItem value="240514" label="240514">

```bash
MD5 (macOS_240514.tar.gz) = 8524abc65668a084589e79f214a9b281
```

  </TabItem>
  <TabItem value="240918" label="240918" default>

```bash
MD5 (macOS_240918.tar.gz) = aeb6ff4b655b04fa47fb45e2caf09792
```

  </TabItem>
</Tabs>

---

Create folder for VM.

<Tabs groupId="macos-image">

  <TabItem value="240306" label="240306">

```bash
mkdir -p $HOME/.tart/vms/macOS_240306
```

  </TabItem>
  <TabItem value="240514" label="240514">

```bash
mkdir -p $HOME/.tart/vms/macOS_240514
```

  </TabItem>
  <TabItem value="240918" label="240918" default>

```bash
mkdir -p $HOME/.tart/vms/macOS_240918
```

  </TabItem>
</Tabs>

Extract archive into VMs folder.

<Tabs groupId="macos-image">

  <TabItem value="240306" label="240306">

```bash
tar -zxf macOS_240306.tar.gz --directory $HOME/.tart/vms/macOS_240306
```

  </TabItem>
  <TabItem value="240514" label="240514">

```bash
tar -zxf macOS_240514.tar.gz --directory $HOME/.tart/vms/macOS_240514
```

  </TabItem>
  <TabItem value="240918" label="240918" default>

```bash
tar -zxf macOS_240918.tar.gz --directory $HOME/.tart/vms/macOS_240918
```

  </TabItem>
</Tabs>

It may take a little to complete. Be patient and wait return of command.

You can track progress of extraction by monitoring VM folder size.

<Tabs groupId="macos-image">

  <TabItem value="240306" label="240306">

```bash
du -sh $HOME/.tart/vms/macOS_240306
```

 </TabItem>
  <TabItem value="240514" label="240514">

```bash
du -sh $HOME/.tart/vms/macOS_240514
```

  </TabItem>
  <TabItem value="240918" label="240918" default>

```bash
du -sh $HOME/.tart/vms/macOS_240918
```

  </TabItem>
</Tabs>

### Download Xcode Images Manually

Download Xcode images from the Appcircle bucket. They are disk images for each Xcode version archived in a package.

<Tabs groupId="macos-image">

  <TabItem value="240306" label="240306">

```bash
curl -L -O -C - https://storage.googleapis.com/appcircle-dev-common/self-hosted/xcodes_240306.tar.gz
```

 </TabItem>
  <TabItem value="240514" label="240514">

```bash
curl -L -O -C - https://storage.googleapis.com/appcircle-dev-common/self-hosted/xcodes_240514.tar.gz
```

  </TabItem>
  <TabItem value="240918" label="240918" default>

```bash
curl -L -O -C - https://storage.googleapis.com/appcircle-dev-common/self-hosted/xcodes_240918.tar.gz
```

  </TabItem>
</Tabs>

If you encounter network interruption, just run the same command again. It should continue download for remaining part. It will result in saving both time and bandwidth.

---

**Note:** You can check the integrity of downloaded file by comparing the MD5 checksum.

<Tabs groupId="macos-image">

  <TabItem value="240306" label="240306">

```bash
md5 xcodes_240306.tar.gz
```

 </TabItem>
  <TabItem value="240514" label="240514">

```bash
md5 xcodes_240514.tar.gz
```

  </TabItem>
  <TabItem value="240918" label="240918" default>

```bash
md5 xcodes_240918.tar.gz
```

  </TabItem>
</Tabs>

After a couple of minutes later you should see the output below.

<Tabs groupId="macos-image">

  <TabItem value="240306" label="240306">

```bash
MD5 (xcodes_240306.tar.gz) = 4df051e11b6c0b8670cd9b82928dfab2
```

 </TabItem>
  <TabItem value="240514" label="240514">

```bash
MD5 (xcodes_240514.tar.gz) = e3edc40c9b6dda91530d8a1f8cf456bc
```

  </TabItem>
  <TabItem value="240918" label="240918" default>

```bash
MD5 (xcodes_240918.tar.gz) = bb26c0070bbd1a8ed23fe59b87f0a144
```

  </TabItem>
</Tabs>

---

Create folder for the Xcode disk images.

```bash
mkdir -p $HOME/images
```

Extract archive into the folder.

<Tabs groupId="macos-image">

  <TabItem value="240306" label="240306">

```bash
tar -zxf xcodes_240306.tar.gz --directory $HOME/images
```

 </TabItem>
  <TabItem value="240514" label="240514">

```bash
tar -zxf xcodes_240514.tar.gz --directory $HOME/images
```

  </TabItem>
  <TabItem value="240918" label="240918" default>

```bash
tar -zxf xcodes_240918.tar.gz --directory $HOME/images
```

  </TabItem>
</Tabs>

It may take a little to complete. Be patient and wait return of command.

---

<Tabs groupId="macos-image">

  <TabItem value="240306" label="240306">

**Note:** This macOS VM image is the Sonoma (`14.1`) stack and comes with the Xcode versions below:

> - `15.3.x`
> - `15.2.x`
> - `15.1.x`
> - `15.0.x`
> - `14.3.x`

  </TabItem>
  <TabItem value="240514" label="240514">

**Note:** This macOS VM image is the Sonoma (`14.1`) stack and comes with the Xcode versions below:

> - `15.4.x`
> - `15.3.x`
> - `15.2.x`
> - `15.1.x`
> - `15.0.x`
> - `14.3.x`

  </TabItem>
  <TabItem value="240918" label="240918" default>

**Note:** This macOS VM image is the Sonoma (`14.5`) stack and comes with the Xcode versions below:

> - `16.1.x`
> - `16.0.x`
> - `15.4.x`
> - `15.3.x`
> - `15.2.x`
> - `15.1.x`
> - `15.0.x`
> - `14.3.x`

  </TabItem>
</Tabs>

In order to keep free disk space sufficient for build pipelines, we're packaging the latest and most frequently used Xcode versions. But you can also install other Xcode versions yourself if required.

You can find more information about the build infrastructure in the documents below:

- [iOS Build Infrastructure](/infrastructure/ios-build-infrastructure)
- [Android Build Infrastructure](/infrastructure/android-build-infrastructure)

:::caution
We're constantly bumping the VM macOS version according to Xcode requirements.

So the latest VM image,`macOS_230921` or later, includes Ventura `13.5.2` or Sonoma `14.x` pre-installed and needs at least a Ventura host to run.

It doesn't support running on older hosts like Monterey, Big Sur, etc.

If you don't need the latest Xcode and you want to run an older version of the macOS VM image that supports running on a Monterey host, contact us through our support channels.
:::

### Download the macOS VM and Xcode Images Automatically

<HostCaution512GB/>

To download and extract the Appcircle runner VM and Xcode images in the background automatically, you can run the command below.

<Tabs groupId="macos-image">

  <TabItem value="240306" label="240306">

```bash
curl -fsSL -O https://cdn.appcircle.io/self-hosted/download-runner.sh && \
chmod +x download-runner.sh && \
nohup ./download-runner.sh "240306" &
```

  </TabItem>
  <TabItem value="240514" label="240514">

```bash
curl -fsSL -O https://cdn.appcircle.io/self-hosted/download-runner.sh && \
chmod +x download-runner.sh && \
nohup ./download-runner.sh "240514" &
```

  </TabItem>
  <TabItem value="240918" label="240918" default>

```bash
curl -fsSL -O https://cdn.appcircle.io/self-hosted/download-runner.sh && \
chmod +x download-runner.sh && \
nohup ./download-runner.sh "240918" &
```

  </TabItem>
</Tabs>

:::tip
If you face any errors while downloading the files, please delete the corrupted file and re-run the command block above.
:::

It may take some time to complete with respect to your network speed. You can see and follow the logs with the command below.

```bash
tail -f nohup.out
```

:::info
You can close the SSH or terminal session while the tool is running. The download and extract process will go on in the background.

But be aware that there might be some errors while downloading and extracting the VM image, such as network or disk errors. Please keep an eye on the logs.
:::

:::tip
If no specific image identifier is provided when executing the `download-runner.sh` tool, it will automatically attempt to download the most recent runner images.
:::

## Create Base Images

### Create Base Runner VMs

Apple's virtualization framework allows us to run up to two macOS VMs on host.

:::caution

If you have installed the macOS VM image previously and you're currently trying to upgrade your self-hosted runner environment to another release, first [stop](#stop-vm) the runners if they're online.

Since the below steps will create new `vm01` and `vm02` from the base image, you should also cleanup the current ones using `tart delete` command.

```bash
tart delete vm01
```

```bash
tart delete vm02
```

:::

Each runner must register to the self-hosted Appcircle server with a unique name and configuration. So we will need two VM base images.

When you list VMs with `tart list` command, you should see our extracted VM image in list.

In the steps below, we will create 2 base images named vm01 and vm02.

:::tip
The `vm01` base image is derived from our base image, and subsequently, the `vm02` base image will be created from the `vm01` base image.

This approach eliminates the need to redo all the configurations applied to `vm01` when setting up `vm02`, ensuring efficiency and consistency across both virtual machines.
:::

Create VM image for runner1.

<Tabs groupId="macos-image">

  <TabItem value="240306" label="240306">

```bash
tart clone macOS_240306 vm01
```

  </TabItem>
  <TabItem value="240514" label="240514">

```bash
tart clone macOS_240514 vm01
```

  </TabItem>
  <TabItem value="240918" label="240918" default>

```bash
tart clone macOS_240918 vm01
```

  </TabItem>
</Tabs>

:::tip
It's not recommended to delete the base image (`macOS_YY0M0D`) as it won't save disk space due to copy-on-write file system on macOS. You can safely re-create `vm01` from the same base image `macOS_YY0M0D` without downloading and extracting again from network if needed.
:::

In docker terminology, `vm01` and `vm02` will be our docker images. We will configure them separately, persist our changes and then create containers to execute build pipelines. On every build, fresh containers will be used for both runners.

### Configure Base Runner VMs

Be cautious when updating the base VMs (`vm01` and `vm02`). Any changes made on these base VMs are persisted and may affect disk usage, keychain, and cache files on the runner VMs created from them.

:::warning

If you're freshly creating the base VMs, you can ignore this warning. However, if you've already registered runners to your Appcircle server and want to make updates to the base VMs, it's highly recommended to [disable the runner](/self-hosted-appcircle/self-hosted-runner/configure-runner/manage-runners.md#monitoring-self-hosted-runners) from the Appcircle dashboard to prevent builds from running on the base VMs.

:::

#### Configure Runner 1

Start runner1 VM image for configuration.

<Tabs groupId="macos-image">

  <TabItem value="240306" label="240306">

```bash
screen -d -m tart run vm01 --no-graphics \
  --disk=$HOME/images/xcode.14.3.dmg:ro \
  --disk=$HOME/images/xcode.15.0.dmg:ro \
  --disk=$HOME/images/xcode.15.1.dmg:ro \
  --disk=$HOME/images/xcode.15.2.dmg:ro \
  --disk=$HOME/images/xcode.15.3.dmg:ro
```

  </TabItem>
  <TabItem value="240514" label="240514">

```bash
screen -d -m tart run vm01 --no-graphics \
  --disk=$HOME/images/xcode.14.3.dmg:ro \
  --disk=$HOME/images/xcode.15.0.dmg:ro \
  --disk=$HOME/images/xcode.15.1.dmg:ro \
  --disk=$HOME/images/xcode.15.2.dmg:ro \
  --disk=$HOME/images/xcode.15.3.dmg:ro \
  --disk=$HOME/images/xcode.15.4.dmg:ro
```

  </TabItem>
  <TabItem value="240918" label="240918" default>

```bash
screen -d -m tart run vm01 --no-graphics \
  --disk=$HOME/images/xcode.14.3.dmg:ro \
  --disk=$HOME/images/xcode.15.0.dmg:ro \
  --disk=$HOME/images/xcode.15.1.dmg:ro \
  --disk=$HOME/images/xcode.15.2.dmg:ro \
  --disk=$HOME/images/xcode.15.3.dmg:ro \
  --disk=$HOME/images/xcode.15.4.dmg:ro \
  --disk=$HOME/images/xcode.16.0.dmg:ro \
  --disk=$HOME/images/xcode.16.1.dmg:ro
```

  </TabItem>
</Tabs>

SSH login into running macOS VM.

```bash
ssh -o StrictHostKeyChecking=no appcircle@$(tart ip vm01)
```

---

**Note:** You should use "cicd" as SSH login password.

---

:::info
While trying to connect VM you can get an SSH connection error as below.

```text
ssh: Could not resolve hostname err: nodename nor servname provided, or not known
```

Wait a couple of seconds and let the VM start its internal services. You can try the same command until you connect successfully.
:::

:::info
Since the VM IPs are rotating, it's possible to see the below error when you try to connect to the VM in the long term.

```text
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the ED25519 key sent by the remote host is
SHA256:f6CfksJoc0/ZIqItwH5IJDN87SP6RiOo9q1irzDxawU.
Please contact your system administrator.
Add correct host key in /Users/appcircle/.ssh/known_hosts to get rid of this message.
Offending ED25519 key in /Users/appcircle/.ssh/known_hosts:5
Password authentication is disabled to avoid man-in-the-middle attacks.
Keyboard-interactive authentication is disabled to avoid man-in-the-middle attacks.
UpdateHostkeys is disabled because the host key is not trusted.
appcircle@192.168.64.2: Permission denied (publickey,password,keyboard-interactive).
```

The above example error message indicates that there is an entry for the server `192.168.64.2` located on line 5 of the `known_hosts` file that needs to be removed.

You can delete the old host key entry with the following command and then try re-connecting.

```bash
ssh-keygen -R $(tart ip vm01)
```

:::

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

- Check the latest version from the [Upgrade Runner](/self-hosted-appcircle/self-hosted-runner/update#1-update-runner) page.

- If your version is not up to date, please follow the [Update Runner](/self-hosted-appcircle/self-hosted-runner/update#1-update-runner) section in the page.

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
For more detailed usage, you can check the [Self-signed Certificates](./configure-runner/custom-certificates#adding-certificates) page.
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
  "ASPNETCORE_REDIS_STREAM_ENDPOINT": "redis.appcircle.spacetech.com:443,ssl=true",
  ...
  "ASPNETCORE_BASE_API_URL": "https://api.appcircle.spacetech.com/build/v1"
}
```

- **`ASPNETCORE_NOSHUTDOWN`**: It should be `false`. So, it will shutdown VM when build complete.
- **`ASPNETCORE_BASE_API_URL`**: It should be your self-hosted Appcircle server API URL.
  - The runner will register to server defined here and take the build jobs from there.

:::tip

The latest macOS VM image,`macOS_240221` or later, has the ASPNETCORE_NOSHUTDOWN setting as `false` by default and has no pre-defined ASPNETCORE_BASE_API_URL setting in the `appsettings.json` file.

So, if you did not upgrade the packaged self-hosted runner at [previous steps](#1-check-the-runner-version) above, only modifying the ASPNETCORE_BASE_API_URL value with the following command should be enough for the configuration up-to-here.

```bash
echo "$(jq '.ASPNETCORE_BASE_API_URL="https://api.test-appcircle.tool.zb/build/v1"' appsettings.json)" > appsettings.json
```

If you upgraded the self-hosted runner, you must also modify the ASPNETCORE_NOSHUTDOWN setting as well.

```bash
echo "$(jq '.ASPNETCORE_NOSHUTDOWN="false"' appsettings.json)" > appsettings.json
```

:::

- **`ASPNETCORE_REDIS_STREAM_ENDPOINT`**: It should be your self-hosted Appcircle server's Redis URL, port, and SSL settings.  
  - If you are using the Appcircle server with HTTPS, then the port should be `443` and the `ssl` argument should be set to `true`.
  - If you are using the Appcircle server with HTTP, then the port should be the external port of Redis which is `6379` by default. And the `ssl` argument should be set to `false`.
    - For instance, `redis.appcircle.spacetech.com:6379,ssl=false`.

<NewRunnerOldServerRedisCaution/>

Create runner access token from appcircle server and register runner to server. See details in [here](/self-hosted-appcircle/self-hosted-runner/installation#2-register).

For example,

```bash
./ac-runner register -t aat_eev4NQdG_7F2jodmMShBFhh_DgabOJSsWSMojX5_lo4 -n runner1 -p macOS_pool
```

It won't print anything to CLI on success. You can also check its exit value with `echo $?`. It should be `0` on success.

Finally run below command to edit self-hosted runner configuration for pre-installed platforms.

```bash
echo "$(jq '.OsValues = ["ios","android"]' selfHosted.json)" > selfHosted.json
```

Start runner service.

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

<Tabs groupId="macos-image">

  <TabItem value="240306" label="240306">

```bash
screen -d -m tart run vm02 --no-graphics \
  --disk=$HOME/images/xcode.14.3.dmg:ro \
  --disk=$HOME/images/xcode.15.0.dmg:ro \
  --disk=$HOME/images/xcode.15.1.dmg:ro \
  --disk=$HOME/images/xcode.15.2.dmg:ro \
  --disk=$HOME/images/xcode.15.3.dmg:ro
```

  </TabItem>
  <TabItem value="240514" label="240514">

```bash
screen -d -m tart run vm02 --no-graphics \
  --disk=$HOME/images/xcode.14.3.dmg:ro \
  --disk=$HOME/images/xcode.15.0.dmg:ro \
  --disk=$HOME/images/xcode.15.1.dmg:ro \
  --disk=$HOME/images/xcode.15.2.dmg:ro \
  --disk=$HOME/images/xcode.15.3.dmg:ro \
  --disk=$HOME/images/xcode.15.4.dmg:ro
```

  </TabItem>
  <TabItem value="240918" label="240918" default>

```bash
screen -d -m tart run vm02 --no-graphics \
  --disk=$HOME/images/xcode.14.3.dmg:ro \
  --disk=$HOME/images/xcode.15.0.dmg:ro \
  --disk=$HOME/images/xcode.15.1.dmg:ro \
  --disk=$HOME/images/xcode.15.2.dmg:ro \
  --disk=$HOME/images/xcode.15.3.dmg:ro \
  --disk=$HOME/images/xcode.15.4.dmg:ro \
  --disk=$HOME/images/xcode.16.0.dmg:ro \
  --disk=$HOME/images/xcode.16.1.dmg:ro
```

  </TabItem>
</Tabs>

SSH login into running macOS VM.

```bash
ssh -o StrictHostKeyChecking=no appcircle@$(tart ip vm02)
```

After login, configuration steps for Appcircle runner service are the same as "runner1". So, we don't need to repeat same commands again.

The only difference should be runner naming. It must be unique. For the second runner, just give a different name. For example, "runner2".

Refer to the [Configure Runner Service](#4-configure-runner-service) for detailed Appcircle runner service configuration.

After shutdown, we're ready to run instances from `vm01` and `vm02` base VM images.

At this stage, your VM list returned by `tart list` might be like below, according to your preferred macOS VM image version.

```txt
Source Name         Size
local  macOS_240306 167
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

<Tabs groupId="macos-image">

  <TabItem value="240306" label="240306">

```bash
curl -L -o $HOME/runner1/run.sh https://storage.googleapis.com/appcircle-dev-common/self-hosted/run-1.0.3.sh && \
chmod u+x $HOME/runner1/run.sh
```

  </TabItem>
  <TabItem value="240514" label="240514">

```bash
curl -L -o $HOME/runner1/run.sh https://storage.googleapis.com/appcircle-dev-common/self-hosted/run-1.0.4.sh && \
chmod u+x $HOME/runner1/run.sh
```

  </TabItem>
  <TabItem value="240918" label="240918" default>

```bash
curl -L -o $HOME/runner1/run.sh https://storage.googleapis.com/appcircle-dev-common/self-hosted/run-1.0.5.sh && \
chmod u+x $HOME/runner1/run.sh
```

  </TabItem>
</Tabs>

For "runner2" use below commands.

<Tabs groupId="macos-image">

  <TabItem value="240306" label="240306">

```bash
curl -L -o $HOME/runner2/run.sh https://storage.googleapis.com/appcircle-dev-common/self-hosted/run-1.0.3.sh && \
chmod u+x $HOME/runner2/run.sh
```

  </TabItem>
  <TabItem value="240514" label="240514">

```bash
curl -L -o $HOME/runner2/run.sh https://storage.googleapis.com/appcircle-dev-common/self-hosted/run-1.0.4.sh && \
chmod u+x $HOME/runner2/run.sh
```

  </TabItem>
  <TabItem value="240918" label="240918" default>

```bash
curl -L -o $HOME/runner2/run.sh https://storage.googleapis.com/appcircle-dev-common/self-hosted/run-1.0.5.sh && \
chmod u+x $HOME/runner2/run.sh
```

  </TabItem>
</Tabs>

:::caution
With new versions of the macOS VM image, we're also constantly updating the `run.sh` tool for fixes and improvements.

So, there might be a new version of `run.sh` that's compatible with the latest macOS VM image.

The above commands should be executed on every macOS VM image upgrade in order to get the latest `run.sh` version that's compatible with the latest macOS VM image.
:::

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
local  macOS_240306                              167
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

If runner is executing build pipeline, you may prefer waiting completion of the build job. See [stop](/self-hosted-appcircle/self-hosted-runner/configure-runner/runner-service#stop) section at self-hosted runner docs. When executing build pipeline completes, runner will be shutdown automatically.

On the other hand if you want to stop runner immediately for whatever reason or it's in idle state, you can SSH into runner and run shutdown command.

First you need to have to find out online runner's VM name from `tart list`.

```txt
Source Name                                      Size
local  macOS_240306                              167
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
local  macOS_240306                              167
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
- You may prefer to get iOS and android tool updates by using [self-hosted runner update](/self-hosted-appcircle/self-hosted-runner/update) method instead of getting fresh macOS VM image. When you get fresh macOS image you may need to make your custom configurations again.
- You may need to make persistent proxy configuration for your internal network requirements.
- You may need to add your corporate's self-signed root CAs to macOS VM image in order to succeed SSL connections.

Steps, that we need to take, are technically similar as in [Create Base Images](#create-base-images) section. So, a conceptual overview of the steps will be sufficient.

- Stop all online runners as explained in [Stop VM](#stop-vm) section.
- Run `vm01` base image.

<Tabs groupId="macos-image">

  <TabItem value="240306" label="240306">

```bash
screen -d -m tart run vm01 --no-graphics \
  --disk=$HOME/images/xcode.14.3.dmg:ro \
  --disk=$HOME/images/xcode.15.0.dmg:ro \
  --disk=$HOME/images/xcode.15.1.dmg:ro \
  --disk=$HOME/images/xcode.15.2.dmg:ro \
  --disk=$HOME/images/xcode.15.3.dmg:ro
```

  </TabItem>
  <TabItem value="240514" label="240514">

```bash
screen -d -m tart run vm01 --no-graphics \
  --disk=$HOME/images/xcode.14.3.dmg:ro \
  --disk=$HOME/images/xcode.15.0.dmg:ro \
  --disk=$HOME/images/xcode.15.1.dmg:ro \
  --disk=$HOME/images/xcode.15.2.dmg:ro \
  --disk=$HOME/images/xcode.15.3.dmg:ro \
  --disk=$HOME/images/xcode.15.4.dmg:ro
```

  </TabItem>
  <TabItem value="240918" label="240918" default>

```bash
screen -d -m tart run vm01 --no-graphics \
  --disk=$HOME/images/xcode.14.3.dmg:ro \
  --disk=$HOME/images/xcode.15.0.dmg:ro \
  --disk=$HOME/images/xcode.15.1.dmg:ro \
  --disk=$HOME/images/xcode.15.2.dmg:ro \
  --disk=$HOME/images/xcode.15.3.dmg:ro \
  --disk=$HOME/images/xcode.15.4.dmg:ro \
  --disk=$HOME/images/xcode.16.0.dmg:ro \
  --disk=$HOME/images/xcode.16.1.dmg:ro
```

  </TabItem>
</Tabs>

- SSH into `vm01`.

```bash
ssh -o StrictHostKeyChecking=no appcircle@$(tart ip vm01)
```

- Make your modifications, configurations or updates in macOS.
- Shutdown `vm01`.
- Run `vm02` base image.

<Tabs groupId="macos-image">

  <TabItem value="240306" label="240306">

```bash
screen -d -m tart run vm02 --no-graphics \
  --disk=$HOME/images/xcode.14.3.dmg:ro \
  --disk=$HOME/images/xcode.15.0.dmg:ro \
  --disk=$HOME/images/xcode.15.1.dmg:ro \
  --disk=$HOME/images/xcode.15.2.dmg:ro \
  --disk=$HOME/images/xcode.15.3.dmg:ro
```

  </TabItem>
  <TabItem value="240514" label="240514">

```bash
screen -d -m tart run vm02 --no-graphics \
  --disk=$HOME/images/xcode.14.3.dmg:ro \
  --disk=$HOME/images/xcode.15.0.dmg:ro \
  --disk=$HOME/images/xcode.15.1.dmg:ro \
  --disk=$HOME/images/xcode.15.2.dmg:ro \
  --disk=$HOME/images/xcode.15.3.dmg:ro \
  --disk=$HOME/images/xcode.15.4.dmg:ro
```

  </TabItem>
  <TabItem value="240918" label="240918" default>

```bash
screen -d -m tart run vm02 --no-graphics \
  --disk=$HOME/images/xcode.14.3.dmg:ro \
  --disk=$HOME/images/xcode.15.0.dmg:ro \
  --disk=$HOME/images/xcode.15.1.dmg:ro \
  --disk=$HOME/images/xcode.15.2.dmg:ro \
  --disk=$HOME/images/xcode.15.3.dmg:ro \
  --disk=$HOME/images/xcode.15.4.dmg:ro \
  --disk=$HOME/images/xcode.16.0.dmg:ro \
  --disk=$HOME/images/xcode.16.1.dmg:ro
```

  </TabItem>
</Tabs>

- SSH into `vm02`.

```bash
ssh -o StrictHostKeyChecking=no appcircle@$(tart ip vm02)
```

- Make your modifications, configurations or updates in macOS.
- Shutdown `vm02`.
- Start offline runners as explained in [Start VM](#start-vm) section.

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

In order to be able to investigate root cause, you should learn the basics of self-hosted runner. Check our [online docs](/self-hosted-appcircle/self-hosted-runner) details.

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

For configuring NTP settings, see [Configure Base Runner's NTP Settings](#2-configure-base-runners-ntp-settings) section above.

### I am facing "SSL cert is not valid yet" error in our builds

This problem is again related to your macOS VM date and time being out of date.

To fix that, you should sync the VMs' date and time with your organization's NTP server.

For updating macOS base image see [related section](#update-base-images) above.

For configuring NTP settings, see [Configure Base Runner's NTP Settings](#2-configure-base-runners-ntp-settings) section above.

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

### Deleting Xcode simulator runtimes to create free disk space

Occasionally, you may need to manage disk space on your macOS base VM due to storage constraints or other reasons. One way to free up disk space is by deleting unused Xcode simulator runtimes.

To list the installed Xcode simulator runtimes, run the following command on your base VM:

```bash
xcrun simctl runtime list 2>/dev/null
```

If you determine that certain iOS, watchOS, tvOS or visionOS(xrOS) runtimes are not needed, you can delete them to free up disk space:

```bash
xcrun simctl runtime delete <runtime_id>
```

:::caution
Xcode simulator runtimes are essential for testing and debugging iOS, watchOS, and tvOS applications on virtual devices. Deleting a runtime will prevent you from running or debugging an app on that specific device. Other simulators and runtimes will remain unaffected.

Be cautious when deleting Xcode simulator runtimes, as this action is irreversible. Removing a simulator runtime can impact the Xcode build process. For example, if you delete a watchOS runtime, you will no longer be able to build an iOS app that targets the deleted watchOS runtime. Ensure that the runtime you plan to delete is not required for your build pipeline.
:::
