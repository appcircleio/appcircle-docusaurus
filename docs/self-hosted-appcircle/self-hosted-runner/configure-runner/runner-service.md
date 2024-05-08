---
title: Service Configuration
description: Learn how to configure self-hosted runner service
tags: [self-hosted runner, service, configuration]
sidebar_position: 3
---

# Overview

After registration and configuration of self-hosted runner, you need to install launchd or systemd service to start runner as a daemon. Launchd service is used for macOS, systemd service is used for Linux.

Self-hosted runner periodically checks for build jobs and dequeues eligible job for pipeline execution. So, it's always up in background and works non-interactively. When service is installed successfully, it will be automatically started on operating system boot without any manual intervention.

Runner service keeps its logs at `$HOME/appcircle-runner` path. There are two log files:

- stdout.log
- stderr.log

`stdout.log` is connected to standard out of service and `stderr.log` is connected to standard error of service.

`stdout.log` file has build job log. You can see same build log as web UI while pipeline is executing:

```bash
tail -f stdout.log
```

Logs are rotated daily and are kept at most 7 days historically.

Old logs can be found under `service.logs` directory. Each archived log file has date suffix and compressed by gzip. If you need to view an archived log, you can use `gzip -dk LOG_FILE.gz` to extract archive file.

### Install

```bash
./ac-runner service -c install
```

Installs and starts self-hosted runner service. It's used once, while installing and configuring self-hosted runner.

### Status

```bash
./ac-runner service -c status
```

You can see current service status of self-hosted runner (up or down).

### Start

```bash
./ac-runner service -c start
```

Starts runner service if it's stopped. If runner service is down for some reason, you can try start manually.

### Stop

```bash
./ac-runner service -c stop
```

You can disable self-hosted runner from web UI. (See, [here](./manage-runners) for details)

If you need to disable self-hosted runner from CLI, you can use service stop option.

Service start from CLI will enable runner again.

:::info

Launchd or systemd service start and stop actions doesn't affect "Enabled" toggle button state on "Self-hosted Runners" list.

When a self-hosted runner service is stopped from CLI, you will see it as `Offline`. When service is started, it will become `Online`.

:::

:::danger

You should be careful for running pipelines while stopping self-hosted runner service. When you stop service, it will immediately terminate self-hosted runner process and build job will be cut. It will be still shown as in-progress build but actually it's not working. It will stuck in that state until build timeout.

Sometimes this situation may not be a problem for you, because you can cancel and retry build job with another online self-hosted runner. But if it's an unacceptable case for you, then you should check current state of runner from "Self-hosted Runners" list before stopping self-hosted runner service.

You can also follow instantly service log `stdout.log` for running build job. When runner becomes idle, you can stop service safely.

While waiting runner to complete its job, you can use "disable" toggle button from "self-hosted runners" list in order to prevent runner getting new build job from queue.

Service restart and uninstall processes have also same situation since they have service stop implicitly.

:::

### Restart

```bash
./ac-runner service -c restart
```

It's equivalent to stop and start with a single command.

### Uninstall

```bash
./ac-runner service -c uninstall
```

Stops self-hosted runner service and removes launchd/systemd service entries. It reverts service install process.
