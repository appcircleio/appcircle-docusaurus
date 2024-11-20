---
title: Appcircle SSO Authentication
description: Establish Single Sign-On (SSO) providers for your organization. Enhance security and simplify access across Appcircle's platform.
tags: [account, organization, sso, configuration]
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';

# Appcircle Login Single Sign-On (SSO) Providers Configuration

## 1. Introduction

Single Sign-On (SSO) allows users to log in to Appcircle using their existing credentials from an Identity Provider (IdP). By integrating SSO, organizations can streamline user access management, enhance security, and provide a seamless login experience across multiple platforms.

This document specifically covers the SSO configuration for the Appcircle Login. Please note that a separate SSO configuration exists for the [Testing Portal (Testing Distribution module)](/account/my-organization/security/authentications/distribution-sso-authentication) and [Enterprise Portal (Enterprise App Store module)](/account/my-organization/security/authentications/store-sso-authentication). This document does not cover those configurations.

Currently, this configuration supports enabling SSO with only one identity provider at a time. Adding multiple SSO providers is not supported at this moment but may be available in the future.

The SSO setup described in this document integrates the selected identity provider with the Appcircle IAM module, essentially adding the provider as an identity source for Appcircle.

This document provides a comprehensive guide to configuring SSO with various supported identity providers, including Auth0, Microsoft Entra ID (formerly Azure Active Directory), Okta, OneLogin and Keycloak. Whether you choose to implement OpenID Connect or SAML, this guide will walk you through the necessary steps to ensure a successful integration with Appcircle.

### Supported Identity Providers

- Auth0:
    - Auth0 (OpenID Connect)
    - Auth0 (SAML)
- Microsoft Entra ID (formerly Azure Active Directory):
    - Microsoft Entra ID (SAML)
- Okta:
    - Okta (OpenID Connect)
    - Okta (SAML)
- OneLogin:
    - OneLogin (SAML)
- Keycloak:
    - Keycloak (OpenID Connect)
    - Keycloak (SAML)

Each section will provide detailed instructions for configuring your chosen identity provider, including screenshots and troubleshooting tips to ensure a smooth setup process.

## 2. Prerequisites

Before you begin configuring SSO for Appcircle, ensure that you have the following prerequisites:

- An active account with one of the supported Identity Providers (IdPs).
- Administrative access to both the Identity Provider and Appcircle's platform. For more details, refer to the [Appcircle Role Management Documentation](/account/my-organization/profile-and-team/role-management#organization-management-permissions).
- Access to SAML tracing tools or other relevant debugging resources.
- SSL certificates (if required by your IdP).

These prerequisites will ensure that the SSO configuration process is smooth and any issues that arise can be quickly resolved.

### SSO Terminology

Understanding the following key terms will help you navigate the SSO configuration process more effectively:

- **Identity Provider (IdP):** The service responsible for authenticating the user and issuing identity information. Common examples include Auth0, Microsoft Entra ID, Okta, OneLogin, and Keycloak.
- **Service Provider (SP):** The service (in this case, Appcircle) that relies on the IdP to authenticate users and grant them access. The SP uses the identity information provided by the IdP to manage user sessions and permissions.
- **SAML Assertion:** A secure XML document sent by the IdP to the SP, containing the user's authentication and authorization information. This document is a core component of the SAML protocol, used to establish a user’s identity across different services.
- **OpenID Connect Token:** A token used in the OpenID Connect protocol to convey identity information from the IdP to the SP. This token typically includes user information and is crucial for establishing secure communication between the IdP and SP.

These terms form the foundation of the SSO process, where the IdP authenticates the user and the SP relies on this authentication to grant access. For more in-depth information, refer to the [OpenID Connect specification](https://openid.net/developers/how-connect-works/) or the [SAML specification](https://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf).

## 3. General Configuration Steps

The following steps outline the general process for configuring Single Sign-On (SSO) with Appcircle, applicable to all supported identity providers. These steps will guide you through the initial setup within the Appcircle dashboard and the configuration within your chosen identity provider.

<details>
    <summary>Step 1: Enable SSO in Appcircle</summary>
  
Begin by enabling SSO within your Appcircle organization settings. Follow these steps:

1. In the Appcircle dashboard, navigate to the **Organization** section located on the far left sidebar.
2. On the **My Organization** screen, select **Security** from the left-hand menu.
3. On the **Security** screen, locate the **Authentications** section on the far right, find **Appcircle SSO Login**, and click **Add New**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/enable-sso_v4.png' />

4. The **Manage Appcircle SSO Login** window will open, presenting two options:
    - **Create New Authentication**
    - **Create From Existing Authentication**
You can create new configuration or create from existing configuration. Click on the **Create New Authentication** section to create new configuration.
Please refer the **Step 3: Create From Existing SSO Configuration** section in the 3. General Configuration Steps.

<Screenshot url='https://cdn.appcircle.io/docs/assets/appcircle-sso-create-options.png' />

5. The **Create New Authentication** window will open, presenting two options:
    - **Set up OpenID Connect Provider**
    - **Set up SAML SSO Provider**
  

    Select the option that corresponds to the identity provider you will configure.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-form_v3.png' />

6. In the setup window, manually enter a unique **Alias** for your organization. This alias is used to create a custom Redirect URI that will be  required for configuring your SSO provider.
7. After setting the alias, Appcircle will automatically generate a **Redirect URL** and a **Logout Redirect URL** specific to your configuration. These URLs must be used in your identity provider's settings to ensure proper redirection after authentication and logout.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-openid1_v3.png' />

Ensure that the alias is unique and easily identifiable, as they are essential for the SSO authentication process. The generated **Redirect URL** and **Logout Redirect URL** are crucial for your SSO setup, so be sure to copy and save them for use in the following steps.

8. Additionally, enter a **Display Name** for your organization.

</details>

<details>
  <summary>Step 2: Select and Configure Your Identity Provider</summary>

After enabling SSO and setting your alias, proceed to select and configure your identity provider:

1. Depending on the option you selected in the previous step, you will either be configuring an OpenID Connect or SAML provider.
2. Follow the specific steps for your chosen provider to enter the necessary configuration details, including Client ID, Client Secret, and other required parameters.
3. Use the previously generated Redirect URI provided by Appcircle when configuring your identity provider settings to ensure proper redirection after authentication.

Only one SSO provider can be configured at a time.

</details>

<details>
  <summary>Step 3: Create From Existing SSO Configuration</summary>

  Appcircle allows you to create a new SSO configuration based on an existing OpenID Connect configuration, ensuring a smooth and efficient setup experience. 

:::caution

**Important:** The 'Create From Existing' SSO feature cannot be used for SAML configurations because some identity providers restrict the use of a single SAML Entity ID or a single Logout Redirect URL.
:::
 
1. Navigate to the **Organization > Security > Authentications** section on your dashboard.
2. Select the **Add New** on the **Appcircle SSO Login**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/security-authentications.png' /> 

3. Select the **Create New Authentication** and then select the **Create From Existing SSO Configuration**.

Existing SSO configurations will be listed in screen. Select one of them and click on **Next**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-create-from-existing.png' /> 

- On the Create SSO Configuration screen, fill in the **Alias** and **Display Name** and **Credential** fields (all other values are prefilled). Customize as needed, then click **Save**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sso-openid1_v3.png' />

- Copy the Redirect URL and go to your identity provider. Paste it into the appropriate field.

</details>

<details>
  <summary>Step 4: SSO Login Direct Link</summary>

 Appcircle also supports direct SSO login links. Use the following URL format to log in directly using your SSO alias:

- For Cloud-Hosted Appcircle:
`https://my.appcircle.io/sso/{SSO_ALIAS}`
- For Self-Hosted Appcircle:
`https://my.appcircle.{your-domain}/sso/{SSO_ALIAS}`

Replace `{SSO_ALIAS}` with the alias you configured, and if you are using a self-hosted solution, replace `{your-domain}` with your actual domain.

</details>

<details>
  <summary>Step 5: Test and Verify SSO Configuration</summary>

After completing the SSO configuration, it's essential to test and ensure everything is functioning correctly. The following steps outline the testing process.

<details>
  <summary>Step 5.1: Initiate SSO Login</summary>

1. Open an incognito window in your browser to avoid any cached sessions interfering with the test.
2. Navigate to the Appcircle login page and click the **Continue with SSO** button.
3. Enter the SSO Alias you configured earlier and proceed. The alias is used to identify your organization's specific SSO setup.

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-alias.png" />

</details>

<details>
  <summary>Step 5.2: Account Linking</summary>

1. After entering the alias, if a user with the same email already exists, you should see a confirmation screen prompting you to link your account with the SSO provider.
2. Confirm the account linking by clicking the appropriate button on the confirmation screen.
3. You will receive an email to verify the account linking. Open the email and click the verification link.

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-linkaccount.png" />

</details>

<details>
  <summary>Step 5.3: Verification via Email</summary>

Once you confirm the account linking, an email will be sent to your registered email address. You must verify your account using the link in this email to complete the process.

1. Open the verification email and click the provided link to confirm your account.
2. After verification, you will be redirected back to the Appcircle dashboard, fully authenticated via SSO.

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-confirmlink.png" />

</details>

<details>
  <summary>Step 5.4: Final Login</summary>

After verifying your account via email, your SSO setup is complete. From now on, you can log in with your SSO alias or using the direct SSO login link.

:::info

After enabling SSO, the traditional login method using your previous credentials will no longer be available for your organization. Ensure that you can log in successfully using SSO before logging out of any sessions.

:::

</details>
</details>

## 4. Specific Provider Configuration

This section provides detailed instructions for configuring Single Sign-On (SSO) with specific identity providers supported by Appcircle. Each provider may have unique requirements, so it's important to follow the steps closely.

<details>
  <summary>4.1 Auth0 (OpenID Connect)</summary>

Auth0 is a popular identity provider that supports the OpenID Connect protocol, which can be integrated with Appcircle for secure authentication.

#### Step 1: Create an Application in Auth0

To start, log in to your Auth0 dashboard and create a new application for Appcircle:

1. In the Auth0 dashboard, navigate to the **Applications** section.
2. Click **Create Application** and choose a name for your application (e.g., "Appcircle SSO - OpenID").

<Screenshot url="https://cdn.appcircle.io/docs/assets/authcreateapp.png" />

3. Select **Regular Web Applications** as the application type.
4. Click **Create** button.

<Screenshot url="https://cdn.appcircle.io/docs/assets/authwebapp.png" />

5. Once application created, navigate to the **Settings** of application.
6. Take note of the **Client ID** and **Client Secret**, which will be needed later.

<Screenshot url="https://cdn.appcircle.io/docs/assets/authopenidsettings1.png" />

#### Step 2: Configure Callback URLs in Auth0

Next, configure the callback URLs in Auth0 to ensure proper redirection to Appcircle after authentication:

1. In the Auth0 dashboard, go to the **Settings** tab of your application.
2. In the **Allowed Callback URLs** field, enter the Redirect URL that was created using the alias in "Step 1: Enable SSO in Appcircle" from the "3. General Configuration Steps" section.

**Example Callback URL:** `https://auth.appcircle.io/auth/realms/appcircle/broker/identity-{your-alias}/endpoint`

<Screenshot url="https://cdn.appcircle.io/docs/assets/authopenidsettings2.png" />

3. In the **Allowed Logout URLs** field, enter the **Logout Redirect URL** that was created using the alias in "Step 1: Enable SSO in Appcircle" from the "3. General Configuration Steps" section.

<Screenshot url="https://cdn.appcircle.io/docs/assets/authopenidsettings2.png" />

4. Click on the **Save Changes** button.

#### Step 3: Download OpenID Configuration from Auth0

Instead of writing all the settings of OpenID, you can download the settings file from Auth0 and import in Appcircle. Download the OpenID configuration JSON file from Auth0 with following steps.

1. In the Auth0 dashboard, go to the **Settings** tab of your application.
2. Scroll to the bottom of the page and expand the **Advanced Settings** section.
3. Navigate to the **Endpoints** tab. 
4. Copy and open **OpenID Configuration** URL in different tab in your browser.

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-auht0-openid-config.png" />

5. Save **OpenID Configuration** as json file.

#### Step 4: Upload OpenID Configuration to Appcircle

Now, upload the OpenID configuration JSON file to Appcircle and complete the configuration:

1. Navigate to the **Set up OpenID Connect Provider** screen in Appcircle, which you accessed during the SSO setup in the "General Configuration Steps".
2. Choose the **Client secret sent as basic auth** as Client Authentication.
3. Enter the **Client ID** and **Client Secret** that you noted earlier from Auth0.
4. Upload the downloaded OpenID configuration JSON file to Appcircle.

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-openid3_v1.png" />

5. Click **Save** to finalize the SSO setup.

#### Step 5: Test the Integration

After configuring the settings, it’s crucial to test the OpenID Connect SSO integration:

:::caution

**Important:** When connecting your Identity Provider, use an incognito window to test the SSO integration. Only log off once you are sure you can log in with your SSO credentials. If the connection fails, review your settings before logging out.

:::

1. Open a incognito window in your browser and initiate a new login session.
2. On the login screen, click the **Login with SSO** button to start the SSO login process

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-loginbutton.png" />

3. Enter your SSO alias when prompted and click **Continue**.

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-alias.png" />

4. You will be redirected to the Auth0 login screen. Enter your Auth0 credentials.
5. After successful authentication, you will be redirected back to Appcircle.
6. If a user with your email already exists, you will be prompted to confirm account linking. Confirm account linking and verify it via the email sent to your registered email address.

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-linkaccount.png" />

7. Once you confirm the account linking, an email will be sent to your registered email address. 

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-confirmlink.png" />

8. Open the verification email and click the provided link to confirm your account.
9. After verification, you will be redirected back to the Appcircle dashboard, fully authenticated via SSO.

<Screenshot url="https://cdn.appcircle.io/docs/assets/empty-appcircle-dashboard.png" />

</details>

<details>
  <summary>4.2 Auth0 (SAML)</summary>

Auth0 supports the SAML protocol, allowing integration with Appcircle for secure authentication.

#### Step 1: Create a SAML Application in Auth0

To start, log in to your Auth0 dashboard and create a new SAML application for Appcircle:

1. In the Auth0 dashboard, navigate to the **Applications** section.
2. Click **Create Application** and choose a name for your application (e.g., "Appcircle SSO - SAML").

<Screenshot url="https://cdn.appcircle.io/docs/assets/authcreateapp.png" />

3. Select **Regular Web Applications** as the application type.
4. Click **Create** button.

<Screenshot url="https://cdn.appcircle.io/docs/assets/authwebapp.png" />

#### Step 2: Configure SAML Settings in Auth0

Next, configure the SAML settings in Auth0 to ensure it can authenticate and redirect back to Appcircle:

1. Enable the SAML addon for your Auth0 application through the **Addons** tab in your Auth0 application settings.

<Screenshot url="https://cdn.appcircle.io/docs/assets/authsamlsettings1.png" />

2. Navigate to the **Settings** tab in the opened dialog. Use the following JSON settings to configure the SAML addon. Enter the **Logout Redirect URL** that was created using the alias in "Step 1: Enable SSO in Appcircle" from the "General Configuration Steps" section as the logout callback value.

```
    {
      "nameIdentifierFormat": "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress",
      "nameIdentifierProbes": [
        "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress"
      ],
      "logout": {
        "callback": "https://auth.appcircle.io/auth/realms/appcircle/broker/identity-{your-alias}/endpoint",
        "slo_enabled": "false"
      }
    }
```

3. In the **Application Callback URL** field, enter the **Redirect URL** that was created using the alias in "Step 1: Enable SSO in Appcircle" from the "General Configuration Steps" section.

**Example Callback URL:** `https://auth.appcircle.io/auth/realms/appcircle/broker/identity-{your-alias}/endpoint`

<Screenshot url="https://cdn.appcircle.io/docs/assets/authsamlsettings2.png" />

4. Download the **SAML metadata** file from Auth0.

This metadata file will be used in the next step to configure Appcircle.

<Screenshot url="https://cdn.appcircle.io/docs/assets/authsamlsettings3.png" />

#### Step 3: Upload SAML Metadata to Appcircle

Now, upload the SAML metadata file to Appcircle and finalize the configuration:

1. Navigate to the **Set up SAML SSO Provider** screen in Appcircle, which you accessed during the SSO setup in the "General Configuration Steps."
2. Upload the downloaded SAML metadata file to Appcircle.

<Screenshot url="https://cdn.appcircle.io/docs/assets/saml-upload-metadata.png" />

Check that the Redirect and SSO URLs are imported correctly. Ensure the X509 Certificate is imported correctly as well. If you need to enter multiple certificates, separate them with a comma. Be sure to remove any new lines or file headers, as this edit box only accepts a long base64 encoded string.

3. Complete any additional configuration settings in Appcircle as required.
5. Click **Save** to finalize the SSO setup.

**Important:** Ensure all settings match those provided in the SAML metadata file to avoid issues with authentication.

#### Step 4: Test the Integration

After configuring the settings, it’s crucial to test the OpenID Connect SSO integration:

:::caution

**Important:** When connecting your Identity Provider, use an incognito window to test the SSO integration. Only log off once you are sure you can log in with your SSO credentials. If the connection fails, review your settings before logging out.

:::

1. Open a incognito window in your browser and initiate a new login session.
2. On the login screen, click the **Login with SSO** button to start the SSO login process

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-loginbutton.png" />

3. Enter your SSO alias when prompted and click **Continue**.

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-alias.png" />

4. You will be redirected to the Auth0 login screen. Enter your Auth0 credentials.
5. After successful authentication, you will be redirected back to Appcircle.
6. If a user with your email already exists, you will be prompted to confirm account linking. Confirm account linking and verify it via the email sent to your registered email address.

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-linkaccount.png" />

7. Once you confirm the account linking, an email will be sent to your registered email address. 

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-confirmlink.png" />

8. Open the verification email and click the provided link to confirm your account.
9. After verification, you will be redirected back to the Appcircle dashboard, fully authenticated via SSO.

<Screenshot url="https://cdn.appcircle.io/docs/assets/empty-appcircle-dashboard.png" />

If the test is successful, your integration is complete, and you can start using Auth0 (SAML) as your identity provider for Appcircle.

</details>

<details>
  <summary>4.3 Microsoft Entra ID (SAML) (formerly Azure Active Directory) </summary>

Microsoft Entra ID supports the SAML protocol, allowing integration with Appcircle for secure authentication. This section will guide you through setting up Microsoft Entra ID as your SAML identity provider for Appcircle.

#### Step 1: Access Microsoft Entra and Create an Enterprise Application

First, log in to your Azure portal as an admin:

1. Log in to Azure portal as an admin and navigate to Azure Services and then click Microsoft Entra ID.

<Screenshot url="https://cdn.appcircle.io/docs/assets/azurecreateapp1.png" />

2. In the Azure portal, go to **Enterprise Applications**

<Screenshot url="https://cdn.appcircle.io/docs/assets/azurecreateapp2.png" />

3. Click **New Application**.

<Screenshot url="https://cdn.appcircle.io/docs/assets/azurecreateapp3.png" />

4. Select **Create your own application**, name it (e.g., "Appcircle SSO - SAML").

<Screenshot url="https://cdn.appcircle.io/docs/assets/azurecreateapp4.png" />

5. Choose **Integrate any other application you don't find in the gallery**.

<Screenshot url="https://cdn.appcircle.io/docs/assets/azurecreateapp5.png" />

6. Click **Create** to set up the application.

#### Step 2: Assign Users to the Enterprise Application

Once the enterprise application is created, you need to assign users to it:

1. Navigate to the created enterprise application and click **Users and Groups**.

<Screenshot url="https://cdn.appcircle.io/docs/assets/azureaddusers.png" />

2. Click **Add User/Group**, search for the user you want to assign, select them, and click **Assign**.

<Screenshot url="https://cdn.appcircle.io/docs/assets/azureaddassignment1.png" />

#### Step 3: Configure SAML-based Sign-on in Microsoft Entra ID

Next, configure the SAML-based sign-on for the Microsoft Entra ID application:

1. In the application settings, navigate to **Single sign-on** and select **SAML** as the sign-on method.

<Screenshot url="https://cdn.appcircle.io/docs/assets/azuressosettings1.png" />

2. Click **Edit** under the **Basic SAML Configuration** section, and set the following:

<Screenshot url="https://cdn.appcircle.io/docs/assets/azuressosettings2.png" />

    - **Identifier (Entity ID)**: Enter `https://auth.appcircle.io/auth/realms/appcircle`.
    - **Reply URL (Assertion Consumer Service URL)**: Enter the Redirect URL created using the alias in "Step 1: Enable SSO in Appcircle" from the "General Configuration Steps" section (e.g., `https://auth.appcircle.io/auth/realms/appcircle/broker/identity-{your-alias}/endpoint`).

<Screenshot url="https://cdn.appcircle.io/docs/assets/azuressosettings3.png" />

5. Click **Save** to apply the settings.

#### Step 4: Download and Upload SAML Metadata

Now, download the SAML metadata from Microsoft Entra ID and upload it to Appcircle:

1. In the Azure portal, go to the **SAML Signing Certificate** section and download the **Federation Metadata XML** file.

<Screenshot url="https://cdn.appcircle.io/docs/assets/azuressosettings5.png" />

2. Navigate to the **Set up SAML SSO Provider** screen in Appcircle, which you accessed during the SSO setup in the "General Configuration Steps."
3. Upload the downloaded Federation Metadata XML file to Appcircle.

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-saml1.png" />

4. Review the settings and click **Save** to finalize the configuration.

#### Step 4: Test the Integration

After configuring the settings, it’s crucial to test the OpenID Connect SSO integration:

:::caution

**Important:** When connecting your Identity Provider, use an incognito window to test the SSO integration. Only log off once you are sure you can log in with your SSO credentials. If the connection fails, review your settings before logging out.

:::

1. Open a incognito window in your browser and initiate a new login session.
2. On the login screen, click the **Login with SSO** button to start the SSO login process

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-loginbutton.png" />

3. Enter your SSO alias when prompted and click **Continue**.

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-alias.png" />

4. You will be redirected to the Auth0 login screen. Enter your Auth0 credentials.
5. After successful authentication, you will be redirected back to Appcircle.
6. If a user with your email already exists, you will be prompted to confirm account linking. Confirm account linking and verify it via the email sent to your registered email address.

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-linkaccount.png" />

7. Once you confirm the account linking, an email will be sent to your registered email address. 

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-confirmlink.png" />

8. Open the verification email and click the provided link to confirm your account.
9. After verification, you will be redirected back to the Appcircle dashboard, fully authenticated via SSO.

<Screenshot url="https://cdn.appcircle.io/docs/assets/empty-appcircle-dashboard.png" />

If the test is successful, your integration is complete, and you can start using Microsoft Entra ID (SAML) as your identity provider for Appcircle.

</details>

<details>
  <summary>4.4 Okta (OpenID Connect)</summary>

Okta supports the OpenID Connect protocol, allowing integration with Appcircle for secure authentication.

#### Step 1: Create an Application in Okta

To start, log in to your Okta dashboard and create a new application for Appcircle:

1. In the Okta dashboard, navigate to **Applications** and click **Create App Integration**.

<Screenshot url="https://cdn.appcircle.io/docs/assets/oktacreateapp.png" />

2. Select **OIDC - OpenID Connect** as the Sign In Method and **Web Application** as the application type.

<Screenshot url="https://cdn.appcircle.io/docs/assets/oktawebapp.png" />

3. Once created, take note of the **Client ID** and **Client Secret**, which will be needed later.

<Screenshot url="https://cdn.appcircle.io/docs/assets/oktaopenidsettings1.png" />

#### Step 2: Configure Callback URLs in Okta

Next, configure the callback URLs in Okta to ensure proper redirection to Appcircle after authentication:

1. Navigate to the settings of the created application in Okta.
2. Add the Appcircle Redirect URL to the **Sign-in redirect URLs** field.

**Example Redirect URL:** `https://auth.appcircle.io/auth/realms/appcircle/broker/identity-{your-alias}/endpoint`

3. Add the **Logout Redirect URL** to the **Sign-out redirect URLs** field.

<Screenshot url="https://cdn.appcircle.io/docs/assets/oktaopenidsettings2.png" />

4. Download the OpenID configuration JSON file from Okta using one of the following URLs:
    - `https://{your_okta_domain}/.well-known/openid-configuration`
    - `https://{your_okta_domain}/oauth2/default/.well-known/openid-configuration?client_id={your_client_id}`

#### Step 3: Upload OpenID Configuration to Appcircle

Now, upload the OpenID configuration JSON file to Appcircle and complete the configuration:

1. Navigate to the **Set up OpenID Connect Provider** screen in Appcircle, which you accessed during the SSO setup in the "General Configuration Steps."
2. Choose the **Client secret sent as basic auth** as Client Authentication.
3. Enter the **Client ID** and **Client Secret** that you noted earlier from Okta.
4. Upload the downloaded OpenID configuration JSON file to Appcircle.

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-openid3_v1.png" />

5. Check that the **Authorization** and **Token URLs** are correctly imported.

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-openid2_v2.png" />

6. Click **Save** to finalize the SSO setup.

#### Step 4: Test the Integration

After configuring the settings, it’s crucial to test the OpenID Connect SSO integration:

:::caution

**Important:** When connecting your Identity Provider, use an incognito window to test the SSO integration. Only log off once you are sure you can log in with your SSO credentials. If the connection fails, review your settings before logging out.

:::

1. Open a incognito window in your browser and initiate a new login session.
2. On the login screen, click the **Login with SSO** button to start the SSO login process

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-loginbutton.png" />

3. Enter your SSO alias when prompted and click **Continue**.

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-alias.png" />

4. You will be redirected to the Auth0 login screen. Enter your Auth0 credentials.

5. After successful authentication, you will be redirected back to Appcircle.

6. If a user with your email already exists, you will be prompted to confirm account linking. Confirm account linking and verify it via the email sent to your registered email address.

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-linkaccount.png" />

7. Once you confirm the account linking, an email will be sent to your registered email address. 

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-confirmlink.png" />

8. Open the verification email and click the provided link to confirm your account.
9. After verification, you will be redirected back to the Appcircle dashboard, fully authenticated via SSO.

<Screenshot url="https://cdn.appcircle.io/docs/assets/empty-appcircle-dashboard.png" />

If the test is successful, your integration is complete, and you can start using Okta (SAML) as your identity provider for Appcircle.

</details>

<details>
  <summary>4.5 Okta (SAML)</summary>

Okta supports the SAML protocol, allowing integration with Appcircle for secure authentication.

#### Step 1: Create a SAML Application in Okta

To start, log in to your Okta dashboard and create a new application for Appcircle:

1. In the Okta dashboard, navigate to **Applications** and click **Create App Integration**.

<Screenshot url="https://cdn.appcircle.io/docs/assets/oktacreateapp.png" />

2. Select **SAML 2.0** as the Sign In Method.

<Screenshot url="https://cdn.appcircle.io/docs/assets/oktacreatesaml.png" />

3. Pick a name and optional logo for the app, then click **Next**.

<Screenshot url="https://cdn.appcircle.io/docs/assets/oktasamlsettings1.png" />

#### Step 2: Configure SAML Settings in Okta

Next, configure the SAML settings in Okta to ensure proper authentication and redirection to Appcircle:

1. In the **Single sign-on URL** field, add the Appcircle Redirect URL.

**Example URL:** `https://auth.appcircle.io/auth/realms/appcircle/broker/identity-mySAML/endpoint`

3. For the **Audience URI (SP Entity ID)** field, copy and paste **Service Provider Entity ID** from Appcircle.

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-saml-appcircle-metadata.png" />

**Example URL:** `https://auth.appcircle.io/auth/realms/appcircle`

<Screenshot url="https://cdn.appcircle.io/docs/assets/oktasamlsettings2.png" />

4. Select **EmailAddress** for the Name ID format.

<Screenshot url="https://cdn.appcircle.io/docs/assets/oktasamlsettings2.png" />

5. Download **Signing Certificate** from Appcircle.

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-saml-appcircle-metadata.png" />

6. Click on **Show Advanced Settings**

7. Upload downloaded certificate to Signature Certificate field.

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-okta-saml-signing-certificate.png" />

8. Enable **Allow application to initiate Single Logout**

9. Copy and paste **Logout Redirect URL** to **Single Logout URL** field. Copy and paste **Service Provider Entity ID** to **SP Issuer**.

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-saml-appcircle-metadata.png" />

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-okta-saml-signing-certificate.png" />

8. Instead of manually configuring all SAML settings in Appcircle, you can download the SAML metadata XML file from Okta:

Click the **Copy** button next to the Metadata URL and open it in another tab to download the XML file.

<Screenshot url="https://cdn.appcircle.io/docs/assets/oktasamlsettings3-new.png" />

#### Step 3: Upload SAML Metadata to Appcircle

Now, upload the SAML metadata XML file to Appcircle to complete the configuration:

1. Navigate to the **Set up SAML SSO Provider** screen in Appcircle, which you accessed during the SSO setup in the "General Configuration Steps."
2. Upload the downloaded SAML metadata XML file to Appcircle.

<Screenshot url="https://cdn.appcircle.io/docs/assets/saml-upload-metadata.png" />

3. Ensure that the Redirect and SSO URLs are imported correctly. You can check if the X509 Certificate is imported correctly as well. If you want to enter multiple certificates you can separate them by using a comma between them. Please be aware that you need to remove any new lines or file headers from this edit box. This edit box only accepts a long base64 encoded string.

4. Enable **Want AuthnRequests Signed** in Appcircle

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-saml-enable-authn-requests-signed.png" />

5. Click **Save** to finalize the SSO setup.

#### Step 4: Test the Integration

After configuring the settings, it’s crucial to test the OpenID Connect SSO integration:

:::caution

**Important:** When connecting your Identity Provider, use an incognito window to test the SSO integration. Only log off once you are sure you can log in with your SSO credentials. If the connection fails, review your settings before logging out.

:::

1. Open a incognito window in your browser and initiate a new login session.
2. On the login screen, click the **Login with SSO** button to start the SSO login process

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-loginbutton.png" />

3. Enter your SSO alias when prompted and click **Continue**.

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-alias.png" />

4. You will be redirected to the Auth0 login screen. Enter your Auth0 credentials.
5. After successful authentication, you will be redirected back to Appcircle.
6. If a user with your email already exists, you will be prompted to confirm account linking. Confirm account linking and verify it via the email sent to your registered email address.

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-linkaccount.png" />

7. Once you confirm the account linking, an email will be sent to your registered email address. 

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-confirmlink.png" />

8. Open the verification email and click the provided link to confirm your account.
9. After verification, you will be redirected back to the Appcircle dashboard, fully authenticated via SSO.

<Screenshot url="https://cdn.appcircle.io/docs/assets/empty-appcircle-dashboard.png" />

If the test is successful, your integration is complete, and you can start using Okta (SAML) as your identity provider for Appcircle.

</details>

<details>
  <summary>4.6 OneLogin (SAML)</summary>
  
OneLogin supports the SAML protocol, allowing integration with Appcircle for secure authentication. The Appcircle application is pre-configured in OneLogin, which simplifies the setup process by providing predefined settings.

#### Step 1: Create a SAML Application in OneLogin

To start, log in to your OneLogin dashboard and create a new SAML application for Appcircle:

1. In the OneLogin dashboard, navigate to **Applications** and click **Add App**.
 
<Screenshot url="https://cdn.appcircle.io/docs/assets/oneloginaddapp.png" />

2. In the search box, type **Appcircle** and select it from the search results. The application is pre-configured with the necessary settings, including URLs and certificates.

<Screenshot url="https://cdn.appcircle.io/docs/assets/oneloginfindapp.png" />

3. Pick a name and optional logo for the app, then click **Save**.

<Screenshot url="https://cdn.appcircle.io/docs/assets/oneloginsettings1.png" />

#### Step 2: Configure SAML Settings in OneLogin

Now configure the SAML settings in OneLogin:

1. Write the alias that you have created earlier and click **Save**.

<Screenshot url="https://cdn.appcircle.io/docs/assets/oneloginsettings2.png" />

2. Instead of writing all the settings of SAML, you can download the settings file from OneLogin and upload it. Click the **More Actions** button and click **SAML Metadata**.

<Screenshot url="https://cdn.appcircle.io/docs/assets/oneloginsettings3.png"/>

#### Step 3: Upload SAML Metadata to Appcircle

Now, upload the SAML metadata XML file to Appcircle to complete the configuration:

1. Navigate to the **Set up SAML SSO Provider** screen in Appcircle, which you accessed during the SSO setup in the "General Configuration Steps."
2. Upload the downloaded SAML metadata XML file to Appcircle.

<Screenshot url="https://cdn.appcircle.io/docs/assets/saml-upload-metadata.png" />

3. Ensure that the Redirect and SSO URLs are imported correctly. You can check if the X509 Certificate is imported correctly as well. If you want to enter multiple certificates you can separate them by using a comma between them. Please be aware that you need to remove any new lines or file headers from this edit box. This edit box only accepts a long base64 encoded string.

4. Click **Save** to finalize the SSO setup.

#### Step 4: Test the Integration

After configuring the settings, it’s crucial to test the OpenID Connect SSO integration:

:::caution

**Important:** When connecting your Identity Provider, use an incognito window to test the SSO integration. Only log off once you are sure you can log in with your SSO credentials. If the connection fails, review your settings before logging out.

:::

1. Open a incognito window in your browser and initiate a new login session.
2. On the login screen, click the **Login with SSO** button to start the SSO login process

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-loginbutton.png" />

3. Enter your SSO alias when prompted and click **Continue**.

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-alias.png" />

4. You will be redirected to the Auth0 login screen. Enter your Auth0 credentials.
5. After successful authentication, you will be redirected back to Appcircle.
6. If a user with your email already exists, you will be prompted to confirm account linking. Confirm account linking and verify it via the email sent to your registered email address.

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-linkaccount.png" />

7. Once you confirm the account linking, an email will be sent to your registered email address. 

<Screenshot url="https://cdn.appcircle.io/docs/assets/sso-confirmlink.png" />

8. Open the verification email and click the provided link to confirm your account.
9. After verification, you will be redirected back to the Appcircle dashboard, fully authenticated via SSO.

<Screenshot url="https://cdn.appcircle.io/docs/assets/empty-appcircle-dashboard.png" />

If the test is successful, your integration is complete, and you can start using OneLogin (SAML) as your identity provider for Appcircle.

</details>

## 5. Troubleshooting

This section provides a list of common issues that users might encounter during the SSO setup and how to resolve them.


<details>
  <summary>6.1 Common Issues and Resolutions</summary>

- **Misconfigured SAML Assertions:** Ensure that the SAML assertions are correctly configured with the appropriate attributes and claims. Incorrect settings here can lead to failed logins.
- **Incorrect Redirect URIs:** Verify that the Redirect URIs configured in your identity provider match the ones set in Appcircle. Mismatches can cause authentication failures.
- **Token Mismatches:** If you encounter token mismatches, ensure that the correct Client ID, Client Secret, and endpoints are configured in both Appcircle and the identity provider.
- **Metadata Import Issues:** If the metadata import fails, manually check the SAML metadata for formatting errors or missing elements that may cause issues during import.
- **SSO Alias Not Recognized:** Make sure the SSO alias entered matches the one configured in Appcircle. Any discrepancies could prevent successful authentication.
- **Account Linking Problems:** If account linking fails, verify that the user’s email address in the identity provider matches the one in Appcircle.

</details>

<details>
  <summary>6.2 Troubleshooting for Auth0 (OpenID Connect)</summary>

- **Callback URL Mismatch:** Ensure that the callback URL in Auth0 matches the one configured in Appcircle. This mismatch often causes authentication failures.
- **Invalid or Missing Redirect URIs:** Ensure that the redirect URIs in both Auth0 and Appcircle match exactly. Any mismatch, even in trailing slashes, can cause authentication to fail.
- **Invalid Client ID/Secret:** Verify that the Client ID and Secret are correctly entered in Appcircle’s SSO settings. Regenerate these values in Auth0 if needed.
- **Logs Don't Show Successful Login Event:** If the user successfully logs in with the identity provider, but the Appcircle logs do not show a successful login event, check the SAML Authentication Assertion returned by the IdP or analyze the HTTP trace for any discrepancies in Appcircle.
- **Misconfigured Scopes:** Ensure that the scopes requested in Appcircle match those defined in Auth0. Mismatches can lead to login failures.

</details>

<details>
  <summary>6.3 Troubleshooting for Auth0 (SAML)</summary>

- **Attribute Mapping Problems:** Verify that the attributes sent by Auth0 match those expected by Appcircle.
- **Token Mismatch:** Ensure the tokens issued by Auth0 match the expected format in Appcircle.
- **Incorrect Assertion Consumer Service (ACS) URL:** Verify that the ACS URL in Auth0 matches the one configured in Appcircle’s SSO settings.
- **SAML Assertion Issues:** Use tools like a SAML debugger to check the contents of the SAML assertion for correct format and expected values before entering them into Appcircle.
- **IdP Login Page Doesn't Display:** If the IdP login page fails to display, ensure the correct SSO URL is being used in Appcircle and that the binding method (HTTP-POST or HTTP-Redirect) is properly configured.
- **Certificate Issues:** Ensure the SAML certificate in Auth0 is valid and correctly configured. Invalid certificates can prevent proper authentication in Appcircle.

</details>

<details>
  <summary>6.4 Troubleshooting for Microsoft Entra ID (SAML)</summary>

- **Incorrect SAML Response:** Check that all required claims and attributes are configured correctly in Microsoft Entra ID.
- **Certificate Expiration:** Ensure that the SAML signing certificate used by Microsoft Entra ID is valid and not expired.
- **Misconfigured Claims or Attributes:** Ensure that the claims and attributes being sent from Microsoft Entra ID are correctly mapped and expected by Appcircle. Mismatches can lead to failed logins or incomplete user profiles.
- **Redirect Loop:** This often occurs due to incorrect reply URLs or session issues. Verify the reply URL in Microsoft Entra ID matches the one in Appcircle and that session cookies are correctly managed.
- **Invalid Certificate or Encryption Issues:** Ensure that the certificates used for signing and encryption are valid and correctly configured in both Microsoft Entra ID and Appcircle’s SSO settings. Expired certificates are a common cause of failures in SAML setups.
- **Unassigned Users:** Ensure that users are assigned to the enterprise application in Microsoft Entra ID. Unassigned users cannot authenticate through Appcircle.

</details>

<details>
  <summary>6.5 Troubleshooting for Okta (OpenID Connect)</summary>

- **Invalid Client ID/Secret:** Verify the Client ID and Secret in Appcircle match those configured in Okta.
- **Incorrect Scopes Configuration:** Ensure that the correct scopes, like `openid`, `profile`, and `email`, are requested by the client application and match those configured in Appcircle. Okta will reject requests with unsupported or misconfigured scopes.
- **Token Validation Issues:** Use Okta’s introspection endpoint for remote validation of access tokens to ensure they have not been revoked or expired in Appcircle’s SSO integration.
- **Key Rotation Problems:** Regularly update the public keys used by Okta in Appcircle’s SSO settings to ensure continuous validation of tokens, as Okta automatically rotates these keys multiple times a year.
- **Invalid Redirect URI:** Ensure that the redirect URI in Okta matches the one specified in Appcircle. Mismatches can cause authentication failures.
- **403 Forbidden Errors:** Ensure the user has the necessary permissions and that the application is set up correctly in Okta to prevent access issues in Appcircle.

</details>

<details>
  <summary>6.6 Troubleshooting for Okta (SAML)</summary>

- **Certificate Errors:** Verify that the SAML certificate used in Okta is valid and has not expired.
- **Incorrect ACS URL:** Ensure the Assertion Consumer Service (ACS) URL in Okta matches the one configured in Appcircle.
- **Signing and Encryption Issues:** Verify that both signing and encryption certificates are correctly configured and up to date in both Okta and Appcircle. Expired or incorrectly installed certificates are a common cause of SAML failures.
- **Misconfigured SAML Responses:** Use Okta’s SAML troubleshooting tools to validate the SAML response, ensuring that all required fields are present and correctly formatted before integrating with Appcircle.
- **Invalid SSO URL or Mismatched Entity IDs:** Confirm that the SSO URL and Entity ID configured in Okta are correctly set up in Appcircle’s SSO settings to prevent login issues or errors in the authentication process.
- **Clock Skew:** Ensure the system clocks of both Okta and Appcircle are synchronized to avoid timing issues in the authentication process.

</details>

<details>
  <summary>6.7 Troubleshooting for OneLogin (SAML)</summary>

- **SSO Errors Due to Incorrect URLs:** Ensure that the SAML Assertion Consumer Service (ACS) URL and other SSO URLs in OneLogin match those in Appcircle.
- **SAML Metadata Misconfiguration:** Ensure that the SAML metadata imported into OneLogin is current and accurately reflects Appcircle’s SSO requirements. Update the metadata periodically to avoid integration issues.
- **Incomplete Attribute Mapping:** Verify that all necessary user attributes are mapped from OneLogin to Appcircle to avoid incomplete user sessions or missing information.
- **Account Linking Failures:** Ensure that user email addresses match between OneLogin and Appcircle. Discrepancies in user data can prevent successful account linking.
- **Certificate Expiration:** Verify that the SAML signing certificate in OneLogin is valid and not expired to ensure seamless authentication with Appcircle.

</details>

<details>
  <summary>6.8 Troubleshooting for Keycloak (OpenID Connect)</summary>

- **Invalid Client ID/Secret:** Verify that the Client ID and Secret from Keycloak are correctly entered in Appcircle.
- **Incorrect Redirect URI:** Ensure that the redirect URIs match between Keycloak and Appcircle.
- **Incorrect Client Configuration:** Ensure that the client settings in Keycloak, including redirect URIs and client secrets, are correctly configured to match those in Appcircle’s SSO settings.
- **Key Rotation Issues:** Periodically check for key rotations in Keycloak and update the keys in Appcircle’s SSO configuration to avoid validation errors.
- **OIDC Token Mismatches:** Validate that the tokens issued by Keycloak match the expected format in Appcircle, including the correct scopes and audience claims.
- **Token Signature Verification Failures:** Ensure the public key in Appcircle matches the one used by Keycloak for token signing.

</details>

<details>
  <summary>6.9 Troubleshooting for Keycloak (SAML)</summary>

- **Certificate Mismatches:** Ensure the SAML certificate in Keycloak matches what Appcircle expects.
- **SAML Response Issues:** Verify that the NameID format and attribute mapping are configured correctly.
- **ACS URL Errors:** Ensure the Assertion Consumer Service (ACS) URL in Keycloak matches the one configured in Appcircle.
- **Assertion Signing Problems:** Ensure that the assertions are properly signed and that the correct signing algorithm is used in both Keycloak and Appcircle. Mismatches in signing algorithms can lead to failed authentication attempts.
- **SAML Assertion Format Issues:** Use a SAML debugging tool to validate the format and content of the SAML assertions before configuring them in Appcircle. Ensure that all required fields, such as the audience and recipient, are correctly set.
- **Misconfigured SAML Bindings:** Verify that the correct SAML binding method (e.g., POST or Redirect) is configured in both Keycloak and Appcircle to ensure smooth communication during the SSO process.
- **Invalid Certificate Configuration:** Ensure that the SAML signing certificate used in Keycloak is valid and correctly configured in Appcircle. Expired or incorrectly configured certificates can cause authentication failures.
- **Clock Synchronization Issues:** Ensure that the system clocks of both Keycloak and Appcircle are synchronized to prevent timing-related authentication errors, such as expired assertions.

</details>