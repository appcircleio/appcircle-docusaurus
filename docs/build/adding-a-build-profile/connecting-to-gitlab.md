---
title: 'Connecting to GitLab'
metaTitle: 'Connecting to GitLab'
metaDescription: 'Connecting to GitLab'
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

# Connecting to GitLab

## Connecting to gitlab.com

If you authorize Appcircle to access your repositories on GitLab, you can select the repository that you want to connect in the next screen.

<Screenshot url='https://cdn.appcircle.io/docs/assets/main-connection.png' />

After you click on **GitLab**, the following screen will appear. This will let you choose between selecting a repository which you are already authorized Appcircle to do or ask your consent about authorizing more repositories.

<Screenshot url='https://cdn.appcircle.io/docs/assets/gitlab-main.png' />

When you successfully authorize your account, the following screen will appear to let you select one for connection:

<Screenshot url='https://cdn.appcircle.io/docs/assets/connect-repository-bitbucket-gitlab.png' />

After the connection is successful, you can [view your newly created profile](./#view-the-newly-created-build-profile) and start building!

## Connecting to GitLab Self Hosted Repository

Overall process is similar with private repository connection through SSH, but Appcircle allows to directly connect through GitLab Self Hosted URL.

:::caution

GitLab's version must be **13.12.9** or higher.

:::

First, select **GitLab** and then **Connect to a Self-Managed GitLab Instance** through the menu:

<Screenshot url='https://cdn.appcircle.io/docs/assets/gitlab-self-hosted2.png' />

Fill the relevant information about your GitLab self-hosted module. If you are not sure what those are, contact your system administrator.

<Screenshot url='https://cdn.appcircle.io/docs/assets/gitlab-self-detail.png' />

:::caution

### Outbound Requests

When you connect to a GitLab repository by creating a profile on Appcircle, Appcircle tries to create webhooks on the GitLab repository.

If your Appcircle server has a local IP address like `10.10.140.20`, you may get an error while connecting to the repository.

To solve this issue, the IP or the Appcircle API subdomain name should be allowed for outbound requests on the GitLab admin panel.

You can follow the steps below to update outbound requests:

1. You must get access to the **Admin Area** of the GitLab server.
2. Expand the "Settings" button at the bottom left.
3. Click on the "Network" button to access network settings.
4. Expand the "Outbound" requests.
5. Add the IP address or the `api` subdomain of the Appcircle server.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2545-sample-configuration.png' />

For example, if you are accessing to the Appcircle server dashboard via

- `my.appcircle.spacetech.com`,

then, for default server configuration, the `api` domain should be

- `api.appcircle.spacetech.com`

:::

:::caution

### Connection Notice

For Appcircle to connect to the Self Hosted GitLab Instance, your connection must be reachable over the network.

:::

Is your self-hosted GitLab instance under enterprise firewall? Learn which IP addresses and ports Appcircle uses to function under the whitelist documentation:

<ContentRef url="/infrastructure/accessing-repositories-in-internal-networks-firewalls">
  Accessing Repositories in Internal Networks (Firewalls)
</ContentRef>

### Token Creation

GitLab has two kinds of token at their Self Hosted instance:

- [Personal Access Token](https://docs.gitlab.com/ee/security/token_overview.html#personal-access-tokens)
- [Project Access Token](https://docs.gitlab.com/ee/security/token_overview.html#project-access-tokens)

Both works to connect your repository through Appcircle. That being said, **Project Access Token **is used to authorize a single project(repository) and **Personal Access Token **is used to authorize every repository the user has access to.

:::info

Appcircle needs admin permission to function properly. The admin permission is needed to create relevant WebHooks automatically.

:::

### Check Token

You can follow the steps below to check if your token is valid.

- Open the terminal and issue the following command

```bash
curl "http://YOUR_GITLAB_HOST/api/v4/projects?private_token=YOUR_TOKEN"
```

Above command should print out your projects. If you don't see an output, please check your token and GitLab address.

:::caution

Please also make sure that the output doesn't show any reference to `localhost`. If you see `localhost`, you need to configure GitLab and put the correct address of your GitLab instance.

:::

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />
