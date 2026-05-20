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
import PersonalApiTokenRef from '@site/docs/\_personal-api-token-reference.mdx';

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

```ruby
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

**Parameter Details:**

- `personalAPIToken` (required): The Appcircle Personal API token is utilized to authenticate and secure access to Appcircle services, ensuring that only authorized users can perform actions within the platform. This token must be generated from your Appcircle account with appropriate permissions.

- `appPath` (required): Indicates the file path to the application package that will be uploaded to Appcircle Enterprise App Store. The path can be specified in two ways:

  **When Build and Enterprise App Store tasks are in the same pipeline:**
  Assuming you are using Enterprise App Store action after a build step, you can use the output directory of the build step. For example:
  - iOS: `"./output/app.ipa"` or `"$(pwd)/output/app.ipa"`
  - Android: `"./app/build/outputs/apk/release/app-release.apk"` or `"$(pwd)/app/build/outputs/apk/release/app-release.apk"`

  **When Enterprise App Store task is a separate pipeline:**
  Assuming you have published a build artifact in your build pipeline, you can get the artifact and use it in the distribution pipeline. For example:
  - `"./artifacts/app.ipa"`
  - `"./artifacts/app.apk"`

  Make sure the path points to a valid application package file (`.ipa` for iOS, `.apk` for Android).

- `summary` (required, string): Used to provide a brief overview of the version of the app that is about to be published. This should be a concise description of what's new in this version (e.g., "Bug fixes and performance improvements", "New user interface design", "Added payment integration").

- `releaseNotes` (required, string): Contains the details of changes, updates, and improvements made in the current version of the app being published. This can include detailed information about new features, bug fixes, and any breaking changes (e.g., "• Fixed login authentication issue\n• Added dark mode support\n• Improved app performance\n• Updated UI components").

- `publishType` (required, string): Specifies the publishing status for the app in the Enterprise App Store. Must be assigned one of the following values:
  - `"0"`: None - App is uploaded but not published (draft status)
  - `"1"`: Beta - App is published for beta testing
  - `"2"`: Live - App is published and available to all users

### Leveraging Environment Variables

Utilize environment variables seamlessly by substituting the parameters with `$(VARIABLE_NAME)` in your task inputs. The extension automatically retrieves values from the specified environment variables within your pipeline.

:::caution Build Steps Order
Ensure that this action is added after build steps have been completed.

:::

:::caution
If two workflows start simultaneously, the last workflow to reach the publish step will be the up-to-date version on the Enterprise App Store. If these workflows building the same package version, the first publish will be successful, while later deployments with the same version will fail.
:::

## References

<PersonalApiTokenRef />

- For more detailed instructions and support, visit the [Appcircle Enterprise App Store documentation](/enterprise-app-store).
