---
title: Firebase Deployment
description: Firebase deployment is quick, and secure app launches. Get started with our concise guide to deploying on Firebase efficiently.
tags: [firebase, web, distribution, deployment]
---

import Screenshot from '@site/src/components/Screenshot';

# Firebase Deployment

[Firebase Deployment](https://firebase.google.com/docs/hosting) is production-grade web content hosting for developers. With a single command, you can quickly deploy web apps and serve both static and dynamic content to a global CDN (content delivery network).

Deploy web applications effortlessly using Appcircle's Firebase Deployment component.

### Prerequisites

Before running the **Firebase Deployment** step, you must complete certain prerequisites, as detailed in the table below:

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [**Flutter Build for Web**](/workflows/flutter-specific-workflow-steps/flutter-build-for-web) | The Flutter Build for Web step builds your web application using the [Flutter SDK](https://docs.flutter.dev/deployment/web#building-the-app-for-release) |
| [**Flutter Install**](/workflows/flutter-specific-workflow-steps/flutter-install) | This step installs the [Flutter SDK](https://docs.flutter.dev/deployment/web#building-the-app-for-release). If no version is specified, it installs the latest stable version. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3150-deployOrder.png' />

### Input Variables

This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3150-deployInput.png' />

:::danger Sensitive Variables

Please do not use sensitive variables such as **Username**, **Password**, **API Key**, or **Personal Access Key** directly within the step.

We recommend using [**Environment Variables**](/environment-variables/managing-variables) groups for such sensitive variables.

:::

| Variable Name                            | Description                                                         | Status           |
|------------------------------------------|---------------------------------------------------------------------|------------------|
| `$AC_FIREBASE_VERSION`                   | Firebase version to be used. Enter v11.11.0 for a specific version. | Required |
| `$AC_FIREBASE_PROJECT_PATH`              | The directory containing your `firebase.json` file.                 | Required |
| `$AC_FIREBASE_TOKEN`                     | A refresh token is generated when you authenticate using the `firebase login:ci` command. Choose either a **Either select Firebase token or Google Service account**. | Optional |
| `$GOOGLE_APPLICATION_CREDENTIALS`        | Specify the path to your Google Service Account JSON file. Upload this file to your environment group under the name `GOOGLE_APPLICATION_CREDENTIALS`. Choose either a **Firebase token**  or a **Google Service account**. | Optional |
| `$AC_FIREBASE_EXTRA_PARAMETERS`          | Extra command line parameters. Enter --debug for debug mode. | Optional |

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-firebase-deploy-component

