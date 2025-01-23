---
title: Manual and Automatic Builds
description: Learn how to build manually or automatically with webhooks and triggers in Appcircle
tags: [build, build process management, manual build, automatic build, triggers, webhooks]
sidebar_position: 10
---

import Screenshot from '@site/src/components/Screenshot';

# Build Manually or Automatically with Webhooks and Triggers

There are multiple ways to trigger a build in Appcircle. You can run builds manually or automate the build process with various triggers.

<iframe width="640" height="315" src="https://www.youtube.com/embed/zxxax79KD9U" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Manual Build

As the name states, your build profile will not build your application until you tell it to. You can browse branches in your Git repository and select any commit from any branch you need to build. To initiate a manual build, just press the **Start Build** button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/adding-a-build-profile-inside.png' />

### Workflows for Manual Builds

For the manual builds, the currently available push triggers apply and if no trigger is configured, the following trigger is provided by default under the [push triggers](#auto-build-on-every-push). If there are others, they may take precedence based on the [trigger priorities](#trigger-priorities).

<Screenshot url='https://cdn.appcircle.io/docs/assets/build-manual-push-trigger.png' />

## Automatic Build

Builds can be triggered with various triggers such as every push to the repository, pull/merge requests, or tagged pushes. This requires the following:

- Webhook connection to the repository
- Setting up build triggers

There are two options to set up webhooks for automatic builds:

- You can [authorize the Appcircle app](/build/manage-the-connections/adding-a-build-profile#connect-your-repository) for GitHub, Bitbucket, or GitLab repositories for direct integration. The triggers will be available for use immediately. (You can skip the next part about the webhook setup.)
- For the repository connections through SSH, you can add the specific webhook for that build profile manually to the compatible git provider. This enables the git provider to send a POST request to Appcircle for the selected events, which you can then use for triggers.

### Setting Up Manual Webhooks for SSH and Public Repositories

For repositories connected through SSH, you can set up triggers with webhooks in compatible repository providers.

When you connect a repository through SSH or through a public URL, the Webhook URL option will be enabled in the context menu of the build profile, accessible from the top of the profile details.

<Screenshot url='https://cdn.appcircle.io/docs/assets/build-manual-webhook-url.png' />

If the git provider is detected, a compatible URL will be displayed automatically. If not, you will be first prompted to select the provider to display the webhook URL.

You can copy this URL and paste it in the related section in the git provider repository settings with the copy button.

You can also regenerate the URL to invalidate/revoke the previous one with the refresh button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/build-manual-webhook-url-menu.png' />

Please refer to the following guides to set up webhooks in various git providers:

- GitHub: [https://docs.github.com/en/developers/webhooks-and-events/webhooks](https://docs.github.com/en/developers/webhooks-and-events/webhooks)
- Bitbucket: [https://support.atlassian.com/bitbucket-cloud/docs/manage-webhooks/](https://support.atlassian.com/bitbucket-cloud/docs/manage-webhooks/)
- GitLab: [https://docs.gitlab.com/ee/user/project/integrations/webhooks.html](https://docs.gitlab.com/ee/user/project/integrations/webhooks.html)
- AWS CodeCommit: [https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-notify.html](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-notify.html)
- Azure DevOps: [https://docs.microsoft.com/en-us/azure/devops/service-hooks/overview?view=azure-devops](https://docs.microsoft.com/en-us/azure/devops/service-hooks/overview?view=azure-devops)

In essence, you need to find the Webhooks section under the repository settings and paste the payload URL. You can then select the relevant events for the triggers, some examples of which are branch/tag creation/removal, pull requests, and pushes.

:::info

You can also use[ appcircle-cli](/appcircle-api-and-cli) to trigger your builds from the command line as well.

:::

## Managing Triggers for Builds

To set up or manage the build triggers, click the Triggers button in the context menu of the build profile, accessible from the top of the profile details.

<Screenshot url='https://cdn.appcircle.io/docs/assets/build-configuration-workflow-trigger-showcase.png' />

The triggers are set up at the profile level and you can specify individual branch names or [utilize wildcards](#wildcard-reference) for branch names to trigger builds.

You also need to select a workflow for each trigger and the build will be run with that trigger for the specified branch. You can build the same branch with different workflows (e.g. production or development) or you can use the same workflow for multiple branches (e.g. multiple feature branches built with the develop workflow).

#### Auto build on every push

Appcircle will start building your application whenever you push a commit to your Git repository. For the specified branches, your project will be built automatically with the selected workflow.

<Screenshot url='https://cdn.appcircle.io/docs/assets/build-manual-push-trigger.png' />

You must choose both workflow and a configuration when you're setting up a trigger.

#### Auto build pull/merge requests

Appcircle will start building your application whenever you initiate a pull request or merge request from the source branch(es) to the target branch.

The build will be done with the pull/merge result using the selected workflow. This allows testing of the PR/MR result before the actual approval of the request.

:::caution
Make sure that the names of the source branch and the target branch are spelled correctly.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/mr-pr-last.png' />

:::info
If spaces are used in the name, Appcircle will trim it without spaces.
:::

:::info
If you are using Azure DevOps Server or Azure DevOps Services Cloud as a Git provider, the Appcircle build trigger will not run for PR status updates (Approve, Approve with suggestions, Wait for author, Reject, etc.) or action changes (Complete, Mark as draft, Abandon).

Appcircle will only run the trigger for PR creation or PR updates.

:::

#### Triggering different workflows at the same time

Now you will be able to trigger different workflows in the same source branch and target branch on Appcircle at once. As soon as the trigger is triggered, Appcircle will start running all the triggered triggers in the build queue, starting from the first place in the established trigger queue.

<Screenshot url='https://cdn.appcircle.io/docs/assets/build-pr-mr-trigger-multiple.png' />

#### Selective auto build with specific tags

Appcircle will start building your application with the selected workflow whenever you perform a push with certain tags to your Git repository. Your project will be built automatically only if the push has the tags you specify or you can specify a wildcard tag to build all tagged pushes.

This allows build scenarios like building only specific pushes that has the "release" in the tag.

<Screenshot url='https://cdn.appcircle.io/docs/assets/tag-last.png' />

### Skipping a workflow

If your commit message includes `[skip ci]` or `[ci skip]`, your workflow will be skipped.

### Retrying a workflow

If your Merge Request comment includes `[retry]`, your workflow will be retried.

## Further Automatic Build Subjects

### Trigger Priorities

If you set multiple triggers, certain branch definitions will not take precedence over wildcard definitions. They will all start at the same time. Below is an example:

Assume that you have a branch named `development` with three push triggers

- Trigger branch: `*` -> Trigger Workflow: Workflow 1
- Trigger branch: `development` -> Trigger Workflow: Workflow 2
- Trigger branch: `develop*` -> Trigger Workflow: Workflow 3

When there is a push or PR for the development branch, all triggers (since the word `development` contains both `*` and `develop*`) will be used to start a different build for each branch. At this point, a total of three build pipelines will begin.

:::info
If multiple triggered builds exceed your plan's concurrency limits, Appcircle will automatically queue them, and all of them will be executed unless you cancel.
:::

### Wildcard Reference

You can specify branch names or tags with an asterisk wildcard to automate builds. Below are some examples:

| Pattern       | Description                                           |
| ------------- | ----------------------------------------------------- |
| `*-fix`       | Build if it ends with `-fix`                          |
| `fix-*`       | Build if it starts with `fix-`                        |
| `*-fix-*`     | Build if it `-fix-` is present anywhere in the name   |
| `fix-*-build` | Build if it starts with `fix-` and ends with `-build` |
| `*`           | Build everything                                      |

## FAQ

### How can I check my triggers is working in my Appcircle Build Profiles?

First of all, it should be ensured that the build profile triggers are set for the desired branches and actions. Please check the trigger settings from the [**Managing Triggers for Builds**](/build/build-process-management/build-manually-or-with-triggers#managing-triggers-for-builds) section in documentation.

To properly work with Triggers, webhooks in the repositories are used by Appcircle. Also should be ensured that repository has webhook access to Appcircle. In order for webhooks to be connected, Git Provider connection needs to be set proper while creating a Build Profile.

Certain Git Actions to the repositories, such as push, merge, pull request, tag push, etc., activate a specified event with the repositories webhooks. It is a necessity to ensure that the desired event is actually triggered by the action in Git Provider's repository. 

To ensure webhooks are set and working, the webhook histories may be reviewed within the Git providers. Lets have a check with Git Providers down below. The steps in the Git Provider's Documentations can be followed to access the webhook event history.

- [**GitHub Webhook Deliveries**](https://docs.github.com/en/webhooks/testing-and-troubleshooting-webhooks/viewing-webhook-deliveries#about-webhook-deliveries)

- [**GitLab Webhook Request History**](https://docs.gitlab.com/ee/user/project/integrations/webhooks.html#view-webhook-request-history)

:::caution GitLab Webhook Request History

Gitlab provides users a `webhook test event`, however Appcircle does **not initiates** a build sequence with webhook test events in GitLab. 

:::

- [**Azure DevOps Services Webhook History**](https://learn.microsoft.com/en-us/azure/devops/service-hooks/services/webhooks?view=azure-devops)

:::info Azure DevOps Webhook Event History

In this Azure DevOps webhooks document, reaching service hooks is enough for checking **webhook histories**.

:::

- [**Bitbucket Webhook Documentations**](https://support.atlassian.com/bitbucket-cloud/docs/manage-webhooks)

:::info Bitbucket Webhook Event History

A document detailing the history of webhooks is **not provided** by the **Bitbucket**. However, webhook histories can be observed by navigating to the webhook section within the repository.

Please navigate to:
**Bitbucket -> Repository -> Repository Settings -> Webhooks**

:::
After confirmation of the webhook is created and connection is set and healthy through the Appcircle Build Profile, and the confirmation of the webhook is set and works as expected in a specific Git Provider. Then Git actions such as pushing a code block, which should activate a webhook event, and then should trigger the Appcircle build sequence automatically.
After confirmation of the webhook is created and connection is set and healthy through the Appcircle Build Profile, and the confirmation of the webhook is set and works as expected in a specific Git Provider. Then Git Actions such as pushing a code block, which should activate a webhook event, and then should trigger the Appcircle Build Sequence automatically.

### How to enable triggers for AWS CodeCommit repositories?

Appcircle supports AWS CodeCommit triggers through an Amazon SNS topic.

For more information, please refer to: [https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-notify-sns.html](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-notify-sns.html)

After you follow the steps in the referenced document above to create a trigger, you need to create a notification rule under CodeCommit Settings as shown below to add a webhook URL.

<Screenshot url='https://cdn.appcircle.io/docs/assets/codecommit-settings.png' />

Then select the "Enable raw message delivery" option while adding the webhook URL as a subscription to the topic.

<Screenshot url='https://cdn.appcircle.io/docs/assets/enable-raw-message-delivery.png' />

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />
