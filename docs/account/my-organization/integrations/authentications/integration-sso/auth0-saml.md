---
title: Auth0 SAML Configuration
description: Configure Auht0 SAML for Single Sign-On (SSO) in your app. A detailed guide to boost security and simplify user logins with Appcircle.
tags: [account, organization, sso, auth0, saml, configuration]
sidebar_position: 3
sidebar_label: Auth0 SAML
---

import Screenshot from '@site/src/components/Screenshot';

# Auth0 SAML Configuration

The document provides a comprehensive guide for setting up Single Sign-On (SSO) login functionality within an organization's infrastructure.
It outlines a series of steps to integrate SSO using Auth0 as the identity provider, facilitating seamless access to various applications and resources.

Beginning with navigating to the organization's Integrations screen and initiating the connection process, users are guided through the configuration steps, which include creating and setting up a SAML SSO Provider.
The document also covers the necessary configurations within Auht0, such as creating an app integration and configuring SAML 2.0 settings.

Additionally, it offers guidance on advanced settings, including the importation of SAML configurations from Auth0.
Through clear instructions and actionable steps, the document aims to empower users in implementing a robust SSO solution.

Appcircle supports [Auth0](https://auth0.com/) as OpenID or SAML provider.

:::info

Only Enterprise accounts support SSO.

:::

:::caution

Please be aware that, enabling SSO for **APPCIRCLE LOGIN** doesn't enable SSO for Testing Distribution and Enterprise App Store. They must be configured separately.

:::

## SSO Login

- To start, go to [My Organization](/account/my-organization) > Integrations screen and press the **Connect** button next to SSO Login under the **Authentications** section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-login1.png' />

- Click Create button to create your SSO Login.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-login2.png' />

:::info

If you want to manage user groups within your SSO provider, you should set **_CLAIM NAME (OPENID) / ATTRIBUTE NAME (SAML)_** field.

:::

- Select Setup SAML SSO Provider.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-login3.png' />

- Pick an alias and display name for your organization. Please pick a short and rememberable alias.

- This screen will auto-generate an URL for the Enterprise App Store and Testing Distribution.

<Screenshot url='https://cdn.appcircle.io/docs/assets/2777-sso-saml1-new.png' />

## Auht0 App Integration

- Login to your [Auth0](https://auth0.com/) account and navigate to Applications and then click **Create Application**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/authcreateapp.png' />

- Select **Regular Web Applications** and give a name.

<Screenshot url='https://cdn.appcircle.io/docs/assets/authwebapp.png' />

- Navigate to **Addons** of the app and enable the SAML option.

<Screenshot url='https://cdn.appcircle.io/docs/assets/authsamlsettings1.png' />

- Click the SAML button and change the settings. For the Callback URL write down the `Store Redirect URL` you have created earlier. For the settings, paste the below JSON.

```json
{
  "nameIdentifierFormat": "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress",
  "nameIdentifierProbes": [
    "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress"
  ]
}
```
<Screenshot url='https://cdn.appcircle.io/docs/assets/authsamlsettings2.png' />

- Instead of writing all the settings of SAML, you can download the settings file from Auth0 and upload it. Navigate to the **Usage** and then click the **Download** button to download the XML file.

<Screenshot url='https://cdn.appcircle.io/docs/assets/authsamlsettings3.png' />

- Go back to Appcircle, upload this XML file by clicking the button under **Import SAML Configuration**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/2777-sso-saml1-new.png' />

- Check all the settings on this page and confirm that Redirect and SSO URLs are imported correctly. You can check if the X509 Certificate is imported correctly as well. If you want to enter multiple certificates you can separate them by using a comma between them. Please note that you need to remove any new lines or file headers from this edit box. This edit box only accepts a long base64 encoded string.

:::info
If you are a **self-hosted Appcircle user**, then you should change the domain of the **Store and Distribute Redirect URL** to your own domain.

You must use the same `auth` domain address with the `store redirect URL`.

For example your Store Redirect URL is `https://auth.self.spacetech.com/auth/realms/store/broker/identity-spacetech/endpoint,
Distribute Redirect URL is `https://auth.self.spacetech.com/auth/realms/distribute/broker/identity-spacetech/endpoint`
:::

- Navigate to the **Settings** tab and go to the **Application URIs** section. Add `Distribute Redirect URL` to the **Allowed Callback URLs** field.

<Screenshot url='https://cdn.appcircle.io/docs/assets/integration-sso-auth0-distribute-redirect-url.png' />

## Auth0 Managing User Groups

Managing user groups within Auth0 provides users and organizations with several benefits.
By organizing users into groups, administrators can efficiently manage access permissions for various applications and resources, saving time and effort.
Administrators can synchronize Auth0 user groups with Appcircle, allowing for granular access control and group-based permissions.
This integration enhances security, simplifies access management, and promotes collaboration within organizations utilizing the Appcircle platform.

- Login to your [Auth0](https://auth0.com/) account and navigate to the organization section. Then create organizations.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-create-groups.png' />

- Add users who will become members of your organization.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-add-members.png' />

- Navigate to the **"Connections"** tab and enable Username-Password-Authentication connection for your organization.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-enable-connections.png' />

- Navigate to the "Applications" section. Select the relevant application, then go to the "Organizations" tab. Click on **"Disable Grants Now"**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-application-organizations1.png' />

- Choose **"Business Users"** for the type of users and select **"Prompt for Organization"** for the login flow. Click on **"Save Changes"**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-application-organizations2.png' />

- Go back to Appcircle, go to [My Organization](/account/my-organization) > Integrations screen and press the **Manage** button next to SSO Login under the **Authentications** section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/integration-sso-manage-sso.png' />

- Update the **Claim Name** as `http://schemas.auth0.com/org_id`.

<Screenshot url='https://cdn.appcircle.io/docs/assets/integration-sso-auth0-saml-org-id-claim.png' />

:::caution

The ``http://schemas.auth0.com/org_id`` claim value is equal to the organization ID, not the organization name. Please refer the [Use Organization Name](https://auth0.com/docs/manage-users/organizations/configure-organizations/use-org-name-authentication-api) documentation to change this behaviour. 

:::

:::tip

#### Sample Scenario

For example there are two groups, one is `developers` and other one is `users`.

The beta channel on Enterprise App Store should be available for `developers` group and not for `users` group that has end-users.

The live channel should be available for both groups in this case.
:::

## Appcircle Integration Configuration

- Go back to Appcircle, upload this XML file by clicking the button under **Import SAML Configuration**

<Screenshot url='https://cdn.appcircle.io/docs/assets/2777-sso-saml1-new.png' />

- Check all the settings on this page and confirm that Redirect and SSO URLs are imported correctly. You can check if the X509 Certificate is imported correctly as well. If you want to enter multiple certificates you can separate them by using a comma between them. Please be aware that you need to remove any new lines or file headers from this edit box. This edit box only accepts a long base64 encoded string.

- Hit `Save` button and save the SAML configuration on Appcircle.

- To enable SSO Login for the Enterprise App Store, you should navigate to the **Enterprise App Store -> Settings** and then click on the `Activate` button next to SSO Login

<Screenshot url='https://cdn.appcircle.io/docs/assets/2777-enterprisestore-sso-login.png' />

- To enable SSO login for the **Testing Distribution**, go to the **Testing Distribution module** and select related profile

<Screenshot url='https://cdn.appcircle.io/docs/assets/2803-distribution-profiles.png' />

- Click on the `Settings` button on the detail screen

<Screenshot url='https://cdn.appcircle.io/docs/assets/2803-distribution-detail.png' />

- Navigate to the `Authentication` tab and select **SSO Login** as the authentication type

<Screenshot url='https://cdn.appcircle.io/docs/assets/2777-distribution-sso-login.png' />
