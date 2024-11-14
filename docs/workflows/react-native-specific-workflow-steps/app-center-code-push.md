---
title: App Center CodePush
description: Effortlessly update apps with App Center Code Push. Learn quick, reliable code deployment without app store delays.
tags: [react native, mobile, workflow, step, code push, app center]
---

import Screenshot from '@site/src/components/Screenshot';

# App Center CodePush

[**App Center CodePush**](https://learn.microsoft.com/en-us/appcenter/distribution/codepush/) is an App Center cloud service that enables React Native developers to deploy mobile app updates directly to their users’ devices. It works by acting as a central repository where developers can publish certain updates (for example, JS, HTML, CSS, and image changes), and apps can query for updates (using the provided client SDKs).

You can seamlessly integrate **App Center CodePush** into your workflow with Appcircle, facilitating easy setup and utilization within your existing development processes.

### Prerequisites

Before running the **App Center CodePush** step, you must complete certain prerequisites, as detailed in the table below:

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [**Git Clone**](/workflows/common-workflow-steps/git-clone) | The repository needs to be cloned to begin the CodePush process. After this step, the variable `AC_REPOSITORY_DIR` will be set. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3174-codepushOrder.png' />

### Input Variables

This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3174-codepushInput.png' />

:::danger

Avoid hard-coding sensitive information, like tokens and API keys, directly into the step parameters.

We recommend using [**Environment Variables**](/environment-variables/managing-variables) groups for such sensitive variables.

:::


| Variable Name                 | Description                                    | Status           |
|-------------------------------|------------------------------------------------|------------------|
| `$AC_APPCENTER_TOKEN`         | App Center API Token. | Required |
| `$AC_APPCENTER_PRIVATE_KEY`   | App Center Private Key to sign updates. Upload your private key (.pem) to environment variables as a file and set its name as `AC_APPCENTER_PRIVATE_KEY`. | Optional |
| `$AC_PROJECT_PATH`            | Relative path of the React Native project. Leave it empty to use the parent repository path. | Optional |
| `$AC_APPCENTER_OWNER`         | Owner of the app. The app's owner can be identified in its URL, such as `https://appcenter.ms/users/JohnDoe/apps/myapp` for a user-owned app (where **JohnDoe** is the owner) and `https://appcenter.ms/orgs/Appcircle/apps/myapp` for an org-owned app (owner is **Appcircle**). | Required |
| `$AC_APPCENTER_APPNAME`       | The name of the app. The app's name can be identified in its URL, such as `https://appcenter.ms/users/JohnDoe/apps/myapp` for a user-owned app (where **myapp** is the app name) and `https://appcenter.ms/orgs/Appcircle/apps/myapp` for an org-owned app (owner is **myapp**). | Required |
| `$AC_APPCENTER_DESCRIPTION`   | This parameter provides an optional change log for the deployment. | Required |
| `$AC_APPCENTER_DEPLOYMENT`    | This parameter specifies which deployment you want to release the update to. It defaults to `Staging`. | Optional |
| `$AC_APPCENTER_ROLLOUT`       | This parameter specifies the percentage of users (as an integer between 1 and 100) that should be eligible to receive this update. | Optional |
| `$AC_APPCENTER_VERSION`       | The latest version will be used if no version is set. | Optional |
| `$AC_APPCENTER_EXTRA`         | Extra command line arguments for appcenter. For example, add `--debug` for verbose logs. | Optional |


---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcenter-codepush-component
