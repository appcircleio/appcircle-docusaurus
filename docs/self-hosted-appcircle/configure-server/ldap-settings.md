---
title: LDAP Settings
metaTitle: LDAP Lookup Decision Settings
metaDescription: LDAP Lookup Decision Settings
sidebar_position: 8
---

## User Lookup Decision Settings

The LDAP (Lightweight Directory Access Protocol) user lookup decision strategy is a crucial aspect of user authentication in applications that utilize LDAP for user management.

When Appcircle receives a user login request from the Enterprise App Store or Testing Distribution, it needs to determine which LDAP configuration to use for the user lookup and authentication process.

In scenarios where a user exists in multiple LDAP configurations, a decision must be made on which configuration to use for authentication.

This documentation provides insights into the LDAP user lookup decision strategy and how it can be configured to handle scenarios where a user has multiple usernames and passwords across different LDAP configurations.

### Editing User Lookup Decision Strategy

To configure LDAP lookup decision settings, you can follow the steps below.

:::info

We're assuming that previously you reviewed or followed [install self-hosted appcircle](../install-server/docker.md#3-configure) section in docs and applied example scenario.

Following steps are using example project as project naming, which was told there.

:::

- Go to the Appcircle server directory.

```bash
cd appcircle-server
```

- Edit the `global.yaml` of the project.

```bash
vi projects/spacetech/global.yaml
```

- Find the keycloak entry and add the `userLookupDecisionStrategy` entry to it. For example;

```yaml
keycloak:
  initialUsername: admin@spacetech.com
  enabledRegistration: true
  userLookupDecisionStrategy: affirmative
```

:::info
The `userLookupDecisionStrategy` variable can have two options: `affirmative` or `decisive`.

If you don't define it or it has an unknown value, it is assumed to be `decisive` by default.

#### Affirmative

When `userLookupDecisionStrategy` is set to "affirmative", the LDAP authentication process will check all LDAP settings, even if the user is found on a particular LDAP configuration. This means that if a user has multiple accounts on different LDAP configurations with different passwords, they will be able to login successfully. The authentication system will search across all LDAP configurations to find a matching username or email and validate the user's password, allowing the user to access the system.

#### Decisive

On the other hand, when `userLookupDecisionStrategy` is set to "decisive", the LDAP authentication process will check a specific LDAP configuration for the user's username or email. If the authentication system finds the username on a particular LDAP, it will verify the user's password only on that specific LDAP configuration. If the provided password is incorrect, the authentication system will not check other LDAP configurations and will immediately return invalid credentials, denying access to the user.

:::

### Applying Changes

After you configure the `global.yaml` of the project, you should restart the Appcircle server for the settings to take effect.

- Stop the server.

```bash
./ac-self-hosted.sh -n "spacetech" down
```

- Apply the configuration changes.

```bash
./ac-self-hosted.sh -n "spacetech" export
```

- Start the server.

```bash
./ac-self-hosted.sh -n "spacetech" up
```

- Check the health of the services.

```bash
./ac-self-hosted.sh -n "spacetech" check
```

You should see the message: _"All services are running successfully."_

### Testing the LDAP Auth

#### 1. Configure multiple LDAPs on server

Ensure that multiple LDAP settings are properly configured on your Appcircle server's [integration settings](../../account/sso-ldap-login.md).

#### 2. Create users with the same username

In each of the configured LDAPs, create user accounts with the same username but different passwords.

For example, you can create users with the username "spacetechuser" in both LDAP configurations, each with unique passwords.

This setup will mimic the scenario where a user has multiple accounts on different LDAPs.

#### 3. Test LDAP authentication with users

Use the "spacetechuser" credentials to attempt a login to the application. For example, enterprise app store or testing distribution

The `affirmative` LDAP authentication strategy will kick in during this test.

#### Verification

If the "spacetechuser" provides the correct password that matches the user's credentials in one of the configured LDAPs, the authentication system will grant access to the Enterprise App Store or Testing Distribution profile.

The `affirmative` strategy ensures that the authentication process checks all LDAP configurations to find a matching username and validate the user's password.

If the "spacetechuser" provides an incorrect password that does not match the user's credentials in any of the LDAP configurations, the authentication process will continue checking all the other LDAPs.

If it finds a matching username with the correct password in any of the other LDAP configurations, the user will be granted access.
