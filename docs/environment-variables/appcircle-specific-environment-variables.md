---
title: Reserved Variables
metaTitle: Reserved Variables in Appcircle
metaDescription: Reserved Variables in Appcircle
sidebar_position: 3
---

# Reserved Variables in Appcircle

Here is a list of pre-defined environment variables in Appcircle.

These reserved environment variables are either predetermined by Appcircle or are set in the build configuration.

You can check how these environment variables are utilized within the related workflow step. For instance, you can set the Xcode version of a build profile through the [build configuration](../build/building-ios-applications.md#selecting-the-xcode-version-and-switching-to-the-xcode-beta), which will then set this value as the `AC_XCODE_VERSION` environment variable.

You can then use this variable in any workflow step and this variable will be assigned as the default input value of the [Xcode Select workflow step](https://github.com/appcircleio/appcircle-xcode-select-component). This assignment is editable, meaning that you can either choose to keep it in the same way it is configured or you can change it by specifying a value directly in the step settings or assigning a different environment variable.

For more information on the inputs of the steps and how the variables in the following steps are used, please refer to the documentation of the specific step that is available at [https://github.com/appcircleio](https://github.com/appcircleio)

### iOS & Android common environment variables

| Variable                 | Description                                                                                                                     |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| AC_OUTPUT_DIR            | Output folder path to upload artifacts                                                                                          |
| AC_TEMP_DIR              | Path to temp directory                                                                                                          |
| AC_ENV_FILE_PATH         | Path to the environment file                                                                                                    |
| AC_REPOSITORY_DIR        | Clone repository destination                                                                                                    |
| AC_PROJECT_PATH          | Project path (For Android, `gradlew` file path. For iOS, `.xcodeproj` or `.xcworkspace` file path)                              |
| AC_APPCIRCLE             | Set to `true` when Appcircle starts a build                                                                                     |
| AC_METADATA_OUTPUT_PATH  | Metadata output file path                                                                                                       |
| AC_GIT_URL               | Git URL of the repository                                                                                                       |
| AC_GIT_COMMIT            | The Git commit that is built                                                                                                    |
| AC_COMMIT_MESSAGE        | Commit message                                                                                                                  |
| AC_COMMIT_AUTHOR_EMAIL   | The email of the author of the commit.                                                                                          |
| AC_COMMIT_AUTHOR_NAME    | The name of the author of the commit.                                                                                           |
| AC_COMMIT_AUTHOR_SUBJECT | The subject of the commit.                                                                                                      |
| AC_TAG_AUTHOR_EMAIL      | The email of the author of the tag.                                                                                             |
| AC_TAG_ANNOTATED_MESSAGE | The annotated message of the tag.                                                                                               |
| AC_COMMIT_TAGS           | Commit tags                                                                                                                     |
| AC_BUILD_NUMBER          | Build number (`Fetch Details` is counted as Build)                                                                              |
| AC_BUILD_TIMESTAMP       | Build timestamp (Unix timestamp format)                                                                                         |
| AC_GIT_BRANCH            | The Git branch that is built (eg: master)                                                                                       |
| AC_GIT_TARGET_COMMIT     | Target commit for a Pull or Merge Request                                                                                       |
| AC_GIT_TARGET_BRANCH     | Target branch for a Pull or Merge Request                                                                                       |
| AC_GIT_PR                | Set to `true` if the workflow started for a Pull or Merge Request                                                               |
| AC_PULL_NUMBER           | Pull or Merge Request Number                                                                                                    |
| AC_PROVIDER_NAME         | **Git Provider** Github,GithubApp,Gitlab,GitlabSelfHosted,Bitbucket,BitbucketServer                                             |
| AC_IS_SUCCESS            | Set to `true` if the previous step was successful                                                                               |
| AC_LOGFILE               | Build log path                                                                                                                  |
| AC_TEST_RESULT_PATH      | Test Result Path                                                                                                                |
| AC_WORKFLOW_ID           | Workflow UUID                                                                                                                   |
| AC_WORKFLOW_NAME         | Workflow Name                                                                                                                   |
| AC_PLATFORM_TYPE         | **Platform Type** ObjectiveCSwift, JavaKotlin, ReactNative, Flutter                                                             |
| AC_PURPOSE               | **Purpose of the Workflow** <br />_Metadata_ = 0<br /> _Build_ = 1<br /> _StoreSubmit_ = 2<br />_Merge_ = 3<br />_TagBuild_ = 4 |
| AC_TRIGGER_REASON        | The trigger reason that causes the building to start. Values it can take: `User`, `Commit`, `Tag`, `PullRequest`                |

### Android specific environment variables

| Variable                     | Description                              |
| ---------------------------- | ---------------------------------------- |
| ANDROID_HOME                 | Android SDK installation directory       |
| AC_MODULE                    | Selected Android module                  |
| AC_VARIANTS                  | Selected Android variant                 |
| AC_OUTPUT_TYPE               | Selected output type of Android artifact |
| AC_APK_PATH                  | Generated APK file path                  |
| AC_AAB_PATH                  | Generated AAB file path                  |
| AC_SIGNED_APK_PATH           | Generated signed APK file path           |
| AC_SIGNED_AAB_PATH           | Generated signed AAB file path           |
| AC_ANDROID_KEYSTORE_PATH     | Selected Android keystore path           |
| AC_ANDROID_KEYSTORE_PASSWORD | Password for the selected keystore       |
| AC_ANDROID_ALIAS             | Selected alias name                      |
| AC_ANDROID_ALIAS_PASSWORD    | Selected alias password                  |
| AC_V2_SIGN                   | Specifies if signing will use V2         |
| AC_ANDROID_APP_ANALYSIS_PATH | Location of the app analyzer JSON file   |
| JAVA_HOME_8_X64              | OpenJDK 8 Location                       |
| JAVA_HOME_11_X64             | OpenJDK 11 Location                      |
| JAVA_HOME_17_X64             | OpenJDK 17 Location                      |
| AC_BUILD_NUMBER_SOURCE       | Build Number Source for Versioning       |
| AC_ANDROID_BUILD_NUMBER      | Build Number for Versioning              |
| AC_BUILD_OFFSET              | Build Number Offset for Versioning       |
| AC_VERSION_NUMBER_SOURCE     | Version Number Source for Versioning     |
| AC_ANDROID_VERSION_NUMBER    | Version Number for Versioning            |
| AC_ANDROID_VERSION_STRATEGY  | Version Increment Strategy               |
| AC_VERSION_OFFSET            | Version Number Offset for Versioning     |
| AC_FLAVOR                    | Flavor for Versioning                    |

### iOS specific environment variables

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
| AC_IOS_VERSION_STRATEGY   | Version Increment Strategy                                                                                                                                                                                                                                                                                                                                                                                             |
| AC_VERSION_OFFSET         | Version Number Offset for Versioning                                                                                                                                                                                                                                                                                                                                                                                   |
| AC_BUNDLE_ID              | Bundle Id for Versioning                                                                                                                                                                                                                                                                                                                                                                                               |
| AC_APPSTORE_COUNTRY       | App Store Country for Versioning                                                                                                                                                                                                                                                                                                                                                                                       |
| AC_TARGETS                | iOS Targets for Versioning                                                                                                                                                                                                                                                                                                                                                                                             |
| AC_IOS_CONFIGURATION_NAME | Configuration name for Versioning                                                                                                                                                                                                                                                                                                                                                                                      |
| AC_AUTOSIGN_CRED_PATH     | App Store Connect API Key Path. **Only active if automatic signing is turned on.**                                                                                                                                                                                                                                                                                                                                     |
| AC_AUTOSIGN_KEY           | App Store Connect API Key Id. **Only active if automatic signing is turned on.**                                                                                                                                                                                                                                                                                                                                       |
| AC_AUTOSIGN_ISSUER_ID     | App Store Connect API Issuer Id. **Only active if automatic signing is turned on.**                                                                                                                                                                                                                                                                                                                                    |

### iOS Publish specific environment variables

| Variable                | Description                                                                                           |
| ----------------------- | ----------------------------------------------------------------------------------------------------- |
| AC_XCODE_LIST_DIR       | Specifies the Xcode folder list directory                                                             |
| AC_XCODE_VERSION        | Specifies the Xcode version                                                                           |
| AC_VALIDATION_CONDITION | TestFlight's `internalBuildState` and `externalBuildState` will be checked according to the selection |
| AC_SUCCESS_STATUSES     | You can customize `Acceptable/Succeeded` App Store statuses for your app                              |
| AC_RELEASE_NOTES        | Filling out that area may effect the App Store submission process.                                    |
| AC_STACK_TYPE           | `App Store` or `TestFlight` stages                                                                    |
| AC_APPROVAL_EMAILS      | Enter an email address to send special `Approve` and `Reject` links                                   |

### Android Publish specific environment variables

| Variable             | Description                                                                                                                       |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| AC_RELEASE_STATUS    | Allow you to specify `draft` or `completed` app statuses on the Google Play Console. The first upload may require a draft upload  |
| AC_TRACK_TO_CHECK    | It's recommended to check Track that you've sent the app in previous steps                                                        |
| AC_ACCEPTED_STATUSES | Statues of `completed`,`inProgress`,`draft`,`halted` can be used                                                                  |
| AC_HUAWEI_APP_ID     | Huawei requires `Huawei App ID` to be send to AppGallery                                                                          |
| AC_RELEASE_NOTES     | Filling out that area may effect `Huawei` or `Google Play` submission process                                                     |
| AC_STACK_TYPE        | Select a release track to which to send the binary. After the binary is uploaded, you can release it from the Google Play Console |
| AC_APPROVAL_EMAILS   | Enter an email address to send special `Approve` and `Reject` links                                                               |
