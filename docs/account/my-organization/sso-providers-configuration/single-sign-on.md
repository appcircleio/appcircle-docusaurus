---
title: Enable SSO
metaTitle: Enable SSO
metaDescription: Enable SSO
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';

# Single Sign-On

Single sign-on(SSO) allows your team members to log in to their accounts.
Appcircle supports both OpenID and SAML Identity providers.

:::info

Only Enterprise accounts support SSO.

:::

### Enable SSO

SSO can only be enabled by the organization's administrator. To start, go to [My Organization](/account/my-organization) Integration screen and press the "Enable Login" button under the "APPCIRCLE LOGIN" section.

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

Child organization can't enable SSO.

:::

:::caution

When you connect your Identity Provider, please open a new incognito window and test the SSO integration. Please only log off when you can log in with SSO credentials. If the connection doesn't work, you need to review your settings.

:::

### Inviting a User to the Organization

If you configure the SSO settings and ask a user to join the organization, an email will be delivered to the user's inbox.

The invitation link in the email will send the user to the SSO login page immediately. As a result, the user will not need to click the SSO button and input their SSO alias.

### SSO Login Direct Link

If you wish to log in to the Appcircle dashboard directly using the integrated SSO you set up for your company, you can use an auto-redirect URL.

Below is the URL template for direct login with SSO for Appcircle Cloud.

```URL
https://my.appcircle.io/sso/${SSO_ALIAS}
```

For example, if you configured an SSO and your **SSO alias** in the Appcircle configuration is `spacetechsso`, you should use the URL below to log in straight to the SSO:

```URL
https://my.appcircle.io/sso/spacetechsso
```

Notice that the name `spacetechsso` in the SSO URL above is the SSO alias. You should replace it with your own SSO alias and use it.

:::info
If you are a self-hosted Appcircle user, you can use the same method too. The only difference will be in the URL.

If you're using `https://my.appcircle.spacetech.com` to access the Appcircle dashboard, for instance, your SSO direct login URL should be

- `https://my.appcircle.spacetech.com/sso/spacetechsso`

:::

After you enter the SSO login URL specified above, you should be redirected to the SSO login page directly or to the Appcircle dashboard if you have already authenticated with the SSO.
