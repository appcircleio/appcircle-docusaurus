---
title: Runner Diagnostic
metaTitle: Runner Diagnostic
metaDescription: Runner Diagnostic
sidebar_position: 6
---

## Overview

Running the diagnostic tool provides a comprehensive snapshot of the runners's configuration and settings, offering a clear overview of its current state.

The diagnostic tool allows users to efficiently troubleshoot issues by identifying potential problems or misconfigurations within the system.

With its ability to gather crucial data such as systemd services, runner configuration, installed packages and environment configurations, the diagnostic tool streamlines the process of diagnosing and resolving issues.

:::info
Appcircle runner `v1.4.6` or higher is required for the `diagnostic` tool.
:::

## Running the Tool

You can run this diagnostic tool either on an Appcircle runner or on an Appcircle runner host if you are using vm.

To run the diagnostic tool and create a diagnostic file to check current system configuration, you can follow the steps below.

### Creating a File to Share

You can run the `diagnostic.sh` tool and create the diagnostic files which will help you to track configuration of your runner or host machine.

When you run the tool, there will be a `diagnostic-${datetime}.tar.gz` file which you can share with us.

The `${datetime}` in the file name above is a dynamic variable which is the date and time you run the script. Date time format is: `yyyymmddHHMMSS` For example: `diagnostic-20240109064747.tar.gz`

:::caution
Diagnostic tool needs `sudo` permission to read some system files.

For better results, you should run the tool with the user which you use to run Appcircle runner.

The diagnostic tool can asks for sudo password, you can write the password and hit enter to continue.
:::

To use the tool, you should go to the `appcircle-runner` directory on your Appcircle runner machine.

```bash
cd appcircle-runner
```

:::info
If you want to use that script on an another machine like a host machine of the runner, you can just copy the `diagnostic.sh` file and see the example commands below.
:::

Example commands:

- Run with default settings which will create the files discussed above:

```bash
./scripts/diagnostic.sh
```

- Change the output file name to `diagnostic-report-${datetime}.tar.gz`:

```bash
./scripts/diagnostic.sh --output "diagnostic-report"
```

- Check the help message:

```bash
./scripts/diagnostic.sh --help
```

- Check the version of the diagnostic tool:

```bash
./scripts/diagnostic.sh --version
```

### Printing Diagnostic Information to the Terminal

If you want to write the diagnostic output to the terminal instead of a file, you can run the command below:

```bash
./scripts/diagnostic.sh --output "/dev/stdout"
```
