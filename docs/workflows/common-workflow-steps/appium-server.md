---
title: Appium Server
description: Enhance your app testing with Appium Server. Automate mobile app testing across platforms for better efficiency and accuracy in development.
tags: [testing, automation, server, cli, development]
sidebar_position: 4
---


import Screenshot from '@site/src/components/Screenshot';

# Appium Server

[**Appium Server**](https://appium.io/docs/en/latest/) is an open-source project and ecosystem of related software designed to facilitate the UI automation of many app platforms.

You can easily integrate the **Appium CLI** into your pipeline using Appcircle's Appium Server component by installing it.

### Prerequisites

:::info

This step does not require any specific components to function. You can place it anywhere within your pipeline according to your workflow needs.

:::

### Input Variables

Below is a list of input variables that can be used with this component, with a description of each.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2795-appiumInput.png' />

| Variable Name                 | Description                                    | Status           |
|-------------------------------|------------------------------------------------|------------------|
| `$AC_APPIUM_VERSION`          | Specifies the version of Appium Server to install, such as `v1.22.3`. If you do not specify a version, the system installs the latest version. | Optional |