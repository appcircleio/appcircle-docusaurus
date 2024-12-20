---
title: Request Size Configuration
description: Learn how to configure max body sizes
tags: [self-hosted, helm, configuration, kubernetes]
sidebar_position: 60
---

import NeedHelp from '@site/docs/\_need-help.mdx';

## Overview

In Appcircle, there are scenarios where the client upload size might exceed the default limit of `4096MB` for the Nginx Ingress controller for a single request body size. To accommodate larger file uploads or if you wish to adjust this setting according to your needs, you can configure the maximum allowed body size in your `values.yaml` file.

```yaml
# For APK, IPA, build artifact uploads from browsers and Appcircle runners
apigateway:
  ingress:
    annotations:
      # For Nginx Ingress Controller
      nginx.ingress.kubernetes.io/proxy-body-size: 1024m
      # For HAProxy Kubernetes Ingress Controller
      haproxy.ingress.kubernetes.io/body-size: 1024m

# For build cache uploads from Appcircle runners
resource:
  ingress:
    annotations:
      # For Nginx Ingress Controller
      nginx.ingress.kubernetes.io/proxy-body-size: 1024m
      # For HAProxy Kubernetes Ingress Controller
      haproxy.ingress.kubernetes.io/body-size: 1024m
```

<NeedHelp />