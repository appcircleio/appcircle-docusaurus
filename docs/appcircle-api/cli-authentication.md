---
title: CLI Authentication
description: Learn how to authenticate with the Appcircle CLI
tags: [authentication, cli token, session token]
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';

### Using the Personal API Token for CLI Authentication

For authentication, you need to generate a session token from the [Appcircle CLI](https://github.com/appcircleio/appcircle-cli#appcircle-command-line-interface) using the Personal API Token and add the generated session token value as an environment variable.

Using the Appcircle CLI, create a full access API token using the following command with the Personal API Token specified as "pat":

```bash
appcircle login ${pat}
```

Then copy the result and set it as the `AC_ACCESS_TOKEN` environment variable.