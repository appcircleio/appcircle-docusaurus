---
title: Setting Up Appcircle Testing Distribution Action
sidebar_label: Testing Distribution
description: Enhance powerful action to distribute your builds to appcircle
tags:
  [
    testing distribution,
    ipa distribution,
    apk distribution,
    binary distribution,
    github marketplace,
  ]
sidebar_position: 1
---

The Appcircle Testing Distribution action allows users to upload their apps and start distribution to test groups or individuals.

### Discover Action

You can discover more about this action and install it from:
https://github.com/marketplace/actions/appcircle-testing-distribution

## System Requirements

**Compatible Agents:**

- macOS 14 (arm64)
- Ubuntu 22.04 (x86_64)

:::caution
Currently, plugins are only compatible to use with **Appcircle Cloud**. **Self-hosted** support will be available in future releases.
:::

### How to Add the Appcircle Testing Distribution Action to Your Pipeline

To install the Appcircle Testing Distribution action, add the following step to your pipeline at the end:

```yaml
- name: Publish App to Appcircle
  id: testing-distribution-appcircle
  uses: appcircleio/appcircle-testing-distribution-githubaction
  with:
    personalAPIToken: ${{ secrets.AC_PROFLE_API_TOKEN }}
    profileName: ${{ secrets.AC_PROFILE_NAME }}
    createProfileIfNotExists: ${{ secrets.CREATE_PROFILE_IF_NOT_EXISTS }}
    appPath: ${{ secrets.APP_PATH }}
    message: ${{ secrets.MESSAGE }}
```

- `personalAPIToken`: The Appcircle Personal API token is used to authenticate and secure access to Appcircle services. Add this token to your credentials to enable its use in your pipeline and ensure authorized actions within the platform.
- `profileName`: Specifies the profile that will be used for uploading the app.
- `createProfileIfNotExists`: Ensures that a user profile is automatically created if it does not already exist; if the profile name already exists, the app will be uploaded to that existing profile instead.
- `appPath`: Indicates the file path to the application package that will be uploaded to Appcircle Testing Distribution Profile.
- `message`: Your message to testers, ensuring they receive important updates and information regarding the application.

## Leveraging Environment Variables

Utilize environment variables seamlessly by substituting the parameters with **secrets.NAME** in your task inputs. The action automatically retrieves values from the specified environment variables within your pipeline.

:::caution Build Steps Order
Ensure that this action is added after build steps have been completed.
:::

:::caution
If multiple workflows start simultaneously, the order in which versions are shared in the Testing Distribution is determined by the execution order of the publish step. The version that completes its build and triggers the publish plugin first will be shared first, followed by the others in sequence.
:::

## References

- For details on generating an Appcircle Personal API Token, visit [Generating/Managing Personal API Tokens](/appcircle-api-and-cli/api-authentication#generatingmanaging-the-personal-api-tokens)

- To create or learn more about Appcircle testing and distribution profiles, please refer to [Creating or Selecting a Distribution Profile](/testing-distribution/create-or-select-a-distribution-profile)
