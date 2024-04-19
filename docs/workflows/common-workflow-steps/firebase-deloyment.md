---
title: Firebase Deployment
description: Firebase deployment is quick, and secure app launches. Get started with our concise guide to deploying on Firebase efficiently.
tags: [firebase, mobile, web, distribution]
sidebar_position: 8
---

import Screenshot from '@site/src/components/Screenshot';

# Firebase Deployment

[Firebase Deployment](https://firebase.google.com/docs/hosting) is production-grade web content hosting for developers. With a single command, you can quickly deploy web apps and serve both static and dynamic content to a global CDN (content delivery network).

Web applications can be easily deployed using Appcircle's Firebase Deployment component.

### Prerequisites
| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [**Flutter Build for Web**](/workflows/flutter-specific-workflow-steps/flutter-build-for-web) | The Flutter Build for Web step builds your web application using the [Flutter SDK](https://docs.flutter.dev/deployment/web#building-the-app-for-release) |
| [**Flutter Install**](/workflows/flutter-specific-workflow-steps/flutter-install) | This step installs the [Flutter SDK](https://docs.flutter.dev/deployment/web#building-the-app-for-release). If no version is specified, it installs the latest stable version. |


### Input Variables

You can find all the parameters required for this step in the table below, with their descriptions in detail.


:::warning

Do not hard-code sensitive variables, such as tokens and API keys, directly to the parameters in the step.

We recommend using [**Environment Variables**](/environment-variables/managing-variables) groups for such sensitive variables.

:::

| Variable Name                            | Description                                                         | Status           |
|------------------------------------------|---------------------------------------------------------------------|------------------|
| `$AC_FIREBASE_VERSION`                   | Firebase version to be used. Enter v11.11.0 for a specific version. | Required |
| `$AC_FIREBASE_PROJECT_PATH`              | The directory containing your `firebase.json` file.                 | Required |
| `$AC_FIREBASE_TOKEN`                     | A refresh token that's printed when you authenticate with `firebase login:ci` command. **Either select Firebase token or Google Service account**. | Optional |
| `$GOOGLE_APPLICATION_CREDENTIALS`        | Path of Google Service Account JSON. Upload service account as a file to your environment group and name it `GOOGLE_APPLICATION_CREDENTIALS`. **Either select Firebase token or Google Service account**. | Optional |
| `$AC_FIREBASE_EXTRA_PARAMETERS`          | Extra command line parameters. Enter --debug for debug mode. | Optional |


To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-firebase-deploy-component

