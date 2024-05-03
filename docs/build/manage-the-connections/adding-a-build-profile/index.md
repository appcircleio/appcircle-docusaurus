---
title: Adding a Build Profile & Connecting a Repository
description: Learn how to add a build profile and connect a repository in Appcircle
tags: [build profile, connection, repository]
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';

# Adding a Build Profile & Connecting a Repository

New to Appcircle Build module? Follow our quick start guide to build your iOS and Android apps in the cloud.

The Build Module allows you to streamline and automate your mobile app build flows.

:::info

The Build Module is the first step to automate your CI/CD processes via Appcircle.

:::

## Create a build profile (app)

A build profile is an app that you can build in a target OS and framework.

To create your first build profile, click on the orange "Add New" button on the top left of the screen.

<Screenshot url='https://cdn.appcircle.io/docs/assets/adding-a-build-profile.png' />

Enter a name for your build profile and select the target operating system (iOS or Android) and target platform.

<Screenshot url='https://cdn.appcircle.io/docs/assets/adding-build-profile-ios-connection-new.png' />

## Connect your repository

You can connect GitHub through a GitHub app or Bitbucket and GitLab repositories to your build profile through OAuth apps. Alternatively, You can connect private repositories through SSH and public repositories directly on GitHub, Bitbucket, GitLab, and other compatible git providers such as Azure DevOps and AWS CodeCommit. ([Please refer here for more information on AWS CodeCommit connections.](/troubleshooting-faq/common-issues#how-to-connect-to-aws-codecommit-repositories-through-ssh))

You can also connect to your Self Hosted Bitbucket and GitLab account directly within Appcircle.

If you authorize Appcircle to connect to your Github, BitBucket, or GitLab account, you can auto-build your project with hooks, get build statuses and the full list of commits. If you connect to a repository through SSH or through a public URL, you need to [set up webhooks manually](/build/build-process-management/build-manually-or-with-triggers#setting-up-manual-webhooks-for-ssh-and-public-repositories).

To test drive Appcircle, you can find various sample projects in the [Appcircle GitHub page](https://github.com/appcircleio?q=sample) or you can just press on the **Quick start using the sample repository** button to populate the repository URL field with a compatible project based on the selected framework.

<Screenshot url='https://cdn.appcircle.io/docs/assets/adding-a-build-profile-connection.png' />

When the "Autofill" toggle is activated on the **Select Repository** popup, Appcircle will try to create a default configuration using the selected repository and fill in the necessary fields.

<Screenshot url='https://cdn.appcircle.io/docs/assets/autofill.png' />

:::caution
When you have exceeded the build limit of your plan, Appcircle will not be able to **Autofill** your build profile, although you activated the toggle.
:::

Refer to the relative documents under this page about the connections and differences between connection types:

- [Connect to GitHub](/build/manage-the-connections/adding-a-build-profile/connecting-to-github)
- [Connect to Bitbucket](/build/manage-the-connections/adding-a-build-profile/connecting-to-bitbucket)
- [Connect to GitLab](/build/manage-the-connections/adding-a-build-profile/connecting-to-gitlab)
- [Connect to Private Repository via SSH Key](/build/manage-the-connections/adding-a-build-profile/connecting-to-private-repository-via-ssh)
- [Connect to Public Repository](/build/manage-the-connections/adding-a-build-profile/connecting-to-public-repository)

## View the newly created build profile

You will see your build profile once it has been created. Click on the build profile to connect a repository and fetch your code to Appcircle.

Appcircle will then pull your branches, commits, and other information from your repository.

<Screenshot url='https://cdn.appcircle.io/docs/assets/adding-a-build-profile-aftermath.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/adding-a-build-profile-inside.png' />

### Delete a Build Profile

In order to delete a build, simply click on the Three Dot and click delete.

<Screenshot url='https://cdn.appcircle.io/docs/assets/build-profile-delete-box.png' />

After the prompt, the profile will be deleted.

In order to free up storage in your organization, you should also remove the other references pointing to the artifact. In example, if you have the same artifact on the testing distribution, you should also delete those artifacts as well.

Is your artifact storage full? Learn more about freeing up space [here](/troubleshooting-faq/common-issues#artifact-storage-is-full).

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />
