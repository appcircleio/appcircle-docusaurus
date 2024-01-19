---
title: SSO and LDAP Login
metaTitle: SSO and LDAP Login
metaDescription: SSO and LDAP Login
sidebar_position: 12
---

import Screenshot from '@site/src/components/Screenshot';

# LDAP Login

To start, go to [My Organization](../account/my-organization.md) > Integrations screen and press the **Connect** button next to LDAP Login under the **Connections** section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-login1.png' />

- Click Create button to create your LDAP

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-login2.png' />

- Fill in the details of your LDAP Configurations

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-login3.png' />

- You can see that the Connect button has changed to the Manage button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-login4.png' />

- To enable Two Factor Authentication, open it by clicking the Manage button and select the verification method.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-login5.png' />

- To change the distribution authorization go to Distribution Profiles screen and press the your distribution profile click **Settings** button and under the Authentication tab you should see LDAP Login. Convert **LDAP Login** to on.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-login6.png' />

- After this step, it will be necessary to log in from the LDAP Login screen to access the distributed links.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-login7.png' />

- You must verify according to the method you have chosen.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-login8.png' />

- If the login is successful, a screen similar to the one below will appear.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-login9.png' />

## Deleting LDAP Login

- To delete, go to the [My Organization](../account/my-organization.md) > Integration screen and press the Manage button next to LDAP Login under the Connections section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-login10.png' />

- Click the Remove button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-login11.png' />

- Type the alias’s name to confirm deletion and click the Delete button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-login12.png' />

## SSO Login

- To start, go to [My Organization](../account/my-organization.md) > Integrations screen and press the **Connect** button next to SSO Login under the **Connections** section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-login1.png' />

- Click Create button to create your SSO Login

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-login2.png' />

Please check [SSO](./sso/single-sign-on.md) document to learn how you can configure different SSO providers. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-login3.png' />


:::caution

Pleas be aware that, enabling SSO for **APPCIRCLE LOGIN** doesn't enable SSO for Testing Distribution and Enterprise Store. They must be configured seprately.

:::

- Click the Save button to save.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-login4.png' />

## Deleting SSO Login


- To delete, go to the [My Organization](../account/my-organization.md) > Integration screen and press the Manage button next to SSO Login under the Connections section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-login5.png' />

- Click the Remove button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-login6.png' />

- Type the alias’s name to confirm deletion and click the Delete button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-login7.png' />
