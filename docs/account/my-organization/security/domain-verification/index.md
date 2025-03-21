---
title: Domain Verification
description: Verify your domains for Appcircle organizations.
tags: [security, domain, verify]
---

import Screenshot from '@site/src/components/Screenshot';

# Domain Verification

The Domain Verification feature ensures that users have ownership of a domain before using it within the system.

This process involves adding a DNS record to the domain's configuration and verifying its correctness through the Appcircle.

### Steps to Verify a Domain

**1.** Navigate to the Domain Verification section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5770-verify8.png' />

**2.** Enter the domain name to be verified. The domain name must be in a valid format (e.g., example.com).

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5770-verify2.png' />

**3.** Copy the provided record and add it to the domain’s DNS settings.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5770-verify3.png' />

**4.** Click Verify to check if the record has been propagated.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5770-verify4.png' />

**5.** If the verification fails, retry after some time as DNS propagation may take time.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5770-verify5.png' />

:::info
The DNS propagation time can be configured on your DNS provider settings. Appcircle will keep running a check automatically for the accuracy of these configs.

Users must have administrative access to their domain’s DNS settings to complete verification.

Please note that unauthorized changes to DNS records may result in domain verification failure.
:::

:::tip Enabling Auto-Verify
After configuring the domain verification, you can enable the Auto Verify Feature on SSO configuration settings for going through verifying process to join an Appcircle organization. This feature can be especially useful for domain email addresses without an inbox.
:::
<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5770-verify6.png' />


#### Validation Rules

- The domain name must be in a valid format (e.g., example.com).

- Special characters and improperly formatted domains will be rejected.

- If an invalid domain is entered, the verification process will not proceed.

### Troubleshooting

- **DNS record value does not match expected value**: Ensure that the exact value provided by the system is entered in the DNS settings.

- **DNS propagation delay**: It may take up to 12-24 hours for the changes to take effect. Retry verification later.

- **Invalid domain format**: Ensure the domain is correctly formatted (e.g., example.com without protocols like http://).

- **Record already exists**: If an old verification record exists, remove it before adding the new one.

- **Invalid characters in domain name**: Avoid using special characters in domain entries.