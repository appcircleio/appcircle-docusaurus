---
title: Custom Script
description: Use Custom Script steps for additional functionalities in your builds.
tags: [custom scripts, build, test, workflow, step]
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import Screenshot from '@site/src/components/Screenshot';

# Custom Script

You can use **Custom Script** steps for additional functionalities in your builds. Appcircle will run the commands in your custom scripts and perform the specified actions. These scripts will be run on the runner and you can use any functionality of the build environment as you need.

:::tip
Note that you can put the **Custom Script** component anywhere you want in the workflow. This step is used to add different capabilities to the existing workflow.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2793-customScript.png' />

### Input Variables

You can find all the parameters required for this step in the table below, with their descriptions in detail.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2793-customInput.png' />

| Variable Name | Description                                                                                                                                                                                                         | Status   |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `Execute`     | You can run your script as **`Bash`** or **`Ruby`** with two different language environments in the **Execute With** input value.                                                                                   | Required |
| `Script`      | With the **Script** input variable, you can add the script you want to run and run it directly in the selected language. If you leave this input blank, it will proceed to the next step without taking any action. | Optional |

:::caution
Note that the **Script** area works according to the selected language variable. If you want to run a script in any language, make sure that you select the language correctly.
:::

## Custom Script FAQ

### How to change JAVA version

If you want to change the JAVA version for your Android project, you can achieve this by changing the `JAVA_HOME` environment variable.

Appcircle currently has `OpenJDK 11` (default), `OpenJDK 8`, `OpenJDK 17` and `OpenJDK 21`.

[Android Build](/workflows/android-specific-workflow-steps/android-build) step uses `OpenJDK 11` as default JDK version.

You can use the below custom script before your build step to change your `JAVA_HOME` environment variable.

```bash
echo "Default JAVA" $JAVA_HOME

echo "OpenJDK 8" $JAVA_HOME_8_X64
echo "OpenJDK 11" $JAVA_HOME_11_X64
echo "OpenJDK 17" $JAVA_HOME_17_X64
echo "OpenJDK 21" $JAVA_HOME_21_X64

# Change JAVA_HOME to OPENJDK 17
echo "JAVA_HOME=$JAVA_HOME_17_X64" >> $AC_ENV_FILE_PATH
```

Create a custom script like above and put it **above** your [Android Build](/workflows/android-specific-workflow-steps/android-build) step.

<Screenshot url="https://cdn.appcircle.io/docs/assets/workflow-android-change-java-workflow.png" />

<Screenshot url="https://cdn.appcircle.io/docs/assets/workflow-android-change-java-workflow-detail.png" />

:::caution

Please be aware that this custom script affects any step that comes after.

Therefore, you should use this step as a standalone step instead of as part of any custom script.

:::

:::tip

You can find more details about the included Java versions on the [Android Build Infrastructure](/infrastructure/android-build-infrastructure#java-version) page.

:::

:::info

#### Changing System Java Version

Changing the `JAVA_HOME` environment variable will be enough for your Android builds, but it won't change the `java` version in the system.

If you're using a tool in the build pipeline that requires another Java version than the default OpenJDK 11, you should also change the system's default Java version using the below commands in the custom script.

```bash
source "$SDKMAN_DIR/bin/sdkman-init.sh"
sdk default java $(basename $JAVA_HOME_17_X64)
```

After that, you will see the output of `java -version` as below in the build logs.

```txt
openjdk version "17.0.7" 2023-04-18 LTS
OpenJDK Runtime Environment Zulu17.42+19-CA (build 17.0.7+7-LTS)
OpenJDK 64-Bit Server VM Zulu17.42+19-CA (build 17.0.7+7-LTS, mixed mode, sharing)
```

You can also switch to other pre-installed Java versions using the relevant environment variable as an argument in the `sdk` command. For more details about these environment variables, see the [Android Build Infrastructure](/infrastructure/android-build-infrastructure#java-version) page.

:::

### How to install a new package to the build machine?

You can use the compatible package managers to install packages.

For the macOS build machines for iOS builds, \_brew \_is a commonly used package manager with commands like `brew install maven`

For the Linux (Debian) build machines for Android builds, _apt-get_ can be used for 3rd party packages such as `apt-get -y install maven`

### How to change the package name/application ID dynamically?

With custom scripts, you can edit the Info.plist and the build.gradle files.

<Tabs>
  <TabItem value="ios" label="iOS" default>

```bash title="iOS sample for Info.plist"
cd $AC_REPOSITORY_DIR/Your-Target-Folder
/usr/libexec/PlistBuddy -c "Set :CFBundleIdentifier io.myapp" "./Info.plist"
```

  </TabItem>
  <TabItem value="android" label="Android">

```bash title="Android sample for build.gradle"
cd $AC_REPOSITORY_DIR/app
sed -i '' 's/old-value/new-value/g' build.gradle
```

  </TabItem>
</Tabs>

### How to access a file in the repository directory?

For each step in the workflow, you can view the input and output variables in the step configuration.

The repository directory is an output of the Git Clone step and its patch can be accessed with the `AC_REPOSITORY_PATH` environment variable by any step added after the Git Clone step. An example is as follows:

```bash
cd $AC_REPOSITORY_DIR
cat README
```

### How to a add a file as a downloadable build artifact?

You can add any file to the output directory that contain the build artifacts using the `AC_OUTPUT_DIR` environment variable. An example is as follows:

```bash
cd $AC_REPOSITORY_DIR/app/build/reports/
mv lint-results* $AC_OUTPUT_DIR/
```

### How to break pipeline on low test coverage

This document provides a sample custom script written in Ruby that can be integrated into your CI/CD pipeline to enforce a minimum test coverage threshold. The script is designed to break the pipeline if the covered test result falls below a specified percentage.

:::warning
Please note that this custom script must be placed after the [**Test Reports**](https://docs.appcircle.io/continuous-testing/android-testing/running-android-unit-tests#generating-test-report) step in the workflow.
:::

```ruby
require 'json'

def env_has_key(key)
    !ENV[key].nil? && ENV[key] != '' ? ENV[key] : abort("Missing #{key}.")
end

output_dir = env_has_key('AC_OUTPUT_DIR')

def read_json_file(test_result_file_path)
  JSON.parse(File.read(test_result_file_path))
end

def extract_line_coverage(json_data)
  json_data['coverage']['lineCoverage']
end

begin
test_result_file_path = "#{output_dir}/test_results.json"
json_data = read_json_file(test_result_file_path)
line_coverage = extract_line_coverage(json_data)

puts "Current Line Coverage: % #{line_coverage * 100}"

min_coverage = 2.0
puts "Minimum coverage percentage: #{min_coverage}"

if (line_coverage * 100) < min_coverage
    puts "Coverage is #{line_coverage} and below minimum coverage percentage given #{min_coverage}. \nExiting."
    exit (1)
else
    puts "Coverage is above the threshold. It is clear."
end

rescue StandardError => e
  puts "An error occurred: #{e.message}"
end
```

:::info

Please feel free to edit the following variables according to your own requirements:

- `test_result_file_path`: The file path of the test result file from which to retrieve the covered percentage value.
- `min_coverage`: The minimum percentage required for the pipeline to continue without breaking.

:::

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-custom-script-component/
