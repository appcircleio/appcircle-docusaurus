---
title: Appcircle Slack Bot
metaTitle: Appcircle Slack Bot Integration and Usage
metaDescription: Appcircle Slack Bot Integration and Usage
sidebar_position: 2
---

import NarrowImage from '@site/src/components/NarrowImage';

# Appcircle Slack Bot

Appcircle supports some operations (`start build` etc.) you can do in [appcircle.io](https://my.appcircle.io/), with `Appcircle Slack Bot` as well. You can add `Appcircle Bot` to your Slack workspace to streamline your CI/CD pipeline using specified commands in the selected channels.

### Adding Appcircle Bot to Slack

You can add the `Appcircle Bot` to the workspace from the `Slack App Directory`. (Please note that only the person who added the `Appcircle Bot` to the Slack workspace can see and manage it.)

![](<https://cdn.appcircle.io/docs/assets/slack-bot-0.png>)

### Connecting Appcircle Bot to the Account

To connect `Appcircle Bot` to the account, you need to use the `Personal Access Token` generated from your account. If you don't know how to generate it, you can follow the steps in [this document](../../appcircle-api/api-authentication.md).

You can reach the `Enter the PAT` screen with the `Add Personal Access Token` button on the `Home` tab when the application is opened.

![](<https://cdn.appcircle.io/docs/assets/slack-bot-1.png>)

Enter the PAT on the mini screen that appears.

![](<https://cdn.appcircle.io/docs/assets/slack-bot-2.png>)

If you enter the password correctly you will receive a confirmation message from `Appcircle Bot`.

![](<https://cdn.appcircle.io/docs/assets/slack-bot-3.png>)

### Adding Appcircle Bot to the Channel

Please note that anyone in the channel where you will add the `Appcircle Bot` can use the app commands.

To add `Appcircle Bot` to the channel, right click on the app and press the `View app details`.

![](<https://cdn.appcircle.io/docs/assets/slack-bot-4.png>)

Press the ` + Add this app to a channel` button on the screen that appears.

![](<https://cdn.appcircle.io/docs/assets/slack-bot-5.png>)


### Starting a Build with the Appcircle Bot

Start a new build by typing `/build` in the channel where `Appcircle Bot` is added and pressing enter.

On the screen that appears, select the profile you want to build.

![](<https://cdn.appcircle.io/docs/assets/slack-bot-6.png>)

Select a configured branch and a workflow then start build. Please note that selecting an unconfigured branch will give an error.

![](<https://cdn.appcircle.io/docs/assets/slack-bot-7.png>)

If the selections are appropriate you will receive a confirmation message from `Appcircle Bot`.

### Distribute the App to Testers

Start a new distribution to testers by typing `/distribute`  in the channel where `Appcircle Bot` is added and pressing enter.

On the screen that appears, select the testing profile you want to distribute.

![](<https://cdn.appcircle.io/docs/assets/slack-bot-8.png>)

Select a version to send then press the `Share with Testers` button. Please note that you should not select app bundle (AAB) files because `AAB` files are only valid for Google Play submission and they cannot be shared with testers and cannot be previewed on the device.

![](<https://cdn.appcircle.io/docs/assets/slack-bot-9.png>)

On the screen that appears, fill in the blanks as described below:
- Select one or more `testing groups` in the options. You can create a new `testing group` via [appcircle.io](https://my.appcircle.io/).
- If you want to specify the tester email addresses to be sent, you can add these emails to the `Email addresses` field by separating them with commas. If you leave this field blank, distribution will be made to the default e-mail addresses.
- Type your message in the `Message to Testers` field to leave a  message to the testers.

![](<https://cdn.appcircle.io/docs/assets/slack-bot-10.png>)

After the required fields are filled, press the 'Share' button. If the selections are appropriate you will receive a confirmation message from `Appcircle Bot`.


### Send the App to Store Submission

Send the built and signed app by typing `/storesubmit` in the channel where `Appcircle Bot` is added and pressing enter.

On the screen that appears, select the `Distribution Profile` you want to send.

![](<https://cdn.appcircle.io/docs/assets/slack-bot-11.png>)

Select a version to send and press the `Send for Store Submit` button. Please note that selecting an unconfigured branch will give an error.

![](<https://cdn.appcircle.io/docs/assets/slack-bot-12.png>)

On the screen that appears, select the `Store` you want to send and press the `Send to Store Submit` button.

![](<https://cdn.appcircle.io/docs/assets/slack-bot-13.png>)

If the selections are appropriate you will receive a confirmation message from `Appcircle Bot`.