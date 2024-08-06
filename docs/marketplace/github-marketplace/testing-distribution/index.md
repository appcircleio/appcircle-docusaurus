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
  ]
sidebar_position: 1
---

The Appcircle Testing Distribution action allows users to upload their apps and start distribution to test groups or individuals.

### Discover Action

You can discover more about this action and install it by:
https://github.com/marketplace/actions/appcircle-testing-distribution

### How to Add the Appcircle Distribute Task Extension to Your Pipeline

To install the Appcircle Testing Distribution action, add the following step to your pipeline at the end:

```yml
- name: Distribute App to Appcircle
  id: testing-distribution
    uses: appcircleio/appcircle-testing-distribution-githubaction@v0.0.1 # provide the version you want to use
  with:
    accessToken: ${{ secrets.AC_ACCESS_TOKEN }} # Your Appcircle Access Token
    profileID: ${{ secrets.AC_PROFILE_ID }} # ID of your Appcircle Distribution Profile
    appPath: ${{ secrets.APP_PATH }} # Path to your iOS .ipa or .xcarchive, or Android APK or App Bundle
    message: ${{ secrets.MESSAGE }} # Your Message
```

:::caution Build Steps Order
You should add this task extension after completing your build steps.
:::

## Leveraging Environment Variables

Utilize environment variables seamlessly by substituting the parameters with **secrets.NAME** in your task inputs. The action automatically retrieves values from the specified environment variables within your pipeline.

## References

- For details on generating an Appcircle Personal Access Token, visit [Generating/Managing Personal API Tokens](/appcircle-api/api-authentication#generatingmanaging-the-personal-api-tokens)

- To create or learn more about Appcircle testing and distribution profiles, please refer to [Creating or Selecting a Distribution Profile](/testing-distribution/create-or-select-a-distribution-profile)
