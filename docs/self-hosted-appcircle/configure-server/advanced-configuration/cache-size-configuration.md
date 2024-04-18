---
title: Cache Size Configuration
description: Learn how to configure the cache size limit in the Appcircle server
tags: [self-hosted, advanced configuration, cache size]
sidebar_position: 11
---

import SpacetechExampleInfo from '@site/docs/self-hosted-appcircle/configure-server/\_spacetech-example-info.mdx';

Appcircle has a limit for cache sizes that can be pushed or pulled on the build workflows.

The `maxBodySize` parameter in the `global.yaml` file allows you to configure the maximum cache file size that can be uploaded with the [Cache Push](/workflows/common-workflow-steps/#cache-push) component.

By default, the cache size is set to **4096m**. However, you can increase or decrease this limit according to your needs by modifying the `global.yaml` file.

:::caution
Please note that this process will cause downtime since it requires a restart of the Appcircle server.
:::

## Configuring the Appcircle Server

We are assuming that you have installed the Appcircle server with version `3.10.0` or later.

To configure the `maxBodySize` parameter, you can follow the steps below:

- Log in to Appcircle server with SSH or remote connection.

- Go to the `appcircle-server` directory.

```bash
cd appcircle-server
```

- Edit the `global.yaml` file of your project.

<SpacetechExampleInfo />

```bash
vi ./projects/spacetech/global.yaml
```

- Find the `nginx` entry, add or edit the key named `maxBodySize`, and set it to the desired value.

```yaml
nginx:
  maxBodySize: 5120m
```

If your `global.yaml` file does not have the `nginx` key, you can add it yourself.

Replace `5120m` with the desired maximum cache size according to your needs. The size should be specified in megabytes (m).

:::caution
Larger cache sizes require more disk space on the Appcircle server. So be cautious about allowing large cache sizes in your installation.
:::

- Shutdown Appcircle server.

```bash
./ac-self-hosted.sh -n "spacetech" down
```

- Apply configuration changes.

```bash
./ac-self-hosted.sh -n "spacetech" export
```

- Boot Appcircle server.

```bash
./ac-self-hosted.sh -n "spacetech" up
```

:::tip
You should check the status of the Appcircle server after boot for any possible errors.

```bash
./ac-self-hosted.sh -n "spacetech" check
```

:::

Once your server is up and healthy, you can run the build that requires pushing a cache file larger than 4096m but less than 5120m.

You can also reduce the default `maxBodySize` for security purposes.
