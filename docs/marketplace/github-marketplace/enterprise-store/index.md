---
title: Setting Up Appcircle Enterprise App Store Action
sidebar_label: Enterprise App Store
description: Enhance powerful action to publish your builds to appcircle app store
tags:
  [
    overview,
    concepts,
    app store,
    internal testing,
    beta testing,
    binary distribution,
    ipa distribution,
    apk distribution,
    github-marketplace,
  ]
sidebar_position: 2
---

The Appcircle Enterprise App Store action allows users to publish their apps to appcircle app store.

### Discover Action

You can discover more about this action and install it by:
https://github.com/marketplace/actions/appcircle-enterprise-store

### How to Add the Appcircle Enterprise App Store Task Extension to Your Pipeline

To install the Appcircle Enterprise App Store action, add the following step to your pipeline at the end:

```yml
- name: Publish App to Appcircle
  id: appcircle-store-publishment
  uses: ./
  with:
    accessToken: ${{ secrets.AC_ACCESS_TOKEN }} # Appcircle Personal API Token
    entProfileId: ${{ secrets.AC_PROFILE_ID }} # Enterprise Profile Id
    appPath: "APP_PATH" # Your App Path
    summary: "SUMMARY" # Your Summary
    releaseNotes: "RELEASE_NOTE" # Your Release Note
    publishType: "1" # 0: None, 1: Beta, 2: Live
```

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

:::caution Build Steps Order
You should add this task extension after completing your build steps.
:::

## Leveraging Environment Variables

Utilize environment variables seamlessly by substituting the parameters with **secrets.NAME** in your task inputs. The action automatically retrieves values from the specified environment variables within your pipeline.

## References

- For details on generating an Appcircle Personal API Token, visit [Generating/Managing Personal API Tokens](/appcircle-api/api-authentication#generatingmanaging-the-personal-api-tokens).

- For more detailed instructions and support, visit the [Appcircle Enterprise App Store documentation](/enterprise-app-store).
