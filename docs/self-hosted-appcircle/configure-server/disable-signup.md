---
title: Disable Signup
metaTitle: Disable Signup
metaDescription: Disable Signup
sidebar_position: 5
---

# Overview

After enabling LDAP or SSO settings, it is recommended to disable the signup function on the server to ensure a centralized user management system.

This prevents unauthorized access and maintains control over user authentication.

Disabling the signup function eliminates the risk of unauthorized user registrations and enforces the use of authenticated accounts through LDAP or SSO integration.

To do that, can you change the `.keycloak.enabledRegistration` setting in the `global.yaml` file

```yaml
keycloak:
  enabledRegistration: false
```

To apply the changes, please follow these steps:

- Down the server

```bash
/ac-self-hosted.sh -n "spacetech" down
```

- Export the updated global.vaml

```bash
/ac-self-hosted.sh -n "spacetech" export
```

- Up the server

```bash
/ac-self-hosted.sh -n "spacetech" up
```

After the server is up and healthy, when you click `Sign up with e-mail` button, you should see
`Registration not allowed` page

:::info
You can login to the dashboard with your initial user after disabling signup.
:::
