---
title: Deploying Applications to AWS Services
metaTitle: Deploying Applications to AWS Services
metaDescription: Deploying Applications to AWS Services
sidebar_position: 4
---

# Deploying Applications to AWS Services

AWS Amplify offers a fully managed service for deploying and hosting static web applications and Appcircle supports building Flutter web apps.

You can deploy Flutter web apps (or any other web app) that you build with Appcircle to AWS Amplify Console for an end-to-end app lifecycle from a single CI/CD platform for web and mobile.

To deploy apps to Amplify, you can use Git, manual uploads, or Amazon S3 buckets as the source.

Since Appcircle supports automated Amazon S3 uploads, you can automatically deploy your apps from Appcircle to Amazon S3 and then sync your S3 bucket with Amplify Console with the following steps:

- First, set up a [Flutter Web App build](../build/building-flutter-web-applications.md).
- Then, add an [Upload to Amazon S3 step to your workflow](uploading-files-to-amazon-sin-the-workflows.md) and configure it to receive the web app artifact as the input of the step.
- To set up Amplify Console and S3 sync, first go to Amplify and [set up a manual deploy](https://docs.aws.amazon.com/amplify/latest/userguide/manual-deploys.html).
- Then, follow the steps [in this AWS blog post](https://aws.amazon.com/blogs/mobile/deploy-files-s3-dropbox-amplify-console/) to automate deployments from an S3 bucket to Amplify.;

You can now build your Flutter web apps with Appcircle and deploy them to Amplify Console with end-to-end automation.
