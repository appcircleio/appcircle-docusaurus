---
title: Overview
metaTitle: Installing Server
metaDescription: Installing Server
sidebar_position: 1
---

This document provides an overview of the steps required to install the self-hosted Appcircle on your infrastructure. It's a summary of the overall journey and gives you an idea of the big picture.

For detailed instructions, please refer to the corresponding pages mentioned below.

## Server Installation

### Supported Linux Distributions

Before proceeding with the installation, it is essential to verify the compatibility of the targeted operating system version.

If you're planning to use **Docker** as the container runtime engine, you should check for compatible OS versions [here.](./docker.md#supported-linux-distributions)

If you're planning to use **Podman** as the container runtime engine, you should check for compatible OS versions [here.](./docker.md#supported-linux-distributions)

### Hardware Requirements

Check CPU, memory, swap, and disk space requirements.

You can check the hardware requirements [here.](./docker.md#hardware-requirements)

### Dependencies for Download

To download and extract the application installation zip package, you need to install the necessary dependencies.

You can see the dependencies [here](./docker.md#1-download).

### Download and Extract the Package

Obtain the application's zip file and extract its contents.

You should follow the download and extract processes [here.](./docker.md#1-download)

### Install Server Dependencies

Install additional dependencies and packages required by the self-hosted Appcircle server.

If you're planning to use **Docker** as the container runtime engine, you can check application dependencies and how to install them [here.](./docker.md#2-packages)

If you're planning to use **Podman** as the container runtime engine, you can check application dependencies and how to install them [here.](./podman.md#2-packages)

#### Configure Podman Specific Settings

:::info
You should skip this step if you are installing the application with Docker.
:::

If you are installing the server with Podman, you must configure Podman's network settings. And also need to install an additional application to use podman rootless.

You can check the port forwarding settings [here.](./podman.md#podman-requirements)

You can check the Podman network stack settings [here.](./podman.md#podman-network-stack)

### Configure Server Settings

You need to edit the default `global.yaml` file for your requirements and infrastructure.

You can see the detailed configuration steps [here.](./docker.md#3-configure)

#### HTTP and HTTPS Settings

You can utilize the Appcircle server in either HTTP or HTTPS mode, which can be configured in the `global.yaml` settings file.

After following the general configuration steps above, see the SSL configuration details [here.](/self-hosted-appcircle/configure-server/integrations-and-access/ssl-configuration)

#### Domain Settings of the Modules

You need to set a main domain for the Appcircle server. Also, you should decide the domain configurations for the Enterprise App Store and Testing Distribution modules.

#### SMTP Settings for Email Notifications

To utilize email services such as registration or testing distribution notifications, it is necessary to define SMTP settings in the `global.yaml` configuration file.

#### Initial Username and Password

The initial user will be the owner or administrator of the organization on the Appcircle server. So, you should configure it in `global.yaml` properly.

### DNS Settings for Subdomains

The Appcircle server has some subdomains for different services. They should be configured according to the network infrastructure.

You can see the DNS configuration details [here.](./docker.md#4-dns-settings)

### Pull the Container Images

The Appcircle server is a containerized application composed of microservices.

Prior to running the server, it is necessary to pull the images from the Appcircle image repository. You don't need to perform an additional step to pull container images, as the Appcircle install script will automatically handle the image retrieval process.

If you're planning to use a proxy repository to access the origin repository, it should be defined in the `global.yaml` configuration file.

You can check the required steps on how to define a custom image registry [here.](../configure-server/external-image-registry.md)

:::caution

You need `cred.json` file to pull the container images. Only the enterprise customers who have self-hosted Appcircle license can have `cred.json`.

For details about the `cred.json`, see [here.](./docker.md#artifact-registry-credentials-credjson)

:::

### Run the Appcircle Server

At the end, you are ready to start the Appcircle server. 🎉

Start the server and verify its [health.](./docker.md#5-run-server)

## Runner Installation

To build and distribute mobile applications, you need self-hosted Appcircle runners that are connected to the server.

You can check out how to install a self-hosted runner [here.](/self-hosted-appcircle/self-hosted-runner/installation)

### Connect Runner to the Server

You need to connect your self-hosted runner to the server. So the server can share builds and distribute jobs with the runner.

You can check how to connect runner to server [here.](/self-hosted-appcircle/self-hosted-runner/installation#2-register)

## Build a Sample App

To test overall functionality and system stabilization, you can build example mobile applications.

If you don't have one, you can use the sample repositories of Appcircle mobile applications.

To build sample applications, create a build profile. After that, you can click Quick start using the sample repository" button to import sample Appcircle repositories.

If you're on a restricted network and cannot reach Appcircle's GitHub repository, you can import the sample apps to your git provider on your private network and use them from there.

Below is a list of sample apps that you can use for demoing or testing:

- [iOS sample app](https://github.com/appcircleio/appcircle-sample-ios)
- [Android sample app](https://github.com/appcircleio/appcircle-sample-android)
- [Flutter sample app](https://github.com/appcircleio/appcircle-sample-flutter)
- [React Native sample app](https://github.com/appcircleio/appcircle-sample-react-native)

:::info

Please note that this overview serves as a high-level roadmap, and detailed instructions for each step can be found in the associated pages.

For more detailed instructions to install the server, please refer to installation page.

Click [here](./docker.md) to see Appcircle server installation on **Docker**.

Click [here](./podman.md) to see Appcircle server installation on **Podman**.

:::
