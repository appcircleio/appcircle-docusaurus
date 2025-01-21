---
title: Connecting to GitLab
description: Learn how to connect to GitLab repositories in Appcircle
tags: [gitlab, connection, repository, self-hosted, token, access, firewall, ip, port]
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

After the connection is successful, you can [view your newly created profile](/build/build-process-management#profile-listing) and start building!

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

- `my.appcircle.spacetech.com`

then, for default server configuration, the `api` domain should be

- `api.appcircle.spacetech.com`

:::

:::caution

### Connection Notice

For Appcircle to connect to the Self Hosted GitLab Instance, your connection must be reachable over the network.

:::

Is your self-hosted GitLab instance under enterprise firewall? Learn which IP addresses and ports Appcircle uses to function under the whitelist documentation:

<ContentRef url="/build/manage-the-connections/accessing-repositories-in-internal-networks-firewalls">
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

### Webhook SSL Verification

When integrating GitLab with your self-hosted Appcircle server using HTTPS, webhooks are sent securely over an encrypted connection (HTTPS). To establish this connection, GitLab must trust the SSL certificate of your Appcircle server. This requires the GitLab to trust the SSL certificate of the Appcircle server.

If you encounter a "self-signed certificate in certificate chain" error during integration, you have two options to resolve the issue:

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2983-self-signed-error.png' />

#### 1. Trust the SSL Certificate (recommended)

To establish a secure connection between your self-hosted Appcircle server and the GitLab server, you need to trust either the SSL certificate of the Appcircle server or the issuer certificate of the  server's certificate in your GitLab configuration.

For detailed instructions on how to install custom public certificates and configure trust in GitLab, refer to GitLab's documentation: [Install Certificates](https://docs.gitlab.com/omnibus/settings/ssl/#install-custom-public-certificates).

#### 2. Disable the SSL verification (not recommended)

Alternatively, you can choose to disable SSL verification for your AppCircle server's webhook connection in GitLab. While this means that GitLab will not attempt to validate the certificate, it is important to note that webhooks will still be sent over an encrypted HTTPS connection but in an insecure way.

:::caution
This approach can create security vulnerabilities such as man-in-the middle attacks.
:::

Take the following steps to disable the SSL verification of the webhook:

1. Go to the Git repository that you have connected to the Appcircle.
2. Open the webhook settings of that Git repository.
3. Click on the **Edit** button next to the webhook.
4. Scroll down to see the **SSL verification** setting.
5. De-select the **Enable SSL verification** checkbox.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2983-disable-ssl-verification.png' />

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />
