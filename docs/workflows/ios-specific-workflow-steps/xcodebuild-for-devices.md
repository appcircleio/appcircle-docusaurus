---
title: Xcodebuild for Devices (Archive & Export)
description: Learn to build iOS apps for ARM devices with Xcodebuild. Essential for Sharing With Testers feature and iOS distribution
tags: [xcode, ios, build, archive, export, workflow, step]
---

import Screenshot from '@site/src/components/Screenshot';

# Xcodebuild for Devices (Archive & Export)

This step builds your application for iOS devices in ARM architecture, which is required for the [**Sharing With Testers**](/distribute/create-or-select-a-distribution-profile) feature or any other means of iOS distribution.

:::info
This step is the archive and export step. When the step is completed, the `.ipa` file of the application is generated.
:::

### Prerequisites

The workflow steps that need to be executed before running this step, along with their respective reasons, are listed in the table below.

| Require Workflow Step                                                                                      | Description                                                                                                                                                                         |
| ---------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [**Git Clone**](https://docs.appcircle.io/workflows/common-workflow-steps/#git-clone)                      | The repository that needs to be built must be fetched from the Git provider. **Xcodebuild for Devices** should be used after this step.                                             |
| [**Cocoapods Install**](https://docs.appcircle.io/workflows/ios-specific-workflow-steps#cocoapods-install) | This step installs all pod dependencies for project. **Xcodebuild for Devices** should be used after this step. If you use SPM (Swift Package Manager), it is not necessary to use. |
| [**Xcode Select**](https://docs.appcircle.io/workflows/ios-specific-workflow-steps#xcode-select-version)   | In this step, select the Xcode version to build. **Xcodebuild for Devices** should be used after this step.                                                                         |

:::danger
This step should always follow steps that may affect Archive and Export, such as Xcode Select and Cocoapods Install.
<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2880-buildOrder.png' />
:::

### Input Variables

You can find all the parameters required for this step in the table below, with their descriptions in detail.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2880-buildInput.png' />

| Variable Name                                 | Description                                                                                                                                                                                                                                              | Status   |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `$AC_REPOSITORY_DIR`                          | Specifies the cloned repository directory. This path will be generated after the [Git Clone](https://docs.appcircle.io/workflows/common-workflow-steps#git-clone) step.                                                                                  | Required |
| `$AC_OUTPUT_DIR_PATH`                         | This variable specifies the path of the artifacts that will be generated after the build is complete.                                                                                                                                                    | Required |
| `$AC_SCHEME`                                  | Specifies the project scheme for build. If you filled in **`Configuration => Build Scheme`**, this variable comes from [Configuration](https://docs.appcircle.io/build/building-ios-applications#build-configuration).                                   | Required |
| `$AC_ARCHIVE_FLAGS`                           | Specifies the extra xcodebuild flag. For example: -quiet                                                                                                                                                                                                 |          |
| `$AC_PROJECT_PATH`                            | Specifies the project path. For example: `./appcircle.xcodeproj`. If you filled in **`Configuration => Project or Workspace`**, this variable comes from [Configuration](https://docs.appcircle.io/build/building-ios-applications#build-configuration). | Required |
| `$AC_CERTIFICATES`                            | This variable specifies the path of the certificates to be signed.                                                                                                                                                                                       | Required |
| `$AC_BUNDLE_IDENTIFIERS`                      | This variable holds the Bundle Identifier of the application to be built.                                                                                                                                                                                | Required |
| `$AC_PROVISIONING_PROFILES`                   | This variable specifies the path of provisioning profiles to be signed.                                                                                                                                                                                  | Required |
| `$AC_CONFIGURATION_NAME`                      | You can build your project with any configuration you want. Specify the configuration as hard coded. Appcircle will add automatically this configuration to the xcodebuild command. For example; **`Debug`**                                             | Optional |
| `$AC_COMPILER_INDEX_STORE_ENABLE`             | You can disable indexing during the build for faster build. Default value is `No`.                                                                                                                                                                       | Optional |
| `$AC_METHOD_FOR_EXPORT`                       | Describes how Xcode should export the archive. Available options are `auto-detect`, `app-store`, `ad-hoc`, `enterprise`, `development`. The default is `auto-detect`.                                                                                    | Optional |
| `$AC_TEAMID_FOR_EXPORT`                       | The Developer Portal team to be use for this export. Defaults to the team used to build the archive.                                                                                                                                                     | Optional |
| `$AC_COMPILE_BITCODE_FOR_EXPORT`              | For non-App Store exports, should Xcode re-compile the app from bitcode? Available options `YES`, `NO`.                                                                                                                                                  | Optional |
| `$AC_UPLOAD_BITCODE_FOR_EXPORT`               | For App Store exports, should the package include a bitcode? Available options `YES`, `NO`.                                                                                                                                                              | Optional |
| `$AC_UPLOAD_SYMBOLS_FOR_EXPORT`               | For App Store exports, should the package include symbols? Available options `YES`, `NO`.                                                                                                                                                                | Optional |
| `$AC_ICLOUD_CONTAINER_ENVIRONMENT_FOR_EXPORT` | For non-App Store exports, if the app is using CloudKit, this configures the "com.apple.developer.icloud-container-environment" entitlement. Available options `Development` and `Production`.                                                           | Optional |
| `$AC_DELETE_ARCHIVE`                          | Delete `build.xcarchive` file after creating ipa file.                                                                                                                                                                                                   | Optional |

### Output Variables

| Variable Name               | Description                                               |
| --------------------------- | --------------------------------------------------------- |
| `$AC_ARCHIVE_PATH`          | This is the path created after retrieving the archive.    |
| `$AC_ARCHIVE_METADATA_PATH` | This is the path created after the metadata is generated. |
| `$AC_EXPORT_DIR`            | This is the path created when exporting.                  |

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-ios-build-sign-component
