---
title: Using The Connections
metaTitle: Using The Connections
metaDescription: Using The Connections
sidebar_position: 11
---

import Screenshot from '@site/src/components/Screenshot';

# Connections

The Connections page is a feature where we can check and edit the connections of the Git providers we are connected to. You can access this page from the left bar in the Builds module.

On this page, you can view **OAuth** and **PAT** (Personal Access Token) connections.

<Screenshot url='https://cdn.appcircle.io/docs/assets/connections-all-main.png' />

:::info
If you have not previously linked to a Git provider on Appcircle, i.e., created a profile and linked a repository, no link will appear on this page.
:::

## Managing OAuth Connections

### Revoke OAuth Connections

Revoke Token revokes the token from the Git provider on the Appcircle side. On the provider side, the token is still active and available. Appcircle cannot revoke the token from the provider.

<Screenshot url='https://cdn.appcircle.io/docs/assets/connections-oauth-revoke.png' />

A revoked Git connection disconnects all profiles connected to the respective provider. For this, Appcircle shows a warning screen. Here you can see all affected profiles.

<Screenshot url='https://cdn.appcircle.io/docs/assets/connections-revoke-modal.png' />

When we cancel a Git provider, the cancel button is now removed. When reconnecting using the Refresh Token button, the Revoke Token button will be active again.

<Screenshot url='https://cdn.appcircle.io/docs/assets/connections-revoked.png' />

:::caution
If we open one of the affected profiles after applying for a revoke for a Git provider, the profile's Appcircle shows us that the profile is nonconnected. If we reconnect this profile, not only the related project but also all other profiles belonging to this Git provider will be connected. 
:::

### Reconnect OAuth Connections

If we want to reconnect to the Git provider, we can use the refresh token button. The refresh token is received when connecting to the Git provider and is used as needed (reconnecting, token expiration).

<Screenshot url='https://cdn.appcircle.io/docs/assets/connections-reconnect.png' />

Refresh reconnects all previously linked and disconnected profiles of the corresponding Git provider in Appcircle. Here again, all affected profiles are shown.

<Screenshot url='https://cdn.appcircle.io/docs/assets/connections-reconnect-modal.png' />

After clicking the Refresh Token button, Appcircle will redirect us to the relevant Git provider's page. After giving the necessary permissions there, the connection will be restored.

:::info
If the connection to the Git provider is active and the Refresh Token button is clicked, Appcircle will re-establish the connection.
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
When editing PAT connections, you can also write the PAT value using environment variables. You can see how to use environment variables on this page.
:::