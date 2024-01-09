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

## Running the Tool

To run the diagnostic tool and create a diagnostic file to check current system configuration, you can follow the steps below.

### Creating a File to Share

You can run the `diagnostic.sh` tool and create the diagnostic files which will help you to track configuration of your server.

When you run the tool, there will be a `diagnostic.tar.gz` file which you can share with us.

:::caution
Diagnostic tool needs `sudo` permission to read some system files.

For better results, you should run the tool with the user which you use to run Appcircle server.

The diagnostic tool can asks for sudo password, you can write the password and hit enter to continue.
:::

To use the tool, you should go to the `appcircle-server` directory on your Appcircle server.

```bash
cd appcircle-server
```

Example commands:

- Run with default settings which will create the files discussed above:

```bash
./helper-tools/diagnostic.sh
```

- Change the output file name to `diagnostic-report.tar.gz`:

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

### Printing Diagnostic Information to the Terminal

If you want to write the diagnostic output to the terminal instead of a file, you can run the command below:

```bash
./helper-tools/diagnostic.sh --output "/dev/stdout"
```
