---
title: Integrations
description: Learn how to configure email and SSO integrations in Appcircle
tags: [integrations, email, sso]
sidebar_position: 2
---

# Integrations

There are mainly two integrations to be filled by the user

- Email
- SSO

## Email

Appcircle provides two methods to configure SMTP settings.

### Configure via Dashboard (recommended)

Starting from the version `3.28.1`, SMTP settings can be configured and updated directly from the Appcircle Dashboard. This is the recommended approach for managing SMTP settings as it allows you to update the configuration at any time without requiring server reset.

:::caution
To access the SMTP configuration page, you must be logged in as the **Admin** user.
:::

- To reach "SMTP Configuration" navigate to "Admin > Self-Hosted Settings" page using the left menus.

- And press the "Manage" button next to "SMTP Configuration".

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-6465-smtp-configuration-manage.png' />

- You will see the SMTP configuration page.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-6465-smtp-configuration-detail.png' />

- Fill in the SMTP settings according to your mail server. See the details below for configuration options:

| Settings | Description | Example |
|----------|-------------|---------|
| FROM | The default email address used in the "From" field for outgoing emails. | noreply@acme.com |
| FROM DISPLAY NAME | The display name that appears alongside the default from address in outgoing emails. | Acme Inc |
| HOST | The hostname or IP address of the SMTP server. | email-smtp.acme.com |
| DOMAIN (optional) | The domain used for authenticating with the SMTP server (often applicable for Exchange or custom SMTP services). | email-smtp.acme.com |
| PORT | The port number to connect to on the SMTP server (typically 25, 465, or 587). | 587 |
| Use SSL | Specifies whether SSL encryption should be used for the SMTP connection. | Off |
| Start TLS | Determines whether to enable STARTTLS, which upgrades a plain connection to a secure one. | On |
| Validate Server Cert | Specifies whether the SMTP server's SSL certificate should be validated. It is recommended to keep this as true for security purposes. | On |
| Auth | Indicates whether SMTP authentication is required. Set to true if both UserName and Password are necessary. | On |
| USERNAME | The username for SMTP server authentication. | your_username |
| PASSWORD | The password for authenticating with the SMTP server. | your_password |
| TO (optional) | The default email address used in the "To" field for outgoing emails. | mobile-team@acme.com | 

- Click the "Test Connection" button to verify that the connection to your SMTP server is successful. If the test fails, check your settings and try again.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-6465-smtp-configuration-test.png' />

- If your settings are correct, click the "Save" button to apply the settings.

<!-- Cautions: Static Config in Use, Shared Across Organizations -->

:::info
Email notifications use the "FROM DISPLAY NAME" as the sender name (or from name). However, when you [share a binary](https://docs.appcircle.io/testing-distribution/create-or-select-a-distribution-profile#share-binary) using the **Testing Distribution** module, the **profile name** will be displayed as the sender, as shown in the example email provided in the linked documentation.
:::

### Configure via `global.yaml`

If you prefer to configure SMTP via `global.yaml` for initial installation; you can edit the `global.yaml` file and change SMTP settings according to your mail server. See the example below for configuration options:

```yaml
smtpServer:
  password: your_password
  user: your_username
  from: noreply@acme.com
  host: email-smtp.acme.com
  fromDisplayName: Acme Inc
  port: '587'
  ssl: 'false'
  auth: 'true'
  starttls: 'true'
  verifyCertificate: 'true'
```

:::tip
Even if you initially configure SMTP using `global.yaml`, you can still use the Appcircle Dashboard for subsequent updates.
:::

Explanation of each key:

|        Key        |         Explanation         |
|-------------------|-----------------------------|
| password          | Password of the SMTP server |
| username          | Default user name for SMTP |
| from              | Sender address of the emails |
| host              | The SMTP server to connect to |
| fromDisplayName   | Sender Display Name |
| port              | The SMTP server port to connect |
| ssl               | If set to `true`, use SSL to connect |
| auth              | If set to `true`, attempt to authenticate the user using the AUTH command. |
| starttls          | If set to `true`, enables the use of the STARTTLS command |
| verifyCertificate | If set to `false`, disables validation of the SMTP server's SSL certificate. The value is `true` by default, shouldn't be disabled in production environments. |

:::info
The `verifyCertificate` option is available in version `3.23.1` or later.
:::

:::info
Email notifications use the `fromDisplayName` as the sender name (or from name). However, when you [share a binary](https://docs.appcircle.io/testing-distribution/create-or-select-a-distribution-profile#share-binary) using the **Testing Distribution** module, the **profile name** will be displayed as the sender, as shown in the example email provided in the linked documentation.
:::

## SSO

Appcircle supports both OpenID and SAML Identity providers. You can follow the below documents to connect your identity providers. If your Identity Provider is not on the list, you can follow any OpenID or SAML integration guide from the below list to find out the parameters.

- [Auth0 OpenID](https://docs.appcircle.io/account/sso/auth-openid/)
- [Auth0 SAML](https://docs.appcircle.io/account/sso/auth-saml/)
- [Azure AD SAML](https://docs.appcircle.io/account/sso/azure-saml/)
- [Okta OpenID](https://docs.appcircle.io/account/sso/okta-openid/)
- [Okta SAML](https://docs.appcircle.io/account/sso/okta-saml/)
- [OneLogin SAML](https://docs.appcircle.io/account/sso/onelogin-saml/)
