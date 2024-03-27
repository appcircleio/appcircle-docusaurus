---
title: Enterprise App Store
metaTitle: Customize the Enterprise App Store on Self-hosted Installations
metaDescription: Customize the Enterprise App Store on Self-hosted Installations
sidebar_position: 14
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

# Customize the Enterprise App Store on Self-hosted Installations

Some additional Enterprise App Store settings can be customized for self-hosted installations in order to make them more tailored to your users.

You can change how your store looks using the **[Customize](../../enterprise-appstore/customize-ent-store.md)** screen in the Enterprise App Store module, just like you can with Appcircle Cloud.

For self-hosted specific settings, you should follow the documentation below.

## Tab Title Localization

You can change the Enterprise App Store tab title according to the language selected on the self-hosted Appcircle server.

For example, you can set a title for **TR** and a different title for **EN** language selection on browsers.

:::info
Appcircle server version v3.12.1 or later is required for this feature.
:::

:::caution
Be aware that this will cause a downtime on the Appcircle server.
:::

If you set titles from `global.yaml` by following the steps below, your title settings configured from the Enterprise App Store's "Customize" page will be overridden.

- Log in to Appcircle server with SSH or remote connection.

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

- Add the `lang` parameter to the `storeWeb` entry.

:::caution
The `storeWeb` key should already have been in the `global.yaml` file.

You just need to add the `lang` key and other sub-keys to that section.

The `global.yaml` should have only one `storeWeb` key for proper working.
:::

```yaml
storeWeb:
  external:
    subdomain: store
  customDomain:
    enabled: true
    domain: store.spacetech.com
  lang:
    TR_STORE_TITLE: Uygulama Mağazası
    EN_STORE_TITLE: App Store
```

- Export the new settings.

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

To see the new configuration updates on the store, follow the steps below:

- Go to the Enterprise App Store page of your organization with a browser.
  - For example, `store.spacetech.com`

- Check the tab title. For our sample configuration,
  - If the language is **TR** selected, then you should see "Uygulama Mağazası" in the tab title.
  - If the language is **EN** selected, then you should see "App Store" in the tab title.
