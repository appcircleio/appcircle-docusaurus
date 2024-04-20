---
title: Danger
description: Streamline your code review process with Danger. Automate checks and enforce code standards pre-merge to maintain high-quality software.
tags: [code review, quality assurance, automaiton, development tools, appcircle, mobile ci/cd]
sidebar_position: 4
---


import Screenshot from '@site/src/components/Screenshot';

# Danger

[Danger](https://danger.systems/ruby/) is a CI tool that allows you to automate code review. It not only helps code reviewers but also the developers who send pull requests. The reviewer spends less time doing chores and more time efficiently reviewing the code.

PRs opened can be easily automated with Appcircle's Danger integration.

For detailed information on the benefits that Danger, please refer to the following blog post:

https://appcircle.io/blog/danger-in-ci-automate-your-mobile-code-reviews

:::warning

This tool does not support AzureDevOps. Therefore, if your repository is hosted on AzureDevOps, this tool will not function. Please use the [**Azure Bot for Swiftlint**](/workflows/ios-specific-workflow-steps/azure-bot-for-swiftlint)(for iOS) and [**Azure Bot for Detekt Report**](/workflows/android-specific-workflow-steps/azure-bot-for-detekt-report)(for Android)  components instead.

:::

### Prerequisites

The workflow steps that need to be executed before running the **Danger** step vary depending on the platform and are listed below:

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [Git Clone](/workflows/common-workflow-steps/git-clone) | The repository needs to be cloned to begin the badge-adding process. After this step, the variable `AC_REPOSITORY_DIR` will be set. |

:::caution

Please note that this component works in synchronization with the [**Appcircle Triggers**](/build/build-process-management/build-manually-or-with-triggers/#managing-triggers-for-builds). If a trigger is not set up, the pipeline will not be triggered when a PR is opened, and therefore, Danger will not function.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3062-dangerOrder.png' />

### Input Variables

Below is a list of input variables that can be used with this component with a description of each.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3062-dangerInput.png' />

:::warning

Avoid hard-coding sensitive information like tokens and API keys directly into the step parameters.

We recommend using [**Environment Variables**](/environment-variables/managing-variables) groups for such sensitive variables.

:::

| Variable Name                             | Description                                                                                                                                    | Status   |
|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| `$AC_REPOSITORY_DIR`                      | Specifies the cloned repository directory. This path will be generated after the [Git Clone](/workflows/common-workflow-steps/git-clone) step. | Required |
| `$AC_DANGER_PATH`                         | Specifies path of Dangerfile. This path comes from `AC_REPOSITORY_DIR`. If DangerFile is in main directory of your repository. Do not change.  | Required |
| `$AC_DANGER_EXTRA_PARAMETERS`             | Extra command line parameters. For Example: enter `--verbose` for verbose mode.                                                                | Optional |
| `$DANGER_GITHUB_API_TOKEN`                | Github Access Token for the bot user.                                                                                                          | Optional |
| `$DANGER_GITHUB_HOST`                     | The host that GitHub is running on. For example: `git.corp.com`                                                                                | Optional |
| `$DANGER_GITHUB_API_BASE_URL`             | The host that the GitHub Enterprise API is reachable on. For example: `https://git.corp.com/api/v3`                                            | Optional |
| `$DANGER_GITLAB_API_TOKEN`                | GitLab Access Token for the bot user.                                                                                                          | Optional |
| `$DANGER_GITLAB_HOST`                     | The host that GitLab is running on. For example: `git.corp.com`                                                                                | Optional |
| `$DANGER_GITLAB_API_BASE_URL`             | The host that the GitHub Enterprise API is reachable on. For example: `https://git.corp.com/api/v4`                                            | Optional |
| `$DANGER_BITBUCKETCLOUD_USERNAME`         | Bitbucket username for the bot user.                                                                                                           | Optional |
| `$DANGER_BITBUCKETCLOUD_PASSWORD`         | Bitbucket password for the bot user.                                                                                                           | Optional |
| `$DANGER_BITBUCKETCLOUD_UUID`             | Bitbucket UUID of the bot user.                                                                                                                | Optional |
| `$DANGER_BITBUCKETSERVER_USERNAME`        | Bitbucket username for the bot user.                                                                                                           | Optional |
| `$DANGER_BITBUCKETSERVER_PASSWORD`        | Bitbucket password for the bot user.                                                                                                           | Optional |
| `$DANGER_BITBUCKETSERVER_HOST`            | The host that Bitbucket is running on. For example: `git.corp.com`                                                                             | Optional |


To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-danger-component
