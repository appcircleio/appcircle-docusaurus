---
title: SSO Authorization
description: Establish SSO authorization your organization. Enhance security and simplify access across Appcircle's platform.
tags: [account, organization, configuration]
sidebar_position: 2
---

## 1. Introduction

In Appcircle, authorization for SSO users is managed by mapping user roles and groups from your identity provider (IdP) to specific module permissions within Appcircle. This ensures seamless Role-Based Access Control (RBAC) across the platform.  
Before configuring SSO-based authorization, you must first complete the SSO integration setup. You can refer to the [SSO Integration Documentation](/account/my-organization/integrations/authentications/sso-authentication) for detailed instructions on how to configure SSO with your chosen provider, such as Keycloak, Azure AD, Okta, or Auth0.  
Once SSO integration is complete, you can configure authorization by mapping IdP roles and groups to Appcircle module permissions.

### Prerequisites

-   SSO integration with your chosen identity provider (Auth0, Azure AD, Okta, OneLogin, Keycloak).
-   Knowledge of groups and roles in your IdP that you want to map to Appcircle permissions.
-   Administrative access to Appcircle and your IdP.

## 2. General Configuration Steps

These steps will guide you through the configuration within your chosen identity provider and Appcircle.

<details>
  <summary>Step 1: Configure Your Identity Provider</summary>

1. Perform identity provider-specific configurations, including creating groups and roles, and defining group and role claims/attributes. 
2. In Appcircle, enter the group and role claim/attribute names as defined in your IdP.

Follow **3. Specific Provider Configuration** section to complete this steps.

</details>

<details>
  <summary>Step 2: Enable SSO Mapping and Configure Group and Role Mappings</summary>

### Accessing SSO Mapping Settings

1. Navigate to the **Organization** section on your dashboard.
2. Select the **Integrations** and click on the **Appcircle Login**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/navigate-sso-mapping1.png' /> 

3. Enable **SSO Mapping** and click **Configure** .

<Screenshot url='https://cdn.appcircle.io/docs/assets/navigate-sso-mapping2.png' /> 

### Group and Role Mapping Configuration

1. Enter the name of the SSO group and select the corresponding Appcircle organization you want to map. Ensure the group name is correct.

2. Click Add to map the SSO group to an Appcircle organization. This will automatically link users from the SSO group to the selected organization in Appcircle.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-group-mapping.png' /> 

3. You can define role mappings for each group mapping. Click the **Configure** button to set up role mappings.
4. Enter the role name and select the corresponding Appcircle roles you want to map. Ensure the role name is correct.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-role-mapping.png' /> 

</details>

## 3. Specific Provider Configuration

<details>
    <summary>Auth0</summary>

<details>
    <summary>Auth0 (OpenID Connect)</summary>

#### Step 1. Create Roles

1. In the Auth0 dashboard, navigate to the **User Management > Roles** section.
2. Click **Create Role** button. Create necessary roles.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-create-roles.png' />

#### Step 2. Create Organization

1. In the Auth0 dashboard, navigate to the **Organization** section.
2. Click **Create Organization** button to create organizations.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-create-groups.png' />

3. Click the created organization to navigate to **Organization Details**.
4. On the **Organization Details** screen, click the **Members** tab to manage members of organization.
5. Click the **Add Members** button to add users who will become members of your organization.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-add-members.png' />

6. On the **Members** screen, click the three dots and select **Assign Roles**. Assign the desired roles to users for organization.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-assign-roles.png' />

7. On the **Organization Details** screen, navigate to the **Connections** tab.
8. Click the **Enable Connections** button
9. Select **Username-Password-Authentication** and click **Enable Connection** 

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-enable-connections.png' />

10. Select **Enable Auto-Membership** and **Enable Signup** on the displayed screen, then click **Save**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-enable-connections2.png' />

#### Step 3. Enable Organization for your application

1. In the Auth0 dashboard, navigate to the **Applications** section.
2. Select the relevant application.
3. On the **Application Details** screen, navigate to the **Organizations** tab.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-application-organizations1.png' />

4. Click **Disable Grants Now**.
5. Choose **Business Users** for the type of users and select **Prompt for Organization** for the login flow.
6. Click **Save Changes**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-application-organizations2.png' />

#### Step 4. Define Group And Role Attributes & Claims

The user's group and role values should be included in the token as claims. This enables retrieval of the user's group and role during SSO login. The groups claim is already present in the token. Follow these steps to add the roles claim:

1. In the Auth0 dashboard, navigate to the **Actions > Library** section.
2. Click the **Create Action** button and select **Build from Scratch**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-actions-library1.png' />

3. Enter an appropriate name for the **Custom Action** in the popup window. Keep the remaining settings at their default values,as shown in the image below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-actions-library2.png' />

4. On the **Custom Action Details** screen, copy and paste following Javascript code to code editor.

```js
exports.onExecutePostLogin = async (event, api) => {
  const namespace = 'your_namespace_';
  if (event.authorization) {
    api.idToken.setCustomClaim(`${namespace}roles`, event.authorization.roles);
    api.accessToken.setCustomClaim(`${namespace}roles`, event.authorization.roles);
  }
}
```

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-actions-library3.png' />

5. Finally click on the **Deploy** button.
6. In the Auth0 dashboard, navigate to the **Flows** section.
7. Click the Login.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-actions-flows1.png' />

8. Drag and drop the custom action created previously. The role claim has been added to the token.

#### Step 5. Define Group and Role Claim Names in Appcircle

1. Navigate to the **Set up OpenID Provider** screen in Appcircle, which you accessed during the SSO setup in the "General Configuration Steps."
2. Enter the Group Claim Name as org_id and the Role Claim Name as your_namespace_roles. Note that the role claim is created as a custom claim in Auth0, so use the name you determined earlier.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-oidc-ac-group-role-claim-name.png' />

</details>

<details>
    <summary>Auth0 (SAML)</summary>

#### Step 1. Create Roles

1. In the Auth0 dashboard, navigate to the **User Management > Roles** section.
2. Click **Create Role** button. Create necessary roles.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-create-roles.png' />

#### Step 2. Create Organization

1. In the Auth0 dashboard, navigate to the **Organization** section.
2. Click **Create Organization** button to create organizations.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-create-groups.png' />

3. Click the created organization to navigate to **Organization Details**.
4. On the **Organization Details** screen, click the **Members** tab to manage members of organization.
5. Click the **Add Members** button to add users who will become members of your organization.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-add-members.png' />

6. On the **Members** screen, click the three dots and select **Assign Roles**. Assign the desired roles to users for organization.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-assign-roles.png' />

7. On the **Organization Details** screen, navigate to the **Connections** tab.
8. Click the **Enable Connections** button
9. Select **Username-Password-Authentication** and click **Enable Connection** 

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-enable-connections.png' />

10. Select **Enable Auto-Membership** and **Enable Signup** on the displayed screen, then click **Save**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-enable-connections2.png' />

#### Step 3. Enable Organization for your application

1. In the Auth0 dashboard, navigate to the **Applications** section.
2. Select the relevant application.
3. On the **Application Details** screen, navigate to the **Organizations** tab.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-application-organizations1.png' />

4. Click **Disable Grants Now**.
5. Choose **Business Users** for the type of users and select **Prompt for Organization** for the login flow.
6. Click **Save Changes**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-application-organizations2.png' />

#### Step 4. Define Group And Role Attributes & Claims

The user's group and role values should be included in the token as claims. This enables retrieval of the user's group and role during SSO login. The groups claim is already present in the token. Follow these steps to add the roles claim:

1. In the Auth0 dashboard, navigate to the **Actions > Library** section.
2. Click the **Create Action** button and select **Build from Scratch**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-actions-library1.png' />

3. Enter an appropriate name for the **Custom Action** in the popup window. Keep the remaining settings at their default values,as shown in the image below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-actions-library2.png' />

4. On the **Custom Action Details** screen, copy and paste following Javascript code to code editor.

```js
exports.onExecutePostLogin = async (event, api) => {
  const namespace = 'your_namespace_';
  if (event.authorization) {
    api.idToken.setCustomClaim(`${namespace}roles`, event.authorization.roles);
    api.accessToken.setCustomClaim(`${namespace}roles`, event.authorization.roles);
  }
}
```

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-actions-library3.png' />

5. Finally click on the **Deploy** button.
6. In the Auth0 dashboard, navigate to the **Flows** section.
7. Click the Login.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-actions-flows1.png' />

8. Drag and drop the custom action created previously. The role claim has been added to the token.

#### Step 5. Define Group and Role Attributes names in Appcircle

1. Navigate to the **Set up OpenID Provider** screen in Appcircle, which you accessed during the SSO setup in the "General Configuration Steps."
2. Enter the Group Attribute Name as `http://schemas.auth0.com/org_id` and the Role Attribute Name as `http://schemas.auth0.com/your_namespace_roles`. Note that the role attribute is created as a custom attribute in Auth0, so you must use the name you determined previously.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-auth0-saml-ac-group-role-attribute-name.png' />

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

#### Step 2. Create Roles in Microsoft Entra ID

1. Navigate to the **Manage > App registrations** section from left menu.
2. Select **All applications** to view a list of all your applications and locate your application.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-azure-saml-app-registrations.png' />

3. Navigate to the **Manage > App Roles** section from left menu.
4. Click the **Create app role**. Create a new app role as shown in the image below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-azure-saml-create-app-roles.png' />

5. Navigate to the **Manage > API permissions** section from left menu.
6. Click the **Add Permissions**. 
7. Select the **My APIs** and click on your application name.  

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-azure-saml-api-permissions1.png' />

8. Select **permissions** and click on **Add permissions**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-azure-saml-api-permissions2.png' />

#### Step 3. Assign user, group and roles to application in Microsoft Entra ID

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

#### Step 4. Define Group and Role Attributes & Claims in Microsoft Entra ID

1. Navigate to the **Manage > Single sign-on** section from left menu. 
2. Click **Edit** in **Attributes & Claims** section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-azure-saml-attributes1.png' />

3. Click the **Add a Group Claim**. 
4. Select the **Groups assigned to the application** 
5. Select the **Cloud only group display names** as source attribute. 
6. Then click on the **Save** button

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-azure-saml-attributes2.png' />

7. Click **Add new claim**. 
8. Enter name as **roles** 
9. Select **user.assignedroles** as source attribute. 
10. Then click on **Save**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-azure-saml-attributes3.png' />

#### Step 5. Define Group and Role Attribute names in Appcircle

1. Navigate to the **Set up SAML SSO Provider** screen in Appcircle, which you accessed during the SSO setup in the "General Configuration Steps."
2. Enter **Group Attribute Name** as ``http://schemas.microsoft.com/ws/2008/06/identity/claims/groups`` and **Role Attribute Name** as ``roles``.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-azure-saml-ac-group-role-attribute-name.png' />

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

#### Step 2. Create and Set Role Attribute to User

The roles will be stored in user attributes.

1. Navigate to the **Directory > Profile Editor** section from left navigation menu.
2. Select the **User (default)** from profile list.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-profile-editor.png' />

3. Click **Add Attribute**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-create-user-attribute1.png' />

4. Add a new user attribute as shown in the image below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-create-user-attribute2.png' />

5. Navigate to the **Directory > Profile Editor** section from left navigation menu.
6. Select the **Your Application Name User** from the profile list.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-oidc-profile-editor.png' />

8. Click **Mappings** and map user roles attribute to application user roles attribute as shown in the image below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-oidc-map-roles-attribute.png' />

9. Navigate to the **Directory > People** section from left navigation menu.
10. Select a user from the list.
11. Navigate to the **Profile** tab. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-edit-user-attribute1.png' />

12. Click **Edit** and update the user's role attribute. For example, set it to 'Manager'.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-edit-user-attribute2.png' />

#### Step 3. Define the Role Claim

1. Navigate to the **Security > API > Authorization Servers** section from left navigation menu.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-oidc-security-api.png' />

2. Click **default**
3. Navigate to the **Claims** tab. 
4. Add new claim as shown in the image below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-oidc-add-roles-claim.png' />

5. Navigate to the **Applications > Applications** section from left navigation menu.
6. Click **Refresh Application Data**.
 
<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-refresh-application-data.png' />

#### Step 4. Define Group and Role Claim in Appcircle

1. Navigate to the **Set up OpenID SSO Provider** screen in Appcircle, which you accessed during the SSO setup in the "General Configuration Steps."
2. Enter **Group Attribute Name** as ``groups`` and **Role Attribute Name** as ``roles``.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-oidc-group-role-claim-name.png' />

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

#### Step 2. Create and Set Role Attribute to User

The roles will be stored in user attributes.

1. Navigate to the **Directory > Profile Editor** section from left navigation menu.
2. Select the **User (default)** from profile list.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-profile-editor.png' />

3. Click **Add Attribute**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-create-user-attribute1.png' />

4. Add a new user attribute as shown in the image below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-create-user-attribute2.png' />

5. Navigate to the **Directory > Profile Editor** section from left navigation menu.
6. Select the **Your Application Name User** from the profile list.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-oidc-profile-editor.png' />

8. Click **Mappings** and map user roles attribute to application user roles attribute as shown in the image below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-oidc-map-roles-attribute.png' />

9. Navigate to the **Directory > People** section from left navigation menu.
10. Select a user from the list.
11. Navigate to the **Profile** tab. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-edit-user-attribute1.png' />

12. Click **Edit** and update the user's role attribute. For example, set it to 'Manager'.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-edit-user-attribute2.png' />

#### Step 3. Define Group and Role Attributes

1. Navigate to the **Applications > Applications** section.
2. Select your application from the list and navigate to the **General** tab.
3. Click on **Edit** in **SAML Settings**

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-application-edit-saml.png' />

4. Enter the Group and Role Attribute statement as as shown in the image below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-add-saml-statement.png' />

#### Step 4. Define Group and Role Claim in Appcircle

1. Navigate to the **Set up OpenID SSO Provider** screen in Appcircle, which you accessed during the SSO setup in the "General Configuration Steps."
2. Enter **Group Attribute Name** as ``groups`` and **Role Attribute Name** as ``roles``.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-mapping-okta-saml-ac-group-role-attribute-name.png' />

</details> 

</details>

## 4. Testing and Verification

After configuring SSO Mapping, it is important to test the integration to ensure that users have the correct permissions based on their roles and groups. This section covers how to test the integration.

When a user logs into Appcircle, their organization membership and roles are updated according to the configured Group and Role Mapping.

1. Open an incognito window in your browser to avoid any cached sessions interfering with the test.
2. Use SSO to log in to Appcircle with a test account.
3. Verify if the user's organization membership and roles are updated according to the configured Group and Role Mapping.

:::info

In self-hosted deployments, the organization memberships and roles of admin users do not change with SSO authorization; they will remain the same.

:::

:::info

Organizations must have at least one owner. After processing SSO Authorization Mapping, if there are no remaining owners in the organization, the user's role and organization membership will remain unchanged for that organization.

:::

## 5. Limitations

Due to technical limitations, SSO mapping does not support automatic synchronization. Changes such as the removal of a user from the Identity Provider or updates to their groups or roles will only take effect when the user logs in to Appcircle.