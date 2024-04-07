---
title: Firebase Test Lab for Android
description: Integrate Appcircle with Firebase Test Lab for continuous Android app testing. Prerequisites include Android Build for UI Testing.
tags: [android, test, Firebase, test lab, continuous testing, UI testing, robo testing, instrumentation testing]
sidebar_position: 8
---

import Screenshot from '@site/src/components/Screenshot';

# Firebase Test Lab for Android

Appcircle is integrated with the [Firebase Test Lab](https://firebase.google.com/products/test-lab) for continuous testing. Your app can be built in Appcircle and directly deployed to the Firebase Test Lab to run automated tests.

## Prerequisites

The necessary workflow steps to execute before running the **Firebase Test Lab for Android** workflow step, along with their respective reasons, are listed in the table below.

| Prerequisite Workflow Step                                                            | Description                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Android Build for UI Testing](./android-build-for-ui-testing) | The **Android Build for UI Testing** step must be executed to obtain the necessary Android application outputs for processing. |

In addition to the steps you need to run on Appcircle, there are also adjustments you need to make on the Firebase Test Lab side. These adjustments can be made as follows:

### 1. Setting Up a Firebase Project and a Service Account

To begin with the [Firebase Test Lab](https://firebase.google.com/products/test-lab), you need to have an associated Firebase Project, which is created in the [Firebase console](https://console.firebase.google.com). Go to the console, press the `Add Project` button, and specify the project name and other settings:

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (45).png' />

Once your project is created, go to the [Google Cloud Platform console](https://console.cloud.google.com/iam-admin/serviceaccounts/) to create a service account. Press the `Create Service Account` button and follow the prompts to create a service account with the **Editor** role:

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (49).png' />

After the service account is created, click on the three-dot (**⋮**) menu next to the service account and press `Create Key`.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (50).png' />

Select the key format as `JSON` and download the created key. This key will be used by Appcircle to deploy apps to the Firebase Test Lab.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (51).png' />

As the final step, go to the [Google Developers Console API Library page](https://console.developers.google.com/apis/library) and find and enable the following APIs:

- Google Cloud Testing API
- Cloud Tool Results API.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (61).png' />

### 2. Build Workflow Configuration for Firebase Test Lab

To utilize the Firebase Test Lab in your builds, open the [workflow editor](/workflows) and add the **Firebase Test Lab for Android** step after the build or sign steps. If you want to run instrumentation tests, also add the **Android Build for UI Testing** step before the **Firebase Test Lab for Android** step.

:::caution

If you want to run **robo** tests, it is highly recommended not to add the **Android Build for UI Testing** step.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/firebasetestlab-workflow-select.png' />

If you want to use the UI Test Build output or the Signed Build output in the Firebase Test Lab, add any of these steps before the **Firebase Test Lab for Android** step and take note of the output path of these steps. You will need this environment variable for testing configuration.

## Input Variables

For each component, specific input variables are required for its operation on your system. The input variables necessary for the **Android Build for UI Testing** are as follows:

<Screenshot url='https://cdn.appcircle.io/docs/assets/firebasetestlab-android-firebase-workflow.png' />

| Variable Name             | Description                                        | Status   |
|---------------------------|----------------------------------------------------|----------|
| `$AC_FIREBASE_PROJECT_ID` | Specifies the name of the Firebase project created. | Optional |
| `$AC_FIREBASE_KEY_FILE`   | Specifies the name of the key file uploaded as an environment variable (`$` is required before the key name). | Optional |
| `$AC_FIREBASE_TEST_TYPE`  | Specifies the test type. `robo` and `instrumentation` are supported. | Required |
| `$AC_FIREBASE_BUCKET_NAME`| Specifies the bucket name to store the test results in a Google Cloud Storage bucket. | Optional |
| `$AC_APK_PATH`            | The default value is the APK produced by the **Android Build** or **Android Build for UI Testing** step. You can specify a different environment variable to use the APK files produced in other steps. | Optional |
| `$AC_TEST_APK_PATH`       | Specify the environment variable as the path of the APK build for UI testing. The default value is the APK produced by the **Android Build for UI Testing** step. | Optional |
| `$AC_FIREBASE_EXTRA_ARGS` | Firebase Test Extra Arguments `(e.g., --timeout=3m)`. For further configuration of the test run, please refer to the [Google Cloud CLI](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run) documentation. | Optional |

Once everything is set up, press save to save your step configuration. Then you can configure and run your build just like any other app.

## Output Variables

This step does not produce any output as a variable. However, after your build is done, you can view the results of the **Firebase Test Lab for Android** step in the build logs.

<Screenshot url='https://cdn.appcircle.io/docs/assets/firebasetestlab-android-test-result.png' />

The full details of the tests are accessible in the [Firebase console](https://console.firebase.google.com) and in your Google Cloud Storage bucket for analysis.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (63).png' />

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-android-firebase-test-lab-component