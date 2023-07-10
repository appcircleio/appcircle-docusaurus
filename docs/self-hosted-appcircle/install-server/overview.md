---
title: Overview
metaTitle: Installing Server
metaDescription: Installing Server
sidebar_position: 1
---

# Appcircle Application Installation Overview

This document provides an overview of the steps required to install the Appcircle server on the server. For detailed instructions, please refer to the corresponding pages mentioned below.

## Server Installation:

### Check the Operating System (OS):

Before proceeding with the installation, it is essential to verify the compatibility of the targeted operating system version.

[You can check compatible os versions here.](./docker.md#supported-linux-distributions)

### Verify Hardware Requirements:

Check CPU, memory, swap, and disk space requirements.

[You can check that hardware reqirements here.](./docker.md#hardware-requirements)

### Install First Dependencies:

To download and unzip the application installation zip package, install the necessary dependencies.

[You can check first dependencies here.](./docker.md#1-download)

### Download and Extract the Application Installation Package :

Obtain the application's zip file and extract its contents.

[You can check download and extract processes here.](./docker.md#1-download)

### Install Application Dependencies:

Install additional dependencies and packages required by the application.

[You can check application dependencies and how to install from here.](./docker.md#2-packages)

### Configure Podman Settings:

You can skip this step if you are installing the application with docker.

If you are installing Appcircle server with podman, you must configure podman's network settings. And also need to install an additional application to use podman rootles.

[You can check the port forwarding settings here.](./podman.md#podman-requirements)

[You can check the podman network stack settings here.](./podman.md#podman-network-stack)

### Configure Application Settings:

Configure various settings below for the application

[You can check detailed configuration steps here.](./docker.md#3-configure)

#### HTTP and HTTPS Settings.

You can utilize the Appcircle server in either HTTP or HTTPS mode, which can be configured in the `global.yaml` settings file.

#### SMTP Settings for Email Functionality.

To utilize email services such as registration or distribution notifications, it is necessary to define SMTP settings in the `global.yaml` configuration file.

#### DNS Settings for Domain Configuration.

It is imperative to configure DNS settings for the application within the network infrastructure.

#### Initial User Setup and Permissions.

Define the initial user and password in the `global.yaml` file.

### Set DNS Settings on the Network

You should set the domains and the server ip address to access appcircle server.

[You can see the the domains that used by appcircle here.](./docker.md#4-dns-settings)

### Pull the Container Images

The Appcircle server is an containerized application. Prior to running the server, it is necessary to pull the images from the Appcircle image repository. You don't need to perform an additional step to pull container images, as the Appcircle install script will automatically handle the image retrieval process.

If a proxy repository was used to access to the origin repository, it should be defined in the `global.yaml` configuration file.

[You can check how to define custom image registry here.](./docker.md#using-sonatype-nexus-as-proxy-registry)

### Run the Server

At the end, you are ready to start the application!

[Run the application and verify its health.](./docker.md#5-run-server)

## Runner Installation

To build and distribute mobile applications, you need a Appcircle runner.

[You can check how to install Appcircle runner here](../self-hosted-runner/installation.md)

### Connect Runner to Your Appcircle Server

You need to connect your Appcircle runner to your Appcircle server. So the server can share build and distribute jobs with the runner.

[You can check how to connect runner to server here](../self-hosted-runner/installation.md#2-register)

## Build an Example Appcircle Application

To test overall functionality and system stabilization, you can build example mobile applications.

If you don't have one, you can use the example repositories of Appcircle mobile applications.

To build example applications, create a build profile. After that, you can click `Quick start using the sample repository` button to import example repositories.

:::info

Please note that this overview serves as a high-level roadmap, and detailed instructions for each step can be found in the associated pages.

For more detailed instructions to install the server, please refer to installation page.

[Click here to see Appcircle server docker Installation.](./docker.md)

[Click here to see Appcircle server podman installation.](./podman.md)

:::
