---
title: Enterprise App Store Customization
description: Learn how to configure Enterprise App Store
tags: [self-hosted, helm, configuration, kubernetes]
sidebar_position: 70
---

import Screenshot from '@site/src/components/Screenshot';
import NeedHelp from '@site/docs/\_need-help.mdx';
import ApplyHelmConfigurationChanges from '@site/docs/self-hosted-appcircle/install-server/helm-chart/configuration/\_apply-helm-configuration-changes.mdx';

## Overview

Some additional Enterprise App Store settings can be customized for self-hosted installations in order to make them more tailored to your users.

You can change how your store looks using the **[Customize](/enterprise-app-store/portal-customization)** screen in the Enterprise App Store module, just like you can with Appcircle Cloud.

For self-hosted specific settings, you should follow the documentation below.

## Custom Domain

To configure a custom domain for your Enterprise App Store, follow the instructions on the [Enterprise App Store settings page](/docs/enterprise-app-store/portal-settings.md#custom-domain).

## Tab Title Localization

You can change the Enterprise App Store tab title according to the language selected on the self-hosted Appcircle server.

For example, you can set a title for **TR** and a different title for **EN** language selection on browsers.

If you set titles from `values.yaml` by following the steps below, your title settings configured from the Enterprise App Store's "Customize" page will be overridden.

```yaml
store:
  store-web:
    extraEnvVars:
      - name: TR_STORE_TITLE
        value: "Uygulama Mağazası"
      - name: EN_STORE_TITLE
        value: "App Store"
```

<ApplyHelmConfigurationChanges />

<NeedHelp />