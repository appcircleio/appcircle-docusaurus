---
title: Proxy Configuration
metaTitle: Configure Proxy Settings for Containers
metaDescription: Configure Proxy Settings for Containers
sidebar_position: 7
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

In this document, we will explore the configuration of a proxy server to enable internet connectivity from your Appcircle containers for accessing external resources.

We will cover Docker and Podman, providing step-by-step instructions to set up and utilize the proxy server effectively.

Using proxies on Appcircle containers ensures smooth connectivity to external resources.

:::info

We're assuming that previously you reviewed or followed [install self-hosted appcircle](../install-server/docker.md#3-configure) section in docs and applied example scenario.

Following steps are using example project as project naming, which was told there.

:::

## 1. Stop Appcircle Server

At first, you must shut down your server and configure it when it is stopped for the overall stability of the host machine.

- Go to the `appcircle-server` folder.

```bash
cd appcircle-server
```

- Stop the server.

```bash
./ac-self-hosted.sh -n "spacetech" down
```

## 2. Configure Proxy for the Server

For a typical proxy configuration, you need to know the arguments for these parameters:

- Username if the proxy has authentication. For example, `user`
- Password if the proxy has authentication. For example, `password`
- Hostname or IP of the proxy server. For example, `proxy.spacetech.com`
- Port of the proxy server. For example, `8080`

:::info

If your proxy server has no authentication, you should ignore the `user` and `password` values in the below sample codes and configurations.

:::

:::info

You can also use the IP of the proxy server if it does not have a dedicated domain name.

:::

Next, you should enable proxy settings on the host server.

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

### `no_proxy` Configuration

`no_proxy` and `NO_PROXY` should be used for your corporate intranet services that should be kept away from the proxy.
You can add all the required domains or IPs separated by a comma. Below are some example cases that are common for a typical enterprise installation.

- Git provider (GitLab, Bitbucket, etc.) For example, `gitlab.spacetech.com`
- Proxy Repository (Nexus, Harbor, etc.) For example, `registry.spacetech.com`

:::

- For shell processes, edit the `/etc/profile.d/proxy.sh`.

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

- Close the terminal and open a new session.

:::caution
To make the changes take effect, please open a brand new terminal session.

Otherwise, you won't succeed in the following steps.
:::

:::info
Don't forget to change `user`, `password`, proxy `host`, proxy `port`, and `no_proxy` settings for your needs while copying from above.
:::

:::caution
Currently we do not support proxies that requires to install it's own certificate.
:::

### Edit `no_proxy` for Internal Container Network

In order not to break the connection of the containers with each other, we must add the service names to the `no_proxy` and `NO_PROXY` environment variables.

You can follow the steps below to edit these variables correctly.

- Go to the `appcircle-server` folder.

```bash
cd appcircle-server
```

- Create a shell script named `noProxy.sh`.

```bash
vi noProxy.sh
```

- Add the content below to the `noProxy.sh` script.

```bash
#!/usr/bin/env bash
set -e

projectName="burakberk"

main_domain=$(yq '.external.mainDomain' ./projects/${projectName}/global.yaml)
api_domain="api${main_domain}"
auth_domain="auth${main_domain}"
dist_domain="dist${main_domain}"
hook_domain="hook${main_domain}"
my_domain="my${main_domain}"
resource_domain="resource${main_domain}"
store_domain="store${main_domain}"

custom_store_domain=$(yq '.storeWeb.customDomain.domain' ./projects/${projectName}/global.yaml)

internal_domains="${api_domain},${auth_domain},${dist_domain},${hook_domain},${my_domain},${resource_domain},${store_domain},${custom_store_domain}"
compose_file="projects/${projectName}/export/compose.yaml"

hostname_values=$(yq eval '.services | to_entries | .[].value.hostname' "$compose_file" | grep -v "null" | sort -u)
hostname_values_comma=$(echo "$hostname_values" | sed ':a;N;$!ba;s/\n/,/g')

service_values=$(yq eval '.services | keys' "$compose_file" | sed 's/^..//' | sort -u)
service_values_comma=$(echo "$service_values" | sed ':a;N;$!ba;s/\n/,/g')

no_proxy_value_comma="$hostname_values_comma,$service_values_comma,$no_proxy,$internal_domains"
new_no_proxy="$(echo "$no_proxy_value_comma" | tr ',' '\n' | sort -u | tr '\n' ',')"

sed -i "s/^no_proxy=.*/no_proxy=$new_no_proxy/" /etc/environment
sed -i "s/^NO_PROXY=.*/NO_PROXY=$new_no_proxy/" /etc/environment

sed -i "s/^export no_proxy=.*/export no_proxy=$new_no_proxy/" /etc/profile.d/proxy.sh
sed -i "s/^export NO_PROXY=.*/export NO_PROXY=$new_no_proxy/" /etc/profile.d/proxy.sh

echo "No_Proxy settings enabled successfully."
echo ""
echo "IMPORTANT!"
echo "Please open a new terminal session to changes take effect."
```

:::info
The above script needs `yq` as a dependency while getting hostnames and services from `compose.yaml`.

Normally, `yq` is expected to be installed within the Appcircle [server installation](../install-server/docker.md#2-packages) steps.
:::

:::caution
Don't forget to change the project name `spacetech` for your needs while copying from above.
:::

- Give execute permission to the script.

```bash
chmod +x noProxy.sh
```

- Execute the script with sudo privileges.

```bash
sudo ./noProxy.sh
```

- Close the terminal and open a new session.

:::caution
To make the changes take effect, please open a brand new terminal session.

Otherwise, you won't succeed in the following steps.
:::

## 3. Enable Settings on the Container Engine

<Tabs groupId="operating-systems">
  <TabItem value="docker" label="Docker">
  
After you enable proxy settings on the host server, you must also edit the Docker's configuration file to notify the container runtime engine that there are proxy settings to use.

You can follow the steps below to enable proxy settings on the Docker:

- Print the value of the `no_proxy` variable to the terminal and copy it.

```bash
echo $no_proxy
```

- Edit the Docker configuration file. It creates if it does not exist.

```bash
vi ~/.docker/config.json
```

- Add the proxy settings to the configuration file like below. Paste the copied `no_proxy` variable to the `noProxy` section on the configuration file.

```json
{
  "proxies": {
    "default": {
      "httpProxy": "http://user:password@proxy.spacetech.com:8080",
      "httpsProxy": "http://user:password@proxy.spacetech.com:8080",
      "noProxy": "localhost,127.0.0.1"
    }
  }
}
```

:::caution
The Docker file `config.json` might exist on the system. If that's the case, then you should **only add the `proxies` section** of the JSON above to the configuration file.
:::

:::caution
For system integrity, the proxy settings in here should be the same as the above settings in `/etc/environment`.
Also see the `no_proxy` tip explained [there](#no_proxy-configuration).
:::

The configuration becomes active after saving the file, you don’t need to restart Docker. However, the configuration only applies to new containers, and doesn’t affect existing containers.

So, if you stop the server as the first step in this document, then you can go on with the next step. If not, it's time to [stopping the server](#1-stop-appcircle-server) before going on.

  </TabItem>

  <TabItem value="podman" label="Podman">
  
  If you followed until here, you don't need to take extra actions for the Podman container engine.
  
  </TabItem>
</Tabs>

## 4. Start Appcircle Server

After configuring the proxy settings on the host, you can start your Appcircle server.

- Go to the `appcircle-server` folder.

```bash
cd appcircle-server
```

- Start the server.

```bash
./ac-self-hosted.sh -n "spacetech" up
```

Your containers will be able to connect to external resources through the proxy now.

## Maintenance of `no_proxy` Variables

The Appcircle server is getting updates regularly, and there might be a new container service in the `compose.yaml` file.

To maintain the stability of the system, you should go back to the [Edit `no_proxy` for Internal Container Network](#edit-no_proxy-for-internal-container-network) step and re-apply the operations done there on every upgrade.
