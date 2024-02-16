---
title: App Center iOS Distribution
metaTitle: App Center iOS Distribution
metaDescription: App Center iOS Distribution
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';

# App Center iOS Distrubiton

With this step you can send your .ipa and dSYM files [App Center](https://appcenter.ms/). For this, the step needs to be configured according to your App Center account.

- First, you need to use this step after **Xcodebuild for Devices.** This is because the project is compiled and archived in the Xcodebuild for Devices step.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2612-center_order.png' />

:::caution
Note that, if you do not use this step after **Xcodebuild for Devices**, Appcircle will not find **.ipa** and **dSYM** files to distribute to App Center.
:::

- Inside the step, there will be some parameters that you need to configure according to your **App Center account**. You need to enter your **App Center Access Token** in this parameter. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2612-center_token.png' />

:::warning
**Caution. Do not hard coded sensitive variables such as token directly to the parameters in the step. We recommend using Environment Variables groups for such sensitive variables.**
:::

- In the owner name parameter, you need to type the owner name of your App Center organization or user. You can get this variable from the App Center URL. 

For example; in the example URL **`https://appcenter.ms/users/JohnDoe/apps/myapp`**, **`JohnDoe`** is the owner name. If you have an organization, you will see a URL like **`https://appcenter.ms/orgs/Appcircle/apps/myapp.`** Here the owner name is **`Appcircle`**

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2612-center_owner.png' />

- In the app name parameter, you need to type the app name of your App Center organization or user. You can get this variable from the App Center URL. 

For example; in the example URL **`https://appcenter.ms/users/JohnDoe/apps/myapp`**, **`myapp`** is the app name. If you have an organization, you will see a URL like **`https://appcenter.ms/orgs/Appcircle/apps/myapp.`** Here the app name is **`myapp`**

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2612-center_app.png' />

- Group name parameter is the distribution Group names you opened in your App Center account. You can type which group you want to send to.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2612-center_grup.png' />

- Store name is the variable where you can decide which store you want to send your app to. You can submit directly to this variable by giving one of the store names in your App Center account.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2612-center_store.png' />

- Finally, with the 3 different options marked in the image, you can decide whether to upload your dSYM file, send notifications to testers, and determine whether the update is mandatory or not.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2612-center_options.png' />


[https://github.com/appcircleio/appcircle-ios-appcenter-distribute-component](https://github.com/appcircleio/appcircle-ios-appcenter-distribute-component)