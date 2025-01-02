---
title: Ingress Configuration
description: Learn how to configure Ingress
tags: [self-hosted, helm, configuration, kubernetes]
sidebar_position: 60
---

import NeedHelp from '@site/docs/\_need-help.mdx';
import ApplyHelmConfigurationChanges from '@site/docs/self-hosted-appcircle/install-server/helm-chart/configuration/\_apply-helm-configuration-changes.mdx';

## Overview

The Appcircle Helm chart includes an Ingress controller, specifically ingress-nginx, which is enabled by default. For production environments, it is recommended to use your own Ingress controller for better control and customization.

## Appcircle Default Ingress-NGINX Configuration

The default `ingress-nginx` configuration in the `values.yaml` file includes several parameters that apply globally to the Ingress controller. These configurations can be adjusted as needed to fit your deployment requirements. If you are using your own Ingress controller, you can configure these values globally or on a per-Ingress basis for Appcircle ingresses.

Default Configurations in `values.yaml` of the Appcircle server Helm chart:

```yaml
ingress-nginx:
  controller:
    config: 
      proxy-body-size: '4096m'
      client-body-buffer-size: '128k'
      proxy-connect-timeout: '600'
      proxy-send-timeout: '600'
      proxy-read-timeout: '600'
      proxy-buffer-size: '128k'
      proxy-buffers-number: '4'
      proxy-busy-buffers-size: '128k'
```

You can change the default values of the Ingress controller that is installed with the Appcircle Helm chart as your needs dictate.

<ApplyHelmConfigurationChanges />

## Configuring Ingress Annotations

Adding per-Ingress annotations is recommended for external Ingress controllers. By setting annotations per Ingress, you can fine-tune the behavior of specific Appcircle services without impacting the entire Ingress controller.

Example Ingress configurations for `values.yaml` of the Appcircle server Helm chart:

```yaml
# For APK, IPA, build artifact uploads from browsers and Appcircle runners
apigateway:
  ingress:
    annotations:
      # For Ingres-Nginx Controller
      nginx.ingress.kubernetes.io/proxy-connect-timeout: "600"
      nginx.ingress.kubernetes.io/proxy-read-timeout: "600"
      nginx.ingress.kubernetes.io/proxy-send-timeout: "180"
      nginx.ingress.kubernetes.io/proxy-buffer-size: "128k"
      nginx.ingress.kubernetes.io/proxy-buffers-number: "4"
      nginx.ingress.kubernetes.io/proxy-busy-buffers-size: "128k"
      nginx.ingress.kubernetes.io/proxy-body-size: "4096m"
      nginx.ingress.kubernetes.io/client-body-buffer-size: "128k"

# For build cache uploads from Appcircle runners
resource:
  ingress:
    annotations:
      # For Ingres-Nginx Controller
      nginx.ingress.kubernetes.io/proxy-connect-timeout: "600"
      nginx.ingress.kubernetes.io/proxy-read-timeout: "600"
      nginx.ingress.kubernetes.io/proxy-send-timeout: "180"
      nginx.ingress.kubernetes.io/proxy-buffer-size: "128k"
      nginx.ingress.kubernetes.io/proxy-buffers-number: "4"
      nginx.ingress.kubernetes.io/proxy-busy-buffers-size: "128k"
      nginx.ingress.kubernetes.io/proxy-body-size: "4096m"
      nginx.ingress.kubernetes.io/client-body-buffer-size: "128k"
```

:::tip
If you are using an ingress controller other than `ingress-nginx`, please refer to the documentation for your specific ingress controller to find the relevant configurations. Each ingress controller may have different annotations and settings to achieve similar functionality.
:::

<ApplyHelmConfigurationChanges />

<NeedHelp />