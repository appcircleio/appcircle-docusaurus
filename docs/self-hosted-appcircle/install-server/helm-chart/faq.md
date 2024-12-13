---
title: Troubleshooting & FAQ for Appcircle Server and Runner
description: Troubleshooting and FAQ for Appcircle server and runner
tags: [troubleshooting, faq, self-hosted, kubernetes]
sidebar_position: 60
---

## Troubleshooting & FAQ

### When we try to login to the Appcircle server, we see `too many redirects` error from browser

This error usually happens when the pods can't resolve some of [the Appcircle server domains](/self-hosted-appcircle/install-server/helm-chart/installation/kubernetes.md#domain-name).

For the solution, please make sure that the domain name server of the worker nodes of the Kubernetes cluster can resolve the Appcircle server domain names.

### When we deploy the Helm chart, the `appcircle-server-webeventredis-master-0` pod is stuck in `CrashLoopBackOff` state

This error usually happens when you select a non-valid `Appcircle CA Certificate File` while [generating the configuration file](/self-hosted-appcircle/install-server/helm-chart/installation/kubernetes.md#create-configuration-file). Please make sure that the certificate you choose is the **root** certificate of the full-chain certificate.

:::tip

If you created the SSL/TLS certificate with LetsEncrypt, you should know that the `fullchain.pem` file doesn't include the root CA certificate by default.

:::

To fix the problem, you can edit the `values.yaml` file and upgrade the Helm chart.

```bash
helm upgrade appcircle-server appcircle/appcircle \
  --timeout 1200s \
  -n appcircle \
  -f values.yaml
```

:::caution
The `stateful` pods won't be recreated from a error state. This is known issue of Kubernetes.

You should delete the pods manually to fix this problem. The new updated pods will be created automatically. You can use the example commands below to delete the pods:

```bash
kubectl delete pods appcircle-server-webeventredis-master-0 -n appcircle && \
kubectl delete pods appcircle-server-webeventredis-replicas-0 -n appcircle && \
kubectl delete pods appcircle-server-webeventredis-replicas-1 -n appcircle
```

:::

### What should we do if the deployment hasn't been completed and timed out?

If the deployment hasn't completed and timed out after `1200` seconds:

- **Low Network Bandwidth or Insufficient Processing Power:** If the timeout occurred due to low network bandwidth or insufficient processing power, you can re-run the Helm deployment command as it is idempotent.

- **Configuration Issues:** If the timeout was caused by a configuration problem, you will need to troubleshoot the issue. Review your configuration settings and logs to identify and resolve any errors before attempting the deployment again.

:::tip
If you face a timeout due to configuration problems, it is better to re-install Appcircle freshly. Refer to the [Uninstalling Appcircle](/docs/self-hosted-appcircle/install-server/helm-chart/uninstallation.md) section for detailed instructions on how to uninstall and clean up the existing deployment before starting anew.
:::

### What should we do if we use an Ingress controller other then Nginx Ingress?

If you are using an ingress controller other than the Nginx Ingress controller, you should add an additional annotation to the `resource` ingress.

By default, Appcircle adds the [`upstream vhost`](https://github.com/kubernetes/ingress-nginx/blob/main/docs/user-guide/nginx-configuration/annotations.md#custom-nginx-upstream-vhost) annotation. You should add alternative annotation for your ingress controller.

For example, if you are using HAProxy as an Ingress controller, you should add the annotation to the `values.yaml` of the Appcircle Helm chart:

:::caution
`appcircle-server` below should be the Helm chart release name. In the installation document, we use `appcircle-server` for the release name. You should change it if you changed the release name. 
:::

```yaml
resource:
  ingress:
    annotations: 
      haproxy.org/set-host: "appcircle-server-minio:9000"
```

