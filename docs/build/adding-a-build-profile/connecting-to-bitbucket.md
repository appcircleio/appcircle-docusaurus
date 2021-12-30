---
title: 'Connecting to Bitbucket'
metaTitle: 'Connecting to Bitbucket'
metaDescription: 'Connecting to Bitbucket'
---

import ContentRef from '@site/src/components/ContentRef';

# Connecting to Bitbucket

## Connecting to bitbucket.com

If you authorize Appcircle to access your repositories on BitBucket, you can select the repository that you want to connect in the next screen.

![](<https://cdn.appcircle.io/docs/assets/image (239).png>)

After you click on **Bitbucket**, the following screen will appear. This will let you choose between selecting a repository which you are already authorized Appcircle to do or ask your consent about authorizing more repositories.

![](<https://cdn.appcircle.io/docs/assets/image (234).png>)

When you successfully authorize your account, the following screen will appear to let you select one for connection:

![](<https://cdn.appcircle.io/docs/assets/image (236).png>)

After the connection is successful, you can [view your newly created profile](./README.md#view-the-newly-created-build-profile) and start building!

## Connecting to Bitbucket Self Hosted Repository

Overall process is similar with private repository connection through SSH, but Appcircle allows to directly connect through Bitbucket Self Hosted URL.

First, select **Bitbucket **and\*\* **then **Connect Self-hosted Bitbucket\*\* through the menu:

![](<https://cdn.appcircle.io/docs/assets/image (229).png>)

Fill the relevant information about your Bitbucket self-hosted module. If you are not sure what those are, contact your system administrator.

![](<https://cdn.appcircle.io/docs/assets/image (230).png>)

:::caution

### Connection Notice

For Appcircle to connect to the Self Hosted GitLab Instance, your connection must be reachable over the internet.&#x20;

:::

Is your self-hosted GitLab instance under enterprise firewall? Learn which IP addresses and ports Appcircle uses to function under the whitelist documentation:

<ContentRef url="../../infrastructure/accessing-repositories-in-internal-networks-firewalls">
  Accessing Repositories in Internal Networks (Firewalls)
</ContentRef>

### Token Creation

Bitbucket has **Personal Access Token** to authorize the user. Relevant guide:

https://confluence.atlassian.com/bitbucketserver/personal-access-tokens-939515499.html

:::info

Appcircle needs admin permission to function properly. The admin permission is needed to create relevant WebHooks automatically.

:::

#### Authorizing a Distinct Repository Through Bitbucket

Bitbucket provides SSH option to authorize a single repository. However, this method of connection is unavailable within Appcircle.
