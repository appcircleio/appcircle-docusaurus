---
title: Server Diagnostic
metaTitle: Server Diagnostic
metaDescription: Server Diagnostic
sidebar_position: 12
---

## Overview

Running the diagnostic tool provides a comprehensive snapshot of the server's configuration and settings, offering a clear overview of its current state.

The diagnostic tool allows users to efficiently troubleshoot issues by identifying potential problems or misconfigurations within the system.

With its ability to gather crucial data such as systemd services, installed packages, and container engine configurations, the diagnostic tool streamlines the process of diagnosing and resolving issues.

:::info
Appcircle server `v3.12.0` or higher is required for the `diagnostic` tool.
:::

## Running the Tool

To run the diagnostic tool and create a diagnostic file to check current system configuration, you can follow the steps below.

### Creating a Diagnostic Report For Sharing

You can run the `diagnostic.sh` tool and create the diagnostic files which will help you to track configuration of your server.

When you run the tool, there will be a `diagnostic-${datetime}.tar.gz` file which you can share with us. The "${datetime}" is a dynamic variable which is the date and time you run the script. Date time format is: `yyyymmddHHMMSS` For example: `diagnostic-20240109064747.tar.gz`

:::caution
Diagnostic tool needs `sudo` permission to read some system files.

For better results, you should run the tool with the user which you use to run Appcircle server.

The diagnostic tool can asks for sudo password, you can write the password and hit enter to continue.
:::

To use the tool, you should go to the `appcircle-server` directory on your Appcircle server.

```bash
cd appcircle-server
```

#### Create a Diagnostic Report

To create a diagnostic report, you can run the diagnostic tool like in the examples below.

- Run with default settings which will create the files discussed above:

```bash
./helper-tools/diagnostic.sh
```

- Change the output file name to `diagnostic-report-${datetime}.tar.gz`:

```bash
./helper-tools/diagnostic.sh --output "diagnostic-report"
```

- Check the help message:

```bash
./helper-tools/diagnostic.sh --help
```

- Check the version of the diagnostic tool:

```bash
./helper-tools/diagnostic.sh --version
```

#### Share the Diagnostic Report

Once you run the the diagnostic tool, the diagnostic reports will be created in the current directory.

- To list diagnostic files with the one, you can list the current directory.

```bash
ls -l | grep -i "diagnostic"
```

- As output, you will see some diagnostic reports.

```bash
-rw-r--r--   1 appcircle  staff   1755 Jan 23 12:01 diagnostic-20240123120153.tar.gz
```

- You can share that diagnostic report with us for analyzing.

### Printing Diagnostic Information to the Terminal

If you want to see the diagnostic report directly in the terminal instead of a report file, you can run the command below:

```bash
./helper-tools/diagnostic.sh --output "/dev/stdout"
```
