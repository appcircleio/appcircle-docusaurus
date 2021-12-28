---
title: 'Using AWS Device Farm for iOS and Android Continuous Testing'
metaTitle: 'Using AWS Device Farm for iOS and Android Continuous Testing'
metaDescription: 'Using AWS Device Farm for iOS and Android Continuous Testing'
---

# Using AWS Device Farm for iOS and Android Continuous Testing

AWS Device Farm is an application testing service that enables you to run your tests concurrently on multiple mobile devices to speed up the execution of your tests and generates videos and logs to help you quickly identify issues with your app.

Appcircle is integrated with AWS Device Farm for continuous testing. You can build your app in Appcircle and deploy it directly to AWS Device Farm to run automated tests.

With the "AWS Device Farm Deploy and Run" step in Appcircle, you can directly deploy your binaries and test scripts during the build to the specified AWS Device Farm project and run tests.

To start, you need to add the

- "Android Build for UI Testing" step for Android
- "Xcodebuild Build for Testing" step for iOS

followed by the "AWS Device Farm Deploy and Run" step to the workflow from the [workflow marketplace](../workflows/why-to-use-workflows#workflow-marketplace).

If you just want to run tests, you can also remove other build steps such as "Android Build" or "Xcodebuild for Devices".

![Android workflow for AWS Device Farm](<https://cdn.appcircle.io/docs/assets/image (102).png>)

![iOS workflow for AWS Device Farm](<https://cdn.appcircle.io/docs/assets/image (103).png>)

Once these steps are added, press save to exit the workflow edit mode and click on the AWS Device Farm step.

The input values are as follows:

- AWS Access Key ID: Enter the AWS access key ID. [For more information, you can refer here.](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys)
- AWS Secret Access Key: Enter the secret access key associated with the ID entered above. [For more information, you can refer here.](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys)
- AWS Default Region: Enter the AWS region where for the run. [You can find the endpoint codes for the regions here.](https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints)

:::info

It is highly recommended to add the keys as [secret environment variables](../environment-variables/managing-variables) instead of typing them here for security purposes.

:::

- AWS Project ARN: The ARN of the project for deploy and run. ([see below](using-aws-device-farm-for-ios-and-android-continuous-testing#how-to-get-the-arn-values))
- AWS Device Pool Arn: The ARN of the device pool for the run. ([see below](using-aws-device-farm-for-ios-and-android-continuous-testing#how-to-get-the-arn-values))
- AWS Device Farm Run Name Prefix: The name prefix for the run to be scheduled. AWS Device Farm Run Test Type: The type of the test for the run.
- AWS Device Farm File Upload Time Out: Time out duration (seconds) for the test file upload. The step is skipped if the time out is reached.
- Maximum Waiting Time for Run Test Results: Time out duration (seconds) for the AWS Device Farm run. The step is skipped if this duration is reached, but the test execution continues in AWS Device Farm.
- AWS Device Farm App ARN: The ARN of the application package to run tests against, created with CreateUpload. If you don't set this parameter, the subsequent App Upload File Name, App Upload Type and App Upload File Path parameters are required.
- AWS Device Farm App Upload File Name: The file to be uploaded. The name should not contain any forward slashes (/ ). If you are uploading an iOS app, the file must have an .ipa extension. If you are uploading an Android app, the file must have an .apk extension.
- AWS Device Farm App Upload Type: The upload type of the file.
- AWS Device Farm App Upload File Path: The file path for the app upload.
- AWS Device Farm Test ARN: The ARN of the uploaded test to be run. If you don't set this parameter, the subsequent Test Upload File Name, Test Upload Type and Test Upload File Path parameters are required.
- AWS Device Farm Test Upload File Name: The test file to be uploaded. The file must have a .zip extension.
- AWS Device Farm Test Upload Type: The upload type of the test.
- AWS Device Farm Test Upload File Path: The file path for the test upload.
- AWS Test Spec ARN: The ARN of the uploaded test spec to be run.
- AWS Test Spec Upload File Name: The test spec file to be uploaded.
- AWS Test Spec Upload Type: The upload type of the test spec.
- AWS Test Spec Upload File Path:The file path for the test spec upload.

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

![](<https://cdn.appcircle.io/docs/assets/image (105).png>)

The full details of the tests are accessible in the [AWS Device Farm console](https://console.aws.amazon.com/devicefarm/).

![](<https://cdn.appcircle.io/docs/assets/image (104).png>)
