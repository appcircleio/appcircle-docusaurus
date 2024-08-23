---
title: Setting Up Appcircle Enterprise App Store Plugin For Jenkins
sidebar_label: Enterprise App Store
description: Enhance powerful plugin to publish your builds to appcircle app store
tags:
  [
    overview,
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

- macOS
- Ubuntu
- Ventura

**Supported Version:**

- Jenkins 2.440.3

Note: We currently support **Appcircle Cloud**, with **self-hosted** support planned in our roadmap.

### Install Appcircle Enterprise App Store Plugin

Go to your Jenkins dashboard and navigate to Manage Jenkins > Manage Plugins. Then, search for "Appcircle Enterprise App Store" in the available plugins section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sp-158-installation_steps.png' />

### Add Plugin in Build Steps

Go to your configuration page of the project and add a build step.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sp-158-store-add_pannel.png' />

### Configure Plugin

After adding the plugin to your build steps, ensure that you provide all required inputs.
Additionally, remember to place the plugin after your build steps as you will need to specify the build path later on.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sp-158-store-configure_pannel.png' />

#### How to Retrieve Your Enterprise App Store Profile ID

You can obtain your Enterprise App Store Profile ID from the profile settings or by using the @appcircle/cli.

##### Retrieving Profile ID from Enterprise App Store Profile Settings

1. Navigate to your Enterprise App Store Profile.
2. Click to Settings button
3. Copy the Profile ID
   <Screenshot url='https://cdn.appcircle.io/docs/assets/EAS-ProfileID-Copy.png' />

##### Retrieving Profile ID Using @appcircle/cli

The upcoming command retrieves the complete list of Enterprise App Store Profiles.

```bash
appcircle enterprise-app-store profile list
```

### Using Plugin into Your Script

```Groovy
   stage('Publish') {
      environment {
         AC_PAT = credentials('AC_PAT')
      }
       steps {
          appcircleEnterpriseAppStore personalAPIToken: AC_PAT,
                  appPath: '$APP_PATH',
                  releaseNote: '$RELEASE_NOTE',
                  summary: '$SUMMARY',
                  publishType: '$PUBLISH_TYPE' // "0": None, "1": Beta, "2": Live
       }
   }
```

- `personalAPIToken`: The Appcircle Personal API token is utilized to authenticate and secure access to Appcircle services, ensuring that only authorized users can perform actions within the platform.
- `appPath`: Indicates the file path to the application that will be uploaded to Appcircle Testing Distribution Profile.
- `releaseNote`: Contains the details of changes, updates, and improvements made in the current version of the app being published.
- `Summary`: Used to provide a brief overview of the version of the app that is about to be published.
- `publishType`: Specifies the publishing status as either none, beta, or live, and must be assigned the values "0", "1", or "2" accordingly.

:::caution
If two builds start simultaneously, such as **v1.0.5(5)** and **v1.0.5(5)**, for the same **publishType**, the build that finishes last will result in failure because the same version cannot be added, while the first build to complete will be successfully uploaded and published
:::

## References

- For details on generating an Appcircle Personal API Token, visit [Generating/Managing Personal API Tokens](https://docs.appcircle.io/appcircle-api/api-authentication#generatingmanaging-the-personal-api-tokens).

- For more detailed instructions and support, visit the [Appcircle Enterprise App Store documentation](/enterprise-app-store).
