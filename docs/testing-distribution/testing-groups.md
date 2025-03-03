---
title: Testing Groups
description: Manage your testers with Testing Groups. Distribute different app versions based on OS, features, and devices.
tags: [testing, group, distribution, testers, ldap]
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';

# Testing Groups

The testing group feature is used to manage and organize testers. Different versions of applications can be distributed to specific groups based on testing needs, such as OS versions, features, devices, and more.

The testing groups feature allows for the definition of various groups for different audiences. For instance, in an enterprise, groups such as testing team, marketing, management, and other functional groups can be created. For an app developer, testing groups can be created for customers and apps. This enables streamlined management of binary sharing flows. Apps can be sent manually to these groups, or different distribution profiles can be associated with different groups for automatic distribution.

You can list, add, edit and manage your groups and testers from this module.

<Screenshot url='https://cdn.appcircle.io/docs/assets/06-10-TestingGroups.png' />

Click on the orange + button to create a new testing group. You can name groups according to your needs, such as "Alpha," "Beta," and so on. After typing the name of the new testing group, press enter to create it.

<Screenshot url='https://cdn.appcircle.io/docs/assets/06-11a-NewTestingGroup.png' />

After a new testing group is created, tester email addresses can be added to the group. The input box at the top of the page should be used to enter the email address, and pressing enter will add it.

A list of your testers will now be displayed. Testers can be selected and deleted as needed.

<Screenshot url='https://cdn.appcircle.io/docs/assets/06-11-EditTestingEmails.png' />

Also by clicking on the edit button next to your testing group name from the list, you can rename, duplicate or delete your testing group if you need to.

<Screenshot url='https://cdn.appcircle.io/docs/assets/06-12-EditTestingGroup.png' />

### Managing Unsubscribed Users

When re-sharing the app with users who have previously unsubscribed, you can seamlessly re-engage them.

Click on the **Share with Testers** button from the distribution profile. Then, simply add the users who have unsubscribed to the recipients.

This action automatically removes them from the unsubscribed list, allowing them to receive emails once again.

A prominent orange warning message confirms the successful re-subscription process, ensuring a seamless experience.

<Screenshot url='https://cdn.appcircle.io/docs/assets/2630-ManagingUnsubscribedUsers.png' />

:::info
If a user who has previously unsubscribed is included in a test group, they will not be re-subscribed when sharing with the test group.
:::

## Importing Testing Group Members via LDAP

If you have a LDAP Mapping in place for your users, you can import them into your Testing Group profile.

For LDAP configuration and mapping, please refer to the [LDAP](/account/my-organization/security/authentications/distribution-ldap-authentication) documentation.

1. **Create or Select a Testing Group**:  
   Either create a new Testing Group in Appcircle or select an existing one.

2. **Import Group Members from LDAP**:
    - Click on the three dots in the top-right corner.
    - Select the **Import From LDAP** option.

   **Note**: The Testing Group must not contain any members. If it does, attempting to import from LDAP will result in an error.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5678-import.png' />

3. **Select LDAP Configuration**:
    - Choose the LDAP configuration from the dropdown menu.
    - Select the LDAP Group from which you want to import members.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-3990-menu.png' />

4. **Preview LDAP Group Members**:  
   The members of the LDAP Group will be displayed in the UI as a preview. This allows you to review the members before importing. At this stage, the members are not yet imported into the Testing Group.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-3990-config.png' />

5. **Determine Sync Frequency**:
   Select a time frame for automatic sync process. Once Testing Group linked to the LDAP Group, it will sync the group members periodically.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-3990-sync.png' />

6. **Sync Group Members**:  
   Click the **Sync Now** button to import and store the LDAP group members in the Testing Group.

**Note:** Clicking **Save** to complete the process will also be sufficient to import the members.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-3990-imported.png' />

7. **Update LDAP Group Configuration**:  
   After linking the Testing Group to the LDAP Group, you can update the LDAP configuration in the same way it was imported.

Testing Groups that use the LDAP sync feature will be marked with a tag displaying the selected LDAP group.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-3990-final.png' />

:::caution

It is not possible to add or remove members of Testing Group on UI manually after establishing a link to LDAP Group.

However, the testing group can still be renamed, duplicated and deleted.

:::

#### Disable LDAP Import Settings

Users can disable LDAP import settings for an LDAP-imported Testing Group by clicking the ‘Disable LDAP Import Settings’ button in the top right corner. 

Note that this option is only available for Testing Groups that have already imported their members via LDAP settings. 

After disabling the settings, existing members will remain, and users can manually add or remove members as needed.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5678-import2.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5678-import3.png' />

## FAQ

### What is the tester limit for app distribution?

Appcircle provides a scalable solution, allowing you to add as many testers as you need without stringent limitations. This ensures you can conduct thorough testing across a wide range of devices and user scenarios. Appcircle also offers flexible group management, so you can easily organize testers into different groups based on testing needs.

### Why have I not received the e-mail after sharing the app version via Appcircle ? 

There could be several reasons why you haven't received the email after sharing the app version with your testers:

- The recipient might be unsubscribed.
- The email may have arrived in the junk folder.
- Company firewall rules might cause delays of up to 30 minutes.
- The Appcircle domain may need to be whitelisted.