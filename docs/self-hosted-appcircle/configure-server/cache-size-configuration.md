---
title: Cache Size Configuration
metaTitle: Cache Size Configuration
metaDescription: Cache Size Configuration
sidebar_position: 9
---

## Cache Size Configuration

The maxBodySize parameter in the `global.yaml` file parameter allows you to configure the maximum cache file size that can be uploaded with the Cache Push component.

By default, the cache size is set to 4096m. However, you can increase or decrease this limit according to your needs by modifying the `global.yaml` file.

:::caution
Please note that this process will cause downtime.
:::

To configure the `maxBodySize` parameter, follow these steps:

- Navigate to the `appcircle-server` directory where you have installed the Appcircle server.

```bash
cd appcircle-server
```

:::caution
Please replace the `spacetech` values in the example code block with your project name.

To find your project name, list the `./projects` directory.
:::

- Edit the `global.yaml` file for your project.

```bash
vi ./projects/spacetech/global.yaml
```

- Add a variable named `maxBodySize` and set it to the desired value, as shown in the example below.

```yaml
nginx:
  maxBodySize: 5120m
```

If your `global.yaml` file does not have the `nginx` parameter, add it.

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
