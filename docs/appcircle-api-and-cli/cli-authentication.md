---
title: CLI Authentication
description: Learn how to authenticate with the Appcircle CLI
tags: [authentication, cli token, session token]
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';

### Appcircle CLI

Appcircle CLI is a unified command-line tool that provides access to Appcircle platform features, enabling you to manage your projects, builds, and more directly from your terminal.

You can install the Appcircle CLI from npm:

```bash
npm install -g @appcircle/cli
```

or yarn:

```bash
yarn global add @appcircle/cli
```

https://www.npmjs.com/package/@appcircle/cli

You can find more information and the open source code of the CLI on GitHub as follows:

https://github.com/appcircleio/appcircle-cli

### Authentication Methods

The Appcircle CLI supports two authentication methods:

1. **Personal Access Token (PAT)** - Recommended for individual users
2. **API Key** - Suitable for organization-level access

### Login with Personal Access Token (PAT)

Personal Access Tokens provide a secure way to authenticate with Appcircle CLI without exposing your account credentials. 

To authenticate using a Personal Access Token:

```bash
appcircle login pat --token "your-personal-access-token-here"
```

:::tip

For generating Personal API Token, please refer to [API Authentication](/appcircle-api-and-cli/api-authentication#generatingmanaging-the-personal-api-tokens) documentation.

:::

### Login with API Key

API Keys provide organization-level authentication, ideal for automated systems and shared environments. Unlike PATs tied to individual users, API Keys belong to the organization and remain valid regardless of user account changes.

To authenticate using an API Key:

```bash
appcircle login api-key --name "my-api-key" --secret "my-secret"
```

For organization-specific access, you can also specify the organization ID:

```bash
appcircle login api-key --name "my-api-key" --secret "my-secret" --organization-id "org-123"
```

:::tip

For creating and managing API keys, please refer to [API Keys](/account/my-organization/security/api-keys).

:::

### Logout

To securely log out and clear your stored authentication credentials from the CLI, please use following command:

```bash
appcircle logout
```

### Authentication Behavior

The Appcircle CLI maintains a single active session and prevents multiple concurrent logins to ensure security and avoid credential conflicts.


- If you're already logged in and try to login again, you'll see a "You are already logged in" message
- You must logout first before logging in with different credentials

### Interactive Mode

In interactive mode (`appcircle -i`), authentication options are grouped under "Authentication (Login/Logout)" menu:

1. Select "Authentication (Login/Logout)" from the main menu
2. Choose "Login" or "Logout" from the submenu
   - When choosing **Login**, you can authenticate using:
     - **API Key**
     - **Personal Access Token (PAT)**

### Examples

```bash
# Login with Personal Access Token
appcircle login pat --token "your-personal-access-token-here"

# Login with API Key
appcircle login api-key --name "my-api-key" --secret "my-secret"

# Login with API Key and specific organization
appcircle login api-key --name "my-api-key" --secret "my-secret" --organization-id "org-123"

# Logout from your current session
appcircle logout
```

### Environment Variable

After successful authentication, the CLI stores your access token locally. You can also manually set the `AC_ACCESS_TOKEN` or `AC_API_KEY_TOKEN` environment variable if needed for other tools or scripts.