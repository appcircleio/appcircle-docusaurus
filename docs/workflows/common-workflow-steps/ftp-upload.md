---
title: FTP Upload
description: Streamline your file transfers with FTP Upload. Secure, fast, and reliable FTP solutions to enhance your data management and operational efficiency.
tags: [file, transfer, secure, fast, upload file]
sidebar_position: 4
---


import Screenshot from '@site/src/components/Screenshot';

# FTP Upload

With Appcircle's FTP Upload (File Transfer Protocol) integration, you can easily upload any file generated within the pipeline to your desired FTP server.

### Prerequisites

:::info

There are no prerequisites for this step. It should be used following the step where the artifact is produced. For instance, as shown in the screenshot below, it is used immediately after the [**Xcodebuild for Devices**](/workflows/ios-specific-workflow-steps/xcodebuild-for-devices) step. This sequence is arranged to send the `IPA` file produced in the pipeline to any **FTP server**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3153-ftpOrder.png' />

:::


:::caution

Please note that in order to send a file to an **FTP server**, the file must have been generated within the pipeline. This means that you need to use this step after the step where the desired file is produced. Otherwise, the **FTP Upload** step will **fail** to find the file and will result in an error.

:::


### Input Variables

Below is a list of input variables that can be used with this component, with a description of each.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3153-ftpInput.png' />

:::warning

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

