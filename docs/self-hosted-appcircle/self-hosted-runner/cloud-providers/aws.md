---
title: Amazon Web Services (AWS)
description: Learn how to create a self-hosted Appcircle runner instance on Amazon Web Services (AWS).
tags: [self-hosted, self-hosted runner, cloud providers, aws, amazon web services, EC2]
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';
import NeedHelp from '@site/docs/\_need-help.mdx';
import RegisterAppcircleRunner from '@site/docs/self-hosted-appcircle/self-hosted-runner/\_register-runner.mdx';
import ConfigureAppcircleRunner from '@site/docs/self-hosted-appcircle/self-hosted-runner/\_configure-runner.mdx';
import RunAppcircleRunner from '@site/docs/self-hosted-appcircle/self-hosted-runner/\_run-service.mdx';
import BuildAppOutro from '@site/docs/self-hosted-appcircle/self-hosted-runner/\_build-app-outro.mdx';

## Overview

In this document, you will see how to create a self-hosted Appcircle runner instance on Amazon Web Services (AWS).

By following the steps below, you will create a dedicated host, Sonoma macOS, from the base AMI, install the Appcircle runner, and make it ready to build Android and iOS applications, just like in the Appcircle cloud.

## Pre-requirements

### Appcircle Requirements

You can use a self-hosted Appcircle runner with your self-hosted Appcircle server or Appcircle cloud account.

:::danger

The only requirement for using self-hosted runners is to be in `enterprise` plan.

See [pricing](https://appcircle.io/pricing) and feature comparison table for details.

:::

### Technical Requirements

Before creating an Appcircle runner on AWS, there are a couple of things that you need to handle.

#### AWS Account

You must have an active AWS account with appropriate permissions to launch EC2 instances and work with other related services.

#### Understanding of AWS Services

A basic understanding of Amazon Web Services (AWS) services, particularly EC2 (Elastic Compute Cloud), is beneficial.

You should be familiar with instance creation, networking, security groups, and storage configurations.

##### 1. Networking and Security Configuration

You might need to configure networking aspects such as Virtual Private Cloud (VPC), subnets, route tables, and security groups to properly integrate the instance within the network environment and manage access controls.

##### 2. SSH Key Pairs for Secure Access

You need an SSH key pair to access to the server that you will create securely.

##### 3. MacOS System Configuration

Basic familiarity with macOS system configurations and commands is essential since this document will use macOS commands.

:::info

MacOS is a Unix-like operating system, much like Linux, which means that many of the commands and underlying principles are similar.

If you have experience with Linux, installing the Appcircle runner on macOS should be a seamless process.

:::

##### 4. Dedicated Hosts and EC2 Mac Instances

While the process of creating an EC2 Mac instance on AWS differs slightly from creating a Linux instance, the key distinction lies in the requirement of a dedicated host.

After selecting a macOS image during the instance creation process, users must specify the dedicated host they have previously provisioned, as outlined in the AWS [documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-mac-instances.html) for comprehensive guidance.

Furthermore, detailed instructions are provided below on creating a dedicated Mac instance, ensuring you have the necessary resources for seamless operation.

However, please make sure that you have a dedicated host service quota before proceeding to create a dedicated host.

For more details about the AWS EC2 Mac instances, you can refer to the [documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-mac-instances.html).

## Creating a Mac Instance for the Appcircle Runner

After you meet all the requirements discussed above, you can follow the steps below to create a Mac instance for the Appcircle runner installation.

### Creating a Dedicated Host for EC2 Mac Instance

- Log in to the AWS console with your account.

- Select the region from the right upper corner.

:::tip

If you have a self-hosted Appcircle server in AWS, it's better to deploy the self-hosted Appcircle runner in the same region as the Appcircle server.

This approach will reduce the latency between two machines.

:::
#### Check and Request the Dedicated Mac Instance Quota

Before creating the dedicated host instance, you should check the dedicated service quota.

- Head to the "Service Quotas" menu.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2757-aws13-dashboard.png' />

- Click on the "AWS services". Filter the EC2 services as below, and then click on the "Amazon Elastic Compute Cloud (Amazon EC2)" service.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2757-aws14-quotas-dashboard.png' />

- Filter the services by "dedicated mac2" and select the relevant instance type service quota.

  - In this tutorial, we will use "mac2" hosts.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2757-aws15-dedicated-hosts.png' />

If the "applied account-level quota value" is `0`, then you should request an increase as below.

- For your first quota request, you can request `1` quota.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2757-aws16-request.png' />

#### Create the Dedicated Host

- Head to the EC2 menu to create an dedicated instance.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2757-aws1-dashboard.png' />

- Head to the "Dedicated Hosts" menu and click on the "Allocate Dedicated Host" button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2757-aws2-dedicated-host-dashboard.png' />

- Enter a dedicated instance name in the "Name tag" field. For example, "Appcircle Dedicated Host".

- Then you should select the **instance family**, **instance type** and the **availability zone**. For example, `mac2` for the instance family and `mac2.metal` for the instance type.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2757-aws3-dedicated-host-launch-1.png' />

:::info

You must select one of the **`mac2`**, **`mac2-m2`** or **`mac2-m2pro`** instance families since the Appcircle runner is supported on these instance families.

In the AWS [documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-mac-instances.html), you can find the underlying infrastructure listed below.

> - EC2 M1 Mac instances (mac2.metal) are built on 2020 Mac mini hardware powered by Apple silicon M1 processors.
>
> - EC2 M2 Mac instances (mac2-m2.metal) are built on 2023 Mac mini hardware powered by Apple silicon M2 processors.
>
> - EC2 M2 Pro Mac instances (mac2-m2pro.metal) are built on 2023 Mac mini hardware powered by Apple silicon M2 Pro processors.

:::

- Since the Mac instances doesn't support "Host maintenance", you must uncheck it.

- Click on the "Allocate" button to create your dedicated host.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2757-aws4-dedicated-host-launch-2.png' />

- You can see the created dedicated host on the **Dedicated Hosts** dashboard.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2757-aws5-dedicated-host-created.png' />

- When you see the state of the dedicated host as "Available", you can continue with creating EC2 Mac instance.

:::tip
If you have more than one dedicated hosts, make a note of the dedicated **Host ID** to avoid confusion when creating the EC2 Mac instance.
:::

### Creating an EC2 Mac Instance on the Dedicated Host

- Head to the EC2 menu to create an EC2 Mac instance.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2757-aws1-dashboard.png' />

- Click on the "Launch Instance" button from the EC2 dashboard.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2757-aws6-ec2-dashboard.png' />

You should fill out the required fields as per your needs. Please follow the below steps for a sample instance configuration.

- Enter an instance name in the "Name and Tags" field. For example, "My Appcircle Runner".

- In order to select the AMI, click on the "macOS" button. Then select "macOS Sonoma" from the AMI drop-down menu. And for the architecture, select "64-bit (Mac-Arm)".

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2757-aws7-ec2-ami.png' />

- We will use the `mac2.metal` instance type for our sample configuration since we have crated a `mac2.metal` dedicated host [above](#creating-a-dedicated-host-for-ec2-mac-instance).

:::caution
If you have created another type of dedicated host, like `mac2-m2.metal` or `mac2-m2pro.metal`, you should choose them from the menu.
:::

- Select an existing key pair or click on the "Create new key pair" button if you don't have any on the AWS console.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2757-aws8-ec2-type.png' />

- For the network settings:
  - We will use the default VPC created on the form.
  - Don't allow HTTP and HTTPS traffic from the internet.
    - The Appcircle runner doesn't require accepting any incoming HTTP(S) requests.
  - You can restrict the SSH connection by specifying the source IP addresses.
    - **SSH is required** to access the runner from the command line.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2757-aws9-ec2-network.png' />

- For the storage, you should select a minimum 300 GB disk for a runner that will build Android and iOS applications with three Xcode versions.
  - For each Xcode version you plan to install side by side, you should add 50 GB of disk space, roughly.
  - In this tutorial, we will install the latest (_at the moment_) three Xcode versions as a sample configuration, which are `15.3`, `15.2`, and `15.1`.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2757-aws10-ec2-storage.png' />

- To select the previously created dedicated host, expand the "Advanced details" settings.

  - Set the "Tenancy" to **`Dedicated Host`**.

  - Set the "Target host by" to **`Host ID`**.

  - Set the "Tenancy host ID" to the dedicated **Host ID** of the previously created dedicated host.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2757-aws11-ec2-dedicated-instance.png' />

Now you're ready to click on the **Launch Instance** button to create the EC2 Mac instance with the configuration you made.

You can head to the EC2 **Instances** page to see if your server is up and running.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2757-aws12-ec2-ready.png' />

:::info
You need to wait until the **Instance state** of the instance is **`Running`** in order to connect to the instance with SSH.

Generally it takes ~5-10 minutes till the **Instance state** becomes **`Running`** from **`Pending`**.
:::

## Configuring the Appcircle Runner Instance

### Connect via SSH

After you have successfully created an EC2 Mac instance, you can follow the steps below to configure it.

- Get the IP address of the instance from EC2 dashboard.

  - Networking > Networking Details > Public IPv4 address
  - Or, Instance > Details > Public IPv4 address

- Locate the SSH key pair, especially the private key, that you've created or used while configuring the instance.

- Get an SSH connection tool like `putty` on Windows or `ssh` on macOS and Linux to connect to the instance.

:::info
The `ssh` command below is for macOS and Linux. The other commands are the same after you connect to the instance.
:::

Using **private key** and **IP address**, you can connect to the instance with SSH as seen below.

```bash
ssh -i "/path/to/your/private/key" ec2-user@ip-address-of-the-instance
```

:::info
The default user for the Sonoma macOS AMI is `ec2-user`. So you should use `ec2-user` while connecting to the newly created EC2 Mac instance.

So, let's assume that your instance IP address is `3.234.230.124` and your private SSH key path is `/home/spacetech/.ssh/id_rsa`.

You can connect to the instance using the below command on macOS or Linux.

```bash
ssh -i "/home/spacetech/.ssh/id_rsa" ec2-user@3.234.230.124
```

:::

:::tip
When you "Create new key pair" while creating the instance, the downloaded private key might cause a permission error when you try to connect to the instance. For instance;

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

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2757-instance-config-ssh-warning.png' />

:::

### Configure Runner

#### Install Latest Package

After you successfully connect to the Appcircle runner instance, you can install the Appcircle runner into it.

Change the current working directory to the home directory.

```bash
cd "$HOME"
```

Download the latest self-hosted runner package.

```bash
curl -O -L https://cdn.appcircle.io/self-hosted/runner/appcircle-runner-osx-arm64-1.6.0.zip
```

Extract self-hosted runner package.

```bash
unzip -o -u appcircle-runner-osx-arm64-1.6.0.zip
```

Change directory into extracted `appcircle-runner` folder for following steps.

```bash
cd appcircle-runner
```

#### Register the Runner to the Appcircle server

:::info

By default, the Appcircle runner is configured to connect to the Appcircle cloud. If you are not using the Appcircle server as self-hosted, you can skip this information.

If you are using a self-hosted Appcircle server, edit the `appsettings.json` file with your favorite editor.

```bash
vi appsettings.json
```

You will see that the `ASPNETCORE_BASE_API_URL` value is pre-defined for the Appcircle cloud. Change it to your Appcircle server API domain without changing the path. For example:

```json
{
...
  "ASPNETCORE_BASE_API_URL": "https://api.appcircle.spacetech.com/build/v1"
}
```

:::

Now you need to create a **Runner Access Token** to register this instance with the Appcircle server.

<RegisterAppcircleRunner />

#### Install the Required Build Tools

<ConfigureAppcircleRunner />

For this tutorial, we will install the Android tools and iOS tools with the latest (_at the moment_) three stable Xcode versions.

```bash
./ac-runner install -o ios,android -x 15.3,15.2,15.1
```

#### Run the Service

<RunAppcircleRunner />

## Building Applications

<BuildAppOutro />

For a comprehensive overview of building applications on the Appcircle platform, you can navigate to the [Platform Build Guides](/build/platform-build-guides) page.

<NeedHelp />

Have questions? [Contact us here.](https://appcircle.io/support/)
