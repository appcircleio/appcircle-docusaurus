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

### Leveraging Environment Variables

Utilize environment variables seamlessly by substituting the parameters with `$(VARIABLE_NAME)` in your task inputs. The extension automatically retrieves values from the specified environment variables within your pipeline.

## References

- For details on generating an Appcircle Personal API Token, visit [Generating/Managing Personal API Tokens](https://docs.appcircle.io/appcircle-api/api-authentication#generatingmanaging-the-personal-api-tokens).

- For more detailed instructions and support, visit the [Appcircle Enterprise App Store documentation](/enterprise-app-store).
