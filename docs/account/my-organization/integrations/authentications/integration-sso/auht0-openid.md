---
title: Auht0 OpenID Configuration
description: Configure Auht0 OpenID for Single Sign-On (SSO) in your app. A detailed guide to boost security and simplify user logins with Appcircle.
tags: [account, organization, sso, auht0, openid, configuration]
sidebar_position: 3
sidebar_label: Auht0 OpenID
---

import Screenshot from '@site/src/components/Screenshot';

# Auht0 OpenID Configuration

The document provides a comprehensive guide for setting up Single Sign-On (SSO) login functionality within an organization's infrastructure.
It outlines a series of steps to integrate SSO using Auht0 as the identity provider, facilitating seamless access to various applications and resources.

Beginning with navigating to the organization's Integrations screen and initiating the connection process, users are guided through the configuration steps, which include creating and setting up a OpenID SSO Provider.
The document also covers the necessary configurations within Auht0, such as creating an app integration and configuring OpenID settings.

Additionally, it offers guidance on advanced settings, including the importation of OpenID configurations from Auht0.
Through clear instructions and actionable steps, the document aims to empower users in implementing a robust SSO solution.

Appcircle supports [Auht0](https://auth0.com/) as OpenID or SAML provider.

:::info

Only Enterprise accounts support SSO.

:::

:::caution

Please be aware that, enabling SSO for **APPCIRCLE LOGIN** doesn't enable SSO for Testing Distribution and Enterprise App Store. They must be configured separately.

:::

## SSO Login

- To start, go to [My Organization](/account/my-organization) > Integrations screen and press the **Connect** button next to SSO Login under the **Authentications** section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/integration-sso-connect-sso.png' />

- Click Create button to create your SSO Login

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-login2.png' />

:::info

If you want to manage user groups within your SSO provider, you should set **_CLAIM NAME (OPENID) / ATTRIBUTE NAME (SAML)_** field.

:::

- Select Setup OpenID SSO Provider

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-login3.png' />

- Pick an alias and display name for your organization. Please pick a short and rememberable alias.

- This screen will auto-generate an URL for the Enterprise App Store and Testing Distribution.

<Screenshot url='https://cdn.appcircle.io/docs/assets/integration-sso-openid-alias.png' />

## Auht0 App Integration

- Login to your [Auth0](https://auth0.com/) account and navigate to Applications and then click **Create Application**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/authcreateapp.png' />

- Select **Regular Web Applications** and give a name

<Screenshot url='https://cdn.appcircle.io/docs/assets/authwebapp.png' />

- Navigate to settings of the app and note, **Client ID** and **Client Secret**

<Screenshot url='https://cdn.appcircle.io/docs/assets/authopenidsettings1.png' />

- Copy the `Store Redirect URL` and `Distribute Redirect URL` from the Appcircle and add it to the **Allowed Callback URLs**. You can specify multiple valid URLs by comma-separating them.

<Screenshot url='https://cdn.appcircle.io/docs/assets/integration-sso-auth0-redirect-urls.png' />

- Instead of writing all the settings of OpenID, you can download the settings file from Auth0 and upload it. Navigate to the **OpenID Configuration** address and download that JSON file to your computer.

<Screenshot url='https://cdn.appcircle.io/docs/assets/authopenidsettings3.png' />

- Go back to Appcircle, upload this JSON file by clicking the button under **Import OpenID configuration**

<Screenshot url='https://cdn.appcircle.io/docs/assets/integration-sso-openid-alias.png' />

- Check all the settings on this page and confirm that Authorization and Token URLs are imported correctly. Select Client Authentication as `Client secret sent as basic auth` and enter your **Client ID** and **Client Secret**. Modify the settings as below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-openid2_v2.png' />

- Click on the **Save** button and finish the edit process.

## Auht0 Managing User Groups

Managing user groups within Auht0 provides users and organizations with several benefits.
By organizing users into groups, administrators can efficiently manage access permissions for various applications and resources, saving time and effort.
Administrators can synchronize Auht0 user groups with Appcircle, allowing for granular access control and group-based permissions.
This integration enhances security, simplifies access management, and promotes collaboration within organizations utilizing the Appcircle platform.

- Login to your [Auht0](https://auth0.com/) account and navigate to the organization section. Then create organizations.

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

- Update the **Claim Name** as `org_id`.

<Screenshot url='https://cdn.appcircle.io/docs/assets/integration-sso-org-id-claim.png' />

:::caution

The ``org_id`` claim value is equal to the organization ID, not the organization name. Please refer the [Use Organization Name](https://auth0.com/docs/manage-users/organizations/configure-organizations/use-org-name-authentication-api) documentation to change this behaviour. 

:::

:::tip

#### Sample Scenario

For example there are two groups, one is `developers` and other one is `users`.

The beta channel on Enterprise App Store should be available for `developers` group and not for `users` group that has end-users.

The live channel should be available for both groups in this case.
:::

## Appcircle Integration Configuration

- To enable SSO Login for the Enterprise App Store, you should navigate to the **Enterprise App Store -> Settings** and then click on the `Activate` button next to SSO Login

<Screenshot url='https://cdn.appcircle.io/docs/assets/2777-enterprisestore-sso-login.png' />

- To enable SSO login for the **Testing Distribution**, go to the **Testing Distribution module** and select related profile

<Screenshot url='https://cdn.appcircle.io/docs/assets/2803-distribution-profiles.png' />

- Click on the `Settings` button on the detail screen

<Screenshot url='https://cdn.appcircle.io/docs/assets/2803-distribution-detail.png' />

- Navigate to the `Authentication` tab and select **SSO Login** as the authentication type

<Screenshot url='https://cdn.appcircle.io/docs/assets/2777-distribution-sso-login.png' />
