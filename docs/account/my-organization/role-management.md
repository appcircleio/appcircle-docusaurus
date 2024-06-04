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

### Build Profile Permissions

Permissions can be customized for build profiles.

| Permission | Explanation                                                                                            |
| ---------- | ------------------------------------------------------------------------------------------------------ |
| Manager    | The user can view and download logs, change configuration, workflows, and triggers and start building. |
| Operator   | The user can only start the build, view logs, and download logs.                                       |
| Viewer     | The user can only view and download logs.                                                              |
| None       | The user cannot reach any details about build profiles.                                                |

:::info

Manager or Operator Build Profile permission can distribute binary if user has Manager or Operator Distribution permission.

:::

:::info

Manager or Operator Build Profile permission can publish if user has Manager or Operator Publish Android/iOS permission.

:::

:::info

Manager, Operator and Viewer Build Profile permissions can view self-hosted runners but cannot modify the configuration.

:::

:::caution

Only Manager permission can view the configurations, workflows, and triggers.

:::

### Environment Variable Permissions

Permissions can be customized for environment variables.

| Permission | Explanation                                                                                                                     |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Manager    | The user can see variable groups, including their details, add new variables, and delete existing variable groups or variables. |
| Viewer     | The user can only see variable groups and their details.                                                                        |
| None       | The user cannot reach any details about environment variables.                                                                  |

:::info

Manager, Operator and Viewer Environment Variable permissions can use variable groups in build profile configuration.

:::

### Signing Identity Management Permissions

Permissions can be customized for signing identity management.

| Permission | Explanation                                                                                                |
| ---------- | ---------------------------------------------------------------------------------------------------------- |
| Manager    | The user can see, delete, and add new certificates, provisioning profiles, keystores, and signing history. |
| Viewer     | The user can only see certificates, provisioning profiles, keystores, and signing history.                 |
| None       | The user cannot reach any details about signing identity.                                                  |

:::info

Manager, Operator and Viewer Signing Identity Management permissions can use signing identities in build profile configuration.

:::

### Distribution Profile Permissions

Permissions can be customized for distribution profiles.

| Permission | Explanation                                                                                                                             |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Manager    | The user can see, create, and delete new distribution profiles and Apple Devices and customize their settings.                          |
| Operator   | The user can only send to testing groups and view distribution profiles and Apple Devices, App Versions Report, and App Sharing Report. |
| Viewer     | The user can only view distribution profiles and Apple Devices, App Versions Report, and App Sharing Report.                            |
| None       | The user cannot reach any details about distribution profiles, Apple Devices, App Versions Report, and App Sharing Report.              |

:::info

Manager or Operator Distribution Profile permission can send to enterprise app store if user has Manager, Uploader or Operator Enterprise App Store permission.

:::

:::info

Manager or Operator Distribution Profile permission can send to publish if user has Manager or Operator Publish Android and Manager or Operator iOS permission.

:::

:::info

Manager or Operator Distribution Profile permission can resign binary if user has Manager or Viewer Signing Identity Management permission.

:::

### Testing Group Permissions

Permissions can be customized for testing groups.

| Permission | Explanation                                                                                                   |
| ---------- | ------------------------------------------------------------------------------------------------------------- |
| Manager    | The user can see, create, and delete testing groups, and also add or delete new test users from these groups. |
| Viewer     | The user can only view testing groups and test users.                                                         |
| None       | The user cannot reach any details about the testing group.                                                    |

### Store Submit Module Permissions

Upload apps to Google Play, Huawei, and App Store.

| Permission      | Explanation                                                                                |
| --------------- | ------------------------------------------------------------------------------------------ |
| Manager Android | The user can upload apps to Google Play and Huawei AppGallery.                             |
| Manager iOS     | The user can upload apps only to the App Store.                                            |
| Viewer          | The user can only view applications and their details belonging to their own organization. |

:::info

Google Play and Huawei AppGallery permissions are managed through a single rule. When this rule is used, it will apply to both platforms.

:::

:::info

If the user does not have any of these permissions, they will not have access to any details related to the store submit module.

:::

### Publish Module iOS Permissions

Publish apps to App Store.

| Permission | Explanation                                                                                                                                                   |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Manager    | The user can make changes to the publish flow, publish settings, start publish to the App Store, add or delete a new app version, and view and download logs. |
| Operator   | The user can start publishing to the App Store and download artifacts and view publish settings, publish flow, and logs.                                      |
| Viewer     | The user can only download artifacts and view the iOS application list and logs for the application.                                                          |
| None       | The user cannot reach any details about the iOS Publish.                                                                                                      |

### Publish Module Android Permissions

Publish apps to Google Play, Huawei.

| Permission | Explanation                                                                                                                                                                           |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Manager    | The user can make changes to the publish flow, publish settings, start publish to the Google Play And Huawei AppGallery, add or delete a new app version, and view and download logs. |
| Operator   | The user can start publishing to the Google Play and Huawei AppGallery and download artifacts and view publish settings, publish flow, and logs.                                      |
| Viewer     | The user can only download artifacts and view the Android application list and logs for the application.                                                                              |
| None       | The user cannot reach any details about the Android Publish.                                                                                                                          |

:::info

Google Play and Huawei AppGallery permissions are managed through a single rule. When this rule is used, it will apply to both platforms.

:::

:::tip

**Publish Variables** permissions in the Publish module are dependent on the iOS or Android permissions that you configure for the Publish module.

For instance, when you give "viewer" permission to a user for iOS or Android, this permission will also make the user "viewer" for the **Publish Variables**. When you give "manager" permission to a user for iOS or Android, this permission also makes the user "manager" for the **Publish Variables**.

:::

### Enterprise App Store Permissions

Manage and Upload Apps to Enterprise App Store.

| Permission | Explanation                                                                                                                                                                                                     |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Manager    | The user can do anything Uploader can do and modify Enterprise Settings including create/update/delete store authentication (LDAP, SSO and Static Login), customize the store and modify store domain settings. |
| Uploader   | The user can only create/update/delete enterprise app store profiles, create/update/delete app versions, publish/notify to beta/live stores, download artifacts and view the profiles.                          |
| Operator   | The user can only publish/notify to beta/live stores, download artifacts and view the profiles.                                                                                                                 |
| Viewer     | The user can only view the profiles.                                                                                                                                                                            |
| None       | The user cannot reach any details about the Enterprise App Store.                                                                                                                                               |

### Organization Management Permissions

The user can create an organization or sub-organization within license limits, add and remove members, and manage their permissions.

Also, the user can view self-hosted runners and change configuration.

| Permission | Explanation                                                                                                         |
| ---------- | ------------------------------------------------------------------------------------------------------------------- |
| Manager    | The user can manage all member permissions and other organization properties mentioned above within license limits. |

### Billing Management Permissions

Manage the subscription, payment details, and invoices.

| Permission | Explanation                                                       |
| ---------- | ----------------------------------------------------------------- |
| Manager    | The user can manage subscriptions, payment details, and invoices. |

### Third-Party Connection Management Permissions

Connect to or disconnect from third-party service providers such as Slack, Microsoft Teams, Google Play Developer API Keys, App Store Connect API Keys, Huawei AppGallery Developer API Keys, etc.

| Permission | Explanation                                                                      |
| ---------- | -------------------------------------------------------------------------------- |
| Manager    | The user can manage third-party service provider connections and disconnections. |

:::caution

The permissions of the Store Submit module affect the visibility of online stores connections.

:::
