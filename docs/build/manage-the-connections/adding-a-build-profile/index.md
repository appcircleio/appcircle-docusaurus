---
title: Adding a Build Profile & Connecting a Repository
description: Learn how to add a build profile and connect a repository in Appcircle
tags: [build profile, connection, repository, faq]
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';

# Connect your repository

You can connect GitHub through a GitHub app or Bitbucket and GitLab repositories to your build profile through OAuth apps. Alternatively, You can connect private repositories through SSH and public repositories directly on GitHub, Bitbucket, GitLab, and other compatible git providers such as Azure DevOps and AWS CodeCommit. ([Please refer here for more information on AWS CodeCommit connections.](/build/manage-the-connections/adding-a-build-profile/connecting-to-private-repository-via-ssh#how-to-connect-to-aws-codecommit-repositories-through-ssh-1))

You can also connect to your Self Hosted Bitbucket and GitLab account directly within Appcircle.

If you authorize Appcircle to connect to your Github, BitBucket, or GitLab account, you can auto-build your project with hooks, get build statuses and the full list of commits. If you connect to a repository through SSH or through a public URL, you need to [set up webhooks manually](/build/build-process-management/build-manually-or-with-triggers#setting-up-manual-webhooks-for-ssh-and-public-repositories).

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-repoconnect1.png' />

When the "Autofill" toggle is activated on the **Select Repository** popup, Appcircle will try to create a default configuration using the selected repository and fill in the necessary fields.

<Screenshot url='https://cdn.appcircle.io/docs/assets/autofill.png' />

:::caution
When you have exceeded the build limit of your plan, Appcircle will not be able to **Autofill** your build profile, although you activated the toggle.
:::

## FAQ

## Repository Connection Issues

Please note that currently only Git repositories are supported. Any third party version control repositories need to be transferred to a proper Git repository on either Github or Bitbucket.

### **How to change your connected GitHub, Bitbucket, or GitLab account?**

You will need to go to your Github, Bitbucket, or GitLab account and revoke access to Appcircle and then reconnect your account from Appcircle.

### Unable to see the repositories in the connected repository provider

Please check if you have owner/admin access in the specific organization from which the repositories will be connected. Appcircle does not allow connections to the repositories with a member-level access.

### Error accessing the repository. Please check if the repository exists or if you have the required privileges.

- Only members who have admin role on repository or are owner of the organization can install the Github App in an organization that owns that repository.
- Only members who have admin role on a repository or are owner of the organization can connect a repository to a profile.

If you still can't solve your issues, ask on our Slack page. Our community and our support engineers will help you whenever they're available:

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />
