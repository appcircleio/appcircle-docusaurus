---
title: Appcircle-Specific (Reserved) Environment Variables
metaTitle: Appcircle-Specific (Reserved) Environment Variables
metaDescription: Appcircle-Specific (Reserved) Environment Variables
sidebar_position: 3
---
# Appcircle-Specific (Reserved) Environment Variables

Here is a list of pre-defined environment variables in Appcircle.

These reserved environment variables are either predetermined by Appcircle or are set in the build configuration.

You can check how these environment variables are utilized within the related workflow step. For instance, you can set the Xcode version of a build profile through the [build configuration](../build/building-ios-applications.md#selecting-the-xcode-version-and-switching-to-the-xcode-beta), which will then set this value as the `AC_XCODE_VERSION` environment variable.

You can then use this variable in any workflow step and this variable will be assigned as the default input value of the [Xcode Select workflow step](https://github.com/appcircleio/appcircle-xcode-select-component). This assignment is editable, meaning that you can either choose to keep it in the same way it is configured or you can change it by specifying a value directly in the step settings or assigning a different environment variable.

For more information on the inputs of the steps and how the variables in the following steps are used, please refer to the documentation of the specific step that is available at [https://github.com/appcircleio](https://github.com/appcircleio)



### iOS & Android common environment variables

| Variable                   | Description                                                                                        |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| AC\_OUTPUT\_DIR            | Output folder path to upload artifacts                                                             |
| AC\_TEMP\_DIR              | Path to temp directory                                                                             |
| AC\_ENV\_FILE\_PATH        | Path to the environment file                                                                       |
| AC\_REPOSITORY\_DIR        | Clone repository destination                                                                       |
| AC\_PROJECT\_PATH          | Project path (For Android, `gradlew` file path. For iOS, `.xcodeproj` or `.xcworkspace` file path) |
| AC\_APPCIRCLE              | Set to `true` when Appcircle starts a build                                                        |
| AC\_METADATA\_OUTPUT\_PATH | Metadata output file path                                                                          |
| AC\_GIT\_URL               | Git URL of the repository                                                                          |
| AC\_GIT\_COMMIT            | The Git commit that is built                                                                       |
| AC\_COMMIT\_MESSAGE        | Commit message                                                                                     |
| AC\_COMMIT\_AUTHOR\_EMAIL  | The email of the author of the commit.                                                             |
| AC\_COMMIT\_AUTHOR\_NAME   | The name of the author of the commit.                                                              |
| AC\_COMMIT\_AUTHOR\_SUBJECT| The subject of the commit.                                                                        |
| AC\_TAG\_AUTHOR\_EMAIL     | The email of the author of the tag.                                                                |
| AC\_TAG\_ANNOTATED\_MESSAGE| The annotated message of the tag.                                                                  |
| AC\_COMMIT\_TAGS           | Commit tags                                                                                        |
| AC\_BUILD\_NUMBER          | Build number (`Fetch Details` is counted as Build)                                                 |
| AC\_BUILD\_TIMESTAMP       | Build timestamp (Unix timestamp format)                                                                                   |
| AC\_GIT\_BRANCH            | The Git branch that is built (eg: master)                                                          |
| AC\_GIT\_TARGET\_COMMIT    | Target commit for a Pull or Merge Request                                                          |
| AC\_GIT\_TARGET\_BRANCH    | Target branch for a Pull or Merge Request                                                          |
| AC\_GIT\_PR                | Set to `true` if the workflow started for a Pull or Merge Request                                  |
| AC\_PULL\_NUMBER           | Pull or Merge Request Number                                                                       |
| AC\_PROVIDER\_NAME         | **Git Provider** Github,GithubApp,Gitlab,GitlabSelfHosted,Bitbucket,BitbucketServer                |
| AC\_IS\_SUCCESS            | Set to `true` if the previous step was successful                                                  |
| AC\_LOGFILE                | Build log path                                                                                     |
| AC\_TEST\_RESULT\_PATH     | Test Result Path                                                                                   |
| AC\_WORKFLOW\_ID           | Workflow UUID                                                                                      |
| AC\_WORKFLOW\_NAME         | Workflow Name                                                                                      |
| AC\_PLATFORM\_TYPE         | **Platform Type** ObjectiveCSwift, JavaKotlin, ReactNative, Flutter                     |
| AC\_PURPOSE                | **Purpose of the Workflow** <br />_Metadata_ = 0<br /> _Build_ = 1<br /> _StoreSubmit_ = 2<br />_Merge_ = 3<br />_TagBuild_ = 4|
| AC\_TRIGGER\_REASON        |  The trigger reason that causes the building to start. Values it can take: `User`, `Commit`, `Tag`, `PullRequest` |


### Android specific environment variables

| Variable                         | Description                              |
| -------------------------------- | ---------------------------------------- |
| ANDROID\_HOME                    | Android SDK installation directory       |
| AC\_MODULE                       | Selected Android module                  |
| AC\_VARIANTS                     | Selected Android variant                 |
| AC\_OUTPUT\_TYPE                 | Selected output type of Android artifact |
| AC\_APK\_PATH                    | Generated APK file path                  |
| AC\_AAB\_PATH                    | Generated AAB file path                  |
| AC\_SIGNED\_APK\_PATH            | Generated signed APK file path           |
| AC\_SIGNED\_AAB\_PATH            | Generated signed AAB file path           |
| AC\_ANDROID\_KEYSTORE\_PATH      | Selected Android keystore path           |
| AC\_ANDROID\_KEYSTORE\_PASSWORD  | Password for the selected keystore       |
| AC\_ANDROID\_ALIAS               | Selected alias name                      |
| AC\_ANDROID\_ALIAS\_PASSWORD     | Selected alias password                  |
| AC\_V2\_SIGN                     | Specifies if signing will use V2         |
| AC\_ANDROID\_APP\_ANALYSIS\_PATH | Location of the app analyzer JSON file   |
| JAVA\_HOME\_8\_X64               | OpenJDK 8 Location                       |
| JAVA\_HOME\_11\_X64              | OpenJDK 11 Location                      |
| JAVA\_HOME\_17\_X64              | OpenJDK 17 Location                      |
| AC\_BUILD\_NUMBER\_SOURCE        | Build Number Source for Versioning       |
| AC\_ANDROID\_BUILD\_NUMBER       | Build Number for Versioning              |
| AC\_BUILD\_OFFSET                | Build Number Offset for Versioning       |
| AC\_VERSION\_NUMBER\_SOURCE      | Version Number Source for Versioning     |
| AC\_ANDROID\_VERSION\_NUMBER     | Version Number for Versioning            |
| AC\_ANDROID\_VERSION\_STRATEGY   | Version Increment Strategy               |
| AC\_VERSION\_OFFSET              | Version Number Offset for Versioning     |
| AC\_FLAVOR                       | Flavor for Versioning                    |

### iOS specific environment variables

| Variable                     | Description                                                                           |
| ---------------------------- | ------------------------------------------------------------------------------------- |
| AC\_XCODE\_LIST\_DIR         | Specifies the Xcode folder list path                                                  |
| AC\_SCHEME                   | Specifies the project scheme for build                                                |
| AC\_ARCHIVE\_FLAGS           | Specifies the extra Xcodebuild flag. For example: `-configuration DEBUG`              |
| AC\_XCODE\_VERSION           | Specifies the Xcode version                                                           |
| AC\_ARCHIVE\_PATH            | Archive path                                                                          |
| AC\_ARCHIVE\_METADATA\_PATH  | Archive metadata path                                                                 |
| AC\_SIMULATOR\_ARCHIVE\_PATH | Simulator archive path description                                                    |
| AC\_METADATA\_OUTPUT\_PATH   | Metadata output file description                                                      |
| AC\_CERTIFICATES             | Concatenated strings of 'cert_pass\|cert_path' combined with a pipe ('\|') character that have the paths of the certificates and their passwords if they exist. <br/><br/> For instance, when we have two certificates A and B that require passwords, then it should be like 'a_cert_pass\|a_cert_path\|b_cert_pass\|b_cert_path'. <br/><br/> If there is no password, its field will be empty, like '\|a_cert_path'.                         |
| AC\_PROVISIONING\_PROFILES   | Paths of the provisioning profiles                                                    |
| AC\_EXPORT\_DIR              | Specifies the path that contains `ipa`, `exportOptions.plist`and other exported files |
| AC\_BUNDLE\_IDENTIFIERS      | Specifies the project bundle identifiers                                              |
| AC\_BUILD\_NUMBER\_SOURCE    | Build Number Source for Versioning                                                    |
| AC\_IOS\_BUILD\_NUMBER       | Build Number for Versioning                                                           |
| AC\_BUILD\_OFFSET            | Build Number Offset for Versioning                                                    |
| AC\_VERSION\_NUMBER\_SOURCE  | Version Number Source for Versioning                                                  |
| AC\_IOS\_VERSION\_NUMBER     | Version Number for Versioning                                                         |
| AC\_IOS\_VERSION\_STRATEGY   | Version Increment Strategy                                                            |
| AC\_VERSION\_OFFSET          | Version Number Offset for Versioning                                                  |
| AC\_BUNDLE\_ID               | Bundle Id for Versioning                                                              |
| AC\_APPSTORE\_COUNTRY        | App Store Country for Versioning                                                      |
| AC\_TARGETS                  | iOS Targets for Versioning                                                            |
| AC\_IOS_CONFIGURATION\_NAME  | Configuration name for Versioning                                                     |
| AC\_AUTOSIGN\_CRED\_PATH     | App Store Connect API Key Path. **Only active if automatic signing is turned on.**    |
| AC\_AUTOSIGN\_KEY            | App Store Connect API Key Id.  **Only active if automatic signing is turned on.**     |
| AC\_AUTOSIGN\_ISSUER\_ID     | App Store Connect API Issuer Id.  **Only active if automatic signing is turned on.**  |

### iOS Publish specific environment variables

| Variable                  | Description                                                                                    |
|---------------------------|------------------------------------------------------------------------------------------------|
| AC\_XCODE\_LIST\_DIR      | Specifies the Xcode folder list directory                                                      |
| AC\_XCODE\_VERSION        | Specifies the Xcode version                                                                    |
| AC\_VALIDATION\_CONDITION | TestFlight's `internalBuildState` and `externalBuildState` will be checked according to the selection |
| AC\_SUCCESS\_STATUSES     | You can customize `Acceptable/Succeeded` App Store statuses for your app                       |
| AC\_RELEASE\_NOTES        | Filling out that area may effect the App Store submission process.                             |
| AC\_STACK\_TYPE           | `App Store` or `TestFlight` stages                                                                 |
| AC\_APPROVAL\_EMAILS      | Enter an email address to send special `Approve` and `Reject` links                            |

### Android Publish specific environment variables

| Variable               | Description                                                                                                                       |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| AC\_RELEASE\_STATUS    | Allow you to specify `draft` or `completed` app statuses on the Google Play Console. The first upload may require a draft upload  |
| AC\_TRACK\_TO\_CHECK   | It's recommended to check Track that you've sent the app in previous steps                                                        |
| AC\_ACCEPTED\_STATUSES | Statues of `completed`,`inProgress`,`draft`,`halted` can be used                                                                  |
| AC\_HUAWEI\_APP\_ID    | Huawei requires `Huawei App ID` to be send to AppGallery                                                                          |
| AC\_RELEASE\_NOTES     | Filling out that area may effect `Huawei` or `Google Play` submission process                                                     |
| AC\_STACK\_TYPE        | Select a release track to which to send the binary. After the binary is uploaded, you can release it from the Google Play Console |
| AC\_APPROVAL\_EMAILS   | Enter an email address to send special `Approve` and `Reject` links                                                               |

