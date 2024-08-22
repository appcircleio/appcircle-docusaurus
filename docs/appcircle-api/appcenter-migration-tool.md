---
title: App Center Migration Tool
description: Migrate App Center organizations, collaborators,  apps to testing distribution profiles and test groups
tags: [app center, migration, cli]
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';

The appcenter-migration-tool is designed to assist organizations and individuals to migrate their Visual Studio App Center projects with organizations, collaborators, app profiles as testing distribution profile and test groups to Appcircle effortlessly.

By using the **appcenter-migration-tool**, you can ensure a smooth and efficient migration process, minimizing downtime and preserving the integrity of your data.

**Key Features**:

- **Organization Migration:** Effortlessly transfer your entire App Center organization structure to Appcircle.

- **Collaborator Migration:** Move all your App Center collaborators to Appcircle with their roles and permissions intact.

- **Test Group Migration:** Transition your test groups from App Center to Appcircle with all their associated configurations and data.

## How to Install the Tool

**Node.js must be installed on your machine. Version v18.19.0 is recommended.**

To install the appcenter-migration-tool globally, simply run the following npm command:

```bash
npm install -g @appcircle/appcenter-migration-tool
```

Alternatively, you can install it locally:

```bash
npm install @appcircle/appcenter-migration-tool
```

https://www.npmjs.com/package/@appcircle/appcenter-migration-tool

## Migrating from App Center to Appcircle Automatically

Migrating your data in App Center manually can be a time-consuming and error-prone process. The **appcenter-migration-tool** automates this task, allowing you to efficiently and accurately transfer the data you need with minimal effort.

## App Center API Token

When creating a new API token for the migration tool from App Center, granting **Full Access** permission is recommended.

<Screenshot url='https://cdn.appcircle.io/docs/assets/SP-194_appcenter-login-access.png' />

## Using the Tool for Migration

The CLI tool offers the following main commands to login to App Center and migrate the respective entities: **Login**, **Organizations**, **App Center Apps** and **App Center Distribution Groups**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/SP-194_commands_all.png' />

### Login Command

Use the Login command to authenticate with App Center and Appcircle using your token.

| Login Subcommands  | Command Name | Command Options | Explanation                                                                                                                                                 |
| ------------------ | ------------ | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| App Center Account | appcenter    | appcenterToken  | Use your App Center token to authenticate and authorize access.                                                                                             |
| Appcircle Account  | appcircle    | appcircleToken  | Use your Appcircle [Personal API token](/appcircle-api/api-authentication#generatingmanaging-the-personal-api-tokens) to authenticate and authorize access. |

To run the command directly instead of starting an interactive session, simply execute the command as shown below:

```bash
appcenter-migration-tool login appcircle --appcircleToken=YOUR_TOKEN
```

### Organizations Command

Use the Organizations command to list and migrate your App Center organizations to Appcircle.

| Organizations Subcommands                     | Command Name                 | Command Options                                          | Explanation                                    |
| --------------------------------------------- | ---------------------------- | -------------------------------------------------------- | ---------------------------------------------- |
| List App Center Organizations                 | list-appcenter-organizations | -                                                        | List App Center Organizations.                 |
| Migrate App Center Organization to Appcircle  | migrate                      | organizationNames                                        | Migrate App Center Organization to Appcircle.  |
| Migrate App Center Organization Collaborators | migrate-collaborators        | organizationName organizationUsers appcircleOrganization | Migrate App Center organization collaborators. |

To run the command directly instead of starting an interactive session, simply execute the command as shown below:

```bash
appcenter-migration-tool organizations list-appcenter-organizations
```

### App Center Apps Command

Use the App Center Apps command to list and migrate your App Center apps to Appcircle.

| Apps Subcommands                                                 | Command Name      | Command Options  | Explanation                                                                                                                       |
| ---------------------------------------------------------------- | ----------------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| List All App Center Apps                                         | list              | -                | List All App Center Apps.                                                                                                         |
| Migrate App Center App to Appcircle Testing Distribution Profile | list-organization | organizationName | List App Center Apps Based on App Center Organization                                                                             |
| Migrate App Center App to Appcircle Testing Distribution Profile | migrate-profile   | profileName      | Migrate App Center App to Appcircle [Testing Distribution Profile](/testing-distribution/create-or-select-a-distribution-profile) |

To run the command directly instead of starting an interactive session, simply execute the command as shown below:

```bash
appcenter-migration-tool apps list
```

:::caution
migrate-profile command only creates an empty **Testing Distribution Profile** with the same app name in Appcircle. Build details are not included in migration for this version.
:::

### App Center Distribution Groups Command

Use the App Center Distribution Groups command to list and migrate your App Center distribution groups to Appcircle.

| Apps Subcommands                                                      | Command Name         | Command Options                                                           | Explanation                                                                |
| --------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| List available distribution groups in App Center                      | list-organization    | organizationName                                                          | List available distribution groups in App Center for a given organization. |
| List App Center App Distribution Groups                               | list-app             | organizationName appName                                                  | List App Center Apps Based on App Center Organization                      |
| Migrate Distribution Groups from App Center Organization to Appcircle | migrate-organization | organizationName distributionGroupName distGroupUsers                     | Migrate Distribution Groups from App Center Organization to Appcircle      |
| Migrate App Center App Distribution Group to Appcircle                | migrate-app          | organizationName appName distributionGroupNameForApp distGroupUsersForApp | Migrate App Center App Distribution Group to Appcircle                     |

To run the command directly instead of starting an interactive session, simply execute the command as shown below:

```bash
appcenter-migration-tool distribution-groups list-organization --organizationName=YOUR_ORGANIZATION_NAME
```

## Example: Migrating an App Center Organization to Appcircle

In this section, we will provide a comprehensive overview of the migration process from App Center to Appcircle. App Center and Appcircle manage organizations and distribution groups in slightly different manner. The following diagram illustrates a sample organization structure in both App Center and Appcircle.

**Organization Hierarchy for Migration:**

App Center organization hierarchy slated for migration is structured as follows:

<Screenshot url='https://cdn.appcircle.io/docs/assets/SP-194_appcenter_hierarchy.png' />

Migrated Appcircle organization is structured as follows:

<Screenshot url='https://cdn.appcircle.io/docs/assets/SP-194_appcircle_hierarchy.png' />

**Step-by-Step Migration Process:**

1. **Migrating Organizations:**

   - Migrate the organizations from App Center to Appcircle.
   - Appcircle uses a main-sub organization structure, meaning every organization you migrate will become part of a main organization.

2. **Migrating Apps:**

   - Create a Testing Distribution Profile in Appcircle for each app from App Center.
   - This process currently includes only the creation of the profile; migration of build configuration details is not supported yet.

3. **Migrating Distribution Groups:**
   - Migrate Distribution Groups from App Center to Appcircle.
   - App Center allows users to manage distribution groups at both the organization level and the app level.
   - In Appcircle, distribution groups are managed exclusively at the organization level.

### Migrate Organization

The appcenter-migration-tool migrates organizations to Appcircle as sub-organizations under a main organization. This means each migrated organization will be nested under a primary organization. During this migration, the tool will only create organizations that match those existing in App Center. If an organization with the same name already exists in Appcircle, the tool will provide an error.

<Screenshot url='https://cdn.appcircle.io/docs/assets/SP-194_migrate_organization.png' />

```bash
appcenter-migration-tool organizations migrate-collaborators --organizationUsers=guven@appcircle.io --appcircleOrganization=Appcircle_Organization
```

### Migrate Organization Collaborators

The tool invites specified collaborators from App Center to the corresponding organization in Appcircle. As a major difference from App Center, Appcircle offers comprehensive [role management](/account/my-organization/profile-and-team/role-management) based on modules. During the invitation process, the roles of the collaborators from App Center are mapped to the Distribution Profile Roles and Testing Group Roles modules in Appcircle as follows:

| App Center Role | Appcircle Role | Module                                           |
| --------------- | -------------- | ------------------------------------------------ |
| Admin           | Manager        | Distribution Profile Roles & Testing Group Roles |
| Collaborator    | Operator       | Distribution Profile Roles & Testing Group Roles |
| Member          | Viewer         | Distribution Profile Roles & Testing Group Roles |

<Screenshot url='https://cdn.appcircle.io/docs/assets/SP-194_migrate_collaborators.png' />

```bash
appcenter-migration-tool organizations migrate --organizationNames=Appcircle_Organization
```

### Migrate App Center Apps to a Testing Distribution Profile at Appcircle

The tool creates a [Testing Distribution Profile](/testing-distribution/create-or-select-a-distribution-profile) in Appcircle using the specified App Center app name.

```bash
appcenter-migration-tool apps migrate-profile --profileNames=Appcircle
```

<Screenshot url='https://cdn.appcircle.io/docs/assets/SP-194_migrate_test_profile.png' />

:::caution
The tool creates only a new [Testing Distribution Profile](/testing-distribution/create-or-select-a-distribution-profile) and does not migrate any existing releases at this time.
:::

### Migrate Organization Distribution Groups

The tool migrates **distribution groups** of the organizations from App Center organizations to **testing groups** in Appcircle.

```bash
appcenter-migration-tool migrate-organization --organizationName=Appcircle_Organization --distributionGroupName=Internal --distGroupUsers=guven@appcircle.io
```

<Screenshot url='https://cdn.appcircle.io/docs/assets/SP-194_migrate_app_profile.png' />

### Migrate App Distribution groups

The tool migrates **distribution groups** of the apps from App Center app to **testing groups** in Appcircle.

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

or if you installed locally, you can run the following npm command:

```bash
npm update @appcircle/appcenter-migration-tool
```

## How to Uninstall the Tool

If you installed appcenter-migration-tool globally, simply run the following npm command:

```bash
npm uninstall -g @appcircle/appcenter-migration-tool
```

or if you installed locally, you can run the following npm command:

```bash
npm uninstall @appcircle/appcenter-migration-tool
```
