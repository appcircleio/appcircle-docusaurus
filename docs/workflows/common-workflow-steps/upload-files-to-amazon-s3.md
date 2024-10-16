---
title: Upload Files to Amazon S3
description: Learn how to upload files to Amazon S3 with Appcircle. Streamline your storage and backup processes for app development.
tags: [build, test, upload, amazon, workflow, step]
---

import Screenshot from '@site/src/components/Screenshot';

# Upload Files to Amazon S3

[Amazon Simple Storage Service (S3)](https://aws.amazon.com/s3/) is an object storage service provided by AWS, utilized for storing build artifacts across diverse use cases.

The **Upload Files to Amazon S3** step in Appcircle enables direct uploading of any file or folder to the designated Amazon S3 bucket during the build process.

### Prerequisites

There are no prerequisites required before using the **Upload Files to Amazon S3** step.

To begin, add the **Upload Files to Amazon S3** step to the workflow from the [workflow marketplace](/workflows/#workflow-marketplace). You can incorporate it at any point within the workflow and multiple times, as necessary, to upload specific files or folders. For example, you can place it after the build step to deploy the build outputs.

<Screenshot url='https://cdn.appcircle.io/docs/assets/s3-workflow-ios.png' />

Once added, exit the workflow edit mode by saving your changes, and then click on the **Upload Files to Amazon S3** step.

### Input Variables

Below is a table containing all the parameters required for the **Upload Files to Amazon S3** step, along with detailed descriptions:

<Screenshot url='https://cdn.appcircle.io/docs/assets/s3-workflow-details.png' />

| Variable Name           | Description                                      | Status    |
|-------------------------|--------------------------------------------------|-----------|
| `$AC_INPUT_FILE_PATH`   | Specifies the file or folder name to be uploaded to S3. You can provide the full path or the output of another step as an environment variable (e.g., `$AC_ARCHIVE_PATH` allows you to upload the output of the **Xcode Build for Devices** step). | Required  |
| `$AWS_ACCESS_KEY_ID`    | Specifies the AWS access key ID. [For more information, refer here](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys). | Required  |
| `$AWS_SECRET_ACCESS_KEY`| Specifies the secret access key associated with the entered ID. [For more information, refer here](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys). | Required  |
| `$AWS_BUCKET_NAME`      | Specifies the S3 bucket name as the deployment target. | Required  |
| `$AWS_BUCKET_REGION`    | Specifies the AWS region where the specified bucket resides. You can find the [endpoint codes for the regions here](https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints). The default value is `us-east-1`. | Optional  |
| `$AWS_TARGET_DIR`       | Specifies the Amazon S3 folder path in the bucket. By default, it selects the date (`Y-m-d-H-M-S`) as the folder. | Optional  |

:::info

It is highly recommended to add the keys as [secret environment variables](../../.././environment-variables/managing-variables) instead of typing them here for security purposes.

:::

### Output Variables

As the output may vary depending on the task you execute, there is no specific output defined by default.

| Output Variable         | Description                                                    |
|-------------------------|----------------------------------------------------------------|
| `$AC_AWS_UPLOAD_URL`    | Specifies that the files and folders are deployed to a newly created directory as `s3://bucket-name/timestamp` to avoid any conflicts and potential overwrites. |

After saving your settings, the build can be run, and the step will be executed accordingly. Details of the upload operation can be viewed in the build logs:

<Screenshot url='https://cdn.appcircle.io/docs/assets/s3-workflow-ios-upload.png' />

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-file-upload-to-amazon-s3