---
title: Personal Access Key
description: Learn how to create personal API token in Appcircle
tags: [api, token, personal access key, personal api token, personal access token, pat]
---

import Screenshot from '@site/src/components/Screenshot';

# Personal Access Key

A Personal Access Key is a secure credential used for obtaining a Personal Access Token (PAT) which is used for authentication when using Appcircle’s APIs. It inherits the permissions of your user account within the organization and is organization-specific—meaning you must generate a separate Personal Access Key for each organization you access.

## Generating/Managing the Personal Access Keys

To generate a Personal Access Key, go to the [My Organization](/account/my-organization/profile-and-team/organization-management) screen in the Appcircle dashboard. After that, find the Security section from the left side menu. The Personal Access Key section is located on the bottom right.

Press the "Generate Key" button to generate your first key.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5035-api1.png' alt="Generate Personal Access Key"/>

The key will then be generated and displayed above the button. Please make sure that you save the key before navigating away from the page as it will be displayed only once for security reasons.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5035-api2.png' alt="Display Personal API Token" />

If you want to delete a previously generated key, press "Delete Key" and confirm. You can then generate a new access key if you would like.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5035-api3.png' alt="Revoke Personal API Token"/>

:::caution Personal Access Key for Sub-Organizations
To generate a Personal Access Key for a sub-organization, you must be added as a **member** of that sub-organization. Users **inherited** from a parent organization cannot generate a Personal Access Key. For additional details on [Organization](/account/my-organization/profile-and-team/organization-management#working-with-multiple-organizations) and [Team management](/account/my-organization/profile-and-team/team-management#managing-team-members), refer to the relevant documentation.
:::

:::info
Personal Access Keys are only accessible within the organization where they were generated. However, a Personal Access Key created in the Root organization can also be used for sub-organizations.

You can pass the `subOrganization` parameter when obtaining a Personal Access Token(PAT) using a Root Personal Access Key.
:::

```bash
curl -X 'POST' \
  'https://auth.appcircle.io/auth/v3/token' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'personalAccessKey=your_access_key' \
  -d 'scope=openid,profile,email'
  -d 'subOrganization={orgId}"
```

Please ensure that the endpoint you are using is v2.

:::warning Personal API Token Renamed
The Personal Access Key was previously referred to as the Personal API Token. The old endpoint is still available, but it is recommended to migrate to the new version.
For reference, the old endpoint was:
```bash
curl -X 'POST' \
  'https://auth.appcircle.io/auth/v2/token' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'pat=$pat' \
  -d 'scope=openid,profile,email'
  -d 'subOrganization={orgId}"
```
:::