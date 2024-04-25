---
title: Auth0 SAML
description: Enable Auth0 SAML for secure user sign-in in your app. Simplify access and enhance security with Appcircle's integration.
tags: [account, organization, sso, auth0, saml, configuration]
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';

# Auth0 SAML

Appcircle supports [Auth0](https://auth0.com/) as OpenID or as a SAML provider.

:::info

Only Enterprise accounts support SSO.

:::

### Enable SSO

SSO can only be enabled by the organization's administrator. To start, go to [My Organization](/account/my-organization) screen and click the **Enable Login** button under the **APPCIRCLE LOGIN** section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/enable-sso_v3.png' />

### Configure Appcircle and Auth0

- Select Setup SAML SSO Provider

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-form_v2.png' />

- Pick an alias and display name for your organization. Please pick a short and rememberable alias.

- This screen will auto-generate an URL for the next step

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-saml1.png' />

- Login to your [Auth0](https://auth0.com/) account and navigate to Applications and then click **Create Application**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/authcreateapp.png' />

- Select **Regular Web Applications** and give a name

<Screenshot url='https://cdn.appcircle.io/docs/assets/authwebapp.png' />

- Navigate to **Addons** of the app and enable the SAML option.

<Screenshot url='https://cdn.appcircle.io/docs/assets/authsamlsettings1.png' />

- Click the SAML button and change the settings. For the Callback URL write down the callback URL you have created earlier. For the settings, paste the below JSON

```json
{
  "nameIdentifierFormat": "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress",
  "nameIdentifierProbes": [
    "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress"
  ]
}
```

<Screenshot url='https://cdn.appcircle.io/docs/assets/authsamlsettings2.png' />

- Instead of writing all the settings of SAML, you can download the settings file from Auth0 and upload it. Navigate to the **Usage** and then click the **Download** button to download the XML file

<Screenshot url='https://cdn.appcircle.io/docs/assets/authsamlsettings3.png' />

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
