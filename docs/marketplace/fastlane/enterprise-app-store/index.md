---
title: Setting Up Appcircle Enterprise App Store Plugin
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

The Appcircle Enterprise App Store plugin allows users to publish their apps and start distribution to test groups or individuals.

### Discover Action

You can discover more about this action and install it by:
https://rubygems.org/gems/fastlane-plugin-appcircle_enterprise_store

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

### Getting Started

This project is a [_fastlane_](https://github.com/fastlane/fastlane) plugin. To get started with `appcircle_enterprise_app_store`, add it to your project by running:

```bash
fastlane add_plugin appcircle_enterprise_app_store
```

After adding the plugin to your project, configure your Fastfile as follows:

```yml
  lane :distribute_app_store do
    appcircle_enterprise_app_store(
      personalAPIToken: "$(AC_PERSONAL_API_TOKEN)",
      appPath: "$(APP_PATH)",
      summary: "$(SUMMARY)",
      releaseNotes: "$(RELEASE_NOTE)",
      publishType: "$(PUBLISH_TYPE)" # Assign the appropriate number based on the status: None (0), Beta (1), Live (2)
    )
  end
```

- `personalAPIToken`: The Appcircle Personal API token is utilized to authenticate and secure access to Appcircle services, ensuring that only authorized users can perform actions within the platform.
- `appPath`: Indicates the file path to the application that will be uploaded to Appcircle Testing Distribution Profile.
- `releaseNote`: Contains the details of changes, updates, and improvements made in the current version of the app being published.
- `Summary`: Used to provide a brief overview of the version of the app that is about to be published.
- `publishType`: Specifies the publishing status as either none, beta, or live, and must be assigned the values "0", "1", or "2" accordingly.

:::caution
If two builds start simultaneously, such as **v1.0.5(5)** and **v1.0.5(5)**, for the same **publishType**, the build that finishes last will result in failure because the same version cannot be added, while the first build to complete will be successfully uploaded and published
:::

:::caution Build Steps Order
You should add this task extension after completing your build steps.
:::

### Leveraging Environment Variables

Utilize environment variables seamlessly by substituting the parameters with `$(VARIABLE_NAME)` in your task inputs. The extension automatically retrieves values from the specified environment variables within your pipeline.

## References

- For details on generating an Appcircle Personal API Token, visit [Generating/Managing Personal API Tokens](/appcircle-api/api-authentication#generatingmanaging-the-personal-api-tokens).

- For more detailed instructions and support, visit the [Appcircle Enterprise App Store documentation](/enterprise-app-store).
