---
title: Building Flutter Web Applications
description: You can build your Flutter web applications in Appcircle.
tags: [flutter, web, flutter web, flutter web build]
sidebar_position: 8
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Building Flutter Web Applications

If your app supports Flutter Web, you can also build the Flutter web app along with the [Flutter iOS or Android build](/build/platform-build-guides/building-flutter-applications).

With Appcircle, you can manage your entire Flutter build workflows both for mobile and web without the need for any third party solutions.

Flutter Web Build is available as a workflow step in the workflow marketplace. Just configure your project as you would for iOS or Android and add the Flutter Build for Web step anywhere after the Flutter Install step to include a web build in the workflow.

<Screenshot url='https://cdn.appcircle.io/docs/assets/flutter-web-build-workflow.png' />

If you want to build your Flutter project only for the web, you can [add a Flutter Android project in the standard way](/build/platform-build-guides/building-flutter-applications), save your project configuration once, and then remove all the Android-related steps from the build workflow.

:::caution

Make sure to not remove **Export Build Artifacts** from the steps.

:::

In this case, after removing Android-related steps, the workflow will look like the following:

<Screenshot url='https://cdn.appcircle.io/docs/assets/build-flutter-web-end-result.png' />

For more information about workflows, refer the workflow documentation below:

<ContentRef url='/workflows/index.html'>What are Workflows</ContentRef>

If you want to deploy your web output automatically, you can use a [Custom Script](https://github.com/appcircleio/appcircle-custom-script-component/) or [upload it to Amazon S3](/workflows/common-workflow-steps/build-and-test/upload-files-to-amazon-s3).

Once your build is configured, it can be built [manually or automatically in the same way with other apps](/build/build-process-management/build-manually-or-with-triggers). With Flutter 2.0, you can build your Flutter web apps in the stable channel. (In Flutter 1.x, it was necessary to use the beta channel.)

<Screenshot url='https://cdn.appcircle.io/docs/assets/build-flutter-web-workflow-success.png' />

After a build, you can download the web build output manually [from the build artifact list](/build/platform-build-guides/building-flutter-applications#starting-a-flutter-build-and-after-a-build) as the `web.zip` file.

<Screenshot url='https://cdn.appcircle.io/docs/assets/build-flutter-web-artifact-download.png' />

:::info

As of Flutter 1.21, the Flutter SDK includes the full Dart SDK. So if you have Flutter installed, you might not need to explicitly download the Dart SDK. If you need to use a different Dart version than the bundled one, you can install it using the below commands.

:::

<Tabs>
  <TabItem value="ios" label="iOS" default>

```bash
brew tap dart-lang/dart
brew install dart
```

  </TabItem>
  <TabItem value="android" label="Android">

```bash
 sudo apt-get update
 sudo apt-get install apt-transport-https
 sudo sh -c 'wget -qO- https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -'
 sudo sh -c 'wget -qO- https://storage.googleapis.com/download.dartlang.org/linux/debian/dart_stable.list > /etc/apt/sources.list.d/dart_stable.list'
 sudo apt-get install dart
```

  </TabItem>
</Tabs>

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />
