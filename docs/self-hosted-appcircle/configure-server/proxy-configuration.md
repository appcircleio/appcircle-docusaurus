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

### Enable Proxy Settings On The Appcircle Server

First, you should enable proxy settings on the host server.

To do that you can follow the steps below:

- For non-shell processes, edit the `/etc/environment`.

```bash
sudo vi /etc/environment
```

- Add the content below to the `/etc/environment` file.

```env
HTTP_PROXY=http://user:password@proxy.spacetech.com:8080/
HTTPS_PROXY=http://user:password@proxy.spacetech.com:8080/
NO_PROXY=localhost,127.0.0.1,gitlab.spacetech.com,registry.spacetech.com

http_proxy=http://user:password@proxy.spacetech.com:8080/
https_proxy=http://user:password@proxy.spacetech.com:8080/
no_proxy=localhost,127.0.0.1,gitlab.spacetech.com,registry.spacetech.com
```

- For shell processes, edit `/etc/profile.d/proxy.sh`.

```bash
sudo vi /etc/profile.d/proxy.sh
```

- Add the content below to the `/etc/profile.d/proxy.sh` file.

```env
export HTTP_PROXY=http://user:password@proxy.spacetech.com:8080/
export HTTPS_PROXY=http://user:password@proxy.spacetech.com:8080/
export NO_PROXY=localhost,127.0.0.1,gitlab.spacetech.com,registry.spacetech.com

export http_proxy=http://user:password@proxy.spacetech.com:8080/
export https_proxy=http://user:password@proxy.spacetech.com:8080/
export no_proxy=localhost,127.0.0.1,gitlab.spacetech.com,registry.spacetech.com
```

:::info
Don't forget to change `user`, `password`, `proxy host`, `proxy port` and `no_proxy` for your needs while copying from above.
:::

:::caution
Currently we do not support proxies that requires to install it's own certificate.
:::

### Edit `no_proxy` Variable for Internal Container Network

In order not to break the connection of the containers with each other, we must add the service names to the `no_proxy` env variable.

You can follow the steps below to edit `no_proxy`.

- Go to your `appcircle-server` directory and create a shell script names `noProxy.sh`

```bash
cd ~/appcircle-server/
vi noProxy.sh
```

- Add the content below to the `noProxy.sh` file.

```bash
#!/usr/bin/env bash
set -e
compose_file="projects/spacetech/export/compose.yaml"

hostname_values=$(yq eval '.services | to_entries | .[].value.hostname' "$compose_file" | grep -v "null" | sort -u)
hostname_values_comma=$(echo "$hostname_values" | sed ':a;N;$!ba;s/\n/,/g')

service_values=$(yq eval '.services | keys' "$compose_file" | sed 's/^..//' | sort -u)
service_values_comma=$(echo "$service_values" | sed ':a;N;$!ba;s/\n/,/g')

no_proxy_value_comma="$hostname_values_comma,$service_values_comma"

echo "no_proxy=${no_proxy_value_comma},${no_proxy}" >> /etc/environment
echo "NO_PROXY=${no_proxy_value_comma},${NO_PROXY}" >> /etc/environment

echo "export no_proxy=${no_proxy_value_comma},${no_proxy},auth.appcircle.spacetech.com" >> /etc/profile.d/proxy.sh
echo "export NO_PROXY=${no_proxy_value_comma},${NO_PROXY},auth.appcircle.spacetech.com" >> /etc/profile.d/proxy.sh

echo "NoProxy settings enabled successfully"
echo ""
echo "IMPORTANT!!!!"
echo "Please open a new terminal session to changes take effect."
```

:::caution
Don't forget to change the project name `spacetech` and the url `auth.appcircle.spacetech.com` for your needs while copying from above.
:::

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

### Run Your Appcircle Server

After configuring the proxy settings on the host server, you can run your Appcircle server.

Your containers will be able to connect external resources through the proxy now.
