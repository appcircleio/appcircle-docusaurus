---
title: Login Configuration
metaTitle: Login Configuration
metaDescription: Disable Signup or Reset Password
sidebar_position: 5
---

import Screenshot from '@site/src/components/Screenshot';

## Overview

Self-hosted Appcircle server `3.9.0` or later versions support enabling or disabling "User Registration" and "Forgot Password" from the "Self-Hosted Settings" admin page.

If your organization has configured LDAP or SSO authentication for the Appcircle users, you may want to disable the email signup flow.

Allowing email signup could result in having users registered both through LDAP/SSO and through email.

This can create duplicate users and make user management more difficult. Disabling email signup ensures all users are created through your centralized LDAP or SSO provider, avoiding duplication.

Just keep in mind that disabling email signup means new users will need to be created directly in your LDAP or SSO provider first before they can sign in to Appcircle.

Disabling email signup also prevents unwanted or unknown users from signing up for accounts through the email flow.

With LDAP or SSO, only users explicitly added to those systems can gain access, keeping tighter control over who can login to Appcircle.

Also, keeping the forgotten password flow open allows users to reset their password. But keep in mind that if a user resets his or her password, the user will no longer be an LDAP user.

It will be better to disable forgotten password flow after you enable LDAP or SSO for authentication.

## Login Settings

In this area, you can manage the creation of new users using the "Sign up with e-mail" button and the renewal of passwords using the "Forgot Password?" button.

You can reach "Login Settings" by navigating to "Admin > Self-Hosted Settings" page.

### User Registration

If this setting is `on`, your users can register to Appcircle and perform operations with this user except LDAP or other authentication methods. If you want only your LDAP users to log in to the system, you need to keep this setting `off`.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-6.png' />

Click on the "Save button to apply the settings.

:::info
If this setting is `off`, the "Sign up with e-mail" button will not appear on the Appcircle login page.
:::

### Forgot Password

If this setting is `on`, your users can renew their passwords themselves. If you want your users' password management operations to be done via LDAP or other authentication methods, you should keep this setting `off`.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-7.png' />

Click on the "Save" button to apply the settings.

:::info
If this setting is `off`, the "Forgot Password?" button will not appear on the Appcircle login page.
:::

### Enable / Disable User Registration With Disposable Emails

With the Appcircle server version `v3.13.0`, Appcircle disables users from registering with disposable (temporary) emails and common emails like Gmail, Outlook, etc. by default.

If you want to change this behavior, you can configure it in the `global.yaml` file of your project by following the steps below.

:::caution
Keep in mind that this action will cause a downtime in the Appcircle dashboard.
:::

- Log in to Appcircle server with SSH or remote connection.

- Go to the `appcircle-server` directory.

```bash
cd appcircle-server
```

:::info

The `spacetech` in the example codes below are example project name.

Please find your own project name and replace `spacetech` with your project name.

To see projects, you can check the `projects` directory.

```bash
ls -l ./projects
```

:::

- Shutdown Appcircle server.

```bash
./ac-self-hosted.sh -n "spacetech" down
```

- Edit the `global.yaml` file of your project.

```bash
vi ./projects/spacetech/global.yaml
```

- Find the `keycloak` key and append the `allowDisposableEmails` key into that section.

The **allowDisposableEmails** key can be `true` or `false`. `false` is the default value, so it disables users from registering with disposable or common emails.

If you want to enable disposable or common emails, change this value to `true`.

You can see a sample part of a configured `global.yaml` below.

```yaml
keycloak:
  initialUsername: admin@spacetech.com
  enabledRegistration: true
  allowDisposableEmails: true
```

- Apply configuration changes.

```bash
./ac-self-hosted.sh -n "spacetech" export
```

- Boot Appcircle server.

```bash
./ac-self-hosted.sh -n "spacetech" up
```

:::tip
You should check the status of the Appcircle server after boot for any possible errors.

```bash
./ac-self-hosted.sh -n "spacetech" check
```

You should see the message: _"All services are running successfully."_

:::

Now, the users can register with disposable or common emails.

If you want to re-disable that behavior, as in the default configuration, you can change the **allowDisposableEmails** value to `false` by following the same steps above.
