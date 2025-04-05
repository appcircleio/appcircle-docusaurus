---
title: Domain Verification
description: Verify your domains for Appcircle organizations.
tags: [security, domain, verify]
---

import Screenshot from '@site/src/components/Screenshot';

# Domain Verification

Domain verification is a security process used to confirm ownership or control over a specific domain. It can currently be used to automatically verify user email addresses and accept pending invitations when users log in via SSO with an email that belongs to a verified domain. This is especially useful in cases where users don't have access to their email inbox or are unable to complete email-based verification.

Appcircle supports domain verification through DNS records, allowing you to confirm ownership of your domain by adding a specific DNS TXT record to your DNS provider. 

#### Which Domain Should You Verify?

You should verify the domain name of the SSO user’s email address.
For example, if the user's email is `user@example.com`, then you should verify `example.com`.

##### Advanced Information:

When using Entra ID B2B users, the user's email may appear as:
```
user_name_guestuserdomain.com#EXT#@yourdomain.onmicrosoft.com
```
In this case, you should verify `yourdomain.onmicrosoft.com` in Microsoft's DNS settings.

### Steps to Verify a Domain

**1.** Navigate to the My Organization > Security > Domain Verification section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5770-verify8.png' />

**2.** Enter the domain name to be verified. The domain name must be in a valid format (e.g., example.com).

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5770-verify2.png' />

**3.** Copy the provided DNS record and add it to your DNS provider as a TXT record, using the specified name (host) and value (data).

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5770-verify3.png' />

**4.** Click Verify to check if the record has been propagated.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5770-verify4.png' />

**5.** If the verification fails, retry after some time as DNS propagation may take time.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5770-verify5.png' />

:::info
Appcircle will periodically check the DNS record to ensure it still exists and remains accurate.

Users must have administrative access to their domain’s DNS settings to complete verification.

Please note that unauthorized changes to DNS records may result in domain verification failure.

Each domain can be verified by only one organization, but an organization can verify multiple domains.
:::

#### Validation Rules

- The domain name must be in a valid format (e.g., example.com).

- Special characters and improperly formatted domains will be rejected.

- If an invalid domain is entered, the verification process will not proceed.

### Enabling Auto-Verify Option in SSO

After configuring domain verification, you can enable the Auto Verify feature in the SSO configuration settings. This feature allows to automatically verify user email addresses and accept pending invitations when users log in via SSO using an email address associated with a verified domain. This is particularly useful in cases where users do not have access to their email inbox or are unable to complete email-based verification.

Go to your SSO configuration and enable the **Auto Verify User Email for Verified Domains** option.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5770-verify6.png' />

### Troubleshooting

- **DNS record value does not match expected value**: Ensure that the exact value provided by the system is entered in the DNS settings.

- **DNS propagation delay**: It may take up to 12-24 hours for the changes to take effect. Retry verification later.

- **Invalid domain format**: Ensure the domain is correctly formatted (e.g., example.com without protocols like http://).

- **Record already exists**: If an old verification record exists, remove it before adding the new one.

- **Invalid characters in domain name**: Avoid using special characters in domain entries.