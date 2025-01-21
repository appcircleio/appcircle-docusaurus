---
title: Connecting to GitHub
description: Learn how to connect your GitHub repositories to Appcircle
tags: [build profile, connection, github]
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';
import NeedHelp from '@site/docs/\_need-help.mdx';

# Connecting to GitHub

If you authorize Appcircle to access your repositories on GitHub, you can select the repository that you want to connect in the next screen.

If you are a part of an organization, you can also connect your organization's repositories too. To grant Appcircle permission to access the repositories of an organization, you need to have the necessary privileges at the organization level. For GitHub, you have to provide selective access to specific repositories.

In such a case, only the selected repositories will be listed. To be able to view other repositories, you must grant access for them under the Applications section in the account/organization settings screen on GitHub. You can directly access this screen by clicking on the **Missing a repository? Grant access from GitHub**.

:::info

For connection to GitHub, Appcircle uses GitHub App instead of GitHub OAuth. GitHub App is more secure and newer way implemented by GitHub to external apps to communicate within GitHub in a better fashion.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/main-connection.png' />

After you click on **GitHub**, the following screen will appear. This will let you choose between selecting a repository which you are already authorized Appcircle to do or ask your consent about authorizing more repositories.

<Screenshot url='https://cdn.appcircle.io/docs/assets/github-main.png' />

When you successfully authorize your repository or repositories, the following screen will appear to let you select one for connection:

<Screenshot url='https://cdn.appcircle.io/docs/assets/connect-repository-github.png' />

After the connection is successful, you can [view your newly created profile](/build/build-process-management#profile-listing) and start building!

## FAQ

### Unable to grant access to a GitHub organization

If you are unable to grant access to a specific organization while connecting to GitHub, it is likely that the permission for Appcircle needs an update from the organization application access settings.

To resolve, go to Organization Settings ->Third-party access and press edit next to Appcircle to authorize it for the organization.

<NeedHelp />
