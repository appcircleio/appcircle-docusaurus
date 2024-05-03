---
title: Authenticate with Netrc
description: Authenticate with Netrc in your Appcircle workflows
tags: [netrc, authentication, git, curl]
---

import Screenshot from '@site/src/components/Screenshot';

# Authenticate with Netrc

The `.netrc` file contains login and initialization information used by the auto-login process. You can use this component to add credentials for hosts such as your repositories or external hosts. Git automatically recognizes the `.netrc` file. However, if you want to use the `.netrc` file with curl, you need to append the `-n` command line parameter. You may also use the `--netrc-optional` parameter if you don't always use the `.netrc` file with curl.

### Prerequisites

There is no mandatory step before the **Authenticate with Netrc** step.

:::warning
Please note that you should use this step before your **Git Clone** step. If you want to connect to a repository that requires access permission or pull a private dependency, please pay attention to the step order.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2792-net_order.png ' />

### Input Variables

You can find all the parameters required for this step in the table below, with their descriptions in detail.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2792-net_inputs.png' />

:::warning
When using the **Authenticate with Netrc** component, you need to specify a token or password in the `$AC_NETRC_PASS` parameter within the component. For security reasons, we recommend using [**Enviroment Variables**](https://docs.appcircle.io/environment-variables/) in steps where you need to specify the token and password.
:::

| Variable Name        | Description                                                                                                                      | Status   |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `$AC_NETRC_HOSTNAME` | Specifies the hostname of the server where the username and password will be used, for example, `github.com`.                    | Required |
| `$AC_NETRC_USER`     | Specifies the username of the host.                                                                                              | Required |
| `$AC_NETRC_PASS`     | The password or the `authentication-token`/`access-token` in the respective field, will be used by the host to authenticate you. | Required |

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-netrc-component
