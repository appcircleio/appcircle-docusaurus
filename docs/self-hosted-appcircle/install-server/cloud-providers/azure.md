---
title: Microsoft Azure Integration
description: Learn how to create an Appcircle server instance on Microsoft Azure
tags: [self-hosted, appcircle server, microsoft azure, azure cloud, instance, image]
sidebar_position: 1
sidebar_label: Microsoft Azure
---

import AppcircleLicenseRequirement from '@site/docs/self-hosted-appcircle/install-server/cloud-providers/\_license-requirement.mdx';


## Overview

An Appcircle server image is a pre-configured template used to create virtual server, known as "virtual machines", in the Microsoft Azure environment.

Think of it as a snapshot of a server that includes the operating system, necessary tools, applications, and any additional services needed to run the Appcircle server.

This documentation provides step-by-step instructions for configuring and setting up Appcircle Server on Microsoft Azure. Follow these guidelines to ensure a successful deployment.


## Pre-requirements

### Appcircle Requirements

<AppcircleLicenseRequirement />

### Technical Requirements

Before using the Appcircle server AMI, there are a couple of things that you need to handle.

#### Microsoft Azure Account

You must have an active Azure account with appropriate permissions to launch virtual machines and work with other related services.

#### Understanding of Azure Services

A basic understanding of Azure services, particularly Virtual Machines, is beneficial.

You should be familiar with virtual machine creation, networking, security groups, and storage configurations.

##### 1. Networking and Security Configuration

You might need to configure networking aspects such as Virtual networks, subnets, route tables, and security groups to properly integrate the instance within the network environment and manage access controls.

##### 2. SSH Key Pairs for Secure Access

You need an SSH key pair to access to the server that you will create securely.

##### 3. Linux System Configuration

Basic familiarity with Linux system configurations and commands is essential since this document will use Linux commands.