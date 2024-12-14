---
title: LDAP Configuration
description: Learn how to configure LDAP configuration
tags: [self-hosted, helm, configuration, kubernetes]
sidebar_position: 80
---

import NeedHelp from '@site/docs/\_need-help.mdx';

## Overview

You can see some options for the LDAP configurations in this documentation.

## LDAP Brute Force Protection

Enabling LDAP authentication introduces the risk of brute-force attacks that can originate from external or internal sources.

A sustained LDAP brute-force attack can result in user accounts being locked out of the LDAP directory, preventing access to other applications integrated with the directory.

To mitigate this risk, a self-hosted Appcircle server can be configured to block repeated failed login attempts for a duration before allowing additional attempts.

The Appcircle server's brute-force algorithm is based on successive failed attempts, not failed attempts over a period of time.

### Default Configuration

Appcircle server comes with brute-force protection **turned off** by default.

It is completely up to you to set this up. See the following sections for details.

### Brute-Force Arguments

The appropriate blocking threshold and duration are dependent on the account lockout policies enforced on the LDAP server itself.

For example, if the LDAP server locks accounts for 1 hour after 10 failed attempts, Appcircle can be configured to block login attempts for 2 hours after 5 failures to provide an early warning system.

So the users won't be blocked by the LDAP server and can continue to use other applications.

Follow the recommendations below when tuning the brute-force protection mechanisms:

- Review the number of failed login attempts that trigger account lockout and the lockout duration configured on your LDAP server.

- Configure the Appcircle server's maximum retry attempts equal to or lower than your LDAP server's threshold. For example, if LDAP locks accounts after 10 failed logins, set the Appcircle server to block after 5-8 attempts.

- Configure Appcircle's lockout duration to be equal to or greater than LDAP. For instance, if LDAP locks accounts for 1 hour, Appcircle should be 1 hour or more.

- Test updated configurations in a non-production environment first. Validate that the Appcircle server lockouts are triggered before LDAP lockouts when deliberately failing logins.

- Monitor logs for incidents blocked by the Appcircle server to optimize configurations based on real activity targeting your environment.

Following these best practices will allow the Appcircle server to effectively function as an early warning system for brute-force attacks against LDAP infrastructure. Besides, you will prevent a general LDAP lockout, which can block your LDAP users from using other systems on the intranet.

:::caution

LDAP brute-force settings can be configured for only **Testing Distribution** and **Enterprise App Store** modules.

[Appcircle login with LDAP](/self-hosted-appcircle/install-server/linux-package/configure-server/integrations-and-access/ldap-settings#appcircle-login-with-ldap) is not supported and is out-of-scope for the brute-force settings.

:::

To configure LDAP brute force protection, you can edit the `values.yaml` file and add the following settings under `auth`:

```yaml
auth:
  auth-keycloak:
    bruteForce:
      distribution:
        maxFailureCount: "5"
        maxLockDuration: "600"
      store:
        maxFailureCount: "5"
        maxLockDuration: "600"
```

## User Lookup Decision Settings

The LDAP (Lightweight Directory Access Protocol) user lookup decision strategy is a crucial aspect of user authentication in applications that utilize LDAP for user management.

When Appcircle receives a user login request from the Enterprise App Store or Testing Distribution, it needs to determine which LDAP configuration to use for the user lookup and authentication process.

In scenarios where a user exists in multiple LDAP configurations, a decision must be made on which configuration to use for authentication.

This documentation provides insights into the LDAP user lookup decision strategy and how it can be configured to handle scenarios where a user has multiple usernames and passwords across different LDAP configurations.

### Editing User Lookup Decision Strategy

To configure LDAP lookup decision settings, you can edit the `values.yaml` like in the example below:

```yaml
auth:
  auth-keycloak:
    userLookupDecisionStrategy: decisive
```

If you don't define it or it has an unknown value, it is assumed to be `decisive` by default.

#### Affirmative

When `userLookupDecisionStrategy` is set to "affirmative", the LDAP authentication process will check all LDAP settings, even if the user is found on a particular LDAP configuration. This means that if a user has multiple accounts on different LDAP configurations with different passwords, they will be able to login successfully. The authentication system will search across all LDAP configurations to find a matching username or email and validate the user's password, allowing the user to access the system.

#### Decisive

On the other hand, when `userLookupDecisionStrategy` is set to "decisive", the LDAP authentication process will check a specific LDAP configuration for the user's username or email. If the authentication system finds the username on a particular LDAP, it will verify the user's password only on that specific LDAP configuration. If the provided password is incorrect, the authentication system will not check other LDAP configurations and will immediately return invalid credentials, denying access to the user.

#### Tolerant

When `userLookupDecisionStrategy` is set to "tolerant", similar to the "affirmative" strategy, it retrieves the list of LDAP providers where the user is found and checks the password sequentially. If the password is correct, the process ends. If it is incorrect, the search continues until the last LDAP provider. Unlike "affirmative", if an LDAP provider is unreachable or an error occurs, the process continues, and the faulty provider is ignored.

:::

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

## LDAP Mapping

LDAP Mapping in Appcircle allows you to synchronize user groups and roles from your LDAP directory to your Appcircle environment seamlessly. This guide provides a step-by-step approach to setting up and managing LDAP mappings, ensuring your user and role integrations are as efficient as possible.

### Group And Role Mapper Configuration

Group and role mapper configuration must be completed before starting the LDAP mapping configuration. The LDAP group and role mapper define how groups and roles are retrieved from LDAP.

You can configure it using the following steps:

1. To get started, click on the **Admin** button from the left menu.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-1.png' />

2. Go to the **Self-Hosted Settings** screen.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-2.png' />

3. And press the **Manage** button next to **LDAP Login**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-manage-button.png' />

4. Click the **Set Up LDAP Configuration**, then click **Edit** button in your LDAP provider.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-edit-button.png' />

5. In the **LDAP Connection screen**, scroll down to find the **Group Mapper** and **Role Mapper** sections.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-group-role-mapper.png' />

6. Click the **Add** button next to the Group Mapper to create a proper group mapper configuration for retrieving groups and members from LDAP.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-group-mapper-empty.png' />

7. Click the **Add** button next to the Role Mapper to create proper role mapper configuration for retrieving roles and members from LDAP.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-role-mapper-empty.png' />

### Accessing LDAP Settings

To configure LDAP Mapping, follow these steps:

1. Navigate to the **Admin** section on your dashboard.
2. Select **Self-Hosted Settings** and click on **LDAP Login** to access the LDAP configuration options.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3671-ldap-mapping-guide.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3671-ldap-mapping-menu.png' />

### Configuring LDAP Mapping

#### Setting Up LDAP Configuration

- **Select LDAP Configuration**: Begin by selecting your LDAP configuration from the dropdown menu. This is where you define and select the LDAP source to be used for mapping.
- **LDAP Groups and Appcircle Organizations**: Choose an LDAP group and the corresponding Appcircle organization you want to synchronize.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3671-ldap-mapping-info.png' />

#### Associating LDAP Groups with Appcircle Organizations

- **Mapping LDAP Groups**: After selecting the LDAP group, map it to an Appcircle organization by clicking **Add**. This establishes a link where users from the LDAP group are automatically mapped to the corresponding organization in Appcircle.

:::caution

- Appcircle Organizations must be created manually before using them with LDAP Mapping.

:::

### Managing LDAP Groups and Mappings

- **View Configurations**: All active LDAP mappings can be viewed under the LDAP Mapping section. You can modify or delete each mapping as needed by using the **Config** option.

### LDAP Role Mapping

LDAP Role Mapping allows you to assign specific roles to users based on their LDAP group memberships. This feature streamlines user management by automatically assigning roles to users based on their LDAP role associations.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3671-ldap-mapping-config.png' />

#### Configuring Role Mappings

- Navigate to the **LDAP Role Mapping** section where you can assign specific Appcircle roles based on the LDAP roles assigned to users.
- **Add a New Role**: Select a role from the available LDAP roles and assign it to users within the specified Appcircle organization. Roles such as administrator, developer, or custom group roles can be mapped accordingly.

#### Role and Permissions Management

- Each role can have varied permissions across different modules such as Build, Deploy, and Admin settings. Configure these permissions to ensure users have appropriate access levels based on their role.

### LDAP Synchronization

You can synchronize users from LDAP groups to Appcircle organizations using LDAP Synchronization. This process involves adding new users and removing unnecessary ones.

:::info

If you configure an Appcircle organization for synchronization, the synchronization task will override any manual configurations.

Please note that the synchronization is one-way from LDAP to Appcircle, meaning changes made in Appcircle do not affect LDAP.

:::

:::caution

- The sync operation does not fetch all users. If a user has not logged in before, they will join the organization with the assigned roles as soon as they log in, provided LDAP Mapping is enabled.
- If a user does not exist in Appcircle (has not been imported yet), they will be ignored by the synchronization task.
- The synchronization operation also does not affect the admin user. Even if the admin user is not in the LDAP group, they remain a member of the Appcircle organization.
- Appcircle Root Organizations must have at least one owner. The synchronization operation will not remove a user if they are the last owner of the root organization.
- You need to run the synchronization task once for users who are already in Appcircle and linked to LDAP.

:::

#### Enabling and Managing Synchronization

- **Activate Synchronization**: Toggle the LDAP Synchronization option to enable automatic syncing between LDAP and Appcircle.
- **Manual Sync and Interval Settings**: Use the **Sync Now** button to manually trigger a sync or set a synchronization interval to automate the process at regular intervals.

### Conclusion

Setting up LDAP Mapping streamlines user management by automating the synchronization of user roles and groups from LDAP into Appcircle. This guide should assist you in effectively managing user access and roles within your organization, ensuring security and efficiency in your app development processes.

## Troubleshooting

:::info
If the LDAP configuration is incorrect or the LDAP server cannot be accessed for some reason, you can always login with the "initial username" and "initial password" that were configured while installing the server.

See the [configure](/self-hosted-appcircle/install-server/linux-package/installation/docker#3-configure) section in the installation page for the `global.yaml` details.
:::

<NeedHelp />