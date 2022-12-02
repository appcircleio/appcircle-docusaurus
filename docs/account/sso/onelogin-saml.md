---
title: OneLogin SAML
metaTitle: OneLogin SAML
metaDescription: OneLogin SAML
sidebar_position: 7
---

import NarrowImage from '@site/src/components/NarrowImage';


# OneLogin SAML

Appcircle supports [OneLogin](https://www.onelogin.com/) as a SAML provider. 

:::info

Only Enterprise accounts support SSO.

:::


### Enable SSO

SSO can only be enabled by the organization's administrator. To start, go to [My Organization](../my-organization.md) screen and click the **Enable SSO** button under the **SSO Integration** section.

![](<https://cdn.appcircle.io/docs/assets/enable-sso.png>)

### Configure Appcircle and OneLogin

-  Select Setup SAML SSO Provider

![](<https://cdn.appcircle.io/docs/assets/sso-form.png>)

-  Pick an alias and display name for your organization. Please pick a short and rememberable alias.

- This screen will auto-generate an URL for the next step

![](<https://cdn.appcircle.io/docs/assets/sso-saml1.png>)

- Login to your  [OneLogin](https://www.onelogin.com/) account and navigate to Applications and then click **Add App**.

![](<https://cdn.appcircle.io/docs/assets/oneloginaddapp.png>)

- Write Appcircle to edit box and select it from the search results.

![](<https://cdn.appcircle.io/docs/assets/oneloginfindapp.png>)

- Pick a name and optional logo for the app and click **Save**

![](<https://cdn.appcircle.io/docs/assets/oneloginsettings1.png>)

- Write the alias that you have created earlier and click **Save**

![](<https://cdn.appcircle.io/docs/assets/oneloginsettings2.png>)

- Instead of writing all the settings of SAML, you can download the settings file from OneLogin and upload it. Click the **More Actions** button and click  **SAML Metadata**.

![](<https://cdn.appcircle.io/docs/assets/oneloginsettings3.png>)

- Go back to Appcircle, upload this XML file by clicking the button under **Import SAML Configuration**

![](<https://cdn.appcircle.io/docs/assets/sso-saml1.png>)

- Check all the settings on this page and confirm that Redirect and SSO URLs are imported correctly. You can check if the X509 Certificate is imported correctly as well. If you want to enter multiple certificates you can separate them by using a comma between them. Please be aware that you need to remove any new lines or file headers from this edit box. This edit box only accepts a long base64 encoded string.

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
