---
title: What are Workflows and How to Use Workflows?
description: Understand workflows in Appcircle. Learn how to use them for building, testing, and deploying your applications.
slug: /build-integrations
tags: [workflow, step, build, test, deploy, integration]
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# What are Workflows and How to Use Them?

<Tabs
  defaultValue="ios"
  values={[
    { label: 'iOS', value: 'ios' },
    { label: 'Android', value: 'android' },
    { label: 'React Native', value: 'reactnative' },
    { label: 'Flutter', value: 'flutter' },
  ]}
>
  <TabItem value="ios">
    <iframe
      width="560"
      height="315"
      src="https://www.youtube.com/embed/WOQedZ15z6s"
      title="YouTube video player"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen
    ></iframe>
  </TabItem>
  <TabItem value="android">
    <iframe
      width="560"
      height="315"
      src="https://www.youtube.com/embed/FcZv2cCnGFA"
      title="YouTube video player"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen
    ></iframe>
  </TabItem>
  <TabItem value="reactnative">
    <iframe
      width="560"
      height="315"
      src="https://www.youtube.com/embed/bo0fWk9cATA"
      title="YouTube video player"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen
    ></iframe>
  </TabItem>
  <TabItem value="flutter">
    <iframe
      width="560"
      height="315"
      src="https://www.youtube.com/embed/vKFfNvJvRDs"
      title="YouTube video player"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen
    ></iframe>
  </TabItem>
</Tabs>

A workflow is a ladder of steps taken to build your applications.

Each step has a different purpose and the workflow can be customized by modifying step parameters and inputs, running custom scripts, or re-ordering steps.

Workflows allow you to have complete control on your build process and enhance it with third-party services and features.

:::caution

Please note that modifying workflow steps may cause your builds to fail, so utmost care is recommended when editing workflows.

:::

:::info
The Workflows feature may also be referred to as Build Integrations in some documentation and internal terminology.
:::

## [How to Create an Integration](/build-integrations/how-to-create-an-integration)

This guide explains the process of creating a new integration, including defining its purpose, configuring inputs and outputs, writing the necessary scripts or code, and integrating it into existing workflows for automation.

## [Common Integrations](/build-integrations/common-integrations)

These steps are common across all build profiles regardless of the target OS and platform.

You can find the full list of available workflow steps in our [workflow marketplace](https://github.com/appcircleio/appcircle-workflow-components) and under each workflow step in this document, you can find the related repository URL, which also includes the documentation for the related step.

## [iOS Specific Integrations](/build-integrations/ios-specific-integrations)

These steps are specific to the iOS build profiles.

You can find the full list of available workflow steps in our [workflow marketplace](https://github.com/appcircleio/appcircle-workflow-components) and under each workflow step in this document, you can find the related repository URL, which also includes the documentation for the related step.

## [Android Specific Integrations](/build-integrations/android-specific-integrations)

These steps are specific to the Android build profiles.

You can find the full list of available workflow steps in our [workflow marketplace](https://github.com/appcircleio/appcircle-workflow-components) and under each workflow step in this document, you can find the related repository URL, which also includes the documentation for the related step.

## [React Native Specific Integrations](/build-integrations/react-native-specific-integrations)

These steps are specific to the React Native build profiles.

You can find the full list of available workflow steps in our [workflow marketplace](https://github.com/appcircleio/appcircle-workflow-components) and under each workflow step in this document, you can find the related repository URL, which also includes the documentation for the related step.

## [Flutter Specific Integrations](/build-integrations/flutter-specific-integrations)

These steps are specific to the Flutter build profiles.

You can find the full list of available workflow steps in our [workflow marketplace](https://github.com/appcircleio/appcircle-workflow-components) and under each workflow step in this document, you can find the related repository URL, which also includes the documentation for the related step.