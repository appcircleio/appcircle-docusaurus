---
title: Setting Up Appcircle Testing Distribution Action
sidebar_label: Testing Distribution
description: Enhance powerful action to distribute your builds to appcircle
tags:
  [
    testing-distribution,
    ipa distribution,
    apk distribution,
    binary distribution,
    github-marketplace,
  ]
sidebar_position: 1
---

The Appcircle Testing Distribution action allows users to upload their apps and start distribution to test groups or individuals.

### Discover Action

You can discover more about this action and install it by:
https://github.com/marketplace/actions/appcircle-testing-distribution

### How to Add the Appcircle Testing Distribution Task Extension to Your Pipeline

To install the Appcircle Testing Distribution action, add the following step to your pipeline at the end:

```yml
- name: Distribute App to Appcircle
  id: testing-distribution
    uses: appcircleio/appcircle-testing-distribution-githubaction@v0.0.1 # provide the version you want to use
  with:
    accessToken: ${{ secrets.AC_ACCESS_TOKEN }} # Your Appcircle Personal API Token
    profileID: ${{ secrets.AC_PROFILE_ID }} # ID of your Appcircle Distribution Profile
    appPath: ${{ secrets.APP_PATH }} # Path to your iOS .ipa or .xcarchive, or Android APK or App Bundle
    message: ${{ secrets.MESSAGE }} # Your Message
```

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

:::caution Build Steps Order
You should add this task extension after completing your build steps.
:::

## Leveraging Environment Variables

Utilize environment variables seamlessly by substituting the parameters with **secrets.NAME** in your task inputs. The action automatically retrieves values from the specified environment variables within your pipeline.

## References

- For details on generating an Appcircle Personal API Token, visit [Generating/Managing Personal API Tokens](/appcircle-api/api-authentication#generatingmanaging-the-personal-api-tokens)

- To create or learn more about Appcircle testing and distribution profiles, please refer to [Creating or Selecting a Distribution Profile](/testing-distribution/create-or-select-a-distribution-profile)
