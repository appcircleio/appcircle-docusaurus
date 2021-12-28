---
title: 'Building Flutter Web Applications'
metaTitle: 'Building Flutter Web Applications'
metaDescription: 'Building Flutter Web Applications'
---

# Building Flutter Web Applications

If your app supports Flutter Web, you can also build the Flutter web app along with the [Flutter iOS or Android build](building-flutter-applications).

With Appcircle, you can manage your entire Flutter build workflows both for mobile and web without the need for any third party solutions.&#x20;

Flutter Web Build is available as a workflow step in the workflow marketplace. Just configure your project as you would for iOS or Android and add the Flutter Build for Web step anywhere after the Flutter Install step to include a web build in the workflow.

![](<https://cdn.appcircle.io/docs/assets/image (97).png>)

If you want to build your Flutter project only for the web, you can [add a Flutter Android project in the standard way](building-flutter-applications#creating-a-react-native-build-profile), save your project configuration once, and then remove all the Android-related steps from the build workflow.

In this case, the workflow may look like the following:

![](<https://cdn.appcircle.io/docs/assets/image (98).png>)

If you want to deploy your web output automatically, you can use a [Custom Script](https://github.com/appcircleio/appcircle-custom-script-component/) or [upload it to Amazon S3](https://docs.appcircle.io/workflows/uploading-files-to-amazon-s3-in-the-workflows).

Once your build is configured, it can be built [manually or automatically in the same way with other apps](build-manually-or-with-triggers). With Flutter 2.0, you can build your Flutter web apps in the stable channel. (In Flutter 1.x, it was necessary to use the beta channel.)

![](<https://cdn.appcircle.io/docs/assets/image (101).png>)

After a build, you can download the web build output manually [from the build artifact list](building-flutter-applications#starting-a-flutter-build-and-after-a-build) as the `web.zip` file.

![](<https://cdn.appcircle.io/docs/assets/image (99).png>)
