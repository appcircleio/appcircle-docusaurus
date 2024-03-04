---
title: Testing Distribution Configuration
metaTitle: Configure Testing Distribution
metaDescription: Configure Testing Distribution
sidebar_position: 13
---

import Screenshot from '@site/src/components/Screenshot';

## Overview

In this section, you will see how to configure Appcircle testing distribution web page.

## Configuring the Testing Distribution Logo

By default, if the Appcircle testing distribution link in the emails is expired or not available, users will be redirected to the testing distribution homepage.

In this homepage, you will see the Appcircle logo by default as you can see in the example below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2857-default-logo.png' />

You may change this logo with your company's logo using 'SVG' or 'PNG' files of the logo as you want.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2857-customized-logo.png' />

To configure this logo, you need to SSH into the Appcircle server and edit the `global.yaml` file of the project.

Also you need to copy the logo image to the Appcircle server before configuring.

:::caution
Please note that this process will cause downtime since it requires a restart of the Appcircle server.
:::

Locate the image file on the Appcircle server. You need to get the full path of the image.

If your logo image file name is `spacetech-logo.svg`, and it is in the current directory, you can run `realpath` command.

```bash
realpath spacetech-logo.svg
```

```output
/home/ubuntu/appcircle-server/spacetech-logo.svg
```

Copy the path of the logo, we will use it in the `global.yaml`.

Go to the `appcircle-server` directory.

```bash
cd appcircle-server
```

Shutdown the Appcircle server.

```bash
./ac-self-hosted.sh -n "spacetech" down
```

Edit the `global.yaml` file of your project.

:::info

The `spacetech` in the example codes below is an example project name.

Please find your own project name and replace `spacetech` with your project name.

To see the projects, you can list the `./projects` directory.

```bash
ls -l ./projects
```

:::

```bash
vi ./projects/spacetech/global.yaml
```

Check for the `testerWeb` key. If it doesn't exists, you can add it.

You should create a `logoSvg` key under the `testerWeb` entry and enter the path of the logo `SVG` file from the host server. See the example `global.yaml` part:

```yaml
testerWeb:
  logoSvg: /home/ubuntu/appcircle-server/spacetech-logo.svg
```

If your logo is a `PNG` file, then you should define `logoPng` key like in the example below.

```yaml
testerWeb:
  logoPng: /home/ubuntu/appcircle-server/spacetech-logo.png
```

After you have done configuring the `global.yaml`, you can `export` the new settings.

```bash
./ac-self-hosted.sh -n "spacetech" export
```

Run the Appcircle server with the new configuration.

```bash
./ac-self-hosted.sh -n "spacetech" up
```

Check the healthy of the services.

```bash
./ac-self-hosted.sh -n "spacetech" check
```

Now you can check the logo of the Appcircle testing distribution.

To check, simply navigate to the Appcircle server's 'dist' URL in your browser. If your 'dist' URL has not changed, it is most likely very similar to the one below.

```URL
https://dist.appcircle.spacetech.com
```
