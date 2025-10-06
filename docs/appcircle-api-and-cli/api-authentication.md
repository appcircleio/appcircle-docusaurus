---
title: API Authentication
description: Learn how to authenticate with the Appcircle API
tags: [api, authentication, personal api token, api token, session token]
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';

# API Authentication

The Appcircle API supports authentication with a _Personal Access Key_. The key for each user will have the same permissions with the user within the organization and each organization require a separate Personal Access Key.

Alternatively, the Appcircle API also supports authentication with an _API Key_. API Keys are typically used for service-to-service or automation scenarios where the authentication is not tied to an individual user. Each API Key is associated with an organization and can be managed from the organization's security settings.

:::tip Generating Personal Access Key and API Key
You can generate your Personal Access Key or API Key within the security section of the Organization module.
- For detailed information on Personal Access Keys, please refer to [Personal Access Key](/account-and-organization/my-organization/security/personal-access-key) documentation.
- For API Keys, please refer to [API Keys](/account-and-organization/my-organization/security/api-keys) documentation.
:::

### Using the Personal Access Key for API Authentication

For authentication, you need to [generate a Personal Access Token(PAT) from the Auth API using the Personal Acccess Key](https://api.appcircle.io/openapi/index.html?urls.primaryName=auth) and add the generated PAT along with an `Authorization` header in all API requests.

A curl-based API call sample is as follows:

First generate a PAT using the Auth API with the Personal Access Key specified as "your_access_key":

```bash
curl -X POST "https://auth.appcircle.io/auth/v3/token" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "personalAccessKey=your_access_key"
```

Then use the generated token specified as "Auth-Token-Goes-Here":

```bash
curl -X GET "https://api.appcircle.io/distribution/v2/profiles" -H  "accept: application/json" -H  "Authorization: Auth-Token-Goes-Here"
```

:::warning Personal API Token Renamed
The Personal Access Key was previously referred to as the Personal API Token. The old endpoint is still available, but it is recommended to migrate to the new version.
For reference, the old endpoint was:
```bash
curl -X POST "https://auth.appcircle.io/auth/v1/token" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "pat=Personal-API-Token""
```
:::

### API Documentation

Access the full API documentation and explore the endpoints available for your integration needs at:

https://api.appcircle.io/openapi/index.html
