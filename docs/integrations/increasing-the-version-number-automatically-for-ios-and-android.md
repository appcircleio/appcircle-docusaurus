---
title: Increasing the Version Number Automatically for iOS and Android
metaTitle: Increasing the Version Number Automatically for iOS and Android
metaDescription: Increasing the Version Number Automatically for iOS and Android
sidebar_position: 5
---

import ContentRef from '@site/src/components/ContentRef';

# Increasing the Version Number Automatically for iOS and Android

Appcircle provides a reserved environment variable that returns the latest build number:;

`AC_BUILD_NUMBER`

This variable stores the number of builds in a specific branch (i.e. on a configuration/worfklow basis) and it is automatically increased every time a new build is run, regardless of the build status.

As with most reserved environment variables, this variable is maintained separately for each branch under each build profile and it is incremented individually for each workflow, so if you have the same project in different build profiles, the build numbers may overlap depending on how they are used.

You can use this variable in the build workflows and custom scripts for different purposes, most commonly for increasing the build number automatically for iOS and Android.



For Android, you may include this in a custom script step as a ruby or a bash script that modifies the `build.gradle` file before the build or incorporate it directly within the file itself:

It is up to you how to reflect the build number to the app, but one common practice is to set the `versionCode` value as the value of `AC_BUILD_NUMBER`.

An example is available in the [Appcircle Sample Android Project in build.gradle as follows](https://github.com/appcircleio/appcircle-sample-android/blob/master/app/build.gradle#L12):

```groovy
if (System.getenv("AC_APPCIRCLE")) {
    def buildNumber = System.getenv("AC_BUILD_NUMBER")
    versionName = "1.0." + buildNumber
    versionCode = Integer.valueOf(buildNumber)
} else {
    versionCode 2
    versionName "1.0.1"
}
```

If you want to have better control over `versionCode` and `versionName` management, you may also use the Android Versioning component. Please check the following document for more information.

<ContentRef url="/versioning/android-version">
  Android Versioning
</ContentRef>

For iOS, you should use the Versioning Tab on your config screen to manage the build and version number. Please check the following document to learn more about the iOS Versioning system.

<ContentRef url="/versioning/ios-version">
  iOS Versioning
</ContentRef>
