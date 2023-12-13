---
title: Disconnect, Reconnect And Change Connection From Build Profile
metaTitle: Disconnect, Reconnect And Change Connection From Build Profile
metaDescription: Disconnect, Reconnect And Change Connection From Build Profile
sidebar_position: 12
---

import Screenshot from '@site/src/components/Screenshot';

You can see the connection details by clicking the **"Connection Settings"** button in the build profile.

<Screenshot url='https://cdn.appcircle.io/docs/assets/connections-new-main.png' />

Different types of connections have different connection details in the connection settings.

### OAuth Connection

For an OAuth connection, the details will be **"Provider"**, **"Token Owner"**, **"Code"**, **"Expire Access Token Date"**, **"Expire Refresh Token Date"**, **"Refresh Token"**, and **"Token"**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/connection-last-1n.png' />

### PAT Connection

For a PAT (personal access token) connection, the details will be **"Token Owner"**, and **"Personal Access Token"**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/connection-last-3n.png' />

:::info
In this section, you can view the PATs you have previously added, if any, and change them profile-specific.

You only need to make sure that the modified token has the required authorizations for the relevant repository.
:::

## Disconnect Profile

You can disconnect the relevant profile from the Git provider with the “Disconnect” button in this window. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/disconnect-1.png' />

If you click the “Disconnect” button in this window, Appcircle will bring up a warning screen:

<Screenshot url='https://cdn.appcircle.io/docs/assets/disconnect-2.png' />

And then Appcircle will bring us a screen to quickly reconnect the profile:

<Screenshot url='https://cdn.appcircle.io/docs/assets/disconnect-3.png' />

If you do not want to connect again at that moment, you can do so later by clicking the "Reconnect" button next to the "Connections Settings" icon.

<Screenshot url='https://cdn.appcircle.io/docs/assets/reconnect-button.png' />


:::info
If you disconnect a profile, only that profile is disconnected from the Git provider. And if you link a profile again, only the relevant profile link will be provided again.
:::

:::caution
If the Revoke Token transaction is made for the Git provider from the connections page and a reconnection is made from a previously added profile through this Git provider, all profiles connected through the relevant Git provider are reconnected.
:::

## Change Provider and Reconnect

Appcircle allows changing the Git provider when reconnecting a profile that has been disconnected.
For example, if a repository connected via GitHub is now on GitLab, you can select the Git provider by clicking the "Reconnect" button next to the "Connection Settings" icon.

<Screenshot url='https://cdn.appcircle.io/docs/assets/reconnect-button.png' />

When clicking the "Reconnect" button within a disconnected profile, Appcircle will display the Git providers and SSH connection method screen. Here you can select the Git provider you want to change or the SSH connection method regardless of the Git provider:

<Screenshot url='https://cdn.appcircle.io/docs/assets/change-provider.png' />

For example, if this project on GitLab is now accessed via GitHub, Github is selected from the list and the login process is performed on GitHub. Once the operations are completed, the Git provider returns the page to the Appcircle profile page and the repository selection window opens:

<Screenshot url='https://cdn.appcircle.io/docs/assets/repo-select.png' />

After the save, the repository will be linked through the new Git provider.

<Screenshot url='https://cdn.appcircle.io/docs/assets/repo-success-c.png' />

:::tip
When changing Git provider the connection method will not matter. SSH connection method can be used when changing the Git provider of a project connected via OAuth method.
:::

:::caution
When changing Git provider, your old builds, tests, configurations, workflows, triggers and branch list will not be deleted. Only the remaining branches from the old connection in your branch list will be collected below and the new branches will appear at the top.
:::