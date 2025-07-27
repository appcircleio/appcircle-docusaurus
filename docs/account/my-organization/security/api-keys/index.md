---
title: API Keys
description: Learn how to generate and manage your API Keys.
tags: [security, api key, token]
---

import Screenshot from '@site/src/components/Screenshot';

# API Keys

Appcircle provides a secure method to create and manage API keys for accessing its API. These tokens can be generated and scoped to match organizational requirements.

## Creating an API Key

To generate a new API key:

**1.** Click on the **Create a New API Key** button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6601-api4.png' />

**2.** Enter a name for your API key and select an expiry date.  
*Note: The expiry date cannot be modified after creation.*

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6601-api1.png' />

**3.** Select the **Organization** and the **Roles** that the API key should have access to.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6601-api2.png' />

**4.** Once the key is created, the **API key secret** will be shown **only once**. Copy and store it securely. After this, it will be encrypted and hidden. However, users can create a new key with the **same expiry date** if needed.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6601-api3.png' />

## Managing API Keys

You can view all your API keys under the API Keys section. The status of each key is indicated as either `Active` or `Expired`.

- **Manage**: Allows updating the **role scope** of the API key.  
  *Note: Updating roles does not require regenerating the API key or secret.*

- **Delete**: Permanently removes the API key from the system.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6601-api4.png' />

- Each API key includes an **auto-generated email** used for audit logging purposes.

:::tip 
This feature is also available for **sub-organizations**.
:::

## Using API Keys to Retrieve Access Tokens

The following script can be used to retrieve an access token using an API key name and secret:

```bash
set -e

API_KEY_NAME=apikey1
API_KEY_SECRET='your_secret'

echo "Retrieving access token for API key: $API_KEY_NAME"

response=$(curl --location 'https://auth.appcircle.io/auth/v1/api-key/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'name='"$API_KEY_NAME"'' \
--data-urlencode 'secret='"$API_KEY_SECRET"'')

ACCESS_TOKEN=$(echo "$response" | jq -r '.access_token')

echo "Access token retrieved: $ACCESS_TOKEN"
```