---
title: Build Manually or Automatically with Webhooks and Triggers
metaTitle: Build Manually or Automatically with Webhooks and Triggers
metaDescription: Build Manually or Automatically with Webhooks and Triggers
sidebar_position: 11
---

# Build Manually or Automatically with Webhooks and Triggers

There are multiple ways to trigger a build in Appcircle. You can run builds manually or automate the build process with various triggers.

<iframe width="640" height="315" src="https://www.youtube.com/embed/zxxax79KD9U" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Manual Build

As the name states, your build profile will not build your application until you tell it to. You can browse branches in your Git repository and select any commit from any branch you need to build. To initiate a manual build, just press the **Build** button next to the commits under a branch.

![](<https://cdn.appcircle.io/docs/assets/image (168).png>)

### Workflows for Manual Builds

For the manual builds, the currently available push triggers apply and if no trigger is configured, the following trigger is provided by default under the [push triggers](#auto-build-on-every-push). If there are others, they may take precedence based on the [trigger priorities](#trigger-priorities).

![](https://cdn.appcircle.io/docs/assets/push-triggers.jpg)

## Automatic Build

Builds can be triggered with various triggers such as every push to the repository, pull/merge requests, or tagged pushes. This requires the following:

- Webhook connection to the repository
- Setting up build triggers

There are two options to set up webhooks for automatic builds:

- You can [authorize the Appcircle app](./adding-a-build-profile/README.md#connect-your-repository) for GitHub, Bitbucket, or GitLab repositories for direct integration. The triggers will be available for use immediately. (You can skip the next part about the webhook setup.)
- For the repository connections through SSH, you can add the specific webhook for that build profile manually to the compatible git provider. This enables the git provider to send a POST request to Appcircle for the selected events, which you can then use for triggers.

### Setting Up Manual Webhooks for SSH and Public Repositories

For repositories connected through SSH, you can set up triggers with webhooks in compatible repository providers.

When you connect a repository through SSH or through a public URL, the Webhook URL option will be enabled in the context menu of the build profile, accessible from the top of the profile details.

![](<https://cdn.appcircle.io/docs/assets/image (174).png>)

If the git provider is detected, a compatible URL will be displayed automatically. If not, you will be first prompted to select the provider to display the webhook URL.

You can copy this URL and paste it in the related section in the git provider repository settings with the copy button.

You can also regenerate the URL to invalidate/revoke the previous one with the refresh button.

![](<https://cdn.appcircle.io/docs/assets/image (175).png>)

Please refer to the following guides to set up webhooks in various git providers:

- GitHub: [https://docs.github.com/en/developers/webhooks-and-events/webhooks](https://docs.github.com/en/developers/webhooks-and-events/webhooks)
- Bitbucket: [https://support.atlassian.com/bitbucket-cloud/docs/manage-webhooks/](https://support.atlassian.com/bitbucket-cloud/docs/manage-webhooks/)
- GitLab: [https://docs.gitlab.com/ee/user/project/integrations/webhooks.html](https://docs.gitlab.com/ee/user/project/integrations/webhooks.html)
- AWS CodeCommit: [https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-notify.html](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-notify.html)
- Azure DevOps: [https://docs.microsoft.com/en-us/azure/devops/service-hooks/overview?view=azure-devops](https://docs.microsoft.com/en-us/azure/devops/service-hooks/overview?view=azure-devops)

In essence, you need to find the Webhooks section under the repository settings and paste the payload URL. You can then select the relevant events for the triggers, some examples of which are branch/tag creation/removal, pull requests, and pushes.

:::info

You can also use[ appcircle-cli](../appcircle-api/about-the-appcircle-cli.md) to trigger your builds from the command line as well.

:::

## Managing Triggers for Builds

To set up or manage the build triggers, click the Triggers button in the context menu of the build profile, accessible from the top of the profile details.

![](https://cdn.appcircle.io/docs/assets/managing-triggers-for-builds.jpg)

The triggers are set up at the profile level and you can specify individual branch names or [utilize wildcards](#wildcard-reference) for branch names to trigger builds.

You also need to select a workflow for each trigger and the build will be run with that trigger for the specified branch. You can build the same branch with different workflows (e.g. production or development) or you can use the same workflow for multiple branches (e.g. multiple feature branches built with the develop workflow).

#### Auto build on every push

Appcircle will start building your application whenever you push a commit to your Git repository. For the specified branches, your project will be built automatically with the selected workflow.

![](https://cdn.appcircle.io/docs/assets/push-triggers-full.jpg)

You must choose a fallback configuration in case the triggered branch doesn't have a configuration. This becomes useful for wildcard triggers for newly created branches.

#### Auto build pull/merge requests

Appcircle will start building your application whenever you initiate a pull request or merge request from the source branch(es) to the target branch.

The build will be done with the pull/merge result using the selected workflow. This allows testing of the PR/MR result before the actual approval of the request. This trigger will use the destination's branch config when the workflow starts. However, you may override the config by choosing **Fallback Config**.

![](<https://cdn.appcircle.io/docs/assets/image (179).png>)

#### Selective auto build with specific tags

Appcircle will start building your application with the selected workflow whenever you perform a push with certain tags to your Git repository. Your project will be built automatically only if the push has the tags you specify or you can specify a wildcard tag to build all tagged pushes.

This allows build scenarios like building only specific pushes that has the "release" in the tag. This trigger will use tag's branch config when the workflow starts. However, you may override the config by choosing **Fallback Config**.

![](<https://cdn.appcircle.io/docs/assets/image (180).png>)

### Skipping a workflow

If your commit message includes `[skip ci]` or `[ci skip]`, your workflow will be skipped.

### Retrying a workflow

If your Merge Request comment includes `[retry]`, your workflow will be retried.

## Further Automatic Build Subjects

### Trigger Priorities

If you set up multiple triggers, specific branch definitions will take priority over wildcard definitions. Below is an example:

Assume that you have a branch named `development` with three push triggers

- Trigger branch: `*` -> Trigger Workflow: Workflow 1
- Trigger branch: `development` -> Trigger Workflow: Workflow 2
- Trigger branch: `develop*` -> Trigger Workflow: Workflow 3

When there is a push or PR for the development branch, the second trigger (the one with Workflow 2) will be used to initiate a build.

###

### Wildcard Reference

You can specify branch names or tags with an asterisk wildcard to automate builds. Below are some examples:

| Pattern       | Description                                           |
| ------------- | ----------------------------------------------------- |
| `*-fix`       | Build if it ends with `-fix`                          |
| `fix-*`       | Build if it starts with `fix-`                        |
| `*-fix-*`     | Build if it `-fix-` is present anywhere in the name   |
| `fix-*-build` | Build if it starts with `fix-` and ends with `-build` |
| `*`           | Build everything                                      |

### How to enable triggers for AWS CodeCommit repositories?

Appcircle supports AWS CodeCommit triggers through an Amazon SNS topic.

For more information, please refer to: [https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-notify-sns.html](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-notify-sns.html)

After you follow the steps in the referenced document above to create a trigger, you need to create a notification rule under CodeCommit Settings as shown below to add a webhook URL.

![](https://cdn.appcircle.io/docs/assets/codecommit-settings.png)

Then select the "Enable raw message delivery" option while adding the webhook URL as a subscription to the topic.

![](https://cdn.appcircle.io/docs/assets/enable-raw-message-delivery.png)

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />
