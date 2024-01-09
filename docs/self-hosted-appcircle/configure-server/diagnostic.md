---
title: Server Diagnostic
metaTitle: Server Diagnostic
metaDescription: Server Diagnostic
sidebar_position: 12
---

## Overview

Running the diagnostic script provides a comprehensive snapshot of the server's configuration and settings, offering a clear overview of its current state.

The diagnostic script allows users to efficiently troubleshoot issues by identifying potential problems or misconfigurations within the system.

With its ability to gather crucial data such as systemd services, installed packages, and container engine configurations, the diagnostic script streamlines the process of diagnosing and resolving issues.

## Running the Script

To run the diagnostic script and create a diagnostic file to check current system configuration, you can follow the steps below.

### Creating a file to share

You can run the `diagnostic.sh` script and create the diagnostic files which will help you to track configuration of your server.

When you run the script, there will be a `diagnostic` and `diagnostic.tar.gz` file.

You can read the `diagnostic` with a text editor or you can share the `diagnostic.tar.gz` file with us.

:::caution
Diagnostic script needs `sudo` permission to read some system files.

For better results, you should run the script with the user which you use to run Appcircle server.

The diagnostic script can asks for sudo password, you can write the password and hit enter to continue.
:::

Example commands:

- Run with default settings which will create the files discussed above:

```bash
./helper-tools/diagnostic.sh
```

- Change the output file names:

```bash
./helper-tools/diagnostic.sh --output "custom"
```

- Check the help message:

```bash
./helper-tools/diagnostic.sh --help
```

- Check the version of the diagnostic script:

```bash
./helper-tools/diagnostic.sh --version
```

### Printing diagnostic information to the terminal

If you want to write the diagnostic output to the terminal instead of a file, you can run the command below:

```bash
./helper-tools/diagnostic.sh --output "/dev/stdout"
```
