---
title: Role Management
description: Overview of role management and permissions in Appcircle
tags:
  [
    permissions,
    role management,
    build profiles,
    environment variables,
    signing identity,
    distribution profiles,
    testing groups,
    store submit,
    publish,
    enterprise app store,
    organization management,
    billing management,
    third-party connections,
  ]
sidebar_position: 5
---

# Role Management

With Appcircle's [Advanced Role Management](/account/my-organization/profile-and-team/team-management#advanced-role-management) structure, you can assign specific roles to organization members for each module, allowing you to manage and restrict their permissions effectively. Appcircle provides various role types for each module, with a brief description of each role provided in the table below. For more detailed information on role management for each module, please refer to the respective module titles.

- **Owner**: The user is authorized for unlimited access to all modules.
- **Manager**: The user becomes the administrator of the relevant module with no restrictions.
- **Operator**: The user manages the operations of the relevant module, with certain restrictions in place.
- **Ext. Operator**: The user has very limited authorization in the relevant module, typically intended for third-party employees from outside the company.
- **Viewer**: The user only has view authorization in the relevant module and cannot take any action.

:::caution Role Types

Some role types are not used in certain modules because they are redundant or unnecessary, as they serve the same function as another role. Therefore, roles may vary for each module.

:::

:::caution Multiple Role Assignment for Users

When assigning roles on Appcircle, you can assign more than one role for a user at the same time. For example, a user can be both **Manager** and **Operator** in the Build module.

For this reason, Appcircle behavior will change when multiple roles are assigned. For example, you have assigned **Ext Operator** and **Viewer** role in **Publish Module** for a user. This means that the Ext Operator role now has the privileges of the Viewer role. So while Ext Operator cannot see Activity logs, it now has access to those logs because it also has the viewer role.

:::

### Build Permissions

The following table details the roles and restrictions for the [**Build**](/build) module. Please refer to the related module information and caution notes. 

| Build Sub-modules   | Scopes                                     | Owner | Manager | Operator | Viewer |
|---------------------|--------------------------------------------|-------|---------|----------|--------|
| Build Profile       | Add/Delete/Update Build Profiles           | ✅     | ✅       | ⛔        | ⛔      |
| Build Profile       | List Build Profiles                        | ✅     | ✅       | ✅        | ✅      |
| Build Profile       | Build List                                 | ✅     | ✅       | ✅        | ✅      |
| Repository          | Connect/Disconnect Repository              | ✅     | ✅       | ⛔        | ⛔      |
| Configuration       | Add/Delete/Update Build Configuration      | ✅     | ✅       | ⛔        | ⛔      |
| Configuration       | View Build Configuration                   | ✅     | ✅       | ✅        | ✅      |
| Workflow            | Add/Delete/Update Workflows                | ✅     | ✅       | ⛔        | ⛔      |
| Workflow            | View Workflows                             | ✅     | ✅       | ✅        | ✅      |
| Triggers            | Add/Delete/Update Triggers                 | ✅     | ✅       | ⛔        | ⛔      |
| Triggers            | View Triggers                              | ✅     | ✅       | ✅        | ✅      |
| Build Actions       | Start Build                                | ✅     | ✅       | ✅        | ⛔      |
| Build Actions       | Delete Commit Artifacts                    | ✅     | ✅       | ⛔        | ⛔      |
| Build Actions       | Download Artifacts                         | ✅     | ✅       | ✅        | ✅      |
| Build Actions       | Distribution Binary                        | ✅     | ✅       | ✅        | ⛔      |
| Test Results        | List Test Results                          | ✅     | ✅       | ✅        | ✅      |
| Connection          | Add/Delete/Update Connections (User Based) | ✅     | ✅       | ✅        | ✅      |
| Connection          | List Connection (User Based)               | ✅     | ✅       | ✅        | ✅      |
| Runner              | Add/Delete/Update Runner(Root Only)        | ✅     | ⛔       | ⛔        | ⛔      |
| Runner              | List Runner(Root Only)                     | ✅     | ✅       | ✅        | ✅      |
| Runner Access Token | Create/Delete Runner Access Token          | ✅     | ⛔       | ⛔        | ⛔      |
| Runner Access Token | List Runner Access Token                   | ✅     | ⛔       | ⛔        | ⛔      |
| Report              | List Build Reports                         | ✅     | ✅       | ✅        | ✅      |


:::caution Distribution Binary and Runner Details

- **Manager** or **Operator** Build Profile permission can distribute binary if user has **Manager** or **Operator** distribution permission.
- **Manager** or **Operator** Build Profile permission can publish if user has **Manager** or **Operator** Publish Android/iOS permission.
- **Manager**, **Operator** and **Viewer** Build Profile permissions can view self-hosted runners but **cannot** modify the configuration.

:::

### Environment Variables Permissions

The following table details the roles and restrictions for the [**Environment Variables**](/environment-variables). Please refer to the related module information and caution notes. 

| Environment Variable | Scopes                                        | Owner | Manager | Viewer |
|----------------------|-----------------------------------------------|-------|---------|--------|
| Environment Variable | Add/Delete/Update Environment Variable Groups | ✅     | ✅       | ⛔      |
| Environment Variable | Add/Delete/Update Environment Variable        | ✅     | ✅       | ⛔      |
| Environment Variable | List Environment Variable                     | ✅     | ✅       | ✅      |
| Environment Variable | List Environment Variable Groups              | ✅     | ✅       | ✅      |

:::info

**Manager**, **Operator** and **Viewer** Environment Variable permissions can use variable groups in [**Build profile configuration**](/build/build-process-management/build-profile-configuration#environment-variables-configuration).

:::

### Signing and Identity Permissions

The following table details the roles and restrictions for the [**Signing and Identity**](/signing-identities) module. Please refer to the related module information and caution notes. 

| Signing Identity Sub-modules    | Scopes                                 | Owner | Manager | Viewer |
|---------------------------------|----------------------------------------|-------|---------|--------|
| Apple Cerficate                 | Add/Delete/Download Apple Certificates | ✅     | ✅       | ⛔      |
| Apple Cerficate                 | List Apple Certificates                | ✅     | ✅       | ✅      |
| Apple Cerficate Signing Request | Add/Delete/Download CSR                | ✅     | ✅       | ⛔      |
| Apple Cerficate Signing Request | Convert CSR to .p12                    | ✅     | ✅       | ⛔      |
| Apple Cerficate Signing Request | List CSR                               | ✅     | ✅       | ✅      |
| Apple Identifiers               | Add/Delete/Update Apple Identifiers    | ✅     | ✅       | ⛔      |
| Apple Identifiers               | List Apple Identifiers                 | ✅     | ✅       | ✅      |
| Apple Device                    | Add Device Manuel                      | ✅     | ✅       | ⛔      |
| Apple Device                    | Invite User via Email                  | ✅     | ✅       | ⛔      |
| Apple Device                    | Delete Apple Device                    | ✅     | ✅       | ⛔      |
| Apple Device                    | Sync from Apple Developer              | ✅     | ✅       | ⛔      |
| Apple Device                    | Register Devices to Apple Developer    | ✅     | ✅       | ⛔      |
| Apple Device                    | Adding New Device to Provision         | ✅     | ✅       | ⛔      |
| Apple Device                    | List Apple Device                      | ✅     | ✅       | ✅      |
| Apple Profile                   | Add/Delete/Update Apple Profiles       | ✅     | ✅       | ⛔      |
| Apple Profile                   | List Apple Profiles                    | ✅     | ✅       | ✅      |
| Keystore                        | Add/Delete/Update Keystores            | ✅     | ✅       | ⛔      |
| Keystore                        | List Keystores                         | ✅     | ✅       | ✅      |
| Report                          | List Signing Reports                   | ✅     | ✅       | ✅      |

:::info Signing and Identities

**Manager** and **Viewer** Signing Identity permissions can use signing identities in [**Build profile configuration**](/build/build-process-management/build-profile-configuration#environment-variables-configuration).

:::

:::caution Signing Identity Permission

- - **Manager** Signing Identity permission can delete Apple Certificates and Apple Profiles if user has **Manager** Build permission.

:::

### Testing Distribution Permissions

The following table details the roles and restrictions for the [**Testing Distribution**](/testing-distribution) module. Please refer to the related module information and caution notes. 

| Testing Distribution | Scopes                                 | Owner | Manager | Operator | Ext. Operator | Viewer |
|----------------------|----------------------------------------|-------|---------|----------|---------------|--------|
| Distribution Profile | Add/Delete/Update Distribution Profile | ✅     | ✅       | ⛔        | ⛔             | ⛔      |
| Distribution Profile | Setting Update Distribution Profile    | ✅     | ✅       | ⛔        | ⛔             | ⛔      |
| Distribution Profile | List Distribution Profiles             | ✅     | ✅       | ✅        | ✅             | ✅      |
| App Version          | Add/Delete/Update App Version          | ✅     | ✅       | ✅        | ✅             | ⛔      |
| App Version Actions  | Send to Testers                        | ✅     | ✅       | ✅        | ✅             | ⛔      |
| App Version Actions  | Send to Enterprise App Store           | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| App Version Actions  | Send to Publish                        | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| App Version Actions  | Download Binary                        | ✅     | ✅       | ✅        | ✅             | ⛔      |
| Settings             | Select Authentication Type             | ✅     | ⛔       | ⛔        | ⛔             | ⛔      |
| Settings             | View Authentication Settings           | ✅     | ✅       | ✅        | ⛔             | ✅      |
| Report               | List Reports App Version               | ✅     | ✅       | ✅        | ⛔             | ✅      |
| Report               | List Reports App Sharing               | ✅     | ✅       | ✅        | ⛔             | ✅      |

:::caution Authentication Settings

If the selected Authentication type is Static login, Manager role can change **Username** and **Password**. However, it cannot change the content for other Authentication types such as **LDAP** or **SSO**.

:::

:::caution Share with Tester

Users can share the binary with registered Tester Groups only if they have **Viewer** or higher Testing Group permission. However, users can still share the binary with individual testers by adding them manually.

:::

:::caution Sending Binary

- **Manager** or **Operator** Distribution Profile permission can send to Enterprise App Store if user has Manager or Operator Enterprise App Store permission.
- **Manager** or **Operator** Distribution Profile permission can send to Publish if user has Manager or Operator Publish Android and Manager or Operator iOS permission.
- **Manager** or **Operator** Distribution Profile permission can resign binary if user has Manager or Viewer Signing Identity Management permission.

:::

:::caution Resign Binary

User can resign the binary if this user has **Manager** or **Viewer** Signing Identity permission

:::


### Testing Group Permissions

The following table details the roles and restrictions for the [**Testing Groups**](/testing-distribution/testing-groups). Please refer to the related module information and caution notes.  


| Testing Groups | Scopes                                    | Owner | Manager | Viewer |
|----------------|-------------------------------------------|-------|---------|--------|
| Testing Groups | Add/Delete/Update Testing Group           | ✅     | ✅       | ⛔      |
| Testing Groups | Add/Delete/Update Testing Group Testers   | ✅     | ✅       | ⛔      |
| Testing Groups | List Testing Groups                       | ✅     | ✅       | ✅      |
| Testing Groups | List Testing Group Testers                | ✅     | ✅       | ✅      |
| Testing Groups | Update LDAP Group Members Synchronization | ✅     | ✅       | ⛔      |
| Testing Groups | Sync Testing Group From LDAP              | ✅     | ✅       | ⛔      |
| Testing Groups | List LDAP Groups and Members              | ✅     | ✅       | ✅      |


### Publish Module iOS Permissions

The following table details the roles and restrictions for the [**Publish**](/publish-module) module for iOS. Please refer to the related module information and caution notes.

| Publish                  | Scopes                                    | Owner | Manager | Operator | Ext. Operator | Viewer |
|--------------------------|-------------------------------------------|-------|---------|----------|---------------|--------|
| Publish Profiles         | Add/Delete/Update Publish Profile         | ✅     | ✅       | ⛔        | ⛔             | ⛔      |
| Publish Profiles         | List Publish Profiles                     | ✅     | ✅       | ✅        | ✅             | ✅      |
| App Version              | Add/Delete App Version                    | ✅     | ✅       | ✅        | ✅             | ⛔      |
| App Version              | List App Versions                         | ✅     | ✅       | ✅        | ✅             | ✅      |
| Publish Profile Settings | View/Update Profile Settings              | ✅     | ✅       | ⛔        | ⛔             | ⛔      |
| Publish Flows            | Add/Delete/Update Publish Flow Step       | ✅     | ✅       | ⛔        | ⛔             | ⛔      |
| Publish Flows            | Download Publish Flow                     | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| Publish Flows            | Upload Publish Flow                       | ✅     | ✅       | ⛔        | ⛔             | ⛔      |
| Publish Flows            | View Publish Flow                         | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| Publish                  | Start/Restart/Stop Flow                   | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| Publish                  | Start Single Step                         | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| Publish                  | Update Publish Details                    | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| Publish                  | View Publish Details                      | ✅     | ✅       | ✅        | ✅             | ✅      |
| App Store Connect Info   | List/Update App Store Connect Information | ✅     | ✅       | ⛔        | ⛔             | ⛔      |
| Check Release Status     | Get Relese Status                         | ✅     | ✅       | ✅        | ✅             | ✅      |
| Metadata                 | Update Metadata Details                   | ✅     | ✅       | ✅        | ✅             | ⛔      |
| Metadata                 | View Metadata Details                     | ✅     | ✅       | ✅        | ✅             | ✅      |
| Mark as RC               | Marking RC a version                      | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| Resing Binary            | Resigning Binary                          | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| Release Note             | Update Release Note                       | ✅     | ✅       | ✅        | ✅             | ⛔      |
| History                  | View/Download History Logs                | ✅     | ✅       | ✅        | ✅             | ✅      |
| History                  | List History                              | ✅     | ✅       | ✅        | ✅             | ✅      |
| Download Binary          | Download Binary                           | ✅     | ✅       | ✅        | ⛔             | ✅      |
| Cancel Submission        | Cancel Submission                         | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| Reject Binary            | Reject Binary                             | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| Activity Logs            | List Activity Log Details                 | ✅     | ✅       | ✅        | ⛔             | ✅      |

:::caution Resign Binary

User can resign the binary if this user has **Manager** or **Viewer** Signing Identity permission

:::


### Publish Module Android Permissions

The following table details the roles and restrictions for the [**Publish**](/publish-module) module for Android. Please refer to the related modules information and caution notes.

| Publish                         | Scopes                                      | Owner | Manager | Operator | Ext. Operator | Viewer |
|---------------------------------|---------------------------------------------|-------|---------|----------|---------------|--------|
| Publish Profiles                | Add/Delete/Update Publish Profile           | ✅     | ✅       | ⛔        | ⛔             | ⛔      |
| Publish Profiles                | List Publish Profiles                       | ✅     | ✅       | ✅        | ✅             | ✅      |
| App Version                     | Add/Delete App Version                      | ✅     | ✅       | ✅        | ✅             | ⛔      |
| App Version                     | List App Versions                           | ✅     | ✅       | ✅        | ✅             | ✅      |
| Publish Profile Settings        | View/Update Profile Settings                | ✅     | ✅       | ⛔        | ⛔             | ⛔      |
| Publish Flows                   | Add/Delete/Update Publish Flow Step         | ✅     | ✅       | ⛔        | ⛔             | ⛔      |
| Publish Flows                   | Download Publish Flow                       | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| Publish Flows                   | Upload Publish Flow                         | ✅     | ✅       | ⛔        | ⛔             | ⛔      |
| Publish Flows                   | View Publish Flow                           | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| Publish                         | Start/Restart/Stop Flow                     | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| Publish                         | Start Single Step                           | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| Publish                         | Update Publish Details                      | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| Publish                         | View Publish Details                        | ✅     | ✅       | ✅        | ✅             | ✅      |
| Google Play Console Information | List/Update Google Play Console Information | ✅     | ✅       | ⛔        | ⛔             | ⛔      |
| Metadata                        | Update Metadata Details                     | ✅     | ✅       | ✅        | ✅             | ⛔      |
| Metadata                        | View Metadata Details                       | ✅     | ✅       | ✅        | ✅             | ✅      |
| Mark as RC                      | Marking RC a version                        | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| Resing Binary                   | Resigning Binary                            | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| Release Note                    | Update Release Note                         | ✅     | ✅       | ✅        | ✅             | ⛔      |
| History                         | View/Download History Logs                  | ✅     | ✅       | ✅        | ✅             | ✅      |
| History                         | List History                                | ✅     | ✅       | ✅        | ✅             | ✅      |
| Download Binary                 | Download Binary                             | ✅     | ✅       | ✅        | ⛔             | ✅      |
| Reject Binary                   | Reject Binary                               | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| Activity Logs                   | List Activity Log Details                   | ✅     | ✅       | ✅        | ⛔             | ✅      |


### Publish Environment Variables

The following table details the roles and restrictions for the [**Publish Variables**](/publish-module/publish-variables) module for Android. Please refer to the related modules information and caution notes.

| Publish              | Scopes                                        | Owner | Manager | Viewer |
|----------------------|-----------------------------------------------|-------|---------|--------|
| Environment Variable | Add/Delete/Update Environment Variable Groups | ✅     | ✅       | ⛔      |
| Environment Variable | Add/Delete/Update Environment Variable        | ✅     | ✅       | ⛔      |
| Environment Variable | List Environment Variable                     | ✅     | ✅       | ✅      |
| Environment Variable | List Environment Variable Groups              | ✅     | ✅       | ✅      |

:::info

Google Play and Huawei AppGallery permissions are managed through a single rule. When this rule is used, it will apply to both platforms.

:::

### Enterprise App Store Permissions

Manage and Upload Apps to Enterprise App Store.

| Ent. App Sub Modules | Scopes                                 | Owner | Manager | Operator | Ext. Operator | Viewer |
|----------------------|----------------------------------------|-------|---------|----------|---------------|--------|
| Store Profile        | Add/Delete/Update Profiles             | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| Store Profile        | List Profiles                          | ✅     | ✅       | ✅        | ✅             | ✅      |
| App Version          | Add/Delete/Update App Versions         | ✅     | ✅       | ✅        | ✅             | ⛔      |
| App Version          | Download App Versions                  | ✅     | ✅       | ✅        | ✅             | ⛔      |
| App Version          | List App Versions                      | ✅     | ✅       | ✅        | ✅             | ✅      |
| App Version Actions  | Publish App Version Live/Beta Channels | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| App Version Actions  | Notify Users                           | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| App Version Actions  | Create/Delete In-app Update            | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| App Version Actions  | Get In-app Update                      | ✅     | ✅       | ✅        | ✅             | ✅      |
| Settings             | Update Store Domain                    | ✅     | ⛔       | ⛔        | ⛔             | ⛔      |
| Settings             | Update Store Customization             | ✅     | ⛔       | ⛔        | ⛔             | ⛔      |
| Settings             | Select Authentication Type             | ✅     | ⛔       | ⛔        | ⛔             | ⛔      |
| Settings             | View Authentication Settings           | ✅     | ✅       | ✅        | ⛔             | ✅      |
| Settings             | View Customization Settings            | ✅     | ✅       | ✅        | ⛔             | ✅      |
| Settings             | View Store Domain                      | ✅     | ✅       | ✅        | ⛔             | ✅      |
| Report               | List Reports                           | ✅     | ✅       | ✅        | ⛔             | ✅      |

:::caution Authentication Settings

If the selected Authentication type is Static login, Manager role can change **Username** and **Password**. However, it cannot change the content for other Authentication types.

:::


### Organization Management Permissions

The user can create an organization or sub-organization within license limits, add and remove members, and manage their permissions.

Also, the user can view self-hosted runners and change configuration.

| Organization Management Sub-modules                  | Scopes                                  | Owner | Manager | Viewer |
| ---------------------------------------------------- | --------------------------------------- | ----- | ------- | ------ |
| Organization and Team Management                     | Create/Delete/Update Organization       | ✅     | ✅       | ⛔      |
| Organization and Team Management                     | Create/Delete/Update Sub-Organization   | ✅     | ✅       | ⛔      |
| Organization and Team Management                     | Add/Delete/Update User                  | ✅     | ✅       | ⛔      |
| Organization and Team Management                     | Assign Role for User                    | ✅     | ✅       | ⛔      |
| Organization and Team Management                     | List User                               | ✅     | ✅       | ✅      |
| Testing Portal and Enterprise Portal Authentications | Add/Delete/Update LDAP/SSO Integrations | ✅     | ✅       | ⛔      |
| Testing Portal and Enterprise Portal Authentications | View LDAP/SSO Integrations              | ✅     | ✅       | ✅      |
| Appcircle Login                                      | Create/Delete/Update SSO                | ✅     | ✅       | ⛔      |
| Appcircle Login                                      | List SSO                                | ✅     | ✅       | ✅      |
| Appcircle Login                                      | Add/Delete/Update LDAP                  | ✅     | ✅       | ⛔      |
| Appcircle Login                                      | List LDAP                               | ✅     | ✅       | ✅      |
| PAT                                                  | Generate PAT                            | ✅     | ✅       | ⛔      |
| PAT                                                  | View PAT                                | ✅     | ✅       | ✅      |
| Runner Access Token                                  | List Runner Access Token                | ✅     | ⛔       | ⛔      |
| Runner Access Token                                  | Create/Delete Runner Access Token       | ✅     | ⛔       | ⛔      |
| Report                                               | View Organziation Report                | ✅     | ✅       | ✅      |
| Artifacts                                            | View Retention Period                   | ✅     | ✅       | ✅      |
| Artifacts                                            | Update Retention Period                 | ✅     | ✅       | ⛔      |

:::info Organization Management

Whatever role a user is assigned in the root organization, they will have the same role in the **sub-organizations**. For example, someone who is a Manager in the root organization is automatically assigned as a Manager in the sub-organizations.  

If you want to assign a role in a sub-organization, please do so within the respective **sub-organization**.

:::

:::caution Appcircle Login and LDAP/SSO Integrations

LDAP/SSO integrations under Integration are only for setting authentication for logins to the Testing Distribution [**Testing Portal**](/testing-distribution/testing-portal) and [**Enterprise App Store**](/enterprise-app-store).

Please use [**Appcircle Login**](/account/my-organization/security/authentications) for **LDAP** and **SSO** integration when logging into Appcircle.

:::

:::caution Organization Management Role Assignment

The Manager role **cannot** assign itself and another user as **Owner** when assigning roles.

:::

### Billing Management Permissions

Manage the subscription, payment details, and invoices.

The following table details the roles and restrictions for the **Billing** details. Please refer to the related module information and caution notes.

| Billing Sub-modules | Scopes                    | Owner | Manager |
|---------------------|---------------------------|-------|---------|
| Subscription        | List Subscription Details | ✅     | ✅       |


### Integrations and Connection Managements

Connect or disconnect from third-party service providers such as notification tools or store connections.

#### Notification Tools

- [**Slack**](/account/my-organization/notifications/slack/slack-notifications) 
- [**Microsoft Teams**](/account/my-organization/notifications/teams-notifications)
- [**Email Notifications**](/account/my-organization/notifications/email-connection) 
 
#### Store Connections

- [**App Store Connect API Keys**](/account/my-organization/security/credentials/adding-an-app-store-connect-api-key) 
- [**Google Play Developer API Keys**](/account/my-organization/security/credentials/adding-google-play-service-account) 
- [**Huawei AppGallery Developer API Keys**](/account/my-organization/security/credentials/adding-huawei-api-key)
- [**Microsoft Intune API Keys**](/account/my-organization/security/credentials/adding-microsoft-intune-api-key) 

| Integrations and Connections | Scopes                        | Owner | Manager | Viewer |
|------------------------------|-------------------------------|-------|---------|--------|
| Credentials                  | Add/Delete/Update Credentials | ✅     | ✅       | ⛔      |
| Credentials                  | View Credentials              | ✅     | ✅       | ✅      |
| Notifications                | Update Notifications          | ✅     | ✅       | ⛔      |
| Notifications                | View Notifications            | ✅     | ✅       | ✅      |
