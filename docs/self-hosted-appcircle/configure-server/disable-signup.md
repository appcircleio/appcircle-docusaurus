---
title: Disable Sign Up
metaTitle: Disable Sign Up
metaDescription: Disable Sign Up
sidebar_position: 5
---

# Overview

After [enabling SSO](../../account/sso/single-sign-on.md#enable-sso) settings for Appcircle CI/CD login, it is recommended to disable the sign-up function on the server to ensure a centralized user management system.

This also improves security and maintains control over user authentication.

Disabling the sign-up function eliminates the risk of unauthorized user registrations and enforces the use of authenticated accounts through SSO integration.

:::caution
Please be aware that in order to disable or enable the signup button again, you must **`reset`** your application data.
:::

To do that, can you follow the steps below:

- Change the `.keycloak.enabledRegistration` setting in the `global.yaml` file.

```yaml
keycloak:
  enabledRegistration: false
```

:::info

We're assuming that previously you reviewed or followed [install self-hosted appcircle](../install-server/docker.md#3-configure) section in docs and applied example scenario.

Following steps are using example project as project naming, which was told there.

:::

To apply the changes, please follow these steps:

- Stop the server

```bash
./ac-self-hosted.sh -n "spacetech" down
```

- Reset the Appcircle Server

:::caution
Be aware that all of your application data, including your build profile and application configurations, will be **deleted** when you run **`reset`** command.
:::

```bash
./ac-self-hosted.sh -n "spacetech" reset
```

- Apply configuration changes

```bash
./ac-self-hosted.sh -n "spacetech" export
```

- Start the server

```bash
./ac-self-hosted.sh -n "spacetech" up
```

After the server is up and healthy, when you click the `Sign up with e-mail` button, you should see
`Registration not allowed` page.

:::info
You can login to the dashboard with your initial user after disabling the sign-up.
:::
