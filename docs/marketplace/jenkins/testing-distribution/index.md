---
title: Setting Up Appcircle Testing Distribution Plugin
sidebar_label: Testing Distribution
description: Enhance powerful plugin to distribute your builds to appcircle
tags:
  [
    testing-distribution,
    ipa distribution,
    apk distribution,
    binary distribution,
    jenkins-plugin,
  ]
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';

The Appcircle Testing Distribution plugin allows users to upload their apps and start distribution to test groups or individuals.

## System Requirements

**Compatible Agents:**

- macOS
- Ubuntu
- Ventura

**Supported Version:**

- Jenkins 2.440.3

:::caution
We currently support **Appcircle Cloud**, with **self-hosted** support planned in our roadmap.
:::

### Install Appcircle Testing Distribution Plugin

Go to your Jenkins dashboard and navigate to Manage Jenkins > Manage Plugins. Then, search for "Appcircle Testing Distribution" in the available plugins section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sp-158-installation_steps.png' />

### Add Plugin in Build Steps

Go to your configuration page of the project add a build step.

<Screenshot url='https://cdn.appcircle.io/docs/assets/SP-175_jenkins_build_step.png' />

### Configure Plugin

After adding the plugin to your build steps, ensure that you provide all required inputs.
Additionally, remember to place the plugin after your build steps as you will need to specify the build path later on.

<Screenshot url='https://cdn.appcircle.io/docs/assets/SP-175_jenkins_plugin_usage.png' />

#### How to Retrieve Your Testing Distribution Profile ID

You can obtain your Testing Distribution Profile ID from the profile settings or by using the @appcircle/cli.

##### Retrieving Profile ID from Testing Distribution Profile Settings

1. Navigate to your Testing Distribution profile.
2. Click to Settings button
3. Copy the Profile ID
   <Screenshot url='https://cdn.appcircle.io/docs/assets/TD-ProfileID-Copy.png' />

##### Retrieving Profile ID Using @appcircle/cli

The upcoming command retrieves the complete list of Testing Distribution Profiles.

```bash
appcircle testing-distribution profile list
```

### Adding the Plugin to Your Pipeline

```Groovy
   stage('Publish') {
      environment {
         AC_PAT = credentials('AC_PAT')
      }
       steps {
          appcircleTestingDistribution personalAPIToken: AC_PAT,
                  profileName: 'PROFILE_NAME',
                  createProfileIfNotExists: false,
                  appPath: 'APP_PATH',
                  message: 'MESSAGE'
       }
   }
```

- `personalAPIToken`: The Appcircle Personal API token is used to authenticate and secure access to Appcircle services. Add this token to your credentials to enable its use in your pipeline and ensure authorized actions within the platform.
- `profileName`: Specifies the profile that will be used for uploading the app.
- `createProfileIfNotExists`: Ensures that a user profile is automatically created if it does not already exist; if the profile name already exists, the app will be uploaded to that existing profile instead.
- `appPath`: Indicates the file path to the application that will be uploaded to Appcircle Testing Distribution Profile.
- `message`: Your message to testers, ensuring they receive important updates and information regarding the application.

## References

- For details on generating an Appcircle Personal API Token, visit [Generating/Managing Personal API Tokens](/appcircle-api/api-authentication#generatingmanaging-the-personal-api-tokens).

- For more detailed instructions and support, visit the [Testing Distribution documentation](/testing-distribution).
