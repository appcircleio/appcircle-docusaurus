---
title: API Authentication
description: Learn how to authenticate with the Appcircle API
tags: [api, authentication, personal api token, api token, session token]
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';

# API Authentication

The Appcircle API supports authentication with a _Personal API Token_. The token for each user will have the same permissions with the user within the organization and each organization require a separate Personal API Token.

### Generating/Managing the Personal API Tokens

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

### Using the Token for API Authentication

For authentication, you need to [generate a session token from the Auth API using the Personal API Token](https://api.appcircle.io/openapi/index.html?urls.primaryName=auth) and add the generated session token value along with an `Authorization` header in all API requests.

A curl-based API call sample is as follows:

First generate an authorization token using the Auth API with the Personal API Token specified as "Personal-API-Token":

```bash
curl -X POST "https://auth.appcircle.io/auth/v1/token" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "pat=Personal-API-Token"
```

Then use the generated auth token specified as "Auth-Token-Goes-Here":

```bash
curl -X GET "https://api.appcircle.io/distribution/v2/profiles" -H  "accept: application/json" -H  "Authorization: Auth-Token-Goes-Here"
```

### API Documentation

Access the full API documentation and explore the endpoints available for your integration needs at:

https://api.appcircle.io/openapi/index.html
