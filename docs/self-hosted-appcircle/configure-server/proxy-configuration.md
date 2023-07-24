---
title: Proxy Configuration
metaTitle: Configure Proxy Settings for Containers
metaDescription: Configure Proxy Settings for Containers
sidebar_position: 7
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Using Proxy On Appcircle Server

In this document, we will explore the configuration of a proxy server to enable internet connectivity from your Appcircle containers for accessing external resources.

We will cover Docker and Podman, providing step-by-step instructions to set up and utilize the proxy server effectively.

Using proxies on Appcircle containers ensures smooth connectivity to external resources.

### Down Your Appcircle Server

- At first, you should down your server and make the configuration for the overall stability of the host machine.

- Go to your `appcircle-server` folder.

```bash
cd ./appcircle-server
```

- Down the Appcircle server.

```bash
./ac-self-hosted.sh -n "spacetech" down
```

### Enable Proxy Settings On The Appcircle Server

For a typical proxy configuration, you need to know the arguments for these parameters:

- Username if the proxy has authentication. For example, `user`
- Password if the proxy has authentication. For example, `password`
- Hostname or IP of the proxy server. For example, `proxy.spacetech.com`
- Port of the proxy server. For example, `8080`

For next, you should enable proxy settings on the host server.

To do that you can follow the steps below:

- For non-shell processes, edit the `/etc/environment`.

```bash
sudo vi /etc/environment
```

- Add the content below to the `/etc/environment` file.

```env
HTTP_PROXY=http://user:password@proxy.spacetech.com:8080/
HTTPS_PROXY=http://user:password@proxy.spacetech.com:8080/
NO_PROXY=localhost,127.0.0.1

http_proxy=http://user:password@proxy.spacetech.com:8080/
https_proxy=http://user:password@proxy.spacetech.com:8080/
no_proxy=localhost,127.0.0.1
```

:::tip

#### `no_proxy` Configuration

`no_proxy` and `NO_PROXY` should be used for your corporate intranet services that should be kept away from the proxy.
You can add all the required domains or IPs separated by a comma. Below are some example cases that are common for a typical enterprise installation.

- Git provider (GitLab, Bitbucket, etc.) For example, `gitlab.spacetech.com`
- Proxy Repository (Nexus, Harbor, etc.) For example, `registry.spacetech.com`

:::

- For shell processes, edit `/etc/profile.d/proxy.sh`.

```bash
sudo vi /etc/profile.d/proxy.sh
```

- Add the content below to the `/etc/profile.d/proxy.sh` file.

```env
export HTTP_PROXY=http://user:password@proxy.spacetech.com:8080/
export HTTPS_PROXY=http://user:password@proxy.spacetech.com:8080/
export NO_PROXY=localhost,127.0.0.1

export http_proxy=http://user:password@proxy.spacetech.com:8080/
export https_proxy=http://user:password@proxy.spacetech.com:8080/
export no_proxy=localhost,127.0.0.1
```

:::caution
For system integrity, the proxy settings in here should be the same as the above settings in `/etc/environment`.
Also see the `no_proxy` tip explained [there](#no_proxy-configuration).
:::

:::info
Don't forget to change `user`, `password`, `proxy host`, `proxy port` and `no_proxy` for your needs while copying from above.
:::

:::caution
Currently we do not support proxies that requires to install it's own certificate.
:::

### Edit `no_proxy` Variable for Internal Container Network

In order not to break the connection of the containers with each other, we must add the service names to the `no_proxy` and `NO_PROXY` environment variables.

You can follow the steps below to edit these variables correctly.

- Go to your `appcircle-server` directory and create a shell script named `noProxy.sh`

```bash
cd appcircle-server/
vi noProxy.sh
```

- Add the content below to the `noProxy.sh` file.

```bash
#!/usr/bin/env bash
set -e

projectName="spacetech"
authUrl="auth.appcircle.spacetech.com"

compose_file="projects/${projectName}/export/compose.yaml"

hostname_values=$(yq eval '.services | to_entries | .[].value.hostname' "$compose_file" | grep -v "null" | sort -u)
hostname_values_comma=$(echo "$hostname_values" | sed ':a;N;$!ba;s/\n/,/g')

service_values=$(yq eval '.services | keys' "$compose_file" | sed 's/^..//' | sort -u)
service_values_comma=$(echo "$service_values" | sed ':a;N;$!ba;s/\n/,/g')

no_proxy_value_comma="$hostname_values_comma,$service_values_comma"

echo "no_proxy=${no_proxy_value_comma},${no_proxy}" >> /etc/environment
echo "NO_PROXY=${no_proxy_value_comma},${NO_PROXY}" >> /etc/environment

echo "export no_proxy=${no_proxy_value_comma},${no_proxy},${authUrl}" >> /etc/profile.d/proxy.sh
echo "export NO_PROXY=${no_proxy_value_comma},${NO_PROXY},${authUrl}" >> /etc/profile.d/proxy.sh

echo "NoProxy settings enabled successfully"
echo ""
echo "IMPORTANT!!!!"
echo "Please open a new terminal session to changes take effect."
```

:::info
This script needs yq as dependency while getting hostname and service names from `compose.yml`

Normally, yq is installed with [Appcircle server installation](../install-server/docker.md#2-packages).
:::

:::caution
Don't forget to change the project name `spacetech` and the url `auth.appcircle.spacetech.com` for your needs while copying from above.

You can find your auth url by following the steps:

- View your `mainDomain` variable in the `global.yaml` file.

```bash
yq '.external.mainDomain' projects/burakberk/global.yaml
```

- This value should be something like `.appcircle.spacetech.com`
- Add `auth.` as prefix. So your auth url should be `auth.appcircle.spacetech.com`

:::

- Give run permission to the script.

```bash
chmod +x ./noProxy.sh
```

- Run with sudo privileges

```bash
sudo ./noProxy.sh
```

:::caution
Don't forget to start a new terminal session for the changes to take effect.
:::

### Enable Proxy Settings On Container Engine

<Tabs groupId="operating-systems">
  <TabItem value="docker" label="Docker">
  
After you enabled proxy settings on the host server, you should also edit docker's configuration file to notify docker that there is proxy settings to use.

You can follow the steps below to enable proxy settings on docker engine:

- Cat the `no_proxy` variables of the server and copy it.

```bash
echo $no_proxy
```

- Edit the docker configuration file:

```bash
vi ~/.docker/config.json
```

- Add the your proxy settings to the configuration file like below. Paste your `no_proxy` variables to the `noProxy` section on the conf file.

```json
{
  "proxies": {
    "default": {
      "httpProxy": "http://user:password@proxy.spacetech.com:8080",
      "httpsProxy": "http://user:password@proxy.spacetech.com:8080",
      "noProxy": "...,web_event,webhook,localhost,127.0.0.1,gitlab.burakberk.dev,..."
    }
  }
}
```

  </TabItem>

  <TabItem value="podman" label="Podman">
  
  If you followed until here, you don't need take extra actions. 
  
  </TabItem>
</Tabs>

### Up Your Appcircle Server

After configuring the proxy settings on the host server, you can run your Appcircle server.

- Go to your `appcircle-server` folder.

```bash
cd ./appcircle-server
```

- Up the Appcircle server.

```bash
./ac-self-hosted.sh -n "spacetech" up
```

Your containers will be able to connect external resources through the proxy now.

### Maintenance of `no_proxy` env variables

Appcircle server is getting updates regularly and there might be a new container service in the `compose.yml` file.

To keep stability of the system, you should go back to [Edit no_proxy Settings for Internal Container Network step](#edit-no_proxy-variable-for-internal-container-network) and take the steps on each update.
