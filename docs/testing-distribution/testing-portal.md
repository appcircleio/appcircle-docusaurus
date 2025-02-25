---
title: Testing Portal
description: Learn how to use the Testing Portal for downloading binaries. Streamline your app testing process with Appcircle.
tags: [appcircle, testing, portal, distribution]
sidebar_position: 4
---

import Screenshot from '@site/src/components/Screenshot';

# Testing Portal

Appcircle has a separate distribution screen designed to make it easy for test group developers and testers download the distributed applications easily.

For iOS and Android, the testers can login from the link shared and then view all the versions shared with them. Downloading iOS and Android binaries are done through the specific flows of each OS.

## Login

When a build is shared with testers, each tester will receive an email with a link to download the binary file and other details like version number and release notes.

When the link is clicked, users will then be redirected to the testing portal.;

:::info

The accounts used in the testing portal are completely independent from Appcircle accounts and only used for downloading shared apps.

:::

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4071-portalentry.png" />

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE5183-mobile1.png" alt="Mobile Login"/>

:::info

Please note that the log out option is available only if an active authentication method is present in your testing distribution profile.

:::

:::warning

Please note that to login to the Testing Portal, you must enable cookies in your browser. Cookies help maintain your session and ensure secure access.

Refer to your browser's settings to enable cookies:

**Chrome**: Settings > Privacy and security > Cookies.
**Safari**: Preferences > Privacy.

:::

## Listing and Downloading Binary

Once logged in, users can now see the list of distributions separated by distribution profile and release version. Files can be downloaded with one click.

:::caution

For running iOS apps signed with an enterprise certificate, you may need to trust the certificate provider after installing the app.

For installing Android apps, you may need to grant the web browser "install apps from unknown sources" permission so that the apps downloaded from the portal can be installed.

:::

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE5183-main.png" alt="Testing Portal Main Page" />

The Testing Portal will also display the size and the certificate type of each app version. For more information on certificate types, please visit the [Signing Identities](/signing-identities) section.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE5183-size.png" alt="Testing Portal Binary Size" />

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

The Testing Portal supports English, German, French, and Turkish.

For desktop usage, it will detect and apply your browser's language if it is supported.

For mobile devices, it will detect the device language.

If the detected language is not supported, the default language will be English.

:::

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4071-language.png" />

## Search Binary

The search bar can be used to filter the available app version list by *app names**, **app versions**, **release notes**, and **build numbers**. 

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE5183-search.png" alt="Testing Portal Search Bar"/>

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE5183-mobile2.png" alt="Mobile Search" />

### Search By Branch

The Testing Portal will provide a dropdown menu containing the source branches of the listed binaries, allowing users to quickly search for the required branch for a clearer display.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE5183-branch.png" alt="Filter by Branch" />

:::tip
If the branch filter is not visible, it may be because the binary was uploaded manually to the Testing Distribution module instead of being sent via the Build module.
:::

### Sort Binaries by Version & Date

The listed binaries on the Testing Portal can be sorted by version or the date they were shared, based on user preferences. This can be toggled using the Date and Version buttons located above the binary list.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE5183-sort.png" alt="Sort by Date or Version" />

## Navigating Between Shared App Profiles

Users can view other distributed app versions from different testing distribution profiles by selecting the menu icon in the top left corner.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4071-portal4.png" />

The Shared App Profiles section allows testers to view other testing distribution profiles that have a shared app version associated with their email address.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4163-portal.png" />

The list will display the other testing distribution profiles along with their authentication methods.

:::caution
**Re-authentication Rules:**
- When switching between profiles that use different authentication methods (e.g., STATIC to SSO), users must log in again to access the new profile.
- If both the current and target profiles use SSO or LDAP, no re-authentication is needed when switching.
- If both profiles use STATIC authentication, re-authentication is required.
:::

For more information about authentication methods, please refer to the [Using Authentication for Distribution](/testing-distribution/create-or-select-a-distribution-profile#authentication) section.

:::info
**Profile Visibility:**
- If public link access is enabled for a profile, it will be visible and accessible from other profiles within the same organization in the testing portal, regardless of whether it has been shared via email.
- The visibility is based on the profile the user is currently logged into, and is not influenced by the type of authentication used.
- If a user gains access to the Testing Portal through a shared public link, they will not be able to navigate to profiles with public link access disabled unless those profiles have been shared with their email.
:::

For more information about using public links, please visit the [using public link for distribution](/testing-distribution/create-or-select-a-distribution-profile#public-link) documentation.

## Profile Information

#### Profile Card

When the user icon is selected, the distribution profile information will be displayed. This information can be updated from the [Info](/testing-distribution/create-or-select-a-distribution-profile#information) tab within the profile settings.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4071-info2.png' />

The Login Method for the Testing Distribution Profile will also be displayed.

In the example image, the profile has a static authentication method, so it is displayed as Static Login.

You can find out more about the login methods in the [using authentication for distribution](/testing-distribution/create-or-select-a-distribution-profile#authentication) section.

:::info
Please note that the Privacy and Terms URLs are optional. If they have not been configured within the Info tab of your profile settings, they will not be visible in the Testing Portal.
:::
