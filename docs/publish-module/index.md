---
title: Publish
metaTitle: Publish
metaDescription: Publish
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

The Publish module will enable your applications to be published in the App Store, Google Play, and Huawei AppGallery stores. You can also submit your mobile applications to TestFlight.
While publishing your mobile application to the stores, you can use predefined flows and customize them according to your specific publishing requirements.
In addition to that, you can add new versions and publish your application to the stores without using the Build module.  

Click on the **Publish** button on the left menu bar to go to the Publish module.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-main.png' />

In order to use the Publish module, first connections must be provided for the relevant stores. You can make these connections from **My Organization -> Integrations -> Connections**.

For detailed information on store **Connections**, follow the links below.

|Store|Connection|
|----------|-----------|
|App Store|https://docs.appcircle.io/account/adding-an-app-store-connect-api-key|
|Google Play| https://docs.appcircle.io/account/adding-google-play-service-account|
|Huawei AppGallery| https://docs.appcircle.io/account/adding-huawei-api-key|

## Publish Profile

### Adding a Publish Profile

After building the application, we can start the publishing process by sending it to the Publish module.

For this, it is necessary to first create a publish profile within the Publish module. Afterwards, the relevant publish profile must be selected from the **Distribution** tab in the configuration of the relevant profile in the Build module.

In order to create a publish profile, click on the "Add New" button in the Publish module.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-add-new.png' />

You should give a descriptive name to the relevant publish profile.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-new-profile.png' />

The publish profile is created, and it's ready for application submission.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-empty-profile.png' />

### Build Profile Configuration

Go to the build profile that we will send to the Publish module, and select the publish profile from the **Distribution** tab in the configuration.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-build.png' />

:::tip
When selecting the publish profile from **Build profile -> Configuration -> Distribution**, more than one target profile can be selected.
:::

Now the build profile is ready for application publishing.

When the build is successful, Appcircle will send the version of the relevant application to the selected publish profiles in the Publish module.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-build-success.png' />

### Publish Flow

Appcircle includes a predefined flow in the Publish module for publishing the application to stores (App Store, Google Play, Huawei AppGallery). This flow can be customized according to your specific publishing requirements.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-flow-button.png' />

When you click on the **Publish Flow** button, the list of steps included in the publish flow will appear.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-flow-w.png' />

We can access the list of steps that can be used in a publish workflow by clicking on the **Manage Flow** button. You can add or remove new steps and customize your publish workflow as you wish.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-workflows.png' />

You can effortlessly obtain a **YAML** file of your current Publish Flow configurations on our platform with the **Download YAML** button at the bottom.
By simply selecting the download option, you'll receive a YAML file containing all the details of your existing workflow setup.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-download-workflow.png' />

Customize your workflows effortlessly by uploading your YAML file with the **Replace Flow** button at the top.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-replace-flow-button.png' />

Simply select the file containing your desired configurations and integrate them seamlessly into the platform.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-upload-workflow.png' />

### Publish Settings

When a build is completed on the Build module and its artifacts are distributed to the Publish module, we can start the publish process to the stores using the **Auto Publish** toggle in **Settings**.

Your configured publish flow will be executed automatically when you enable **Auto Publish**.

You can also select a runner pool from the **SELECT A POOL** dropdown list.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-settings.png' />

"Default Intel Pool" and "Default M1 Pool" are Appcircle cloud-hosted pools and only available for the cloud services.

If there are any self-hosted pools in your organization, you can also select them from the list. Self-hosted Appcircle users will only see the self-hosted pools in this list.

<ContentRef url="/self-hosted-appcircle/self-hosted-runner/configure-runner/manage-pools">
  Self-hosted Pools
</ContentRef>

:::info
If group or variable definitions have been made in **Publish Variables**, you will see the list of variable groups in **Settings**, and you can select one or more of them to use in your publish flow.
:::

### Publish Variables

Variables, similar to the [environment variables](../environment-variables/index.md) in build, can be defined in this section to be used specifically in the publish flow for store submissions.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-variables.png' />

To use these defined variables, it will be necessary to select them from the [Publish Settings](#publish-settings).

### Rename Publish Profile

Appcircle allows previously created Publish profiles to be renamed.

To do this, click on the three dots at the top right of the relevant publish profile in the profiles list and select **Rename**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-rename.png' />

:::caution
Publish profile names must be unique for both **`iOS`** and **`Android`**.

For example, if you have a Publish profile named **`My Great App`** for iOS Publish, Appcircle will not allow you to create a profile named **`My Great App`** again for Android Publish or iOS Publish.

Also, you cannot rename a Publish profile to an existing name on the same platform.
:::

### Delete Publish Profile

To delete the Publish profile, click on the three dots at the top right of the relevant Publish profile in the profiles list and select **Delete**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-remove.png' />

:::caution
Appcircle **does not delete** the application that has been submitted to the stores.

By deleting the Publish profile, all the application versions and Publish action logs related to that publish profile will be removed on the Appcircle side.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-remove-confirm.png' />

## Publish Versions

### Add Version

Appcircle supports publishing the application to the stores without using the Build module. To add an application version manually, you need to add a publish profile beforehand and then **Open** its details.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-manuel.png' />

You can then upload the application by clicking on the **Add Version** button on the right.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-upload.png' />

When the upload is completed successfully, the relevant application version will appear in the list.

Afterwards, you can start submitting your application to the stores with the publish flow that you have configured.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-version-list.png' />

For this, click on the **Actions** button for the relevant version and go to **Details**. From there, you can manually **Start Flow** for the uploaded application version.

### Version History

You can browse the history of the previous publishing actions of the related application version with the **History** button on the **Actions** menu opened by clicking the three dots on the version list.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-history-button.png' />

The list of publishing actions performed with the relevant application version will appear in the **Publish History**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-history-list.png' />

When you click on an item in the list, you can see the detailed publishing logs.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-history-log.png' />

### Version Download

Appcircle allows you to download the published application artifact for all listed versions. For this, you can click on the **Download** button on the **Actions** menu opened by clicking the three dots on the version list.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-download.png' />

### Version Delete

Appcircle allows you to delete the published application versions. For this, you can click on the **Delete** button on the **Actions** menu opened by clicking the three dots on the version list.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-delete.png' />

You should confirm the **Delete** action by entering the version name into the dialog box, which prevents unintentional version removals.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-delete-confirm.png' />

:::caution
Appcircle does not delete the application that has been submitted to the stores. This deletion will only delete the version of the application in the Publish module.
:::
