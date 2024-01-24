---
title: Publish
metaTitle: Publish
metaDescription: Publish
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';

The Publish module will enable your applications to be published in the App Store, Google Play, and Huawei AppGallery stores. You can also submit your mobile applications to TestFlight.

Click on the **Publish** button on the left menu bar to go to the Publish module.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-main.png' />

In order to use the Publish module, first connections must be provided for the relevant stores. You can make these connections from **My Organization -> Integrations -> Connections**.

For detailed information on store **Connections**, follow the links below.

|Store|Connection|
|----------|-----------|
|App Store|https://docs.appcircle.io/account/adding-an-app-store-connect-api-key|
|Google Play| https://docs.appcircle.io/account/adding-google-play-service-account|
|Huawei AppGallery| https://docs.appcircle.io/account/adding-huawei-api-key|

## Starting Publish Process with Build

After building the application, we can start the publishing process by sending it to the Publish module.

For this, it is necessary to first create a publish profile within the Publish module. Afterwards, the relevant publish profile must be selected from the **Distribution** tab in the configuration of the relevant profile in the Build module.

In order to create a publish profile, click on the "Add New" button in the Publish module.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-add-new.png' />

You should give a descriptive name to the relevant publish profile.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-new-profile.png' />

The publish profile is created, and it's ready for application submission.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-empty-profile.png' />

Go to the build profile that we will send to the Publish module, and select the publish profile from the **Distribution** tab in the configuration.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-build.png' />

:::tip
When selecting the publish profile from **Build profile -> Configuration -> Distribution**, more than one target profile can be selected.
:::

Now the build profile is ready for application publishing.

When the build is successful, Appcircle will send the version of the relevant application to the selected publish profiles in the Publish module.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-build-success.png' />

## Publish Flow

Appcircle includes a predefined flow in the Publish module for publishing the application to stores (App Store, Google Play, Huawei AppGallery). This flow can be customized according to your specific publishing requirements.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-flow-button.png' />

When you click on the **Publish Flow** button, the list of steps included in the publish flow will appear.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-flow-w.png' />

We can access the list of steps that can be used in a publish workflow by clicking on the **Manage Flow** button. You can add or remove new steps and customize your publish workflow as you wish.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-workflows.png' />

## Publish Settings

When a build is completed on the Build module and its artifacts are distributed to the Publish module, we can start the publish process to the stores using the **Auto Publish** toggle in **Settings**.

Your configured publish flow will be executed automatically when you enable **Auto Publish**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-settings.png' />

:::info
If group or variable definitions have been made in **Publish Variables**, you will see the list of variable groups in **Settings**, and you can select one or more of them to use in your publish flow.
:::

## Publish Variables

Variables, similar to the [environment variables](../environment-variables/index.md) in build, can be defined in this section to be used specifically in the publish flow for store submissions.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-variables.png' />

To use these defined variables, it will be necessary to select them from the [Publish Settings](#publish-settings).

## Adding an Application Version Manually

Appcircle supports publishing the application to the stores without using the Build module. To add an application version manually, you need to add a publish profile beforehand and then **Open** its details.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-manuel.png' />

You can then upload the application by clicking on the **Add Version** button on the right.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-upload.png' />

When the upload is completed successfully, the relevant application version will appear in the list.

Afterwards, you can start submitting your application to the stores with the publish flow that you have configured.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-version-list.png' />

For this, click on the **Actions** button for the relevant version and go to **Details**. From there, you can manually **Start Flow** for the uploaded application version.

## App Version History

You can browse the records of the previous transactions of the related application version with the History button on the modal opened by clicking the three dots on the right side of the version list.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-history-button.png' />

The list of operations performed with the relevant application version will appear on the opened modal.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-history-list.png' />

When a record is selected from the window that opens, the log screen of the transaction will appear. All logs of the related transaction will appear here.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-history-log.png' />

## App Version Download

Appcircle allows you to download the previously installed application output again. For this, you can click on the **Download** button on the modal opened by clicking on the three dots on the right side of the version list.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-download.png' />

## App Version Delete

Appcircle allows you to delete the previously installed application version. For this, you can click on the **Delete** button on the modal opened by clicking on the three dots on the right side of the version list.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-delete.png' />

Sonrasında ekrana gelen uyarı penceresindeki konfirmasyonu tamamlayarak silme işlemini gerçekleştirebilirsiniz.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-delete-confirm.png' />

:::caution
Appcircle does not delete the app that has been submitted to the store. This deletion will only delete the version of the app in the Publish module.
:::

## Publish Profile Rename

Appcircle allows previously created profiles to be renamed. To do this, the **Rename** button is used by clicking on the three dots at the top right of the relevant profile card from the cards in the Publish profile list.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-rename.png' />

:::caution
Publish profile names must be unique for all platforms. For example, if you have a profile named "Example" for iOS Publish, Appcircle will not allow you to create a profile named "Example" again for Android Publish or rename it with the existing name.
:::

## Publish Profile Remove

To delete the Publish profile, click on the three dots on the upper right side of the relevant profile card from the cards in the profile list and use the **Delete** button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-remove.png' />

:::caution
Deleting the Publish profile does not remove app versions submitted to the store. Only the profile on Appcircle will be deleted.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-remove-confirm.png' />