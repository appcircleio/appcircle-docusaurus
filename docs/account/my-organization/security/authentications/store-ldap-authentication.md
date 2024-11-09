---
title: Enterprise Portal LDAP Authentication
description: Learn how to set up and manage LDAP login integration for your organization in Appcircle
tags: [account, my organization, ldap login, distribution, distribution profile, authentication, 2fa]
sidebar_position: 6
---

import Screenshot from '@site/src/components/Screenshot';

# Enterprise Portal LDAP Settings

This document serves as a helpful guide for setting up and managing LDAP (Lightweight Directory Access Protocol) login integration within our organizational system.
Whether you're new to LDAP or looking to streamline your authentication process, this document provides step-by-step instructions to ensure a smooth setup and management experience.

To get started, simply navigate to the **Security** page within our platform and click on the "Add New" button next to LDAP Login under the **Authentications** section.
From there, you'll be guided through the process of creating LDAP configurations, including filling in the necessary details and enabling Two Factor Authentication (2FA) for added security.

Once set up, LDAP Login allows you to control access to distributed links and adjust distribution authorization through the Distribution Profiles.
This means you can tailor access permissions according to your organization's specific needs.

If you ever need to remove LDAP Login integration, the document also provides clear instructions for doing so, ensuring that your system remains secure and up-to-date.

To start, go to [My Organization](/account/my-organization) > Security screen and press the **Add New** button next to LDAP Login under the **Authentications** section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/store-ldap-add-new.png' />

- The **Manage Testing Portal LDAP Login** window will open, click **Create New Authentication** button.

- The **Create New Authentication** window will open, presenting two options:
    - **Create New Authentication**
    - **Create From Existing Authentication**
You can create a new configuration or create one from an existing configuration. Click on the **Create New Authentication** section to create new configuration.
Please refer the [**Create From Existing LDAP Configuration**](/account/my-organization/security/authentications/store-ldap-authentication#create-from-existing-ldap-configuration).

<Screenshot url='https://cdn.appcircle.io/docs/assets/store-ldap-create-options.png' />

- Fill in the details of your LDAP Configurations

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-login3.png' />

- You can see that the Connect button has changed to the Manage button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/store-ldap-login4.png' />

- To access the LDAP integration settings, click the "Manage" button of the "LDAP Login". Then,  click **Manage Authentication** button and select the "Edit" button of the existing LDAP provider.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-login-configuration-edit.png' />

- The "Order" field in your LDAP configuration determines the priority or sequence in which providers are utilized when conducting a user lookup.
  Providers are entities responsible for retrieving user information from LDAP servers.
  Specifying the order allows you to prioritize certain providers over others, ensuring efficient user lookup operations.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-login-order.png' />

:::info

Provider A: Order: 1

Provider B: Order: 2

In this example, when conducting a user lookup, Appcircle will first attempt to retrieve information from "Provider A" before falling back to "Provider B".

:::

- The "Connection Pooling" option in your LDAP configuration determines whether Appcircle should utilize connection pooling for accessing the LDAP server.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-login-connection-pooling.png' />

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

## Create From Existing LDAP Configuration

  Appcircle allows you to create a new SSO configuration based on an existing one, ensuring a smooth and efficient setup experience. 
 
- Navigate to the **Organization > Security > Authentications** section on your dashboard.
- Select the **Add New** on the **Enterprise Portal LDAP Login**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/distribute-ldap-manage-button.png' /> 

- Select the **Create New Authentication** and then select the **Create From Existing Configuration**.

Existing LDAP configurations will be listed on the screen. Select one, and click on **Next** to proceed.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-create-from-existing.png' /> 

- On the Create LDAP Configuration screen, fill in the **Name** and **Credential** fields (all other values are prefilled). Customize as needed, then click **Save**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-login3.png' />

## Deleting LDAP Login

- To delete, go to the [My Organization](/account/my-organization) > Security screen and press the Manage button next to LDAP Login under the Authentications section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-login10.png' />

- Click the Remove button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-login11.png' />

- Type the alias’s name to confirm deletion and click the Delete button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ldap-login12.png' />
