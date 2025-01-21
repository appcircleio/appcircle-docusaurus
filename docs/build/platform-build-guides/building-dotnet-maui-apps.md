---
title: Building .NET MAUI Apps
description: Learn how to build a .NET MAUI app on Appcircle
tags: [build, platform build guides, MAUI, .NET MAUI, custom scripts]
sidebar_position: 10
---

# Building .NET MAUI Apps

This guide gives necessary information about the steps that should be followed to successfully build and publish a [.NET MAUI](https://dotnet.microsoft.com/en-us/apps/maui) app with Appcircle.

It's an introduction to the basic steps such as build, code signing, and app publishing. Although these steps are minimum requirements for a mobile app build pipeline, you should go on with other sections of the Appcircle documentation for numerous advanced CI/CD features.

If you don't have a .NET MAUI app already or want to follow the steps quickly for a fast evaluation, you can use the [sample app](https://github.com/dotnet/maui-samples/tree/main/8.0/Apps/Calculator) Calculator from the `dotnet/maui-samples` repository. To simulate a .NET MAUI repository, it will be good to clone the app folder and add it as a repository to your own Git provider.

:::tip

Some Appcircle features might not be supported for .NET MAUI build profiles on the dashboard, or you might need to do some extra customizations in the custom scripts to use them.

In this case, do not hesitate to [contact us](https://appcircle.io/support/) for support. We will do our best to support your build pipeline for .NET MAUI apps.

Additionally, **official .NET MAUI support is on our roadmap**, and we are actively working on it to give you the best solution for your .NET MAUI apps.

:::

### .NET MAUI Build for iOS

In order to build a .NET MAUI iOS app on Appcircle follow the steps below.

**1.** [Create](/build/manage-the-connections/adding-a-build-profile) a new build profile for your app.

- `iOS` should be selected as the **Target Operating System**, and `Objective-C / Swift` should be selected as the **Target Platform**.

**2.** Connect your repository using a compatible connection method.

:::tip

You can disable the **Autofill** toggle or ignore the output of **Autofill** run since it does not support .NET MAUI app metadata processing.

:::

:::info

As of now, Appcircle does not have a sample repository for .NET MAUI apps. So the **quick start using the sample repository** option will not work for .NET MAUI build profiles. You should use your own repository.

:::

**3.** Configure [Apple Certificates](/signing-identities/apple-certificates) and [Apple Profiles](/signing-identities/apple-profiles) using the **Signing Identities** module on Appcircle.

These certificates and provisioning profiles will be used while building the signed app in the build pipeline.

:::info

Keep in mind that, in order to use iOS Signing Identities in the build pipeline, the [workflow](/workflows) should also have an [**Install Certificates & Profiles**](/workflows/ios-specific-workflow-steps/install-certificates-provisions) step.

:::

**4.** In the [build profile configuration](/build/build-process-management#profile-configuration), open the **Config** tab and edit the settings below.

- **XCODE VERSION**: Select the Xcode version that's compatible with your app. For instance, `15.4.x`. You can take a look at the table [here](https://github.com/dotnet/maui/wiki/Release-Versions) for the compatible Xcode versions.
- **XCODE PROJECT OR WORKSPACE PATH**: Enter the project or workspace file name. For instance, `Calculator.xcodeproj`.
- **BUILD SCHEME**: Enter a build scheme from your project for the release configuration. For instance, `Calculator`.

:::info

Keep in mind that, in order to switch to the selected Xcode version in the build pipeline, the [workflow](/workflows) should also have an [**Xcode Select**](/workflows/ios-specific-workflow-steps/xcode-select) step.

:::

:::caution

The selected pool in the **SELECT A POOL** list should be the `Appcircle Standard macOS Pool (arm64)` for the Appcircle Cloud or a pool that has **`arm64`** macOS runners for the self-hosted Appcircle.

Intel-based runners are not supported or documented as of now, and you might need extra customizations done in the custom scripts.

:::

**5.** In the [build profile configuration](/build/build-process-management#profile-configuration), open the **Signing** tab and **add provisioning profile** by selecting from the list of Signing Identities.

:::caution

Currently, **Automatic Code Signing** is not supported for iOS .NET MAUI builds. For this reason, do not enable that toggle and go on with manual code signing as mentioned above.

:::

**6.** In your [workflow](/workflows), use the below custom script as a replacement of the default **Xcodebuild for Devices** step.

:::info

When you remove the **Xcodebuild for Devices** step from the default workflow, the workflow editor might give some errors or warnings for other components that depend on the **Xcodebuild for Devices** step.

Just ignore them and go on with the **Save** button when you remove the **Xcodebuild for Devices** step in the workflow editor.

As an alternative, you can disable the **Step Execution Active** toggle in **Xcodebuild for Devices** step details, which will also make it inactive in the build pipeline.

:::

```bash
set -e
set -x

dotnetVersion="8.0.303"

framework="net8.0-ios"
project="$AC_REPOSITORY_DIR/src/Calculator/Calculator.csproj"
appleCertificate="Apple Distribution: APPCIRCLE, INC. (8U2Z24R99J)"
appleProfile="AppStore Appcircle Sample"

curl -sS -O https://cdn.appcircle.io/dotnet-install.sh
chmod u+x dotnet-install.sh
./dotnet-install.sh --version $dotnetVersion
dotnet="$HOME/.dotnet/dotnet"

$dotnet workload install maui-ios
$dotnet build $project -p:TargetFrameworks=$framework
$dotnet publish $project -p:TargetFrameworks=$framework \
  -f $framework -c Release \
  -p:ArchiveOnBuild=true \
  -p:RuntimeIdentifier=ios-arm64 \
  -p:CodesignKey="\"$appleCertificate\"" \
  -p:CodesignProvision="\"$appleProfile\"" \
  -o "$AC_OUTPUT_DIR"

```

The custom script above does the following operations in order to build a .NET MAUI iOS app:

- Install .NET SDK
- Install `maui-ios` workload
- Build the project with dependencies
- Publish the app for deployment

The custom script has some **variables that should be changed or customized** for your pipeline.

- **`dotnetVersion`**: You can select a .NET SDK version that's compatible with your project or solution. See [here](https://github.com/dotnet/maui/wiki/Release-Versions) for details.
- **`framework`**: You should select a target framework that the app will be built for, considering your project requirements and .NET SDK version. See [here](https://learn.microsoft.com/en-us/dotnet/standard/frameworks) for details.
- **`project`**: It should be the path to the project file for your app. `$AC_REPOSITORY_DIR` is a [reserved environment variable](/environment-variables/appcircle-specific-environment-variables) that should not be changed since it has the repository path value. You can change the rest of the path to customize it for your project structure.
- **`appleCertificate`**: You should use the certificate name as seen on the [Apple Certificates](/signing-identities/apple-certificates) list. It should also be compatible with the selected provisioning profile that you have selected from the  [build profile configuration](/build/build-process-management#profile-configuration) **Signing** tab.
- **`appleProfile`**: It should be the name of the selected provisioning profile at the [build profile configuration](/build/build-process-management#profile-configuration) **Signing** tab. You can also see the name on the [Apple Profiles](/signing-identities/apple-profiles) list.

When the build pipeline is completed successfully, you will see the signed `.ipa` in the [build artifacts](/build/build-process-management#download-artifacts).

#### References

You can find more information in the following resources for customizing and troubleshooting the .NET MAUI build pipeline.

- .NET Multi-platform App UI [documentation](https://learn.microsoft.com/en-us/dotnet/maui)
- `dotnet-install.sh` script [documentation](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-install-script)
- `dotnet workload install` [documentation](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-workload-install)
- `dotnet build` [documentation](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-build)
- `dotnet publish` [documentation](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-publish)
- [Publish an iOS app](https://learn.microsoft.com/en-us/dotnet/maui/ios/deployment/publish-cli?view=net-maui-8.0) using the command line

### .NET MAUI Build for Android

In order to build a .NET MAUI Android app on Appcircle follow the steps below.

**1.** [Create](/build/manage-the-connections/adding-a-build-profile) a new build profile for your app.

- `Android` should be selected as the **Target Operating System**, and `Java / Kotlin` should be selected as the **Target Platform**.

**2.** Connect your repository using a compatible connection method.

:::tip

You can disable the **Autofill** toggle or ignore the output of **Autofill** run since it does not support .NET MAUI app metadata processing.

:::

:::info

As of now, Appcircle does not have a sample repository for .NET MAUI apps. So the **quick start using the sample repository** option will not work for .NET MAUI build profiles. You should use your own repository.

:::

**4.** Add your keystore to [Android Keystores](https://docs.appcircle.io/signing-identities/android-keystores) using the **Signing Identities** module on Appcircle.

These keystores will be used while building the signed app in the build pipeline.

:::info

Keep in mind that, in order to use Android Signing Identities in the build pipeline, the [workflow](/workflows) should also have an [**Android Sign**](/workflows/android-specific-workflow-steps/android-sign) step.

:::

**5.** In the [build profile configuration](/build/build-process-management#profile-configuration), open the **Signing** tab and select your app's keystore from the list of Signing Identities.

**6.** In your [workflow](/workflows), use the below **Custom Script** as a replacement of the default **Android Build** step.

:::info

When you remove the **Android Build** step from the workflow, the workflow editor might give some errors or warnings for other components that depend on the **Android Build** step.

Just ignore them and go on with the **Save** button when you remove the **Android Build** step in the workflow editor.

As an alternative, you can disable the **Step Execution Active** toggle in **Android Build** step details, which will also make it inactive in the build pipeline.

:::

```bash
set -e
set -x

dotnetVersion="8.0.303"

framework="net8.0-android"
project="$AC_REPOSITORY_DIR/src/Calculator/Calculator.csproj"
packageFormat="apk"

curl -sS -O https://cdn.appcircle.io/dotnet-install.sh
chmod u+x dotnet-install.sh
./dotnet-install.sh --version $dotnetVersion
dotnet="$HOME/.dotnet/dotnet"

$dotnet workload install maui-android
$dotnet build $project -p:TargetFrameworks=$framework
$dotnet publish $project -p:TargetFrameworks=$framework \
  -f $framework -c Release \
  -p:AndroidPackageFormats="\"$packageFormat\"" \
  -p:AndroidKeyStore=false \
  -o "$AC_REPOSITORY_DIR/build/outputs"

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

The custom script above does the following operations in order to build a .NET MAUI Android app:

- Install .NET SDK
- Install `maui-android` workload
- Build the project with dependencies
- Publish the app for deployment
- Pass build outputs to **Android Sign** step

The custom script has some **variables that should be changed or customized** for your pipeline.

- **`dotnetVersion`**: You can select a .NET SDK version that's compatible with your project or solution. See [here](https://github.com/dotnet/maui/wiki/Release-Versions) for details.
- **`framework`**: You should select a target framework that the app will be built for, considering your project requirements and .NET SDK version. See [here](https://learn.microsoft.com/en-us/dotnet/standard/frameworks) for details.
- **`project`**: It should be the path to the project file for your app. `$AC_REPOSITORY_DIR` is a [reserved environment variable](/environment-variables/appcircle-specific-environment-variables) that should not be changed since it has the repository path value. You can change the rest of the path to customize it for your project structure.
- **`packageFormat`**: A semi-colon delimited property that indicates if you want to package the app as an APK file or AAB. Set to either `aab` or `apk` to generate only one format.

When the build pipeline is completed successfully, you will see the signed `.apk` or `.aab` in the [build artifacts](/build/build-process-management#download-artifacts).

:::info

If your project includes a keystore, you can generate a signed artifact in the custom script using relevant `dotnet publish` arguments. See [here](https://learn.microsoft.com/en-us/dotnet/maui/android/deployment/publish-cli?view=net-maui-8.0#build-and-sign-your-app) for comprehensive documentation about the `dotnet publish` command and its parameters.

You can also use the **Signing Identities** from Appcircle when you are signing your app with `dotnet publish`. In this case, you should bind the relevant command parameters to the [**reserved Android variables**](/environment-variables/appcircle-specific-environment-variables#reserved-android-variables) as arguments.

Keep in mind that, if you sign your app with the `dotnet publish`, you will not need the **Android Sign** step in your workflow. So, you should disable it or remove it from your workflow.

Also, change the output directory (`-o|--output`) to `$AC_OUTPUT_DIR` to send the signed artifacts directly to the [build artifacts](/build/build-process-management#download-artifacts).

:::

#### References

You can find more information in the following resources for customizing and troubleshooting the .NET MAUI build pipeline.

- .NET Multi-platform App UI [documentation](https://learn.microsoft.com/en-us/dotnet/maui)
- `dotnet-install.sh` script [documentation](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-install-script)
- `dotnet workload install` [documentation](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-workload-install)
- `dotnet build` [documentation](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-build)
- `dotnet publish` [documentation](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-publish)
- [Publish an Android app](https://learn.microsoft.com/en-us/dotnet/maui/android/deployment/publish-cli?view=net-maui-8.0) using the command line

### Next Steps

The document above has introduced the basic steps such as build, code signing, and app publishing for [.NET MAUI](https://dotnet.microsoft.com/en-us/apps/maui) apps on Appcircle.

Although these steps are the minimum requirements for a mobile app build pipeline, they are certainly not the end. Appcircle has some other advanced features that can help your mobile operations.

We suggest you check out the following modules for specific use cases mentioned below:

- Use [Testing Distribution](/testing-distribution) to deploy the .NET MAUI app to your tester groups to get feedback.
- Ready to release? Then [Publish](/publish-module) the .NET MAUI app to public stores such as Google Play, App Store, or Huawei AppGallery.
- Use the [Enterprise App Store](/enterprise-app-store) if you want to distribute the .NET MAUI app to your in-house or private users.

___

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />
