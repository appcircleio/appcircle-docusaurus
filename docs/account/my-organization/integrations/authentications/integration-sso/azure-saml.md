---
title: Microsoft Entra ID (Azure AD) SAML Configuration
description: Configure Microsoft Entra ID SAML for Single Sign-On (SSO) in your app. A detailed guide to boost security and simplify user logins with Appcircle.
tags: [account, organization, sso, azure_ad, microsoft_entra_id, saml, configuration]
sidebar_position: 3
sidebar_label: Microsoft Entra ID SAML
---

import Screenshot from '@site/src/components/Screenshot';

# Microsoft Entra ID SAML Configuration

The document provides a comprehensive guide for setting up Single Sign-On (SSO) login functionality within an organization's infrastructure.
It outlines a series of steps to integrate SSO using Microsoft Entra ID as the identity provider, facilitating seamless access to various applications and resources.

Beginning with navigating to the organization's Integrations screen and initiating the connection process, users are guided through the configuration steps, which include creating and setting up a SAML SSO Provider.
The document also covers the necessary configurations within Microsoft Entra ID, such as creating an app integration and configuring SAML 2.0 settings.

Additionally, it offers guidance on advanced settings, including the importation of SAML configurations from Microsoft Entra ID.
Through clear instructions and actionable steps, the document aims to empower users in implementing a robust SSO solution.

Appcircle supports [Microsoft Entra ID](https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id) as OpenID or SAML provider.

:::info

Only Enterprise accounts support SSO.

:::

:::caution

Please be aware that, enabling SSO for **APPCIRCLE LOGIN** doesn't enable SSO for Testing Distribution and Enterprise App Store. They must be configured separately.

:::

## SSO Login

- To start, go to [My Organization](/account/my-organization) > Integrations screen and press the **Connect** button next to SSO Login under the **Authentications** section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-login1.png' />

- Click Create button to create your SSO Login

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-login2.png' />

:::info

If you want to manage user groups within your SSO provider, you should set **_CLAIM NAME (OPENID) / ATTRIBUTE NAME (SAML)_** field.

:::

- Select Setup SAML SSO Provider

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-login3.png' />

- Pick an alias and display name for your organization. Please pick a short and rememberable alias.

- This screen will auto-generate an URL for the Enterprise App Store and Testing Distribution.

<Screenshot url='https://cdn.appcircle.io/docs/assets/2777-sso-saml1-new.png' />

## Microsoft Entra ID App Integration

- Log in to [Azure AD](https://azure.microsoft.com/en-us/) as an admin and navigate to **Azure Services** and then click **Azure Active Directory**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/azurecreateapp1.png' />

- Click **Enterprise applications**

<Screenshot url='https://cdn.appcircle.io/docs/assets/azurecreateapp2.png' />

- Click **New application**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/azurecreateapp3.png' />

- Click **Create your own application**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/azurecreateapp4.png' />

- Give a name for your application and select **Integrate another application you don't find in the gallery (Non-gallery)** and click **Create**

<Screenshot url='https://cdn.appcircle.io/docs/assets/azurecreateapp5.png' />

### Adding Users

You need to select users/groups in Azure AD to enable SSO. All members of your Appcircle organization must be added to Azure AD.

- Select **Users and groups** and click **Add user/group**

<Screenshot url='https://cdn.appcircle.io/docs/assets/azureaddusers.png' />

- Click **Add Assignment**, find the users from the list, and click **Select**

<Screenshot url='https://cdn.appcircle.io/docs/assets/azureaddassignment1.png' />

- Finally, click the **Assign** button to confirm the assignment.

<Screenshot url='https://cdn.appcircle.io/docs/assets/azureaddassignment2.png' />

### Configuring SSO

- Click **Single sign-on** and select **SAML**

<Screenshot url='https://cdn.appcircle.io/docs/assets/azuressosettings1.png' />

- Click **Edit** button on **Basic SAML Configuration** section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/azuressosettings2.png' />

- Add `the Store Redirect URL` and `Distribute Redirect URL` to **Reply URL (Assertion Consumer Service URL)**
- Write `https://auth.appcircle.io/auth/realms/store` for the **Identifier (Entity ID)**

<Screenshot url='https://cdn.appcircle.io/docs/assets/integration-sso-azure-entity-id.png' />

- Edit the attributes according to the below screenshot.

<Screenshot url='https://cdn.appcircle.io/docs/assets/azuressosettings4.png' />

- Instead of writing all the settings of SAML, you can download the settings file from Azure AD and upload it. Click the **Download** button next to the **Federation Metadata XML** link to download the XML file.

<Screenshot url='https://cdn.appcircle.io/docs/assets/azuressosettings5.png' />

- Go back to Appcircle, upload this XML file by clicking the button under **Import SAML Configuration**

<Screenshot url='https://cdn.appcircle.io/docs/assets/2777-sso-saml1-new.png' />

- Check all the settings on this page and confirm that Redirect and SSO URLs are imported correctly. You can check if the X509 Certificate is imported correctly as well. If you want to enter multiple certificates you can separate them by using a comma between them. Please be aware that you need to remove any new lines or file headers from this edit box. This edit box only accepts a long base64 encoded string.

:::info
If you are a **self-hosted Appcircle user**, then you should change the domain of the **Store and Distribute Redirect URL** to your own domain.

You must use the same `auth` domain address with the `store redirect URL`.

For example your Store Redirect URL is `https://auth.self.spacetech.com/auth/realms/store/broker/identity-spacetech/endpoint,
Distribute Redirect URL is `https://auth.self.spacetech.com/auth/realms/distribute/broker/identity-spacetech/endpoint`
:::

## Microsoft Entra ID Managing User Groups

Managing user groups within Microsoft Entra ID provides users and organizations with several benefits.
By organizing users into groups, administrators can efficiently manage access permissions for various applications and resources, saving time and effort.
Administrators can synchronize Microsoft Entra ID user groups with Appcircle, allowing for granular access control and group-based permissions.
This integration enhances security, simplifies access management, and promotes collaboration within organizations utilizing the Appcircle platform.

- Log in to [Azure](https://azure.microsoft.com/en-us/) as an admin and navigate to **Azure Services** and then click **Microsoft Entra ID**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-azure-saml-goto-entra-id.png' />

- Navigate to **Manage > Groups**, and click on **New Group**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-azure-saml-groups.png' />

- Assign a proper name and description to the new group. Designate an owner and members to the group.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-azure-saml-new-group.png' />

- Navigate to **Azure Services** and then click **Microsoft Entra ID**. Click on **Manage > Enterprise applications**. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-azure-saml-enterprise-applications1.png' />

- Click on your application. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-azure-saml-enterprise-applications2.png' />

- Click on **Assign users and groups**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-azure-saml-assign-users-groups1.png' />

- Click on **Add user/group**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-azure-saml-assign-users-groups2.png' />

- Select users and groups . This process can be repeated as needed.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-azure-saml-assign-users-groups3.png' />

- Navigate to **Manage > Single sign-on**. Click on **Edit** in **Attributes & Claims** section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-azure-saml-attributes1.png' />

- Click on **Add a Group Claim**. Select **Groups assigned to the application** and select **Groups assigned to the application** as source attribute. Then click on **Save**

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-azure-saml-attributes2.png' />

- Go back to Appcircle, go to [My Organization](/account/my-organization) > Integrations screen and press the **Manage** button next to SSO Login under the **Authentications** section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/integration-sso-manage-sso.png' />

- Update the **Claim Name** as `http://schemas.microsoft.com/ws/2008/06/identity/claims/groups`.

<Screenshot url='https://cdn.appcircle.io/docs/assets/integration-sso-azure-saml-org-id-claim.png' />

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
