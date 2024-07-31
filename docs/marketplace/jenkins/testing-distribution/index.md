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

You can obtain your testing distribution profile from the URL or by using the @appcircle/cli.

##### How to Extract Your Profile ID from the URL

1. Navigate to your Testing Distribution profile.
2. Check the URL, which should be in this format: **distribute/detail/PROFILE_ID**. The **PROFILE_ID** refers to your specific profile ID.

##### Retrieving Profile ID Using @appcircle/cli

The upcoming command retrieves the complete list of Testing Distribution Profiles.

```bash
appcircle testing-distribution profile list
```

### Leveraging Environment Variables

Utilize environment variables seamlessly by substituting the parameters with `$(VARIABLE_NAME)` in your task inputs. The extension automatically retrieves values from the specified environment variables within your pipeline.

### Adding the Plugin to Your Pipeline

```Groovy
   stage('Publish') {
      environment {
         AC_PAT = credentials('AC_PAT')
      }
       steps {
          withCredentials([string(credentialsId: 'CREDENTIAL_ID', variable: 'VARIABLE_NAME')]) {
             appcircleTestingDistribution accessToken: hudson.util.Secret.fromString('VARIABLE_NAME'),
                     profileID: 'PROFILE_ID',
                     appPath: 'APP_PATH',
                     message: 'MESSAGE'
          }
       }
   }
```

## References

- For details on generating an Appcircle Personal API Token, visit [Generating/Managing Personal API Tokens](/appcircle-api/api-authentication#generatingmanaging-the-personal-api-tokens).

For more detailed instructions and support, visit the [Testing Distribution documentation](/distribute).
