---
title: Role Management
description: Overview of role management and permissions in Appcircle
tags:
  [
    permissions,
    role-management,
    build-profiles,
    environment-variables,
    signing-identity,
    distribution-profiles,
    testing-groups,
    store-submit,
    publish,
    enterprise-app-store,
    organization-management,
    billing-management,
    third-party-connections,
  ]
---

# Role Management

With Appcircle's [**Advanced Role Management**](/account/my-organization#advanced-role-management) structure, you can detail the roles of the members you add to your organisation separately for each module and restrict the authority of the members. Appcircle offers different role types for each module. A short description of each role is given in the table below. In addition, you can find detailed role management information for each module under module titles.

- **Owner**: The user is authorised unlimited access to all modules.
- **Manager**: The user becomes the administrator of the relevant module and no restrictions are made.
- **Operator**: The user is the person who manages the operations of the relevant module and certain restrictions apply.
- **Ext. Operator**: The user has very limited authorisation in the relevant module. It is usually for third party employees from outside the company.
- **Viewer**: User only has view authorisation in the relevant module, cannot take any action.

:::caution Role Types

Some role types are not used in some modules because they are not required in that module. For this reason, roles may vary for each module.

:::

### Build Permissions

The following table details the roles and restrictions for the [**Build**](/build) module. Please refer to the modules related information and coution notes. 

| Build Sub-modules   | Scopes                                | Owner | Manager | Operator | Viewer |
|---------------------|---------------------------------------|-------|---------|----------|--------|
| Build Profile       | Add/Delete/Update Build Profiles      | ✅     | ✅       | ⛔        | ⛔      |
| Build Profile       | List Build Profiles                   | ✅     | ✅       | ✅        | ✅      |
| Repository          | Connect/Disconnect Repository         | ✅     | ✅       | ⛔        | ⛔      |
| Commit              | List Commit                           | ✅     | ✅       | ✅        | ✅      |
| Configuration       | Add/Delete/Update Build Configuration | ✅     | ✅       | ⛔        | ⛔      |
| Configuration       | View Build Configuration              | ✅     | ✅       | ✅        | ✅      |
| Workflow            | Add/Delete/Update Workflows           | ✅     | ✅       | ⛔        | ⛔      |
| Workflow            | View Workflows                        | ✅     | ✅       | ✅        | ✅      |
| Build Actions       | Start Build                           | ✅     | ✅       | ✅        | ⛔      |
| Build Actions       | Delete Commit Artifacts               | ✅     | ✅       | ⛔        | ⛔      |
| Build Actions       | Download Artifacts                    | ✅     | ✅       | ✅        | ✅      |
| Build Actions       | Distribution Binary                   | ✅     | ✅       | ✅        | ⛔      |
| Test Results        | List Test Results                     | ✅     | ✅       | ✅        | ✅      |
| Connection          | Add/Delete/Update Connections         | ✅     | ✅       | ⛔        | ⛔      |
| Connection          | List Connection                       | ✅     | ✅       | ✅        | ✅      |
| Runner              | Add/Delete/Update Runner(Root Only)   | ✅     | ⛔       | ⛔        | ⛔      |
| Runner              | List Runner(Root Only)                | ✅     | ✅       | ✅        | ✅      |
| Runner Access Token | Create/Delete Runner Access Token     | ✅     | ⛔       | ⛔        | ⛔      |
| Runner Access Token | List Runner Access Token              | ✅     | ⛔       | ⛔        | ⛔      |
| Report              | List Build Reports                    | ✅     | ✅       | ✅        | ✅      |


:::caution Distrubition Binary and Runner Details

- **Manager** or **Operator** Build Profile permission can distribute binary if user has Manager or Operator Distribution permission.
- **Manager** or **Operator** Build Profile permission can publish if user has Manager or Operator Publish Android/iOS permission.
- **Manager**, **Operator** and **Viewer** Build Profile permissions can view self-hosted runners but cannot modify the configuration.

:::

### Environment Variables Permissions

The following table details the roles and restrictions for the [**Environment Variables**](/environment-variables). Please refer to the modules related information and coution notes. 

| Environment Variable | Scopes                                        | Owner | Manager | Viewer |
|----------------------|-----------------------------------------------|-------|---------|--------|
| Environment Variable | Add/Delete/Update Environment Variable Groups | ✅     | ✅       | ⛔      |
| Environment Variable | Add/Delete/Update Environment Variable        | ✅     | ✅       | ⛔      |
| Environment Variable | List Environment Variable                     | ✅     | ✅       | ✅      |
| Environment Variable | List Environment Variable Groups              | ✅     | ✅       | ✅      |

:::info

Manager, Operator and Viewer Environment Variable permissions can use variable groups in build profile configuration.

:::

### Signing and Identity Permissions

The following table details the roles and restrictions for the [**Signing and Identity**](/signing-identities) module. Please refer to the modules related information and coution notes. 

| Signing Identity Sub-modules    | Scopes                               | Owner | Manager | Viewer |
|---------------------------------|--------------------------------------|-------|---------|--------|
| Apple Cerficate                 | Add/Delete/Update Apple Certificates | ✅     | ✅       | ⛔      |
| Apple Cerficate                 | List Apple Certificates              | ✅     | ✅       | ✅      |
| Apple Cerficate Signing Request | Add/Delete CSR                       | ✅     | ✅       | ⛔      |
| Apple Cerficate Signing Request | Convert CSR to .p12                  | ✅     | ✅       | ⛔      |
| Apple Cerficate Signing Request | List CSR                             | ✅     | ✅       | ✅      |
| Apple Identifiers               | Add/Delete/Update Apple Identifiers  | ✅     | ✅       | ⛔      |
| Apple Identifiers               | List Apple Identifiers               | ✅     | ✅       | ✅      |
| Apple Profile                   | Add/Delete/Update Apple Profiles     | ✅     | ✅       | ⛔      |
| Apple Profile                   | List Apple Profiles                  | ✅     | ✅       | ✅      |
| Keystore                        | Add/Delete/Update Keystores          | ✅     | ✅       | ⛔      |
| Keystore                        | List Keystores                       | ✅     | ✅       | ✅      |
| Report                          | List Signing Reports                 | ✅     | ✅       | ✅      |

:::info

Manager, Operator and Viewer Signing Identity Management permissions can use signing identities in build profile configuration.

:::

### Testing Distribution Permissions

The following table details the roles and restrictions for the [**Testing Distribution**](/distribute) module. Please refer to the modules related information and coution notes. 

| Testing Distribution | Scopes                                 | Owner | Manager | Operator | Ext. Operator | Viewer |
|----------------------|----------------------------------------|-------|---------|----------|---------------|--------|
| Distribution Profile | Add/Delete/Update Distribution Profile | ✅     | ✅       | ⛔        | ⛔             | ⛔      |
| Distribution Profile | Setting Update Distribution Profile    | ✅     | ✅       | ⛔        | ⛔             | ⛔      |
| Distribution Profile | List Distribution Profiles             | ✅     | ✅       | ✅        | ✅             | ✅      |
| App Version          | Add/Delete/Update App Version          | ✅     | ✅       | ✅        | ✅             | ⛔      |
| App Version Actions  | Send to Testers                        | ✅     | ✅       | ✅        | ✅             | ⛔      |
| App Version Actions  | Send to Enterprise App Store           | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| App Version Actions  | Send to Publish                        | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| Settings             | Select Authentication Type             | ✅     | ⛔       | ⛔        | ⛔             | ⛔      |
| Settings             | View Authentication Settings           | ✅     | ✅       | ✅        | ⛔             | ✅      |
| Apple Device         | Add/Delete Apple Device                | ✅     | ✅       | ⛔        | ⛔             | ⛔      |
| Apple Device         | Register Apple Device                  | ✅     | ✅       | ⛔        | ⛔             | ⛔      |
| Apple Device         | Adding New Device to Provision         | ✅     | ✅       | ⛔        | ⛔             | ⛔      |
| Apple Device         | Sync from Apple Developer              | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| Apple Device         | List Apple Device                      | ✅     | ✅       | ✅        | ⛔             | ✅      |
| Report               | List Reports App Version               | ✅     | ✅       | ✅        | ⛔             | ✅      |
| Report               | List Reports App Sharing               | ✅     | ✅       | ✅        | ⛔             | ✅      |

:::caution Authentication Settings

If the selected Authentication type is Static login, Manager role can change **Username** and **Password**. However, it cannot change the content for other Authentication types.

:::

:::caution Sending Binary

- **Manager** or **Operator** Distribution Profile permission can send to enterprise app store if user has Manager, Operator or Ext. Operator Enterprise App Store permission.
- **Manager** or **Operator** Distribution Profile permission can send to publish if user has Manager or Operator Publish Android and Manager or Operator iOS permission.
- **Manager** or **Operator** Distribution Profile permission can resign binary if user has Manager or Viewer Signing Identity Management permission.

:::


### Testing Group Permissions

The following table details the roles and restrictions for the [**Testing Groups**](/distribute/testing-management/testing-groups). Please refer to the modules related information and coution notes. 


| Testing Groups | Scopes                                  | Owner | Manager | Viewer |
|----------------|-----------------------------------------|-------|---------|--------|
| Testing Groups | Add/Delete/Update Testing Group         | ✅     | ✅       | ⛔      |
| Testing Groups | Add/Delete/Update Testing Group Testers | ✅     | ✅       | ⛔      |
| Testing Groups | List Testing Groups                     | ✅     | ✅       | ✅      |
| Testing Groups | List Testing Group Testers              | ✅     | ✅       | ✅      |


### Publish Module iOS Permissions

The following table details the roles and restrictions for the [**Publish**](/publish-module) module for iOS. Please refer to the modules related information and coution notes.

| Publish                   | Scopes                                    | Owner | Manager | Operator | Ext. Operator | Viewer |
|---------------------------|-------------------------------------------|-------|---------|----------|---------------|--------|
| Publish Profiles          | Add/Delete/Update Publish Profile         | ✅     | ✅       | ⛔        | ⛔             | ⛔      |
| Publish Profiles          | List Publish Profiles                     | ✅     | ✅       | ✅        | ✅             | ✅      |
| App Version               | Add/Delete App Version                    | ✅     | ✅       | ✅        | ✅             | ⛔      |
| App Version               | List App Versions                         | ✅     | ✅       | ✅        | ✅             | ✅      |
| Publish Profile Settings  | View/Update Profile Settings              | ✅     | ✅       | ⛔        | ⛔             | ⛔      |
| Manage Publish Flow Steps | Download/Upload Publish Flow              | ✅     | ✅       | ⛔        | ⛔             | ⛔      |
| Manage Publish Flow Steps | Add/Delete Publish Flow Step              | ✅     | ✅       | ⛔        | ⛔             | ⛔      |
| Manage Publish Flow Steps | List Publish Flow                         | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| Manage Publish Flow Steps | Update Publish Flow Step Details          | ✅     | ✅       | ⛔        | ⛔             | ⛔      |
| Publish Process           | Start/Restart/Stop Flow                   | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| Publish Process           | Start Single Step                         | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| Publish Process           | Update Custom UI details                  | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| Publish Process           | View Custom UI Details                    | ✅     | ✅       | ✅        | ⛔             | ✅      |
| Publish Process           | List Publish Flow Details                 | ✅     | ✅       | ✅        | ⛔             | ✅      |
| App Store Connect Info    | List/Update App Store Connect Information | ✅     | ✅       | ⛔        | ⛔             | ⛔      |
| Check Release Status      | Get Relese Status                         | ✅     | ✅       | ✅        | ✅             | ✅      |
| Metadata                  | Update Metadata Details                   | ✅     | ✅       | ✅        | ✅             | ⛔      |
| Metadata                  | View Metadata Details                     | ✅     | ✅       | ✅        | ✅             | ✅      |
| Mark as RC                | Marking RC a version                      | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| Resing Binary             | Resigning Binary                          | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| Release Note              | Update Release Note                       | ✅     | ✅       | ✅        | ✅             | ⛔      |
| History                   | Download History Logs                     | ✅     | ✅       | ✅        | ⛔             | ✅      |
| History                   | List History                              | ✅     | ✅       | ✅        | ✅             | ✅      |
| Download Binary           | Download Binary                           | ✅     | ✅       | ✅        | ⛔             | ✅      |
| Environment Variables     | Add/Delete/Update Env Variables           | ✅     | ✅       | ⛔        | ⛔             | ⛔      |
| Environment Variables     | List Environment Variables                | ✅     | ✅       | ✅        | ⛔             | ✅      |
| Activity Logs             | List Activity Log Details                 | ✅     | ✅       | ✅        | ⛔             | ✅      |


### Publish Module Android Permissions

The following table details the roles and restrictions for the [**Publish**](/publish-module) module for Android. Please refer to the modules related information and coution notes.

| Publish                   | Scopes                                    | Owner | Manager | Operator | Ext. Operator | Viewer |
|---------------------------|-------------------------------------------|-------|---------|----------|---------------|--------|
| Publish Profiles          | Add/Delete/Update Publish Profile         | ✅     | ✅       | ⛔        | ⛔             | ⛔      |
| Publish Profiles          | List Publish Profiles                     | ✅     | ✅       | ✅        | ✅             | ✅      |
| App Version               | Add/Delete App Version                    | ✅     | ✅       | ✅        | ✅             | ⛔      |
| App Version               | List App Versions                         | ✅     | ✅       | ✅        | ✅             | ✅      |
| Publish Profile Settings  | View/Update Profile Settings              | ✅     | ✅       | ⛔        | ⛔             | ⛔      |
| Manage Publish Flow Steps | Download/Upload Publish Flow              | ✅     | ✅       | ⛔        | ⛔             | ⛔      |
| Manage Publish Flow Steps | Add/Delete Publish Flow Step              | ✅     | ✅       | ⛔        | ⛔             | ⛔      |
| Manage Publish Flow Steps | List Publish Flow                         | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| Manage Publish Flow Steps | Update Publish Flow Step Details          | ✅     | ✅       | ⛔        | ⛔             | ⛔      |
| Publish Process           | Start/Restart/Stop Flow                   | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| Publish Process           | Start Single Step                         | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| Publish Process           | Update Custom UI details                  | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| Publish Process           | View Custom UI Details                    | ✅     | ✅       | ✅        | ⛔             | ✅      |
| Publish Process           | List Publish Flow Details                 | ✅     | ✅       | ✅        | ⛔             | ✅      |
| App Store Connect Info    | List/Update App Store Connect Information | ✅     | ✅       | ⛔        | ⛔             | ⛔      |
| Check Release Status      | Get Relese Status                         | ✅     | ✅       | ✅        | ✅             | ✅      |
| Metadata                  | Update Metadata Details                   | ✅     | ✅       | ✅        | ✅             | ⛔      |
| Metadata                  | View Metadata Details                     | ✅     | ✅       | ✅        | ✅             | ✅      |
| Mark as RC                | Marking RC a version                      | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| Resing Binary             | Resigning Binary                          | ✅     | ✅       | ✅        | ⛔             | ⛔      |
| Release Note              | Update Release Note                       | ✅     | ✅       | ✅        | ✅             | ⛔      |
| History                   | View/Download History Logs                | ✅     | ✅       | ✅        | ⛔             | ✅      |
| History                   | List History                              | ✅     | ✅       | ✅        | ✅             | ✅      |
| Download Binary           | Download Binary                           | ✅     | ✅       | ✅        | ⛔             | ✅      |
| Environment Variables     | Add/Delete/Update Env Variables           | ✅     | ✅       | ⛔        | ⛔             | ⛔      |
| Environment Variables     | List Environment Variables                | ✅     | ✅       | ✅        | ⛔             | ✅      |
| Activity Logs             | List Activty Log Details                  | ✅     | ✅       | ✅        | ⛔             | ✅      |

:::info

Google Play and Huawei AppGallery permissions are managed through a single rule. When this rule is used, it will apply to both platforms.

:::

:::tip

**Publish Variables** permissions in the Publish module are dependent on the iOS or Android permissions that you configure for the Publish module.

For instance, when you give "**Viewer**" permission to a user for iOS or Android, this permission will also make the user "**Viewer**" for the **Publish Variables**. When you give "**Manager**" permission to a user for iOS or Android, this permission also makes the user "**Manager**" for the **Publish Variables**.

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
| Settings             | Update Store Domain                    | ✅     | ⛔       | ⛔        | ⛔             | ⛔      |
| Settings             | Update Store Customization             | ✅     | ⛔       | ⛔        | ⛔             | ⛔      |
| Settings             | Select Authentication Type             | ✅     | ⛔       | ⛔        | ⛔             | ⛔      |
| Settings             | View Authentication Settings           | ✅     | ✅       | ✅        | ⛔             | ✅      |
| Settings             | View Customization Settings            | ✅     | ✅       | ✅        | ⛔             | ✅      |
| Settings             | View Store Domain                      | ✅     | ✅       | ✅        | ⛔             | ✅      |
| Report               | List Reports                           | ✅     | ✅       | ⛔        | ⛔             | ⛔      |

:::caution Authentication Settings

If the selected Authentication type is Static login, Manager role can change **Username** and **Password**. However, it cannot change the content for other Authentication types.

:::


### Organization Management Permissions

The user can create an organization or sub-organization within license limits, add and remove members, and manage their permissions.

Also, the user can view self-hosted runners and change configuration.

| Organization Management Sub-modules | Scopes                                | Owner | Manager |
|-------------------------------------|---------------------------------------|-------|---------|
| Organization and Team Management    | Create/Delete/Update Organization     | ✅     | ⛔       |
| Organization and Team Management    | Create/Delete/Update Sub-Organization | ✅     | ⛔       |
| Organization and Team Management    | Add/Delete/Update User                | ✅     | ✅       |
| Organization and Team Management    | Assign Role for User                  | ✅     | ✅       |
| Organization and Team Management    | List User                             | ✅     | ✅       |
| SSO                                 | Create/Delete/Update SSO              | ✅     | ⛔       |
| SSO                                 | List SSO                              | ✅     | ✅       |
| LDAP                                | Add/Delete/Update LDAP                | ✅     | ⛔       |
| LDAP                                | List LDAP                             | ✅     | ✅       |
| PAT                                 | Generate PAT                          | ✅     | ✅       |
| PAT                                 | View PAT                              | ✅     | ✅       |
| Runner Access Token                 | List Runner Access Token              | ✅     | ⛔       |
| Runner Access Token                 | Create/Delete Runner Access Token     | ✅     | ⛔       |
| Report                              | View Organziation Report              | ✅     | ✅       |

:::info Organization Management

Whatever role a user is assigned in the root organisation, user has the same role in the sub-organisations. For example, someone who is a Manager in the root organisation is automatically assigned as Manager in the sub-organisations. 

If you want to assign a role in a sub-organisation, please do so within the respective sub-organisation.

:::

:::caution Organization Management Role Assignment

The Manager role **cannot** assign itself and another user as **Owner** when assigning the role.

:::

### Billing Management Permissions

Manage the subscription, payment details, and invoices.

The following table details the roles and restrictions for the **Billing** details. Please refer to the modules related information and coution notes.

| Billing Sub-modules | Scopes                    | Owner | Manager |
|---------------------|---------------------------|-------|---------|
| Subscription        | List Subscription Details | ✅     | ✅       |


### Connection Managements

Connect or disconnect from third-party service providers such as notification tools or store connections

#### Notification Tools

- [**Slack**](/account/my-organization/notifications-and-communication/slack/slack-notifications) 
- [**Microsoft Teams**](/account/my-organization/notifications-and-communication/teams-notifications)
- [**Email Notifications**](/account/my-organization/notifications-and-communication/email-connection) 
 
#### Store Connections

- [**App Store Connect API Keys**](/account/my-organization/api-integrations/adding-an-app-store-connect-api-key) 
- [**Google Play Developer API Keys**](/account/my-organization/api-integrations/adding-google-play-service-account) 
- [**Huawei AppGallery Developer API Keys**](/account/my-organization/api-integrations/adding-huawei-api-key)
- [**Microsoft Intune API Keys**](/account/my-organization/api-integrations/adding-microsoft-intune-api-key) 

| Connections Management | Scopes                        | Owner | Manager |
|------------------------|-------------------------------|-------|---------|
| Connections            | Add/Delete/Update Connections | ✅     | ⛔       |
| Connections            | View Connections              | ✅     | ✅       |
| Notifications          | Update Notifications          | ✅     | ✅       |
| Notifications          | View Notifications            | ✅     | ✅       |
