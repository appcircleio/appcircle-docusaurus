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

Inside the `helper-tools` directory, there is a bash script file called `no-proxy.sh`.

:::caution

The `no-proxy.sh` helper tool exists in self-hosted server versions `3.7.1` or later.

If you have an older version installed, please [upgrade](../update.md) your self-hosted server to a newer version. If upgrading is not possible, you should contact us for support.

:::

- Execute the script with sudo privileges and give your project as argument.

```bash
sudo ./helper-tools/no-proxy.sh ${YOUR_PROJECT}
```

For example if your project name is "spacetech", you should run the command like below.

```bash
sudo ./helper-tools/no-proxy.sh spacetech
```

:::caution
You must run the script from the parent directory of the `no-proxy.sh` script.

Be aware that if you run the script like `./no-proxy spacetech`, it will fail.
:::

- Restart your terminal session.

:::caution
Don't forget to start a new terminal session after you run command above for the changes to take effect.
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
