---
title: FTP Upload
description: Streamline your file transfers with FTP Upload. Secure, fast, and reliable FTP solutions to enhance your data management and operational efficiency.
tags: [file, transfer, secure, fast, upload file]
---


import Screenshot from '@site/src/components/Screenshot';

# FTP Upload

Appcircle's FTP Upload (File Transfer Protocol) integration lets you easily upload any file generated within the pipeline to your chosen FTP server.

### Prerequisites

:::info

This step has no prerequisites but must follow the artifact production step. For example, as the screenshot below demonstrates, use it right after the [**Xcodebuild for Devices**](/workflows/ios-specific-workflow-steps/xcodebuild-for-devices) step. This setup ensures the IPA file produced in the pipeline is sent to any **FTP server**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3153-ftpOrder.png' />

:::


:::caution

Note that to send a file to an **FTP server**, the file must be generated within the pipeline. Therefore, deploy this step only after the file production step. Failing to do so means the **FTP Upload** step cannot find the file, resulting in an error.

:::


### Input Variables

Below is a list of input variables that can be used with this component, with a description of each.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3153-ftpInput.png' />

:::danger

Avoid hard-coding sensitive information, like tokens and API keys directly into the step parameters.

We recommend using [**Environment Variables**](/environment-variables/managing-variables) groups for such sensitive variables.

:::

| Variable Name                 | Description                                                                                                                              | Status    |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| `$AC_FTP_HOST`                | Hostname of the FTP server. For example: `ftp.example.com:21`                                                                            | Required  |
| `$AC_FTP_USER`                | FTP server username.                                                                                                                     | Required  |
| `$AC_FTP_PASS`                | FTP server password.                                                                                                                     | Required  |
| `$AC_FTP_SOURCE`              | Source file or path to upload. For example: the file path can be set to `$AC_OUTPUT_DIR/Myapp.ipa`. Ensure that the file name is correct.| Required  |
| `$AC_FTP_TARGET`              | The target path is on the FTP server.                                                                                                           | Required  |



To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-ftp-upload-component

