---
title: Connecting to Bitbucket
description: Learn how to connect to Bitbucket in Appcircle
tags: [source code management, bitbucket, bitbucket self-hosted]
sidebar_position: 3
slug: /build/manage-the-connections/connection-guides/connecting-to-bitbucket
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';
import NeedHelp from '@site/docs/\_need-help.mdx';

# Connecting to Bitbucket

If you authorize Appcircle to access your repositories on Bitbucket, you can select the repository that you want to connect in the next screen.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-repoconnect1.png' />

After you click on **Bitbucket**, the following screen will appear. This will let you choose between selecting a repository that you are already authorized to do with Appcircle or asking your consent about authorizing more repositories.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE7873-bitbucket1.png' />

When you successfully authorize your account, the following screen will appear to let you select one for connection:

<Screenshot url='https://cdn.appcircle.io/docs/assets/connect-repository-bitbucket-gitlab.png' />

After the connection is successful, you can [view your newly created profile](/build/build-process-management/profile-creation#profile-listing) and start building!

## Connecting to Bitbucket Cloud Repository

To connect to a Bitbucket Cloud repository, you can choose from the following connection types:

- **OAuth2 Connection**  
Click **Get Repositories from Bitbucket Cloud (OAuth2)** to authorize Appcircle using your Bitbucket Cloud credentials. This provides secure and seamless integration.

- **App Password - User** (Deprecated)
  Choose this to authenticate using your Bitbucket username and an [App Password](https://support.atlassian.com/bitbucket-cloud/docs/app-passwords/). You will need to provide:

    - Connection Name
    - Bitbucket Server URL (e.g., `https://bitbucket.org`)
    - Username
    - App Password

:::caution

Bitbucket has replaced **App Passwords** with **API Tokens**. However, existing App Passwords can still be used until mid-2026. For more information, please refer to the [official Bitbucket documentation](https://support.atlassian.com/bitbucket-cloud/docs/api-tokens/).

:::

- **API Token - User**
  Choose this to authenticate using your Bitbucket username and an [API Tokens](https://support.atlassian.com/bitbucket-cloud/docs/api-tokens/). You will need to provide:

    - Connection Name
    - Bitbucket Server URL (e.g., `https://bitbucket.org`)
    - Email Address
    - API Token

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6369-bucket2.png' />

- **Access Tokens - Repo**  
  Use a repository-specific token for limited-scope access to individual repositories.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6369-bucket3.png' />

### OAuth2, App Password (Deprecated) and Access Token Permissions for Bitbucket Cloud Integration

The following table details the OAuth permissions required for Appcircle to connect with Bitbucket. These permissions grant read access to projects, repositories, pull requests, and webhooks, ensuring proper functionality when integrating with Bitbucket via OAuth2, App Password and Access Token. 

| Scope        | Permission   | Description                                                                                                                                                               |
|--------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Account      | Email        | Provides access to view the user's primary email address.                                                                                                                 |
| Project      | Read         | Provides access to view the projects the user has access to view. Read access (repository) to all the repositories in the projects is also granted.                       |
| Repository   | Read         | Provides access to view all the repositories the user has access to view, including the source code, Issues, and Wiki. This does not include pull requests.               |
| Pull Request | Read         | Provides access to view and list pull requests on the repositories the user has access to view. This permission (scope) also allows the user to create and resolve tasks. |
| Webhooks     | Read & Write | Needed for enabling Appcircle triggers through webhook operations.                                                                                                        |

### API Token Permissions for Bitbucket Cloud Integration

The following table details the API Token permissions required for Appcircle to connect with Bitbucket. These permissions grant read access to projects, repositories, pull requests, and webhooks, ensuring proper functionality when integrating with Bitbucket via API Token.

- While creating an API Token, select the **Create API Token with scopes**, then choose **Bitbucket Application** as the API Token App.

| Scope                      | Description                                                                                                                                                               |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| read:account               | Provides access to view the user's primary email address.                                                                                                                 |
| read:project:bitbucket     | Provides access to view the projects the user has access to view. Read access (repository) to all the repositories in the projects is also granted.                       |
| read:repository:bitbucket  | Provides access to view all the repositories the user has access to view, including the source code, Issues, and Wiki. This does not include pull requests.               |
| read:pullrequest:bitbucket | Provides access to view and list pull requests on the repositories the user has access to view. This permission (scope) also allows the user to create and resolve tasks. |
| read:webhook:bitbucket     | Needed for enabling Appcircle triggers through webhook operations.                                                                                                        |
| write:webhook:bitbucket    | Needed for enabling Appcircle triggers through automaticly creating webhooks.                                                                                             |
| delete:webhook:bitbucket   | Needed for enabling Appcircle triggers through removing automaticly created webhooks.                                                                                     |


## Connecting to Bitbucket Server (Self-Hosted) Repository

The overall process is similar with a private repository connection through SSH, but Appcircle allows connections to self-hosted Bitbucket servers via HTTP Access Tokens.

:::caution

Bitbucket's version must be **7.14** or higher.

:::

1. Select **Bitbucket** > **HTTP Access Token - User** or **HTTP Access Token - Repo** based on your token type.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE7873-bitbucket1.png' />

2. Fill in the connection form with:
  - Connection Name
  - Bitbucket Server URL
  - Username
  - HTTP Access Token

If you are not sure what those are, contact your system administrator.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6369-bucket4.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6369-bucket5.png' />

:::info

Appcircle requires admin-level access to automatically create the necessary webhooks. After the webhooks are successfully created, the associated access token can be safely downgraded to read access.

:::

:::caution Connection Notice

For Appcircle to connect to the self-hosted Bitbucket instance, your connection must be reachable over the internet.

:::

Is your self-hosted Bitbucket instance under an enterprise firewall? Learn which IP addresses and ports Appcircle uses to function under the whitelist documentation:

<ContentRef url="/build/manage-the-connections/accessing-repositories-in-internal-networks-firewalls">
  Accessing Repositories in Internal Networks (Firewalls)
</ContentRef>

### Token Creation

Bitbucket has **Personal Access Token** to authorize the user. Relevant guide:

https://confluence.atlassian.com/bitbucketserver/personal-access-tokens-939515499.html

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4940-bitbucket.png' />

:::info

Appcircle needs admin permission to function properly. The admin permission is needed to create relevant WebHooks automatically.

:::

:::danger

Bitbucket doesn't allow scoped repository permissions like GitHub. Therefore the token you add can access all the repositories of the token's owner. When you're adding a token, it's better to create a new bot user or a project and give access to only the required repositories for build to succeed.

:::

### Check Token

You can follow the steps below to check if your token is valid.

- Open the terminal and issue the following command

```bash
curl --user name:password http://YOUR_BITBUCKET_HOST/rest/api/1.0/repos
```

Above command should print out your projects. If you don't see an output, please check your token and Bitbucket address.

:::caution

Please also make sure that the output doesn't show any reference to `localhost`. If you see `localhost`, you need to configure Bitbucket and put the correct address of your Bitbucket instance.

:::

<NeedHelp />
