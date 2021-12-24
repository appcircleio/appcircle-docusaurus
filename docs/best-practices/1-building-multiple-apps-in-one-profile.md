---
title: "Building Multiple Apps in One Profile"
metaTitle: "Building Multiple Apps in One Profile"
metaDescription: "Building Multiple Apps in One Profile"
---
# Building Multiple Apps in One Profile

Depending on the structure of your project(s), at one point there might be a need to produce more than one application from a single codebase.

For this situation, there are two ways to accomplish this goal:

* Configure your relevant file to produce different outputs.
  * Android -> Build Variants with Product Flavors
  * For iOS -> Creating different Targets with Schemes
* Do the steps manually via custom scripts.

:::info

For this task, the developer should configure those from Android Studio or Xcode.

:::

> A different Application means a different packagename for Android and different bundleId for iOS.

### Using Android Product Flavors and Build Variant to Configure Multiple Apps

The Android Developers document has a detailed guide on how to configure build variants and product flavors:

{% embed url="https://developer.android.com/studio/build/build-variants" %}

The assets that you can directly change with the `productFlavor`

* Package Id -> packageName
* App Name
* App Icon

For more information, check the Android Developer Document on `productFlavor`

{% embed url="https://developer.android.com/reference/tools/gradle-api/4.2/com/android/build/api/dsl/ProductFlavor" %}

#### How to Change Variant Programmatically on Appcircle

:::info


This method will not be required in common scenarios. Unless you have a special case, it is advised to stick with configuring `build.gradle` instead, as specified at the Android Developers document.

:::

For example, the script below will change the variant if the built branch is `release` .&#x20;

:::tip

Put this script before the relevant **build **step. E.g. for Android, this script should be executed **before **`Android Build` step.

:::

Note: This script is in `Bash` language.

```bash
if [ $AC_GIT_BRANCH = 'release' ]; then
	echo "AC_VARIANTS=YOUR_FLAVOR" >> $AC_ENV_FILE_PATH
fi
```

For more information about environment variables, [click here](https://docs.appcircle.io/environment-variables/appcircle-specific-environment-variables#android-specific-environment-variables).

### Using iOS Schemes to Configure Multiple Apps

Creating and controlling multiple Schemes on an Xcode project is fairly easy. Check the [Apple Help Documentation](https://help.apple.com/xcode/mac/current/#/dev0bee46f46) about how to create & manage schemes.

The assets that you can directly change with the Schemes

* Bundle ID
* Plist file
* App Icon

<!-- ![](<../assets/image (216).png>) -->

&#x20;For more information about iOS Multiple Targets, navigate to the [Apple Help Documentation](https://help.apple.com/xcode/mac/current/#/dev38419576c)&#x20;

###

#### How to Change Target Programmatically on Appcircle

:::info


This method will not be required in common scenarios. Unless you have a special case, it is advised to configure multiple `plist` files and bundling them into a single scheme.

:::

For example, the script below will change the scheme if the built branch is `release` .

:::tip

Put this script before the relevant **build **step. E.g. for Android, this script should be executed **before **`Android Build` step.

:::

Note: This script is in `Bash` language.

```bash
if [ $AC_GIT_BRANCH = 'release' ]; then
	echo "AC_SCHEME=YOUR_FLAVOR" >> $AC_ENV_FILE_PATH
fi
```

For more information about environment variables, [click here](https://docs.appcircle.io/environment-variables/appcircle-specific-environment-variables#ios-specific-environment-variables)

### Testing & Downloading Multiple Apps Through Appcircle

As specified in the Appcircle docs, your multiple outputs will be located on the testing distribution and they will be available for download just like a single application.

{% embed url="https://docs.appcircle.io/distribute/create-or-select-a-distribution-profile#android-applications-with-multiple-flavor" %}

