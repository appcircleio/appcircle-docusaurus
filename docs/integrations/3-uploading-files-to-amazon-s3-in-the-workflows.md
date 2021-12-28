---
title: 'Uploading Files to Amazon S3 with the Workflows'
metaTitle: 'Uploading Files to Amazon S3 with the Workflows'
metaDescription: 'Uploading Files to Amazon S3 with the Workflows'
---

# Uploading Files to Amazon S3 with the Workflows

Amazon Simple Storage Service (S3) is an object storage service provided by AWS. It can be used to store build artifacts for various use cases.

With the "File Upload to Amazon S3" step in Appcircle, you can directly upload any file or folder during the build to the specified Amazon S3 bucket.

To start, add the "File Upload to Amazon S3" step to the workflow from the [workflow marketplace](../workflows/why-to-use-workflows#workflow-marketplace). You can add it anywhere within the workflow and multiple times as needed to upload specific files or folders. For instance, you can add it after the build step to deploy the build outputs.

![](<https://cdn.appcircle.io/docs/assets/image (81).png>)

Once added, press save to exit the workflow edit mode and click on the Amazon S3 step.

The input values are as follows:

- AWS Input File Path: This is the file/folder name to be uploaded to S3. You can specify the full path or you can specify the output of another step an environment variable. (e.g. \_$AC_ARCHIVE_PATH \_allows you to upload the output of the Xcode Build for Devices step)
- AWS Access Key ID: Enter the AWS access key ID. [For more information, you can refer here.](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys)
- AWS Secret Access Key: Enter the secret access key associated with the ID entered above. [For more information, you can refer here.](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys)
- AWS Bucket Name: Enter the S3 bucket name as the deployment target.
- AWS Bucket Region: Enter the AWS region where the specified bucket resides. You can find the [endpoint codes for the regions here](https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints).

:::info

It is highly recommended to add the keys as [secret environment variables](../environment-variables/managing-variables) instead of typing them here for security purposes.

:::

As for the output, the specified files and the folders are deployed to a newly created directory as `s3://bucket-name/timestamp` to avoid any conflicts and potential overwrites.

![](<https://cdn.appcircle.io/docs/assets/image (82).png>)

After you save your settings, you can run the build and the step will be executed accordingly. You can view the details of the upload operation in the build logs:

![](<https://cdn.appcircle.io/docs/assets/image (83).png>)
