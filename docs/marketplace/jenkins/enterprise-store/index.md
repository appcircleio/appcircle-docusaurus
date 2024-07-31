---
title: Setting Up Appcircle Enterprise Store Plugin For Jenkins
sidebar_label: Enterprise Store
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

# Setting Up Appcircle Enterprise Store Plugin

The Appcircle Enterprise Store plugin enables users to publish their apps to the Appcircle App Store.

### Install Appcircle Enterprise Store Plugin

Go to your Jenkins dashboard and navigate to Manage Jenkins > Manage Plugins. Then, search for "Appcircle Enterprise Store" in the available plugins section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sp-158-installation_steps.png' />

### Add Plugin in Build Steps

Go to your configuration page of the project and add a build step.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sp-158-store-add_pannel.png' />

### Configure Plugin

After adding the plugin to your build steps, ensure that you provide all required inputs.
Additionally, remember to place the plugin after your build steps as you will need to specify the build path later on.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sp-158-store-configure_pannel.png' />

#### How to Retrieve Your Enterprise Store Profile ID

You can obtain your Enterprise Store Profile ID from the URL or by using the @appcircle/cli.

##### How to Extract Your Enterprise Store Profile ID from the URL

1. Navigate to your Enterprise Store Profile.
2. Check the URL, which should be in this format: **/enterprise-store/profiles/PROFILE_ID**. The PROFILE_ID refers to your specific profile ID.

##### Retrieving Profile ID Using @appcircle/cli

The upcoming command retrieves the complete list of Enterprise Store Profiles.

```bash
appcircle enterprise-app-store profile list
```

### Leveraging Environment Variables

Utilize environment variables seamlessly by substituting the parameters with `$(VARIABLE_NAME)` in your task inputs. The extension automatically retrieves values from the specified environment variables within your pipeline.

## References

- For details on generating an Appcircle Personal API Token, visit [Generating/Managing Personal API Tokens](https://docs.appcircle.io/appcircle-api/api-authentication#generatingmanaging-the-personal-api-tokens).

- For more detailed instructions and support, visit the [Appcircle Enterprise App Store documentation](https://appcircle.io/enterprise-app-store).
