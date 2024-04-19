---
title: Okta SAML Configuration
description: Configure Okta SAML for Single Sign-On (SSO) in your app. A detailed guide to boost security and simplify user logins with Appcircle.
tags: [account, organization, sso, okta, saml, configuration]
sidebar_position: 3
sidebar_label: Okta SAML
---

import Screenshot from '@site/src/components/Screenshot';

# Okta SAML Configuration

The document provides a comprehensive guide for setting up Single Sign-On (SSO) login functionality within an organization's infrastructure.
It outlines a series of steps to integrate SSO using Okta as the identity provider, facilitating seamless access to various applications and resources.

Beginning with navigating to the organization's Integrations screen and initiating the connection process, users are guided through the configuration steps, which include creating and setting up a SAML SSO Provider.
The document also covers the necessary configurations within Okta, such as creating an app integration and configuring SAML 2.0 settings.

Additionally, it offers guidance on advanced settings, including the importation of SAML configurations from Okta.
Through clear instructions and actionable steps, the document aims to empower users in implementing a robust SSO solution.

Appcircle supports [Okta](https://www.okta.com/) as OpenID or SAML provider.

:::info

Only Enterprise accounts support SSO.

:::

:::caution

Please be aware that, enabling SSO for **APPCIRCLE LOGIN** doesn't enable SSO for Testing Distribution and Enterprise App Store. They must be configured separately.

:::

## SSO Login

- To start, go to [My Organization](/account/my-organization) > Integrations screen and press the **Connect** button next to SSO Login under the **Connections** section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-login1.png' />

- Click Create button to create your SSO Login

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-login2.png' />

:::info

If you want to manage user groups within your SSO provider, you should set **_CLAIM NAME (OPENID) / ATTRIBUTE NAME (SAML)_** field.

:::

- Select Setup SAML SSO Provider

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-login3.png' />

- Pick an alias and display name for your organization. Please pick a short and rememberable alias.

- This screen will auto-generate an URL for the Enterprise App Store and Distribute

<Screenshot url='https://cdn.appcircle.io/docs/assets/2777-sso-saml1-new.png' />

## Okta App Integration

- Login to your [Okta](https://www.okta.com/) account and navigate to Applications and then click **Create App Integration**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/oktacreateapp.png' />

- Select **SAML 2.0** as Sign In Method and hit `Next`.

<Screenshot url='https://cdn.appcircle.io/docs/assets/oktacreatesaml.png' />

- Pick a name and optional logo for the app and hit `Next`.

<Screenshot url='https://cdn.appcircle.io/docs/assets/oktasamlsettings1.png' />

- Copy the `Store Redirect URL` from the Appcircle and paste it to the **Single sign-on URL** section on the OKTA.
- Write `https://auth.appcircle.io/auth/realms/store` for the **Audience URI(SP Entity ID)**

:::info
If you are a **self-hosted Appcircle user**, then you should change the domain of the **Audience URI** to your own domain.

You must use the same `auth` domain address with the `store redirect URL`.

For example your store redirect URL is `https://auth.self.spacetech.com/auth/realms/store/broker/identity-spacetech/endpoint`. Then your `Audience URI` must be `https://auth.self.spacetech.com/auth/realms/store`
:::

:::caution
Please ensure that there is no **`/`** at the end of the `Audience URI` which will cause errors.
:::

- Select `EmailAddress` for the Name ID format.

<Screenshot url='https://cdn.appcircle.io/docs/assets/2777-oktasamlsettings.png' />

- Click "Show Advance Settings" button
- Copy the `Distribute Redirect URL` from the Appcircle and paste it to the **Other Requestable SSO URLs** section and set index to `1` on the OKTA.

<Screenshot url='https://cdn.appcircle.io/docs/assets/2777-oktasamlsettings2-new.png' />

- You can hit `Next` and `Finish` the OKTA configuration as your needs.

- Instead of writing all the settings of SAML, you can download the settings file from Okta and upload it. Click the "Copy" button of **Metadata URL** and open it another tab then save the XML file.

<Screenshot url='https://cdn.appcircle.io/docs/assets/oktasamlsettings3-new.png' />

## Okta Managing User Groups

Managing user groups within Okta provides users and organizations with several benefits.
By organizing users into groups, administrators can efficiently manage access permissions for various applications and resources, saving time and effort.
Administrators can synchronize Okta user groups with Appcircle, allowing for granular access control and group-based permissions.
This integration enhances security, simplifies access management, and promotes collaboration within organizations utilizing the Appcircle platform.

- Login to your [Okta](https://www.okta.com/) account and navigate to Directory and then click **_Groups_**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/2812-okta-groups-1.png' />

- Click "Add group" button and after fill the fields click "Save" button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/2812-okta-groups-2.png' />

- Click recently created group name and assign people to your group.

<Screenshot url='https://cdn.appcircle.io/docs/assets/2812-okta-groups-3-new.png' />

- Navigate to Applications tab and assign the recently created user group(s) with "Assign applications" button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/2812-okta-groups-4.png' />

- Navigate to Applications and click on integrated app.

<Screenshot url='https://cdn.appcircle.io/docs/assets/2812-okta-groups-5.png' />

- Navigate "General" tab and edit **_SAML Settings_**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/2812-okta-groups-6.png' />

- In Configure SAML step, you should set Group Attribute Statements.
- Name field should be matched with the **_CLAIM NAME (OPENID) / ATTRIBUTE NAME (SAML)_** field set in Appcircle SSO integration page. Name format should be `Basic`.
- If you want to get all the groups that you created you should set filter section as `Matches regex` and `.*`.

<Screenshot url='https://cdn.appcircle.io/docs/assets/2812-okta-groups-7.png' />

- Click on the "Next" button and finish the edit process.

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
