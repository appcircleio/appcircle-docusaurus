---
title: My Organization and Team Management
metaTitle: My Organization and Team Management
metaDescription: My Organization and Team Management
sidebar_position: 4
---

import Screenshot from '@site/src/components/Screenshot';

# My Organization and Team Management

Organizations in Appcircle are separate units with separate "workspaces" that allow collaboration on the same apps with a team.

Each user is the owner of their individual organization by default. You can create additional organizations as needed or join an existing one.

All apps (build profiles, distribution profiles, etc.) created under an organization is accessible by all the members of that organization.

Billing management is also per-organization basis so that you can work with different plans with a single account. (e.g. You can be a member of two different organizations at the same time: an individual organization for personal projects under the free plan and another organization for your company under the enterprise plan.)

:::info

Team management with fine-grained roles and integration with enterprise identity systems are available in the enterprise plan. Please [contact us](https://appcircle.io/contact) for more information.

:::

### Accessing the My Organization Screen

The "My Organization" screen is accessible from the button with the organization name initials at the bottom left and it contains all operations to manage an organization.

<Screenshot url='https://cdn.appcircle.io/docs/assets/myaccount-organization.png' />

### Organization Name and ID Management

When you create an account, an individual organization for you is created by default with your email address.

In the left column under the organization management screen, you can change your organization name, which is a descriptive name, and you can change your unique organization ID, which is used for identification purposes for that specific organization.

To update these details, simply enter the new values and press _Update_.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (36).png' />

###

### Working with Multiple Organizations

#### Adding an Organization

To add a new organization, press the "Create New Organization" button on the top-right (denoted by a plus sign) and type in the Organization Name. The organization will be created with the specified name and your role will be set as the owner.

:::caution

If you are on the Starter Plan, you cannot add a new organization. To create more organizations, you need to upgrade to a higher plan.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (39).png' />

#### Adding a Sub Organization

Appcircle's Sub Organization feature allows you to create multiple sub organizations from your organization, providing a way to manage different teams and projects separately. With this feature, each sub organization is linked to the organization.


It's worth noting that sub organizations are very similar to the organization. When you are inside a sub organization, you will have access to all the features and functionality that are available in your  organization. Any licenses  associated with the organization will also be applicable to the sub organization.

:::caution

To use this feature, an enterprise license is required.

:::

If you have an enterprise license, you can create sub organizations from the  organization by navigating to the "My Organization" page, clicking on the "Create Sub Organization" button, and entering the necessary details for the sub organization.

<Screenshot url='https://cdn.appcircle.io/docs/assets/My-Organization-Sub-Create.png' />

Multiple sub organizations can be created from an organization as required. This feature is particularly useful for businesses with multiple teams working on different projects, providing a way to manage each team's access to Appcircle separately. With the Sub Organization feature, businesses can create and manage multiple sub organizations linked to the organization, giving different teams access to the tools they need to work on their specific projects.



#### Switching Organizations

Once you create an organization or accept an organization invite, you will be switched to that organization automatically. To switch between organizations, press the quick team switching button on the bottom-left on status bar and select an organization from the menu. The currently selected one is indicated with a check mark.

Each organization is isolated from each other, and switching means that you will switch to the "workspace" of that organization.

:::info

Once you select your organization, you will only see the profiles, artifacts, and reports belonging to that organization in all modules.

You can switch between organizations at any time without any data loss.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/My-Organization-Switch.png' />

#### Leaving or Deleting an Organization

To leave or delete an organization, press the organization operations button on the top-right (three-dots menu) and select the related operation.

You will be prompted before the leave/delete operation.

:::caution

Both leaving and deleting are irreversible operations and it is advised to use them with caution:

- If you leave an organization, only an Owner can add you back, even if you were an Owner.
- If you delete an organization, you will lose ALL platform data including apps, profiles, and artifacts.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (41).png' />

###

### Managing the Team Under an Organization

#### Team Ownership

The creator of a team starts with the Owner role. The Owner role has full administrative privileges for the team and organization management such as adding/removing members or editing the organization details, while any new members can be assigned specific module-based read/write roles.

:::caution

Each organization must have at least one Owner and each user must be an Owner of at least one organization.

:::

#### Managing Team Members

As an Owner, you can invite new members simply by entering their email address under the related field in Team Management and pressing the Add button.

The user will be then shown in a "Pending" state until the invitation is accepted. You can also revoke a pending invite by pressing the delete button at the end of the row.

Once a user accepts an invite, it will be added to the team as a Member with read only access. You can change the role of any user, including yourself, with the "Manage Roles" button next to the user ID. You can also delete a user by pressing the delete button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (151).png' />

### Advanced Role Management

Once you click the "Manage Roles" button, you will be presented with a detailed selection of roles for each module.

<Screenshot url='https://cdn.appcircle.io/docs/assets/permission-all-v3.png' />

Here, you can assign the Owner role to a user for full access or you can select specific read or write roles for use cases like developers or testers or billing administrators.

<Screenshot url='https://cdn.appcircle.io/docs/assets/permission-owner-v2.png' />

You can see the full list of the available roles below:

---

### BUILD PROFILE PERMISSIONS

Permissions can be customized for build profiles.

|Permission|Explanation|
|----------|-----------|
| Manager | The user can change configuration, workflows, and triggers and start building.|
| Operator | The user can only start the build, view logs, and download logs.|
| Viewer | The user can only view and download logs.|
| None | The user cannot reach any details about build profiles.|

### ENVIRONMENT VARIABLE PERMISSIONS

Permissions can be customized for environment variable.

|Permission|Explanation|
|----------|-----------|
| Manager | The user can see variable groups, add new variables, and delete existing variable groups or variables.|
| Viewer | The user can only see variable groups and their details.|
| None | The user cannot reach any details about environment variables.|

### SIGNING IDENTITY MANAGEMENT PERMISSIONS

Permissions can be customized for signing identity management.

|Permission|Explanation|
|----------|-----------|
| Manager | The user can see, delete, and add new certificates, provisionings, and keys.|
| Viewer | The user can only see certificates, provisioning, and keys.|
| None | The user cannot reach any details about signing identity.|

### DISTRIBUTION PROFILE PERMISSIONS

Permissions can be customized for distribution profiles.

|Permission|Explanation|
|----------|-----------|
| Manager | The user can see, create, and delete new distribution profiles and Apple Devices and customize their settings.|
| Viewer | The user can only view distribution profiles and Apple Devices.|
| None | The user cannot reach any details about distribution profiles.|

### TESTING GROUP PERMISSIONS

Permissions can be customized for testing groups.

|Permission|Explanation|
|----------|-----------|
| Manager | The user can see, create, and delete testing groups and add new test users to groups.|
| Viewer | The user can only view testing groups and test users.|
| None | The user cannot reach any details about the testing group.|

### STORE SUBMIT MODULE PERMISSIONS

Upload apps to Google Play, Huawei, and App Store.

|Permission|Explanation|
|----------|-----------|
| Upload apps to Google Play Console & Huawei AppGallery Console | The user can upload apps to Google Play and Huawei AppGallery.|
| Upload apps to the App Store Console | The user can upload apps only to the App Store.|
| Read-Only Access| The user can only view applications belonging to their own organization.|
:::info
Google Play and Huawei AppGallery permissions are managed through a single rule. When this rule is used, it will apply to both platforms.
:::

### PUBLISH MODULE IOS PERMISSIONS

Publish apps to App Store.

|Permission|Explanation|
|----------|-----------|
| Manager | The user can make changes to the publish flow, publish settings, start publish to the App Store, add or delete a new app version, and view and download logs.|
| Operator | The user can start publishing to the App Store and view and download publish settings, publish flow, and logs.|
| Viewer | The user can only view the iOS application list and logs for the application.|
| None | The user cannot reach any details about the iOS Publish.|

### PUBLISH MODULE ANDROID PERMISSIONS

Publish apps to Google Play, Huawei.

|Permission|Explanation|
|----------|-----------|
| Manager | The user can make changes to the publish flow, publish settings, start publish to the Google Play And  Huawei AppGallery, add or delete a new app version, and view and download logs.|
| Operator | The user can start publishing to the Google Play and Huawei AppGallery and view and download publish settings, publish flow, and logs.|
| Viewer | The user can only view the Android application list and logs for the application.|
| None | The user cannot reach any details about the Android Publish.|
:::info
Google Play and Huawei AppGallery permissions are managed through a single rule. When this rule is used, it will apply to both platforms.
:::

### ENTERPRISE STORE PERMISSIONS

Manage and Upload Apps to Enterprise Store.

|Permission|Explanation|
|----------|-----------|
| Manage Enterprise Settings & Apps | The user can modify both Enterprise Store settings and the uploaded apps.|
| Upload apps to Enterprise Store | The user can only use apps.|
| Read-Only Access| The user can only view the profiles.|

### ORGANIZATION MANAGEMENT PERMISSIONS

The user can create organization or sub organization within license limits, add and remove members, and manage their permissions.

|Permission|Explanation|
|----------|-----------|
| Manager | The user can manage all member permissions and other organization properties mentioned above within license limits.|

### BILLING MANAGEMENT PERMISSIONS

Manage the subscription, payment details, and invoices.

|Permission|Explanation|
|----------|-----------|
| Manager | The user can manage subscriptions, payment details, and invoices.|

### THIRD-PARTY CONNECTION MANAGEMENT PERMISSIONS

Connect to or disconnect from third-party service providers such as Slack, Microsoft Teams, Google Play Developer API Keys, App Store Connect API Keys, Huawei AppGallery Developer API Keys etc.

|Permission|Explanation|
|----------|-----------|
| Manager | The user can manage third-party service provider connections and disconnections.|
