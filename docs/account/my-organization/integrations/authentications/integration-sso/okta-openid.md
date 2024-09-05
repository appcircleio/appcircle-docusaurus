---
title: Okta OpenID Configuration
description: Configure Okta OpenID for Single Sign-On (SSO) in your app. A detailed guide to boost security and simplify user logins with Appcircle.
tags: [account, organization, sso, okta, openid, configuration]
sidebar_position: 3
sidebar_label: Okta OpenID
---

import Screenshot from '@site/src/components/Screenshot';

# Okta OpenID Configuration

The document provides a comprehensive guide for setting up Single Sign-On (SSO) login functionality within an organization's infrastructure.
It outlines a series of steps to integrate SSO using Okta as the identity provider, facilitating seamless access to various applications and resources.

Beginning with navigating to the organization's Integrations screen and initiating the connection process, users are guided through the configuration steps, which include creating and setting up a OpenID SSO Provider.
The document also covers the necessary configurations within Okta, such as creating an app integration and configuring OpenID settings.

Additionally, it offers guidance on advanced settings, including the importation of OpenID configurations from Okta.
Through clear instructions and actionable steps, the document aims to empower users in implementing a robust SSO solution.

Appcircle supports [Okta](https://www.okta.com/) as OpenID or SAML provider.

:::info

Only Enterprise accounts support SSO.

:::

:::caution

Please be aware that, enabling SSO for **APPCIRCLE LOGIN** doesn't enable SSO for Testing Distribution and Enterprise App Store. They must be configured separately.

:::

## SSO Login

- To start, go to [My Organization](/account/my-organization) > Integrations screen and press the **Connect** button next to SSO Login under the **Authentications** section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/integration-sso-connect-sso.png' />

- Click Create button to create your SSO Login.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-login2.png' />

:::info

If you want to manage user groups within your SSO provider, you should set **_CLAIM NAME (OPENID) / ATTRIBUTE NAME (SAML)_** field.

:::

- Select Setup OpenID SSO Provider.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-login3.png' />

- Pick an alias and display name for your organization. Please pick a short and rememberable alias.

- This screen will auto-generate an URL for the Enterprise App Store and Testing Distribution.

<Screenshot url='https://cdn.appcircle.io/docs/assets/integration-sso-openid-alias.png' />

## Okta App Integration

- Login to your [Okta](https://www.okta.com/) account and navigate to Applications and then click **Create App Integration**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/oktacreateapp.png' />

- Select **OIDC - OpenID Connect** as Sign In Method and select **Web Application** as application type then hit `Next`.

<Screenshot url='https://cdn.appcircle.io/docs/assets/integration-sso-okta-openid-create-app.png' />

- Pick a name and optional logo for the app.

<Screenshot url='https://cdn.appcircle.io/docs/assets/integration-sso-okta-openid-create-app2.png' />

- Copy the `Store Redirect URL` and `Distribute Redirect URL` from the Appcircle and add it to the **Single sign-on URL** section on the OKTA.

<Screenshot url='https://cdn.appcircle.io/docs/assets/integration-sso-okta-openid-create-app-redirect-uri.png' />

- Select **Skip group assignment for now** in the Assignments section. We will assign groups later manuall.

<Screenshot url='https://cdn.appcircle.io/docs/assets/integration-sso-okta-openid-create-app-assign.png' />

- You can hit `Next`.

- Navigate to the application's General Settings and locate the Client ID and Client Secret. These credentials will be required and should be noted for future configuration steps.

<Screenshot url='https://cdn.appcircle.io/docs/assets/integration-sso-okta-openid-client-id-secret.png' />

- Instead of writing all the settings of OpenID, you can download the settings file from Okta and upload it to Appcircle.

Download your OpenID configuration file from one of the below locations:

```
https://customer_name_here.okta.com/.well-known/openid-configuration
https://customer_name_here.okta.com/oauth2/default/.well-known/openid-configuration?client_id=<your_client_id>

```

- Go back to Appcircle, upload this JSON file by clicking the button under **Import OpenID configuration**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/integration-sso-openid-alias.png' />

- Select Client Authentication as `Client secret sent as basic auth` and enter your **Client ID** and **Client Secret** in OpenID Connect Config section. Also review the imported OpenID Connect Configuration in this section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/integration-sso-okta-openid-ac-client-id-secret.png' />

- Review the **Advanced Configurations** on this page.

<Screenshot url='https://cdn.appcircle.io/docs/assets/integration-sso-okta-openid-ac-advanced-config.png' />

- Click on the **Save** button and finish the edit process.

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

<Screenshot url='https://cdn.appcircle.io/docs/assets/integration-sso-okta-openid-assign-group-to-app.png' />

- Navigate to Applications and click on integrated app.

<Screenshot url='https://cdn.appcircle.io/docs/assets/integration-sso-okta-openid-navigate-to-app.png' />

- Navigate "Sign On" tab and edit **Groups claim filter** in **OpenID Connect ID Token** section. If you want to get all the groups that you created you should set filter section as `Matches regex` and `.*`.

<Screenshot url='https://cdn.appcircle.io/docs/assets/integration-sso-okta-openid-group-claim.png' />

- Click on the **Save** button and finish the edit process.

- Click the Back to applications link. From the More button dropdown menu, click Refresh Application Data.

<Screenshot url='https://cdn.appcircle.io/docs/assets/integration-sso-okta-refresh-app-data.png' />

- Go back to Appcircle, go to [My Organization](/account/my-organization) > Integrations screen and press the **Manage** button next to SSO Login under the **Authentications** section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/integration-sso-manage-sso.png' />

- Click **Edit** on your SSO integration. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/integration-sso-edit-sso.png' />

- Update the **Default Scope** attribute as `openid profile email groups`.

<Screenshot url='https://cdn.appcircle.io/docs/assets/integration-sso-openid-groups-scope.png' />

- Click on the **Save** button and finish the edit process.

- Update the **Claim Name** as `groups`.

<Screenshot url='https://cdn.appcircle.io/docs/assets/integration-sso-groups-claim.png' />


:::tip

#### Sample Scenario

For example there are two groups, one is `developers` and other one is `users`.

The beta channel on Enterprise App Store should be available for `developers` group and not for `users` group that has end-users.

The live channel should be available for both groups in this case.
:::

## Appcircle Integration Configuration

- Go back to Appcircle, upload this XML file by clicking the button under **Import SAML Configuration**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/2777-sso-saml1-new.png' />

- Check all the settings on this page and confirm that Redirect and SSO URLs are imported correctly. You can check if the X509 Certificate is imported correctly as well. If you want to enter multiple certificates you can separate them by using a comma between them. Please be aware that you need to remove any new lines or file headers from this edit box. This edit box only accepts a long base64 encoded string.

- Hit `Save` button and save the SAML configuration on Appcircle.

- To enable SSO Login for the Enterprise App Store, you should navigate to the **Enterprise App Store -> Settings** and then click on the `Activate` button next to SSO Login.

<Screenshot url='https://cdn.appcircle.io/docs/assets/2777-enterprisestore-sso-login.png' />

- To enable SSO login for the **Testing Distribution**, go to the **Testing Distribution module** and select related profile.

<Screenshot url='https://cdn.appcircle.io/docs/assets/2803-distribution-profiles.png' />

- Click on the `Settings` button on the detail screen.

<Screenshot url='https://cdn.appcircle.io/docs/assets/2803-distribution-detail.png' />

- Navigate to the `Authentication` tab and select **SSO Login** as the authentication type.

<Screenshot url='https://cdn.appcircle.io/docs/assets/2777-distribution-sso-login.png' />
