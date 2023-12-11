---
title: Using the Connections
metaTitle: Using the Connections
metaDescription: Using the Connections
sidebar_position: 11
---

import Screenshot from '@site/src/components/Screenshot';

# Connections

The Connections page is a feature where we can check and edit the connections of the Git providers we are connected to. You can access this page from the left bar in the Build module.

On this page, you can view **OAuth** and **PAT** (Personal Access Token) connections.

<Screenshot url='https://cdn.appcircle.io/docs/assets/connections-all-main.png' />

:::info
If you have not previously connected to a Git provider on Appcircle, i.e., created a profile and not connected a repository, you will not see any connection on this page.
:::

## Managing OAuth Connections

### Revoke OAuth Connections

**Revoke Token** revokes the token of the Git provider on the Appcircle side. On the Git provider side, the token is still active and available. Appcircle cannot revoke the token from the provider.

<Screenshot url='https://cdn.appcircle.io/docs/assets/connections-oauth-revoke.png' />

A revoked connection disconnects all build profiles connected to the respective Git provider. In this case, Appcircle shows a clear warning message. Here, you can see all the affected profiles.

<Screenshot url='https://cdn.appcircle.io/docs/assets/connections-revoke-modal.png' />

When we revoke a Git provider successfully, the "Revoke Token" button disappears. If we reconnect using the **Refresh Token** button, the "Revoke Token" button will appear again.

<Screenshot url='https://cdn.appcircle.io/docs/assets/connections-revoked.png' />

:::info
If we open one of the affected build profiles after applying a revoke for a Git provider, we should see the disconnected build profile state in the UI.

If we reconnect this profile, not only the related build profile but also all other build profiles belonging to that Git provider will be connected.
:::

### Reconnect OAuth Connections

If we want to reconnect to the Git provider, we can use the **Refresh Token** button.

The `refresh token` is received while connecting to the Git provider, and it's used when needed, for instance, in reconnection or token expiration cases.

<Screenshot url='https://cdn.appcircle.io/docs/assets/connections-reconnect.png' />

The refreshing connection action reconnects all previously linked and disconnected build profiles of the corresponding Git provider in Appcircle. Here again, all affected build profiles will be shown.

<Screenshot url='https://cdn.appcircle.io/docs/assets/connections-reconnect-modal.png' />

When the **Refresh Token** button is clicked, Appcircle redirects to the relevant Git provider's page. After giving the necessary permissions there, the connection will be restored.

:::info
If the connection to the Git provider is active and the **Refresh Token** button is clicked, Appcircle will re-establish the connection.
:::

## Managing PAT Connections

The PAT field lists the profiles we connect with.

<Screenshot url='https://cdn.appcircle.io/docs/assets/connections-pat-main.png' />

:::info
The list first shows the logo of the Git provider we're connecting to, then the name we gave to the profile or connection (when multiple instances are used), and finally the URL of the Git provider we're connecting to.
:::

### Editing PAT Connections
We can see the details of the PAT connection with the **Edit** button on the right side. These are **Provider**, **Instance URL**, **Token Owner**, **Token**, and **PAT**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/connections-pat-detail.png' />

In the edit screen, we can change the PAT (Personal Access Token) value. However, we must make sure that the value we change here is correct and that it was created by the Git provider. Otherwise, the affected profile or profiles will not be connected.

<Screenshot url='https://cdn.appcircle.io/docs/assets/connections-pat-edit.png' />

:::caution
In the Edit screen, you can see the profiles where PAT is used under "Affected Build Profiles". Changing a PAT value will affect all profiles shown here.
:::

:::tip
When editing PAT connections, you can also write the PAT value using environment variables. You can review [Using Environment Variables For SSH And PAT (Personal Access Token) Connections of the Git Provider](../environment-variables/managing-variables.md#using-environment-variables-for-ssh-and-pat-personal-access-token-connections-of-the-git-provider) page.
:::