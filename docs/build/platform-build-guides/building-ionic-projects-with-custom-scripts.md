---
title: Ionic Applications
description: Learn how to build Ionic applications with custom scripts in Appcircle
tags: [build, platform build guides, ionic, custom scripts]
sidebar_position: 10
---

# Ionic Applications with Custom Scripts

Appcircle supports Ionic applications through custom scripts.

You can use the following project as an example for running Ionic builds on Appcircle:[ https://github.com/appcircleio/appcircle-sample-ionic](https://github.com/appcircleio/appcircle-sample-ionic)

The sample project is built with Vue though other Ionic application types can also be built in a similar manner. For the build, Capacitor is recommended, and this document is based on projects configured to be built with Capacitor in Android Studio or Xcode.

To build an Ionic application, first, add and configure it like a [React Native application](building-react-native-applications).


:::warning `capacitor-cordova-android-plugins`

One important point to note is that the `capacitor-cordova-android-plugins` folder is automatically added to the `.gitignore` file, but it is required during the build process. You can either remove this folder from `.gitignore` or allow it to be regenerated during the build; however, the former is recommended to ensure a successful [fetch](/build/build-process-management/configurations#config-details) operation. For more information, you can refer to the following Git issue for Capacitor: [https://github.com/ionic-team/capacitor/issues/1628](https://github.com/ionic-team/capacitor/issues/1628)

:::

You can then add the custom scripts right before the build steps and run the build normally.

:::warning "npm/Yarn Commands" step

Make sure the "npm/Yarn Commands" step is included in your workflow before the build steps. It doesn’t need to be placed immediately before, but it must come earlier in the sequence.

:::

### Android Custom Script for Ionic Builds

For Android, add the following custom script **immediately before** the "Android Build" step.

```bash
set -e
set -x

cd $AC_REPOSITORY_DIR

sudo npm install -g @ionic/cli

ionic build
ionic capacitor copy android
```

:::tip

If you encounter issues such as missing plugins, outdated configurations, or build failures after adding new dependencies, you can run:

```bash
ionic capacitor sync android
```

This ensures web assets, plugin installations, and config updates are fully synchronized with your native platforms.

:::

### iOS Custom Script for Ionic Builds

For iOS, add the following custom script **immediately before** the "Xcodebuild for Devices" step.

```bash
set -e
set -x

cd $AC_REPOSITORY_DIR

sudo npm install -g @ionic/cli

ionic build
ionic capacitor copy ios
```

:::tip

If you encounter issues such as missing plugins, outdated configurations, or build failures after adding new dependencies, you can run:

```bash
ionic capacitor sync ios
```

This ensures web assets, plugin installations, and config updates are fully synchronized with your native platforms.

:::

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />
