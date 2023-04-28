---
title: Appcircle Slack Bot
metaTitle: Appcircle Slack Bot Integration and Usage
metaDescription: Appcircle Slack Bot Integration and Usage
sidebar_position: 2
---

import NarrowImage from '@site/src/components/NarrowImage';

# Appcircle Slack Bot

Appcircle supports some operations such as `start build`, which you can do in [appcircle.io](https://my.appcircle.io/), with the help of `Appcircle Slack Bot`. By adding the `Appcircle Bot` to your Slack workspace, you can streamline your CI/CD pipeline using specific commands in selected channels.

**Note:** There is currently no Slack integration available on the self-hosted Appcircle. However, we are actively working on it and it will be available for use on the self-hosted Appcircle in the near future.

### Adding Appcircle Bot to Slack

Please note that only the person who added the `Appcircle Bot` to the Slack workspace can see and manage it, and that person must be a `Workspace Owner` or a `Workspace Admin`. 

To add the `Appcircle Bot` to the workspace, you can choose one of the two options below:

1. You can use the `Slack App Directory` to add the `Appcircle Bot` to the workspace.

   ![](https://cdn.appcircle.io/docs/assets/slack-bot-0.png)

2. You can use the button below to add the `Appcircle Bot` to the workspace.

   <a href="https://slack.com/oauth/v2/authorize?client_id=4982900113170.4983351339554&scope=app_mentions:read,channels:history,channels:manage,channels:read,chat:write,chat:write.customize,commands,groups:read,groups:write,im:read,im:write,mpim:read,mpim:write,team:read,users:read&user_scope="><img alt="Add to Slack - slack-bot-01.png" height="44" width="140" src="https://cdn.appcircle.io/docs/assets/slack-bot-01.png"/></a>

   Then, you need to allow the `Appcircle Bot` application.
   
   ![](https://cdn.appcircle.io/docs/assets/slack-bot-02.png)

You will then see that Slack is connected.

### Connecting Appcircle Bot to the Account

To connect `Appcircle Bot` to your account, you need to use the `Personal Access Token` generated from your account. If you don't know how to generate it, you can follow the steps in [this document](../../appcircle-api/api-authentication.md).

You can reach the `Enter the PAT` screen with the `Add Personal Access Token` button on the `Home` tab when the application is opened.

![](https://cdn.appcircle.io/docs/assets/slack-bot-1.png)

Enter the PAT on the mini screen that appears.

![](https://cdn.appcircle.io/docs/assets/slack-bot-2.png)

If you enter the password correctly, you will receive a confirmation message from `Appcircle Bot`.

![](https://cdn.appcircle.io/docs/assets/slack-bot-3.png)

If you want to update the PAT, you can follow the above steps for the new PAT.

### Adding Appcircle Bot to a Channel

To be able to use the `Appcircle Bot` commands, you need to add it to a channel. Commands cannot be used in private chat. Please note that anyone in the channel where you add the `Appcircle Bot` can use the app commands. If an unauthorized person adds `Appcircle Bot` to the channel, the app will leave the channel by itself.

To add `Appcircle Bot` to the channel, right-click on the app and click the `View app details`.

![](https://cdn.appcircle.io/docs/assets/slack-bot-4.png)

Click the ` + Add this app to a channel` button on the screen that appears.

![](https://cdn.appcircle.io/docs/assets/slack-bot-5.png)

### Starting a Build with Appcircle Bot

Start a new build by typing `/build` in the channel where `Appcircle Bot` has been added and pressing Enter.

On the screen that appears, select the profile you want to build.

![](https://cdn.appcircle.io/docs/assets/slack-bot-6.png)

Select a configured branch and a workflow, then start the build. Please note that selecting an unconfigured branch will result in an error. Only Smartface builds do not require configuration.

![](https://cdn.appcircle.io/docs/assets/slack-bot-7.png)

If the selections are correct, you will receive a confirmation message from `Appcircle Bot`.

### Distributing the App to Testers

Start a new distribution to testers by typing `/distribute` in the channel where `Appcircle Bot` has been added and pressing Enter.

On the screen that appears, select the testing profile you want to distribute.

![](https://cdn.appcircle.io/docs/assets/slack-bot-8.png)

Select a version to send, then press the `Share with Testers` button. Please note that you should not select app bundle (AAB) files because `AAB` files are only valid for Google Play submission, and they cannot be shared with testers or previewed on the device.

![](https://cdn.appcircle.io/docs/assets/slack-bot-9.png)

On the screen that appears, fill in the following fields:
- Select one or more `testing groups` from the options. You can create a new `testing group` via [appcircle.io](https://my.appcircle.io/).
- If you want to specify the email addresses of the testers to be sent, you can add these email addresses to the `Email addresses` field by separating them with commas and spaces.
- Type your message in the `Message to Testers` field to leave a message for the testers.

After filling in the required fields, press the `Share` button.

![](https://cdn.appcircle.io/docs/assets/slack-bot-10.png)

Preview your choices on the screen that appears. You can remove email addresses or testing groups, and correct the messages to be sent to the testers. Then press the `Next` button.

![](https://cdn.appcircle.io/docs/assets/slack-bot-10.0.png)


If the selections are correct, you will receive a confirmation message from `Appcircle Bot`.

### Send the App to Store Submission

Send the built and signed app by typing `/storesubmit` in the channel where `Appcircle Bot` has been added and pressing Enter.

On the screen that appears, select the `Distribution Profile` you want to send.

![](https://cdn.appcircle.io/docs/assets/slack-bot-11.png)

Select a version to send, and press the `Send for Store Submit` button. Please note that selecting an unconfigured branch will result in an error.

![](https://cdn.appcircle.io/docs/assets/slack-bot-12.png)

On the screen that appears, select the `Store` you want to send, and press the `Send to Store Submit` button.

![](https://cdn.appcircle.io/docs/assets/slack-bot-13.png)

If the selections are correct, you will receive a confirmation message from `Appcircle Bot`.