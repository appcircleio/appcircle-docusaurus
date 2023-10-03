---
title: 'Connecting to Multiple Instance'
metaTitle: 'Multiple Instances Using Git Providers (Bitbucket, Gitlab, Azure)'
metaDescription: 'Multiple Instances Using Git Providers (Bitbucket, Gitlab, Azure)'
---

import ContentRef from '@site/src/components/ContentRef';

### Multiple Instances Using Git Providers (Bitbucket, Gitlab, Azure)

Multiple connection features have been introduced for connections made with PAT (Personnel Access Token) on Bitbucket, Azure, or Gitlab. Thus, it is possible to add Bitbucket, Azure, or Gitlab servers located in different environments by a single user.

For example, the same user can connect to two different instances, such as dev1.azure.campaignname.com and
We can also give it to dev2.azure.campaignname.com.

Similar examples are dev1.gitlab.campaignname.com and dev2.gitlab.campaignname.com or dev.bitbucket.campaignname.com and prod.bitbucket.campaignname.com.

:::caution
In order to use this feature, it is necessary to create a PAT on the provider.
:::

If we give a connection example for Azure,

First of all, we select the relevant Git provider from the add new repository screen.

![](<https://cdn.appcircle.io/docs/assets/azure-m-repo.png>)

Then click on the "Connect to an Azure DevOps Server" button in the window that opens;

![](<https://cdn.appcircle.io/docs/assets/azure-m-repo-1.png>)

In the next window, fill in the relevant fields and click on the "Connect" button.

![](<https://cdn.appcircle.io/docs/assets/azure-m-repo-2.png>)

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />