---
title: Connecting to Azure DevOps
metaTitle: Connecting to Azure DevOps
metaDescription: Connecting to Azure DevOps
sidebar_position: 4
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

# Connecting to Azure DevOps

## Connecting to Azure DevOps Services Cloud

### Requirements

You must enable third-party application access via OAuth. To do that, you can follow the steps:

- Go to https://dev.azure.com
- Click to Organization setting from the left sidebar.
- Go to your policies settings below security.
- Enable Third-Party application access via OAuth.

:::caution
If you don't enable third-party application access via the Oauth setting, you can't authorize Appcircle.
:::

### Configuration Azure DevOps Services Setting on Appcircle

If you authorize Appcircle to access your repositories on Azure DevOps, you can select the repository that you want to connect in the next screen.

<Screenshot url='https://cdn.appcircle.io/docs/assets/azure-connect-main.png' />

After you click on **Azure**, the following screen will appear. This will let you choose between selecting a repository, which you have already authorized Appcircle to do, or ask your consent about authorizing more repositories.

<Screenshot url='https://cdn.appcircle.io/docs/assets/azure-connection-3.png' />

When you successfully authorize your account, the following screen will appear to let you select one for connection:

<Screenshot url='https://cdn.appcircle.io/docs/assets/connect-repository-bitbucket-gitlab.png' />

After the connection is successful, you can [view your newly created profile](./#view-the-newly-created-build-profile) and start building!

## Connecting to Azure DevOps Server Repository

The overall process is similar to a private repository connection through SSH, but Appcircle allows you to directly connect through the Azure DevOps Server URL.

:::caution
TFS is not compatible with Azure DevOps Server on Appcircle.
:::

:::caution
Azure DevOps Server version must be **Azure DevOps Server 2020** or higher.
:::

First, select **Azure** and then **Connect to an Azure DevOps Server** through the menu:

<Screenshot url='https://cdn.appcircle.io/docs/assets/azure-con-2.png' />

Fill in the relevant information about your Azure DevOps Server. If you are not sure what those are, contact your system administrator.

<Screenshot url='https://cdn.appcircle.io/docs/assets/azure-con-5.png' />

- **Connection Name**: Appcircle allows multiple instance connections. Here, you can give the connection a name so you can group the connections together.

  - For example: `InternalAzure`

- **Azure DevOps Server URL**: Use the server URL without a path. If the server has a custom port, it should be appended to the URL using `:` in front of the port.

  - For example: `https://azure.spacetech.com`

- **Owner Username**: Use the collection name on the Azure Devops Server. You can see collections on the left-hand side when you open your Azure Devops Server home page.

  - For example: `DefaultCollection`

- **Personal Access Token**: Use the personal access token that you created earlier and that has enough permissions.
  - For example: `54rdrkce6wa4d22kf75lhmq4hosgx7iy7h76cc62y77oguombnnq`

:::caution

### Azure Devops Server That Is Upgraded From a TFS Server

If your Azure Devops Server is upgraded from a TFS server, you should identify your Azure Devops Server URL.

- Copy a repository clone URL for any git repository.
- Check if your URL has an unexpected **path** in the URL.
  - For example: `https://azure.spacetech.com/tfs/DefaultCollection/MOBILE_IOS/_git/wallet`
- If there is a path between your domain (`azure.spacetech.com`) and your collection name (`DefaultCollection`), you must give that path (`tfs`) as a prefix in the "Owner Username".
  - For example, the fields should have values like below.
    - Azure DevOps Server URL: `https://azure.spacetech.com`
    - Owner Username: `tfs/DefaultCollection`
    - Personal Access Token: `54rdrkce6wa4d22kf75lhmq4hosgx7iy7h76cc62y77oguombnnq`

:::

:::caution

### Connection Notice

For Appcircle to connect to the Azure DevOps Server instance, your connection must be reachable over the network.

:::

Is your Azure DevOps Server instance under the enterprise firewall? Learn which IP addresses and ports Appcircle uses to function under the whitelist documentation:

<ContentRef url="/build/manage-the-connections/accessing-repositories-in-internal-networks-firewalls">
Accessing Repositories in Internal Networks (Firewalls)
</ContentRef>

### Token Creation

Azure DevOps Server has one kind of token at their self-hosted instance:

- [Personal Access Token](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&tabs=Windows)

That being said, **Personal Access Token** is used to authorize every repository the user has access to.

:::info

Appcircle needs admin permission to function properly. The admin permission is needed to create relevant WebHooks automatically.

:::

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
