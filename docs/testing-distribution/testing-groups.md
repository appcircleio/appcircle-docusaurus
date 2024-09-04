---
title: Testing Groups
description: Manage your testers with Testing Groups. Distribute different app versions based on OS, features, and devices.
tags: [testing, group, distribution, testers]
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

This action automatically removes them from the unsubscribed list, allowing them to receive emails once again.

A prominent orange warning message confirms the successful re-subscription process, ensuring a seamless experience.

<Screenshot url='https://cdn.appcircle.io/docs/assets/2630-ManagingUnsubscribedUsers.png' />

:::info
If a user who has previously unsubscribed is included in a test group, they will not be re-subscribed when sharing with the test group.
:::

## FAQ

### What is the tester limit for app distribution?

Appcircle provides a scalable solution, allowing you to add as many testers as you need without stringent limitations. This ensures you can conduct thorough testing across a wide range of devices and user scenarios. Appcircle also offers flexible group management, so you can easily organize testers into different groups based on testing needs.

### Why have I not received the e-mail after sharing the app version via Appcircle ? 

There could be several reasons why you haven't received the email after sharing the app version with your testers:

- The recipient might be unsubscribed.
- The email may have arrived in the junk folder.
- Company firewall rules might cause delays of up to 30 minutes.
- The Appcircle domain may need to be whitelisted.