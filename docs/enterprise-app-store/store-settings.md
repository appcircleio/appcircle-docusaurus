---
title: Store Settings
description: Learn how to configure your enterprise app store profile in Appcircle
tags: [store settings, enterprise app store, authentication, custom domain, sso, ldap, static login, saml, openid, two-factor authentication]
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

Store settings allow you to configure your authentication and domain settings.

## Store Authentication

Appcircle supports Static, SSO, and LDAP login. Users can also set the authentication to 'none' for direct logins.

:::info

SSO and LDAP login is only available for Enterprise accounts. Only the Organization owner or users with **Manage Enterprise Settings & Apps** rights can change the login settings.

:::

### No Authentication Login

Enterprise Store authentication can be set to 'none,' allowing users to log in automatically without entering credentials.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4456.png" />

Please note that this authentication method will also affect the shared links and QR codes for app versions across all Enterprise Store profiles.

### Static Login

You can set a different username and password for live and beta apps. The usernames of the live and beta section must be different.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4456-2.png" />

### SSO Login

You may also use SSO for your Enterprise App Store. Appcircle supports both OpenID and SAML SSO providers. In order to enable SSO integration, please turn on the toggle that says **Enable SSO**. After you have enabled the SSO, please click the **Create** link to configure the SSO, according to your provider.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4456-3.png' />

:::info

If you're configuring SAML Provider, you must set `https://auth.appcircle.io/auth/realms/store` as Audience URI (SP Entity ID).

:::

**Identity Providers​**

You can follow the below documents to connect your identity providers. If your Identity Provider is not on the list, you can follow any OpenID or SAML integration guide from the below list to find out the parameters.

- [Auth0 OpenID](/account/my-organization/integrations/authentications/sso-providers-configuration/auth-openid)
- [Auth0 SAML](/account/my-organization/integrations/authentications/sso-providers-configuration/auth-saml)
- [Azure AD SAML](/account/my-organization/integrations/authentications/sso-providers-configuration/azure-saml)
- [Okta OpenID](/account/my-organization/integrations/authentications/sso-providers-configuration/okta-openid)
- [Okta SAML](/account/my-organization/integrations/authentications/sso-providers-configuration/okta-saml)
- [OneLogin SAML](/account/my-organization/integrations/authentications/sso-providers-configuration/onelogin-saml)

Please check the below document to learn more about SSO integration.

<ContentRef url="/account/my-organization/integrations/authentications/sso-providers-configuration/single-sign-on">
  Single Sign-On
</ContentRef>

### LDAP Login

In order to create an LDAP login, first click the **Activate** link next to the LDAP login. If you select **Enable LDAP Login**, your previous login options will be disabled and LDAP login will be enabled. Click the **Details** link and then click the **Create** link. Appcircle supports multiple LDAP providers. You can add multiple LDAP servers with different settings.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4456-4.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4456-6.png' />

**Configuration**

Each setting has a tooltip that shows a detailed explanation.

**Name**
Display the name of the LDAP provider. You can write any name for this area.

**Vendor**
Appcircle supports multiple LDAP providers such as Active Directory, Red Hat Directory Server, Tivoli, and Novell Directory out of the box. If your provider is not on the above list, you can select the Other option to configure your LDAP login manually.

**Username LDAP attribute**
Name of LDAP attribute, which is mapped as username. For many LDAP server vendors, it can be 'uid'. For Active directory, it can be 'sAMAccountName' or 'cn'

**RDN LDAP attribute**
Name of LDAP attribute, which is used as RDN (top attribute) of typical user DN. Usually, it's the same as the Username LDAP attribute, however, it is not required. For example for the Active directory, it is common to use 'cn' as the RDN attribute when the username attribute might be 'sAMAccountName'.

**UUID LDAP attribute**
Name of LDAP attribute, which is used as a unique object identifier (UUID) for objects in LDAP. For many LDAP server vendors, it is 'entryUUID'; however, some are different. For example, for the Active directory, it should be 'objectGUID'. If your LDAP server does not support the notion of UUID, you can use any other attribute that is supposed to be unique among LDAP users in the tree. For example 'uid' or 'entryDN'

**User Object Classes**
All values of the LDAP objectClass attribute for users in LDAP divided by comma. For example: 'inetOrgPerson, organizationalPerson'.

**Connection Url**
Connection URL to your LDAP server

**Users DN**
Full DN of LDAP tree where your users are. This DN is the parent of LDAP users. It could be for example 'ou=users,dc=example,dc=com' assuming that your typical user will have DN like 'uid=john,ou=users,dc=example,dc=com'

**Custom User LDAP Filter**
Additional LDAP Filter for filtering searched users. Leave this empty if you don't need additional filter. Make sure that it starts with '(' and ends with ')'

**Phone Number LDAP Attribute**
This attribute will be used to get email address for Two Factor Authentication(2FA).

**Search Scope**
For one level, the search applies only for users in the DNs specified by User DNs. For subtree, the search applies to the whole subtree. See LDAP documentation for more details

**Bind Type**
Type of the Authentication method used during LDAP Bind operation. It is used in most of the requests sent to the LDAP server. Options: 'none' (anonymous LDAP authentication) and 'simple' (Bind credential + Bind password authentication)

**Bind DN**
DN of LDAP admin, which will be used to access LDAP server

**Enable StartTLS**
Encrypts the connection to LDAP using STARTTLS

**Connection Timeout**
LDAP Connection Timeout in milliseconds

**Read Timeout**
LDAP Read Timeout in milliseconds. This timeout applies for LDAP read operations

**Pagination**
Does the LDAP server support pagination

### User Federation

After you have configured the main LDAP settings, you need to configure the **User Federation Mapper** section to set group DN settings. These settings will be used to query groups.

### Testing LDAP Connection

After you have configured LDAP, you can use **Test Connection** and **Test Authentication** to check the connection and credentials.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4456-7.png' />

### Two-factor Authentication

To further protect your logins, you may add Two-factor Authentication(2FA) to your LDAP integration. Appcircle supports both email and SMS 2FA authentication.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4456-8.png' />

## Store Domain

You can customize your store prefix which will be reflected in your Enterprise Store access URL.

The URL can be copied by clicking the copy icon next to it.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4456-9.png' />

### Custom Domain

**Custom Domain**

It's possible to use a custom domain for the Enterprise App Store. You need to have the following to create a custom domain

- A custom domain that you can create a CNAME record.
- SSL Certificate that is exported as a p12 or pfx file.

**Creating CNAME Record**

Open your DNS provider's website and add a CNAME with the below details

**Name:** Your subdomain name. Ex. **store**

**Destination:** _**store-domain.appcircle.io**_

The below screenshot shows an example configuration screen from Cloudflare.

<Screenshot url='https://cdn.appcircle.io/docs/assets/entstore-cname.png' />

**Updating Settings**

After creating the DNS settings, type your custom domain name, select your certificate, and update the configuration. DNS changes can take time to propagate. You may have to wait a few minutes or hours to see the redirect.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4456-5.png" />

:::caution

If you are working on a sub organization, you will not have access to Customize and Settings sections on Enterprise App Store module.
Only the main organization has the privilege to Set up, Configure and Customize the Enterprise store.

:::

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4082-enterprisesub.png" />