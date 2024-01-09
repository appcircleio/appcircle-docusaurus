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

- You should contact us to get the license file for accessing to the Appcircle Google cloud resources such as container images.

- If you are a licensed user, you should contact us to the licensed Appcircle server package with your actual license.

- If you are a PoC user, you can go on with the package located in the AMI.

### Technical Requirements

Before using the Appcircle server AMI, there is a couple of things that you need to handle.

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

Basic familiarity with Linux system configurations and commands is essential since this document will use linux commands.

## Creating an Appcircle Server From the AMI

After you meet all the requirements discussed above, you can follow the steps below to create an Appcircle server from the AMI.

- Login to the AWS console with your account.

- Select the region from right upper corner.

- Head to the EC2 menu to create EC2 instance.

- Click on "Launch Instance" button from the EC2 dashboard.

- You should fill the required fields as your needs such as:

  - Instance name
  - AMI
  - Instance type
  - Key pair (optional but required for secure access)
  - Network settings
  - Storage

- Select the AMI.

- We will use `t2.xlarge` instance type since it meets the minimum requirements.

  - For details you can head to the [Hardware Requirements](../docker.md#hardware-requirements) section.

- Select an existing Key pair or click on "Create new key pair" button if you don't have any on the AWS console.

- For the network settings:

  - We will use the default VPC.
  - Allow HTTP and HTTPS traffic from the internet.
    - This is required for accessing to the Appcircle dashboard.
  - You can restrict the SSH request by specifying the source IP addresses.
    - SSH is also required to access to the server.

- For storage, you can select 100GB for a PoC setup.

  - You can see the recommended storage sizes in the [Hardware Requirements](../docker.md#hardware-requirements) section.

- You can see an example configuration in the screenshots below 👇:

- AMI configuration:

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2503-aws9-ami1.png' />
<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2503-aws10-ami2.png' />
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

:::

- You can head to the EC2 Instances page to see if your server is up and running.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2503-aws5-instance-running.png' />

## Configuring Appcircle Server EC2 Instance

After you have successfully created an EC2 instance from the Appcircle server AMI, you can follow the steps below to configure it.

- Get the IP address of the instance.

- Use and SSH tool like `Putty` on windows, `ssh` command on macOS and linux to connect to the instance.

  - The `ssh` command below is for macOS and linux. The other commands are same after you connect to the instance.

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

- If you are licensed user, you should get the licensed Appcircle zip package from us.

  - Please contact us with a communication channel if you don't have it already.

- In the `appcircle-server` directory, copy the content of `cred.json` file you received from us to a file named `cred.json`. The file name is important.

  - If you don't have `cred.json` file, you can contact us to get it.

- The Appcircle server is ready to be [Configured](../docker.md#3-configure) for your project.

- You should also handle the [DNS](../docker.md#4-dns-settings) settings. Create `A` and `CNAME` record for your instances.

- After the configuration and running the server, you can access to the Appcircle dashboard with the [domain](../docker.md#4-dns-settings) of your server.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2503-aws8-dashboard.png' />

- 🎉 You can now enjoy using the Appcircle and build your mobile applications.

- 📚 For the quick start tutorials for building mobile apps, you can head to the [Tutorials](../../../tutorials) page.
