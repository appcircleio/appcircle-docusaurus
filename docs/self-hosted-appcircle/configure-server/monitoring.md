---
title: Monitoring
description: Monitoring the Appcircle Server service logs and metrics with Grafana.
tags: [monitoring, logging, Grafana]
---

import Screenshot from '@site/src/components/Screenshot';
import SpacetechExampleInfo from '@site/docs/self-hosted-appcircle/configure-server/\_spacetech-example-info.mdx';
import RestartAppcircleServer from '@site/docs/self-hosted-appcircle/configure-server/\_restart-appcircle-server.mdx';
import DowntimeCaution from '@site/docs/self-hosted-appcircle/configure-server/\_appcircle-server-downtime-caution.mdx';

## Overview

This document provides instructions on how to access and use the monitoring system implemented for the self-hosted Appcircle server.

The monitoring system is designed to provide visibility into the application logs, enabling you to troubleshoot issues, monitor performance, and gain insights into the application's behavior.

The subsequent sections of this document will guide you through the process of accessing the Grafana web interface, navigating the log data.

:::info
To access and use the monitoring capabilities, you must be running Appcircle server version `3.15.0` or later.
:::

## Accessing to Grafana Web UI

<SpacetechExampleInfo />

:::info
We will use `.appcircle.spacetech.com` example URLs below. You should change this domain with your own Appcircle domain.
:::

The Grafana monitoring UI is accessible by default through the `monitor` subdomain. In our example, the full domain URL is `monitor.appcircle.spacetech.com`.

:::caution
You can face SSL errors while connecting to the `monitor` URL like `ERR_CERT_COMMON_NAME_INVALID`. That error indicates the SSL certificate of the Appcircle server doesn't include the `monitor` subdomain.

The recommended solution is to update the SSL certificate of the Appcircle server.
:::

Upon navigating to the Grafana login page, you should authenticate using the initial username and password specified in the global.yaml file of your project. To verify these credentials, you can execute the following command on the Appcircle server:

Change directory to Appcircle server.

```bash
cd appcircle-server
```

Print the Keycloak authentication credentials.

```bash
cat projects/spacetech/global.yaml | grep -A 5 "keycloak"
```

The example output below displays the initialUsername and initialPassword values. These credentials serve as your login information for the Grafana monitoring interface.

```yaml
keycloak:
  initialUsername: admin@spacetech.com
  initialPassword: SuperSecretPassword
```

## Retention Period of Logs

Retention period refers to the duration for which log data is stored before being deleted or archived. It's used to manage storage space, optimize system performance, and ensure compliance with regulatory requirements.

### Retention Period on Loki

The Appcircle server logs will be stored in the Loki. So the queries and filters that you run from the Grafana UI will run on the Loki side.

The logs in the loki should be cleaned automatically. By default, the retention period for the Appcircle server logs on the Loki side are 720 hours (30 days).

If you want to change this, you can edit the `global.yaml` of your project.

<DowntimeCaution />

```bash
vi ./projects/spacetech/global.yaml
```

Add or change the retention period variable.

```yaml
loki:
  retentionPeriod: 168h # 7 days
```

<RestartAppcircleServer />

### Retention on Systemd

The Appcircle server and other system services also transmit their logs to the Journald log driver. However, once Appcircle server logs are successfully forwarded to Loki, the local server logs become redundant and can be safely deleted.

If you wish to configure a maximum size limit for automatic log deletion on the Journald, you can modify the relevant configuration settings.

:::info
Modifying the Journald configuration requires elevated privileges with `sudo` permissions, as it involves altering system-level settings.
:::

Edit the Journald config file.

```bash
sudo vim /etc/systemd/journald.conf
```

Uncomment or add the `SystemMaxUse` variable in the configuration file and assign it the desired value, such as `200M` for a 200 megabyte limit.

```bash
SystemMaxUse=200M
```

Restart the Systemd journal service to apply the changes.

```bash
sudo systemctl restart systemd-journald
```

With this configuration change, the Journald log driver will now utilize a maximum of 200 megabytes of disk space for storing logs.

## Filtering Logs

After successfully authenticating with the Grafana user interface, you can commence filtering and exploring log data by navigating to the "Explore" menu.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2111-1-explore.png' />

To filter and view logs for a specific service, follow the steps outlined below. For instance, if you wish to examine the log entries pertaining to the `build` service:

1. Select `container` as label from `1`. box.
2. Select `spacetech-build-1` as value from `2`. box.
3. Select the date time you want to query from `3`. box.
4. After you set the query parameters, hit "Run query" button to see the logs.
5. Additionally, if you want to "follow" the logs in realtime, you can hit "Live" button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2111-2-filter-logs.png' />

Upon executing the query by clicking the "Run query" button, the log entries generated by the `spacetech-build-1` service will be displayed.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2111-3-view-logs.png' />

You can also filter words. For example you can filter any log line that contain "error" word.

1. Select the `container` and relevant container.
2. Change filter to `Line contains case insensitive` for a case insensitive search.
3. Write "error" to the input.
4. Select the date time and hit "Run query" button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2111-6-filter-errors.png' />

## Downloading and Sharing the Logs

If you want to download and share the logs after you [filter](#filtering-logs), you can the same UI.

1. Filter the logs according to your needs.
2. Hit the "Download" button from upper right corner of the logs.
3. Select `txt` as the format.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2111-4-download-logs.png' />

A file that contains the filtered logs will be downloaded to your local computer.

You can share that log file to troubleshoot the problems.

## Grafana User Management

It is important to note that the user accounts for the Appcircle Server and the Grafana monitoring interface are entirely separate and unrelated entities. There is no direct association or shared credentials between these two user management systems.

If you require additional users beyond the initial user account to have access to view log data, you can create new user accounts within the Grafana user management system.

To create a new user account, navigate to the "Administration" section of the Grafana interface, then access the "Users" menu. From there, click on the "New user" button to initiate the process of adding a new user.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2111-7-adding-users.png' />

Provide the necessary user information in the respective fields, and then click the "Create user" button to save and create the new user account.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2111-8-creating-user-menu.png' />

To grant administrative privileges to the user, click the "Change" button and toggle the "Grafana Admin" switch to the "Yes" position. Click "Change" again to confirm and save the updated permissions.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2111-9-make-it-admin.png' />

For more detailed information, you can check the official [Grafana User Management](https://grafana.com/docs/grafana/latest/administration/user-management/) documentation.
