---
title: Building .NET MAUI Apps with Custom Scripts
description: Learn how to build .NET MAUI apps with custom scripts in Appcircle
tags: [build, platform build guides, MAUI, .NET MAUI, custom scripts]
sidebar_position: 10
---

# Building .NET MAUI Apps with Custom Scripts

// todo

:::tip

Some Appcircle features might not be supported for .NET MAUI build profiles on the dashboard, or you might need to do some extra customizations in the custom scripts to use them.

In this case, do not hesitate to [contact us](https://appcircle.io/support/) for support. We will do our best to support your build pipeline for .NET MAUI apps.

Also, **official .NET MAUI support is on our roadmap**, and we're actively working on it to provide you with the best solution for your .NET MAUI apps.

:::

### iOS Custom Script for .NET MAUI Builds

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

**4.** In the [build profile configuration](/build/build-process-management/build-profile-configuration), open the **Config** tab and edit the settings below.

- **XCODE VERSION**: Select the Xcode version that's compatible with your app. For instance, `15.4.x`. You can take a look at the table [here](https://github.com/dotnet/maui/wiki/Release-Versions) for the compatible Xcode versions.
- **XCODE PROJECT OR WORKSPACE PATH**: Enter the project or workspace file name. For instance, `Calculator.xcodeproj`.
- **BUILD SCHEME**: Enter a build scheme from your project for the release configuration. For instance, `Calculator`.

:::info

Keep in mind that, in order to switch to the selected Xcode version in the build pipeline, the [workflow](/workflows) should also have an [**Xcode Select**](/workflows/ios-specific-workflow-steps/xcode-select) step.

:::

:::caution

The selected pool in the **SELECT A POOL** list should be the `Default M1 Pool` for the Appcircle Cloud or a pool that has **`arm64`** macOS runners for the self-hosted Appcircle.

Intel-based runners are not supported or documented as of now, and you might need extra customizations done in the custom scripts.

:::

**5.** In the [build profile configuration](/build/build-process-management/build-profile-configuration), open the **Signing** tab and **add provisioning profile** by selecting from the list of Signing Identities.

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
- **`appleCertificate`**: You should use the certificate name as seen on the [Apple Certificates](/signing-identities/apple-certificates) list. It should also be compatible with the selected provisioning profile that you have selected from the  [build profile configuration](/build/build-process-management/build-profile-configuration) **Signing** tab.
- **`appleProfile`**: It should be the name of the selected provisioning profile at the [build profile configuration](/build/build-process-management/build-profile-configuration) **Signing** tab. You can also see the name on the [Apple Profiles](/signing-identities/apple-profiles) list.

When the build pipeline is completed successfully, you will see the signed `.ipa` in the [build artifacts](/build/post-build-operations/after-a-build#ios-outputs).

### Android Custom Script for .NET MAUI Builds

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

**3.** In your [workflow](/workflows), use the below **Custom Script** as a replacement of the default **Android Build** step.

:::info

When you remove the **Android Build** step from the workflow, the workflow editor might give some errors or warnings for other components that depend on the **Android Build** step.

Just ignore them and go on with the **Save** button when you remove the **Android Build** step in the workflow editor.

As an alternative, you can disable the **Step Execution Active** toggle in **Android Build** step details, which will also make it inactive in the build pipeline.

:::

```bash
set -e
set -x

curl -sS -O https://cdn.appcircle.io/dotnet-install.sh
chmod u+x dotnet-install.sh
./dotnet-install.sh --version 8.0.303
dotnet="$HOME/.dotnet/dotnet"

framework="net8.0-ios"
project="$AC_REPOSITORY_DIR/src/Calculator/Calculator.csproj"

$dotnet workload install maui-ios
$dotnet build $project -p:TargetFrameworks=$framework
$dotnet publish $project -p:TargetFrameworks=$framework \
  -f $framework -c Release \
  -p:AndroidPackageFormats=apk \
  -p:AndroidKeyStore=false \
  -o "$AC_REPOSITORY_DIR/build/outputs"

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

// TODO: in progress...

___

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />
