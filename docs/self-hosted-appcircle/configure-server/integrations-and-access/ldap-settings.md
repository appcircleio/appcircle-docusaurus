---
title: LDAP Settings
metaTitle: LDAP Lookup Decision Settings
metaDescription: LDAP Lookup Decision Settings
sidebar_position: 9
---

import Screenshot from '@site/src/components/Screenshot';

## User Lookup Decision Settings

The LDAP (Lightweight Directory Access Protocol) user lookup decision strategy is a crucial aspect of user authentication in applications that utilize LDAP for user management.

When Appcircle receives a user login request from the Enterprise App Store or Testing Distribution, it needs to determine which LDAP configuration to use for the user lookup and authentication process.

In scenarios where a user exists in multiple LDAP configurations, a decision must be made on which configuration to use for authentication.

This documentation provides insights into the LDAP user lookup decision strategy and how it can be configured to handle scenarios where a user has multiple usernames and passwords across different LDAP configurations.

### Editing User Lookup Decision Strategy

To configure LDAP lookup decision settings, you can follow the steps below.

:::info

We're assuming that previously you reviewed or followed [install self-hosted appcircle](/self-hosted-appcircle/install-server/docker#3-configure) section in docs and applied example scenario.

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

Ensure that multiple LDAP settings are properly configured on your Appcircle server's [integration settings](/account/my-organization/ldap-login).

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

Appcircle login with LDAP aims to provide an alternative authentication solution via the LDAP server. Appcircle's LDAP integration allows businesses to integrate existing directory services, especially Active Directory, directly into the Appcircle login process. This integration simplifies user management.

The LDAP distinguished name (DN) is associated with existing Appcircle registered users when:

- The existing user signs in to Appcircle with LDAP for the first time.
- The LDAP email address is the email address of an existing Appcircle user.

If the LDAP email attribute isn’t found in the Appcircle user database, a new user is created.

If existing Appcircle users want to enable LDAP to sign in for themselves, they should:

- Check that their Appcircle user email address matches their LDAP user email address.
- Sign in to Appcircle by using their LDAP credentials.

:::caution
This feature only provides a solution for self-hosted Appcircle server installations. Appcircle Login with LDAP is not possible for Appcircle Cloud users.
:::

### Attribute Configuration Settings

LDAP users must have an email address, regardless of whether or not it’s used to sign in.

Appcircle uses these LDAP attributes to create an account for the LDAP user.

- The username LDAP attribute is a string. For example,'mail'.

| Settings                | Description                                                                                                                                                     | Required | Examples   |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ---------- |
| Username LDAP Attribute | Name of LDAP attribute, which is mapped as username. For many LDAP server vendors it can be 'uid'. For an active directory, it can be 'sAMAccountName' or 'cn'. | Yes      | mail,email |

### Adding LDAP Configuration

- To get started, click on the "Admin" button from the left menu.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-1.png' />

- Go to the "Self-Hosted Settings" screen.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-2.png' />

- And press the "Connect" button next to "LDAP Login".

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-3.png' />

- Click on the "Create" button to create your LDAP configuration.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-4.png' />

- Enter the details of your LDAP configuration.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-5.png' />

:::caution
After you fill out the LDAP configuration form, it's strongly recommended that you test the configuration using the test buttons below.

- Test Connection
- Test Authentication

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-8.png' />

:::info
Appcircle supports multiple LDAP configurations. If you are using multiple LDAP configurations and a user exists in both LDAPs, user authentication will look at the LDAP order.

The "Order" field when adding a LDAP configuration is required to do this ordering.

LDAP configuration with an order value of `1` will be used before LDAP configuration with an order value of `2` in user authentication.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-9.png' />

### Remove User From LDAP Server

If the user is deleted via LDAP, users coming from LDAP or previously connected users cannot log in to the system. And users who are logged in are automatically logged out.

### Remove LDAP Configuration

You can quickly remove your saved LDAP configuration from Appcircle Login.

- To delete a LDAP configuration, press the "Manage" button next to the "LDAP Login" option on the "Self-Hosted Settings" page.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-10.png' />

- Select the LDAP configuration you want to delete and click on the "Remove" button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-11.png' />

After confirmation, the LDAP configuration will be deleted from Appcircle.

:::info
If a user is logged in to Appcircle with an LDAP configuration and that LDAP configuration is removed, the user will not be able to register in Appcircle.

This user is also removed from the organization in Appcircle.
:::

## Troubleshooting

:::info
If the LDAP configuration is incorrect or the LDAP server cannot be accessed for some reason, you can always login with the "initial username" and "initial password" that were configured while installing the server.

See the [configure](/self-hosted-appcircle/install-server/docker#3-configure) section in the installation page for the `global.yaml` details.
:::

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />
