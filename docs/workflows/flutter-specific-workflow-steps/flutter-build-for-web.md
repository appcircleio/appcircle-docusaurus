---
title: ​Flutter Build for Web
description: Learn to build web apps with the Flutter Build for Web component. Ensure Flutter Install and Git Clone steps are completed first.
tags: [flutter, build, test, workflow, step]
---

import Screenshot from '@site/src/components/Screenshot';

# ​Flutter Build for Web

The **Flutter Build for Web** step builds your web application using the [Flutter SDK](https://flutter.dev/docs/deployment/web#building-the-app-for-release).

### Prerequisites

There are no prerequisites required before using the **​Flutter Build for Web** step.

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [**Git Clone**](/workflows/common-workflow-steps/git-clone) | This step clones your project from the connected Git provider and creates the `$AC_REPOSITORY_DIR` variable, which defaults to `$AC_FLUTTER_PROJECT_DIR`. |
| [**Flutter Install**](./flutter-install) | This step installs the [Flutter SDK](https://flutter-ko.dev/development/tools/sdk/releases). If no version is specified, it installs the latest **stable** version. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2855-flutterWebOrder.png' />

:::warning

This step relies heavily on the **Flutter Install** step. If the Flutter SDK is not installed, the step will report an error stating that the required command was not found.

:::

### Input Variables

You can find all the parameters required for this step in the table below, along with detailed descriptions.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2855-flutterWebInput.png' />

| Variable Name                 | Description                         | Status 			|
|-------------------------------|-------------------------------------|-----------------|
| `$AC_FLUTTER_PROJECT_DIR`     | This parameter represents the repository path. The default value is `$AC_REPOSITORY_DIR`, which is created after the **Git Clone** step. | Required|


### Output Variables

| Variable Name          | Description                         |
|------------------------|-------------------------------------|
| `$AC_FLUTTER_WEB_PATH` | This path is generated after the completion of the **Flutter Build for Web** step and stores the generated web application. | 


### Deploying Applications to AWS Services

AWS Amplify offers a fully managed service for deploying and hosting static web applications, and Appcircle supports building Flutter web apps.

You can deploy Flutter web apps (or any other web app) that you build with Appcircle to AWS Amplify Console for an end-to-end app lifecycle from a single CI/CD platform for web and mobile.

To deploy apps to Amplify, you can use Git, manual uploads, or Amazon S3 buckets as the source.

Since Appcircle supports automated Amazon S3 uploads, you can automatically deploy your apps from Appcircle to Amazon S3 and then sync your S3 bucket with Amplify Console with the following steps:

- First, set up a [Flutter Web App build](../../.././build/platform-build-guides/building-flutter-applications/building-flutter-web-applications).
- Then, add an [Upload to Amazon S3 step to your workflow](/workflows/common-workflow-steps/upload-files-to-amazon-s3) and configure it to receive the web app artifact as the input of the step.
- To set up Amplify Console and S3 sync, first go to Amplify and [set up a manual deployment](https://docs.aws.amazon.com/amplify/latest/userguide/manual-deploys.html).
- Then, follow the steps [in this AWS blog post](https://aws.amazon.com/blogs/mobile/deploy-files-s3-dropbox-amplify-console/) to automate deployments from an S3 bucket to Amplify.

You can build your Flutter web apps with Appcircle and deploy them to the Amplify Console with end-to-end automation.

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-flutter-web-build-component