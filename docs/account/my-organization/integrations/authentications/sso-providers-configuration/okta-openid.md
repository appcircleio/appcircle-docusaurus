---
title: Okta OpenID
description: Utilize Okta OpenID for user authentication in your app. Streamline sign-in processes and boost security with Appcircle.
tags: [account, organization, sso, okta, openid, configuration]
sidebar_position: 5
---

import Screenshot from '@site/src/components/Screenshot';

# Okta OpenID

Appcircle supports [Okta](https://www.okta.com/) as OpenID or SAML provider.

:::info

Only Enterprise accounts support SSO.

:::

### Enable SSO

SSO can only be enabled by the organization's administrator. To start, go to [My Organization](/account/my-organization) screen and click the **Enable Login** button under the **APPCIRCLE LOGIN** section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/enable-sso_v3.png' />

### Configure Appcircle and Okta

- Select Setup an OpenID Provider

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-form_v2.png' />

- Pick an alias and display name for your organization. Please pick a short and rememberable alias.

- This screen will auto-generate an URL for the next step

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-openid1_v2.png' />

- Login to your [Okta](https://www.okta.com/) account and navigate to Applications and then click "Create App Integration".

<Screenshot url='https://cdn.appcircle.io/docs/assets/oktacreateapp.png' />

- Select "OIDC - OpenID Connect" as Sign In Method and then select **Web Application** as application type

<Screenshot url='https://cdn.appcircle.io/docs/assets/oktawebapp.png' />

- Navigate to settings of the app and note, **Client ID** and **Client Secret**

<Screenshot url='https://cdn.appcircle.io/docs/assets/oktaopenidsettings1.png' />

- Add the Appcircle Redirect URL to **Sign-in redirect URLs**

<Screenshot url='https://cdn.appcircle.io/docs/assets/oktaopenidsettings2.png' />

- Instead of writing all the settings of OpenID, you can download the settings file from Okta and upload it.

Download your OpenID configuration file from one of the below locations

```
https://customer_name_here.okta.com/.well-known/openid-configuration
https://customer_name_here.okta.com/oauth2/default/.well-known/openid-configuration?client_id=<your_client_id>

```

- Go back to Appcircle, upload this JSON file by clicking the button under **Import OpenID configuration**

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-openid1_v2.png' />

- Check all the settings on this page and confirm that Authorization and Token URLs are imported correctly. Enter your **Client ID** and **Client Secret**. Modify the settings as below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-openid2_v2.png' />

- The Group Claim Name and Role Claim Name fields are optional. Please refer to the [SSO Mapping Documentation](/account/my-organization/integrations/authentications/sso-providers-configuration/okta-openid#sso-mapping).

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

### SSO Mapping

This step is optional and can be skipped if you do not plan to use SSO Mapping.

- Navigate to the **Directory** section in the Okta Dashboard, click on **Groups**, and create the groups as needed.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-create-groups.png' />

- Assign users to groups.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-assign-users-to-groups.png' />

- Navigate to the **Applications** section, click on **Applications** tab.
- Select your application from the list and navigate to the **Sign on** tab. Click on **Edit** for OpenID Connect ID Token.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-oidc-edit-id-token.png' />

- Enter Groups claim filter as shown in the image below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-oidc-groups-claim.png' />

- User roles will be stored in a user attribute. 
- Navigate to the **Directory** section, click on **Profile Editor**. Select the **User (default)** from profile list.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-profile-editor.png' />

- Click on **Add Attribute**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-create-user-attribute1.png' />

- Add a new user attribute as shown in the image below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-create-user-attribute2.png' />

- Navigate to the **Directory** section, click on **Profile Editor**. Select the **Your Application Name User** from the profile list.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-oidc-profile-editor.png' />

- Add a new user attribute as shown in the image below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-oidc-add-roles-attribute.png' />

- Add a new user attribute as shown in the image below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-oidc-add-roles-attribute.png' />

- Click on **Mappings** and map user roles attribute to application user roles attribute as shown in the image below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-oidc-map-roles-attribute.png' />

- Now, you can edit roles attribute of the users. 
- Navigate to the **Directory** section, click on **People**, select a user from the list, and then click on the **Profile** tab. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-edit-user-attribute1.png' />

- Click on **Edit** and update the user's role attribute. For example, set it to 'Manager'.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-edit-user-attribute2.png' />

- Navigate to the **Security** section, click on **API** and select **Authorization Servers** tab.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-oidc-security-api.png' />

- Click on **default** and select **Claims** tab. Add new claim as shown in the image below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-oidc-add-roles-claim.png' />

- Navigate to the **Applications** section, click on **Applications** tab. Click on **Refresh Application Data**.
 
<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-refresh-application-data.png' />

- Return to Appcircle and then enter **Group Attribute Name** as ``groups`` and **Role Attribute Name** as ``roles``.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-oidc-group-role-claim-name.png' />

- Now you can define group and role mappings. Please refer to [Group and Role Mapping Configuration](/account/my-organization/integrations/authentications/sso-providers-configuration/single-sign-on#group-and-role-mapping-configuration).