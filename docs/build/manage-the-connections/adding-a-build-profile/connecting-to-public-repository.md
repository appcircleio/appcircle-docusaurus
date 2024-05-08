---
title: Connecting to Public Repository
description: Learn how to connect to a public repository in Appcircle
tags: [build profile, connection, public repository]
sidebar_position: 5
---

import Screenshot from '@site/src/components/Screenshot';

# Connecting to Public Repository

Since public repositories doesn't require any authentication or connection, the actions that can be taken with public repositories are limited. You will only have read only access towards the specified repository. Only use public repositories if you plan to use the profile for:

- Testing & Previewing Appcircle
- Benchmarking build times to see how fast we are 🚀
- Not planning to use the profile for long term

#### Using a Git Provider?

If your repository is located under these providers, Appcircle has built-in support to automatically connect and do the automated work for you. All you need to do is click on the appropriate button in the profile setup page (image below).

For more information on your provider, see the links below:

- [Github](/build/manage-the-connections/adding-a-build-profile/connecting-to-github)
- [Bitbucket](/build/manage-the-connections/adding-a-build-profile/connecting-to-bitbucket)
- [GitLab](/build/manage-the-connections/adding-a-build-profile/connecting-to-gitlab)

#### Using a Private Git Server?

If you plan to use Appcircle to connect your private repository, please refer to [connecting to private repositories documentation](/build/manage-the-connections/adding-a-build-profile/connecting-to-private-repository-via-ssh) for more information.

### Public Repository Connection

When you enter the profile after the build, the following screen will appear. Click on **Connect via URL** to connect a public repository.

:::tip

Clicking **Quick start using the sample repository **will also connect the relevant sample project with public connection.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/main-connection.png' />

After you click on **Connect via URL**, the following screen will appear and let you enter an URI

<Screenshot url='https://cdn.appcircle.io/docs/assets/connect-via-url.png' />

Enter the URL of your repository, or continue with sample project if you plan to preview Appcircle.

:::tip

Public connection refers to the HTTP(s) connection by Git Providers. SSH links in public repositories are not accepted.

:::

After the connection is successful, you can [view your newly created profile](/build/manage-the-connections/adding-a-build-profile/#view-the-newly-created-build-profile) and start building!

:::info

### Webhook Events

Keep in mind that certain hook events **will not work** with a public connection.

:::

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />
