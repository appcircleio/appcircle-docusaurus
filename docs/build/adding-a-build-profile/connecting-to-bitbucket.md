---
title: 'Connecting to Bitbucket'
metaTitle: 'Connecting to Bitbucket'
metaDescription: 'Connecting to Bitbucket'
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';
import NeedHelp from '@site/docs/\_need-help.mdx';

# Connecting to Bitbucket

## Connecting to bitbucket.com

If you authorize Appcircle to access your repositories on BitBucket, you can select the repository that you want to connect in the next screen.

<Screenshot url='https://cdn.appcircle.io/docs/assets/main-connection.png' />

After you click on **Bitbucket**, the following screen will appear. This will let you choose between selecting a repository which you are already authorized Appcircle to do or ask your consent about authorizing more repositories.

<Screenshot url='https://cdn.appcircle.io/docs/assets/main-connection-bt.png' />

When you successfully authorize your account, the following screen will appear to let you select one for connection:

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (236).png' />

After the connection is successful, you can [view your newly created profile](./#view-the-newly-created-build-profile) and start building!

## Connecting to Bitbucket Self Hosted Repository

Overall process is similar with private repository connection through SSH, but Appcircle allows to directly connect through Bitbucket Self Hosted URL.

:::caution

Bitbucket's version must be **7.14** or higher.

:::

First, select **Bitbucket** then **Connect to a Bitbucket Server** through the menu:

<Screenshot url='https://cdn.appcircle.io/docs/assets/bt-connect-self.png' />

Fill the relevant information about your Bitbucket self-hosted module. If you are not sure what those are, contact your system administrator.

<Screenshot url='https://cdn.appcircle.io/docs/assets/bt-self-hosted-detail.png' />

:::caution

### Connection Notice

For Appcircle to connect to the Self Hosted Bitbucket Instance, your connection must be reachable over the internet.

:::

Is your self-hosted Bitbucket instance under enterprise firewall? Learn which IP addresses and ports Appcircle uses to function under the whitelist documentation:

<ContentRef url="/infrastructure/accessing-repositories-in-internal-networks-firewalls">
  Accessing Repositories in Internal Networks (Firewalls)
</ContentRef>

### Token Creation

Bitbucket has **Personal Access Token** to authorize the user. Relevant guide:

https://confluence.atlassian.com/bitbucketserver/personal-access-tokens-939515499.html

:::info

Appcircle needs admin permission to function properly. The admin permission is needed to create relevant WebHooks automatically.

:::

:::warning

Bitbucket doesn't allow scoped repository permissions like GitHub. Therefore the token you add can access all the repositories of the token's owner. When you're adding a token, it's better to create a new bot user or a project and give access to only the required repositories for build to succeed. 

:::

You may create access token to specific project or a repository which can help you to restrict the access level of the token.

### Create HTTP access tokens for projects or repositories
HTTP access tokens can be created for teams to grant permissions at the project or repository level rather than for specific users.

To create an HTTP access token for a project or repository (requires project or repository admin permissions):

- From either the Project or Repository settings, select HTTP access tokens.
- Select Create token.
- Set the token name, permissions, and expiry.


### Check Token

You can follow the steps below to check if your token is valid. 

- Open the terminal and issue the following command

```bash
curl --user name:password http://YOUR_BITBUCKET_HOST/rest/api/1.0/repos
```

Above command should print out your projects. If you don't see an output, please check your token and Bitbucket address. 

:::caution

Please also make sure that the output doesn't show any reference to `localhost`. If you see `localhost`,  you need to configure Bitbucket and put the correct address of your Bitbucket instance.

:::


<NeedHelp />
