---
title: Monitoring
description: Monitoring the Appcircle Server service logs and metrics with Grafana.
tags: [monitoring, logging, grafana]
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

:::caution
The log monitoring system is for viewing the logs of the running Appcircle Server services. If you are having issues about starting the Appcircle Server services, you should use other CLI tools for troubleshooting and resolving the issues.

You may not access to the monitoring UI if services are not running healthy.
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

- Update the environment variable `PATH` with the required dependencies.

```bash
export PATH=$PATH:$(pwd)/deps/bin
```

Print the Keycloak authentication credentials.

```bash
yq '.keycloak.initialUsername' ./projects/spacetech/export/.global.yaml && \
yq '.keycloak.initialPassword' ./projects/spacetech/export/.global.yaml
```

The example output below displays the `initialUsername` on the first line and `initialPassword` on the second line. These credentials serve as your login information for the Grafana monitoring interface.

```text
admin@spacetech.com
SuperSecretPassword
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

### Configuring Log Retention with Systemd and Syslog

Proper log management is crucial for maintaining system performance and ensuring compliance with policies. 

This section outlines how to determine whether your system uses systemd or syslog as the log driver and how to configure log retention accordingly.

First, identify whether systemd or syslog is being used as the primary log driver on your system.

To check if systemd is forwarding logs to syslog, use the following command:
```bash
grep "ForwardToSyslog" /etc/systemd/journald.conf
```

- If the output shows `#ForwardToSyslog=yes`, `ForwardToSyslog=yes` or `#ForwardToSyslog=No`, this indicates that [logs are being forwarded to `syslog`](#configuring-log-rotation-with-syslog) for further processing.

- If the output shows `ForwardToSyslog=no`, this indicates that [`systemd` is handling the logs](#configuring-log-rotation-with-systemd) without forwarding them to `syslog`.

Depending on the output, proceed to the relevant configuration section below.

#### Configuring Log Rotation with Syslog

If your logs are forwarded to syslog, you'll need to configure `logrotate` to manage the rotation and compression of log files such as `/var/log/messages` and `/var/log/syslog`.

##### Identify the responsible `logrotate` configuration:

First, find out which `logrotate` configuration file is responsible for managing the rotation of these log files:

```bash
grep -RE "/var/log/(syslog|messages)" /etc/logrotate.d/
```

The output should indicate which file handles the rotation, typically `/etc/logrotate.d/rsyslog` or `/etc/logrotate.d/syslog`:

```output
/etc/logrotate.d/rsyslog:/var/log/syslog
/etc/logrotate.d/rsyslog:/var/log/messages
```

##### Edit the `logrotate` configuration

Open the configuration file for editing:

```bash
sudo vi /etc/logrotate.d/rsyslog
```

You should see a configuration similar to the following:

```text {12-13,20-22} showLineNumbers
/var/log/mail.info
/var/log/mail.warn
/var/log/mail.err
/var/log/mail.log
/var/log/daemon.log
/var/log/kern.log
/var/log/auth.log
/var/log/user.log
/var/log/lpr.log
/var/log/cron.log
/var/log/debug
/var/log/messages
/var/log/syslog
{
        rotate 4
        weekly
        missingok
        notifempty
        sharedscripts
        postrotate
                /usr/lib/rsyslog/rsyslog-rotate
        endscript
}
```

Before making additional configurations, remove the existing lines for `/var/log/syslog` and `/var/log/messages` to avoid conflicts.

Next, copy the lines between `postrotate` and `endscript` — these commands instruct the `rsyslog` service to handle log file rotation properly. We will use the copied line in the configuration below.

##### Modify the configuration for daily log rotation

Add the following configuration at the top of the rsyslog configuration file to rotate the log files daily:

:::info
We are editing the same configuration file which is `/etc/logrotate.d/rsyslog` in the example above.

Please add the lines below to the top of your existing configuration file.
:::

```text
/var/log/messages
/var/log/syslog
{
    rotate 7
    daily
    missingok
    notifempty
    compress
    delaycompress
    postrotate
        /usr/lib/rsyslog/rsyslog-rotate
    endscript
}
```

After you add the configuration above to your `logrotate` configuration file, you should update the `postrotate ... endscript` block and paste the copied block from the [previous step](#edit-the-logrotate-configuration).

:::caution
The `postrotate ... endscript` block might differ from system to system, depending on how `rsyslog` or other logging services are configured. 

When editing the `logrotate` configuration, ensure you paste the exact `postrotate` line from your original configuration file. This guarantees the correct service is reloaded after the rotation.
:::

##### Save and apply the configuration

Once the configuration is complete, save the file. `logrotate` will now handle the rotation of `/var/log/syslog` and `/var/log/messages` on a daily basis.

The added configuration in the `/etc/logrotate.d/rsyslog` file ensures that log files such as `/var/log/syslog` and `/var/log/messages` are rotated daily. Here's what each directive means:

- `rotate 7`: Keeps the last 7 rotated log files. Older files are deleted.
- `daily`: Rotates the log files every day.
- `missingok`: Ignores errors if the log file is missing.
- `notifempty`: Does not rotate the log file if it is empty.
- `compress`: Compresses the rotated log files to save space.
- `delaycompress`: Delays the compression of the most recent rotated log file until the next rotation. This ensures that the most recent log is available in an uncompressed format for easier access.
- `postrotate ... endscript`: The commands between these directives are executed after log rotation. In this case, the rsyslog service is reloaded to start writing to the new log file.

##### Validating the `logrotate` configuration

To ensure that the `logrotate` configuration is valid and will work as expected, you can use the following command:

:::caution
If the `logrotate` configuration file is different on your system, please update the path in the example command below.
:::

```bash
sudo logrotate -d /etc/logrotate.d/rsyslog
```

This runs logrotate in debug mode, where it simulates the rotation process and outputs what actions it would take, but without making any actual changes. This allows you to verify that the configuration is correct.

To force log rotation and apply the new configuration immediately, use the following command:

```bash
sudo logrotate --force /etc/logrotate.d/rsyslog
```

This command forces the rotation of logs according to the configuration specified in `/etc/logrotate.d/rsyslog`.

After forcing the log rotation, you can check if the rotation was successful by listing the log files:

```bash
ls -lh /var/log/syslog* /var/log/messages*
```

You should see the following:

- The original log files (`/var/log/syslog` and `/var/log/messages`) should be much smaller, indicating that the old logs have been rotated.
- You should see files like `/var/log/syslog.1.gz` and `/var/log/messages.1.gz`, showing that the previous day's logs have been rotated and compressed.

If everything is as expected, the log rotation has been successful.

:::tip
After you configure the `logrotate`, the existing and already rotated log files (`messages.1` or `messages-20240721`) won't be affected, deleted or compressed by the `logrotate`.

You can simple compress the files if you want to save to use later or delete them if you need to save disk space.
:::

##### Handling the "Insecure Permissions" error

When configuring `logrotate`, you might encounter the following error:

```bash
error: skipping "/var/log/rsyslog" because parent directory has insecure permissions (It's world writable or writable by group which is not "root") Set "su" directive in config file to tell logrotate which user/group should be used for rotation.
```

To resolve this error, you need to add the `su` directive in your `logrotate` configuration. This directive tells `logrotate` which user and group to use when rotating the logs, ensuring the operation is performed securely.

Open the logrotate configuration file:

```bash
sudo vi /etc/logrotate.d/rsyslog
```

Add the following line just before the section that handles /var/log/messages and /var/log/syslog:

```bash
su root adm
var/log/messages
/var/log/syslog
...
```

This line specifies that `logrotate` should run as the `root` user and the `adm` group, ensuring that the log rotation process has the necessary permissions.

#### Configuring Log Rotation with Systemd

The Appcircle server and other system services also transmit their logs to the Journald log driver. However, once Appcircle server logs are successfully forwarded to Loki, the local server logs become redundant and can be safely deleted.

If you wish to configure a maximum size limit for automatic log deletion on the Journald, you can modify the relevant configuration settings.

:::info
Modifying the Journald configuration requires elevated privileges with `sudo` permissions, as it involves altering system-level settings.
:::

Edit the Journald config file.

```bash
sudo vi /etc/systemd/journald.conf
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

## Disable the Monitoring Services

The monitoring services have been activated in the default configuration. However, you can disable them when you need to and then re-enable them again.

If you need to disable the monitoring services of the Appcircle server, edit the `global.yaml` file of your project and set the `monitoring.enabled` parameter to `false`.

<DowntimeCaution/>

<SpacetechExampleInfo/>

- Go to the `appcircle-server` directory.

```bash
cd appcircle-server
```

- Edit the `global.yaml` file of your project.

```bash
vi ./projects/spacetech/global.yaml
```

- Add or update the `monitoring.enabled` parameter as below.

```yaml
monitoring:
  enabled: false
```

:::tip
If you can't find the `monitoring` parameter in the `global.yaml` file, you can add it manually at the end of the `global.yaml`.
:::

<RestartAppcircleServer/>

When you run the `check` command, you should see that the logging service is not running, as below:

```text
Appcircle logging service is not running.
All services are running successfully. Project name is spacetech
```

When you need to re-enable the monitoring services again, you can remove `monitoring` from `global.yaml` or set its value to `true`. After that, you should follow the Appcircle server restart steps above to apply the configuration changes.

:::info

Disabling the Appcircle monitoring services does not disable the Appcircle logging.

You can always access the container logs from container engine (`docker` or `podman`).

The container logs are also sent to the `systemd` journal. So the log entries can be retrieved using the `journalctl` command through the journal API. For more information, see the [`journald` logging driver](https://docs.docker.com/config/containers/logging/journald/) page.

:::
