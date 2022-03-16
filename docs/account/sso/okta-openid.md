---
title: Okta OpenID
metaTitle: Okta OpenID
metaDescription: Okta OpenID
sidebar_position: 5
---

# Okta OpenID

Appcircle supports [Okta](https://www.okta.com/) as OpenID or SAML provider. 

:::info

Only Enterprise accounts support SSO.

:::


### Enable SSO

SSO can only be enabled by the organization's administrator. To start, go to [My Organization](../my-organization.md) screen and click the **Enable SSO** button under the **SSO Integration** section.

![](<https://cdn.appcircle.io/docs/assets/enable-sso.png>)

### Configure Appcircle and Okta

-  Select Setup an OpenID Provider

![](<https://cdn.appcircle.io/docs/assets/sso-form.png>)

-  Pick an alias and display name for your organization. Please pick a short and rememberable alias.

- This screen will auto-generate an URL for the next step

![](<https://cdn.appcircle.io/docs/assets/sso-openid1.png>)

- Login to your [Okta](https://www.okta.com/) account and navigate to Applications and then click "Create App Integration".

![](<https://cdn.appcircle.io/docs/assets/oktacreateapp.png>)

- Select "OIDC - OpenID Connect" as Sign In Method and then select **Web Application** as application type

![](<https://cdn.appcircle.io/docs/assets/oktawebapp.png>)

- Navigate to settings of the app and note, **Client ID** and **Client Secret**

![](<https://cdn.appcircle.io/docs/assets/oktaopenidsettings1.png>)

- Add the Appcircle Redirect URL to **Sign-in redirect URLs**

![](<https://cdn.appcircle.io/docs/assets/oktaopenidsettings2.png>)

- Instead of writing all the settings of OpenID, you can download the settings file from Okta and upload it. 

Download your OpenID configuration file from one of the below locations

```
https://customer_name_here.okta.com/.well-known/openid-configuration
https://customer_name_here.okta.com/oauth2/default/.well-known/openid-configuration?client_id=<your_client_id>

```

- Go back to Appcircle, upload this JSON file by clicking the button under **Import OpenID configuration** 

![](<https://cdn.appcircle.io/docs/assets/sso-openid1.png>)


- Check all the settings on this page and confirm that Authorization and Token URLs are imported correctly. Enter your **Client ID** and **Client Secret**. Modify the settings as below.

![](<https://cdn.appcircle.io/docs/assets/sso-openid2.png>)


### Testing SSO

- When you connect your Identity Provider, please open a new incognito window and test the SSO integration.
- Click the **Continue with SSO** button.

![](<https://cdn.appcircle.io/docs/assets/sso-loginbutton.png>)

- Enter the alias you picked.

![](<https://cdn.appcircle.io/docs/assets/sso-alias.png>)

- You should first see the below confirmation screen.

![](<https://cdn.appcircle.io/docs/assets/sso-linkaccount.png>)


- After you confirmed account linking, you will get an email.

![](<https://cdn.appcircle.io/docs/assets/sso-confirmlink.png>)

- You can now access your account with SSO integration when you confirm the email.
- After you enable the SSO, you can only log in to your account with the SSO link. Your old credentials won't work anymore.

:::caution

When you connect your Identity Provider, please open a new incognito window and test the SSO integration. Please only log off when you can log in with SSO credentials. If the connection doesn't work, you need to review your settings. 

:::
