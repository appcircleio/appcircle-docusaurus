---
title: Okta SAML
metaTitle: Okta SAML
metaDescription: Okta SAML
sidebar_position: 6
---

import Screenshot from '@site/src/components/Screenshot';

# Okta SAML

Appcircle supports [Okta](https://www.okta.com/) as OpenID or SAML provider.

:::info

Only Enterprise accounts support SSO.

:::

### Enable SSO

SSO can only be enabled by the organization's administrator. To start, go to [My Organization](../my-organization.md) screen and click the **Enable Login** button under the **APPCIRCLE LOGIN** section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/enable-sso_v3.png' />

### Configure Appcircle and Okta

- Select Setup SAML SSO Provider

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-form_v2.png' />

- Pick an alias and display name for your organization. Please pick a short and rememberable alias.

- This screen will auto-generate an URL for the next step

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-saml1.png' />

- Login to your [Okta](https://www.okta.com/) account and navigate to Applications and then click **Create App Integration**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/oktacreateapp.png' />

- Select **SAML 2.0** as Sign In Method

<Screenshot url='https://cdn.appcircle.io/docs/assets/oktacreatesaml.png' />

- Pick a name and optional logo for the app.

<Screenshot url='https://cdn.appcircle.io/docs/assets/oktasamlsettings1.png' />

- Add the Appcircle Redirect URL to **Single sign on URL** write `https://auth.appcircle.io/auth/realms/appcircle` for the **Audience URI (SP Entity ID)** and select `EmailAddress` for the Name ID format.

<Screenshot url='https://cdn.appcircle.io/docs/assets/oktasamlsettings2.png' />

- Instead of writing all the settings of SAML, you can download the settings file from Okta and upload it. Click the "Copy" button of **Metadata URL** and open it another tab then save the XML file.

<Screenshot url='https://cdn.appcircle.io/docs/assets/oktasamlsettings3-new.png' />

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
