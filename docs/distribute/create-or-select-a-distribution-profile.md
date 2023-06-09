---
title: Create a Distribution Profile and Sharing with Testers
metaTitle: Create a Distribution Profile and Sharing with Testers
metaDescription: Create a Distribution Profile and Sharing with Testers
sidebar_position: 1
---

import ContentRef from '@site/src/components/ContentRef';
import NarrowImage from '@site/src/components/NarrowImage';

# Create a Distribution Profile and Sharing with Testers

<iframe width="600" height="315" src="https://www.youtube.com/embed/vZ3p5uZZcmk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

In order to share your builds with testers, you can create distribution profiles and assign testing groups to the distribution profiles.

:::info

A distribution profile corresponds to the multiple versions of the same application for iOS and Android.

:::

###

### Create a distribution profile

Select the Distribute module from the left and click on the Add New button. Give a name to your distribution profile.

:::info

As a best practice, we recommend using one single distribution profile for both iOS and Android versions of the same application.

:::

![](<https://cdn.appcircle.io/docs/assets/image (152).png>)

Once you create the distribution profile, you can now customize its settings. Click on the newly created build profile and then the settings button within the profile.

![](<https://cdn.appcircle.io/docs/assets/image (153).png>)

### Auto send your build to the testers

Auto send feature lets your applications to be distributed to specific testing groups whenever a new version is deployed.

To enable the auto send feature, you need to create testing groups and add testers into these groups.

<ContentRef url="/distribute/testing-groups">Testing Groups</ContentRef>

Under the Auto Send tab in the settings, you can see the testing groups you have created earlier. Just enable each testing group you want to have your application sent automatically whenever a new version is deployed.

The first section allows you to share the deployed binaries automatically with the selected groups. They will receive a link to download the specific version on their mobile devices.

![](<https://cdn.appcircle.io/docs/assets/image (192).png>)

Your application will be sent to the related testing groups as soon as your build is complete.

### Using authentication for distribution

Under the Authentication tab in the settings, you can select a preferred authentication method for sharing your application.

- **None**: No authentication, anyone with the link can download binary files
- **Static Username and Password**: One single username and password for all testers
- **SSO Login**: SSO login for all testers (Enterprise accounts only)
- **LDAP Login**: LDAP login for all testers (Enterprise accounts only)

![](<https://cdn.appcircle.io/docs/assets/image (154).png>)

To add your SSO and LDAP details, go to [My Organization](../account/my-organization.md) Integrations screen and press the "Connect" button next to SSO Login or LDAP Login under the "Connections" section.

### Device Registration (iOS Only)

You may enable this option to automatically register devices in the Apple Developer Portal and update your Ad Hoc provisioning profiles. You must select App Store Connect API Key, a build profile, and a configuration.

![](<https://cdn.appcircle.io/docs/assets/ios-device-registration.png>)


### Using public link for distribution

You may also enable public link for your distribution. If you enable public distribution, anyone who has the link can access all artifacts of the distribution profile.


![](<https://cdn.appcircle.io/docs/assets/image (155).png>)



### Manually upload your version

If you have pre-built iOS or Android applications and want to distribute or preview them for testing, you can upload them using the upload field on the right panel (if no version is available) or using the "Upload New Version" button at the bottom right (if there are versions already present) to upload your files to the distribution profile.

![](<https://cdn.appcircle.io/docs/assets/image (157).png>)

After the file is uploaded, it is checked for errors and parsed for metadata. If there is an error, it is displayed on the upload area.

![](<https://cdn.appcircle.io/docs/assets/image (156).png>)

Once the upload is complete, you will see the new version added to the top of the list with parsed metadata. You can now share this version with the testers or preview it on a virtual device in your browser.

![](<https://cdn.appcircle.io/docs/assets/image (158).png>)

###

### New version from build module

With a successful build, a new version of your application will be added to your distribution profile.

Simply go to _Build Module_ _>_ _Build Configuration_ _>_ _Distribution_ and select a distribution profile you want your build to be sent.

:::info

Only signed builds will be distributed. Unsigned builds cannot be distributed.

:::

### Android applications with multiple flavors

For detailed information about multiple flavors, refer to this documentation:

<ContentRef url="/best-practices/building-multiple-apps-in-one-profile">Building Multiple Apps in One Profile</ContentRef>

If your Android application has multiple product flavors, Appcircle will create a build for each flavor of your application and let you distribute them at once. A common usage to multi-flavor applications can be free and paid versions of the same application.

When you build and distribute an application with multiple flavors, and `.apk` file will be created for each flavor. When the build is distributed, all of the binaries will be seen on the distribution profile:

<NarrowImage src="https://cdn.appcircle.io/docs/assets/image%20(250).png" />

#### How to see the multiple flavor results

If you also want to download or see the output, you can check through the following steps:

- Click on the **Builds** tab on your desired branch
- Click the three dot under the actions tab
- Click **Artifacts** to see all the build outputs.

![](<https://cdn.appcircle.io/docs/assets/image (249).png>)

<NarrowImage src="https://cdn.appcircle.io/docs/assets/image%20(248).png" />

:::info

If your Git commit has any messages, they will be included in the distribution in Message To Testers area.

:::

### Share your application with the test groups manually

When you have your build ready or uploaded your binary file to Appcircle, you can manually send the file to testers to let them download, install on their devices and run the application for testing purposes.

Click on the Share with Testers button and select the testing groups you created previously that need to receive this version of your application. Alternatively, you can enter email addresses of the testers here to send them the application regardless of the testing groups.

You can also add a message to testers including testing instructions and release notes.

![](https://cdn.appcircle.io/docs/assets/06-07a-SendToTesterGroups.png)

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

![](<https://cdn.appcircle.io/docs/assets/image (158).png>)

### Delete a Distribution Profile

In order to remove clutter and/or free up storage, you can delete an entire profile in a single click.;

- Click on the three dot on the top right of the profile menu
- Click `Delete`
- Go through the confirmation dialog

![](<https://cdn.appcircle.io/docs/assets/image (200).png>)

:::info

In order to free up space, you should also remove the other references pointing to the artifact. In example, if you have the same artifact on the builds, you should also delete those artifacts as well.

:::

#### Delete Multiple Testing Distribution Versions

If you don't want to delete an entire distribution profile but free up the past distributions, you can also remove multiple entries.

Click on the `Edit` Text to toggle edit mode:

![](<https://cdn.appcircle.io/docs/assets/image (202).png>)

On edit mode, you will be able to select multiple entries. Select the versions you wish to delete, and click on the `Delete` Text on the top right of the versions:

![](<https://cdn.appcircle.io/docs/assets/image (204).png>)

#### Delete a Single Distribution Profile Version

As an alternative method to bulk delete versions, you can delete a single version at the three dot menu on the top right of the screen.;

![](<https://cdn.appcircle.io/docs/assets/image (205).png>)

After clicking `Delete` , type in the version name in the prompt.
