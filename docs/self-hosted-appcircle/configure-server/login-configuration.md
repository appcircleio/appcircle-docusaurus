---
title: Login Configuration
metaTitle: Login Configuration
metaDescription: Disable Signup or Reset Password
sidebar_position: 10
---

## Login Configuration

With the self-hosted Appcircle server `v3.9.0`, you can enable/disable user signup feature and forgot password feature from the self-hosted admin page.

If your organization has configured LDAP or OAuth authentication for Appcircle users, you may want to disable the email signup feature.

Allowing email signup could result in having users registered both through LDAP/OAuth and through email.

This can create duplicated users and make user management more difficult. Disabling email signup ensures all users are created through your centralized LDAP or OAuth provider, avoiding duplication.

Just keep in mind that disabling email signup means new users will need to be created directly in your LDAP or OAuth provider first before they can sign in to Appcircle.

Disabling email signup also prevents unwanted or unknown users from signing up for accounts through the email flow.

With LDAP or OAuth, only users explicitly added to those systems can gain access, keeping tighter control over who can login to Appcircle.

Also keeping the forgot password feature opened allows users to reset their password. If a user reset his/her password, the user will be no longer LDAP user.

You might want to keep in mind to disable forgot password feature after you enable LDAP or OAUTH.

## Disabling User Registration

- To disable `User Registration`, access your Appcircle from your preferred web browser.

- Navigate to the `Admin` and `Self-Hosted Settings` page.

![](https://cdn.appcircle.io/docs/assets/user-registration.png)

- To disable `User Registration`, deselect the related toggle as shown in the example above 👆.

- Click the save button to apply the settings.

- To verify that `User Registration` has been disabled, you can log out from the current account.

- As shown in the image below, users are now unable to register with email.

![](https://cdn.appcircle.io/docs/assets/user-registration-disabled.png)

## Disabling the Forgot Password Feature

- To disable the `Forgot Password` feature, access your Appcircle from your preferred web browser.

- Navigate to the `Admin` and `Self-Hosted Settings` page.

![](https://cdn.appcircle.io/docs/assets/forgot-password.png)

- To disable `Forgot Password`, deselect the related toggle as shown in the example above 👆.

- Click the save button to apply the settings.

- To verify that the `Forgot Password` feature has been disabled, you can log out from the current account.

- As shown in the image below, users are now unable to reset their password using the `Forgot Password` feature.

![](https://cdn.appcircle.io/docs/assets/forgot-password-disabled.png)
