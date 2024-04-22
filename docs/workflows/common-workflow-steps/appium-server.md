---
title: Appium Server
description: Enhance your app testing with Appium Server. Automate mobile app testing across platforms for better efficiency and accuracy in development.
tags: [testing, automation, server, cli, development]
sidebar_position: 4
---


import Screenshot from '@site/src/components/Screenshot';

# Appium Server

[**Appium Server**](https://appium.io/docs/en/latest/) is an open-source project and ecosystem of related software designed to facilitate the UI automation of many app platforms.

With Appcircle's Appium Server component, you can easily integrate the **Appium CLI** into your pipeline by installing it.

### Prerequisites

:::info

There are no specific components required for this step to function. You can place it within the pipeline according to your own workflow.

:::

### Input Variables

Below is a list of input variables that can be used with this component, with a description of each.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2795-appiumInput.png' />

| Variable Name                 | Description                                    | Status           |
|-------------------------------|------------------------------------------------|------------------|
| `$AC_APPIUM_VERSION`          | Specifies the version of Appium Server to use. For example: `v1.22.3`. If no version is specified, the latest version will be installed. | Optional |