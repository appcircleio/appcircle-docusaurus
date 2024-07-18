---
title: App Center Migration CLI Tool
description: Migrate App Center organizations, collaborators,  apps to testing distribution profiles and test groups
tags: [appcenter, migration, cli]
sidebar_position: 3
---

The appcenter-migration-tool is designed to assist App Center users in seamlessly migrating their organizations, collaborators, app profiles, and test groups to Appcircle.

By using the **appcenter-migration-tool**, you can ensure a smooth and efficient migration process, minimizing downtime and preserving the integrity of your data.

**Key Features**:

- **Organization Migration:** Effortlessly transfer your entire organization structure to the new platform.

- **Collaborator Migration:** Move all your collaborators with their roles and permissions intact.

- **App Profile Migration:** Migrate app profiles, ensuring all settings and configurations are preserved.

- **Test Group Migration:** Transition your test groups with all their associated configurations and data.

By using the appcenter-migration-tool, you can ensure a smooth and efficient migration process, minimizing downtime and preserving the integrity of your data.

## Migrating App Center Automatically with CLI

Migrating your data in App Center manually can be a time-consuming and error-prone process. The **appcenter-migration-tool** automates this task, allowing you to efficiently and accurately transfer the data you need with minimal effort.

This version emphasizes the benefits of using the tool and highlights the efficiency and accuracy it offers compared to manual migration.

## Using the CLI Tool for Migration

The CLI tool offers the following main commands **Login**, **Organizations**, **App Center Apps** and **App Center Distribution Groups**. You can interact with these commands to achieve your desired migration seamlessly.

[-Screen Shot showecase main commands on terminal-]

### Login Command

Use the Login command to authenticate with App Center and Appcircle using your token.

| Login Subcommands  | Command Name | Command Options           | Explanation                                                     |
| ------------------ | ------------ | ------------------------- | --------------------------------------------------------------- |
| App Center Account | appcenter    | appcenterToken, profileId | Use your App Center token to authenticate and authorize access. |
| Appcircle Account  | appcircle    | --appcircleToken          | Use your Appcircle token to authenticate and authorize access.  |

To run a direct command instead of an interactive session, you can achieve it by executing the command as shown below:

```bash
appcenter-migration-tool login appcenter --appcenterToken=YOUR_TOKEN
```

## Migrate Sample Organization

In this section, we will walk through the process of a migration to provide a comprehensive overview.

**Organization Hierarchy for Migration:**

App Center organization hierarchy slated for migration is structured as follows:

- **Appcircle Organization**

  - **Apps**
    - Appcircle_iOS
      - **Distribution groups**
        - Beta Testers
  - **Distribution group**

    - Internal Testers

  - **Collaborators**
    - user1
    - user2

Migrated Appcircle organization is structured as follows:

- **Main Organization**
  - Appcircle Organization
    - **Testing Distribution**
      - Appcircle_iOS
    - **Testing Groups**
      - Internal Testers
      - Beta Testers
