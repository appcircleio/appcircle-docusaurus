---
title: Customize Enterprise Store
metaTitle: Customize Enterprise Store
metaDescription: Customize Enterprise Store
sidebar_position: 3
---

# Customize Your Enterprise Store


### Customizing Appearance

You can customize the appearance of your store by going to Customize section.

![](<https://cdn.appcircle.io/docs/assets/entstore-customize.png>)

### Advanced Settings

**Authentication**

You can also add a username and password for your store and change your store's domain. You must set two different usernames and passwords for live and beta apps. The username of the live and beta section must be different. 

![](<https://cdn.appcircle.io/docs/assets/entstore-settings.png>)

**Custom Domain**

It's possible to use a custom domain for the Enterprise Store. You need to have the following to create a custom domain

- A custom domain that you can create a CNAME record.
- SSL Certificate that is exported as a p12 or pfx file.

**Creating CNAME Record**

Open your DNS provider's website and add a CNAME with the below details

**Name:** Your subdomain name. Ex. *store*

**Destination:** _**store-domain.appcircle.io**_

The below screenshot shows an example configuration screen from Cloudflare.

![](<https://cdn.appcircle.io/docs/assets/entstore-cname.png>)


**Updating Settings**

After creating the DNS settings, type your custom domain name, select your certificate and update the configuration. DNS changes can take time to propagate. You may have to wait a few minutes or hours to see the redirect.

![](<https://cdn.appcircle.io/docs/assets/entstore-customdomain.png>)

