---
title: Connecting to Multiple Instances
description: Learn how to connect to multiple instances of the same Git provider in Appcircle
tags: [build profile, multiple instances, git providers]
sidebar_position: 7
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

### Multiple Instances Using Git Providers (Bitbucket, GitLab, Azure DevOps)

Multiple connection features have been introduced for connections made with PAT (Personnel Access Token) on Bitbucket, Azure DevOps, or GitLab. Thus, it is possible to add Bitbucket, Azure DevOps, or GitLab servers located in different environments by a single user.

For example, the same user can connect to two different instances, such as dev1.azure.companyname.com and dev2.azure.companyname.com.

Similar examples are dev1.gitlab.companyname.com and dev2.gitlab.companyname.com or dev.bitbucket.companyname.com and prod.bitbucket.companyname.com.

:::caution
In order to use this feature, it is necessary to create a PAT on the provider.
:::

:::info
To add a git provider, PAT support is sufficient. There is no distinction between self-hosted and cloud-based.
:::

See below steps for an example case from Azure DevOps.

First of all, we select the relevant Git provider from the add new repository screen.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-repoconnect1.png' />

Then click on the "Connect to an Azure DevOps Server" button in the window that opens.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-repoconnect4.png' />

In the next window, fill in the relevant fields and click on the "Connect" button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/azure-m-new-1.png' />

After the connection, the connected instances will appear on the new repository adding screen as follows.

<Screenshot url='https://cdn.appcircle.io/docs/assets/azure-m-last-1.png' />

Additionally, when we click on an instance, we can see it here with the name we gave it.

<Screenshot url='https://cdn.appcircle.io/docs/assets/azure-m-new-2.png' />

:::caution
The instance name for each Git provider must be unique.

For example, if you create an instance named "Instance" for Azure DevOps Server, you cannot reconnect an instance named "Instance" for Azure DevOps Server.

However, you can connect an instance with that name for GitLab or Bitbucket Server.
:::

### Connection Settings for Multiple Instances

When we connect a repository using PAT (Personal Access Token) on multiple instances, you can use the "Connection Settings" button to view the PAT information and change the PAT information if there is a previously defined connection.

When we connect a repository using PAT over multiple instances, User Email and PAT list appears in the "Connection Settings".

<Screenshot url='https://cdn.appcircle.io/docs/assets/connection-settings-main-3.png' />

:::caution
In order to change the Personal Access Token (PAT), you must have provided more than one connection for the same Git provider. If you have more than one connection, you can switch between PATs.
:::

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />
