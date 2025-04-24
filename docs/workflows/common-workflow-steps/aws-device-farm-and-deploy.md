---
title: AWS Device Farm and Deploy
description: AWS Device Farm is an application testing service that enables you to run your tests concurrently on multiple mobile devices to speed up the execution of your tests and generates videos and logs to help you quickly identify issues with your app.
tags: [android, ios, mobile, testing, aws, device]
---

import Screenshot from '@site/src/components/Screenshot';

# AWS Device Farm and Deploy

[AWS Device Farm](https://aws.amazon.com/device-farm/) is an application testing service that enables you to run your tests concurrently on multiple mobile devices to speed up the execution of your tests and generates videos and logs to help you quickly identify issues with your app.

Appcircle is integrated with the AWS Device Farm for continuous testing. You can build your app in Appcircle and deploy it directly to AWS Device Farm to run automated tests.

With the **AWS Device Farm Deploy and Run** step in Appcircle, you can directly deploy your binaries and test scripts during the build to the specified AWS Device Farm project and run tests.

The full details of the tests are accessible in the [AWS Device Farm console](https://console.aws.amazon.com/devicefarm/).

### Prerequisites

Before running the **AWS Device Farm and Deploy** step, you must complete certain prerequisites, as detailed in the table below:

:::caution

Pay attention to the dependent step on whichever platform you are working on.

:::

| Prerequisite Workflow Step                                                                                                            | Description                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [**Android Build for UI Testing**](/workflows/android-specific-workflow-steps/android-build-for-ui-testing)      | This step is tailored to build your Android test application using Gradle Wrapper (gradlew) for the designated architectures outlined in your project. |
| [**Xcodebuild Build for Testing**](/workflows/ios-specific-workflow-steps/xcodebuild-for-testing) | This step builds your application and generates an IPA for testing so that it can be used in test automation frameworks.                                                                    |

#### For iOS

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3049-awsiosOrder.png' />

#### For Android

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3049-awsandroidOrder.png' />

### Input Variables

This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3049-awsInput.png' />

:::danger Sensitive Variables

Please do not use sensitive variables such as **Username**, **Password**, **API Key**, or **Personal Access Key** directly within the step.

We recommend using [**Environment Variables**](/build/build-environment-variables) groups for such sensitive variables.

:::

| Variable Name                     | Description                                                                                                                                                                                                                            | Status   |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `$AWS_ACCESS_KEY_ID`              | AWS Access Key ID. Please follow the [**AWS documentation**](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html#access-keys-and-secret-access-keys).                                                                 | Required |
| `$AWS_SECRET_ACCESS_KEY`          | AWS Secret Access Key. Please follow the [**AWS documentation**](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html#access-keys-and-secret-access-keys)                                                              | Required |
| `$AWS_DEFAULT_REGION`             | AWS Default Region. The default value is `us-west-2`. For more information, please visit this [documentation](https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints).                                            | Optional |
| `$AWS_PROJECT_ARN`                | The ARN of the project for deploy and run.                                                                                                                                                                                             | Required |
| `$AWS_DEVICE_POOL_ARN`            | The ARN of the device pool for the run.                                                                                                                                                                                                | Required |
| `$AWS_SCHEDULE_RUN_NAME_PREFIX`   | The name prefix for the run to be scheduled.                                                                                                                                                                                           | Required |
| `$AWS_SCHEDULE_TEST_TYPE`         | The type of the test for the run. Enter **BUILTIN_FUZZ** for sample test runs. [**See API Reference**](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_CreateUpload.html#API_CreateUpload_RequestSyntax).               | Required |
| `$AWS_UPLOAD_TIMEOUT`             | Time out duration (seconds) for the test file upload. The step is skipped if the time out is reached.                                                                                                                                  | Required |
| `$AWS_TEST_TIMEOUT`               | Time out duration (seconds) for the AWS Device Farm run. The step is skipped if this duration is reached, but the test execution continues in AWS Device Farm.                                                                         | Required |
| `$AWS_APP_ARN`                    | The ARN of the application package to run tests against, created with CreateUpload. If you don't set this parameter, the subsequent App Upload File Name, App Upload Type and App Upload File Path parameters are required.            | Optional |
| `$AWS_APP_UPLOAD_FILE_NAME`       | The file to be uploaded. The name should not contain any forward slashes (/ ). If you are uploading an iOS app, the file must have an **IPA** extension. If you are uploading an Android app, the file must have an **APK** extension. | Optional |
| `$AWS_APP_UPLOAD_TYPE`            | The upload type of the file. Enter **ANDROID_APP** or **IOS_APP** for simple APK or IPA uploads.                                                                                                                                       | Optional |
| `$AWS_APP_UPLOAD_FILE_PATH`       | The file path for the app upload. You can use predetermined environment variables like `$AC_APK_PATH`.                                                                                                                                 | Optional |
| `$AWS_TEST_ARN`                   | The ARN of the uploaded test to be run. If you don't set this parameter, the subsequent Test Upload File Name, Test Upload Type and Test Upload File Path parameters are required.                                                     | Optional |
| `$AWS_TEST_UPLOAD_FILE_NAME`      | The test file to be uploaded. The file must have a `.zip` extension.                                                                                                                                                                   | Optional |
| `$AWS_TEST_UPLOAD_TYPE`           | The upload type of the file. Enter **ANDROID_APP** or **IOS_APP** for simple APK or IPA uploads.                                                                                                                                       | Optional |
| `$AWS_TEST_UPLOAD_FILE_PATH`      | The file path for the app upload. You can use predetermined environment variables like `$AC_APK_PATH`.                                                                                                                                 | Optional |
| `$AWS_TEST_SPEC_ARN`              | The ARN of the uploaded test spec to be run.                                                                                                                                                                                           | Optional |
| `$AWS_TEST_SPEC_UPLOAD_FILE_NAME` | The test spec file to be uploaded.                                                                                                                                                                                                     | Optional |
| `$AWS_TEST_SPEC_UPLOAD_TYPE`      | The upload type of the test spec.                                                                                                                                                                                                      | Optional |
| `$AWS_TEST_SPEC_UPLOAD_FILE_PATH` | The file path for the test spec upload.                                                                                                                                                                                                | Optional |

#### How to get the ARN values

To get the ARN values, you first need to install the AWS CLI. Please refer to the guide for your operating system to install it: [https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)

Once the CLI is installed, first run the following command to list the projects and get the project ARN:

```bash
aws devicefarm list-projects
```

You can then get the ARN of the device pools of a specific project as follows. Replace `MyProjectARN` with the project ARN obtained from the previous command.

```bash
aws devicefarm list-device-pools --arn MyProjectARN
```

For the details of the other AWS Device Farm-specific parameters, please refer to the following documents:

https://docs.aws.amazon.com/cli/latest/reference/devicefarm/create-upload.html

https://docs.aws.amazon.com/cli/latest/reference/devicefarm/schedule-run.html

After you save your settings, you can run the build and the step will be executed accordingly. You can view the details of the AWS Device Farm Deploy and Run step in the build logs:

<Screenshot url='https://cdn.appcircle.io/docs/assets/aws-farm-android-workflow-result.png' />

The full details of the tests are accessible in the [AWS Device Farm console](https://console.aws.amazon.com/devicefarm/).

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (104).png' />

### Output Variables

The outputs resulting from the operation of this component are as follows:

| Variable Name                | Description                  |
| ---------------------------- | ---------------------------- |
| `AWS_RUN_ARN`               | AWS Device Farm Run ARN.     |
| `AWS_TEST_RESULT`           | AWS Device Farm Test result. |
| `AWS_OUTPUT_DEVICEPOOL_ARN` | The ARN of the Device pool.  |
| `AWS_OUTPUT_APPUPLOAD_ARN`  | The ARN of the App Upload.   |

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-aws-device-farm-deploy-and-run
