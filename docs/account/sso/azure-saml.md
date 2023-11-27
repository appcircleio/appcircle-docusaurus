---
title: Azure AD SAML
metaTitle: Azure AD SAML
metaDescription: Azure AD SAML
sidebar_position: 4
---

import NarrowImage from '@site/src/components/NarrowImage';
import Screenshot from '@site/src/components/Screenshot';

# Azure AD SAML

Appcircle supports [Azure AD](https://azure.microsoft.com/en-us/) as a SAML provider.

:::info

Only Enterprise accounts support SSO.

:::

### Enable SSO

SSO can only be enabled by the organization's administrator. To start, go to [My Organization](../my-organization.md) screen and click the **Enable Login** button under the **APPCIRCLE LOGIN** section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/enable-sso_v2.png' />

### Configure Appcircle and Azure AD

- Select **Setup SAML SSO Provider**

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-form.png' />

- Pick an alias and display name for your organization. Please pick a short and rememberable alias.

- This screen will auto-generate an URL for the next step

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-saml1.png' />

- Log in to [Azure AD](https://azure.microsoft.com/en-us/) as an admin and navigate to **Azure Services** and then click **Azure Active Directory**.

<ExternalScreenshot url='https://cdn.appcircle.io/docs/assets/azurecreateapp1.png' width='2870px' height='1530px' />

- Click **Enterprise applications**

<ExternalScreenshot url='https://cdn.appcircle.io/docs/assets/azurecreateapp2.png' width='2468px' height='1170px' />

- Click **New application**.

<ExternalScreenshot url='https://cdn.appcircle.io/docs/assets/azurecreateapp3.png' width='2880px' height='544px' />

- Click **Create your own application**.

<ExternalScreenshot url='https://cdn.appcircle.io/docs/assets/azurecreateapp4.png' width='2880px' height='1488px' />

- Give a name for your application and select **Integrate another application you don't find in the gallery (Non-gallery)** and click **Create**

<ExternalScreenshot url='https://cdn.appcircle.io/docs/assets/azurecreateapp5.png' width='1162px' height='1596px' />

### Adding Users

You need to select users/groups in Azure AD to enable SSO. All members of your Appcircle organization must be added to Azure AD.

- Select **Users and groups** and click **Add user/group**

<ExternalScreenshot url='https://cdn.appcircle.io/docs/assets/azureaddusers.png' width='2880px' height='1506px' />

- Click **Add Assignment**, find the users from the list, and click **Select**

<ExternalScreenshot url='https://cdn.appcircle.io/docs/assets/azureaddassignment1.png' width='2880px' height='1600px' />

- Finally, click the **Assign** button to confirm the assignment.

<ExternalScreenshot url='https://cdn.appcircle.io/docs/assets/azureaddassignment2.png' width='1390px' height='1498px' />

### Configuring SSO

- Click **Single sign-on** and select **SAML**

<ExternalScreenshot url='https://cdn.appcircle.io/docs/assets/azuressosettings1.png' width='2880px' height='1550px' />

- Click **Edit** button on **Basic SAML Configuration** section.

<ExternalScreenshot url='https://cdn.appcircle.io/docs/assets/azuressosettings2.png' width='2880px' height='1540px' />

- Add the Appcircle Redirect URL to **Reply URL (Assertion Consumer Service URL)** write `https://auth.appcircle.io/auth/realms/appcircle` for the **Identifier (Entity ID)** and select `EmailAddress` for the Name ID format.

<ExternalScreenshot url='https://cdn.appcircle.io/docs/assets/azuressosettings3.png' width='1716px' height='1557px' />

- Edit the attributes according to the below screenshot.

<ExternalScreenshot url='https://cdn.appcircle.io/docs/assets/azuressosettings4.png' width='2880px' height='1474px' />

- Instead of writing all the settings of SAML, you can download the settings file from Azure AD and upload it. Click the **Download** button next to the **Federation Metadata XML** link to download the XML file.

<ExternalScreenshot url='https://cdn.appcircle.io/docs/assets/azuressosettings5.png' width='2880px' height='1538px' />

- Go back to Appcircle, upload this XML file by clicking the button under **Import SAML Configuration**

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-saml1.png' />

- Check all the settings on this page and confirm that Redirect and SSO URLs are imported correctly. You can check if the X509 Certificate is imported correctly as well. If you want to enter multiple certificates you can separate them by using a comma between them. Please be aware that you need to remove any new lines or file headers from this edit box. This edit box only accepts a long base64 encoded string.

### Testing SSO

- When you connect your Identity Provider, please open a new incognito window and test the SSO integration.
- Click the **Continue with SSO** button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-loginbutton.png' />

- Enter the alias you picked.

<NarrowImage src="https://cdn.appcircle.io/docs/assets/sso-alias.png" />

- You should first see the below confirmation screen.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-linkaccount.png' />

- After you confirmed account linking, you will get an email.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-confirmlink.png' />

- You can now access your account with SSO integration when you confirm the email.
- After you enable the SSO, you can only log in to your account with the SSO link. Your old credentials won't work anymore.

:::caution

When you connect your Identity Provider, please open a new incognito window and test the SSO integration. Please only log off when you can log in with SSO credentials. If the connection doesn't work, you need to review your settings.

:::
