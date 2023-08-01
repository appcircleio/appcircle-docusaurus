---
title: LDAP Settings
metaTitle: LDAP Lookup Decision Settings
metaDescription: LDAP Lookup Decision Settings
sidebar_position: 8
---

## LDAP Lookup Decision Settings

The LDAP (Lightweight Directory Access Protocol) user lookup decision strategy is a crucial aspect of user authentication in applications that utilize LDAP for user management.

When Appcircle receives a user login request from Enterprise App Store or Tester Distribution, it needs to determine which LDAP configuration to use for the user lookup and authentication process.

In scenarios where a user exists in multiple LDAP configurations, a decision must be made on which configuration to use for authentication.

This documentation provides insights into the LDAP user lookup decision strategy and how it can be configured to handle scenarios where a user has multiple usernames and passwords across different LDAP configurations.

## Configure Appcircle Server

To configure LDAP lookup decision settings, you can follow the steps below:

:::caution

Change the `spacetech` values below with the project name you want to configure.

:::

- Go to the Appcircle server directory.

```bash
cd appcircle-server
```

- Edit the global.yaml of the project

```bash
vi ./projects/spactech/global.yaml
```

- Find the keycloak entry and add `userLookupDecisionStrategy` to it:

```yaml
---
keycloak:
  initialUsername: admin@spacetech.com
  initialPassword: Spacetech123!
  enabledRegistration: true
  userLookupDecisionStrategy: affirmative
---
```

:::info
The `userLookupDecisionStrategy` variable can have two options: `affirmative` or `decisive`.

If you don't define it, it is `decisive` by default.

Affirmative: When userLookupDecisionStrategy is set to affirmative, the LDAP authentication process will check all LDAP settings, even if the user is found on a particular LDAP configuration. This means that if a user has multiple accounts on different LDAP configurations with different passwords, the user will be able to login successfully. The authentication system will search across all LDAP configurations to find a matching username or email and validate the user's password, allowing the user to access the system.

Decisive: On the other hand, when userLookupDecisionStrategy is set to decisive, the LDAP authentication process will check a specific LDAP configuration for the user's username or email. If the authentication system finds the username on a particular LDAP, it will verify the user's password only on that specific LDAP configuration. If the provided password is incorrect, the authentication system will not check other LDAP configurations and will immediately return invalid credentials, denying access to the user.

:::

## Restart The Appcircle Server

After you configured the `global.yaml` of the project, you should restart your Appcircle server for the settings to take effect.

- Down the server:

```bash
./ac-self-hosted.sh -n "spacetech" down
```

- Export the new configured settings:

```bash
./ac-self-hosted.sh -n "spacetech" export
```

- Up the server back:

```bash
./ac-self-hosted.sh -n "spacetech" up
```

- Check the health of server:

```bash
./ac-self-hosted.sh -n "spacetech" check
```

## Test LDAP Auth

### Configure Multiple LDAPs:

Ensure that multiple LDAP settings has properly configured on your Appcircle server's integration settings.

### Create Users with Same Username:

In each of the configured LDAPs, create user accounts with the same username but different passwords.

For example, you can create users with the username "spacetech" in both LDAP configurations, each having unique passwords.

This setup will mimic the scenario where a user has multiple accounts on different LDAPs.

### Test Authentication:

Use the "spacetech" credentials to attempt a login to the application.

The affirmative LDAP authentication strategy will kick in during this test.

### Verification:

If the "spacetech" provides the correct password that matches the user's credentials in one of the configured LDAPs, the authentication system will grant access to the Enterprise App Store or Distribution UI.

The affirmative strategy ensures that the authentication process checks all LDAP configurations to find a matching username and validate the user's password.

If the "spacetech" provides an incorrect password that does not match the user's credentials in any of the LDAP configurations, the authentication process will continue checking all the other LDAPs.

If it finds a matching username with a correct password in any of the other LDAP configurations, the user will be granted access.
