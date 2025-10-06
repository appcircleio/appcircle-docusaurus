---
title: App Store Connect API Key
description: Learn how to generate an App Store Connect API Key for linking your Apple Developer account to Appcircle
tags: [account, my organization, api integrations, app store connect, app store connect api key]
sidebar_position: 2
slug: /account-and-organization/my-organization/security/credentials/adding-an-app-store-connect-api-key
---

import Screenshot from '@site/src/components/Screenshot';

# App Store Connect API Key

<iframe width="560" height="315" src="https://www.youtube.com/embed/A0OgvrX5L-U" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

You can add, delete and manage iOS Certificates and Provisioning Profiles manually using Appcircle. There is also an easier way. By linking your Apple Developer account to Appcircle, you can see a list of certificates and provisioning profiles and pick the ones you want to use for building and distributing.

To link your Apple Developer account, **you need an App Store Connect API Key** from Apple's **App Store Connect Panel**.

## Login to App Store Connect

Go to [https://appstoreconnect.apple.com](https://appstoreconnect.apple.com) and login with your account.

<Screenshot url='https://cdn.appcircle.io/docs/assets/app-store-connect-logged-in-low (1).jpg' />

:::caution

Make sure that the correct team is selected on the top right. For developer accounts that belong to multiple teams, this is important.

:::

Once the team is correct, select **Users and Access** from the menu:

<Screenshot url='https://cdn.appcircle.io/docs/assets/app-store-connect-logged-in-selected-low (1).jpg' />

After navigating to **Users and Access**, you will see 4 tabs next to the title. Select the **Integrations** tab. Then make sure that **App Store Connect API** is selected from the list on the left.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5630-AppStoreConnect-keys.png' />

## Generating a New Key

To generate a new key, press the + button.

:::caution

Only Account Holders can enable the API Key generation. If you see a disabled **Request Access** button, contact your account holder and make them follow the steps above. After they request access, you can create new keys.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/api-keys-add-new-low (1).jpg' />

A modal popup will ask you to enter a name and add roles for this key:

<Screenshot url='https://cdn.appcircle.io/docs/assets/api-keys-new-modal-low.jpg' />

:::caution

The Admin access is required to create new and download certificates or provisioning profiles. You can also give access to certain users, and on per app basis, but they require additional configuration from Apple Developer Portal.\
\
To see a list of permissions each role has, visit: [https://developer.apple.com/support/roles/](https://developer.apple.com/support/roles/)

:::

### Downloading the Key

After generating the key, download the key file by pressing Download API Key next to it.

<Screenshot url='https://cdn.appcircle.io/docs/assets/download-api-key-low (2).jpg' />

:::caution

**You can only download the file once**. If you lose the file, you need to generate a new key.

:::

## Linking Appcircle with App Store Connect

Adding a key to Appcircle is pretty easy. **Go to your organization** by selecting the bottom left button from the toolbar:

<Screenshot url='https://cdn.appcircle.io/docs/assets/FE1719-ss1.png' />

On the Organization screen, select **Add New** on **App Store Connect API Keys **list item**:**

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5765-api1.png' />

On the form, upload the **.p8** key file downloaded from App Store Connect:

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5765-api2.png' />

Fill in the rest of the form. You can find the **Key ID** and **Issuer ID** from App Store Connect Panel here:

<Screenshot url='https://cdn.appcircle.io/docs/assets/keyid-issuerid-low (1).jpg' />

Copy and paste them to the form in Appcircle, give it a name, and save.

:::info

You can add multiple keys. We'll ask you which key to use while downloading a certificate.

:::

### Enterprise API Key Option for App Store Connect

The App Store Connect Enterprise API Key is a crucial component for managing Apple Enterprise accounts within Appcircle. This API key allows seamless integration with App Store Connect, enabling automated provisioning, certificate management, and distribution processes for enterprise applications.

#### Prerequisites

Before using the App Store Connect Enterprise API Key, ensure that:
- You have an Apple Developer Enterprise Program account.
- You have Admin or Account Holder privileges in App Store Connect.
- Your App Store Connect account supports API access.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5765-api3.png' />

### Adding the API Key to Appcircle

Once the API key is generated, it must be added to Appcircle:

1.	Navigate to the Organization module in Appcircle.
2.	Click **Add New** next to the App Store Connect API Keys section under Credentials area.
3.	Upload the downloaded .p8 file.
4.	Enter the Key ID and Issuer ID obtained from App Store Connect.
5.	Select the Enterprise API Key option for enterprise account integration.
6.	Click Save to complete the setup.

:::info
Please note that the registered Enterprise API Key cannot be used within the Publish module because the Apple Enterprise Program does not provide TestFlight or App Store Connect services.
:::

## Sharing App Store Connect Credentials

Root Organization users have the ability to share their saved credentials with Sub-Organization users. This feature helps streamline credential management across distributed teams and multiple organizational units.

#### How to Share Credentials

<Screenshot url='https://cdn.appcircle.io/docs/assets/FE1719-ss2.png' />

**1.**	Navigate to the Credentials Section
Go to My Organization > Security > Credentials.

**2.** Open Manage Panel
Click the respective credential type (e.g., App Store Connect API Keys) to view your saved credentials.

**3.** Select the Credential
Click the Share icon under the Actions column for the credential you want to share.

**4.** Configure Sharing Settings
In the Share Credentials panel:
- Enter or confirm the Settings Name.
- Toggle Share with all sub-organizations if you want to make the credential available to all sub-organizations automatically.
- Alternatively, manually select specific sub-organizations that should have access by checking the boxes under Sub-Organizations.

**5.** Save Sharing Configuration
Once your selections are made, click Share to apply.

<Screenshot url='https://cdn.appcircle.io/docs/assets/FE1719-ss3.png' />

Shared credentials will be visible and usable in the selected Sub-Organizations as if they were their own.

:::info
Sub-Organizations cannot edit or delete credentials shared by the Root Organization.
:::

The shared credentials by the Root Organization will be marked with Root Tag on the Sub Organization's credential list. 