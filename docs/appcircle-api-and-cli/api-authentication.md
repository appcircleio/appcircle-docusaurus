---
title: API Authentication
description: Learn how to authenticate with the Appcircle API
tags: [api, authentication, personal api token, api token, session token]
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';

# API Authentication

The Appcircle API supports authentication with a _Personal API Token_. The token for each user will have the same permissions with the user within the organization and each organization require a separate Personal API Token.

:::tip Generating Personal API Token
You can generate your personal API token within the security section of the Organization module. For detailed information, please refer to [Personal API Token](/account/my-organization/security/personal-api-token) documentation.
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
