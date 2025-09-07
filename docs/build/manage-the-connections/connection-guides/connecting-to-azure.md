---
title: Connecting to Azure DevOps
description: Learn how to connect to Azure DevOps in Appcircle
tags: [build profile, connection]
sidebar_position: 4
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

# Connecting to Azure DevOps

### Requirements

You must enable third-party application access via OAuth. To do that, you can follow the steps:

- Go to https://dev.azure.com
- Click on the Organization setting from the left sidebar.
- Go to your policy settings below security.
- Enable third-party application access via OAuth.

:::important Third-party application access via OAuth
To successfully connect your Azure DevOps Cloud Repository with an Appcircle Build Profile, the “**Third-party application access via OAuth**” policy must be enabled in your Azure DevOps organization settings.

This setting allows Appcircle to authenticate and interact with your repositories securely. If this policy is turned off, Appcircle will be unable to establish a connection, and repository integration will fail.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6017-azure.png' />

### Configuration Azure DevOps Services Setting on Appcircle

If you authorize Appcircle to access your repositories on Azure DevOps, you can select the repository that you want to connect in the next screen.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-repoconnect1.png' />

After you click on **Azure**, the following screen will appear. This will let you choose between selecting a repository, which you have already authorized Appcircle to do, or asking your consent about authorizing more repositories.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6369-githubimage.png' />

When you successfully authorize your account, the following screen will appear to let you select one for connection:

<Screenshot url='https://cdn.appcircle.io/docs/assets/connect-repository-bitbucket-gitlab.png' />

After the connection is successful, you can [view your newly created profile](/build/build-process-management/profile-creation#profile-listing) and start building!

## Connecting to Azure DevOps Cloud Repository

To connect to a Azure DevOps Cloud repository using either OAuth or Personal Access Token,

- **OAuth2 Connection**  
  Click **Get Repositories from Azure DevOps (OAuth2)** to authenticate Appcircle using your Azure DevOps account credentials. This will grant Appcircle access to your repositories through the authorized scope.

- **Personal Access Token (User)**  
  Use your Azure DevOps username and [Personal Access Token (PAT)](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops) to connect manually. Required fields:

  - Connection Name
  - Azure DevOps Server URL (e.g., `https://dev.azure.com`)
  - Collection Name (e.g., `DefaultCollection`)
  - Personal Access Token

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6369-azure4.png' />

### OAuth2 Permissions for Azure DevOps Integration

The following table details the OAuth permissions required for Appcircle to connect with Azure DevOps. These permissions grant read access to projects, repositories, pull requests, and webhooks, ensuring proper functionality when integrating with Azure DevOps via OAuth. 

| Scope            | Permission        | Description                                                                                                                                                                            |
|------------------|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code             | Read , Status     | Provides read access to repositories, enabling applications to fetch and view source code. Allows applications to post and update build or commit statuses in repositories.            |
| PR threads       | Full              | Enables access to pull request comments and discussions (threads), including reading and posting messages.                                                                             |
| Service Endpoints| Read , Query      | Grants read, query access to service endpoints. Allows listing external service integrations and retrieving details of existing connections, but does not permit creating or modifying.|
| Project and team | Read              | Provides read access to project and team-related information, such as project details and team memberships.                                                                            |
| Notifications    | Read              | Grants read-only access to notification settings.                                                                                                                                      |

## Connecting to Azure DevOps Server Repository

The overall process is similar to a private repository connection through SSH, but Appcircle allows you to directly connect through the Azure DevOps Server URL.

:::caution
TFS is not compatible with Azure DevOps Server on Appcircle.
:::

:::caution
Azure DevOps Server version must be **Azure DevOps Server 2020** or higher.
:::

First, select **Azure** and then **Personal Access Token (User)** under **Create a new Azure Devops Connection** through the menu:

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6369-githubimage.png' />

Fill in the relevant information about your Azure DevOps Server. If you are not sure what those are, contact your system administrator.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6369-azure5.png' />

- **Connection Name**: Give a name to this connection for easier identification in your list of integrations.
- **Azure DevOps Server URL**: Provide the base URL of your Azure DevOps Server (e.g., `https://azuredevops.mycompany.com`).
- **Collection Name**: Specify the name of the collection on your Azure DevOps Server (e.g., `DefaultCollection`).
- **Personal Access Token**: Enter the token generated in your Azure DevOps Server profile settings for Git access.

Required permissions are listed below:

| Scope            | Permission        | Description                                                                                                                                                                |
|------------------|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Identity         | Read              | Allows reading identity information, such as users and groups within the organization                                                                                      |
| Code             | Read , Status     | Provides read access to repositories, enabling applications to fetch and view source code. Allows applications to post and update build or commit statuses in repositories.|
| Notifications    | Read              | Grants read-only access to notification settings.                                                                                                                          |

### Azure Devops Server That Is Upgraded From a TFS Server

:::caution

If your Azure DevOps Server is upgraded from a TFS server, you should identify your Azure DevOps Server URL.

- Copy a repository clone URL for any git repository.
- Check if your URL has an unexpected **path** in the URL.
  - For example: `https://azure.spacetech.com/tfs/DefaultCollection/MOBILE_IOS/_git/wallet`
- If there is a path between your domain (`azure.spacetech.com`) and your collection name (`DefaultCollection`), you must give that path (`tfs`) as a prefix in the "Owner Username".
  - For example, the fields should have values like below.
    - Azure DevOps Server URL: `https://azure.spacetech.com`
    - Owner Username: `tfs/DefaultCollection`
    - Personal Access Token: `54rdrkce6wa4d22kf75lhmq4hosgx7iy7h76cc62y77oguombnnq`

:::

:::caution Connection Notice

For Appcircle to connect to the Azure DevOps Server instance, your connection must be reachable over the network.

:::

Is your Azure DevOps Server instance under the enterprise firewall? Learn which IP addresses and ports Appcircle uses to function under the whitelist documentation:

<ContentRef url="/build/manage-the-connections/accessing-repositories-in-internal-networks-firewalls">
Accessing Repositories in Internal Networks (Firewalls)
</ContentRef>

### Token Creation

- [Personal Access Token Azure DevOps Documentation](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&tabs=Windows)

A user’s **Personal Access Token** enables connection to their repository through Appcircle. It is used to authorize access to all repositories the user can access.

### Check Token

You can follow the steps below to check if your token is valid.

- Open the terminal and issue the following command:

```bash
personalAccessToken=abcde && \
serverUrl=https://azure.spacetech.com && \
organizationName=Appcircle && \
curl -H "Authorization: Basic $(echo -n :${personalAccessToken} | base64)" \
"${serverUrl}/${organizationName}/_apis/projects?api-version=6.0" | jq
```

The above command should print out your projects. If you don't see an output, please check your token, Azure DevOps Server address, or collection name.

:::caution

Please also make sure that the output doesn't show any reference to `localhost`. If you see `localhost`, you need to configure Azure DevOps Server and put the correct address of the instance.

:::

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />
