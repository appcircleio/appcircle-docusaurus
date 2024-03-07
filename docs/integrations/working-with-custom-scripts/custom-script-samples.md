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

Appcircle currently has OpenJDK 11 (default), OpenJDK 8, OpenJDK 17 and OpenJDK 21.

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

Create a custom script like above and put it **above** your Android build step.

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

### Deploying Apps to Firebase App Distribution

Appcircle Testing Distribution provides an integrated and automated enterprise-grade solution for distributing apps to the testers, but if you want to use other solutions for app distribution, you can do so with custom scripts. You can use the following script below to deploy apps to Firebase App Distribution automatically from the Appcircle Build module.

- The binary to be deployed can be obtained with the related environment variable. `AC_EXPORT_DIR` and the binary path.
- `FIREBASE_TOKEN` must be obtained through a local console. Please follow the [instructions here](https://firebase.google.com/docs/cli#cli-ci-systems) to set up the Firebase CLI locally and then you can request a token with the `firebase login:ci `command.
- `FIREBASE_APP_ID` can be obtained from the Firebase Dashboard under the settings screen:

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (133).png' />

The sample script is as follows:

```bash
#!/usr/bin/env bash
#
# Deploy a binary to Firebase App Distribution
#
curl -sL firebase.tools | bash

firebase appdistribution:distribute $AC_EXPORT_DIR/Runner.ipa --app $FIREBASE_APP_ID --release-notes "Release Notes..." --token $FIREBASE_TOKEN --groups "testers"
```

You may also use our Firebase App Distribution Component for this process.

https://github.com/appcircleio/appcircle-firebase-distribution-component

### Send email notification when a build is complete

You can send notification emails when your build is complete so that you or your teammates will know the build status.

Here's a sample Bash script to send emails from a custom script step:

```bash
#!/usr/bin/env bash
#
# Send an email when a build is completed in Appcircle.
#

# Email address for the receipent
RCP_ADDRESS="receipent@example.com"
CC_ADDRESS="cc_receipent@example.com"

# Subject line for email
EMAIL_SUBJECT="Appcircle Build"

# Send a corresponding email for successful builds.

echo "Build completed successfully, sending email notification."
echo -e "Your build in Appcircle is completed successfully." | mail -s "Build completed with success." ${RCP_ADDRESS} -c ${CC_ADDRESS}
echo "Email notification sent."
```

###

### Send Slack notification when a build is complete

Appcircle supports a wide range of options for sending notifications to Slack, but you can also send any custom messages to Slack with custom scripts.

If you have a Slack webhook created, you can send a message to your Slack channel with a single line of Bash script.

You can refer to Slack's webhook documentation here: :link: [**Creating Slack webhooks**](https://api.slack.com/tutorials/slack-apps-hello-world)


```bash
#!/usr/bin/env bash
#
# Send a Slack notification when a build is completed in Appcircle.
#

curl -X POST -H 'Content-type: application/json' --data '{"text":"Appcircle build is completed successfully!"}' SLACK_WEBHOOK_URL
```
