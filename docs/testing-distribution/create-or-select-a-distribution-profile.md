---
title: Distribution Profile
description: Learn how to create or select a distribution profile for testing in Appcircle
tags: [distribution, testing, distribution profile]
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

To share builds with testers, distribution profiles should be created and testing groups assigned to these profiles.

## Creating a Profile

Select the Testing Distribution from the left and click on the Add New button. Give a name to your distribution profile.

:::info

As a best practice, we recommend using one single distribution profile for both iOS and Android versions of the same application.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4163-main1.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4163-update.png' />

### Profile Actions

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4163-profilenew.png' />

#### Rename a Distribution Profile

The Distribution Profile can be renamed by following these steps:

- Click on the three dot on the top right of the profile menu.
- Click `Rename`.
- Enter the new name for your profile.

#### Pin a Distribution Profile

The Distribution Profile can be pinned by following these steps:

- Click on the three dot on the top right of the profile menu.
- Click `Pin Item`.

Pinned profiles will stand out by appearing first in the list, making them easily accessible and distinguishable from the rest of the profiles. A pin icon will also be displayed on their profile card.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4163-main22.png' />

#### Delete a Distribution Profile

To remove clutter and/or free up storage, an entire profile can be deleted with a single click:

- Click on the three dot on the top right of the profile menu.
- Click `Delete`.
- Go through the confirmation dialog.

:::info

To free up space, other references pointing to the artifact should also be removed. For example, if the same artifact is present in the builds, those artifacts should also be deleted.

:::

## Uploading Binary

### Manual Binary Upload

Pre-built iOS or Android applications can be uploaded for distribution or preview by using the upload field on the right panel (if no version is available) or the "Upload New Version" button at the bottom right (if versions are already present) to upload files to the distribution profile.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4163-main7.png' />

After the file is uploaded, it is checked for errors and parsed for metadata. Any errors that occur will be displayed in the upload area.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (156).png' />

Once the upload is complete, the new version will be added to the top of the list with parsed metadata. This version can then be shared with testers or previewed on a virtual device in the browser.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4163-main8.png' />

:::info

Please note that iOS and Android binaries are displayed in separate tabs. The required OS tab should be clicked to navigate between them.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4163-update2.png' />

### Upload via Build Module

With a successful build, a new version of the application will be added to the distribution profile.

Simply go to _Build Module_ _>_ _Build Configuration_ _>_ _Distribution_ and select a distribution profile you want your build to be sent.

:::tip

The Android build output can be selected as .AAB (Android App Bundle) from the configuration settings within the Build profile.

When the `.AAB` build is sent to the designated Testing Distribution profile, either automatically or manually by uploading the file directly within the Testing Distribution profile, it will be automatically converted to `.APK` format when shared with a Testing Group. This ensures that the `.APK` format is used for the artifact downloaded by the receiving tester.

This conversion capability also applies when app versions are sent from a Testing Distribution profile to an [Enterprise App Store](/enterprise-app-store) profile. The shared `.AAB` artifact will be converted and downloaded in `.APK` format from the Enterprise App Store profile.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-3167-buildoutput.png' />

:::caution

Only signed builds will be distributed. Unsigned builds will not be distributed.

:::

#### Android applications with multiple flavors

For detailed information about multiple flavors, refer to this documentation:

<ContentRef url="/best-practices/building-multiple-apps-in-one-profile">Building Multiple Apps in One Profile</ContentRef>

If multiple product flavors are present in your Android application, a build will be created for each flavor, allowing for simultaneous distribution. A common use case for multi-flavor applications includes offering free and paid versions of the same application.

When an application with multiple flavors is built and distributed, an `.apk` file will be created for each flavor. Once distributed, all of the binaries will be visible on the distribution profile

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4163-main9.png" />

#### How to see the multiple flavor results

If you also want to download or see the output, you can check through the following steps within the Build Profile:

- Click the three dot under the actions tab
- Click **Download Artifacts** to see all the build outputs.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4163-main10.png' />

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4163-main11.png" />

:::info

If your Git commit has any messages, they will be included in the distribution in Message To Testers area.

:::

### Upload using API & CLI

If you use your own CI structre, you can use our Appcircle API & CLI to upload binaries to your Distribution Profile.

To get more information, please refer to our [API & CLI](/appcircle-api-and-cli) documentation.

## Settings

The settings of your distribution profile can be customized. Click on the distribution profile, then click the settings button within the profile.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4163-main2.png' />

### Information

The Info tab allows you to enter the publisher information for your distributed applications.

You can submit your **Publisher Name**, **Contact Email**, **Privacy Policy URL**, and **Terms of Service URL**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4071-info.png' />

Once you click the save button, the information you have provided will be displayed on the Tester Portal.

<ContentRef url="/distribute/downloading-binaries">Tester Portal</ContentRef>

When the tester selects the user icon, the Publisher Information will be displayed.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4071-info2.png' />

It will also display the Login Method for the Testing Distribution Profile.

In the example image, the profile has static authentication method, so it is displayed as Static Login.

You can find out more about the login methods in the [using authentication for distribution](/testing-distribution/create-or-select-a-distribution-profile#authentication) section.

### Auto Send

Auto send feature lets your applications be distributed to specific testing groups whenever a new version is deployed, whether the deployment is triggered via a build process, CLI, or manual upload.

To enable the auto send feature, you need to create testing groups and add testers to these groups.

<ContentRef url="/distribute/testing-groups">Testing Groups</ContentRef>

Under the Auto Send tab in the settings, you can see the testing groups you have created earlier. Just enable each testing group you want to have your application sent automatically whenever a new version is deployed.

The first section allows you to share the deployed binaries automatically with the selected groups. They will receive a link to download the specific version on their mobile devices.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4163-main3.png' />

Your application will be sent to the related testing groups as soon as your build is complete, or when a package is manually uploaded or deployed via CLI.

### Authentication

Under the Authentication tab in the settings, you can select a preferred authentication method for sharing your application. This will be the login method for the [Testing Portal](/testing-distribution/testing-portal).

- **None**: No authentication, anyone with the link can download binary files
- **Static Username and Password**: One single username and password for all testers
- **SSO Login**: SSO login for all testers (Enterprise accounts only)
- **LDAP Login**: LDAP login for all testers (Enterprise accounts only)

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4163-main4.png' />

To add your SSO and LDAP details, go to [My Organization](/account/my-organization) Security screen and press the "Connect" button next to SSO Login or LDAP Login under the "Authentications" section.

<ContentRef url="/account/my-organization/security/authentications/distribution-sso-authentication">SSO Login</ContentRef>
<ContentRef url="/account/my-organization/security/authentications/distribution-ldap-authentication">LDAP Login</ContentRef>

:::info

If SSO and LDAP details are not configured for your organization, these authentication methods will not be visible in the Distribution Profile settings.

:::

### Public Link

You may enable a public link for your distribution. This allows anyone who has the link to access all artifacts of the distribution profile. Additionally, users can now conveniently scan a QR code to retrieve the public link directly. This simplifies the process of accessing and sharing the distribution link, making it more accessible for users on mobile devices or others who prefer quick scanning.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4163-main6.png' />

:::info

The Tester Portal that you will have access via the Public Link, will have the same authentication method that you have set from the authentication settings.

:::

## Share Binary

### Share your application with the test groups manually

Once your build is ready or the binary file is uploaded to Appcircle, the file can be manually sent to testers for downloading, installing on their devices, and running the application for testing purposes.

Click on the 'Share with Testers' button, and the [testing groups](/testing-distribution/testing-groups) previously created can be selected to receive this version of your application. Alternatively, email addresses of testers can be entered here to send the application directly, bypassing the testing groups.

You can also add a message to testers including testing instructions and release notes.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4163-main14.png' />

You can automate this message using [Release Notes Component](https://github.com/appcircleio/appcircle-release-notes-component/). You can enrich the contents of your release notes with environment variables or Ruby snippets. The following default template will print the branch name, commit hash and commit message.

```ruby
Branch: $AC_GIT_BRANCH
Commit Hash:  <%= ENV['AC_GIT_COMMIT'][0..6] %>
Commit Message: $AC_COMMIT_MESSAGE
```

:::info

If you are using the self-hosted version of Appcircle, you can configure it to use your own business domain for distribution emails instead of the default noreply@appcircle.io address. For details on how to configure SMTP settings in a self-hosted installation see [Email Integration](https://docs.appcircle.io/self-hosted-appcircle/configure-server/integrations-and-access/integration#email).

:::

The Distribution Profile name will be displayed as the sender name in the email address that testers will receive.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4163-mail.png' />

:::tip

After sharing your app versions with testers, the most recent sharing time will be displayed on your testing distribution profile card.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4163-share.png' />

### Tracking your distribution

After sending your application to testing groups, you can track the actions of testers:

- **Pending** - Means your tester didn't click on the link they received yet.
- **Clicked** - Means your tester clicked on the link they received but has not logged in to the system yet (only for authenticated distributions).
- **Login, No Download** - Means your tester has logged in (for authenticated distributions) and at the download screen but has not downloaded the binary file yet.
- **Downloaded** - Means your tester clicked and downloaded the binary file.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4163-main15.png' />

## Binary Actions

### Binary Details

1. Select the binary.

You can either select the files from the list or upload binaries by clicking the **Upload New Version** button at the bottom.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4163-ios9.png' />

2. Click the **...** button and select **Binary Details**

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4163-ios14.png' />

3. This window provides information about your binary, including the provisioning profile type, certificate name, and build details, such as the branch and logs.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5184-binary.png' alt="Binary Details" />

### Send your application to Enterprise App Store

You can send your application from your Testing Distribution profile to an Enterprise App Store profile by following these steps:

- Click the three dots next to your application.
- Click **Send to Enterprise App Store**.
- Click **Send**.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4163-enterprise1.png" />

:::info

Appcircle will not ask you to pick a profile after choosing the **Send to Enterprise App Store** option. If the binary is unique, it will create the Enterprise App Store profile automatically. If the same app version already exists within the profiles, it will be delivered within that profile.

:::

### Send your application to Publish

You can send your application from your Testing Distribution profile to a designated Publish profile by following these steps:

- Click the three dots next to your application.
- Click **Send to Publish**.
- Choose your Publish profile from the list.
- Click **Send**.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4163-main12.png" />

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4163-main13.png" />

:::caution

You must have already created the designated Publish profile within the Publish Module, and it should correspond to the operating system of your application (Android or iOS) listed in your Testing Distribution Profile.

:::

### Re-sign Binary

Resigning is the process of modifying an existing binary with a new signing certificate or keystore, which is required when an application needs to be published under a different developer account or when updating an existing application. It involves removing the original signature and replacing it with a new one.

For more information please visit the Re-sign Binary documentation.

### Re-sign History

Re-sign History allows you to view the re-sign process logs for your app versions. For more information, please visit [Re-sign History](/testing-distribution/resigning-binaries#re-sign-history) documentation.

### Download Binary

The binary file in the Testing Distribution profile can be downloaded by selecting the Download button from the actions menu.

<Screenshot url='https://cdn.appcircle.io/docs/assets/TD-Binary-Download.png' />

### Delete Multiple Testing Distribution App Versions

If you don't want to delete an entire distribution profile but free up the past distributions, you can also remove multiple entries.

Click on the `Edit` Text to toggle edit mode:

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4163-main17.png' />

On edit mode, you will be able to select multiple entries. Select the versions you wish to delete, and click on the `Delete` Text on the top right of the versions:

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4163-main18.png' />

### Delete a Single Distribution App Version

As an alternative method to bulk deleting versions, you can delete a single version by selecting the three-dot menu next to the app version and then clicking **delete** button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4163-main19.png' />

After clicking `Delete` , type in the version name in the prompt.


## FAQ

#### Can I set an authentication method for accessing the Testing Portal?

Yes, you can choose one of the authentication methods provided by Appcircle to authenticate your users and control their access to the store. For more information, please visit the Testing Distribution [**Authentication**](/testing-distribution/create-or-select-a-distribution-profile#authentication) documentations.

#### Can I send a binary from another CI tool?

Yes, you can use Appcircle **API & CLI** tools within your current CI tool to directly send the binary and utilize it within the Testing Distribution. For more information, please visit the [**Appcircle API & CLI**](/appcircle-api-and-cli) documentations.


#### What does email/month mean? How is the number calculated?

An email is calculated every time an app is shared via email from our servers. So every send email adds to email count.

#### Do you offer plans specific to Enterprise App Store (without CI/CD features)?

Thanks to the modular structure of Appcircle, all modules can be used independently. Accordingly, you can also request a special plan only for Testing Distribution. Please [contact us](https://appcircle.io/contact) for detailed information.