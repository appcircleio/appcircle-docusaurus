---
title: Customize Enterprise Store
metaTitle: Customize Enterprise Store
metaDescription: Customize Enterprise Store
sidebar_position: 3
---

import ContentRef from '@site/src/components/ContentRef';
import NarrowImage from '@site/src/components/NarrowImage';

# Customize Your Enterprise Store


### Customizing Appearance

You can customize the appearance of your store by going to Customize section.

![](<https://cdn.appcircle.io/docs/assets/entstore-customize.png>)

### Advanced Settings

**Authentication**

You can also add a username and password for your store and change your store's domain. You must set two different usernames and passwords for live and beta apps. The username of the live and beta section must be different. 

<NarrowImage src="https://cdn.appcircle.io/docs/assets/entstore-settings.png" />

**Custom Domain**

It's possible to use a custom domain for the Enterprise Store. You need to have the following to create a custom domain

- A custom domain that you can create a CNAME record.
- SSL Certificate that is exported as a p12 or pfx file.

**Creating CNAME Record**

Open your DNS provider's website and add a CNAME with the below details

**Name:** Your subdomain name. Ex. *store*

**Destination:** _**store-domain.appcircle.io**_

The below screenshot shows an example configuration screen from Cloudflare.

![](<https://cdn.appcircle.io/docs/assets/entstore-cname.png>)


**Updating Settings**

After creating the DNS settings, type your custom domain name, select your certificate and update the configuration. DNS changes can take time to propagate. You may have to wait a few minutes or hours to see the redirect.

<NarrowImage src="https://cdn.appcircle.io/docs/assets/entstore-customdomain.png" />

## SSO Integration

You can enable SSO for your Enterprise Store. Appcircle supports both OpenID and SAML SSO providers. In order to enable SSO integration, please turn on the toggle that says **Enable SSO**. After you have enabled the SSO, please click the **Create** link to configure the SSO, according to your provider.

![](<https://cdn.appcircle.io/docs/assets/entstore-ssotoogle.png>)


:::info

If you're configuring SAML Provider, you must set `https://auth.appcircle.io/auth/realms/store` as Audience URI (SP Entity ID).

:::


## Identity Providers​

You can follow the below documents to connect your identity providers. If your Identity Provider is not on the list, you can follow any OpenID or SAML integration guide from the below list to find out the parameters.

- [Auth0 OpenID](../account/sso/auth-openid.md)
- [Auth0 SAML](../account/sso/auth-saml.md)
- [Azure AD SAML](../account/sso/azure-saml.md)
- [Okta OpenID](../account/sso/okta-openid.md)
- [Okta SAML](../account/sso/okta-saml.md)
- [OneLogin SAML](../account/sso/onelogin-saml.md)

Please check the below document to learn more about SSO integration.

<ContentRef url="/account/sso/single-sign-on">
  Single Sign-On
</ContentRef>
