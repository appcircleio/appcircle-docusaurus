---
title: Using the Testing Portal
description: Learn how to use the Testing Portal for downloading binaries. Streamline your app testing process with Appcircle.
tags: [appcircle, testing, portal, distribution]
sidebar_position: 4
---

import Screenshot from '@site/src/components/Screenshot';

# Using the Testing Portal

Appcircle has a separate distribution screen designed to make it easy for test group developers and testers download the distributed applications easily.

For iOS and Android, the testers can login from the link shared and then view all the versions shared with them. Downloading iOS and Android binaries are done through the specific flows of each OS.

When a build is shared with testers, each tester will receive an email with a link to download the binary file and other details like version number and release notes.

When the link is clicked, users will then be redirected to the distribution portal.;

If your distribution requires enrollment, users will be asked to create an enrollment account. If your distribution requires a login, users will be asked to log into the distribution portal.

:::info

The accounts used in the testing portal are completely independent from Appcircle accounts and only used for downloading shared apps.

:::

<Screenshot url="https://cdn.appcircle.io/docs/assets/10-14-EnrollLogin.jpg" />

Once logged in, users can now see the list of distributions separated by distribution profile and release version. Files can be downloaded with one click.

:::caution

For running iOS apps signed with an enterprise certificate, you may need to trust the certificate provider after installing the app.

For installing Android apps, you may need to grant the web browser "install apps from unknown sources" permission so that the apps downloaded from the portal can be installed.

:::

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4071-portal2.png" />

The Testing Portal will also display the size and the certificate type of each app version. For more information on certificate types, please visit the [Signing Identities](/signing-identities) section.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4071-size.png" />

:::tip
Users can use the search bar to filter the available app version list for **app names**, **app versions**, **release notes** and **build numbers**. 
:::

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4071-portal5.png" />

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4071-portal.png" />

:::tip

The Testing Portal includes a toggle feature that allows users to switch between two display modes for the app version's upload time. 

By default, the Testing Portal displays the time for the selected app version as a relative time (e.g., "2 hours ago").

To view the exact date and time of the upload, simply click on the relative time display. The display will switch to show the exact date and time (e.g., "July 4, 2024 AT 10:30 AM").

:::

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4071-dates1.png" />

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4071-dates2.png" />

:::info
If your app version has an enterprise-type certificate, the Testing Portal will display a guidance message on how to proceed with the installation on your device.
:::

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4071-enterprise.png" />

:::tip 

The Testing Portal supports English, German, French, and Turkish. It will detect your browser's language and apply it if it is supported. If your browser's language is not supported, the default language will be English.

:::

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4071-language.png" />

## Shared App Profiles

Users can view other distributed app versions from different testing distribution profiles by selecting the menu icon in the top left corner.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4071-portal4.png" />

The Shared App Profiles section allows testers to view other testing distribution profiles that have a shared app version associated with their email address.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4071-portal3.png" />

The list will display the other testing distribution profiles along with their authentication methods.

:::caution

While navigating between shared profiles, if a profile requires authentication, users will need to log in again to gain access.

:::

For more information about authentication methods, please refer to the [Using Authentication for Distribution](/distribute/create-or-select-a-distribution-profile#using-authentication-for-distribution) section.

:::info

If you are using a public link to access the Testing Portal, you can only navigate between testing distribution profiles that have public links enabled.

For more information about using public links, please visit the [using public link for distribution](/distribute/create-or-select-a-distribution-profile#using-public-link-for-distribution) documentation.

:::

## Logging Out of the Testing Portal

Users can log out of the Testing Portal by following these steps:

1. **Click the Profile Icon:**
    - Locate and click on the profile icon in the top right corner of the screen.

2. **Display the Profile Card:**
    - Clicking the profile icon will open the profile card, which displays the publisher information.

3. **Click the Logout Button:**
    - In the profile card, find and click the **Logout** button.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4071-logout.png" />

:::info

The log out option is available only if your testing distribution profile has an active authentication method.

:::
