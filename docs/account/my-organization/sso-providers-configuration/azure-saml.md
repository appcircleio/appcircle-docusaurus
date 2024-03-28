---
title: Azure AD SAML
metaTitle: Azure AD SAML
metaDescription: Azure AD SAML
sidebar_position: 4
---

import Screenshot from '@site/src/components/Screenshot';

# Azure AD SAML

Appcircle supports [Azure AD](https://azure.microsoft.com/en-us/) as a SAML provider.

:::info

Only Enterprise accounts support SSO.

:::

### Enable SSO

SSO can only be enabled by the organization's administrator. To start, go to [My Organization](/account/my-organization) screen and click the **Enable Login** button under the **APPCIRCLE LOGIN** section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/enable-sso_v3.png' />

### Configure Appcircle and Azure AD

- Select **Setup SAML SSO Provider**

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-form_v2.png' />

- Pick an alias and display name for your organization. Please pick a short and rememberable alias.

- This screen will auto-generate an URL for the next step

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-saml1.png' />

- Log in to [Azure AD](https://azure.microsoft.com/en-us/) as an admin and navigate to **Azure Services** and then click **Azure Active Directory**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/azurecreateapp1.png' />

- Click **Enterprise applications**

<Screenshot url='https://cdn.appcircle.io/docs/assets/azurecreateapp2.png' />

- Click **New application**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/azurecreateapp3.png' />

- Click **Create your own application**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/azurecreateapp4.png' />

- Give a name for your application and select **Integrate another application you don't find in the gallery (Non-gallery)** and click **Create**

<Screenshot url='https://cdn.appcircle.io/docs/assets/azurecreateapp5.png' />

### Adding Users

You need to select users/groups in Azure AD to enable SSO. All members of your Appcircle organization must be added to Azure AD.

- Select **Users and groups** and click **Add user/group**

<Screenshot url='https://cdn.appcircle.io/docs/assets/azureaddusers.png' />

- Click **Add Assignment**, find the users from the list, and click **Select**

<Screenshot url='https://cdn.appcircle.io/docs/assets/azureaddassignment1.png' />

- Finally, click the **Assign** button to confirm the assignment.

<Screenshot url='https://cdn.appcircle.io/docs/assets/azureaddassignment2.png' />

### Configuring SSO

- Click **Single sign-on** and select **SAML**

<Screenshot url='https://cdn.appcircle.io/docs/assets/azuressosettings1.png' />

- Click **Edit** button on **Basic SAML Configuration** section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/azuressosettings2.png' />

- Add the Appcircle Redirect URL to **Reply URL (Assertion Consumer Service URL)** write `https://auth.appcircle.io/auth/realms/appcircle` for the **Identifier (Entity ID)** and select `EmailAddress` for the Name ID format.

<Screenshot url='https://cdn.appcircle.io/docs/assets/azuressosettings3.png' />

- Edit the attributes according to the below screenshot.

<Screenshot url='https://cdn.appcircle.io/docs/assets/azuressosettings4.png' />

- Instead of writing all the settings of SAML, you can download the settings file from Azure AD and upload it. Click the **Download** button next to the **Federation Metadata XML** link to download the XML file.

<Screenshot url='https://cdn.appcircle.io/docs/assets/azuressosettings5.png' />

- Go back to Appcircle, upload this XML file by clicking the button under **Import SAML Configuration**

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-saml1.png' />

- Check all the settings on this page and confirm that Redirect and SSO URLs are imported correctly. You can check if the X509 Certificate is imported correctly as well. If you want to enter multiple certificates you can separate them by using a comma between them. Please be aware that you need to remove any new lines or file headers from this edit box. This edit box only accepts a long base64 encoded string.

### Testing SSO

- When you connect your Identity Provider, please open a new incognito window and test the SSO integration.
- Click the **Continue with SSO** button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-loginbutton.png' />

- Enter the alias you picked.

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-alias.png" />

- You should first see the below confirmation screen.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-linkaccount.png' />

- After you confirmed account linking, you will get an email.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-confirmlink.png' />

- You can now access your account with SSO integration when you confirm the email.
- After you enable the SSO, you can only log in to your account with the SSO link. Your old credentials won't work anymore.

:::caution

When you connect your Identity Provider, please open a new incognito window and test the SSO integration. Please only log off when you can log in with SSO credentials. If the connection doesn't work, you need to review your settings.

:::
