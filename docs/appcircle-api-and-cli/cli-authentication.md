---
title: CLI Authentication
description: Learn how to authenticate with the Appcircle CLI
tags: [authentication, cli token, session token]
sidebar_position: 3
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

### Using the Personal API Token for CLI Authentication

For authentication, you need to generate a session token from the [Appcircle CLI](https://github.com/appcircleio/appcircle-cli#appcircle-command-line-interface) using the Personal API Token and add the generated session token value as an environment variable.

:::tip

For generating Personal API Token, please refer to [API Authentication.](/appcircle-api-and-cli/api-authentication#generatingmanaging-the-personal-api-tokens)

:::

Using the Appcircle CLI, create a full access API token using the following command with the Personal API Token specified as "pat":

```bash
appcircle login ${pat}
```

Then copy the result and set it as the `AC_ACCESS_TOKEN` environment variable.