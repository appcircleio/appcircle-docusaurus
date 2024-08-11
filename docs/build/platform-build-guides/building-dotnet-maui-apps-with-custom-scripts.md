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

:::

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

echo $PWD

curl -sS -O https://cdn.appcircle.io/dotnet-install.sh
chmod u+x dotnet-install.sh
./dotnet-install.sh --version 8.0.303
dotnet="$HOME/.dotnet/dotnet"

framework="net8.0-android"
project="$AC_REPOSITORY_DIR/src/Calculator/Calculator.csproj"

$dotnet workload install maui-android
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

**3.** In your [workflow](/workflows), use the below custom script as a replacement of the default **Xcodebuild for Devices** step.

```bash
set -e
set -x

cd $AC_REPOSITORY_DIR

echo "Hello world!"

```

// TODO: in progress...

___

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />
