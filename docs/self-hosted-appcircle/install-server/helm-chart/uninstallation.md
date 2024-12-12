---
title: Uninstallation
description: Learn how to uninstall the Appcircle server Helm chart deployment
tags: [self-hosted, helm, configuration, kubernetes]
sidebar_position: 50
---

import NeedHelp from '@site/docs/\_need-help.mdx';

If you want to uninstall the Appcircle server, you can just remove the Helm release from the Kubernetes cluster.

If you haven't changed the release name and namespace name while following the [Deploy Using Helm](/self-hosted-appcircle/install-server/helm-chart/installation/kubernetes.md#deploy-using-helm) section, you can run the command below to uninstall the Appcircle server.

```bash
helm uninstall -n appcircle appcircle-server
```

Helm uninstall doesn't delete the Appcircle server data stored in the persistent volumes. If you want to delete all the data of the Appcircle server, you can simply delete the namespace.

If you haven't changed the namespace name while following the [Deploy Using Helm](/self-hosted-appcircle/install-server/helm-chart/installation/kubernetes.md#deploy-using-helm) section, you can run the command below to delete all data of the Appcircle server.

```bash
kubectl delete namespace appcircle
```

<NeedHelp />
