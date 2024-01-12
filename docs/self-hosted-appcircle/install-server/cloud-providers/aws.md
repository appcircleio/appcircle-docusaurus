---
title: Amazon Web Services (AWS)
metaTitle: Amazon Web Services (AWS)
metaDescription: Appcircle Server on AWS
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';

## Overview

An Appcircle server Amazon Machine Image (AMI) is a pre-configured template used to create virtual servers, known as instances, in the Amazon Web Services (AWS) environment.

Think of it as a snapshot of a server that includes the operating system, necessary tools, applications, and any additional services needed to run the Appcircle server.

## Pre-requirements

### Appcircle Requirements

- You should contact us to get the license file for accessing to the Appcircle Google cloud resources, such as container images.

- If you are a licensed user, you should contact us about the licensed Appcircle server package with your actual license.

- If you are a PoC user, you can go on with the package located in the AMI.

### Technical Requirements

Before using the Appcircle server AMI, there are a couple of things that you need to handle.

- AWS Account

You must have an active AWS account with appropriate permissions to launch EC2 instances and work with other related services.

- Understanding of AWS Services

A basic understanding of Amazon Web Services (AWS) services, particularly EC2 (Elastic Compute Cloud), is beneficial.

You should be familiar with instance creation, networking, security groups, and storage configurations.

- Networking and Security Configuration

You might need to configure networking aspects such as Virtual Private Cloud (VPC), subnets, route tables, and security groups to properly integrate the instance within their network environment and manage access controls.

- SSH Key Pairs for Secure Access

You need an SSH key pair to access to the server that you will create securely.

- Linux System Configuration

Basic familiarity with Linux system configurations and commands is essential since this document will use Linux commands.

## Creating an Appcircle Server From the AMI

After you meet all the requirements discussed above, you can follow the steps below to create an Appcircle server from the AMI.

- Log in to the AWS console with your account.

- Select the region from the right upper corner.

- Head to the EC2 menu to create an EC2 instance.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2503-aws23-region-menu.png' />

- Click on the "Launch Instance" button from the EC2 dashboard.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2503-aws24-launch-ec2.png' />

- You should fill out the required fields as per your needs, such as:

  - Instance name
  - AMI
  - Instance type
  - Key pair (optional but required for secure access)
  - Network settings
  - Storage

- Select the AMI.

- We will use the `t2.xlarge` instance type since it meets the minimum requirements.

  - For details, you can head to the [Hardware Requirements](../docker.md#hardware-requirements) section.

- Select an existing key pair or click on the "Create new key pair" button if you don't have any on the AWS console.

- For the network settings:

  - We will use the default VPC.
  - Allow HTTP and HTTPS traffic from the internet.
    - This is required for accessing to the Appcircle dashboard.
  - You can restrict the SSH request by specifying the source IP addresses.
    - SSH is also required to access to the server.

- For storage, you can select 100GB for a PoC setup.

  - You can see the recommended storage sizes in the [Hardware Requirements](../docker.md#hardware-requirements) section.

- You can see an example configuration in the screenshots below 👇:

- Click ""Browse more AMIs" button to search for Appcircle AMI :

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2503-aws9-ami1.png' />

- Search for "Appcircle" in the "AWS Marketplace AMIs" tab and click "Select" on the AMI:

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2503-aws10-ami2.png' />

- Click "Continue" to select Appcircle server AMI.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2503-aws11-ami3.png' />

- Instance type and SSH key configuration:

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2503-aws14-instance-type.png' />

- Network configuration:

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2503-aws15-network.png' />

- Storage configuration:

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2503-aws16-storage.png' />

- You can click on the `Launch Instance` button to create the instance with the configuration you made.

:::info

The instance creation may take some time due to AWS AMI subscriptions.

Please wait patiently while the AWS is creating your Appcircle server instance.

You can check the subscription in the "AWS Marketplace Subscriptions" service in the AWS console.

If the instance is not created within 2 hours, you can follow the steps above and launch it again.

:::

- You can head to the EC2 Instances page to see if your server is up and running.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2503-aws18-instance-running.png' />

- To enable SSH access, head to the security group settings of your "Appcircle server".

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2503-aws19-ssh1.png' />

- Edit the inbound rules to add SSH access.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2503-aws20-ssh2.png' />

- Add the SSH rule for ip addresses you want hit "Save Rules" button to save the settings.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2503-aws21-ssh3.png' />

## Configuring Appcircle Server EC2 Instance

After you have successfully created an EC2 instance from the Appcircle server AMI, you can follow the steps below to configure it.

- Get the IP address of the instance from EC2 dashboard.

- Use a SSH tool like `Putty` on windows, `ssh` command on macOS and Linux to connect to the instance.

:::info
The `ssh` command below is for macOS and Linux. The other commands are same after you connect to the instance.
:::

- Locate the SSH private key of the public key if you used to create the instance.

```bash
ssh -i "/path/to/your/private/ssh/key" ubuntu@ip-address-of-the-instance
```

- For example 👇:

```bash
ssh -i "/home/spacetech/.ssh/id_rsa" ubuntu@34.205.139.17
```

- The SSH command may ask you to add this server to the known hosts list. You can write `yes` and hit enter.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2503-aws6-ssh.png' />

- After you connect to the Appcircle instance, the first thing you should do is a system update. Although the Appcircle AMI is up to date, it is recommended that you perform security updates again.

```bash
sudo apt update && \
sudo apt upgrade
```

- The Appcircle Server directory is located in the `$HOME` directory.

```bash
ls -l "$HOME"
```

- You can go into the `appcircle-server` directory to start configuring the Appcircle

```bash
cd "$HOME/appcircle-server"
```

:::info

**If you are licensed user**, you should get the licensed Appcircle zip package via contacting us and [Update](../../update.md) the package in the server.

Also, in the `appcircle-server` directory, copy the content of `cred.json` file you received from us to a file named `cred.json`. Please ensure that the file name is `cred.json`.

Please contact us with a communication channel if you don't have the licensed package and `cred.json` already.

:::

- The Appcircle server is ready to be [Configured](../docker.md#3-configure) for your project.

- You should also handle the [DNS](../docker.md#4-dns-settings) settings. Create `A` and `CNAME` record for your instance.

- After the configuration and running the server, you can access to the Appcircle dashboard with the [domain](../docker.md#4-dns-settings) of your server.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2503-aws22-dashboard.png' />

- 🎉 You can now enjoy using the Appcircle and build your mobile applications.

- 📚 For the quick start tutorials for building mobile apps, you can head to the [Tutorials](../../../tutorials) page.

## Connecting Runners

When you complete installation successfully by following above steps, you're ready for your first build. :tada:

But in order to run build pipelines, you need to install and connect self-hosted runners. We have dedicated section for installation and configuration of self-hosted runners.

Follow and apply related guidelines in [here](../self-hosted-runner/installation.md).

Self-hosted runner section in docs, has all details about runners and their configuration.

:::caution

By default, self-hosted runner package has pre-configured `ASPNETCORE_BASE_API_URL` for Appcircle-hosted cloud.

- `https://api.appcircle.io/build/v1`

:point_up: You need to change its value with your self-hosted Appcircle server's API URL.

Assuming our sample scenario explained above, its value should be

- `http://api.appcircle.spacetech.com/build/v1`

for our example configuration.

:reminder_ribbon: After [download](../self-hosted-runner/installation.md#1-download), open `appsettings.json` with a text editor and change `ASPNETCORE_BASE_API_URL` value according to your configuration.

Please note that, you should do this before [register](../self-hosted-runner/installation.md#2-register).

:::

Considering system performance, it will be good to install self-hosted runners to other machines. Self-hosted Appcircle server should run on a dedicated machine itself.

You can install any number of runners regarding to your needs and connect them to self-hosted Appcircle server.
