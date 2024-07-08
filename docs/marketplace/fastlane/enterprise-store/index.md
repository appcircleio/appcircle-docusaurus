---
title: Setting Up Appcircle Enterprise Store Plugin
sidebar_label: Enterprise App Store
description: Enhance powerful action to publish your builds to appcircle app store with fastlane
tags:
  [
    testing-distribution,
    overview,
    concepts,
    app store,
    internal testing,
    beta testing,
    binary distribution,
    ipa distribution,
    apk distribution,
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

:::caution Build Steps Order
You should add this task extension after completing your build steps.
:::

### Leveraging Environment Variables

Utilize environment variables seamlessly by substituting the parameters with `$(VARIABLE_NAME)` in your task inputs. The extension automatically retrieves values from the specified environment variables within your pipeline.

## References

- For details on generating an Appcircle Personal Access Token, visit [Generating/Managing Personal API Tokens](/appcircle-api/api-authentication#generatingmanaging-the-personal-api-tokens).

- To create or learn more about Appcircle testing and distribution profiles, please refer to [Creating or Selecting a Distribution Profile](/distribute/create-or-select-a-distribution-profile).
