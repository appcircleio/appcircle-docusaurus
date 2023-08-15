---
title: My Organization and Team Management
metaTitle: My Organization and Team Management
metaDescription: My Organization and Team Management
sidebar_position: 4
---

import NarrowImage from '@site/src/components/NarrowImage';

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

![](<https://cdn.appcircle.io/docs/assets/image (162).png>)

### Organization Name and ID Management

When you create an account, an individual organization for you is created by default with your email address.

In the left column under the organization management screen, you can change your organization name, which is a descriptive name, and you can change your unique organization ID, which is used for identification purposes for that specific organization.

To update these details, simply enter the new values and press _Update_.

![](<https://cdn.appcircle.io/docs/assets/image (36).png>)

###

### Working with Multiple Organizations

#### Adding an Organization

To add a new organization, press the "Create New Organization" button on the top-right (denoted by a plus sign) and type in the Organization Name and ID. The organization will be created with the specified values and your role will be set as the owner.

:::caution

If you are on the Starter Plan, you can only add one new organization. To create more organizations, you need to upgrade to a higher plan.

:::

![](<https://cdn.appcircle.io/docs/assets/image (39).png>)


#### Adding a Sub Organization

Appcircle's Sub Organization feature allows you to create multiple sub organizations from your organization, providing a way to manage different teams and projects separately. With this feature, each sub organization is linked to the organization.


It's worth noting that sub organizations are very similar to the organization. When you are inside a sub organization, you will have access to all the features and functionality that are available in your  organization. Any licenses  associated with the organization will also be applicable to the sub organization.

:::caution

To use this feature, an enterprise license is required.

:::

If you have an enterprise license, you can create sub organizations from the  organization by navigating to the "My Organization" page, clicking on the "Create Sub Organization" button, and entering the necessary details for the sub organization.

![](<https://cdn.appcircle.io/docs/assets/My-Organization-Sub-Create.png>)

Multiple sub organizations can be created from an organization as required. This feature is particularly useful for businesses with multiple teams working on different projects, providing a way to manage each team's access to Appcircle separately. With the Sub Organization feature, businesses can create and manage multiple sub organizations linked to the organization, giving different teams access to the tools they need to work on their specific projects.



#### Switching Organizations

Once you create an organization or accept an organization invite, you will be switched to that organization automatically. To switch between organizations, press the quick team switching button on the bottom-left on status bar and select an organization from the menu. The currently selected one is indicated with a check mark.

Each organization is isolated from each other, and switching means that you will switch to the "workspace" of that organization.

:::info

Once you select your organization, you will only see the profiles, artifacts, and reports belonging to that organization in all modules.

You can switch between organizations at any time without any data loss.

:::

![](<https://cdn.appcircle.io/docs/assets/My-Organization-Switch.png>)

#### Leaving or Deleting an Organization

To leave or delete an organization, press the organization operations button on the top-right (three-dots menu) and select the related operation.

You will be prompted before the leave/delete operation.

:::caution

Both leaving and deleting are irreversible operations and it is advised to use them with caution:

- If you leave an organization, only an Owner can add you back, even if you were an Owner.
- If you delete an organization, you will lose ALL platform data including apps, profiles, and artifacts.

:::

![](<https://cdn.appcircle.io/docs/assets/image (41).png>)

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

![](<https://cdn.appcircle.io/docs/assets/image (151).png>)

####

#### Advanced Role Management

Once you click the "Manage Roles" button, you will be presented with a detailed selection of roles for each module. Here, you can assign the Owner role to a user for full access or you can select specific read or write roles for use cases like developers or testers or billing administrators.

You can see the full list of the available roles below:

## General Permissions

Full access allows users to view and manage the contents of the modules. This permission allows users to create, delete, and modify the contents of the module. 

Read only access only allows users to see the content or list of the modules. The modification doesn't allow any modification.

If the access is set as None, users can't access that module.

## Special Permissions

Some modules have different permissions besides general permissions. You can customize permissions of team membet specifically.

**BUILD PROFILE PERMISSIONS**

Permissions can be customized for build profiles.

|Permission|Explanation|
|----------|-----------|
| Full Access | User can change configuration, workflows, triggers and start Build.|
| Read Only | User can start build, but can not see configuration, workflow and trigger details.|
| None | User can not reach any details of build profiles.|

**ENVIRONMENT VARIABLE PERMISSIONS**

Permissions can be customized for environment variable.

|Permission|Explanation|
|----------|-----------|
| Full Access | User can see variable groups, add new variable and delete existing variable or variable groups. |
| Read Only | User can only see variable groups and its details. |
| None | User can not reach any details of environment variables. |

**SIGNIN AND IDENTITY MANAGEMENT PERMISSIONS**

Permissions can be customized for signin and identity management.

|Permission|Explanation|
|----------|-----------|
| Full Access | User can see, delete and add new certificates, provisionings and keys. |
| Read Only | User can only see certificates, provisioning and keys.|
| None | User can not reach any details of signin identity. |


**DISTRIBUTION PROFILE PERMISSIONS**

Permissions can be customized for distribution profiles.

|Permission|Explanation|
|----------|-----------|
| Full Access | User can see, create and delete new distribution profiles and customize its settings. |
| Read Only | User can only see distribution profiles. Can not change settings. |
| None | User can not reach any details of distribution profiles. |

**TESTING GROUP PERMISSIONS**

Permissions can be customized for testing groups.

|Permission|Explanation|
|----------|-----------|
| Full Access | User can see, create and delete testing groups, add new test user to groups. |
| Read Only | User can only see testing groups and test users. Can not add or delete test user. |
| None | User can not reach any details of testing group. |


**STORE SUBMIT MODULE PERMISSIONS**

Upload apps to Google Play, Huawei, and App Store

|Permission|Explanation|
|----------|-----------|
| Upload apps to Google Play and App Store | User can upload apps to all stores|
| Upload apps to Google Play Console | User can upload apps to only Google Play, Huawei|
| Upload apps to Google Play Console | User can upload apps to only App Store|
| Read Only | User can't upload any apps to stores|

**ORGANIZATION MANAGEMENT PERMISSIONS**

Manage the organization and add, remove and manage members

**BILLING MANAGEMENT PERMISSIONS**

Manage the subscription, payment details, and invoices

**THIRD-PARTY CONNECTION MANAGEMENT PERMISSIONS**

Connect to or disconnect from third-party service providers such as Slack, Microsoft Teams.

**ENTERPRISE STORE PERMISSIONS**

Manage and Upload Apps to Enterprise Store

|Permission|Explanation|
|----------|-----------|
|Manage Enterprise Settings & Apps | User can modify both Enterprise Store settings and the uploaded apps|
|Upload Apps to Enterprise Store | User can only apps.|
|Read Only Access| Can only see the profiles|

<NarrowImage src="https://cdn.appcircle.io/docs/assets/screenshot-my.appcircle.io-2021.02.11-23_27_39.png" />
