---
title: Setting Up Appcircle Enterprise App Store Plugin For Jenkins
sidebar_label: Enterprise App Store
description: Enhance powerful plugin to publish your builds to appcircle app store
tags:
  [
    concepts,
    app store,
    internal-testing,
    beta testing,
    binary distribution,
    ipa distribution,
    apk distribution,
  ]
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';

# Setting Up Appcircle Enterprise App Store Plugin

The Appcircle Enterprise App Store plugin enables users to publish their apps to the Appcircle App Store.

## System Requirements

**Compatible Agents:**

- macOS 14.2, 14.5

**Supported Version:**

- Jenkins 2.440.3

:::caution
Currently, plugins are only compatible to use with **Appcircle Cloud**. **Self-hosted** support will be available in future releases.
:::

### Install Appcircle Enterprise App Store Plugin

Go to your Jenkins dashboard and navigate to Manage Jenkins > Manage Plugins. Then, search for "Appcircle Enterprise App Store" in the available plugins section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sp-158-installation_steps.png' />

### Add Plugin in Build Steps

Go to your configuration page of the project and add a build step.

<Screenshot url='https://cdn.appcircle.io/docs/assets/SP-205_ent_add.png' />

### Configure Plugin

After adding the plugin to your build steps, ensure that you provide all required inputs.
Additionally, remember to place the plugin after your build steps as you will need to specify the build path later on.

<Screenshot url='https://cdn.appcircle.io/docs/assets/SP-205_ent_usage.png' />

### Using Plugin into Your Script

```Groovy
   stage('Publish') {
      environment {
         AC_PAT = credentials('AC_PAT')
      }
       steps {
          appcircleEnterpriseAppStore personalAPIToken: AC_PAT,
                  appPath: '$APP_PATH',
                  releaseNotes: '$RELEASE_NOTE',
                  summary: '$SUMMARY',
                  publishType: '$PUBLISH_TYPE' // "0": None, "1": Beta, "2": Live
       }
   }
```

- `personalAPIToken`: The Appcircle Personal API token is utilized to authenticate and secure access to Appcircle services, ensuring that only authorized users can perform actions within the platform.
- `appPath`: Indicates the file path to the application package that will be uploaded to Appcircle Testing Distribution Profile.
- `releaseNotes`: Contains the details of changes, updates, and improvements made in the current version of the app being published.
- `summary`: Used to provide a brief overview of the version of the app that is about to be published.
- `publishType`: Specifies the publishing status as either none, beta, or live, and must be assigned the values "0", "1", or "2" accordingly.

:::caution Build Steps Order
Ensure that this action is added after build steps have been completed.

:::

:::caution
If two workflows start simultaneously, the last workflow to reach the publish step will be the up-to-date version on the Enterprise App Store. If these workflows building the same package version, the first publish will be successful, while later deployments with the same version will fail.
:::

## References

- For details on generating an Appcircle Personal API Token, visit [Generating/Managing Personal API Tokens](/appcircle-api/api-authentication#generatingmanaging-the-personal-api-tokens).

- For more detailed instructions and support, visit the [Appcircle Enterprise App Store documentation](/enterprise-app-store).
