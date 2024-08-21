---
title: Okta SAML
description: Implement SAML authentication in your app with Appcircle. Enhance user security and streamline login processes.
tags: [account, organization, sso, okta, saml, configuration]
sidebar_position: 6
---

import Screenshot from '@site/src/components/Screenshot';

# Okta SAML

Appcircle supports [Okta](https://www.okta.com/) as OpenID or SAML provider.

:::info

Only Enterprise accounts support SSO.

:::

### Enable SSO

SSO can only be enabled by the organization's administrator. To start, go to [My Organization](/account/my-organization) screen and click the **Enable Login** button under the **APPCIRCLE LOGIN** section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/enable-sso_v3.png' />

### Configure Appcircle and Okta

- Select Setup SAML SSO Provider

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-form_v2.png' />

- Pick an alias and display name for your organization. Please pick a short and rememberable alias.

- This screen will auto-generate an URL for the next step

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-saml1.png' />

- Login to your [Okta](https://www.okta.com/) account and navigate to Applications and then click **Create App Integration**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/oktacreateapp.png' />

- Select **SAML 2.0** as Sign In Method

<Screenshot url='https://cdn.appcircle.io/docs/assets/oktacreatesaml.png' />

- Pick a name and optional logo for the app.

<Screenshot url='https://cdn.appcircle.io/docs/assets/oktasamlsettings1.png' />

- Add the Appcircle Redirect URL to **Single sign on URL** write `https://auth.appcircle.io/auth/realms/appcircle` for the **Audience URI (SP Entity ID)** and select `EmailAddress` for the Name ID format.

<Screenshot url='https://cdn.appcircle.io/docs/assets/oktasamlsettings2.png' />

- Instead of writing all the settings of SAML, you can download the settings file from Okta and upload it. Click the "Copy" button of **Metadata URL** and open it another tab then save the XML file.

<Screenshot url='https://cdn.appcircle.io/docs/assets/oktasamlsettings3-new.png' />

- Go back to Appcircle, upload this XML file by clicking the button under **Import SAML Configuration**

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-saml1.png' />

- Check all the settings on this page and confirm that Redirect and SSO URLs are imported correctly. You can check if the X509 Certificate is imported correctly as well. If you want to enter multiple certificates you can separate them by using a comma between them. Please be aware that you need to remove any new lines or file headers from this edit box. This edit box only accepts a long base64 encoded string.

- The Group Attribute Name and Role Attribute Name fields are optional. Please refer to the [SSO Mapping Documentation](/account/my-organization/sso-providers-configuration/okta-saml#sso-mapping).

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

- Navigate to the **Applications** section and click on **Applications** tab.
- Select your application from the list and navigate to the **Assignments** tab. Assign the previously created groups to the application.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-assign-groups-to-application.png' />

- User roles will be stored in a user attribute. 
- Navigate to the **Directory** section, click on **Profile Editor**. Select the **User (default)** from profile list.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-profile-editor.png' />

- Click on **Add Attribute**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-create-user-attribute1.png' />

- Add a new user attribute as shown in the image below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-create-user-attribute2.png' />

- Now, you can edit the roles attribute of users. 
- Navigate to the **Directory** section, click on **People**, select a user from the list, and then click on the **Profile** tab. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-edit-user-attribute1.png' />

- Click on **Edit** and update the user's role attribute. For example, set it to 'Manager'.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-edit-user-attribute2.png' />

- Claim names for group and role need to be determined. These values can be changed via application settings.
- Navigate to the **Applications** section, click on **Applications** tab.
- Select your application from the list and navigate to the General tab. Click on **Edit** in **SAML Settings**

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-application-edit-saml.png' />

- Enter the Group and Attribute statement as as shown in the image below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-add-saml-statement.png' />

- Go back to Appcircle, enter **Group Attribute Name** as ``groups`` and **Role Attribute Name** as ``roles``.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-saml-ac-group-role-attribute-name.png' />

- Now you can define group and role mappings. Please refer to [Group and Role Mapping Configuration](/account/my-organization/sso-providers-configuration/single-sign-on#group-and-role-mapping-configuration).