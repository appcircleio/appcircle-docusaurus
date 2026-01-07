---
title: Signing In
description: Learn how to change your password and setup two factor authenticator in Appcircle
tags: [account, account management, change password, two-factor authentication, 2FA, authenticator]
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';

# Signing In

The **Signing In** section allows you to manage how you access your account. You can update your password for basic authentication and enable **Two-Factor Authentication (2FA)** for an extra layer of security.

## Basic Authentication

Your account is protected by a password, which you can update at any time.

- **Password**: Sign in by entering your account password.
- **Created**: Displays the date and time when the password was last set or updated.
- **Update**: Use the **Update** button to change your password.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE6855-account3.png"/>

## Two-Factor Authentication (2FA)

For improved security, you can set up **Two-Factor Authentication** using an authenticator application.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE6855-account6.png"/>

- **Authenticator application**: When enabled, you will be asked to provide a verification code from your authenticator app (such as Google Authenticator, Microsoft Authenticator and FreeOTP) each time you sign in.
- **Set up Authenticator application**: Click this link to configure 2FA for your account.
- **Status**: When enabled, you will see the name you have provided during the authenticator configuration. If not configured, it will show *"Authenticator application is not set up."*

:::tip
You can use any other authenticator service which supports generation of SHA1 OTP codes.
:::

- Click on the **Set up Authenticator Application**.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE6855-account5.png"/>

- Scan the QR Code with your selected Authenticator Application. However, if you can't scan the QR code, you can also select **Unable to scan?** field and fill the information accordingly.
- After the code is successfully entered, assign it a friendly name and click on **Save.**
- The newly created OTP will be under effect the next time you login. Your current login session will not be terminated(you will not be logged out).

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE6855-account4.png"/>

#### CLI Log In with 2FA

Currently, CLI does not support 2FA connection. You can use the CLI without 2FA connection, even if you have 2FA set up in your account.

:::info Locked out of your Account?

If you have lost your one time password or locked out of your 2FA provider, you can contact us for recovery of your account.

:::