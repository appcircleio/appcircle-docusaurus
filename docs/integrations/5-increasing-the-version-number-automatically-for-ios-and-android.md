---
title: "Increasing the Version Number Automatically for iOS and Android"
metaTitle: "Increasing the Version Number Automatically for iOS and Android"
metaDescription: "Increasing the Version Number Automatically for iOS and Android"
---
# Increasing the Version Number Automatically for iOS and Android

Appcircle provides a reserved environment variable that returns the latest build number:&#x20;

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



For iOS, you need to include this in a custom script step as a ruby or a bash script that modifies the `Info.plist` file before the build.

It is up to you how to reflect the build number to the app, but one common practice is to set the `CFBundleVersion` value as the value of `AC_BUILD_NUMBER`.

An example custom bash script for this purpose is as follows:

```bash
set -e
set -x
/usr/libexec/PlistBuddy -c "Set :CFBundleVersion $AC_BUILD_NUMBER" "$AC_REPOSITORY_DIR/<path-to-plist>/Info.plist"
```

**Make sure you enter the path to your Plist file correctly.**

