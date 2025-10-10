---
title: Appcircle CodePush
description: Learn how to use Appcircle CodePush profile.
tags: [appcircle codepush, codepush, react native, sdk]
sidebar_position: 1
---

import ContentRef from '@site/src/components/ContentRef';

# Appcircle CodePush

Appcircle CodePush is a module that enables seamless over-the-air updates for React Native applications. This document explains how to configure and use the CodePush profile within Appcircle step by step.

:::caution Appcircle CodePush

The Appcircle CodePush feature is specifically designed for **React Native** projects. Other mobile technologies in the ecosystem **are not** supported. This feature **should only be used** in **React Native** projects.

:::

:::tip Learn More
For a complete overview of the Appcircle CodePush feature's capabilities, check out the [Appcircle's CodePush Section](https://appcircle.io/codepush).
:::

## [Appcircle CodePush Profile](/code-push/code-push-profile/appcircle-code-push-profile)

To start using CodePush in your React Native project, you first need to create a CodePush profile in Appcircle.

<ContentRef url="/code-push/code-push-profile">CodePush Profile</ContentRef>

## [Appcircle CodePush SDK](/code-push/code-push-sdk)

The Appcircle CodePush SDK is required to integrate CodePush functionality into your React Native application and to handle update processes on the client side.

<ContentRef url="/code-push/code-push-sdk">CodePush SDK</ContentRef>

## [Appcircle CodePush CLI](/code-push/code-push-cli)

The Appcircle CodePush CLI allows you to manage your CodePush deployments, upload new bundles, and interact with your CodePush profile from the command line.

<ContentRef url="/code-push/code-push-cli">CodePush CLI</ContentRef>

## [CodePush Code Signing](/code-push/code-push-code-signing)

CodePush Code Signing ensures that every over‑the‑air (OTA) JavaScript bundle your React Native application receives originates from a trusted source and has not been altered in transit.

<ContentRef url="/code-push/code-push-code-signing">CodePush Code Signing</ContentRef>

## [CodePush via Build Module](/code-push/code-push-via-build-module)

You can also use the CodePush feature directly through the Appcircle Build Module to automate bundle uploads as part of your CI/CD pipeline.

<ContentRef url="/code-push/code-push-via-build-module">CodePush via Build Module</ContentRef>