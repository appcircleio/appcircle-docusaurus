---
title: Authanticate with Netrc
metaTitle: Authanticate with Netrc
metaDescription: Authanticate with Netrc
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';

# Authanticate with Netrc

The `.netrc` file contains login and initialization information used by the auto-login process. You can use this component to add credentials for hosts such as your repositories or external hosts. Git automatically recognizes the .netrc file. However, if you want to use the .netrc file with curl, you need to append the `-n` command line parameter. You may also use the `--netrc-optional` parameter if you don't always use the `.netrc` file with curl.

:::caution
Note that you should use this step before your Git Clone step. If you want to connect to a repo that requires access permission or pull a private dependency, please pay attention to the step order.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2792-net_order.png ' />

## Input Variables

The parameters required for this step to work are listed in detail below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2792-net_inputs.png' />

:::warning
When using the Netrc component, you need to specify a token or password in the `$AC_NETRC_PASS` parameter in the component. For security reasons, we recommend using **Enviroment Variables** in steps where you need to specify token and password.
:::

| Variable Name                 | Description                                    | Required |
|-------------------------------|------------------------------------------------|----------|
| `$AC_NETRC_HOSTNAME`          | Specifies the hostname of the server where the username and password will be used, for example, `github.com`.| ✅ |
| `$AC_NETRC_USER`              | Specifies the username of the host. | ✅ |
| `$AC_NETRC_PASS`              | The password or the authentication-token/access-token in the respective field which will be used by the host to authenticate you. | ✅ |

https://github.com/appcircleio/appcircle-netrc-component
