---
title: Self-Hosted Enterprise Store
metaTitle: Self-Hosted Enterprise Store
metaDescription: Self-Hosted Enterprise Store
sidebar_position: 14
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

# Customize Your Enterprise Store

In this page, you can see some titles to configure and customize your Enterprise Store of the self-hosted Appcircle server.

## Change Tab Title by Language

You can change the Enterprise Store tab titles according to the language selected on **self-hosted Appcircle servers** only.

For example you can set a title for **TR** and a different title for **EN** language selection on browsers.

Appcircle server version v3.12.1 or later is required for this feature.

If you set titles from `global.yaml` by following the steps below, your title setting configured from the Enterprise Store's "Customize" page will be overridden.

:::warning

Be aware that this will cause an downtime on the Appcircle server.

:::

To customize this, you need to `SSH` into the Appcircle Server Linux machine and follow the steps below:

- Go into the `appcircle-server` directory.

```bash
cd appcircle-server
```

- List the projects and find yours.

```bash
ls  -l ./projects
```

- Down the Appcircle server.

:::info

**"spacetech"** in the below command is an example project name. Please replace with your own project name.

:::

```bash
./ac-self-hosted.sh -n "spacetech" down
```

- Edit the `global.yaml` file of your project.

```bash
vim ./projects/spacetech/global.yaml
```

- Add the `lang` parameter to the `storeWeb` entry.

:::info
The `storeWeb` key should already be in the `global.yaml` file.

You just need to add `lang`, `TR_STORE_TITLE` and `EN_STORE_TITLE` keys.
:::

```yaml
storeWeb:
  external:
    subdomain: store
  customDomain:
    enabled: true
    domain: store.spacetech.com
  lang:
    TR_STORE_TITLE: Turkey Store
    EN_STORE_TITLE: UK Store
```

- Export the new settings.

```bash
./ac-self-hosted.sh -n "spacetech" export
```

- Up the Appcircle server.

```bash
./ac-self-hosted.sh -n "spacetech" up
```

- Check if the Appcircle server is healthy.

```bash
./ac-self-hosted.sh -n "spacetech" check
```

Now your Appcircle server and the Enterprise Store is ready.

To test the new configuration:

- Please head to the Enterprise Store page of your organization with a browser, for example `store.appcircle.spacetech.com`.

- Check the tab title. If the language is **TR**, you should see "Turkey Store" for example.

- Change the language from the upper right corner and check the tab title again. It should be "UK Store" according to the sample configuration.
