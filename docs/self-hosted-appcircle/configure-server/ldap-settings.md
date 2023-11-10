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

## Appcircle Login with LDAP

Appcircle Login with LDAP aims to provide an alternative authentication solution via the LDAP server. Appcircle's LDAP integration allows businesses to integrate existing directory services, especially Active Directory, directly into the Appcircle login process. This integration simplifies user management.

The LDAP distinguished name (DN) is associated with existing Appcircle registered users when:
- The existing user signs in to Appcircle with LDAP for the first time.
- The LDAP email address is the email address of an existing Appcircle user. If the LDAP email attribute isn’t found in the Appcircle user database, a new user is created.

If an existing Appcircle user wants to enable LDAP sign-in for themselves, they should:
- Check that their Appcircle user email address matches their LDAP user email address.
- Sign in to Appcircle by using their LDAP credentials.

:::caution
This feature only provides a solution for self-hosted applications.
:::

#### Attribute Configuration Settings

LDAP users must have an email address, regardless of whether or not it’s used to sign in. 

Appcircle uses these LDAP attributes to create an account for the LDAP user. The specified attribute can be either:
- The attribute Username LDAP Attribute as a string. For example,'mail'.

|Settings|Description|Requried|Examples|
|----------|-----------|----------|-----------|
|Username LDAP Attribute|Name of LDAP attribute, which is mapped as username. For many LDAP server vendors it can be 'uid'. For Active directory it can be 'sAMAccountName' or 'cn'.|Yes|mail,email|

### Adding LDAP Configuration

- To get started, click on the Admin button from the left menu.

![](https://cdn.appcircle.io/docs/assets/ldap-1.png)

- Go to the Self-Hosted Settings screen.

![](https://cdn.appcircle.io/docs/assets/ldap-2.png)

- And press the Connect button next to LDAP Login.

![](https://cdn.appcircle.io/docs/assets/ldap-3.png)

- Click on the Create button to create your LDAP.

![](https://cdn.appcircle.io/docs/assets/ldap-4.png)

- Enter the details of your LDAP configurations.

![](https://cdn.appcircle.io/docs/assets/ldap-5.png)

:::caution
After configuring LDAP, to test the configuration use the from adding LDAP config page bottom "Test" buttons.
:::

![](https://cdn.appcircle.io/docs/assets/ldap-8.png)

:::info
Appcircle supports multiple LDAP configurations. If you are using multiple LDAP configurations and a user exists in both LDAPs, user authentication will look at the LDAP order. The "Order" field when adding a LDAP configuration is required to do this ordering. A LDAP configuration with an order value of 1 will be used before a LDAP configuration with an order value of 2 in user authentication.
:::

![](https://cdn.appcircle.io/docs/assets/ldap-9.png)

### Appcircle Login Page Settings

In this area, you can manage the creation of new users using the "Sign up by email" button and the renewal of passwords using the "Forgot password" button.

#### User Registration

If this setting is on, your users can register to Appcircle and perform operations with this user except LDAP management. If you want only your LDAP users to log in to the system, you need to keep this setting off.

![](https://cdn.appcircle.io/docs/assets/ldap-6.png)

:::info
If this setting is off, the "Sign up by email" button will not appear on the Appcircle login page.
:::

#### Forgot Password

If this setting is on, your users can renew their passwords themselves. If you want your users' password management operations to be done via LDAP, you should keep this setting off.

![](https://cdn.appcircle.io/docs/assets/ldap-7.png)

:::info
If this setting is off, the "Forgot Password" button will not appear on the Appcircle login page.
:::

### Remove User From LDAP Server

If the user is deleted via LDAP, users coming from LDAP or previously connected users cannot log in to the system. And users who are logged in are automatically logged out.

# Remove LDAP Configuration

You can quickly remove your saved LDAP configuration via Appcircle. For this

- To delete a LDAP configuration, press the "Manage" button next to the LDAP Login option on the Self-Hosted Settings page.

![](https://cdn.appcircle.io/docs/assets/ldap-10.png)

- In the window that opens, select the LDAP configuration you want to delete and click on the "Remove" button. After confirmation, the LDAP configuration will be deleted from Appcircle.

![](https://cdn.appcircle.io/docs/assets/ldap-11.png)

:::info
When a user on LDAP is deleted, the user can no longer log in to Appcircle. If a user logged in to Appcircle with a LDAP configuration is removed from the LDAP configuration, the user will not be able to register in Appcircle. This user is also removed from the corporate organization in Appcircle.
:::

## Troubleshooting

:::info
If the LDAP configuration is incorrect or cannot be accessed, they can log in with the initial users.
:::

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />