---
title: Git Providers
metaTitle: Configure Git Providers
metaDescription: Configure Git Providers
sidebar_position: 1
---

# Overview

With default installation, self-hosted Appcircle comes with two git providers:

- Self-hosted Bitbucket
- Self-hosted GitLab

![](https://cdn.appcircle.io/docs/assets/be-850-default-git-providers.png)

But you're not limited with these options. You can configure other git providers and use them within your self-hosted appcircle, same as in cloud.

Following sections will give you more details about adding other git providers.

:::info

We're assuming that previously you reviewed or followed [install self-hosted appcircle](../install-server/docker#3-configure) section in docs, understood configuration made there and scenarios told there.

:::

:::caution

Current working directory is assumed `appcircle-server` for following steps. See [here](../install-server/docker#1-download) for installation details.

:::

:::caution

`global.yaml` configuration file is located under **project** folder.

- `projects/${YOUR_PROJECT}`

You can see an example project configuration from [here](../install-server/docker#3-configure).

:::

### Connecting to Private Repository via SSH

To enable "Connect via SSH" git provider option, add below configuration to `global.yaml`.

```yaml
build:
  oauths:
    ssh:
      enabled: true
```

![](https://cdn.appcircle.io/docs/assets/be-850-connect-via-SSH.png)

For more details about "Connect via SSH" usage, see related docs in [here](../../build/adding-a-build-profile/connecting-to-private-repository-via-ssh).

### Connecting to Public Repository

To enable "Connect to a Public Repository" git provider option, add below configuration to `global.yaml`.

```yaml
build:
  oauths:
    publicRepository:
      enabled: true
```

![](https://cdn.appcircle.io/docs/assets/be-850-connect-to-public-repository.png)

For more details about "Connect to a Public Repository" usage, see related docs in [here](../../build/adding-a-build-profile/connecting-to-public-repository).

### Applying Git Provider Changes

You can add git providers at [installation](../install-server/docker) steps or later when you need. Following sections will explain how to apply changes especially after installation.

Let's assume we want to enable both "Connect via SSH" and "Connect to a Public Repository" options. Then we need to add below section to our `global.yaml`.

```yaml
build:
  oauths:
    ssh:
      enabled: true
    publicRepository:
      enabled: true
```

If we do this at installation time then there is no extra step to take. These options will be enabled on first boot without any extra effort.

If we don't do the configuration at installation, then after editing `global.yaml` we need to apply below steps to activate changes.

:::info

We're assuming that previously you reviewed or followed [install self-hosted appcircle](../install-server/docker#3-configure) section in docs and applied example scenario.

Following steps are using example project as project naming, which was told there.

:::

1. Shutdown Appcircle server.

```bash
./ac-self-hosted.sh -n "spacetech" down
```

2. Apply configuration changes.

```bash
./ac-self-hosted.sh -n "spacetech" export
```

3. Boot Appcircle server.

```bash
./ac-self-hosted.sh -n "spacetech" up
```

On complete, refresh your browser and login to Appcircle with your account. You should see new git providers on repository connection page. :tada:

![](https://cdn.appcircle.io/docs/assets/be-850-sample-enable-both-options.png)
