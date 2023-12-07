---
title: LDAP Brute Force
metaTitle: LDAP Brute Force Settings
metaDescription: LDAP Brute Force Settings
sidebar_position: 10
---

## Overview

Enabling LDAP authentication introduces the risk of brute-force attacks that can originate from external or internal sources.

A sustained LDAP brute-force attack can result in user accounts being locked out of the LDAP directory, preventing access to other applications integrated with the directory.

To mitigate this risk, a self-hosted Appcircle server can be configured to block repeated failed login attempts for a duration before allowing additional attempts.

The Appcircle server's brute-force algorithm is based on successive failed attempts, not failed attempts over a period of time.

:::info

**Minimum Required Version**

If you want to enable LDAP brute-force settings, the Appcircle server version must be `3.10.0` or later.

:::

### Default Configuration

Appcircle server comes with brute-force protection **turned off** by default.

It is completely up to you to set this up. See the following sections for details.

## Brute-Force Arguments

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

## Configuring the Appcircle Server

We are assuming that you have installed the Appcircle server with version `v3.10.0` or later, and configured the LDAP settings from the UI.

To configure LDAP brute-force settings on the Appcircle server, you can follow the steps below:

- SSH into the Appcircle server.

- Go to the `appcircle-server` directory.

```bash
cd appcircle-server
```

- Edit the `global.yaml` of your project.

:::info

The `spacetech` in the example codes below are example project name.

Please find your own project name and replace `spacetech` with your project name.

To see projects, you can check the `projects` directory.

```bash
ls -l ./projects
```

:::

```bash
vi projects/spacetech/global.yaml
```

- Find the `keycloak` entry and add or edit the missing `bruteForce` key to it. For example;

```yaml
keycloak:
  initialUsername: admin@spacetech.local
  initialPassword: SuperSecretPassword1234%!
  enabledRegistration: true
  bruteForce:
    distribution:
      maxFailureCount: 10
      maxLockDuration: 3600
    store:
      maxFailureCount: 10
      maxLockDuration: 3600
```

:::info

`maxFailureCount`: This variable represents the needed count of successive failed attempts to block user.

`maxLockDuration`: This variable expresses the time in seconds required to unblock the user.

:::

- Export the new variables.

```bash
./ac-self-hosted.sh -n "spacetech" export
```

- Stop the Appcircle server.

```bash
./ac-self-hosted.sh -n "spacetech" down
```

- Start the Appcircle server with new brute-force variables.

```bash
./ac-self-hosted.sh -n "spacetech" up
```

- Check the health of the services.

```bash
./ac-self-hosted.sh -n "spacetech" check
```
