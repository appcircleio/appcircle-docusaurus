---
title: Send Email
sidebar_label: Send Email
description: Allows you to send customized emails from Publish Flow steps.
tags: [send email, publish]
---

import Screenshot from '@site/src/components/Screenshot';
import RunnerUsage from '@site/docs/\_publish-steps-runner-usage-caution.mdx';

# Send Email

The **Send Email** step allows you to send customized email notifications during your Appcircle Publish Flow for both iOS and Android builds. This can be used to alert stakeholders, notify of publish statuses, or provide deployment-related information.

<RunnerUsage />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6186-email1.png' />

## Configuration Options

To be able to send email in your publish flow, you need to configure the fields listed below. These settings define how the email is sent, including the SMTP server, sender details, recipients, and the email content. Make sure the credentials and connection details match your email service provider’s requirements.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6186-email2.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6186-email3.png' />

| Field                      | Description                                                                                                                                                   |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Mail Host**             | Domain or IP address of the SMTP server (e.g., `smtp.gmail.com`).                                                                                              |
| **Mail Port**             | Port number of the SMTP server. Common values: `465` (SSL) or `587` (TLS).                                                                                     |
| **SMTP Username**         | Email address used for SMTP login.                                                                                                                             |
| **SMTP Password**         | Password or app-specific password for the SMTP account.                                                                                                        |
| **From**                  | Sender information in the format: `Name <email@example.com>`.                                                                                                  |
| **To**                    | Comma-separated list of recipient email addresses.                                                                                                             |
| **Subject**               | Subject of the email. Environment variables (e.g., `$AC_BUILD_NUMBER`) can be used.                                                                            |
| **Use TLS**               | Set to `true` to use TLS (if supported by the provider).                                                                                                       |
| **Use SSL**               | Set to `true` to use SSL (if supported by the provider).                                                                                                       |
| **Use Authentication**    | Set to `true` if authentication is required by the SMTP server.                                                                                                |
| **Email Provider Account**| Email provider configuration key (e.g., `gmail`).                                                                                                              |
| **Email Content**         | Body content of the email. Plain text or HTML. Environment variables can be used.                                                                              |

### Example Configuration (Gmail)

| Field                    | Value                                                                 |
|-------------------------|-----------------------------------------------------------------------|
| **Mail Host**           | `smtp.gmail.com`                                                      |
| **Mail Port**           | `465`                                                                 |
| **SMTP Username**       | `youremail@gmail.com`                                                 |
| **SMTP Password**       | App-specific password generated via Google account                   |
| **From**                | `Your Name <youremail@gmail.com>`                                    |
| **To**                  | `qa@example.com,pm@example.com`                                       |
| **Subject**             | `Build $AC_BUILD_NUMBER completed for $AC_PROJECT_NAME`              |
| **Use TLS**             | `true`                                                                |
| **Use SSL**             | `true`                                                                |
| **Use Authentication**  | `true`                                                                |
| **Email Provider Account** | `gmail`                                                            |
| **Email Content**       | `Hello Team, the build $AC_BUILD_NUMBER for $AC_PROJECT_NAME is done.`|

## Using Environment Variables

You can dynamically populate subject and content using environment variables. They can also be used to securely fill your email settings.

### Creating Environment Variables

First, you need to define the environment variables. To do this, go to the Publish module and select Publish Variables. From there, you can start creating the variables for your email settings.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6186-email6.png' />


For more information, please refer to the [Publish Variables](/publish-module/publish-variables) documentation.

### Selecting Environment Variables

After creating the environment variables, you will need to select this variable group from your profile settings.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6186-email5.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6186-email4.png' />

You can now use the defined environment variables in your email settings, including the subject and content. For example:

```text
Subject:
Build $AC_BUILD_NUMBER for $AC_PROJECT_NAME is Ready

Email Content:
Hi team,

A new build for $AC_PROJECT_NAME (Build #$AC_BUILD_NUMBER) has been successfully published.

Best,
Appcircle CI/CD
```