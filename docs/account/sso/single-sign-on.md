---
title: Enable SSO
metaTitle: Enable SSO
metaDescription: Enable SSO
sidebar_position: 1
---

# Single Sign-On

Single sign-on(SSO) allows your team members to log in to their accounts.
Appcircle supports both OpenID and SAML Identity providers.

:::info

Only Enterprise accounts support SSO.

:::


### Enable SSO

SSO can only be enabled by the organization's administrator. To start, go to [My Organization](../my-organization.md) screen and press the "Enable SSO" button under the "SSO Integration" section.

### Identity Providers

Appcircle supports both OpenID and SAML Identity providers. You can follow the below documents to connect your identity providers. If your Identity Provider is not on the list, you can follow any OpenID or SAML integration guide from the below list to find out the parameters.

- [Auth0 OpenID](./auth-openid.md)
- [Auth0 SAML](./auth-saml.md)
- [Azure AD SAML](./azure-saml.md)
- [Okta OpenID](./okta-openid.md)
- [Okta SAML](./okta-saml.md)
- [OneLogin SAML](./onelogin-saml.md)

:::info

Two-factor authentication (2FA) can only be enabled by your SSO provider. Please check their documentation to learn how to enable it.

:::

### Testing SSO

- When you connect your Identity Provider, please open a new incognito window and test the SSO integration.
- Click the **Continue with SSO** button.

![](<https://cdn.appcircle.io/docs/assets/sso-loginbutton.png>)

- Enter the alias you picked.

![](<https://cdn.appcircle.io/docs/assets/sso-alias.png>)

- You should first see the below confirmation screen.

![](<https://cdn.appcircle.io/docs/assets/sso-linkaccount.png>)


- After you confirmed account linking, you will get an email.

![](<https://cdn.appcircle.io/docs/assets/sso-confirmlink.png>)

- You can now access your account with SSO integration when you confirm the email.
- After you enable the SSO, you can only log in to your account with the SSO link. Your old credentials won't work anymore.

:::caution

When you connect your Identity Provider, please open a new incognito window and test the SSO integration. Please only log off when you can log in with SSO credentials. If the connection doesn't work, you need to review your settings. 

:::
