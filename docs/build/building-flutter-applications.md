---
title: Building Flutter Mobile Applications
metaTitle: Building Flutter Mobile Applications
metaDescription: Building Flutter Mobile Applications
sidebar_position: 7
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';
import NarrowImage from '@site/src/components/NarrowImage';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Building Flutter Mobile Applications

You can build your Flutter applications in Appcircle for iOS or Android platforms.

### Creating a Flutter Build Profile

Simply create a new build profile as usual and select your target operating system as iOS or Android. Select **Flutter **for **Target Platform**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (1).png' />

Once your build profile is created, click on it and connect your Git repository. For details on this step, please follow the directions on the following page:

<ContentRef url="/build/adding-a-build-profile">Adding a Build Profile</ContentRef>

To test drive the Appcircle platform for Flutter app builds, you can also use our sample Flutter App by forking it or adding it as a public repository: [https://github.com/appcircleio/appcircle-sample-flutter](https://github.com/appcircleio/appcircle-sample-flutter)

### Build Configuration for Flutter Applications

Build configuration options are very similar to native iOS or Android applications. You can select configuration details, build triggers, signing identities and distribution options.

### Private Modules

If your project uses private modules, don't forget the add necessary SSH keys to your workflow steps. You can use `Activate SSH Private Key` step to add your private SSH keys.

<ContentRef url="/build/adding-a-build-profile/connecting-to-private-repository-via-ssh">Connecting to Private Repository via SSH</ContentRef>

You may also use `Authenticate with netrc` step to access your private modules.

https://github.com/appcircleio/appcircle-netrc-component

### Build Configuration for Flutter iOS applications

First, we need to set up a build configuration. Select the configuration from the **Configuration** section. The first step will be to enter project details. You can enter details manually or click on the "Autofill" button to retrieve them from your project.

Your iOS project needs to have an **Xcode project** or an **Xcode workspace** and a **shared scheme** to complete the build configuration successfully. Appcircle can fetch these workspaces and shared schemes from your branch automatically.

You can also select a specific Xcode version if you have certain dependencies or if you want to test your build on a specific version.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (2).png' />

### Build Configuration for Flutter Android applications

First, we need to set up a build configuration. Select the configuration from the **Configuration** section. The first step will be to enter project details. For Flutter Android apps, the fetch operation is not required. You can simply select the build mode (e.g. debug or release) and the output type (APK or Splik APK as AAB).

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (3).png' />

### Build Configuration for Flutter Web applications

Flutter Web apps are built alongside with iOS or Android Flutter apps. For more information please refer to the following guide:

<ContentRef url="/build/building-flutter-web-applications">Building Flutter Web Applications</ContentRef>

### Sending the Build Status to the Repository Providers

At the bottom of the config tab, you will the **Set Commit Build Status **option.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (8).png' />

When this option is enabled, the build status for that commit is shared with the repository provider.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (213).png' />

![](https://cdn.appcircle.io/docs/assets/appcircle-github-commit-status-pass.png)

### Build Triggers

The next section, Triggers, is common for both iOS and Android.

Appcircle allows you to trigger builds manually or automatically using build triggers.

- On push: Whenever code is pushed to a configured branch, the build is triggered.
- On a tagged push: Whenever a tagged commit is pushed, the build is triggered for that commit. Commits without any tags are ignored.
- On push with selective tags: Whenever a commit includes one of the typed in tags, the build is triggered. You can specify tags with Unix shell-style wildcards to trigger builds.

<ContentRef url="/build/build-manually-or-with-triggers">
  Build Manually or Automatically with Webhooks and Triggers
</ContentRef>

###

### Signing Flutter iOS Applications

The next step in the build configuration is Signing. Here, please select the provisioning profile you added in the [iOS Certificates & Provisioning Profiles](../signing-identities/ios-certificates-and-provisioning-profiles.md) section.

For signing iOS apps, press add, select the bundle ID from the first dropdown and then select a compatible provisioning profile (added from the signing identities module) from the second dropdown.

<NarrowImage src="https://cdn.appcircle.io/docs/assets/image%20(5).png" />


### Signing Flutter Android Applications

Here, please select the Android Keystore you added in the [Android Keystores](../signing-identities/android-keystores.md) section. For signing Android apps, simply select a keystore (added from the signing identities module).

<NarrowImage src="https://cdn.appcircle.io/docs/assets/image%20(4).png" />

###

### Distribution (Deployment) Configuration

The next step on build configuration is Distribution.

You can select a previously created distribution profile or create a new one in this window. Use the top input box to enter a name for the new distribution profile you want to create. Press enter or click on the green + icon on the right to create the distribution profile.

Finally, check Auto Distribute if you want your build to be deployed to the Testing Distribution automatically and Auto Deployment if you want the build to be deployed to Store Submission automatically.

<ContentRef url="/distribute/create-or-select-a-distribution-profile">
  Create a Distribution Profile and Sharing with Testers
</ContentRef>

:::info

Any previous build can be deployed to the Distribute module without the need for rebuilding.

:::

### Environment Variables

The final tab is to add environment variables to the build. For advanced use cases, you can define variables and secrets to be incorporated during the build in the Environment Variables submodule so that you don’t need to store certain keys and configurations within the repository.

Please refer to the following document for more information on environment variables:

<ContentRef url="/environment-variables/why-to-use-environment-variables-and-secrets">
  Why to Use Environment Variables and Secrets?
</ContentRef>

### Build Workflows for Flutter Applications

Once you complete your build configuration, you can edit your build workflow. Flutter builds have additional steps for Flutter commands. You can also arrange, add or remove workflow steps using Appcircle's workflow editor and Workflow Marketplace.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (6).png' />

To learn more about Appcircle's Workflow editor, see the corresponding page below:

<ContentRef url="/workflows/why-to-use-workflows">What are Workflows and How to Use Them?</ContentRef>

### How to Set a Specific Flutter Version for the Build

To change the Flutter version, open the Flutter Install workflow step from the workflow editor and set the version under the "Selected Flutter Version" field.

<NarrowImage src="https://cdn.appcircle.io/docs/assets/image%20(167).png" />

You can also set the preferred Flutter version on config screen. If you don't set any version, `stable` version will be used.
### Starting a Flutter Build and After a Build

You are now ready to start your first build. Select the branach from the left side and click on the **Start Build** button.


![](https://cdn.appcircle.io/docs/assets/start-build.png)

Select a configuration, workflow, commit id and click on **Start Build button**

![](https://cdn.appcircle.io/docs/assets/start-build-configuration.png)


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
