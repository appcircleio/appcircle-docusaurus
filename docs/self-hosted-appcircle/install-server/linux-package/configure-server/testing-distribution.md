---
title: Testing Distribution Customization
description: Customize the Testing Distribution on Self-hosted Installations
tags: [testing distribution, customize, self-hosted]
sidebar_position: 13
---

import Screenshot from '@site/src/components/Screenshot';

# Customize the Testing Distribution on Self-hosted Installations

Some additional Testing Distribution settings can be customized for self-hosted installations in order to make them more tailored to your users.

For self-hosted specific settings, you should follow the documentation below.

## Testing Portal Logo

By default, if the shared app link in the emails is expired or not available, users will be redirected to the Testing Portal homepage. And on this homepage, users will see the Appcircle logo, as you can see in the example below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2857-default-logo.png' />

You can change this logo with your company's assets using SVG or PNG files of the logo as you want.

To configure the testing portal logo, you need to SSH into the Appcircle server and edit the `global.yaml` file of the project.

Also, you need to copy the logo file to the Appcircle server before starting configuration.

:::caution
Be aware that this will cause a downtime on the Appcircle server.
:::

- Log in to Appcircle server with SSH or remote connection.

- Locate the image file on the Appcircle server and find out the full path of the logo file.

For example, assume that your logo file is `spacetech-logo.svg`, and it is in the current working directory. 

You should run the `realpath` command to get absolute path of the file as below.

```bash
realpath spacetech-logo.svg
```

Sample output can like below:

```bash
/home/ubuntu/appcircle-server/spacetech-logo.svg
```

We will use that path in the `global.yaml` file.

- Go to the `appcircle-server` directory.

```bash
cd appcircle-server
```

:::info

The `spacetech` in the example codes below are example project name.

Please find your own project name and replace `spacetech` with your project name.

To see projects, you can check the `projects` directory.

```bash
ls -l ./projects
```

:::

- Shutdown Appcircle server.

```bash
./ac-self-hosted.sh -n "spacetech" down
```

- Edit the `global.yaml` file of your project.

```bash
vi ./projects/spacetech/global.yaml
```

Check for the `testerWeb` key. If it does not exist in the `global.yaml`, you should add it.

You should create a `logoSvg` key under the `testerWeb` and enter the path of the logo (SVG) file that we got before.

See the example `global.yaml` section below that's compatible with our sample logo file.

```yaml
testerWeb:
  logoSvg: /home/ubuntu/appcircle-server/spacetech-logo.svg
```

If your logo is a PNG file, then you should set the file path to the `logoPng` key, like in the example below.

```yaml
testerWeb:
  logoPng: /home/ubuntu/appcircle-server/spacetech-logo.png
```

:::info
If you declare both of the `logoPng` and `logoSvg` in the `global.yaml`, then the **PNG** image will be used as the logo on the Testing Portal.
:::

- Apply configuration changes.

```bash
./ac-self-hosted.sh -n "spacetech" export
```

- Start Appcircle server.

```bash
./ac-self-hosted.sh -n "spacetech" up
```

:::tip
You should check the status of the Appcircle server after boot for any possible errors.

```bash
./ac-self-hosted.sh -n "spacetech" check
```

You should see the message: _"All services are running successfully."_

:::

To see the new configuration updates on the Testing Portal, follow the steps below:

- Navigate to the Appcircle server's `dist` URL in your browser.
  - For example, `https://dist.appcircle.spacetech.com`

You can get more information about `dist` subdomain from the [DNS Settings](https://docs.appcircle.io/self-hosted-appcircle/install-server/linux-package/installation/docker#4-dns-settings) document.
