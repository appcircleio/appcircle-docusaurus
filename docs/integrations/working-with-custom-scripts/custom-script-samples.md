---
title: Custom Script Samples
metaTitle: Custom Script Samples
metaDescription: Custom Script Samples
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';

# Custom Script Samples

### Changing JAVA version

If you want to change the JAVA version for your Android project, you can achieve this by changing the `JAVA_HOME` environment variable.

Appcircle currently has `OpenJDK 11` (default), `OpenJDK 8`, `OpenJDK 17` and `OpenJDK 21`.

[Android Build](/workflows/android-specific-workflow-steps/build-and-test/android-build) step uses `OpenJDK 11` as default JDK version.

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

Create a custom script like above and put it **above** your [Android Build](/workflows/android-specific-workflow-steps/build-and-test/android-build) step.

<Screenshot url="https://cdn.appcircle.io/docs/assets/workflow-android-change-java-workflow.png" />

<Screenshot url="https://cdn.appcircle.io/docs/assets/workflow-android-change-java-workflow-detail.png" />

:::caution

Please be aware that this custom script affects any step that comes after.

Therefore, you should use this step as a standalone step instead of as part of any custom script.

:::

:::tip

You can find more details about the included Java versions on the [Android Build Infrastructure](../../infrastructure/android-build-infrastructure.md#java-version) page.

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

You can also switch to other pre-installed Java versions using the relevant environment variable as an argument in the `sdk` command. For more details about these environment variables, see the [Android Build Infrastructure](../../infrastructure/android-build-infrastructure.md#java-version) page.

:::

### Pipeline Break on Low Test Coverage

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

### Deploying Apps to Firebase App Distribution

Appcircle Testing Distribution provides an integrated and automated enterprise-grade solution for distributing apps to the testers, but if you want to use other solutions for app distribution, you can do so with custom scripts.

You can use the following script to deploy apps to Firebase App Distribution automatically from the Appcircle Build module.

```bash
#!/usr/bin/env bash
#
# Deploy a binary to Firebase App Distribution
#
curl -sL firebase.tools | bash

firebase appdistribution:distribute $AC_EXPORT_DIR/Runner.ipa --app $FIREBASE_APP_ID --release-notes "Release Notes..." --token $FIREBASE_TOKEN --groups "testers"
```

- `AC_EXPORT_DIR`: The binary path to be deployed can be obtained from the relevant environment variable.
- `FIREBASE_TOKEN`: It must be obtained through a local console.
  - Please follow the instructions [here](https://firebase.google.com/docs/cli#cli-ci-systems) to set up the [**Firebase CLI**](https://firebaseopensource.com/projects/firebase/firebase-tools/) locally, and then you can request a token with the `firebase login:ci` command.
- `FIREBASE_APP_ID`: It can be obtained from the Firebase Dashboard under the **Settings** screen.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (133).png' />

You can also use our [Firebase App Distribution](/workflows/common-workflow-steps#firebase-app-distribution) workflow step for Firebase app deployment.
