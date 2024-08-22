---
title: Team Management
description: Organizations in Appcircle are separate units with separate "workspaces" that allow collaboration on the same apps with a team.
tags: [organization, team, settings]
sidebar_position: 2
---

import ContentRef from '@site/src/components/ContentRef';
import Screenshot from '@site/src/components/Screenshot';

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

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4072-org4.png" />

:::tip
The search bar within the Team Management area allows you to efficiently manage and locate organization members by searching their email addresses to enhance visibility and streamline the management of both current and newly invited members.

:::

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4072-search.png" />

### Advanced Role Management

:::info
Team management with fine-grained roles and integration with enterprise identity systems are available in the enterprise plan. Please [contact us](https://appcircle.io/contact) for more information.
:::

Once you click the "Manage Roles" button, you will be presented with a detailed selection of roles for each module.

<Screenshot url='https://cdn.appcircle.io/docs/assets/permission-all-v3.png' />

Here, you can assign the Owner role to a user for full access or you can select specific read or write roles for use cases like developers or testers or billing administrators.

<Screenshot url='https://cdn.appcircle.io/docs/assets/permission-owner-v2.png' />

:::info

The "None" is a special type of permission that denotes that a user has no defined role or special permissions. If the user's permission is set to "None" in sub-organizations, the user's permission defaults from the organization.

:::

For more information on the roles and permissions, please refer to the:

<ContentRef url="/account/my-organization/profile-and-team/role-management"> 
    Role Management
</ContentRef>
