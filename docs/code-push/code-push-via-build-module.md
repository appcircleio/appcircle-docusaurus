---
title: CodePush via Build Module
description: Learn how to work with Appcircle CodePush SDK on build module.
tags: [appcircle codepush, build, ci, build module]
sidebar_position: 5
---

# CodePush via Build Module

This section explains how to configure and use Appcircle's Build Module to automatically upload CodePush updates as part of your CI/CD pipeline.

## Using Build Module for CodePush

Appcircle's Build Module allows you to trigger a CodePush release automatically at the end of a successful build by configuring the necessary environment variables and using the Appcircle CodePush Step. 

With Appcircle's Build Module, you can both send a new CodePush release to active devices and generate a new binary for a fresh distribution of your React Native project.

With the end-to-end automation capability of the Build Module, you can also include CodePush releases in your automated workflows. Please follow the documentation below for detailed instructions.

- [**Build Module Overview:**](/build) Learn about the core functionalities and capabilities of the Appcircle Build Module and how it fits into your CI/CD workflow.

- [**Building React Native Projects:**](/build/platform-build-guides/building-react-native-applications) A step-by-step guide for configuring and building React Native applications using Appcircle's Build Module.

- [**Appcircle CodePush Step:**](/workflows/react-native-specific-workflow-steps/appcircle-codepush) Details on how to add and configure the CodePush step in your workflow to automate the release of OTA updates.