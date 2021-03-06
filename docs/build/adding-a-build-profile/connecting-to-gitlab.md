---
title: 'Connecting to GitLab'
metaTitle: 'Connecting to GitLab'
metaDescription: 'Connecting to GitLab'
---

import ContentRef from '@site/src/components/ContentRef';

# Connecting to GitLab

## Connecting to gitlab.com

If you authorize Appcircle to access your repositories on GitLab, you can select the repository that you want to connect in the next screen.

![](<https://cdn.appcircle.io/docs/assets/image (238).png>)

After you click on **GitLab**, the following screen will appear. This will let you choose between selecting a repository which you are already authorized Appcircle to do or ask your consent about authorizing more repositories.

![](<https://cdn.appcircle.io/docs/assets/image (235).png>)

When you successfully authorize your account, the following screen will appear to let you select one for connection:

![](<https://cdn.appcircle.io/docs/assets/image (236).png>)

After the connection is successful, you can [view your newly created profile](./README.md#view-the-newly-created-build-profile) and start building!

## Connecting to GitLab Self Hosted Repository

Overall process is similar with private repository connection through SSH, but Appcircle allows to directly connect through GitLab Self Hosted URL.

First, select **GitLab **and\*\* **then **Connect Self-hosted GitLab\*\* through the menu:

![](<https://cdn.appcircle.io/docs/assets/image (242).png>)

Fill the relevant information about your Gitlab self-hosted module. If you are not sure what those are, contact your system administrator.

![](<https://cdn.appcircle.io/docs/assets/image (243).png>)

:::caution

### Connection Notice

For Appcircle to connect to the Self Hosted GitLab Instance, your connection must be reachable over the internet.

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

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />
