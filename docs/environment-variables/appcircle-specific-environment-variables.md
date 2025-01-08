---
title: Reserved Variables
description: Here is a list of pre-defined environment variables in Appcircle.
tags: [environment variables, env vars, variables, build configuration, custom build scripts]
sidebar_position: 3
---

# Reserved Variables in Appcircle

Here is a list of pre-defined environment variables in Appcircle.

These reserved environment variables are either predetermined by Appcircle or are set in the build configuration.

You can check how these environment variables are utilized within the related workflow step. For instance, you can set the Xcode version of a build profile through the [build configuration](../build/platform-build-guides/building-ios-applications#selecting-the-xcode-version-and-switching-to-the-xcode-beta), which will then set this value as the `AC_XCODE_VERSION` environment variable.

You can then use this variable in any workflow step and this variable will be assigned as the default input value of the [Xcode Select workflow step](https://github.com/appcircleio/appcircle-xcode-select-component). This assignment is editable, meaning that you can either choose to keep it in the same way it is configured or you can change it by specifying a value directly in the step settings or assigning a different environment variable.

For more information on the inputs of the steps and how the variables in the following steps are used, please refer to the documentation of the specific step that is available at [https://github.com/appcircleio](https://github.com/appcircleio)

### iOS & Android Common Environment Variables

| Variable                 | Description                                                                                        |
| ------------------------ | -------------------------------------------------------------------------------------------------- |
| AC_OUTPUT_DIR            | Output folder path to upload artifacts.                                                            |
| AC_TEMP_DIR              | Path to temp directory.                                                                            |
| AC_ENV_FILE_PATH         | Path to the environment file.                                                                      |
| AC_REPOSITORY_DIR        | Clone repository destination.                                                                      |
| AC_PROJECT_PATH          | Project path (For Android `gradlew` file path. For iOS `.xcodeproj` or `.xcworkspace` file path).  |
| AC_APPCIRCLE             | Set to `true` when Appcircle starts a build.                                                       |
| AC_METADATA_OUTPUT_PATH  | Metadata output file path.                                                                         |
| AC_GIT_URL               | Git URL of the repository.                                                                         |
| AC_GIT_COMMIT            | The Git commit that is built.                                                                      |
| AC_COMMIT_MESSAGE        | Commit message.                                                                                    |
| AC_COMMIT_AUTHOR_NAME    | The name of the author of the commit.                                                              |
| AC_COMMIT_AUTHOR_EMAIL   | Email address of the commit author.                                                                |
| AC_COMMIT_SUBJECT	       | Subject or title of the commit message.                                                            |
| AC_TAG_AUTHOR_EMAIL      | The email of the author of the tag.                                                                |
| AC_TAG_ANNOTATED_MESSAGE | The annotated message of the tag.                                                                  |
| AC_COMMIT_TAGS           | Commit tags.                                                                                       |
| AC_BUILD_NUMBER          | Build number (`Fetch Details` is counted as Build).                                                |
| AC_BUILD_TIMESTAMP       | Build timestamp (Unix timestamp format).                                                           |
| AC_BUILD_PROFILE_ID      | Unique identifier for the build profile.
| AC_GIT_BRANCH            | The Git branch that is built (eg: master).                                                         |
| AC_GIT_TARGET_COMMIT     | Target commit for a Pull or Merge Request.                                                         |
| AC_GIT_TARGET_BRANCH     | Target branch for a Pull or Merge Request.                                                         |
| AC_GIT_PR                | Set to `true` if the workflow started for a Pull or Merge Request.                                 |
| GIT_VERSION              | Version of the Git installed.                                                                      |
| AC_PULL_NUMBER           | Pull or merge request number.                                                                      |
| AC_INTERNAL_TRIGGER_USER | The user who initiated the build, either [manually](https://docs.appcircle.io/build/build-process-management/build-manually-or-with-triggers#manual-build) or [automatically](https://docs.appcircle.io/build/build-process-management/build-manually-or-with-triggers#automatic-build). |
| AC_INTERNAL_CONFIGURATION_NAME | Name of the configuration that used the build.                                               |
| AC_INTERNAL_CONFIGURATION_ID | Unique identifier for the [configuration](https://docs.appcircle.io/build/build-process-management/build-profile-configuration) that started the build. |
| AC_PROVIDER_NAME         | **Git Provider**. Options include: GitHub, GitHub App, GitLab, GitLab Self-Hosted, Bitbucket, Bitbucket Server, Azure DevOps Services. |
| AC_IS_SUCCESS            | Set to `true` if the previous step was successful.                                                 |
| AC_LOGFILE               | Build log path.                                                                                    |
| AC_TEST_RESULT_PATH      | Test result path.                                                                                  |
| AC_WORKFLOW_ID           | Workflow UUID.                                                                                     |
| AC_WORKFLOW_NAME         | Workflow name.                                                                                     |
| AC_PLATFORM_TYPE         | **Platform Type**: ObjectiveCSwift, JavaKotlin, ReactNative, Flutter.                              |
| AC_PURPOSE               | **Purpose of the Workflow** <br />_Metadata_ = 0<br /> _Build_ = 1<br /> _StoreSubmit_ = 2<br />_Merge_ = 3<br />_TagBuild_ = 4. |
| AC_TRIGGER_REASON        | The trigger reason that causes the building to start. Values it can take: `User`, `Commit`, `Tag`, `PullRequest`. |
| AC_USER_ORG_ROLES        | The permission list of the user who started the build. |
| AC_OMIT_ZERO_PATCH_VERSION |	Controls whether zero is omitted in the patch version. Options are true  or false.              |
| LC_CTYPE	               | Defines the character encoding and character classification properties.                            |
| AC_VERSION_STRATEGY      | Strategy used for versioning (e.g., major, minor, patch).                                          |
| AC_ORGANIZATION_ID       | Unique identifier for the organization.                                                            |

### Reserved Android Variables

| Variable                     | Description                                                                                                                         |
| ---------------------------- |-------------------------------------------------------------------------------------------------------------------------------------|
| ANDROID_HOME                 | Android SDK installation directory.                                                                                                 |
| AC_MODULE                    | Selected Android module.                                                                                                            |
| AC_VARIANTS                  | Selected Android variant.                                                                                                           |
| AC_OUTPUT_TYPE               | Selected output type of Android artifact.                                                                                           |
| AC_APK_PATH                  | Generated APK file path.                                                                                                            |
| AC_AAB_PATH                  | Generated AAB file path.                                                                                                            |
| AC_SIGNED_APK_PATH           | Generated signed APK file path.                                                                                                     |
| AC_SIGNED_AAB_PATH           | Generated signed AAB file path.                                                                                                     |
| AC_ANDROID_KEYSTORE_PATH     | Selected Android keystore path.                                                                                                     |
| AC_ANDROID_KEYSTORE_PASSWORD | Password for the selected keystore.                                                                                                 |
| AC_ANDROID_ALIAS             | Selected alias name.                                                                                                                |
| AC_ANDROID_ALIAS_PASSWORD    | Selected alias password.                                                                                                            |
| AC_V2_SIGN                   | Specifies if signing will use V2.                                                                                                   |
| AC_ANDROID_POST_PROCESS_OUTPUT_PATH | Path to the output file generated by the [Android Post-Processing](/workflows/android-specific-workflow-steps/app-post-processor) step. |
| JAVA_HOME                    | Directory path of the Java JDK installation.                                                                                        |
| JAVA_OPTS                    | Options for Java arguments. For example: `-Xms1536M -Xmx9216M`                                                                      |
| JAVA_VERSION                 | Version of the Java JDK installed.                                                                                                  |
| JAVA_HOME_8_X64              | OpenJDK 8 location.                                                                                                                 |
| JAVA_HOME_11_X64             | OpenJDK 11 location.                                                                                                                |
| JAVA_HOME_17_X64             | OpenJDK 17 location.                                                                                                                |
| JAVA_HOME_21_X64             | OpenJDK 21 location.                                                                                                                |
| GRADLE_OPTS                  | Configuration options for [Gradle build](https://docs.gradle.org/current/userguide/command_line_interface.html).                    |
| AC_BUILD_NUMBER_SOURCE       | Build number source for versioning.                                                                                                 |
| AC_ANDROID_BUILD_NUMBER      | Build number for versioning.                                                                                                        |
| AC_BUILD_OFFSET              | Build number offset for versioning.                                                                                                 |
| AC_VERSION_NUMBER_SOURCE     | Version number source for versioning.                                                                                               |
| AC_ANDROID_VERSION_NUMBER    | Version number for versioning.                                                                                                      |
| AC_VERSION_OFFSET            | Version number offset for versioning.                                                                                               |
| AC_VERSION_FLAVOR            | Flavor for versioning.                                                                                                              |

### Reserved iOS Variables

| Variable                  | Description                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AC_XCODE_LIST_DIR         | Specifies the Xcode folder list path                                                                                                                                                                                                                                                                                                                                                                                   |
| AC_SCHEME                 | Specifies the project scheme for build                                                                                                                                                                                                                                                                                                                                                                                 |
| AC_ARCHIVE_FLAGS          | Specifies the extra Xcodebuild flag. For example: `-configuration DEBUG`                                                                                                                                                                                                                                                                                                                                               |
| AC_XCODE_VERSION          | Specifies the Xcode version                                                                                                                                                                                                                                                                                                                                                                                            |
| AC_ARCHIVE_PATH           | Archive path                                                                                                                                                                                                                                                                                                                                                                                                           |
| AC_ARCHIVE_METADATA_PATH  | Archive metadata path                                                                                                                                                                                                                                                                                                                                                                                                  |
| AC_SIMULATOR_ARCHIVE_PATH | Simulator archive path description                                                                                                                                                                                                                                                                                                                                                                                     |
| AC_METADATA_OUTPUT_PATH   | Metadata output file description                                                                                                                                                                                                                                                                                                                                                                                       |
| AC_CERTIFICATES           | Concatenated strings of 'cert_pass\|cert_path' combined with a pipe ('\|') character that have the paths of the certificates and their passwords if they exist. <br/><br/> For instance, when we have two certificates A and B that require passwords, then it should be like 'a_cert_pass\|a_cert_path\|b_cert_pass\|b_cert_path'. <br/><br/> If there is no password, its field will be empty, like '\|a_cert_path'. |
| AC_PROVISIONING_PROFILES  | Paths of the provisioning profiles                                                                                                                                                                                                                                                                                                                                                                                     |
| AC_EXPORT_DIR             | Specifies the path that contains `ipa`, `exportOptions.plist`and other exported files                                                                                                                                                                                                                                                                                                                                  |
| AC_BUNDLE_IDENTIFIERS     | Specifies the project bundle identifiers                                                                                                                                                                                                                                                                                                                                                                               |
| AC_BUILD_NUMBER_SOURCE    | Build Number Source for Versioning                                                                                                                                                                                                                                                                                                                                                                                     |
| AC_IOS_BUILD_NUMBER       | Build Number for Versioning                                                                                                                                                                                                                                                                                                                                                                                            |
| AC_BUILD_OFFSET           | Build Number Offset for Versioning                                                                                                                                                                                                                                                                                                                                                                                     |
| AC_VERSION_NUMBER_SOURCE  | Version Number Source for Versioning                                                                                                                                                                                                                                                                                                                                                                                   |
| AC_IOS_VERSION_NUMBER     | Version Number for Versioning                                                                                                                                                                                                                                                                                                                                                                                          |
| AC_VERSION_OFFSET         | Version Number Offset for Versioning                                                                                                                                                                                                                                                                                                                                                                                   |
| AC_BUNDLE_ID              | Bundle Id for Versioning                                                                                                                                                                                                                                                                                                                                                                                               |
| AC_TARGETS                | iOS Targets for Versioning                                                                                                                                                                                                                                                                                                                                                                                             |
| AC_IOS_CONFIGURATION_NAME | Configuration name for Versioning                                                                                                                                                                                                                                                                                                                                                                                      |
| AC_AUTOSIGN_CRED_PATH     | App Store Connect API Key Path. **Only active if automatic signing is turned on.**                                                                                                                                                                                                                                                                                                                                     |
| AC_AUTOSIGN_METHOD_FOR_EXPORT | Specifies the signing method when [automatic signing](https://docs.appcircle.io/signing-identities/apple-profiles#automatic-signing) is enabled. Options include `App Store`, `Ad-Hoc`, `Development`, `Enterprise`". Default value is `App Store`. |
| AC_AUTOSIGN_KEY           | App Store Connect API Key Id. **Only active if automatic signing is turned on.**                                                                                                                                                                                                                                                                                                                                       |
| AC_AUTOSIGN_ISSUER_ID     | App Store Connect API Issuer Id. **Only active if automatic signing is turned on.**                                                                                                                                                                                                                                                                                                                                    |

                                                       
