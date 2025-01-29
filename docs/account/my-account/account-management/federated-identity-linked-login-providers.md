---
title: Federated Identity Management
description: Learn how to manage the linked accounts for login in Appcircle
tags: [account, account management, federated identity, linked login providers]
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';

# Federated Identity Management

In this screen, you can manage the linked accounts for login. You can link a new account by pressing **Add **and following the permission prompts displayed by the provider or you can disconnect an account by pressing **Remove**.

For login, Appcircle does not ask for any additional permissions other than the email address. Multiple providers can be linked to a single account, but only a single account can be linked from each provider.

If you signed up with an identity provider, you need to set a password to login with email before you can disconnect that linked account.

:::info

Identity providers linked for login purposes are managed independently from the accounts linked for repository connections. (i.e. Disconnecting GitHub or Bitbucket from My Account does not break the repository connections.)

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/myaccount-federated-identities.png' />

###
