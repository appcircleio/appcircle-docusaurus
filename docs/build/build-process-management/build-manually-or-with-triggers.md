---
title: Triggers
description: Learn how to build manually or automatically with webhooks and triggers in Appcircle
tags: [build, build process management, manual build, automatic build, triggers, webhooks]
sidebar_position: 5
---

import Screenshot from '@site/src/components/Screenshot';

There are multiple ways to trigger a build in Appcircle. You can run builds manually or automate the build process with various triggers.

<iframe width="640" height="315" src="https://www.youtube.com/embed/zxxax79KD9U" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Triggers for Manual Builds

For the manual builds, the currently available push triggers apply, and if no trigger is configured, the following trigger is provided by default under the [push triggers](#auto-build-on-every-push). If there are others, they may take precedence based on the [trigger priorities](#trigger-priorities).

<Screenshot url='https://cdn.appcircle.io/docs/assets/build-manual-push-trigger.png' />

## Triggers Configuration

To set up or manage the build triggers, click the Triggers button in the context menu of the build profile, accessible from the top of the profile details.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-trigger.png' />

The triggers are set up at the profile level, and you can specify individual branch names or [utilize wildcards](/build/build-process-management/build-manually-or-with-triggers#wildcard-reference) for branch names to trigger builds.

You also need to select a workflow for each trigger, and the build will be run with that trigger for the specified branch. You can build the same branch with different workflows (e.g., production or development), or you can use the same workflow for multiple branches (e.g., multiple feature branches built with the develop workflow).

## Automatic Build

Builds can be triggered with various triggers such as every push to the repository, pull/merge requests, or tagged pushes. This requires the following:

- Webhook connection to the repository
- Setting up build triggers

There are two options to set up webhooks for automatic builds:

- You can [authorize the Appcircle app](/build/manage-the-connections/adding-a-build-profile) for GitHub, Bitbucket, or GitLab repositories for direct integration. The triggers will be available for use immediately. (You can skip the next part about the webhook setup.)
- For the repository connections through SSH, you can add the specific webhook for that build profile manually to the compatible git provider. This enables the Git provider to send a POST request to Appcircle for the selected events, which you can then use for triggers.

### Setting Up Manual Webhooks for SSH and Public Repositories

For repositories connected through SSH, you can set up triggers with webhooks in compatible repository providers.

When you connect a repository through SSH or through a public URL, the Webhook URL option will be enabled in the context menu of the build profile, accessible from the top of the profile details.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-webhooks.png' />

You can copy this URL and paste it in the related section in the git provider repository settings with the copy button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6019-ss1.png' />

To manually configure a webhook:

**1.**	Go to your build profile.

**2.**	Click the Settings (gear icon) and select Repository Webhook URL.

**3.**	In the Repository Webhook URL popup:

- Select a Git Provider:
If the Git provider is detected, a compatible URL will be displayed automatically. If not, choose your Git provider (e.g., GitHub, GitLab, Bitbucket) from the dropdown list.

- Copy the Webhook URL:
The generated Public Repository Webhook URL will appear based on your selection. Copy this URL and paste it into your repository’s webhook settings.

- Generate a New Webhook Key (Optional):
If needed, you can generate a new webhook key to refresh or reset the endpoint’s security token.

**4.**	Paste the Webhook URL in your Git repository:

For example, in **GitHub**:
- Go to your repository.
- Click Settings > Webhooks > Add webhook.
- Paste the URL into the Payload URL field.
- Choose application/json as the content type.
- Paste the Webhook Key if required.
- Select the appropriate events (e.g., push or tag creation).
- Save the webhook.

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

### Auto build on every push

Appcircle will start building your application whenever you push a commit to your Git repository. For the specified branches, your project will be built automatically with the selected workflow.

<Screenshot url='https://cdn.appcircle.io/docs/assets/build-manual-push-trigger.png' />

You must choose both workflow, and a configuration when you're setting up a trigger.

### Auto build pull/merge requests

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

### Triggering different workflows at the same time

Now you will be able to trigger different workflows in the same source branch and target branch on Appcircle at once. As soon as the trigger is triggered, Appcircle will start running all the triggered triggers in the build queue, starting from the first place in the established trigger queue.

<Screenshot url='https://cdn.appcircle.io/docs/assets/build-pr-mr-trigger-multiple.png' />

### Selective auto build with specific tags

Appcircle will start building your application with the selected workflow whenever you perform a push with certain tags to your Git repository. Your project will be built automatically only if the push has the tags you specify, or you can specify a wildcard tag to build all tagged pushes.

This allows building scenarios like building only specific pushes that have the "release" in the tag.

<Screenshot url='https://cdn.appcircle.io/docs/assets/tag-last.png' />

### Skipping a workflow

If your commit message includes `[skip ci]` or `[ci skip]`, your workflow will be skipped.

### Retrying a workflow

If your merge request comment includes `[retry]`, your workflow will be retried.

### Auto Cancel Redundant Pipeline

When enabled, this feature automatically cancels any previously running build that matches the same build configuration, build workflow, build trigger and branch if a new run is triggered.
This helps prevent unnecessary resource usage and reduces queue time by skipping outdated pipeline runs.

To enable this feature:

1. Go to the `Build Profiles` and select `Configurations`.
2. Scroll down and activate `Auto Cancel Redundant Pipeline`.
3. Click `Save` changes.

<Screenshot url='https://cdn.appcircle.io/docs/assets/auto-cancel-redundant-pipeline.png' />

The Auto-Cancel Redundant Pipeline mechanism works based on four key parameters:
- Build Configuration
- Build Workflow
- Build Trigger
- Git Branch

If a new build is triggered with the same values for all these parameters, any previously queued or running build is automatically cancelled.

:::warning Manual Builds Bypass Auto Cancel Redundant Pipeline

Builds that are **manually started** do not affect ongoing or queued builds; the auto-cancel mechanism does not apply to manually started builds.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/auto-cancel-redundant-pipeline-canceled-builds-v3.png' />

## Further Automatic Build Subjects

### Trigger Priorities

If you set multiple triggers, certain branch definitions will not take precedence over wildcard definitions. They will all start at the same time. Below is an example:

Assume that you have a branch named `development` with three push triggers.

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

### Why is my Appcircle trigger not working and how can I fix it?

First, ensure that the build profile triggers are set for the desired branches and actions. Please check the trigger settings from the [**Managing Triggers for Builds**](/build/build-process-management/build-manually-or-with-triggers#managing-triggers-for-builds) section in the documentation.

Appcircle is triggered via the Git provider's webhooks. To properly work with triggers, webhooks in the repositories are used by Appcircle. Also, ensure that the repository has webhook access to Appcircle. To connect webhooks, the Git provider connection must be set up properly while creating a build profile.

Certain Git actions to the repositories, such as push, merge, pull request, tag push, etc., activate a specified event with the repository's webhooks. It is necessary to ensure that the desired event is actually triggered by the action in the Git provider's repository.

If webhooks are disabled due to frequent use or connection-based errors, using test events may help re-enable webhooks in Git providers.

To ensure webhooks are set and working, the webhook history can be reviewed within the Git providers. Let's check the Git providers below. You can follow the steps in the Git provider's documentation to access the webhook event history.

- [**GitHub Webhook Deliveries**](https://docs.github.com/en/webhooks/testing-and-troubleshooting-webhooks/viewing-webhook-deliveries#about-webhook-deliveries)
- [**GitLab Webhook Request History**](https://docs.gitlab.com/ee/user/project/integrations/webhooks.html#view-webhook-request-history)
- [**Azure DevOps Services Webhook History**](https://learn.microsoft.com/en-us/azure/devops/service-hooks/services/webhooks?view=azure-devops)
- [**Bitbucket Webhook Documentations**](https://support.atlassian.com/bitbucket-cloud/docs/manage-webhooks)

:::info Bitbucket Webhook Event History

A document detailing the history of webhooks is not provided by Bitbucket. To access the webhook history, please navigate to:

**Bitbucket -> Repository -> Repository Settings -> Webhooks -> View Requests**

View Requests has to be enabled before requests can be seen.

:::

Once the webhook is created and confirmed to be properly set up and healthy in the Appcircle build profile, and it is verified to work correctly with the specific Git provider, the process works as follows:

- A Git action, such as pushing a code block, triggers a webhook event.
- This webhook event activates the trigger in Appcircle.
- Appcircle then automatically starts the build process.

### Why does my tag trigger start a build on a different branch?

When you create a tag, it is applied to a specific commit, not a branch. The system does not have explicit branch information linked to the tag. Therefore, when the tag trigger starts a build in Appcircle, it may select any branch that contains the tagged commit, leading to seemingly random behavior.

To control this behavior, push an empty commit to the desired branch and then apply the tag to this new commit. This ensures that the tag trigger starts from the intended branch.

### How to enable triggers for AWS CodeCommit repositories?

Appcircle supports AWS CodeCommit triggers through an Amazon SNS topic.

For more information, please refer to: [https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-notify-sns.html](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-notify-sns.html)

After you follow the steps in the referenced document above to create a trigger, you need to create a notification rule under CodeCommit Settings as shown below to add a webhook URL.

<Screenshot url='https://cdn.appcircle.io/docs/assets/codecommit-settings.png' />

Then select the "Enable raw message delivery" option while adding the webhook URL as a subscription to the topic.

<Screenshot url='https://cdn.appcircle.io/docs/assets/enable-raw-message-delivery.png' />

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />
