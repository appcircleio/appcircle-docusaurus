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

## System Requirements

**Compatible Agents:**

- macOS
- Ubuntu
- Ventura

**Supported Version:**

- Fastlane 2.222.0
- Ruby 3.2.2

:::caution
We currently support **Appcircle Cloud**, with **self-hosted** support planned in our roadmap.
:::

### How to Add the Appcircle Distribute Task Extension to Your Pipeline

To install the Appcircle Testing Distribution action, install the plugin and add the following step to your pipeline at the end:

```bash
fastlane add_plugin appcircle_testing_distribution
```

```yml
  appcircle_testing_distribution(
    personalAPIToken: "$(AC_PERSONAL_API_TOKEN)",
    profileName: "$(AC_PROFILE_NAME)",
    createProfileIfNotExists: Boolean,
    appPath: "$(AC_APP_PATH)",
    message: "$(AC_MESSAGE)",
  )
```

- `personalAPIToken`: The Appcircle Personal API token is used to authenticate and secure access to Appcircle services. Add this token to your credentials to enable its use in your pipeline and ensure authorized actions within the platform.
- `profileName`: Specifies the profile that will be used for uploading the app.
- `createProfileIfNotExists`: Ensures that a user profile is automatically created if it does not already exist; if the profile name already exists, the app will be uploaded to that existing profile instead.
- `appPath`: Indicates the file path to the application that will be uploaded to Appcircle Testing Distribution Profile.
- `message`: Your message to testers, ensuring they receive important updates and information regarding the application.

:::caution Build Steps Order
You should add this task extension after completing your build steps.
:::

### Leveraging Environment Variables

Utilize environment variables seamlessly by substituting the parameters with `$(VARIABLE_NAME)` in your task inputs. The extension automatically retrieves values from the specified environment variables within your pipeline.

## References

- For details on generating an Appcircle Personal API Token, visit [Generating/Managing Personal API Tokens](/appcircle-api/api-authentication#generatingmanaging-the-personal-api-tokens).

- To create or learn more about Appcircle testing and distribution profiles, please refer to [Creating or Selecting a Distribution Profile](/testing-distribution/create-or-select-a-distribution-profile).
