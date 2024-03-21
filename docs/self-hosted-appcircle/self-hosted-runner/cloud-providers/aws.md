---
title: Amazon Web Services (AWS)
metaTitle: Amazon Web Services (AWS)
metaDescription: Appcircle Server on AWS
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';
import NeedHelp from '@site/docs/\_need-help.mdx';
import RegisterAppcircleRunner from '@site/docs/self-hosted-appcircle/self-hosted-runner/\_register-runner.mdx';

## Overview

An Appcircle runner Amazon Machine Image (AMI) is a pre-configured template used to create virtual servers, known as instances, in the Amazon Web Services (AWS) environment.

Think of it as a snapshot of a Appcircle runner that includes the operating system, necessary tools, applications, and any additional services needed to build mobile applications.

## Pre-requirements

### Appcircle Requirements

You can use a self-hosted Appcircle runner for your self-hosted Appcircle server or cloud Appcircle account.

:::warning

The only requirement for using self-hosted runners is to be in `enterprise` plan.

See [pricing](https://appcircle.io/pricing) and feature comparison table for details.

:::

### Technical Requirements

Before using the Appcircle runner AMI, there are a couple of things that you need to handle.

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

##### 4. Dedicated Hosts and MacOS Instances

While the process of creating a macOS EC2 instance on AWS differs slightly from creating a Linux instance, the key distinction lies in the requirement of a dedicated host.

After selecting a macOS image during the instance creation process, users must specify the dedicated host they have previously provisioned, as outlined in the AWS documentation for comprehensive guidance.

For more details about the AWS macOS EC2 instances, you can refer to the [AWS documents](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-mac-instances.html).

## Creating an Appcircle Runner from the AMI

After you meet all the requirements discussed above, you can follow the steps below to create an Appcircle runner from the AMI.

- Log in to the AWS console with your account.

- Select the region from the right upper corner.

:::info

If you have a self-hosted Appcircle server in AWS, its better to deploy the self-hosted Appcircle runner in the same region as the Appcircle server. This will reduce the latency between two machines.

:::

### Creating a Dedicated Host for MacOS EC2 Instance

- Head to the EC2 menu to create an dedicated instance.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2757-aws1-dashboard.png' />

- Head to the "Dedicated Hosts" menu and click on the "Allocate Dedicated Host" button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2757-aws2-dedicated-host-dashboard.png' />

- Enter an dedicated instance name in the "Name tag" field. For example, "Appcircle Dedicated Host".

- Then you should select the instance family, instance type and the availability zone. For example, "mac2" for the instance family and "mac2.metal" for the instance type.

:::info

You must select one of the "mac2", "mac2-m2" or "mac2-m2pro" instance family types since the Appcircle runner AMI is supported on these family types.

In the [AWS documents](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-mac-instances.html), you can find the underlying infrastructure.

> EC2 M1 Mac instances (mac2.metal) are built on 2020 Mac mini hardware powered by Apple silicon M1 processors.

> EC2 M2 Mac instances (mac2-m2.metal) are built on 2023 Mac mini hardware powered by Apple silicon M2 processors.

> EC2 M2 Pro Mac instances (mac2-m2pro.metal) are built on 2023 Mac mini hardware powered by Apple silicon M2 Pro processors.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2757-aws3-dedicated-host-launch-1.png' />

- Since the `mac` instances doesn't support "Host maintenance", you should uncheck it and click on the "Allocate" button to create your dedicated host.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2757-aws4-dedicated-host-launch-2.png' />

- You can see the created dedicated host on the dedicated hosts dashboards.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2757-aws5-dedicated-host-created.png' />

- When you see the state of the dedicated host as "Available", you can continue with creating EC2 instance.

:::info
If you have more than one dedicated hosts, make a note of the dedicated host id to avoid confusion when creating the EC2 instance.
:::

### Creating an EC2 Instance on the Dedicated Host

- Head to the EC2 menu to create an EC2 instance.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2503-aws23-region-menu.png' />

- Click on the "Launch Instance" button from the EC2 dashboard.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2503-aws24-launch-ec2.png' />

You should fill out the required fields as per your needs. Please follow the below steps for a sample instance configuration.

- Enter an instance name in the "Name and Tags" field. For example, "My Appcircle Server".

- In order to select the AMI, click on the "Browse more AMIs" button and search for the Appcircle server AMI.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2503-aws9-ami1.png' />

- Search for "Appcircle" in the "AWS Marketplace AMIs" tab and click on the "Select" button for the AMI.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2503-aws10-ami2.png' />

- Click "Continue" to select Appcircle server AMI.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2503-aws11-ami3.png' />

- We will use the `t3.2xlarge` instance type for our sample configuration since it meets the minimum requirements for the vCPU count.

:::info
For the details about minimum hardware requirements, you should see the [Hardware Requirements](../docker.md#hardware-requirements) section.
:::

- Select an existing key pair or click on the "Create new key pair" button if you don't have any on the AWS console.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2503-aws14-instance-type.png' />

- For the network settings:
  - We will use the default VPC created on the form.
  - Allow HTTP and HTTPS traffic from the internet.
    - This is required for accessing the Appcircle server dashboard.
  - You can restrict the SSH connection by specifying the source IP addresses.
    - **SSH is also required** to access the server from the command line.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2503-aws15-network.png' />

- For storage, you can select a minimum 100-GB disk for a PoC setup or testing purposes.

:::info
You should see the recommended storage sizes and other disk requirements in the [Hardware Requirements](../docker.md#hardware-requirements) section.
:::

:::caution
Keep in mind that the pre-configured swap also consumes disk space, and its size is as large as the memory size.

So, although a minimum 100-GB disk is enough to run the Appcircle server, we recommend a minimum 200-GB disk space for long-term usage.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2503-aws16-storage.png' />

Now you're ready to click on the **Launch Instance** button to create the instance with the configuration you made.

:::info
The instance creation may take some time due to the AWS AMI subscriptions.

Please wait patiently while AWS creates your Appcircle server instance. If the instance is not created within 2 hours, you can follow the steps above and launch it again.

You can check the subscription in the "AWS Marketplace Subscriptions" service in the AWS console.
:::

You can head to the EC2 **Instances** page to see if your server is up and running.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2503-aws18-instance-running.png' />

**To enable SSH access,** head to the security group settings of your instance. It's required for later configuration steps.

For our sample server instance above, select "My Appcircle Server" instance and click on the "Security" tab.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2503-aws19-ssh1.png' />

Edit the inbound rules to enable SSH access to your Appcircle server instance.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2503-aws20-ssh2.png' />

Add an SSH rule for the IP addresses you want, and click on the "Save Rules" button to activate the settings.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2503-aws21-ssh3.png' />

:::tip
If you want to also send `ping` requests to the instance for health check purposes, you should also add another rule with the type "All ICMP-IPv4" while editing the inbound rules.
:::

## Configuring the Appcircle Runner Instance

### Connect via SSH

After you have successfully created an EC2 instance from the Appcircle runner AMI, you can follow the steps below to configure it connect to an Appcircle server.

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
The default user for the Appcircle Runner AMI is `ec2-user`.

So, let's assume that your instance IP address is `34.205.139.17` and your private SSH key path is `/home/spacetech/.ssh/id_rsa`.

You can connect to the instance using the below command on macOS or Linux.

```bash
ssh -i "/home/spacetech/.ssh/id_rsa" ec2-user@34.205.139.17
```

:::

:::tip
When you "Create new key pair" while creating the instance from Appcircle AMI, the downloaded private key might cause a permission error when you try to connect to the instance. For instance;

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

After you successfully connect to the Appcircle runner instance, you can configured the Appcircle runner instance to connect to an Appcircle server.

The Appcircle runner directory is located in the `$HOME` directory as the `appcircle-runner` folder.

```bash
ls -l "$HOME"
```

Change the current working directory to that folder.

```bash
cd "$HOME/appcircle-runner"
```

:::info

By default, the Appcircle runner AMI is configured to connect the Appcircle cloud. If you are not using Appcircle server as self-hosted, you can skip this info.

If you are using self-hosted Appcircle server, edit the `appsettings.json` file with your favorite editor.

```bash
vi appsettings.json
```

You will see the the `ASPNETCORE_BASE_API_URL` value is pre-defined for Appcircle cloud. Change it to your Appcircle server API domain and without changing the path. For example:

```json
{
...
"ASPNETCORE_BASE_API_URL": "https://api.appcircle.spacetech.com/build/v1"
}
```

:::

Stop the running service before registering the runner.

```bash
./ac-runner service -c stop
```

<RegisterAppcircleRunner />

To make the runner online, you just need to start the service.

```bash
./ac-runner service -c start
```

After ~10 seconds, you will see that your Appcircle runner as online.

## Building Applications

When you register the Appcircle runner successfully by following the above steps, you're ready for your first build. :tada:

You can head to the [Tutorials](../../../tutorials/index.md) page for a brief of building applications on the Appcircle.

<NeedHelp />

Have questions? [Contact us here.](https://appcircle.io/support/)
