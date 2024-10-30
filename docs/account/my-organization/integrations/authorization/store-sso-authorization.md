---
title: Enterprise App Store SSO Authorization
description: Establish SSO authorization your Enterprise App Store. Enhance security and simplify access across Appcircle's platform.
tags: [account, organization, configuration]
sidebar_position: 3
---

### Introduction

Managing user groups within Auth0 provides users and organizations with several benefits. By organizing users into groups, administrators can efficiently manage access permissions for various applications and resources, saving time and effort. Administrators can synchronize Auth0 user groups with Appcircle, allowing for granular access control and group-based permissions. This integration enhances security, simplifies access management, and promotes collaboration within organizations utilizing the Appcircle platform.

### Summary of Configuration Steps

This section provides a brief summary of the configuration steps.

1. Perform identity provider-specific configurations, including creating groups, and defining group claims/attributes.
2. In Appcircle, specify the **Claim Name (OpenID)/Attribute Name (SAML)** according to your Identity Provider configuration.
3. In Appcircle, enable **SSO Authentication** for Enteprise App Store and Testing Distribution.

### Specific Provider Configuration

<details>
    <summary>Auth0</summary>

<details>
    <summary>Auth0 (OpenID Connect)</summary>

#### Step 1. Create Organizations

1. In the Auth0 dashboard, navigate to the **Organization** section.
2. Click **Create Organization** button to create organizations.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-create-groups.png' />

3. Click created organization to navigated **Organization Details**.
4. On the **Organization Details** screen, click on the **Members** tab to manage members of organization.
5. Click the **Add Members** button. Add users who will become members of your organization.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-add-members.png' />

6. On the **Organization Details** screen, navigate to the **Connections** tab.
7. Click the **Enable Connections** button
8. Select **Username-Password-Authentication** and click on **Enable Connection** 

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-enable-connections.png' />

9. Select **Enable Auto-Membership** and **Enable Signup** on the displayed screen, then click **Save**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-enable-connections2.png' />

#### Step 2. Enable organization for your application

1. In the Auth0 dashboard, navigate to the **Applications** section.
2. Select the relevant application. 
3. On the **Application Details** screen, navigate to the **Organizations** tab.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-application-organizations1.png' />

4. Click **Disable Grants Now**.
5. Choose **Business Users** for the type of users and select **Prompt for Organization** for the login flow.
6. Click **Save Changes**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-application-organizations2.png' />

#### Step 3. Define Group Claim Name

1. Navigate to the **SSO Login** screen in Appcircle.
2. Enter the **Claim Name (OpenID)/Attribute Name (SAML)** as `org_id`.

<Screenshot url='https://cdn.appcircle.io/docs/assets/integration-sso-org-id-claim.png' />

</details>

<details>
    <summary>Auth0 (SAML)</summary>

#### Step 1. Create Organizations

1. In the Auth0 dashboard, navigate to the **Organization** section.
2. Click **Create Organization** button to create organizations.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-create-groups.png' />

3. Click created organization to navigated **Organization Details**.
4. On the **Organization Details** screen, click on the **Members** tab to manage members of organization.
5. Click the **Add Members** button. Add users who will become members of your organization.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-add-members.png' />

6. On the **Organization Details** screen, navigate to the **Connections** tab.
7. Click the **Enable Connections** button
8. Select **Username-Password-Authentication** and click on **Enable Connection** 

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-enable-connections.png' />

9. Select **Enable Auto-Membership** and **Enable Signup** on the displayed screen, then click **Save**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-enable-connections2.png' />

#### Step 2. Enable organization for your application

1. In the Auth0 dashboard, navigate to the **Applications** section.
2. Select the relevant application. 
3. On the **Application Details** screen, navigate to the **Organizations** tab.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-application-organizations1.png' />

4. Click **Disable Grants Now**.
5. Choose **Business Users** for the type of users and select **Prompt for Organization** for the login flow.
6. Click **Save Changes**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-application-organizations2.png' />

#### Step 3. Define Group Attribute Name

1. Navigate to the **SSO Login** screen in Appcircle.
2. Enter the **Claim Name (OpenID)/Attribute Name (SAML)** as `http://schemas.auth0.com/org_id`.

<Screenshot url='https://cdn.appcircle.io/docs/assets/integration-sso-auth0-saml-org-id-claim.png' />

</details>

</details>

<details>
    <summary>Microsoft Entra ID (formerly Azure Active Directory) </summary>

<details>
    <summary>Microsoft Entra ID (SAML)</summary>

#### Step 1. Create Groups in Microsoft Entra ID

1. Log in to [Azure](https://azure.microsoft.com/en-us/) as an admin and navigate to **Azure Services > Microsoft Entra ID** 

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-azure-saml-goto-entra-id.png' />

2. Navigate to the **Manage > Groups** section from left menu.
3. Click the **New Group**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-azure-saml-groups.png' />

4. Assign a proper name and description to the new group. Designate an owner and members to the group.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-azure-saml-new-group.png' />

#### Step 3. Assign user and group to application in Microsoft Entra ID

1. Navigate to the **Azure Services > Microsoft Entra ID**.
2. Navigate to the **Manage > Enterprise applications** section from left menu. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-azure-saml-enterprise-applications1.png' />

3. Click your application. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-azure-saml-enterprise-applications2.png' />

4. Click **Assign users and groups**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-azure-saml-assign-users-groups1.png' />

5. Click **Add user/group**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-azure-saml-assign-users-groups2.png' />

6. Select users, groups and role. This process can be repeated as needed.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-azure-saml-assign-users-groups3.png' />

#### Step 4. Define Group Attributes & Claims in Microsoft Entra ID

1. Navigate to the **Manage > Single sign-on** section from left menu. 
2. Click **Edit** in **Attributes & Claims** section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-azure-saml-attributes1.png' />

3. Click the **Add a Group Claim**. 
4. Select the **Groups assigned to the application** 
5. Select the **Cloud only group display names** as source attribute. 
6. Then click on the **Save** button

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-azure-saml-attributes2.png' />

#### Step 5. Define Group Role Attributes names in Appcircle

1. Navigate to the **SSO Login** screen in Appcircle.
2. Enter the **Claim Name (OpenID)/Attribute Name (SAML)** as ``http://schemas.microsoft.com/ws/2008/06/identity/claims/groups``.

<Screenshot url='https://cdn.appcircle.io/docs/assets/integration-sso-azure-saml-org-id-claim.png' />

</details>

</details>

<details>
    <summary>Okta</summary>

<details>
    <summary>Okta (OpenID Connect)</summary>

#### Step 1. Create Groups and Define Group Claim

1. Navigate to the **Directory > Groups** section in the Okta Dashboard
2. Create the groups as needed.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-create-groups.png' />

3. Assign users to groups.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-assign-users-to-groups.png' />

4. Navigate to the **Applications > Applications** section from left navigation menu.
5. Select your application from the list 
6. Navigate to the **Sign on** tab. 
7. Click **Edit** for OpenID Connect ID Token.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-oidc-edit-id-token.png' />

8. Enter Groups claim filter as shown in the image below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-oidc-groups-claim.png' />

9. Navigate to the **Applications > Applications** section from left navigation menu.
10. Click **Refresh Application Data**.
 
<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-refresh-application-data.png' />

#### Define Group Claim in Appcircle

1. Navigate to the **SSO Login** screen in Appcircle.
2. Enter the **Claim Name (OpenID)/Attribute Name (SAML)** as ``groups``.

<Screenshot url='https://cdn.appcircle.io/docs/assets/integration-sso-groups-claim.png' />

</details>

<details>
    <summary>Okta (SAML)</summary>

#### Step 1. Create Groups and Assign to the Application

1. Navigate to the **Directory > Groups** section in the Okta Dashboard. Create the groups as needed.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-create-groups.png' />

2. Assign users to groups.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-assign-users-to-groups.png' />

3. Navigate to the **Applications > Applications** section from left navigation menu.
4. Select your application from the list 
5. Navigate to the **Assignments** tab. 
6. Assign the previously created groups to the application.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-assign-groups-to-application.png' />

#### Step 3. Define Group Attributes

1. Navigate to the **Applications > Applications** section.
2. Select your application from the list and navigate to the **General** tab.
3. Click on **Edit** in **SAML Settings**

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-application-edit-saml.png' />

4. Enter the Group Attribute statement as as shown in the image below. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/2812-okta-groups-7.png' />

#### Step 4. Define Group and Role Claim in Appcircle

1. Navigate to the **SSO Login** screen in Appcircle.
2. Enter the **Claim Name (OpenID)/Attribute Name (SAML)** as ``groups``.

<Screenshot url='https://cdn.appcircle.io/docs/assets/integration-sso-groups-claim.png' />

</details> 

</details>

### Testing and Troubleshooting

After configuring Authorization with SSO for Enterprise App Store, it is important to test the integration to ensure that users authorization work seamlessly and as expected. Follow [Enterprise App Store Documentation](/enterprise-app-store/enterprise-app-store-profile) to test the integration.