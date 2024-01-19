---
title: Using Firebase Test Lab for Android Continuous Testing
metaTitle: Using Firebase Test Lab for Android Continuous Testing
metaDescription: Using Firebase Test Lab for Android Continuous Testing
sidebar_position: 4
---

import Screenshot from '@site/src/components/Screenshot';

# Using Firebase Test Lab for Android Continuous Testing

Appcircle is integrated with Firebase Test Lab for continuous testing. You can build your app in Appcircle and deploy it directly to the Firebase Test Lab to run automated tests.

### Setting Up a Firebase Project and a Service Account

To start with the [Firebase Test Lab](https://firebase.google.com/products/test-lab), you need to have an associated Firebase Project, which is created in the [Firebase console](https://console.firebase.google.com). Go to the console, press the "Add Project" button and specify the project name and the other settings:

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (45).png' />

After your project is created, go to the [Google Cloud Platform console](https://console.cloud.google.com/iam-admin/serviceaccounts/) to create a service account. Press the "Create Service Account" button and follow the prompts to create a service account with the **Editor** role:

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (49).png' />

Once the service account is created, click on the three dot menu next to the service account and press "Create Key".

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (50).png' />

Select the key format as "JSON" and download the created key. We will be using this key for Appcircle to be able to deploy apps to Firebase Test Lab.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (51).png' />

As the final step, go to the [Google Developers Console API Library page](https://console.developers.google.com/apis/library) and find and enable the following APIs:

- Google Cloud Testing API
- Cloud Tool Results API.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (61).png' />

### Firebase Test Lab Authentication Configuration in Appcircle

To start, go to the environment variables section and add the service account JSON key created in the previous step as a [new environment variable](../environment-variables/managing-variables.md#creating-environment-variable-groups). Take a note of the variable name, which will be necessary in the workflow configuration.

<Screenshot url='https://cdn.appcircle.io/docs/assets/firebasetestlab-environment.png' />

Then [select the related environment variable group](../environment-variables/managing-variables.md#using-environment-variable-groups-in-builds) in the build configuration of the project that will be using Firebase Test Lab.

<Screenshot url='https://cdn.appcircle.io/docs/assets/firebasetestlab-config-env-select.png' />

### Build Workflow Configuration for Firebase Test Lab

To utilize Firebase Test Lab in your builds, open the [workflow editor](../workflows/why-to-use-workflows.md) and add the "Firebase Test Lab for Android" step after the build or sign steps. If you want to run instrumentation tests, also add the "Android Build for UI Testing" step before the Firebase Test Lab step.

:::caution

If you want to run **robo** test, it is highly recommended to not add **Android Build for UI Testing** step.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/firebasetestlab-workflow-select.png' />

If you want to use the UI Test Build output or the Signed Build output in Firebase Test Lab, add any of these steps before the Firebase Test Lab step and take a note of the output path of these steps. You will need this environment variable for testing configuration.

<Screenshot url='https://cdn.appcircle.io/docs/assets/firebasetestlab-ui-test-workflow.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/firebasetestlab-android-sign-workflow.png' />

Before the build, the last task is to configure the Firebase Test Lab for Android step:

- **Project ID: **Enter the name of the Firebase project created
- **Key File:** Enter the name of the key file uploaded as an environment variable ($ is required before the key name).
- **Test Type: **Select a test type. `robo` and `instrumentation` are supported.
- **Bucket Name: **Enter a bucket name to store the test results in a Google Cloud Storage bucket.
- **APK Path: **The default value is the APK produced by the "Android Build" step. You can specify a different environment variable to use the APK files produced in other steps.
- **Test APK Path: **Specify the environment variable to the path of the APK build for UI testing
- **Extra Arguments: **For further configuration of the test run. Please refer to the [Google Cloud CLI Documentation](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run).

Once everything is set up, press save to save your step configuration. Then you can configure and run your build just like any other app.

<Screenshot url='https://cdn.appcircle.io/docs/assets/firebasetestlab-android-firebase-workflow.png' />

### Viewing the Firebase Test Lab Step Results

Once your build is done, you can view the results of the Firebase Test Lab step in the build logs.

<Screenshot url='https://cdn.appcircle.io/docs/assets/firebasetestlab-android-test-result.png' />

The full details of the tests are accessible in the [Firebase console](https://console.firebase.google.com) and in your Google Cloud Storage bucket for analysis.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (63).png' />
