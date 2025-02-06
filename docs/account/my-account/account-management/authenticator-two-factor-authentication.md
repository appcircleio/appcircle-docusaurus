---
title: Two-Factor Authentication Setup
description: Learn how to set up two-factor authentication in Appcircle
tags: [account, account management, two-factor authentication, 2FA, authenticator]
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';

# Two-Factor Authentication Setup

Navigate to the [Authenticator page](https://auth.appcircle.io/auth/realms/appcircle/account/totp) through your account.

In this screen, you can manage your 2FA connection and create new keys. Simply scan the QR code on your mobile phone (or on your computer) and paste the code at the **One-time code** field.

Appcircle supports those services out of the box:

- FreeOTP
- Google Authenticator

:::tip

You can use any other authenticator service which supports generation of SHA1 OTP codes.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5444-auth1.png' />

However, if you use another Authenticator service and you can't scan the QR code, you can also select **Unable to scan?** field and fill the information accordingly.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5444-auth2.png' />

After the code is successfully entered, assign it a friendly name and click on **Save.**

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5444-auth3.png' />

The newly created OTP will be under effect the next time you login. Your current login session will not be terminated(you will not be logged out).

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (231).png' />

#### CLI Log In with 2FA

Currently, CLI does not support 2FA connection. You can use the CLI without 2FA connection, even if you have 2FA set up in your account.

:::info

#### Locked out of your Account?

If you have lost your one time password or locked out of your 2FA provider, you can contact us for recovery of your account.

:::
