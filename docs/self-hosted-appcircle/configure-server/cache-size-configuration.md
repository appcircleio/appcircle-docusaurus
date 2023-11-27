---
title: Cache Size Configuration
metaTitle: Cache Size Configuration
metaDescription: Cache Size Configuration
sidebar_position: 9
---

## Cache Size Configuration

Appcircle has a limit for cache sizes that can be pushed or pulled on the build workflows.

The `maxBodySize` parameter in the `global.yaml` file parameter allows you to configure the maximum cache file size that can be uploaded with the Cache Push component.

By default, the cache size is set to 4096m. However, you can increase or decrease this limit according to your needs by modifying the `global.yaml` file.

:::caution
Please note that this process will cause downtime.
:::

## Configuring the Appcircle Server

We are assuming that you have installed the Appcircle server with version `v3.10.0` or later.

To configure the `maxBodySize` parameter, you can follow the steps below:

- SSH into the Appcircle server.

- Go to the `appcircle-server` directory.

```bash
cd appcircle-server
```

- Edit the `global.yaml` file of your project.

:::info

The `spacetech` in the example codes below are example project name.

Please find your own project name and replace `spacetech` with your project name.

To see projects, you can check the `projects` directory.

```bash
ls -l ./projects
```

:::

```bash
vi ./projects/spacetech/global.yaml
```

- Find the `nginx` entry and add or edit the key named `maxBodySize` and set it to the desired value:

```yaml
nginx:
  maxBodySize: 5120m
```

If your `global.yaml` file does not have the `nginx` key, you can add it freely.

Replace `5120m` with the desired maximum cache size according to your needs. The size should be specified in megabytes (m).

- Export the new settings.

```bash
./ac-self-hosted.sh -n "spacetech" export
```

- Down the Appcircle server.

```bash
./ac-self-hosted.sh -n "spacetech" down
```

- Up the Appcircle server for the new changes to take effect

```bash
./ac-self-hosted.sh -n "spacetech" up
```

- Check the status of the Appcircle server

```bash
./ac-self-hosted.sh -n "spacetech" check
```

- Once your server is up and healthy, you can run the build that requires pushing a cache file larger than 4096m but less than 5120m.

- You can also reduce the default `maxBodySize` for security purposes. The choice is yours.
