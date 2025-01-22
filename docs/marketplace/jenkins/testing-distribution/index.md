---
title: Setting Up Appcircle Testing Distribution Plugin
sidebar_label: Testing Distribution
description: Enhance powerful plugin to distribute your builds to appcircle
tags:
  [
    testing distribution,
    ipa distribution,
    apk distribution,
    binary distribution,
    jenkins plugin,
  ]
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';

# Setting Up Appcircle Testing Distribution Plugin

The Appcircle Testing Distribution plugin allows users to upload their apps and start distribution to test groups or individuals.

### Discover Plugin

You can discover more about this action and install it from:
https://plugins.jenkins.io/appcircle-testing-distribution/

## System Requirements

**Compatible Agents:**

- macOS 14 (arm64)
<!-- - Ubuntu 22.04 (x86_64) -->

**Supported Version:**

- Jenkins 2.440.3

:::caution
Currently, plugins are only compatible to use with **Appcircle Cloud**. **Self-hosted** support will be available in future releases.
:::

## Install the Appcircle Testing Distribution Plugin

Go to your Jenkins dashboard and navigate to Manage Jenkins > Manage Plugins. Then, search for "Appcircle Testing Distribution" in the available plugins section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sp-158-installation_steps.png' />

## Plugin Usage

There are two primary ways to use this Jenkins plugin: from the user interface in freestyle projects and from a script in pipeline projects.

### Using the Plugin in Freestyle Projects

#### Adding the Plugin to Build Steps

Go to your configuration page of the project add a build step.

<Screenshot url='https://cdn.appcircle.io/docs/assets/SP-175_jenkins_build_step.png' />

#### Configuring the Plugin

After adding the plugin to your build steps, ensure that you provide all required inputs.
Additionally, remember to place the plugin after your build steps as you will need to specify the build path later on.

:::info
For the "App Path" field, full path to the package should be provided. For example: `<your-jenkins-home>/workspace/<project-name>/build/MyProject.ipa`.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/SP-205_td_usage.png' />

### Using the Plugin in Pipeline Projects

#### Adding the Plugin to a Pipeline Script

```Groovy
stage('Publish') {
    environment {
        AC_PAT = credentials('AC_PAT')
    }
    script {
        def pathToApp = "${env.WORKSPACE}/build/outputs/apk/release/app-release.apk"

        appcircleTestingDistribution (
            personalAPIToken: AC_PAT,
            profileName: 'MyProfile',
            createProfileIfNotExists: false,
            appPath: pathToApp,
            message: 'New version 1.2.3'
        )
    }
}
```

- `personalAPIToken`: The Appcircle Personal API token is used to authenticate and secure access to Appcircle services. Add this token to your credentials to enable its use in your pipeline and ensure authorized actions within the platform.
- `profileName`: Specifies the profile that will be used for uploading the app.
- `createProfileIfNotExists`: Ensures that a user profile is automatically created if it does not already exist; if the profile name already exists, the app will be uploaded to that existing profile instead.
- `appPath`: Indicates the file path to the application package that will be uploaded to Appcircle Testing Distribution Profile. You can define the path using `def` as shown in the example script above, or pass it using `withEnv`. For instance:
    ```
    steps {
        withEnv(["APP_PATH=${env.WORKSPACE}/build/MyProject.ipa"]) {    
            appcircleTestingDistribution (
                ...
                appPath: env.APP_PATH,
    ```
- `message`: Your message to testers, ensuring they receive important updates and information regarding the application.

:::caution Build Steps Order
Ensure that this action is added after build steps have been completed.

:::

:::caution
If multiple workflows start simultaneously, the order in which versions are shared in the Testing Distribution is determined by the execution order of the publish step. The version that completes its build and triggers the publish plugin first will be shared first, followed by the others in sequence.
:::

## References

- For details on generating an Appcircle Personal API Token, visit [Generating/Managing Personal API Tokens](/appcircle-api-and-cli/api-authentication#generatingmanaging-the-personal-api-tokens).

- For more detailed instructions and support, visit the [Testing Distribution documentation](/testing-distribution).
