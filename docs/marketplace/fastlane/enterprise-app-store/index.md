---
title: Setting Up Appcircle Enterprise App Store Plugin
sidebar_label: Enterprise App Store
description: Enhance powerful action to publish your builds to appcircle app store with fastlane
tags:
  [
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

You can discover more about this action and install it from:
https://rubygems.org/gems/fastlane-plugin-appcircle_enterprise_store

## System Requirements

**Compatible Agents:**

- macOS 14 (arm64)
- RHEL 9 (x86_64)
- Ubuntu 22.04 (x86_64)

**Supported Version:**

- Fastlane 2.222.0
- Ruby 3.2.2

:::caution
Currently, plugins are only compatible to use with Appcircle Cloud. Self-hosted support will be available in future releases.
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
- `appPath`: Indicates the file path to the application package that will be uploaded to Appcircle Testing Distribution Profile.
- `releaseNotes`: Contains the details of changes, updates, and improvements made in the current version of the app being published.
- `summary`: Used to provide a brief overview of the version of the app that is about to be published.
- `publishType`: Specifies the publishing status as either none, beta, or live, and must be assigned the values "0", "1", or "2" accordingly.

### Leveraging Environment Variables

Utilize environment variables seamlessly by substituting the parameters with `$(VARIABLE_NAME)` in your task inputs. The extension automatically retrieves values from the specified environment variables within your pipeline.

:::caution Build Steps Order
Ensure that this action is added after build steps have been completed.

:::

:::caution
If two workflows start simultaneously, the last workflow to reach the publish step will be the up-to-date version on the Enterprise App Store. If these workflows building the same package version, the first publish will be successful, while later deployments with the same version will fail.
:::

## References

- For details on generating an Appcircle Personal API Token, visit [Generating/Managing Personal API Tokens](/appcircle-api-and-cli/api-authentication#generatingmanaging-the-personal-api-tokens).

- For more detailed instructions and support, visit the [Appcircle Enterprise App Store documentation](/enterprise-app-store).
