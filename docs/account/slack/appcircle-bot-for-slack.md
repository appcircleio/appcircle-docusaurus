---
title: Appcircle Bot For Slack
metaTitle: Appcircle Bot for Slack Integration and Usage
metaDescription: Appcircle Bot for Slack Integration and Usage
sidebar_position: 2
---

import NarrowImage from '@site/src/components/NarrowImage';
import Screenshot from '@site/src/components/Screenshot';

# Appcircle Bot for Slack

Appcircle is a comprehensive mobile CI/CD platform that automates the build, test, and deployment processes for mobile app development.

By adding `Appcircle Bot` to your Slack workspace, you gain the ability to perform the same actions available on [appcircle.io](https://my.appcircle.io/) directly within Slack, including:

- :package: Start a build based on your chosen profile, branch, and workflow.
- :outbox_tray: Send the selected version to your preferred test profiles or email addresses.
- :mailbox: Send the designated version to the `Submit Store` for review and distribution.  

:::info

There is currently no integration of Slack available on the self-hosted Appcircle. However, we are actively working on it and it will be available for use on the self-hosted Appcircle in the near future.

:::

### Adding Appcircle Bot to Slack

Please note that only the person who added the `Appcircle Bot` to the Slack workspace can see and manage it, and that person must be a `Workspace Owner` or a `Workspace Admin`. 

To add the `Appcircle Bot` to the workspace, you can choose one of the two options below:

1. You can use the button below to add the `Appcircle Bot` to the workspace.

   <a href="https://slackbot.appcircle.io/slack/install"><img alt="Add to Slack - slack-bot-01.png" height="44" width="140" src="https://cdn.appcircle.io/docs/assets/slack-bot-01.png"/></a>

   Then, you need to allow the `Appcircle Bot` application.
   
   <ExternalScreenshot url='https://cdn.appcircle.io/docs/assets/slack-bot-02.png' width='720px' height='457px' />

2. You can use the `Slack App Directory` to add the `Appcircle Bot` to the workspace.

   <ExternalScreenshot url='https://cdn.appcircle.io/docs/assets/slack-bot-0.png' width='1118px' height='704px' />

You will then see that Slack is connected.

### Connecting Appcircle Bot to the Account

To connect `Appcircle Bot` to your account, you need to use the `Personal Access Token` generated from your account. If you don't know how to generate it, you can follow the steps in [this document](../../appcircle-api/api-authentication.md).

You can reach the `Enter the PAT` screen with the `Add Personal Access Token` button on the `Home` tab when the application is opened.

<ExternalScreenshot url='https://cdn.appcircle.io/docs/assets/slack-bot-1.png' width='1254px' height='777px' />

Enter the PAT on the mini screen that appears.

<ExternalScreenshot url='https://cdn.appcircle.io/docs/assets/slack-bot-2.png' width='1254px' height='777px' />

If you enter the password correctly, you will receive a confirmation message from `Appcircle Bot`.

<ExternalScreenshot url='https://cdn.appcircle.io/docs/assets/slack-bot-3.png' width='1254px' height='777px' />

If you want to update the PAT, you can follow the above steps for the new PAT.

### Adding Appcircle Bot to a Channel

To be able to use the `Appcircle Bot` commands, you need to add it to a channel. Commands cannot be used in private chat. Please note that anyone in the channel where you add the `Appcircle Bot` can use the app commands. If an unauthorized person adds `Appcircle Bot` to the channel, the app will leave the channel by itself.

To add `Appcircle Bot` to the channel, right-click on the app and click the `View app details`.

<ExternalScreenshot url='https://cdn.appcircle.io/docs/assets/slack-bot-4.png' width='1118px' height='557px' />

Click the ` + Add this app to a channel` button on the screen that appears.

<ExternalScreenshot url='https://cdn.appcircle.io/docs/assets/slack-bot-5.png' width='1124px' height='558px' />

### Starting a Build with Appcircle Bot

Start a new build by typing `/build` in the channel where `Appcircle Bot` has been added and pressing Enter.

On the screen that appears, select the profile you want to build.

<ExternalScreenshot url='https://cdn.appcircle.io/docs/assets/slack-bot-6.png' width='1391px' height='883px' />

Select a configured branch and a workflow, then start the build. Please note that selecting an unconfigured branch will result in an error. Only Smartface builds do not require configuration.

<ExternalScreenshot url='https://cdn.appcircle.io/docs/assets/slack-bot-7.png' width='1257px' height='820px' />

If the selections are correct, you will receive a confirmation message from `Appcircle Bot`.

### Distributing the App to Testers

Start a new distribution to testers by typing `/distribute` in the channel where `Appcircle Bot` has been added and pressing Enter.

On the screen that appears, select the testing profile you want to distribute.

<ExternalScreenshot url='https://cdn.appcircle.io/docs/assets/slack-bot-8.png' width='1257px' height='820px' />

Select a version to send, then press the `Share with Testers` button. Please note that you should not select app bundle (AAB) files because `AAB` files are only valid for Google Play submission, and they cannot be shared with testers or previewed on the device.

<ExternalScreenshot url='https://cdn.appcircle.io/docs/assets/slack-bot-9.png' width='1257px' height='820px' />

On the screen that appears, fill in the following fields:
- Select one or more `testing groups` from the options. You can create a new `testing group` via [appcircle.io](https://my.appcircle.io/).
- If you want to specify the email addresses of the testers to be sent, you can add these email addresses to the `Email addresses` field by separating them with commas and spaces.
- Type your message in the `Message to Testers` field to leave a message for the testers.

After filling in the required fields, press the `Share` button.

<ExternalScreenshot url='https://cdn.appcircle.io/docs/assets/slack-bot-10.png' width='1389px' height='811px' />

Preview your choices on the screen that appears. You can remove email addresses or testing groups, and correct the messages to be sent to the testers. Then press the `Next` button.

<ExternalScreenshot url='https://cdn.appcircle.io/docs/assets/slack-bot-10.0.png' width='1389px' height='811px' />


If the selections are correct, you will receive a confirmation message from `Appcircle Bot`.

### Send the App to Store Submission

Send the built and signed app by typing `/storesubmit` in the channel where `Appcircle Bot` has been added and pressing Enter.

On the screen that appears, select the `Distribution Profile` you want to send.

<ExternalScreenshot url='https://cdn.appcircle.io/docs/assets/slack-bot-11.png' width='1257px' height='820px' />

Select a version to send, and press the `Send for Store Submit` button. Please note that selecting an unconfigured branch will result in an error.

<ExternalScreenshot url='https://cdn.appcircle.io/docs/assets/slack-bot-12.png' width='1257px' height='820px' />

On the screen that appears, select the `Store` you want to send, and press the `Send to Store Submit` button.

<ExternalScreenshot url='https://cdn.appcircle.io/docs/assets/slack-bot-13.png' width='1262px' height='785px' />

If the selections are correct, you will receive a confirmation message from `Appcircle Bot`.