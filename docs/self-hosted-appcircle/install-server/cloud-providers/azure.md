---
title: Microsoft Azure Integration
description: Learn how to create an Appcircle server instance on Microsoft Azure
tags:
  [self-hosted, appcircle server, microsoft azure, azure cloud, instance, image]
sidebar_position: 1
sidebar_label: Microsoft Azure
---

import AppcircleLicenseRequirement from '@site/docs/self-hosted-appcircle/install-server/cloud-providers/\_license-requirement.mdx';
import ConnectingRunners from '@site/docs/self-hosted-appcircle/install-server/cloud-providers/\_connecting-runners.mdx';
import ConfigureServer from '@site/docs/self-hosted-appcircle/install-server/cloud-providers/\_configure-server.mdx';
import Screenshot from '@site/src/components/Screenshot';
import NeedHelp from '@site/docs/\_need-help.mdx';


## Overview

An Appcircle server image is a pre-configured template used to create virtual server, known as "virtual machines", in the Microsoft Azure environment.

Think of it as a snapshot of a server that includes the operating system, necessary tools, applications, and any additional services needed to run the Appcircle server.

This documentation provides step-by-step instructions for configuring and setting up Appcircle Server on Microsoft Azure. Follow these guidelines to ensure a successful deployment.

## Pre-requirements

### Appcircle Requirements

<AppcircleLicenseRequirement />

### Technical Requirements

Before using the Appcircle server image, there are a couple of things that you need to handle.

#### Microsoft Azure Account

You should have an active Azure account with appropriate permissions to launch virtual machines and work with other related services.

#### Understanding of Azure Services

A basic understanding of Azure services, particularly Virtual Machines, is beneficial.

You should be familiar with virtual machine creation, networking, security groups, and storage configurations.

##### 1. Networking and Security Configuration

You might need to configure networking aspects such as Virtual networks, subnets, route tables, and security groups to properly integrate the instance within the network environment and manage access controls.

##### 2. SSH Key Pairs for Secure Access

You need an SSH key pair to access to the server that you will create securely.

##### 3. Linux System Configuration

Basic familiarity with Linux system configurations and commands is essential since this document will use Linux commands.

## Creating an Appcircle Server from the server image

After you meet all the requirements discussed above, you can follow the steps below to create an Appcircle server from the server image.

- Log in to the Microsoft Azure with your account.

- Head to the Virtual machines menu to create a virtual machine.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4345-1-virtual-machine-menu.png' />

- Click on the "+ Create" button and "Azure virtual machine" from the virtual machines dashboard.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4345-2-create-vm-button.png' />

You should fill out the required fields as per your needs. Please follow the below steps for a sample instance configuration.

- Select the Subscription and Resource group for your needs.

- Enter an virtual machine name in the "Instance details" field. For example, "My-Appcircle-Server".

- Choose which region you want the server to be in.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4345-3-create-vm-1.png' />

- In order to select the Appcircle server image, click on the "See all images" button and search for the Appcircle server image.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4345-4-create-vm-2-see-all-images.png' />

- Search for "Appcircle" in the "Marketplace" tab and click on the "Select" button for the server image and select "Gen2".

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4345-5-create-vm-3-select-appcircle-image.png' />

- We will use the `Standart_B4ms` size for our sample configuration since it meets the minimum requirements for the vCPU count and memory size.

:::info
For the details about minimum hardware requirements, you should see the [Hardware Requirements](/self-hosted-appcircle/install-server/docker#hardware-requirements) section.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4345-11-machine-type.png' />

- We highly recommend changing the Username to `ubuntu`.

- Select an existing key pair or click on the "Generate new key pair" button if you don't have any on the Azure. In the sample configuration, we will use an existing key stored in Azure by selecting from the dropdown menu.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4345-6-create-vm-authentication.png' />

- From the Disks menu, configure the OS disk size. By default, the image comes with 100GiB disk space. You can increase that size for your needs.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4345-7-create-vm-disks.png' />

:::info
You should see the recommended storage sizes and other disk requirements in the [Hardware Requirements](/self-hosted-appcircle/install-server/docker#hardware-requirements) section.
:::

- We will use default Virtual network that Azure provides. You can customize the network according to your needs, such as limiting incoming traffic to known IP addresses for SSH connections.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4345-8-create-vm-network.png' />

Now you're ready to click on the **Review + create** & **Create** button to create the virtual machine with the configuration you made.

After the deployment is completed, you can click **Go to resource** button, or head to the **Virtual machines** service to see the deployed instance.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4345-9-create-vm-successful.png' />

:::tip
By default, `80`, `443` and `22` ports are allowed on the firewall.

If you want send `ping` requests to the instance for health check purposes, you should add a inbound port rule with the protocol "ICMPv4" from the networking tab of the virtual machine.
:::

## Configuring the Appcircle Server Instance

### Connect via SSH

After you have successfully created an Virtual machine from the Appcircle server image, you can follow the steps below to configure it.

- Get the IP address of the instance from Virtual machines dashboard.

- Locate the SSH key pair, especially the private key, that you've created or used while configuring the virtual machine.

- Get an SSH connection tool like `putty` on Windows or `ssh` on macOS and Linux to connect to the instance.

:::info
The `ssh` command below is for macOS and Linux. The other commands are the same after you connect to the instance.
:::

Using **private key** and **IP address**, you can connect to the instance with SSH as seen below.

```bash
ssh -i "/path/to/your/private/key" ubuntu@ip-address-of-the-instance
```

:::info
The default user for the Appcircle server image is `ubuntu` if you have followed the [Creating Virtual Machine](#creating-an-appcircle-server-from-the-server-image) section above.

So, let's assume that your instance IP address is `34.205.139.17` and your private SSH key path is `/home/spacetech/.ssh/id_rsa`.

You can connect to the instance using the below command on macOS or Linux.

```bash
ssh -i "/home/spacetech/.ssh/id_rsa" ubuntu@34.205.139.17
```

:::

:::tip
When you "Create new key pair" while creating the instance from Appcircle server image, the downloaded private key might cause a permission error when you try to connect to the instance. For instance;

> ... Permissions 0644 for 'MyCICDSSHKey.pem' are too open.
> It is required that zour private key files are NOT accessible by others.
> This private key will be ignored. ...

In this case, you need to change the permissions of the private key using the below command before connecting.

```bash
chmod 600 "/path/to/your/private/key"
```

It will be a one-time-operation that should be done once per private key.

:::

:::info
The SSH command may ask you to add this server to the list of known hosts. You should write `yes` and hit enter.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2503-aws6-ssh.png' />

:::


### Configure Server

<ConfigureServer />

## Connecting Runners

<ConnectingRunners />

<NeedHelp />

Have questions? [Contact us here.](https://appcircle.io/support/)
