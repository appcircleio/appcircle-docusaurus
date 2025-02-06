---
title: Connection Management
description: Learn how to manage connections in Appcircle
tags: [build, manage, connections]
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';

## Connection Settings

You can see the connection details by clicking the **"Connection Settings"** button in the build profile.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-management1.png' />

Different types of connections have different connection details in the connection settings.

### OAuth Connection

For an OAuth connection, the details will be **"Provider"**, **"Token Owner"**, **"Code"**, **"Expire Access Token Date"**, **"Expire Refresh Token Date"**, **"Refresh Token"**, and **"Token"**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-management2.png' />

### PAT Connection

For a PAT (personal access token) connection, the details will be **"Token Owner"**, and **"Personal Access Token"**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/connection-last-3n.png' />

:::info
In this section, you can view the PATs you have previously added, if any, and change them profile-specific.

You only need to make sure that the modified token has the required authorizations for the relevant repository.
:::

## Disconnect Build Profile

You can disconnect the build profile from the Git provider by using the **Disconnect** button below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-management3.png' />

When you click on the "Disconnect" button, Appcircle will bring up a warning dialog box for confirmation.

<Screenshot url='https://cdn.appcircle.io/docs/assets/disconnect-2.png' />

When we open a disconnected build profile, Appcircle will bring us a popup to quickly **Reconnect** build the profile.

<Screenshot url='https://cdn.appcircle.io/docs/assets/disconnect-3.png' />

If you do not want to connect again at that moment, you can do it later by clicking the "Reconnect" button next to the "Connection Settings".

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-management5.png' />

:::info
If you disconnect a build profile, only that build profile is disconnected from the Git provider.

When you reconnect a build profile again, only the relevant build profile will be connected again.
:::

:::caution
On the other hand, connection operations done from the **[Connections](/build/manage-the-connections)** page affect all relevant build profiles using those connections.
:::

## Change Git Provider and Reconnect

Appcircle allows changing the Git provider while reconnecting a profile that has been disconnected.

For example, assume that a build profile was previously connected to GitLab and then its Git repository had been moved to GitHub. In this case, you can select the new Git provider for that build profile by clicking the "Reconnect" button next to "Connection Settings".

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-management5.png' />

Appcircle will display the Git providers and "Connect via SSH" connection options in a selectable list.

Here you can select the Git provider you want to change or the "Connect via SSH" method regardless of the Git provider.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-management4.png' />

Once the connection operations are completed, the Git provider redirects to the Appcircle build profile with the repository selection window.

<Screenshot url='https://cdn.appcircle.io/docs/assets/repo-select.png' />

After you select the relevant Git repository and "Save", the build profile will be connected to the new Git provider.

<Screenshot url='https://cdn.appcircle.io/docs/assets/repo-success-c.png' />

:::caution
After changing the Git provider and reconnecting the repository, you can use the existing branches that are also available in the new repository. When you try to **Start Build** with these branches, you should see the up-to-date "Commit ID" from the new repository.

Unavailable branches from the old repository connection will be inactive. You can see them in the branch list, but Appcircle does not allow building with the branches that do not exist in the new repository. These kinds of branches will be unusable.
:::

:::tip
While switching from one connection to another type of connection, the older connection method is not important.

You can select one of the listed options and switch to that one without considering anything about the previous one.
:::

:::info
While changing the Git provider, your previous builds, tests, configurations, workflows, triggers, and branch list will not be deleted.
:::

## Change Owner

The **token owner** of a build profile can now be changed without the need to create a new build profile on Appcircle. The **Change Owner** button in the build profile **Connection** detail will help you change the connection ownership so that you can resolve the broken connections or misconfigured repository authorization cases easily by yourself.

:::info
To use this feature, the user must have previously connected to the relevant Git provider on Appcircle via [OAuth](/build/manage-the-connections/reconnect-change-provider#managing-oauth-connections).
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

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-management6.png' />

## Managing OAuth Connections

### Revoke OAuth Connections

**Revoke Token** revokes the token of the Git provider on the Appcircle side. On the Git provider side, the token is still active and available. Appcircle cannot revoke the token from the provider.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-con1.png' />

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

Now you're ready to use the added PAT connection in your build profiles. While making a new connection, you can see the PAT connection in the available connections list after selecting the Git provider.

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

You can review [Using Environment Variables For SSH And PAT (Personal Access Token) Connections](/build/build-environment-variables#using-environment-variables-for-ssh-and-pat-personal-access-token-connections-of-the-git-provider) page for details.
:::

### Deleting PAT Connections

You can delete a Personal Access Token (PAT) connection by clicking on the **Delete** next to the respective entry in your list of PAT connections.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3112-deletepat.png' />

Upon clicking the **Delete** button, Appcircle will prompt you to enter the name of the PAT Connection to confirm the deletion operation. After entering the connection name, simply click **Delete** on the pop-up screen.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3112-deletepat2.png' />

:::warning
If you have an existing Build profile that would be affected by the deletion of the PAT Connection, Appcircle will display a warning message listing the affected builds.

You will need to disconnect them before you can delete the PAT connection.

For more information about disconnecting a build profile please refer to the related [documentation](/build/manage-the-connections/reconnect-change-provider#disconnect-build-profile).
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3112-deletepat3.png' />
