---
title: Ionic Applications
description: Learn how to build Ionic applications with custom scripts in Appcircle
tags: [build, platform build guides, ionic, custom scripts]
sidebar_position: 10
---

# Ionic Applications with Custom Scripts

Appcircle provides Ionic applications through custom scripts.

You can use the following project as an example for running Ionic builds in Appcircle:[ https://github.com/appcircleio/appcircle-sample-ionic](https://github.com/appcircleio/appcircle-sample-ionic)

The sample project is built with Vue though other Ionic application types can also be built in a similar manner. For the build, Capacitor is recommended, and this document is based on projects configured to be built with Capacitor in Android Studio or Xcode.

To build an Ionic application, first, add and configure it like a [React Native application](building-react-native-applications).

One important point to take note of is that `capacitor-cordova-android-plugins` folder is automatically added to the .gitignore file, but it is required during the build. The folder can be removed from the .gitignore or it can be regenerated during the build, though the former is recommended for a successful [Fetch](/build/build-process-management/configurations#config-details) operation. For more information, you can refer to the following Git issue for Capacitor: [https://github.com/ionic-team/capacitor/issues/1628](https://github.com/ionic-team/capacitor/issues/1628)

You can then add the custom scripts before the build steps and run the build normally.

### Android Custom Script for Ionic Builds

For Android, add the following script before the "Android Build" step.

```bash
set -e
set -x

cd $AC_REPOSITORY_DIR

npm install -g @ionic/cli
ionic capacitor copy android
```

### iOS Custom Script for Ionic Builds

For iOS, add the following script before the "Xcodebuild for Devices" step.

```bash
set -e
set -x

cd $AC_REPOSITORY_DIR

npm install
-g @ionic/cli

ionic capacitor copy ios
```

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />
