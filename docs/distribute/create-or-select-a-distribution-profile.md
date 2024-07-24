---
title: Testing Distribution Profile
description: Learn how to create or select a distribution profile for testing in Appcircle
tags: [distribution, testing, distribution profile]
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

Select the Testing Distribution from the left and click on the Add New button. Give a name to your distribution profile.

:::info

As a best practice, we recommend using one single distribution profile for both iOS and Android versions of the same application.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (152).png' />

Once you create the distribution profile, you can now customize its settings. Click on the newly created build profile and then the settings button within the profile.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (153).png' />

### Publisher Information

The Info tab allows you to enter the publisher information for your distributed applications. 

You can submit your **Publisher Name**, **Contact Email**, **Privacy Policy URL**, and **Terms of Service URL**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4071-info.png' />

Once you click the save button, the information you have provided will be displayed on the Testing Portal. 

If the tester selects the user icon, they will be able to see the Publisher Information.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4071-info2.png' />

It will also display the Login Method for the Testing Distribution Profile. 

In the example image, the profile has static authentication method, so it is displayed as Static Login. 

You can find out more about the login methods on [using authentication for distribution](/distribute/create-or-select-a-distribution-profile#using-authentication-for-distribution) section.

### Auto send your build to the testers

Auto send feature lets your applications be distributed to specific testing groups whenever a new version is deployed, whether the deployment is triggered via a build process, CLI, or manual upload.

To enable the auto send feature, you need to create testing groups and add testers to these groups.

<ContentRef url="/distribute/testing-management/testing-groups">Testing Groups</ContentRef>

Under the Auto Send tab in the settings, you can see the testing groups you have created earlier. Just enable each testing group you want to have your application sent automatically whenever a new version is deployed.

The first section allows you to share the deployed binaries automatically with the selected groups. They will receive a link to download the specific version on their mobile devices.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (192).png' />

Your application will be sent to the related testing groups as soon as your build is complete, or when a package is manually uploaded or deployed via CLI.

### Using authentication for distribution

Under the Authentication tab in the settings, you can select a preferred authentication method for sharing your application.

- **None**: No authentication, anyone with the link can download binary files
- **Static Username and Password**: One single username and password for all testers
- **SSO Login**: SSO login for all testers (Enterprise accounts only)
- **LDAP Login**: LDAP login for all testers (Enterprise accounts only)

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (154).png' />

To add your SSO and LDAP details, go to [My Organization](/account/my-organization) Integrations screen and press the "Connect" button next to SSO Login or LDAP Login under the "Connections" section.

<ContentRef url="/account/my-organization/sso-providers-configuration/single-sign-on">SSO Login</ContentRef>
<ContentRef url="/account/my-organization/ldap-login">LDAP Login</ContentRef>

### Device Registration (iOS Only)

You may enable this option to automatically register devices in the Apple Developer Portal and update your Ad Hoc provisioning profiles. You must select App Store Connect API Key, a build profile, and a configuration.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ios-device-registration.png' />

### Using Public Link for Distribution

You may enable a public link for your distribution. This allows anyone who has the link to access all artifacts of the distribution profile. Additionally, users can now conveniently scan a QR code to retrieve the public link directly. This simplifies the process of accessing and sharing the distribution link, making it more accessible for users on mobile devices or others who prefer quick scanning.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3160-testing-distribution-public-link.png' />

### Manually upload your version

If you have pre-built iOS or Android applications and want to distribute or preview them for testing, you can upload them using the upload field on the right panel (if no version is available) or using the "Upload New Version" button at the bottom right (if there are versions already present) to upload your files to the distribution profile.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (157).png' />

After the file is uploaded, it is checked for errors and parsed for metadata. If there is an error, it is displayed on the upload area.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (156).png' />

Once the upload is complete, you will see the new version added to the top of the list with parsed metadata. You can now share this version with the testers or preview it on a virtual device in your browser.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (158).png' />

###

### New version from build module

With a successful build, a new version of your application will be added to your distribution profile.

Simply go to _Build Module_ _>_ _Build Configuration_ _>_ _Distribution_ and select a distribution profile you want your build to be sent.

:::tip

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-3167-buildoutput.png' />

Users have the capability to select their Android build output as .AAB (Android App Bundle) from configuration settings within their Build profile.

When the `.AAB` build is sent to the designated Testing Distribution profile, either automatically or manually by uploading the file directly within the Testing Distribution profile, it will be automatically converted to `.APK` format when shared with a Testing Group. This ensures that the receiving tester downloads the shared artifact in `.APK` format.

This conversion capability also applies when sending app versions from a Testing Distribution profile to an [Enterprise App Store](/enterprise-appstore) profile. The shared `.AAB` artifact will be downloaded in `.APK` format from the Enterprise App Store profile.

:::

:::caution

Only signed builds will be distributed. Unsigned builds cannot be distributed.

:::

### Android applications with multiple flavors

For detailed information about multiple flavors, refer to this documentation:

<ContentRef url="/best-practices/building-multiple-apps-in-one-profile">Building Multiple Apps in One Profile</ContentRef>

If your Android application has multiple product flavors, Appcircle will create a build for each flavor of your application and let you distribute them at once. A common usage to multi-flavor applications can be free and paid versions of the same application.

When you build and distribute an application with multiple flavors, and `.apk` file will be created for each flavor. When the build is distributed, all of the binaries will be seen on the distribution profile:

<Screenshot url="https://cdn.appcircle.io/docs/assets/testing-android-multi-flavor.png" />

#### How to see the multiple flavor results

If you also want to download or see the output, you can check through the following steps:

- Click the three dot under the actions tab
- Click **Artifacts** to see all the build outputs.

<Screenshot url='https://cdn.appcircle.io/docs/assets/testing-android-multi-flavor-download-artifacts.png' />

<Screenshot url="https://cdn.appcircle.io/docs/assets/testing-android-multi-flavor-artifacts.png" />

:::info

If your Git commit has any messages, they will be included in the distribution in Message To Testers area.

:::

### Send your application to Publish

You can send your application from your Testing Distribution profile to a designated Publish profile by following these steps:

- Click the three dots next to your application
- Click **Send to Publish**
- Choose your Publish profile from the list.
- Click **Send**

<Screenshot url="https://cdn.appcircle.io/docs/assets/be-3110-sendpublish.png" />

<Screenshot url="https://cdn.appcircle.io/docs/assets/be-3110-sendpublish2.png" />

:::caution

You must have already created the designated Publish profile within the Publish Module, and it should correspond to the operating system of your application (Android or iOS) listed in your Testing Distribution Profile.

:::

### Share your application with the test groups manually

When you have your build ready or uploaded your binary file to Appcircle, you can manually send the file to testers to let them download, install on their devices and run the application for testing purposes.

Click on the Share with Testers button and select the testing groups you created previously that need to receive this version of your application. Alternatively, you can enter email addresses of the testers here to send them the application regardless of the testing groups.

You can also add a message to testers including testing instructions and release notes.

<Screenshot url='https://cdn.appcircle.io/docs/assets/06-07a-SendToTesterGroups.png' />

You can automate this message using [Release Notes Component](https://github.com/appcircleio/appcircle-release-notes-component/). You can enrich the contents of your release notes with environment variables or Ruby snippets. The following default template will print the branch name, commit hash and commit message

```ruby
Branch: $AC_GIT_BRANCH
Commit Hash:  <%= ENV['AC_GIT_COMMIT'][0..6] %>
Commit Message: $AC_COMMIT_MESSAGE
```

###

### Tracking your distribution

After sending your application to testing groups, you can track the actions of testers:

- **Pending** - Means your tester didn't click on the link they received yet
- **Clicked, No Login** - Means your tester clicked on the link they received but has not logged in to the system yet (only for authenticated distributions)
- **Login, No Download** - Means your tester has logged in (for authenticated distributions) and at the download screen but has not downloaded the binary file yet
- **Downloaded** - Means your tester clicked and downloaded the binary file

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (158).png' />

### Delete a Distribution Profile

In order to remove clutter and/or free up storage, you can delete an entire profile in a single click.;

- Click on the three dot on the top right of the profile menu
- Click `Delete`
- Go through the confirmation dialog

<Screenshot url='https://cdn.appcircle.io/docs/assets/testing-delete-distribution-profile.png' />

:::info

In order to free up space, you should also remove the other references pointing to the artifact. In example, if you have the same artifact on the builds, you should also delete those artifacts as well.

:::

#### Delete Multiple Testing Distribution Versions

If you don't want to delete an entire distribution profile but free up the past distributions, you can also remove multiple entries.

Click on the `Edit` Text to toggle edit mode:

<Screenshot url='https://cdn.appcircle.io/docs/assets/testing-delete-multiple-edit-button.png' />

On edit mode, you will be able to select multiple entries. Select the versions you wish to delete, and click on the `Delete` Text on the top right of the versions:

<Screenshot url='https://cdn.appcircle.io/docs/assets/testing-delete-multiple-delete-button.png' />

#### Delete a Single Distribution Profile Version

As an alternative method to bulk delete versions, you can delete a single version at the three dot menu on the top right of the screen.;

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (205).png' />

After clicking `Delete` , type in the version name in the prompt.
