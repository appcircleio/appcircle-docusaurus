---
title: Setting Up Appcircle Testing Distribution Plugin For Fastlane
sidebar_label: Testing Distribution
description: Enhance powerful action to distribute your builds to appcircle with fastlane
tags:
  [
    testing-distribution,
    ipa distribution,
    apk distribution,
    binary distribution,
    fastlane-marketplace,
  ]
sidebar_position: 1
---

# Setting Up Appcircle Testing Distribution Plugin

The Appcircle Testing Distribution plugin allows users to upload their apps and start distribution to test groups or individuals.

### Discover Action

You can discover more about this action and install it by:
https://rubygems.org/gems/fastlane-plugin-appcircle_testing_distribution

### How to Add the Appcircle Distribute Task Extension to Your Pipeline

To install the Appcircle Testing Distribution action, install the plugin and add the following step to your pipeline at the end:

```bash
fastlane add_plugin appcircle_testing_distribution
```

```yml
  appcircle_testing_distribution(
    accessToken: "$(AC_ACCESS_TOKEN)", # Your Appcircle Personal API Token
    profileID: "$(AC_PROFILE_ID)", # ID of your Appcircle Distribution Profile
    appPath: "$(AC_APP_PATH)", # Path to your iOS .ipa or .xcarchive, or Android APK or App Bundle
    message: "$(AC_MESSAGE)", # Your Message
  )
```

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

:::caution Build Steps Order
You should add this task extension after completing your build steps.
:::

### Leveraging Environment Variables

Utilize environment variables seamlessly by substituting the parameters with `$(VARIABLE_NAME)` in your task inputs. The extension automatically retrieves values from the specified environment variables within your pipeline.

## References

- For details on generating an Appcircle Personal API Token, visit [Generating/Managing Personal API Tokens](/appcircle-api/api-authentication#generatingmanaging-the-personal-api-tokens).

- To create or learn more about Appcircle testing and distribution profiles, please refer to [Creating or Selecting a Distribution Profile](/distribute/create-or-select-a-distribution-profile).
