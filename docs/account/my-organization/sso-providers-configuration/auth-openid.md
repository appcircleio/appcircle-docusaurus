---
title: Auth0 OpenID
description: Set up OpenID Connect for user authentication in your app. Secure and simplify user access with Appcircle's integration.
tags: [account, organization, sso, auth0, openid, configuration]
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';

# Auth0 OpenID

Appcircle supports [Auth0](https://auth0.com/) as OpenID or as SAML provider.

:::info

Only Enterprise accounts support SSO.

:::

### Enable SSO

SSO can only be enabled by the organization's administrator. To start, go to [My Organization](/account/my-organization) screen and click the **Enable Login** button under the **APPCIRCLE LOGIN** section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/enable-sso_v3.png' />

### Configure Appcircle and Auth0

- Select **Setup OpenID Provider**

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-form_v2.png' />

- Pick an alias and display name for your organization. Please pick a short and rememberable alias.

- This screen will auto-generate an URL for the next step

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-openid1_v2.png' />

- Login to your [Auth0](https://auth0.com/) account and navigate to Applications and then click **Create Application**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/authcreateapp.png' />

- Select **Regular Web Applications** and give a name

<Screenshot url='https://cdn.appcircle.io/docs/assets/authwebapp.png' />

- Navigate to settings of the app and note, **Client ID** and **Client Secret**

<Screenshot url='https://cdn.appcircle.io/docs/assets/authopenidsettings1.png' />

- Add the Appcircle Redirect URL to your allowed list

<Screenshot url='https://cdn.appcircle.io/docs/assets/authopenidsettings2.png' />

- Instead of writing all the settings of OpenID, you can download the settings file from Auth0 and upload it. Navigate to the **OpenID Configuration** address and download that JSON file to your computer.

<Screenshot url='https://cdn.appcircle.io/docs/assets/authopenidsettings3.png' />

- Go back to Appcircle, upload this JSON file by clicking the button under **Import OpenID configuration**

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-openid1_v2.png' />

- Check all the settings on this page and confirm that Authorization and Token URLs are imported correctly. Enter your **Client ID** and **Client Secret**. Modify the settings as below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-openid2_v2.png' />

- The Group Claim Name and Role Claim Name fields are optional. Please refer to the [SSO Mapping Documentation](/account/my-organization/sso-providers-configuration/auth-openid#sso-mapping).

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

- To create roles, navigate to the **User Management** section in the Auth0 Dashboard, click on **"Roles"**, and create the necessary roles.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-create-roles.png' />

- Navigate to the organization section and create organizations.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-create-groups.png' />

- Add users who will become members of your organization.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-add-members.png' />

- Click on the three dots and select **Assign Roles**. Assign the desired roles to users.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-assign-roles.png' />

- Navigate to the **"Connections"** tab and enable connections for your organization.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-enable-connections.png' />

- Navigate to the "Applications" section. Select the relevant application, then go to the "Organizations" tab. Click on **"Disable Grants Now"**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-application-organizations1.png' />

- Choose **"Business Users"** for the type of users and select **"Prompt for Organization"** for the login flow. Click on **"Save Changes"**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-application-organizations2.png' />

- To retrieve the groups and roles of a user via tokens, follow these steps:

1. Navigate to **Actions**.
2. Click on the **Library** tab.
3. Select **Create Action**.
4. Choose **Build from Scratch**.

The groups claim is already present on the token, but these steps will help you add the roles claim as well.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-actions-library1.png' />

- Give an appropriate name to the custom action. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-actions-library2.png' />

- Paste following Javascript code and click on the deploy.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-actions-library3.png' />

```js
exports.onExecutePostLogin = async (event, api) => {
  const namespace = 'your_namespace';
  if (event.authorization) {
    api.idToken.setCustomClaim(`${namespace}roles`, event.authorization.roles);
    api.accessToken.setCustomClaim(`${namespace}roles`, event.authorization.roles);
  }
}
```
- Navigate to **Actions** and click on the **Flows** tab. 
- Click on the **Login**. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-actions-flows1.png' /> 

- Drag and drop the custom action created previously. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-actions-flows2.png' />

- Return to Appcircle and enter the **Group Claim Name** as ``org_id`` and the **Role Claim Name** as ``your_namespace_roles``. Note that the role claim is created as a custom claim in Auth0, so you must enter the name you determined previously.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-oidc-ac-group-role-claim-name.png' />

- Now you can define group and role mappings. Please refer to [Group and Role Mapping Configuration](/account/my-organization/sso-providers-configuration/single-sign-on#group-and-role-mapping-configuration).

:::caution

The ``org_id`` claim value is equal to the organization ID, not the organization name.

:::