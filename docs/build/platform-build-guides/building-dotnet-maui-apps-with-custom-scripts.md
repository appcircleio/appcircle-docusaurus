---
title: Building .NET MAUI Apps with Custom Scripts
description: Learn how to build .NET MAUI apps with custom scripts in Appcircle
tags: [build, platform build guides, MAUI, .NET MAUI, custom scripts]
sidebar_position: 10
---

# Building .NET MAUI Apps with Custom Scripts

// todo

:::tip

Some Appcircle features might not be supported for .NET MAUI build profiles on the dashboard, or you might need to do some extra customizations in the custom scripts to use them.

In this case, do not hesitate to [contact us](https://appcircle.io/support/) for support. We will do our best to support your build pipeline for .NET MAUI apps.

:::

### Android Custom Script for .NET MAUI Builds

In order to build a .NET MAUI Android app on Appcircle follow the steps below.

**1.** [Create](/build/manage-the-connections/adding-a-build-profile) a new build profile for your app.

- `Android` should be selected as the **Target Operating System**, and `Java / Kotlin` should be selected as the **Target Platform**.

**2.** Connect your repository using a compatible connection method.

:::tip

You can disable the **Autofill** toggle or ignore the output of **Autofill** run since it does not support .NET MAUI app metadata processing.

:::

:::info

As of now, Appcircle does not have a sample repository for .NET MAUI apps. So the **quick start using the sample repository** option will not work for .NET MAUI build profiles. You should use your own repository.

:::

**3.** In your [workflow](/workflows), use the below custom script as a replacement of the default **Android Build** step.

```bash
set -e
set -x

cd $AC_REPOSITORY_DIR

echo "Hello world!"

```

// TODO: in progress...

### iOS Custom Script for .NET MAUI Builds

In order to build a .NET MAUI iOS app on Appcircle follow the steps below.

**1.** [Create](/build/manage-the-connections/adding-a-build-profile) a new build profile for your app.

- `iOS` should be selected as the **Target Operating System**, and `Objective-C / Swift` should be selected as the **Target Platform**.

**2.** Connect your repository using a compatible connection method.

:::tip

You can disable the **Autofill** toggle or ignore the output of **Autofill** run since it does not support .NET MAUI app metadata processing.

:::

:::info

As of now, Appcircle does not have a sample repository for .NET MAUI apps. So the **quick start using the sample repository** option will not work for .NET MAUI build profiles. You should use your own repository.

:::

**3.** In your [workflow](/workflows), use the below custom script as a replacement of the default **Xcodebuild for Devices** step.

```bash
set -e
set -x

cd $AC_REPOSITORY_DIR

echo "Hello world!"

```

// TODO: in progress...

___

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />
