---
title: Connecting to GitHub
description: Learn how to connect your GitHub repositories to Appcircle
tags: [build profile, connection, github]
sidebar_position: 1
slug: /build/manage-the-connections/connection-guides/connecting-to-github
---

import Screenshot from '@site/src/components/Screenshot';
import NeedHelp from '@site/docs/\_need-help.mdx';

# Connecting to GitHub

If you authorize Appcircle to access your repositories on GitHub, you can select the repository that you want to connect in the next screen. Only the selected repositories will be listed.

:::info

If you are a part of an organization, you can also connect your organization's repositories too. To grant Appcircle permission to access the repositories of an organization, you need to have the necessary privileges at the organization level. For GitHub, you have to provide selective access to specific repositories.

:::

:::info

For connection to GitHub, Appcircle uses GitHub App instead of GitHub OAuth. GitHub App is a more secure and newer way that implemented by GitHub uses OAuth2 for external apps to communicate within GitHub in a better fashion.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-repoconnect1.png' />

After you click on **GitHub**, the following screen will appear. This will let you choose between selecting a repository that you are already authorized to do with Appcircle.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6444-github1.png' />

When you successfully authorize your repository or repositories, the following screen will appear to let you select one for connection:

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6444-connect-repository-github.png' />

After the connection is successful, you can [view your newly created profile](/build/build-process-management/profile-creation#profile-listing) and start building!

## Connecting to GitHub Cloud Repository

To connect to a GitHub cloud repository, you can use two different authentication methods:

- **GitHub App Cloud**  
  Authenticate and authorize Appcircle to access your GitHub repositories using GitHub App OAuth2 integration. This is the recommended and default method.

- **GitHub Cloud**  
  Use this method to manually connect using a GitHub Fine-Grained Personal Access Token (PAT). You will be required to fill out:

  - Connection Name
  - GitHub Server URL (e.g., `https://github.com`)
  - GitHub Username
  - Fine-Grained Personal Access Token

### OAuth2 and Personal Access Token Permissions for GitHub Integration

The following table details the OAuth2 and fine-grained personal access token permissions required for Appcircle to connect with GitHub. These permissions grant read access to projects, repositories, pull requests, and webhooks, ensuring proper functionality when integrating with GitHub via OAuth2 and Personal Access Token. 

| Scope                | Permission   | Description                                                                                                                                                                                   |
|----------------------|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Commit statuses      | Read & Write | Allows read and write access to commit statuses. This enables an application to create, update, and retrieve statuses for specific commits.                                                   |
| Contents             | Read         | Read-only access to a repository's contents, including files, commits, branches, and directories. This scope allows an application to fetch and display repository data without modifications.|
| Metadata (Mandatory) | Read         | Grants read access to repository metadata, such as repository names, descriptions, and other settings. This scope is essential for accessing basic repository information.                    |
| Pull requests        | Read         | Allows read access to pull requests and related comments.                                                                                                                                     |
| Webhooks             | Read & Write | Provides the ability to manage repository webhooks. This includes creating, updating, listing, and deleting webhooks                                                                          |

## Connecting to GitHub Enterprise Repository

The overall process is similar to a private repository connection through cloud personal access token, but Appcircle allows you to directly connect through GitHub Enterprise self-hosted URL.

First, select **GitHub** and then **GitHub Enterprise** under **Create a New GitHub Enterprise Connection** through the menu:

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6444-githubenterprise1.png' />

To connect to a self-hosted GitHub Enterprise instance, use the following fields when selecting the **GitHub Enterprise** option:

- **Connection Name**: A custom name to identify this connection.
- **GitHub Server URL**: Your GitHub instance URL (e.g., `https://github.company.com`)
- **Username**: The GitHub username of the account owning the token.
- **Personal Access Token**: The fine-grained token generated in your GitHub profile for API or repository access.

If you are not sure what those are, contact your system administrator.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6444-githubenterprise2.png' />

## FAQ

### Unable to grant access to a GitHub organization

If you are unable to grant access to a specific organization while connecting to GitHub, it is likely that the permission for Appcircle needs an update from the organization application access settings.

To resolve, go to Organization Settings -> Third-party access and press edit next to Appcircle to authorize it for the organization.

<NeedHelp />
