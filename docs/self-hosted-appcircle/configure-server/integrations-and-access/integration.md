---
title: Integrations
metaTitle: Integrate Appcircle With Other Tools
metaDescription: Integrate Appcircle With Other Tools
sidebar_position: 2
---

# Integrations

There are mainly two integrations to be filled by the user

- Email
- SSO

## Email

Please edit `global.yaml` file and change SMTP settings according to your mail server. Check the below example for configuration options

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

```

Explanation of each key

|Key|Explanation|
|---|-----------|
|password|Password of the SMTP server|
|username|Default user name for SMTP.|
|from|Sender address of the emails |
|host|The SMTP server to connect to|
|fromDisplayName |Sender Display Name|
|port |The SMTP server port to connect|
|ssl | If set to true, use SSL to connect |
|auth | If set to true, attempt to authenticate the user using the AUTH command. |
|starttls | If set to true, enables the use of the STARTTLS command |

## SSO

Appcircle supports both OpenID and SAML Identity providers. You can follow the below documents to connect your identity providers. If your Identity Provider is not on the list, you can follow any OpenID or SAML integration guide from the below list to find out the parameters.

- [Auth0 OpenID](https://docs.appcircle.io/account/sso/auth-openid/)
- [Auth0 SAML](https://docs.appcircle.io/account/sso/auth-saml/)
- [Azure AD SAML](https://docs.appcircle.io/account/sso/azure-saml/)
- [Okta OpenID](https://docs.appcircle.io/account/sso/okta-openid/)
- [Okta SAML](https://docs.appcircle.io/account/sso/okta-saml/)
- [OneLogin SAML](https://docs.appcircle.io/account/sso/onelogin-saml/)
