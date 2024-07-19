---
title: App Center Migration Tool
description: Migrate App Center organizations, collaborators,  apps to testing distribution profiles and test groups
tags: [app center, migration, cli]
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';

The appcenter-migration-tool is designed to assist App Center projects in seamlessly migrating their organizations, collaborators, app profiles, and test groups to Appcircle.

By using the **appcenter-migration-tool**, you can ensure a smooth and efficient migration process, minimizing downtime and preserving the integrity of your data.

**Key Features**:

- **Organization Migration:** Effortlessly transfer your entire organization structure to the new platform.

- **Collaborator Migration:** Move all your collaborators with their roles and permissions intact.

- **App Profile Migration:** Migrate app profiles, ensuring all settings and configurations are preserved.

- **Test Group Migration:** Transition your test groups with all their associated configurations and data.

By using the appcenter-migration-tool, you can ensure a smooth and efficient migration process, minimizing downtime and preserving the integrity of your data.

## Migrating App Center Automatically with tool

Migrating your data in App Center manually can be a time-consuming and error-prone process. The **appcenter-migration-tool** automates this task, allowing you to efficiently and accurately transfer the data you need with minimal effort.

This version emphasizes the benefits of using the tool and highlights the efficiency and accuracy it offers compared to manual migration.

## How to Install the Tool

**Node.js must be installed on your machine. We recommend using version v18.19.0.**

To install the appcenter-migration-tool globally, simply run the following npm command:

```bash
npm install -g @appcircle/appcenter-migration-tool
```

Alternatively, you can install it locally:

```bash
npm install @appcircle/appcenter-migration-tool
```

## Using the Tool for Migration

The CLI tool offers the following main commands **Login**, **Organizations**, **App Center Apps** and **App Center Distribution Groups**. You can interact with these commands to achieve your desired migration seamlessly.

<Screenshot url='https://cdn.appcircle.io/docs/assets/SP-194_commands_all.png' />

### Login Command

Use the Login command to authenticate with App Center and Appcircle using your token.

| Login Subcommands  | Command Name | Command Options | Explanation                                                                                                                                                 |
| ------------------ | ------------ | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| App Center Account | appcenter    | appcenterToken  | Use your App Center token to authenticate and authorize access.                                                                                             |
| Appcircle Account  | appcircle    | appcircleToken  | Use your Appcircle [Personal API token](/appcircle-api/api-authentication#generatingmanaging-the-personal-api-tokens) to authenticate and authorize access. |

To run a command directly instead of entering an interactive session, simply execute the command as shown below:

```bash
appcenter-migration-tool login appcircle --appcircleToken=YOUR_TOKEN
```

### Organizations Command

Use the Organizations command to list and migrate your App Center organizations.

| Organizations Subcommands                     | Command Name                 | Command Options                                          | Explanation                                    |
| --------------------------------------------- | ---------------------------- | -------------------------------------------------------- | ---------------------------------------------- |
| List App Center Organizations                 | list-appcenter-organizations | -                                                        | List App Center Organizations.                 |
| Migrate App Center Organization to Appcircle  | migrate                      | organizationNames                                        | Migrate App Center Organization to Appcircle.  |
| Migrate App Center Organization Collaborators | migrate-collaborators        | organizationName organizationUsers appcircleOrganization | Migrate App Center organization collaborators. |

To run a command directly instead of entering an interactive session, simply execute the command as shown below:

```bash
appcenter-migration-tool organizations list-appcenter-organizations
```

### App Center Apps Command

Use the App Center Apps command to list and migrate your App Center apps.

| Apps Subcommands                                                 | Command Name      | Command Options  | Explanation                                                                                                             |
| ---------------------------------------------------------------- | ----------------- | ---------------- | ----------------------------------------------------------------------------------------------------------------------- |
| List All App Center Apps                                         | list              | -                | List All App Center Apps.                                                                                               |
| Migrate App Center App to Appcircle Testing Distribution Profile | list-organization | organizationName | List App Center Apps Based on App Center Organization                                                                   |
| Migrate App Center App to Appcircle Testing Distribution Profile | migrate-profile   | profileName      | Migrate App Center App to Appcircle [Testing Distribution Profile](/distribute/create-or-select-a-distribution-profile) |

To run a command directly instead of entering an interactive session, simply execute the command as shown below:

```bash
appcenter-migration-tool apps list
```

:::caution
migrate-profile command only creates a **Testing Distribution Profile** with the app name at Appcircle. Currently Build details does not included in migration
:::

### App Center Distribution Groups Command

Use the App Center Distribution Groups command to list and migrate your App Center distribution groups.

| Apps Subcommands                                                      | Command Name         | Command Options                                                           | Explanation                                                                |
| --------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| List available distribution groups in App Center                      | list-organization    | organizationName                                                          | List available distribution groups in App Center for a given organization. |
| List App Center App Distribution Groups                               | list-app             | organizationName appName                                                  | List App Center Apps Based on App Center Organization                      |
| Migrate Distribution Groups from App Center Organization to Appcircle | migrate-organization | organizationName distributionGroupName distGroupUsers                     | Migrate Distribution Groups from App Center Organization to Appcircle      |
| Migrate App Center App Distribution Group to Appcircle                | migrate-app          | organizationName appName distributionGroupNameForApp distGroupUsersForApp | Migrate App Center App Distribution Group to Appcircle                     |

To run a command directly instead of entering an interactive session, simply execute the command as shown below:

```bash
appcenter-migration-tool distribution-groups list-organization --organizationName=YOUR_ORGANIZATION_NAME
```

## Migrate Sample Organization

In this section, we will provide a comprehensive overview of the migration process from App Center to Appcircle. App Center and Appcircle manage organizations and distribution groups slightly differently. The following diagram illustrates a sample organization structure in both App Center and Appcircle.

**Organization Hierarchy for Migration:**

App Center organization hierarchy slated for migration is structured as follows:

<Screenshot url='https://cdn.appcircle.io/docs/assets/SP-194_appcenter_hierarchy.png' />

Migrated Appcircle organization is structured as follows:

<Screenshot url='https://cdn.appcircle.io/docs/assets/SP-194_appcircle_hierarchy.png' />

Demonstrates how migration might look like step-by-step:

1. Migrating the organizations from App Center to Appcircle. Appcircle manages organizations using a main-sub organization structure. This means that every organization you migrate will be part of a main organization.
2. Migrating apps from App Center to Appcircle involves creating a Testing Distribution Profile in Appcircle. This process currently includes only the creation of the profile; **migration of build configuration details is not supported yet**.
3. Migrating Distribution Groups from App Center to Appcircle. App Center allows users to manage distribution groups in two ways: at the organization level and at the app level. In Appcircle, distribution groups are managed exclusively at the organization level.

### Migrate Organization

The appcenter-migration-tool migrates organizations to Appcircle as sub-organizations under a main organization. This means each migrated organization will be nested under a primary organization. During this migration, the tool will only create organizations that match those existing in App Center. If an organization with the same name already exists in Appcircle, the tool will throw an error.

<Screenshot url='https://cdn.appcircle.io/docs/assets/SP-194_migrate_organization.png' />

```bash
appcenter-migration-tool organizations migrate-collaborators --organizationUsers=guven@appcircle.io --appcircleOrganization=Appcircle_Organization
```

### Migrate Organization Collaborators

The tool invites specified collaborators from App Center to the corresponding organization in Appcircle. Additionally, Appcircle offers comprehensive [role management](/account/my-organization/role-management) based on modules. During the invitation process, we map the collaborators' roles from App Center to the Distribution Profile Roles and Testing Group Roles modules in Appcircle as follows:

| App Center Role | Appcircle Role | Module                                           |
| --------------- | -------------- | ------------------------------------------------ |
| Admin           | Manager        | Distribution Profile Roles & Testing Group Roles |
| Collaborator    | Operator       | Distribution Profile Roles & Testing Group Roles |
| Member          | Viewer         | Distribution Profile Roles & Testing Group Roles |

<Screenshot url='https://cdn.appcircle.io/docs/assets/SP-194_migrate_collaborators.png' />

```bash
appcenter-migration-tool organizations migrate --organizationNames=Appcircle_Organization
```

### Migrate App Center Apps to Testing Distribution Profile at Appcircle

The tool creates a [Testing Distribution Profile](/distribute/create-or-select-a-distribution-profile) in Appcircle using only the specified App Center app name.

```bash
appcenter-migration-tool apps migrate-profile --profileNames=Appcircle
```

<Screenshot url='https://cdn.appcircle.io/docs/assets/SP-194_migrate_test_profile.png' />

:::caution
The tool creates only a new [Testing Distribution Profile](/distribute/create-or-select-a-distribution-profile) and does not migrate any existing releases at this time.
:::

### Migrate Organization Distribution Groups

The tool migrates **distribution groups** from App Center organizations to **testing groups** in Appcircle.

```bash
appcenter-migration-tool migrate-organization --organizationName=Appcircle_Organization --distributionGroupName=Internal --distGroupUsers=guven@appcircle.io
```

<Screenshot url='https://cdn.appcircle.io/docs/assets/SP-194_migrate_app_profile.png' />

### Migrate App Distribution groups

The tool migrates **distribution groups** from App Center app to **testing groups** in Appcircle.

```bash
appcenter-migration-tool migrate-organization --organizationName=Appcircle_Organization --appName=Appcircle-iOS --distributionGroupNameForApp="Beta Testers" --distGroupUsersForApp=guven@appcircle.io

```

:::info
In App Center, distribution groups can be managed at both the organization level and the app level. In contrast, Appcircle consolidates all testing groups into a single management location.
:::

## How to Upgrade the Tool

If you installed appcenter-migration-tool globally, simply run the following npm command:

```bash
npm update -g @appcircle/appcenter-migration-tool
```

or if you installed locally, run the following npm command:

```bash
npm update @appcircle/appcenter-migration-tool
```

## How to Uninstall the Tool

If you installed appcenter-migration-tool globally, simply run the following npm command:

```bash
npm uninstall -g @appcircle/appcenter-migration-tool
```

or if you installed locally, run the following npm command:

```bash
npm uninstall @appcircle/appcenter-migration-tool
```
