---
title: Disconnect, Reconnect, Change Connection and Change Owner From Build Profile
metaTitle: Disconnect, Reconnect, Change Connection and Change Owner From Build Profile
metaDescription: Disconnect, Reconnect, Change Connection and Change Owner From Build Profile
sidebar_position: 12
---

import Screenshot from '@site/src/components/Screenshot';

## Connection Settings

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

## Disconnect Build Profile

You can disconnect the build profile from the Git provider by using the **Disconnect** button below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/disconnect-1.png' />

When you click on the "Disconnect" button, Appcircle will bring up a warning dialog box for confirmation.

<Screenshot url='https://cdn.appcircle.io/docs/assets/disconnect-2.png' />

When we open a disconnected build profile, Appcircle will bring us a popup to quickly **Reconnect** build the profile.

<Screenshot url='https://cdn.appcircle.io/docs/assets/disconnect-3.png' />

If you do not want to connect again at that moment, you can do it later by clicking the "Reconnect" button next to the "Connection Settings".

<Screenshot url='https://cdn.appcircle.io/docs/assets/reconnect-button.png' />

:::info
If you disconnect a build profile, only that build profile is disconnected from the Git provider.

When you reconnect a build profile again, only the relevant build profile will be connected again.
:::

:::caution
On the other hand, connection operations done from the **[Connections](./connections.md)** page affect all relevant build profiles using those connections.
:::

## Change Git Provider and Reconnect

Appcircle allows changing the Git provider while  reconnecting a profile that has been disconnected.

For example, assume that a build profile was previously connected to GitLab and then its Git repository had been moved to GitHub. In this case, you can select the new Git provider for that build profile by clicking the "Reconnect" button next to "Connection Settings".

<Screenshot url='https://cdn.appcircle.io/docs/assets/reconnect-button.png' />

Appcircle will display the Git providers and "Connect via SSH" connection options in a selectable list.

Here you can select the Git provider you want to change or the "Connect via SSH" method regardless of the Git provider.

<Screenshot url='https://cdn.appcircle.io/docs/assets/change-provider.png' />

Once the connection operations are completed, the Git provider redirects to the Appcircle build profile with the repository selection window.

<Screenshot url='https://cdn.appcircle.io/docs/assets/repo-select.png' />

After you select the relevant Git repository and "Save", the build profile will be connected to the new Git provider.

<Screenshot url='https://cdn.appcircle.io/docs/assets/repo-success-c.png' />

:::caution
After changing the git provider and reconnecting the repository, Appcircle does not allow build with old branches in the branch list. Old branches will be unusable.
:::

:::tip
While switching from one connection to another type of connection, the older connection method is not important.

You can select one of the listed options and switch to that one without considering anything about the previous one.
:::

:::info
While changing the Git provider, your previous builds, tests, configurations, workflows, triggers and branch list will not be deleted.
:::

## Change Owner

The **token owner** of a build profile can now be changed without the need to create a new build profile on Appcircle. The **Change Owner** button in the build profile **Connection** detail will help you change the connection ownership so that you can resolve the broken connections or misconfigured repository authorization cases easily by yourself.

:::info
To use this feature, the user must have previously connected to the relevant Git provider on Appcircle via [OAuth](connections.md#managing-oauth-connections).
:::

:::info
The build profile owners will not see the **Change Owner** button in the **Connection** detail for their build profiles.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/owner-main.png' />

When you browse the same build profile with a different member within the same organization, the **Change Owner** button will be visible in the window that's opened when we click on the **Connection Settings** button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/owner-modal.png' />

After clicking on the **Change Owner** button and giving approval on the confirmation screen that appears, the process of taking token ownership of the build profile connection will begin.

<Screenshot url='https://cdn.appcircle.io/docs/assets/owner-warning.png' />

:::caution
The connection ownership change will be permitted for users who are in the same organization (team members) and have **Manager** role in the **build profile** scope.

In addition, the user who wants to take ownership of the connection must also have access to the repository on the relevant Git provider.
:::

When the process is completed successfully, you can click on the **Connection Settings** button again to see the changed ownership of the build profile connection. In the window that's opened, there won't be a **Change Owner** button because you are now the profile owner.

<Screenshot url='https://cdn.appcircle.io/docs/assets/owner-changed.png' />
