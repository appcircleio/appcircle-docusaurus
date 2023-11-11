---
title: 'Connecting to Multiple Instances'
metaTitle: 'Multiple Instances Using Git Providers (Bitbucket, GitLab, Azure DevOps)'
metaDescription: 'Multiple Instances Using Git Providers (Bitbucket, GitLab, Azure DevOps)'
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

<Screenshot url='https://cdn.appcircle.io/docs/assets/azure-m-repo.png' />

Then click on the "Connect to an Azure DevOps Server" button in the window that opens.

<Screenshot url='https://cdn.appcircle.io/docs/assets/azure-m-repo-1.png' />

In the next window, fill in the relevant fields and click on the "Connect" button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/azure-m-new.png' />

After the connection, the connected instances will appear on the new repository adding screen as follows.

<Screenshot url='https://cdn.appcircle.io/docs/assets/azure-m-last.png' />

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />