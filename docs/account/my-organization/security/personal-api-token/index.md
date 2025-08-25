---
title: Personal API Token
description: Learn how to create personal API token in Appcircle
tags: [api, token, personal api token, api token, session token]
---

import Screenshot from '@site/src/components/Screenshot';

# Personal API Token

A Personal API Token (PAT) is a secure credential used for authentication when using Appcircle’s APIs. It inherits the permissions of your user account within the organization and is organization-specific—meaning you must generate a separate PAT for each organization you access.

## Generating/Managing the Personal API Tokens

To generate a Personal API Token, go to the [My Organization](/account/my-organization/profile-and-team/organization-management) screen in the Appcircle dashboard. After that, find the Security section from the left side menu. The Personal API Token section is located on the bottom right.

Press the "Generate Token" button to generate your first token.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5035-api1.png' alt="Generate Personal API Token"/>

The token will then be generated and displayed above the button. Please make sure that you save the token before navigating away from the page as it will be displayed only once for security reasons.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5035-api2.png' alt="Display Personal API Token" />

If you want to revoke a previously generated token, press "Revoke Token" and confirm. You can then generate a new token if you would like.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5035-api3.png' alt="Revoke Personal API Token"/>

:::caution Personal API Token for Sub-Organizations
To generate a PAT for a sub-organization, you must be added as a **member** of that sub-organization. Users **inherited** from a parent organization cannot generate a PAT. For additional details on [Organization](/account/my-organization/profile-and-team/organization-management#working-with-multiple-organizations) and [Team management](/account/my-organization/profile-and-team/team-management#managing-team-members), refer to the relevant documentation.
:::

:::info
PATs are only accessible within the organization where they were generated. However, a PAT created in the Root organization can also be used for sub-organizations.

You can pass the `subOrganization` parameter when obtaining an access token using a Root PAT.
:::

```bash
curl -X 'POST' \
  'https://auth.appcircle.io/auth/v2/token' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'pat=$pat' \
  -d 'scope=openid,profile,email'
  -d 'subOrganization={orgId}"
```

Please ensure that the endpoint you are using is v2.