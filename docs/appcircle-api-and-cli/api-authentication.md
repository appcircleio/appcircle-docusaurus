---
title: API Authentication
description: Learn how to authenticate with the Appcircle API
tags: [api, authentication, personal api token, api token, session token]
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';

# API Authentication

The Appcircle API supports authentication with a _Personal API Token_. The token for each user will have the same permissions with the user within the organization and each organization require a separate Personal API Token.

Alternatively, the Appcircle API also supports authentication with an _API Key_. API Keys are typically used for service-to-service or automation scenarios where the authentication is not tied to an individual user. Each API Key is associated with an organization and can be managed from the organization's security settings.

:::tip Generating Personal API Token and API Key
You can generate your Personal API Token or API Key within the security section of the Organization module.
- For detailed information on Personal API Tokens, please refer to [Personal API Token](/account/my-organization/security/personal-api-token) documentation.
- For API Keys, please refer to [API Keys](/account/my-organization/security/api-keys) documentation.
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
