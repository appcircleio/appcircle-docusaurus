---
title: Enterprise App Store Profile
description: Learn how to create an Enterprise App Store profile in Appcircle
tags: [enterprise app store, enterprise profile, enterprise app store setup, faq]
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';
import PatDanger from '@site/docs/\_pat-usage-workflows-danger.mdx';
import EnvGroupSetCaution from '@site/docs/\_env-group-set-on-config-caution.mdx';
import NewerVersionCodeCaution from '@site/docs/\_newer-version-code-caution.mdx';

The Enterprise App Store provides a centralized platform for managing an organization’s mobile applications. This guide will outline the essential steps involved in setting up the profile, uploading application binaries, configuring profile settings, and executing actions on the uploaded binaries.

## Creating a Profile

An Enterprise build profile can be created in several ways. IPA or APK files can either be manually uploaded or sent from Appcircle’s Distribution, Build, or Publish modules.

## Uploading Binary

Uploading binaries to the Enterprise App Store is an important step in managing an organization’s mobile applications. Several methods are offered by the platform to perform this action, each catering to different stages of the application lifecycle. The available options for uploading a binary are listed below:

### Manual Binary Upload

- If no profile has been created before, the following screen will be displayed. The **Add New App** button should be clicked to open the upload panel.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4225-upload1.png' />

- Choose your APK or IPA file and click the **Upload** button.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-upload2.png" />

- If a valid APK or IPA file has been uploaded, a brand new profile should be displayed.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4225-profile2.png' />

:::caution

Ensure that the bundle ID matches the current profile and that the version or build number differs from the other files in the list.

:::

### Upload via Build Module

Binaries can also be uploaded via the Build module. For more information, please visit the [Build Configuration](/build/build-process-management/configurations#distribution-configuration) and [Build Actions](/build/build-process-management#binary-actions) documentations.

### Upload via Testing Distribution Module

Binaries can also be uploaded via the Testing Distribution module. For more information, please visit the [Testing Distribution](/testing-distribution/create-or-select-a-distribution-profile#send-your-application-to-enterprise-app-store) documentation.

### Upload via Publish Module

The Publish Flow steps can be customized to send the binary to the Enterprise App Store. For more information, please visit the [Publish Integrations](/publish-integrations/common-publish-integrations/send-to-enterprise-app-store) documentation.

### Upload via API & CLI

The above tasks can also be initiated using the Appcircle CLI. The Appcircle CLI documentation should be checked for the command line parameters.

<ContentRef url="/appcircle-api-and-cli">Appcircle CLI</ContentRef>

### Upload via Appcircle Marketplace

You can also upload binaries from other CI tools using ready-to-use plugins.

<ContentRef url="/marketplace">Appcircle Marketplace</ContentRef>

## Profile Actions

Several key actions are available within the Enterprise App Store to manage and interact with profiles efficiently. The descriptions of the available profile actions are provided below:

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4225-profile3.png' />

#### 1. **Open**
The "Open" action allows entry into a specific profile, providing access to all details and settings associated with that profile. By selecting "Open" the apps, binaries, and configurations linked to the profile can be viewed and managed.

#### 2. **Pin**
The "Pin" action allows a profile to be prioritized by pinning it to the top of the profile list. When a profile is pinned, it remains easily accessible, especially when multiple profiles are managed. This action is particularly useful for frequently accessed profiles, ensuring they stay at the forefront of the workflow.

#### 3. **Delete**
The "Delete" action results in the permanent removal of a profile from the Enterprise App Store. Once a profile is deleted, all associated data, including uploaded binaries and settings, is also erased.

:::info

Unlike profiles from other modules within Appcircle, Enterprise App Store profiles cannot be manually named or renamed. Instead, the binary names will be displayed for these profiles.

:::

## Profile Settings

After the profile has been created, it should be configured and sent to different users and channels.

Profile information can be accessed, and users can be added to grant them access to the Live and Beta channels by clicking the **Settings** button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4225-profile4.png' />

### Information

The Profile ID can be copied from the Info tab by clicking the copy icon located on the right side of the displayed ID.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE6223-toggle5.png" />

#### Show on Top

The **Show on Top** feature allows you to prioritize app versions by displaying them at the top of the list in their respective channels within the Enterprise Portal.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE6223-toggle2.png" />

:::caution
Please note that due to the caching model in the service, updates may take up to 10 minutes to take effect.
:::

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4070-8.png" />

#### Hide Certificate Details

Enabling the Hide Certificate Details toggle in the Enterprise App Store profile settings will hide the certificate information associated with the iOS and Android app versions on the Enterprise Portal. This helps maintain confidentiality by preventing end users from viewing the certificate used to sign the application binaries. 

This setting applies across all listed versions under the selected profile.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE6223-toggle3.png" />

#### Binary Tags

The Binary Tags feature allows you to label your application binaries with meaningful metadata, which is displayed on the Enterprise Portal for easy identification by users.

These tags help testers understand each binary's origin, purpose, and how it was triggered. The available tags are:
- Commit ID
- Commit Hash
- Commit Message
- Commit Author
- Git Source Branch
- Trigger Reason
- Git Target Branch
- Git Tag
- Trigger User
- Build Profile ID
- Workflow Name
- Configuration Name

:::info Build Module Dependency

This section appears only if the binary is distributed to the Enterprise App Store profile from the Build Module.

Uploaded binaries without metadata from a build module won’t show the selected tags on the Enterprise Portal.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6223-toggle4.png' />

Binary tags can be managed through the Enterprise App Store Profile Settings under the Info tab:
1. Navigate to **Enterprise App Store** module.
2. Select the relevant profile.
3. Click the **Settings** icon.
4. Under the **Info** tab, locate the **Binary Tags** section.
5. Use the “Add a new tag” field to enter or select tags.
6. Click **Save** to apply changes.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6223-toggle1.png' />

Once tags are saved in the profile settings:
- Tags will automatically appear next to the app version on the Enterprise Portal after being published to a channel.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6099-ss10.png' />
<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6099-ss11.png' />

#### In-App Update Secret

In-app updates enable applications to deliver and install updates directly within the app, enhancing user experience by minimizing disruption.

For more information, please visit [In-App Updates](/enterprise-app-store/in-app-updates) documentation.

### Manage Access

Multiple users can be added to the Beta and Live channels by pressing the Tab key.

Defined user groups from your provider can also be added after configuration.

:::info
Email entries are not case-sensitive; however, group names are case-sensitive.
:::

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE5950-ss.png" />

:::important

To configure the Manage Access tab, the authentication method for the Enterprise Portal must be set to either SSO or LDAP. For more information about authentication types, please refer to the [Portal Settings](/enterprise-app-store/portal-settings#store-authentication) documentation.

:::

:::caution
If a sub-organization is being worked for, visibility will be limited to the apps within that organization. However, if an app is published, it will also be displayed in the showcase of the parent organization on the Enterprise Portal.

User permissions within the Enterprise App Store can be managed using **Okta SAML**. By configuring authorization groups through **Okta** and subsequently applying these group names to **Alpha** or **Beta** channels via Appcircle, access will be restricted to only the relevant users.

For further details, please refer to the document: [Okta Managing User Groups](/account/my-organization/security/authorization/store-sso-authorization).
:::

:::info
If Beta Channel Access is not configured, versions marked for the Beta channel will not be visible to anyone by default.

If Live Channel Access is not configured, versions marked for the Live channel will be visible to everyone by default.

:::

### Links

The Enterprise App Store allows users to publish app versions to either the Beta or Live channels. 

Once published, these versions can be accessed via direct links or QR codes, facilitating easy distribution and installation.

To retrieve the direct links or QR codes for published app versions, follow these steps:

- In the selected app profile, go to the Settings section.
- Click on the Links tab to view the available Beta and Live channel links.
- If the app version is published to either the Beta or Live channels, the corresponding direct link and QR code will be displayed.
- Click the Copy button next to the link to copy it for sharing. Alternatively, you can use the QR code image to access via mobile devices.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE5857-ent8.png" />

:::info
If no app versions are published to either channel, the links and QR codes will not be available.
:::

:::warning Link Usage
Always use the original share link from EAS → Profile → Settings, as sharing the redirected URL may prevent users from accessing the required app version if the published version is later changed or removed.
:::

## Binary Actions

### Binary Information

This window provides information about your binary, including the provisioning profile type, certificate name, and build details, such as the branch and logs.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6767-eas1.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6767-eas8.png' />

#### Build Metadata Details

The following metadata is displayed in the Binary Details section of a Enterprise App Store Profile only when the binary is generated via the Build Module, either through automatic or manual triggers, and subsequently distributed using Auto Distribution to the Enterprise App Store module.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6767-eas4.png' />

- **Trigger Type**: Indicates what initiated the build. Possible values include:

1. Pull Request: The build was triggered by the creation or update of a pull request.
2. User: A build was manually triggered by a user.
3. Commit: A new commit triggered the build automatically.
4. Tag: The build was initiated when a new Git tag was pushed to the repository.

- **Branch Name**: The source branch used during the build process.
- **Target Branch**: Typically used in pull request or merge-based triggers, this is the destination branch for the pull request or merge target.
- **Git Tag**: If the trigger type is Tag, this field shows the tag that initiated the build.
- **Triggered Internal User**: Displays the email address of the internal user who triggered the build or the user responsible for the action.
- **Workflow Name**: The name of the workflow profile name executed during the build process (e.g., Default Push Workflow).
- **Config Name**: Indicates the configuration profile name used within the selected workflow (e.g., Default Configuration).

#### Binary Comparison

In the top-right corner of the Binary Information screen, you can click the **Compare** button to compare the current binary with another of your choice. The comparison highlights differences between the two binaries using color-coded indicators for easy identification.

:::caution Build Details Comparison

Binaries generated through the Appcircle Build Module include associated build details. **However**, if the compared binary was **manually** uploaded to Appcircle, those details **will not be available** for comparison.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6767-eas2.png' />
<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6767-eas3.png' />

### Publish

The Enterprise App Store module includes two channels: Beta and Live.

- **Beta Channel**: This channel can be used for testing new updates, features, or changes before they are rolled out to all users. The beta channel is ideal for trialing updates without affecting the broader user base, ensuring that everything works as expected before being moved to production.
- **Live Channel**: The live channel serves as the production environment where all end users interact with the Enterprise App Store. This channel may contain stable, fully tested binary versions.

Apps can be sent to the Beta or Live channels by hitting the `...` button and then selecting the **Publish** menu.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6767-eas5.png' />

The channel can be selected, and a summary and release notes for the release can be written. Once the **Publish** button is clicked, the particular binary will be made available to all beta users.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE5939-ss2.png" />

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE5939-ss3.png" />

A version can be sent to the Live Channel in two ways:

- Click the **Publish** button and select **Live** for the channel.
- Click the ... button for any beta build and select **Go Live** from the menu.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6767-eas10.png' />

:::info

Only **one binary version** can be sent to the Live and Beta channels. When another Beta or Live binary version is sent, the previous app version in that channel will be replaced.

:::

:::tip

Any app versions published by sub-organizations to the **Live** or **Beta** channel will be available in the Enterprise Portal created by the root organization for users to view and download.

:::

When a binary is published to the Live or Beta channel, it will be displayed with the corresponding channel tag. This information will also be shown in the profile header within the profile and on the profile card in the Enterprise App Store profile list.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-tags.png" />

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-profiles.png" />

:::info

If two binaries are published to the Beta and Live channels, the profile header will display the binary from the Live channel.

:::

#### Publish as Unlisted

The **‘Publish as Unlisted’** feature allows users to provide direct access to an app version in the Enterprise Portal without listing it with the other published app versions. This ensures that the app version is accessible only via a direct link, without appearing in the general app list.

When publishing an app version to either Beta or Live channels, you can enable the ‘Publish as Unlisted’ toggle.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE5939-ss1.png" />

If enabled, the app version will not be displayed in the Enterprise Portal App List.

You can access the app version only through a direct link, which can be obtained from the Profile Settings > [Links](/enterprise-app-store/enterprise-app-store-profile#links) section.

Other applications published in the Enterprise Portal will not be visible to users accessing via this unlisted link. You can always use the main Enterprise Portal link which is located within the [Portal settings](/enterprise-app-store/portal-settings#store-domain), in order to access the rest of the app list.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE5857-ent0.png" />

:::info Authentication Method
•	The authentication process for accessing an Unlisted app remains the same as the Enterprise Portal’s configured [authentication](/enterprise-app-store/portal-settings#store-authentication) settings.
:::

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE5939-ss6.png" />

:::tip
App versions that were published to the Beta or Live channels as unlisted will display an **'Unlisted'** tag in the app version list within the Enterprise App Store profile.
:::

#### Unpublish

Any binary can be removed from the Live or Beta channels by selecting the **Unpublish** action from the actions menu.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6767-eas9.png' />

### Download

The binary artifact in the Enterprise App Store profile can be downloaded by selecting the Download button from the actions menu.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6767-eas6.png' />

### Delete

Binaries in the Enterprise App Store profiles can be deleted by clicking the Delete button in the actions menu.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6767-eas7.png' />

:::info

Please note that you **cannot** delete a binary that is published to the Beta or Live channels. You must unpublish it before you can delete it.

:::

## Apple Enterprise Program

The Apple Developer Enterprise Program allows large organizations to develop and deploy proprietary, internal-use apps directly to their employees. This program is designed for specific use cases that require private distribution through secure internal systems or a Mobile Device Management solution.

The Apple Developer Enterprise Program is intended solely for the internal use and distribution of proprietary apps in scenarios that are not adequately addressed by public apps on the App Store, custom apps through Apple Business Manager, Ad Hoc distribution, or beta testing via TestFlight.

https://developer.apple.com/programs/enterprise/


:::danger Apple Enterprise Program

**Please note that** if you have an **Apple Developer** account with an **Enterprise Organization** and you are using an app signed with an [**Enterprise Certificate**](/signing-identities/apple-certificates) for **internal distribution**, you must use [**authentication**](https://docs.appcircle.io/enterprise-app-store/store-customization#authentication) for user access.

Apple does not allow public distribution of internally distributed apps, and if Apple detects that you are distributing an app signed with an Enterprise certificate without using authentication, it will impose severe sanctions.

You can access the relevant terms and conditions from the links below and get detailed information.

- [**Apple Developer Enterprise Program License Agreement**](https://developer.apple.com/support/terms/)
    - Please navigate the `Apple Developer Enterprise Program License Agreement` section and see Section 2.1 on page 8 for **usage and restrictions**, and Section 11.2 on page 34 for **terms and terminations**.

:::

## Enterprise App Store FAQ

#### What is Enterprise App Store?

Enterprise App Store is Appcircle's new feature that lets you create your own mobile app store for your in-house apps (apps that are not meant to be distributed through Apple's App Store and Google Play Store).

#### What is the difference between Enterprise App Store and Testing Distribution

[**Testing Distribution**](/testing-distribution) is a process designed to facilitate the manual testing of new builds by internal or third-party teams, ensuring that each iteration is thoroughly validated before final release.

[**Enterprise App Store**](/enterprise-app-store), on the other hand, serves as the final distribution method, offering a secure and branded experience for internal customers.

Understanding the difference between these two methods is essential for effective internal distribution, ensuring that the right version of your app reaches the right audience at the right time.

https://appcircle.io/blog/understanding-the-difference-between-testing-distribution-and-enterprise-app-store

#### Can non-Enterprise companies use this feature?

Yes. From small teams to large enteprises, anybody can create their own app store.

#### How can I get a binary from another organization to use in the Enterprise App Store ?

Let’s assume there are two organizations: Organization A and Organization B.
In Organization A, we have a build profile that generates an IPA, APK, or AAB.
In Organization B, we have a Enterprise App Store profile that we want to send the binary to.

In Organization A's build profile workflow, after the build step, we can add a [Custom Script](/workflows/common-workflow-steps/custom-script/) step that includes the code snippet below to transfer the binary generated in Organization A to the Enterprise App Store profile in Organization B. In order to do this, we need [Appcircle CLI](/appcircle-api-and-cli/cli-authentication), so this code snippet sets up the necessary information and sends binary with parameters.

#### Upload binary for an already existing Enterprise App Store profile

```bash
#Bash script
sudo npm install -g @appcircle/cli
appcircle login personal-access-key --secret $ORG_B_PERSONAL_ACCESS_KEY
# If an IPA or AAB is required, change *.apk to *.ipa or *.aab
appcircle enterprise-app-store version upload-for-profile \
  --entProfileId "$ORG_B_ENT_APP_STORE_PROFILE_ID" \
  --app "$AC_OUTPUT_DIR"/*.apk
```

#### Uploads a binary and creates the Enterprise App Store profile if it does not already exist

```bash
#Bash script
sudo npm install -g @appcircle/cli
appcircle login personal-access-key --secret $ORG_B_PERSONAL_ACCESS_KEY
# If an IPA or AAB is required, change *.apk to *.ipa or *.aab
appcircle enterprise-app-store version upload-without-profile \
  --app "$AC_OUTPUT_DIR"/*.apk
```

This will also generate a new Enterprise App Store profile and application will be sent into this profile.

<NewerVersionCodeCaution />

The key point here is that we need two essential parameters to make this work.
- `$ORG_B_PERSONAL_ACCESS_KEY` => Personal Access Key from Organization B.
- `ORG_B_ENT_APP_STORE_PROFILE_ID` => Enterprise App Store profile ID from Organization B.
- `$AC_OUTPUT_DIR` => Automatically defined by the system. See [Reserved Variables](/environment-variables/appcircle-specific-environment-variables/).

To generate Personal Access Key, follow this [documentation](/account/my-organization/security/personal-access-key#generatingmanaging-the-personal-access-keys)

To obtain the Enterprise App Store profile ID, follow the steps below: 
1. Log in to organization B.
2. Go to Enterprise App Store module.
3. Select the desired Enterprise App Store profile
4. Copy it from the URL. `https://my.appcircle.io/enterprise-store/profiles/123456f-7d89-4545-5454-123456789abc`
5. Then the Enterprise App Store profile ID is => `123456f-7d89-4545-5454-123456789abc`

After collecting the required parameters, set the following values as [Environment Variables](/environment-variables/):
- `ORG_B_PERSONAL_ACCESS_KEY`
- `ORG_B_ENT_APP_STORE_PROFILE_ID`

<PatDanger />

<EnvGroupSetCaution />

#### What kind of apps can I put to my Enterprise Portal

As long as they are signed with an Ad Hoc or Enterprise Distribution Certificate, all apps with .ipa or .apk/.aab files can be uploaded.

#### Can we customize our Enterprise Portal and how?

Yes. You can customize your logo, primary and secondary color and the main text color.

#### How will users enter my Enterprise Portal?

Once you go to your portal's settings in Appcircle, you can define a prefix and Appcircle will give you a URL with the given prefix. Alternatively, you can use your own domain. (Not eligible on Starter plans. Please [contact us](https://appcircle.io/contact) to request custom domains).

#### Can I set an authentication method for accessing the Enterprise Portal?

Yes, you can choose one of the authentication methods provided by Appcircle to authenticate your users and control their access to the portal. For more information, please visit the Enterprise App Store [**Store Authentication**](/enterprise-app-store/portal-settings#store-authentication) documentations.

#### Can I send a binary from another CI tool?

Yes, you can use Appcircle API & CLI tools within your current CI tool to directly send the binary and utilize it within the Enterprise App Store. For more information, please visit the [**Appcircle API & CLI**](/appcircle-api-and-cli) documentations.

#### Is my app store accessible from desktop web?

Yes. Desktop users can access your app portal and view the available apps through your store's URL. To install and run an app, you need to open the store from a mobile device. Desktop website will display a QR code next to your portal to pen the page from mobile devices easily.

#### How can I create an Enterprise Distribution Certificate on iOS?

You have to be enrolled on [Apple Enterprise Developer Program](https://developer.apple.com/programs/enterprise/) ($299/year). You can alternatively use Ad Hoc certificates if you aren'a a member of the Enterprise Developer program (see question below).

#### Can I distribute apps signed with Ad Hoc / App Store Provisioning Profile from my Enterprise Portal?

You can distribute apps that are signed with an Ad Hoc certificate (iOS). Please note that your users' device identifiers must be added to Apple Developer Portal and should be included in the provisioning profile used in signing the build. Apps signed with App Store certificates can't be distributed.

#### What does downloads/month mean? How is the number calculated?

A download is calculated every time an app is downloaded from our servers. So a user downloading an app, updating to a new version and re-installing any version adds to the download count.

#### Do you offer plans specific to Enterprise App Store (without CI/CD features)?

Thanks to the modular structure of Appcircle, all modules can be used independently. Accordingly, you can also request a special plan only for Enterprise App Store. Please [contact us](https://appcircle.io/contact) for detailed information.