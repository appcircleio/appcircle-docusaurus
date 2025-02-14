---
title: Connecting to GitHub
description: Learn how to connect your GitHub repositories to Appcircle
tags: [build profile, connection, github]
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';
import NeedHelp from '@site/docs/\_need-help.mdx';

# Connecting to GitHub

If you authorize Appcircle to access your repositories on GitHub, you can select the repository that you want to connect in the next screen.

If you are a part of an organization, you can also connect your organization's repositories too. To grant Appcircle permission to access the repositories of an organization, you need to have the necessary privileges at the organization level. For GitHub, you have to provide selective access to specific repositories.

In such a case, only the selected repositories will be listed. To be able to view other repositories, you must grant access for them under the Applications section in the account/organization settings screen on GitHub. You can directly access this screen by clicking on the **Missing a repository? Grant access from GitHub**.

:::info

For connection to GitHub, Appcircle uses GitHub App instead of GitHub OAuth. GitHub App is a more secure and newer way implemented by GitHub for external apps to communicate within GitHub in a better fashion.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-repoconnect1.png' />

After you click on **GitHub**, the following screen will appear. This will let you choose between selecting a repository that you are already authorized to do with Appcircle or asking your consent about authorizing more repositories.

<Screenshot url='https://cdn.appcircle.io/docs/assets/github-main.png' />

When you successfully authorize your repository or repositories, the following screen will appear to let you select one for connection:

<Screenshot url='https://cdn.appcircle.io/docs/assets/connect-repository-github.png' />

After the connection is successful, you can [view your newly created profile](/build/build-process-management/profile-creation#profile-listing) and start building!

## Connecting to GitHub Cloud Repository

To connect to a GitHub Cloud repository using either OAuth or Personal Access Token,

- OAuth Connection

Clicking on Get Repositories from GitHub Cloud for the first time will require application access to Appcircle, and this access will require these permissions in order to work properly.

- PAT (Personal Access Token) Connection

Clicking on Connect to a GitHub server, which can be selected to connect to self-hosted and PAT connections, will require a token. Generating a PAT for Appcircle will require a list of permissions down below.

### OAuth Permissions for GitHub Integration

The following table details the OAuth permissions required for Appcircle to connect with GitHub. These permissions grant read access to projects, repositories, pull requests, and webhooks, ensuring proper functionality when integrating with GitHub via OAuth. 

| Scope                | Permission   | Description                                                                                                                                                                                   |
|----------------------|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Checks               | Read&Write   | Grants the ability to manage check suites and check runs. This includes creating, updating, and retrieving check statuses.                                                                    |
| Commit statuses      | Read&Write   | Allows read and write access to commit statuses. This enables an application to create, update, and retrieve statuses for specific commits.                                                   |
| Contents             | Read         | Read-only access to a repository's contents, including files, commits, branches, and directories. This scope allows an application to fetch and display repository data without modifications.|
| Metadata (Mandatory) | Read         | Grants read access to repository metadata, such as repository names, descriptions, and other settings. This scope is essential for accessing basic repository information.                    |
| Pull requests        | Read&Write   | Allows read and write access to pull requests and related comments.                                                                                                                           |
| Webhooks             | Read&Write   | Provides the ability to manage repository webhooks. This includes creating, updating, listing, and deleting webhooks                                                                          |

## FAQ

### Unable to grant access to a GitHub organization

If you are unable to grant access to a specific organization while connecting to GitHub, it is likely that the permission for Appcircle needs an update from the organization application access settings.

To resolve, go to Organization Settings -> Third-party access and press edit next to Appcircle to authorize it for the organization.

<NeedHelp />
