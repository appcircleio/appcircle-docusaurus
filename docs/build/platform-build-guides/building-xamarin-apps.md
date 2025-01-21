---
title: Building Xamarin Apps
description: Learn how to build a Xamarin app on Appcircle
tags: [build, platform build guides, .net, xamarin, custom scripts]
sidebar_position: 10
---

# Building Xamarin Apps

This guide gives necessary information about the steps that should be followed to successfully build and publish a [Xamarin](https://dotnet.microsoft.com/en-us/apps/xamarin) app with Appcircle.

It's an introduction to the basic steps such as build, code signing, and app publishing. Although these steps are minimum requirements for a mobile app build pipeline, you should go on with other sections of the Appcircle documentation for numerous advanced CI/CD features.

If you don't have a Xamarin app already or want to follow the steps quickly for a fast evaluation, you can use the [sample app](https://github.com/appcircleio/appcircle-sample-xamarin) repository. To simulate a Xamarin repository, it will be good to clone the app folder and add it as a repository to your own Git provider.

:::danger
As of May 1, 2024, Xamarin is no longer supported or updated by Microsoft. **Therefore, Appcircle does not officially support Xamarin and does not guarantee that all Xamarin projects will build without issues.** See the [Xamarin support policy](https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin) for details.

Some Appcircle features might not be supported for Xamarin build profiles on the dashboard, or you might need to do some extra customizations in the custom scripts to use them.

In this case, do not hesitate to [contact us](https://appcircle.io/support/) for support. We will do our best to support your build pipeline for Xamarin apps.
:::

### Xamarin Build for iOS

In order to build a Xamarin iOS app on Appcircle, follow the steps below.

**1.** [Create](/build/manage-the-connections/adding-a-build-profile) a new build profile for your app.

- `iOS` should be selected as the **Target Operating System**, and `Objective-C/Swift` should be selected as the **Target Platform**.

**2.** Connect your repository using a compatible connection method.

:::tip

You can disable the **Autofill** toggle or ignore the output of the **Autofill** run since it does not support Xamarin app metadata processing.

:::

:::info

As of now, Appcircle does not have a sample repository for Xamarin apps. So the **quick start using the sample repository** option will not work for Xamarin build profiles. You should use your own repository.

:::

**3.** Configure [Apple Certificates](/signing-identities/apple-certificates) and [Apple Profiles](/signing-identities/apple-profiles) using the **Signing Identities** module on Appcircle.

These certificates and provisioning profiles will be used while building the signed app in the build pipeline.

:::info

Keep in mind that, in order to use iOS Signing Identities in the build pipeline, the [workflow](/workflows) should also have an [**Install Certificates & Profiles**](/workflows/ios-specific-workflow-steps/install-certificates-provisions) step.

:::

**4.** In the [Build Profile Configuration](/build/build-process-management#profile-configuration), open the **Config** tab and edit the settings below.

- **XCODE VERSION**: Select the Xcode version that's compatible with your app. For instance, `14.3.x`.
- **XCODE PROJECT OR WORKSPACE PATH**: The custom script we will use does not require a valid Xcode project path. If you haven't exported your Xamarin project to Xcode yet, you can provide a temporary path. For instance, `temp.xcodeproj`.
- **BUILD SCHEME**: Enter a build scheme from your project for the release configuration. For instance, `TempDev`.

:::info

Keep in mind that, in order to switch to the selected Xcode version in the build pipeline, the [workflow](/workflows) should also have an [**Xcode Select**](/workflows/ios-specific-workflow-steps/xcode-select) step.

:::

:::caution

The selected pool in the **SELECT A POOL** list should be the `Appcircle Standard macOS Pool (arm64)` for the Appcircle Cloud or a pool that has **`arm64`** macOS runners for the self-hosted Appcircle.

Intel-based runners are not supported or documented as of now, and you might need extra customizations done in the custom scripts.

:::

**5.** In the [Build Profile Configuration](/build/build-process-management#profile-configuration), open the **Signing** tab and **add provisioning profile** by selecting from the list of Signing Identities.

:::caution

Currently, **Automatic Code Signing** is not supported for iOS Xamarin builds. For this reason, do not enable that toggle and go on with manual code signing as mentioned above.

:::

**6.** In your [workflow](/workflows), use the below custom script as a replacement of the default **Xcodebuild for Devices** step. Remove the **CocoaPods Install** and **Increment Build and Version Number** steps from your workflow.

:::info

When you remove the **Xcodebuild for Devices** step from the default workflow, the workflow editor might give some errors or warnings for other components that depend on the **Xcodebuild for Devices** step.

Just ignore them and go on with the **Save** button when you remove the **Xcodebuild for Devices** step in the workflow editor.

As an alternative, you can disable the **Step Execution Active** toggle in **Xcodebuild for Devices** step details, which will also make it inactive in the build pipeline.

:::

```bash
set -e

MONO_VERSION="6.12.0.206"
DOTNET_VERSION="8.0.402"
XAMARIN_IOS_SDK_DOWNLOAD_URL="https://download.visualstudio.microsoft.com/download/pr/ceb0ea3f-4db8-46b4-8dc3-8049d27c0107/3960868aa9b1946a6c77668c3f3334ee/xamarin.ios-16.4.0.23.pkg"
PROJECT_ROOT_DIR="$AC_REPOSITORY_DIR"
IOS_PROJECT_DIR="AppcircleXamarin.iOS/AppcircleXamarin.iOS.csproj"
APPLE_PROFILE_NAME="Adhoc Appcircle Sample"
APPLE_CERTIFICATE_NAME="Apple Distribution: APPCIRCLE, INC. (8U2Z24R99J)"


APPLE_CERTIFICATE_ID=$(security find-identity -v -p codesigning | grep "$APPLE_CERTIFICATE_NAME" | awk '{print $2}' | head -n 1)
APPLE_PROFILE_ID=$(for profile in ~/Library/MobileDevice/Provisioning\ Profiles/*.mobileprovision; do
    if security cms -D -i "$profile" | grep -q "<key>Name</key>" && \
       security cms -D -i "$profile" | grep -A 1 "<key>Name</key>" | grep -q "$APPLE_PROFILE_NAME"; then
        security cms -D -i "$profile" | grep "<key>UUID</key>" -A 1 | grep "<string>" | awk -F '[<>]' '{print $3}'
    fi
done)

curl -sS -O https://cdn.appcircle.io/docs/assets/mono_install.sh
chmod u+x mono_install.sh
./mono_install.sh --version $MONO_VERSION
export PATH=$PATH:/Library/Frameworks/Mono.framework/Versions/Current/bin/

curl -sS -O https://cdn.appcircle.io/dotnet-install.sh
chmod u+x dotnet-install.sh
sudo ./dotnet-install.sh --version $DOTNET_VERSION --install-dir /usr/local/share/dotnet
export PATH=$PATH:/usr/local/share/dotnet:$HOME/.dotnet/tools

dotnet tool install --global boots
sudo boots $XAMARIN_IOS_SDK_DOWNLOAD_URL

cd $PROJECT_ROOT_DIR
nuget restore $IOS_PROJECT_DIR
dotnet restore

msbuild $IOS_PROJECT_DIR /t:Build /p:Configuration=Release /p:Platform=iPhone /p:BuildIpa=true /p:OutputPath=$AC_OUTPUT_DIR /p:KeychainPath=$AC_KEYCHAIN_PATH /p:KeychainPassword=$AC_KEYCHAIN_PASSWORD /p:CodesignKey=$APPLE_CERTIFICATE_ID /p:ProvisioningProfileId=$APPLE_PROFILE_ID


```

The custom script above does the following operations in order to build a Xamarin iOS app:

- Install [Mono](https://www.mono-project.com/)
- Install .NET SDK
- Install Xamarin iOS SDK
- Build the project with dependencies
- Publish the app for deployment

The custom script has some **variables that should be changed or customized** for your pipeline.

- **`MONO_VERSION`**: You can select a Mono version that's compatible with your project or solution. See [here](https://www.mono-project.com/) for details.
- **`DOTNET_VERSION`**: You can select a .NET SDK version that's compatible with your project or solution. See [here](https://versionsof.net/) for details.
- **`XAMARIN_IOS_SDK_DOWNLOAD_URL`**: The download link for the Xamarin iOS SDK version you want to install. Copy the link for the version from [here](https://github.com/xamarin/xamarin-macios/blob/main/DOWNLOADS.md).
- **`PROJECT_ROOT_DIR`**: The location of your `<YourProject>.sln` file. Your Git repository is typically saved within the `$AC_REPOSITORY_DIR` inside the runner. However, your .sln file may be located in a subdirectory of this folder. Please specify this. For instance, `$AC_REPOSITORY_DIR/src`
- **`IOS_PROJECT_DIR`**: The location of the `<YOUR_IOS_PROJECT>.csproj` file is required for performing iOS-specific builds. In this script, it is `AppcircleXamarin.iOS/AppcircleXamarin.iOS.csproj`.
- **`APPLE_CERTIFICATE_NAME`**: You should use the certificate name as seen on the [Apple Certificates](/signing-identities/apple-certificates) list. It should also be compatible with the selected provisioning profile that you have selected from the  [Build Profile Configuration](/build/build-process-management#profile-configuration) **Signing** tab.
- **`APPLE_PROFILE_NAME`**: It should be the name of the selected provisioning profile at the [Build Profile Configuration](/build/build-process-management#profile-configuration) **Signing** tab. You can also see the name on the [Apple Profiles](/signing-identities/apple-profiles) list.

When the build pipeline is completed successfully, you will see the signed `.ipa` in the [build artifacts](/build/build-process-management#download-artifacts).


### Xamarin Build for Android

In order to build a Xamarin Android app on Appcircle, follow the steps below.

**1.** [Create](/build/manage-the-connections/adding-a-build-profile) a new build profile for your app.

- `Android` should be selected as the **Target Operating System**, and `Java/Kotlin` should be selected as the **Target Platform**.

**2.** Connect your repository using a compatible connection method.

:::tip

You can disable the **Autofill** toggle or ignore the output of the **Autofill** run since it does not support Xamarin app metadata processing.

:::

:::info

As of now, Appcircle does not have a sample repository for Xamarin apps. So the **quick start using the sample repository** option will not work for Xamarin build profiles. You should use your own repository.

:::

**4.** Add your keystore to [Android Keystores](/signing-identities/android-keystores) using the **Signing Identities** module on Appcircle.

These keystores will be used while building the signed app in the build pipeline.

:::info

Keep in mind that, in order to use Android Signing Identities in the build pipeline, the [workflow](/workflows) should also have an [**Android Sign**](/workflows/android-specific-workflow-steps/android-sign) step.

:::

**5.** In the [Build Profile Configuration](/build/build-process-management#profile-configuration), open the **Signing** tab and select your app's keystore from the list of Signing Identities.

**6.** In your [workflow](/workflows), use the below **Custom Script** as a replacement of the default **Android Build** step. Remove the **Android App Post-Processor** and **Increment Build and Version Number** steps from your workflow.

:::info

When you remove the **Android Build** step from the workflow, the workflow editor might give some errors or warnings for other components that depend on the **Android Build** step.

Just ignore them and go on with the **Save** button when you remove the **Android Build** step in the workflow editor.

As an alternative, you can disable the **Step Execution Active** toggle in **Android Build** step details, which will also make it inactive in the build pipeline.

:::

```bash
set -e

MONO_VERSION="6.12.0.206"
DOTNET_VERSION="8.0.402"
XAMARIN_ANDROID_SDK_DOWNLOAD_URL="https://aka.ms/xamarin-android-commercial-d17-5-macos"
PROJECT_ROOT_DIR="$AC_REPOSITORY_DIR"
ANDROID_PROJECT_DIR="AppcircleXamarin.Android/AppcircleXamarin.Android.csproj"
ANDROID_PACKAGE_FORMAT="apk"

curl -sS -O https://cdn.appcircle.io/docs/assets/mono_install.sh
chmod u+x mono_install.sh
./mono_install.sh --version $MONO_VERSION
export PATH=$PATH:/Library/Frameworks/Mono.framework/Versions/Current/bin/

curl -sS -O https://cdn.appcircle.io/dotnet-install.sh
chmod u+x dotnet-install.sh
sudo ./dotnet-install.sh --version $DOTNET_VERSION --install-dir /usr/local/share/dotnet
export PATH=$PATH:/usr/local/share/dotnet:$HOME/.dotnet/tools

dotnet tool install --global boots
sudo boots $XAMARIN_ANDROID_SDK_DOWNLOAD_URL

cd $PROJECT_ROOT_DIR
nuget restore $ANDROID_PROJECT_DIR
dotnet restore


msbuild $ANDROID_PROJECT_DIR /t:Package /p:Configuration=Release /p:Platform=AnyCPU /p:AndroidPackageFormat=$ANDROID_PACKAGE_FORMAT /p:OutputPath=$AC_REPOSITORY_DIR/build/outputs


# The code section below is for passing unsigned artifacts
# to the Android Sign step. So it should not be customized.
#
# Changing it might cause incompatibility issues for the next step.
$(which ruby) <<EOF

require 'fileutils'

def get_env_variable(key)
    return (ENV[key] == nil || ENV[key] == "") ? nil : ENV[key]
end
ac_repo_path = get_env_variable("AC_REPOSITORY_DIR") || abort('Missing repo path.')
ac_output_folder = get_env_variable("AC_OUTPUT_DIR") || abort('Missing output folder.')

build_output_folder="#{ac_repo_path}/build/outputs"

puts "Filtering artifacts: #{build_output_folder}/**/*.apk, #{build_output_folder}/**/*.aab"

apks = Dir.glob("#{build_output_folder}/**/*.apk")
aabs = Dir.glob("#{build_output_folder}/**/*.aab")

FileUtils.cp apks, "#{ac_output_folder}"
FileUtils.cp aabs, "#{ac_output_folder}"

apks = Dir.glob("#{ac_output_folder}/**/*.apk").join("|")
aabs = Dir.glob("#{ac_output_folder}/**/*.aab").join("|")

puts "Exporting AC_APK_PATH=#{apks}"
puts "Exporting AC_AAB_PATH=#{aabs}"

open(ENV['AC_ENV_FILE_PATH'], 'a') { |f|
    f.puts "AC_APK_PATH=#{apks}"
    f.puts "AC_AAB_PATH=#{aabs}"
}

exit 0

EOF

```

The custom script above does the following operations in order to build a Xamarin Android app:

- Install [Mono](https://www.mono-project.com/)
- Install .NET SDK
- Install Xamarin Android SDK
- Build the project with dependencies
- Publish the app for deployment
- Pass build outputs to **Android Sign** step

The custom script has some **variables that should be changed or customized** for your pipeline.

- **`MONO_VERSION`**: You can select a Mono version that's compatible with your project or solution. See [here](https://www.mono-project.com/) for details.
- **`DOTNET_VERSION`**: You can select a .NET SDK version that's compatible with your project or solution. See [here](https://versionsof.net/) for details.
- **`XAMARIN_ANDROID_SDK_DOWNLOAD_URL`**: The download link for the Xamarin Android SDK version you want to install. Copy the link for the version from [here](https://github.com/dotnet/android/blob/main/Documentation/previous-releases.md).
- **`PROJECT_ROOT_DIR`**: The location of your `<YourProject>.sln` file. Your Git repository is typically saved within the `$AC_REPOSITORY_DIR` inside the runner. However, your .sln file may be located in a subdirectory of this folder. Please specify this. For instance, `$AC_REPOSITORY_DIR/src`
- **`ANDROID_PROJECT_DIR`**: The location of the `<YOUR_IOS_PROJECT>.csproj` file is required for performing iOS-specific builds. In this script, it is `AppcircleXamarin.Android/AppcircleXamarin.Android.csproj`.
- **`ANDROID_PACKAGE_FORMAT`**: Please specify the type of your application package. It can be either `apk` or `aab`.

When the build pipeline is completed successfully, you will see the signed `.apk` or `.aab` in the [build artifacts](/build/build-process-management#download-artifacts).


### Next Steps

The document above has introduced the basic steps such as build, code signing, and app publishing for [Xamarin](https://dotnet.microsoft.com/en-us/apps/xamarin) apps on Appcircle.

Although these steps are the minimum requirements for a mobile app build pipeline, they are certainly not the end. Appcircle has some other advanced features that can help your mobile operations.

We suggest you check out the following modules for specific use cases mentioned below:

- Use [Testing Distribution](/testing-distribution) to deploy the Xamarin app to your tester groups to get feedback.
- Ready to release? Then [Publish](/publish-module) the Xamarin app to public stores such as Google Play, App Store, or Huawei App Gallery.
- Use the [Enterprise App Store](/enterprise-app-store) if you want to distribute the Xamarin app to your in-house or private users.

___

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />
