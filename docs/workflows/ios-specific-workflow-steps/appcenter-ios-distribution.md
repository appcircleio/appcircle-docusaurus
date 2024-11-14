---
title: App Center iOS Distribution
description: Distribute your iOS app to App Center for testing and distribution.
tags: [build, test, distribute, app center, ios, workflow, step]
---

import Screenshot from '@site/src/components/Screenshot';

# App Center iOS Distrubiton

With this step, you can send your `IPA` and `dSYM` files to the [App Center](https://appcenter.ms/). For this, the step needs to be configured according to your App Center account.

### Prerequisites

Before running the **App Center iOS Distrubiton** step, you must complete certain prerequisites, as detailed in the table below:

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [**Xcodebuild for Devices**](https://docs.appcircle.io/workflows/ios-specific-workflow-steps#xcodebuild-for-devices-archive--export) | This step will build your application in ARM architecture and generate an `IPA` and `dSYM` file. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2612-center_order.png' />

:::caution

Note that if you do not use this step after the [**Xcodebuild for Devices**](https://docs.appcircle.io/workflows/ios-specific-workflow-steps#xcodebuild-for-devices-archive--export), Appcircle will not find **IPA** and **dSYM** files to distribute to the **App Center**.

:::

### Input Variables

This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2612-centerInput.png' />

:::danger Sensitive Variables

Please do not use sensitive variables such as **Username**, **Password**, **API Key**, or **Personal Access Key** directly within the step.

We recommend using [**Environment Variables**](/environment-variables/managing-variables) groups for such sensitive variables.

:::


| Variable Name                 | Description                                    | Status |
|-------------------------------|------------------------------------------------|--------|
| `$AC_APPCENTER_TOKEN`        | You need to enter your **App Center Access Token** in this parameter. The CLI tool will be authenticated with this token. | Required |
| `$AC_APPCENTER_IPA_PATH`     | Full path of the build. The path will be generated after the **Xcodebuild for Devices** step. You may enter the exact path of the `IPA` or the parent folder. | Required |
| `$AC_APPCENTER_OWNER`       | Owner of the app. The app's owner can be identified in its URL, such as `https://appcenter.ms/users/JohnDoe/apps/myapp` for a user-owned app (where **JohnDoe** is the owner) and `https://appcenter.ms/orgs/Appcircle/apps/myapp` for an org-owned app (the owner is **Appcircle**). | Required |
| `$AC_APPCENTER_APPNAME`            | The name of the app. The app's name can be identified in its URL, such as `https://appcenter.ms/users/JohnDoe/apps/myapp` for a user-owned app (where **myapp** is the app name) and `https://appcenter.ms/orgs/Appcircle/apps/myapp` for an org-owned app (the owner is **myapp**). | Required |
| `$AC_APPCENTER_GROUPS`             | The group name parameter is the distribution of `Group Names` you opened in your App Center account. You can type in which group you want to send it to. | Optional |
| `$AC_APPCENTER_STORE`              | Name of the store (App Store, Google Play, Intune). You can submit directly to this variable by giving one of the store names in your App Center account. | Optional |
| `$AC_APPCENTER_RELEASE_NOTES_PATH`  | If you use the `Publish Release Notes` component before this step, release-notes.txt will be used as release notes. | Optional |
| `$AC_APPCENTER_UPLOAD_DSYM`        | The user can decide whether to upload your `dSYM` file. This parameter uploads the `dSYM` file automatically. The default value is **true**. | Optional |
| `$AC_APPCENTER_MANDATORY`          | This parameter specifies whether the update should be considered mandatory or not. The default value is **false**. | Optional |
| `$AC_APPCENTER_NOTIFY`             | This parameter sends notifications to testers. The default value is **true**. | Optional |
| `$AC_APPCENTER_VERSION`             | The latest version will be used if no version is set. | Optional |
| `$AC_APPCENTER_EXTRA`               | Extra command line arguments for App Center. For example, add `--debug` for verbose logs. | Optional |

---

To access the source code of this component, please use the following link:

[https://github.com/appcircleio/appcircle-ios-appcenter-distribute-component](https://github.com/appcircleio/appcircle-ios-appcenter-distribute-component)