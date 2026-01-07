---
title: License Configuration
description: Learn how to configure license for the Appcircle server
tags: [self-hosted, helm, configuration, kubernetes, openshift, license]
sidebar_position: 50
---

import NeedHelp from '@site/docs/\_need-help.mdx';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SampleReleaseNameInfo from '@site/docs/self-hosted-appcircle/install-server/helm-chart/configuration/\_sample-release-name-info.mdx';

## Overview

The Appcircle server comes with a default license to let you explore Appcircle if you have installed it with Helm to a Kubernetes cluster.

If you have purchased a license from Appcircle, you can follow this documentation to apply your license.

### Retrieving the Initial Organization ID

The initial organization ID is printed alongside the Helm output during installation. If you miss the initial output or need to retrieve the organization ID later, use the following command:

<SampleReleaseNameInfo />

<Tabs groupId="Platform">
  <TabItem value="kubernetes" label="Kubernetes" default>

```bash
kubectl get secret appcircle-server-auth-keycloak \
  -n appcircle \
  -o jsonpath="{.data.initialOrganizationId}" | base64 --decode && echo
```

  </TabItem>
  <TabItem value="openshift" label="OpenShift">

```bash
oc get secret appcircle-server-auth-keycloak \
  -n appcircle \
  -o jsonpath="{.data.initialOrganizationId}" | base64 --decode && echo
```

  </TabItem>
</Tabs>

### Creating a Secret for License Authentication

Create a secret that contains the `cred.json` file you received from Appcircle to authenticate the Appcircle license.

1. Save the `cred.json` file.

2. Create/update the secret named **`${releaseName}-auth-license`** with the **`credentialJson`** key:

<Tabs  groupId="Platform">
  <TabItem value="kubernetes" label="Kubernetes" default>

```bash
kubectl create secret generic appcircle-server-auth-license \
  -n appcircle \
  --from-literal=credentialJson="$(cat cred.json | base64 -w0)" \
  --save-config --dry-run=client -o yaml | kubectl apply -f -
```

  </TabItem>
  <TabItem value="openshift" label="OpenShift">

```bash
oc create secret generic appcircle-server-auth-license \
  -n appcircle \
  --from-literal=credentialJson="$(cat cred.json | base64 -w0)" \
  --save-config --dry-run=client -o yaml | oc apply -f -
```

  </TabItem>
</Tabs>

:::tip
Creating a secret for the license should be done once. Other license updates do not require repeating this step.
:::

### Updating the License

If your organization’s Appcircle server license has been updated and you need to apply the new license, you can upgrade the Appcircle server deployment using Helm:

```bash
helm upgrade appcircle-server appcircle/appcircle \
  -n appcircle  \
  -f values.yaml
```

<NeedHelp />