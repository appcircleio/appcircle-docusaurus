---
title: Auth0 OpenID
metaTitle: Auth0 OpenID
metaDescription: Auth0 OpenID
sidebar_position: 2
---

import NarrowImage from '@site/src/components/NarrowImage';

# Auth0 OpenID

Appcircle supports [Auth0](https://auth0.com/) as OpenID or as SAML provider. 

:::info

Only Enterprise accounts support SSO.

:::


### Enable SSO

SSO can only be enabled by the organization's administrator. To start, go to [My Organization](../my-organization.md) screen and click the **Enable SSO** button under the **SSO Integration** section.

![](<https://cdn.appcircle.io/docs/assets/enable-sso.png>)


### Configure Appcircle and Auth0

-  Select **Setup OpenID Provider**

![](<https://cdn.appcircle.io/docs/assets/sso-form.png>)

- Pick an alias and display name for your organization. Please pick a short and rememberable alias.

- This screen will auto-generate an URL for the next step

![](<https://cdn.appcircle.io/docs/assets/sso-openid1.png>)

- Login to your  [Auth0](https://auth0.com/) account and navigate to Applications and then click **Create Application**.

![](<https://cdn.appcircle.io/docs/assets/authcreateapp.png>)

- Select **Regular Web Applications** and give a name

![](<https://cdn.appcircle.io/docs/assets/authwebapp.png>)

- Navigate to settings of the app and note, **Client ID** and **Client Secret**

![](<https://cdn.appcircle.io/docs/assets/authopenidsettings1.png>)

- Add the Appcircle Redirect URL to your allowed list

![](<https://cdn.appcircle.io/docs/assets/authopenidsettings2.png>)

- Instead of writing all the settings of OpenID, you can download the settings file from Auth0 and upload it. Navigate to the **OpenID Configuration** address and download that JSON file to your computer.

![](<https://cdn.appcircle.io/docs/assets/authopenidsettings3.png>)

- Go back to Appcircle, upload this JSON file by clicking the button under **Import OpenID configuration** 

![](<https://cdn.appcircle.io/docs/assets/sso-openid1.png>)


- Check all the settings on this page and confirm that Authorization and Token URLs are imported correctly. Enter your **Client ID** and **Client Secret**. Modify the settings as below.

![](<https://cdn.appcircle.io/docs/assets/sso-openid2.png>)


### Testing SSO

- When you connect your Identity Provider, please open a new incognito window and test the SSO integration.
- Click the **Continue with SSO** button.

![](<https://cdn.appcircle.io/docs/assets/sso-loginbutton.png>)

- Enter the alias you picked.

<NarrowImage src="https://cdn.appcircle.io/docs/assets/sso-alias.png" />

- You should first see the below confirmation screen.

![](<https://cdn.appcircle.io/docs/assets/sso-linkaccount.png>)


- After you confirmed account linking, you will get an email.

![](<https://cdn.appcircle.io/docs/assets/sso-confirmlink.png>)

- You can now access your account with SSO integration when you confirm the email.
- After you enable the SSO, you can only log in to your account with the SSO link. Your old credentials won't work anymore.

:::caution

When you connect your Identity Provider, please open a new incognito window and test the SSO integration. Please only log off when you can log in with SSO credentials. If the connection doesn't work, you need to review your settings. 

:::
