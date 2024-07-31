---
title: Setting Up Appcircle Enterprise Store Plugin
sidebar_label: Enterprise App Store
description: Enhance powerful action to publish your builds to appcircle app store with fastlane
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
    fastlane-marketplace,
  ]
sidebar_position: 2
---

The Appcircle Enterprise Store plugin allows users to publish their apps and start distribution to test groups or individuals.

### Discover Action

You can discover more about this action and install it by:
https://rubygems.org/gems/fastlane-plugin-appcircle_enterprise_store

### Getting Started

To get started with `appcircle_enterprise_store`, add it to your project by running:

```bash
fastlane add_plugin appcircle_enterprise_store
```

After adding the plugin to your project, configure your Fastfile as follows:

```yml
  lane :distribute_app_store do
    appcircle_enterprise_store(
      accessToken: "$(AC_ACCESS_TOKEN)",
      entProfileId: "$(ENTERPRISE_PROFILE_ID)",
      appPath: "$(APP_PATH)",
      summary: "$(SUMMARY)",
      releaseNotes: "$(RELEASE_NOTE)",
      publishType: "$(PUBLISH_TYPE)" # Assign the appropriate number based on the status: None (0), Beta (1), Live (2)
    )
  end
```

#### How to Retrieve Your Enterprise Store Profile ID

You can obtain your Enterprise Store Profile ID from the URL or by using the @appcircle/cli.

**How to Extract Your Enterprise Store Profile ID from the URL**

1. Navigate to your Enterprise Store Profile.
2. Check the URL, which should be in this format: /enterprise-store/profiles/PROFILE_ID. The PROFILE_ID refers to your specific profile ID.

**Retrieving Profile ID Using @appcircle/cli**

The upcoming command retrieves the complete list of Enterprise Store Profiles.

```bash
appcircle enterprise-app-store profile list
```

:::caution Build Steps Order
You should add this task extension after completing your build steps.
:::

### Leveraging Environment Variables

Utilize environment variables seamlessly by substituting the parameters with `$(VARIABLE_NAME)` in your task inputs. The extension automatically retrieves values from the specified environment variables within your pipeline.

## References

- For details on generating an Appcircle Personal Access Token, visit [Generating/Managing Personal API Tokens](/appcircle-api/api-authentication#generatingmanaging-the-personal-api-tokens).

- For more detailed instructions and support, visit the [Appcircle Enterprise App Store documentation](https://appcircle.io/enterprise-app-store).
