---
title: Auth0 SAML
description: Enable Auth0 SAML for secure user sign-in in your app. Simplify access and enhance security with Appcircle's integration.
tags: [account, organization, sso, auth0, saml, configuration]
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';

# Auth0 SAML

Appcircle supports [Auth0](https://auth0.com/) as OpenID or as a SAML provider.

:::info

Only Enterprise accounts support SSO.

:::

### Enable SSO

SSO can only be enabled by the organization's administrator. To start, go to [My Organization](/account/my-organization) screen and click the **Enable Login** button under the **APPCIRCLE LOGIN** section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/enable-sso_v3.png' />

### Configure Appcircle and Auth0

- Select Setup SAML SSO Provider

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-form_v2.png' />

- Pick an alias and display name for your organization. Please pick a short and rememberable alias.

- This screen will auto-generate an URL for the next step

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-saml1.png' />

- Login to your [Auth0](https://auth0.com/) account and navigate to Applications and then click **Create Application**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/authcreateapp.png' />

- Select **Regular Web Applications** and give a name

<Screenshot url='https://cdn.appcircle.io/docs/assets/authwebapp.png' />

- Navigate to **Addons** of the app and enable the SAML option.

<Screenshot url='https://cdn.appcircle.io/docs/assets/authsamlsettings1.png' />

- Click the SAML button and change the settings. For the Callback URL write down the callback URL you have created earlier. For the settings, paste the below JSON

```json
{
  "nameIdentifierFormat": "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress",
  "nameIdentifierProbes": [
    "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress"
  ]
}
```

<Screenshot url='https://cdn.appcircle.io/docs/assets/authsamlsettings2.png' />

- Instead of writing all the settings of SAML, you can download the settings file from Auth0 and upload it. Navigate to the **Usage** and then click the **Download** button to download the XML file

<Screenshot url='https://cdn.appcircle.io/docs/assets/authsamlsettings3.png' />

- Go back to Appcircle, upload this XML file by clicking the button under **Import SAML Configuration**

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-saml1.png' />

- Check all the settings on this page and confirm that Redirect and SSO URLs are imported correctly. You can check if the X509 Certificate is imported correctly as well. If you want to enter multiple certificates you can separate them by using a comma between them. Please be aware that you need to remove any new lines or file headers from this edit box. This edit box only accepts a long base64 encoded string.

- The Group Attribute Name and Role Attribute Name fields are optional. Please refer to the [SSO Mapping Documentation](/account/my-organization/sso-providers-configuration/auth-saml#sso-mapping).

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

- Navigate to the **User Management** section in the Auth0 Dashboard, click on **Roles**, and create the roles as needed.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-create-roles.png' />

- Navigate to the organization section and create organizations.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-create-groups.png' />

- Add users who will become members of your organization.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-add-members.png' />

- Click on the three dots and select **Assign Roles**. Assign the desired roles to users.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-assign-roles.png' />

- Navigate to the **Connections** tab and enable Connections for your organization. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-enable-connections.png' />

- Navigate to the "Applications" section. Select the relevant application, then go to the "Organizations" tab. Click on **"Disable Grants Now"**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-application-organizations1.png' />

Choose "**Business Users**" for the type of users and select "**Prompt for Organization**" for the login flow. Click on "**Save Changes**".

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

- Return to Appcircle, enter **Group Attribute Name** as ``http://schemas.auth0.com/org_id`` and **Role Attribute Name** as ``http://schemas.auth0.com/your_namespace_roles``. Note that the role claim is created as a custom claim in Auth0 so you must enter the name you determined previously.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-saml-ac-group-role-attribute-name.png' />

- Now you can define group and role mappings. Please refer to [Group and Role Mapping Configuration](/account/my-organization/sso-providers-configuration/single-sign-on#group-and-role-mapping-configuration).

:::caution

The ``org_id`` attribute value is equal to the organization ID, not the organization name.

:::