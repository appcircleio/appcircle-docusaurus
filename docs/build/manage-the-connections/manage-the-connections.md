---
title: Manage the Connections
description: The Connections page is a feature where we can check and edit the connections of the Git providers we are connected to.
tags: [build, connections, git providers, oauth, pat, personal access token]
sidebar_position: 11
---

import Screenshot from '@site/src/components/Screenshot';

# Connections

The Connections page is a feature where we can check and edit the connections of the Git providers we are connected to. You can access this page from the left bar in the Build module.

On this page, you can view **OAuth** and **PAT** (Personal Access Token) connections.

<Screenshot url='https://cdn.appcircle.io/docs/assets/connections-all-main-new.png' />

:::info
If you have not previously connected to a Git provider on Appcircle, i.e., created a profile and not connected a repository, you will not see any connection on this page.
:::

## Managing OAuth Connections

### Revoke OAuth Connections

**Revoke Token** revokes the token of the Git provider on the Appcircle side. On the Git provider side, the token is still active and available. Appcircle cannot revoke the token from the provider.

<Screenshot url='https://cdn.appcircle.io/docs/assets/connections-oauth-revoke-new.png' />

A revoked connection disconnects all build profiles connected to the respective Git provider. In this case, Appcircle shows a clear warning message. Here, you can see all the affected profiles.

<Screenshot url='https://cdn.appcircle.io/docs/assets/connections-revoke-modal.png' />

When we revoke a Git provider successfully, the "Revoke Token" button disappears. If we reconnect using the **Refresh Token** button, the "Revoke Token" button will appear again.

<Screenshot url='https://cdn.appcircle.io/docs/assets/connections-revoked-new.png' />

:::info
If we open one of the affected build profiles after applying a revoke for a Git provider, we should see the disconnected build profile state in the UI.

If we reconnect this profile, not only the related build profile but also all other build profiles belonging to that Git provider will be connected.
:::

### Reconnect OAuth Connections

If we want to reconnect to the Git provider, we can use the **Refresh Token** button.

The `refresh token` is received while connecting to the Git provider, and it's used when needed, for instance, in reconnection or token expiration cases.

<Screenshot url='https://cdn.appcircle.io/docs/assets/connections-reconnect-new.png' />

The refreshing connection action reconnects all previously linked and disconnected build profiles of the corresponding Git provider in Appcircle. Here again, all affected build profiles will be shown.

<Screenshot url='https://cdn.appcircle.io/docs/assets/connections-reconnect-modal.png' />

When the **Refresh Token** button is clicked, Appcircle redirects to the relevant Git provider's page. After giving the necessary permissions there, the connection will be restored.

:::info
If the connection to the Git provider is active and the **Refresh Token** button is clicked, Appcircle will re-establish the connection.
:::

## Managing PAT Connections

The PAT connection list section on the right-hand side has a list of connections that were made using a personal access token.

<Screenshot url='https://cdn.appcircle.io/docs/assets/connections-main-pat-new.png' />

The list first shows the logo of the Git provider we're connecting to, then the name we gave to the connection (when multiple instances are used), and finally the URL of the Git provider we're connecting to.

### Adding PAT Connection

The "Add New" button at the top of the PAT connection list on the right side allows us to add PAT (Personal Access Token) without creating a new build profile. Then you can use that PAT connection on existing build profiles or while adding a new build profile.

<Screenshot url='https://cdn.appcircle.io/docs/assets/add-new-main.png' />

After clicking on the "Add New" button, Appcircle will ask us to select a Git provider and fill in the necessary information according to the Git provider, just like in the build profile PAT connection.

<Screenshot url='https://cdn.appcircle.io/docs/assets/connections-select-provider.png' />

:::info
The name you defined in the **Connection Name** section must be unique for each Git provider.

For example, if you have created a PAT named "my-secret-pat" for GitHub, you cannot create another PAT with the same name for GitHub.

But you can create a PAT named "my-secret-pat" for GitLab or Bitbucket, for instance.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/connections-fill-provider-new-1.png' />

:::info
In Azure DevOps Server connections, the **Owner Username** field on Appcircle corresponds to the **Collection Name** on Azure.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/connection-success-pat.png' />

Now you're ready to use the added PAT connection in your build profiles. While making a new connection, you can see the PAT connection in the available connections list after selecting Git provider.

### Editing PAT Connections

We can see the details of the PAT connection with the **Edit** button on the right side. These are **Provider**, **Instance URL**, **Token Owner**, **Token**, and **PAT**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/connections-pat-detail.png' />

In the **Connection Edit**, we can change the PAT (Personal Access Token) value.

However, we must make sure that the value we change here is correct and that it was created on the Git provider correctly. Otherwise, the affected build profile or profiles will not be connected.

<Screenshot url='https://cdn.appcircle.io/docs/assets/connections-pat-edit.png' />

:::caution
In the **Connection Edit**, you can see the build profiles where PAT is used under "Affected Build Profiles".

Changing a PAT value will affect all the build profiles shown here.
:::

:::tip
While editing PAT connections, you can also write the PAT value using environment variables.

You can review [Using Environment Variables For SSH And PAT (Personal Access Token) Connections](/environment-variables/managing-variables#using-environment-variables-for-ssh-and-pat-personal-access-token-connections-of-the-git-provider) page for details.
:::
