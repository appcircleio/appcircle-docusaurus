---
title: Google Play Service Account
description: Learn how to add a Google Play Service Account to your Appcircle account
tags: [account, my organization, api integrations, google play service account]
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';

# Google Play Service Account

Google Service Account is required to upload your binary to Google Play Store. This JSON key must be added to your account to publish apps to Google Play.

1. Please go to [Google Cloud Platform](https://console.cloud.google.com/apis) and create a Google Cloud Project.

2. **Enable** the `Google Play Android Developer API` for your Google Cloud Project. 

    <Screenshot url='https://cdn.appcircle.io/docs/assets/google-service00.01.png' />

    <Screenshot url='https://cdn.appcircle.io/docs/assets/google-service00.02.png' />


    :::danger

    Skipping this step will result in your JSON being rejected by Appcircle because it will not have access to the project.

    :::


3. Login with your account, then head over to **Credentials -> Create Credentials**, and then click **Service account**.

    <Screenshot url='https://cdn.appcircle.io/docs/assets/google-service01.png' />

4. This screen will forward you to the **Create service account** page. Fill in the details of your service account. According to the service name you set, an automatic **Service account ID** will be created.

    <Screenshot url='https://cdn.appcircle.io/docs/assets/google-service03.png' />

5. Please select `Editor` in the Role dropdown.

    <Screenshot url='https://cdn.appcircle.io/docs/assets/google-service04.png' />

6. Click Done to save this account.

    <Screenshot url='https://cdn.appcircle.io/docs/assets/google-service05.png' />

7. Click **Manage service accounts** to open manage page.

    <Screenshot url='https://cdn.appcircle.io/docs/assets/google-service05-1.png' />

8. Find the account you have just created. Click three dots on the Actions column, and then click **Manage keys**.

    <Screenshot url='https://cdn.appcircle.io/docs/assets/google-service06.png' />

9. Click **ADD KEY** and then click **Create new key**.

    <Screenshot url='https://cdn.appcircle.io/docs/assets/google-service07.png' />

10. Download your key as JSON and save it.

    <Screenshot url='https://cdn.appcircle.io/docs/assets/google-service08.png' />

11. Go to [Google Play Console](https://play.google.com/console) and login with your account and then head over to **User and permissions** and then click **Invite new users**.

    <Screenshot url='https://cdn.appcircle.io/docs/assets/google-service09-2.png' />

12. Add the email, generated in step 6 in the **E-mail address** field.

    <Screenshot url='https://cdn.appcircle.io/docs/assets/google-service12.png' />

13. Check the permissions of your user.

    <Screenshot url='https://cdn.appcircle.io/docs/assets/google-service11-1.png' />

Make sure this account has access to **Releases**, **Store presence**, and **App access** (for read-only ones).

    <Screenshot url='https://cdn.appcircle.io/docs/assets/google-service11.png' />

Then click **Invite User**. Your account key is ready. 🎉

14. To add the key on Appcircle, follow these steps:

    a. Navigate to [My Organization](/account/my-organization).

    b. Locate the `Google Play Developer API Keys` under the `Credentials` section.
  
    c. Click the `Manage` button if you have saved keys, or directly click the `Add New` button.

    <Screenshot url='https://cdn.appcircle.io/docs/assets/google-service14.png' />

## Sharing Google Play Developer Credentials

Root Organization users have the ability to share their saved credentials with Sub-Organization users. This feature helps streamline credential management across distributed teams and multiple organizational units.

#### How to Share Credentials

<Screenshot url='https://cdn.appcircle.io/docs/assets/FE1719-ss8.png' />

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

<Screenshot url='https://cdn.appcircle.io/docs/assets/FE1719-ss9.png' />

Shared credentials will be visible and usable in the selected Sub-Organizations as if they were their own.

:::info
Sub-Organizations cannot edit or delete credentials shared by the Root Organization.
:::

The shared credentials by the Root Organization will be marked with Root Tag on the Sub Organization's credential list.

## FAQ

**Can I retrieve the JSON private key that I uploaded to Appcircle?**

No, for security reasons, you cannot download the JSON file you uploaded to Appcircle.

**Why cannot I save the JSON after uploading it?**

You might have missed the first step. Please ensure that you have enabled the Service Account.
