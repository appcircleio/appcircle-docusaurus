---
title: Platform Build Guides
description: Find detailed instructions on building applications for various platforms using Appcircle. Learn how to build iOS, Android, React Native, Flutter, and Ionic applications with ease.
tags:
  [
    platform build guides,
    ios build,
    android build,
    React Native build,
    flutter build,
    ionic build,
    .NET MAUI build,
    MAUI build,
    app development,
    app deployment,
    appcircle platform build,
  ]
---

# Platform Build Guides

Find detailed instructions on building applications for various platforms using Appcircle:

### [Building iOS Applications](/build/platform-build-guides/building-ios-applications)

Comprehensive guide for setting up iOS app builds, from provisioning to distribution.

### [Building Android Applications](/build/platform-build-guides/building-android-applications)

Step-by-step instructions on how to configure and optimize the Android build process.

### [Building React Native Applications](/build/platform-build-guides/building-react-native-applications)

Tailored guidance for building React Native apps, covering both iOS and Android builds.

### [Building Flutter Applications](/build/platform-build-guides/building-flutter-applications)

Everything you need to know to build Flutter applications for multiple platforms.

### [Building Ionic Projects with Custom Scripts](/build/platform-build-guides/building-ionic-projects-with-custom-scripts)

Learn how to use custom scripts to build and customize Ionic projects for any requirements.

### [Building .NET MAUI Apps](/build/platform-build-guides/building-dotnet-maui-apps)

Learn how to use custom scripts to build and customize .NET MAUI apps on Appcircle.

### [Building Xamarin Apps](/build/platform-build-guides/building-xamarin-apps)

Learn how to use custom scripts to build and customize Xamarin apps on Appcircle.

## FAQ

### General Build Troubleshooting

There may be a bunch of reasons for a build to fail.

The best way to learn the reason is to check the build logs. See [**Working With Build Logs**](/build/build-process-management#working-with-build-logs) section for details on this.

Build logs will display everything that happened in each workflow step in detail and let you examine what went wrong during the build.

If you are unable to determine the exact cause, feel free to get in touch with Appcircle using the in-app messaging for additional support.

### Troubleshooting Workflow Steps for Build Failures

Most build failures are related with the following build steps. If you encounter any errors, [please remove or edit the following steps](/workflows) and get a build to help isolate the cause of the issue.

- **iOS Sign Errors:** If the selected provisioning profile does not match with the selected bundle ID or if the certificate is not valid, you may have an issue in the iOS signing step. In this case, you may try getting an unsigned build
- **Xcode Build for Simulator step:** This step builds your target for either x86_64 or arm64 architecture. In some projects, there may be dependencies that are not compatible with given architecture. In this case, please remove this step from the workflow or remove the conflicting dependencies to get a successful build.
- **Android Sign Errors:** If you encounter errors while signing your Android app, you can remove this step to get an unsigned build or you can configure the app signing within your project.

### The Build is Taking Too Long

With every build, a brand new virtual machine is started to perform your workflow and build your application.

Some applications may have 3rd party dependencies which need to be installed before the build is performed. With every new build, these dependencies need to be re-installed.

One way to speed up the build time may be to manage your dependencies in your project. This will speed up your builds significantly if your application has an excess amount of dependencies to be installed.

If you still think that your build is taking significantly longer than it should, please feel free to [**get in touch with Appcircle**](https://appcircle.io/support/) for additional support.
