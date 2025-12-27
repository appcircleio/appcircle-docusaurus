---
title: Runner Diagnostic
metaTitle: Runner Diagnostic
metaDescription: Runner Diagnostic
sidebar_position: 6
---

## Overview

Running the diagnostic tool provides a comprehensive snapshot of the runner's configuration and settings, offering a clear overview of its current state.

The diagnostic tool allows users to efficiently troubleshoot issues by identifying potential problems or misconfigurations within the system.

With its ability to gather crucial data such as systemd services, runner configuration, installed packages and environment configurations, the diagnostic tool streamlines the process of diagnosing and resolving issues.

:::info
Appcircle runner `v1.4.6` or higher is required for the `diagnostic` tool.
:::

## Running the Tool

You can run this diagnostic tool either on an Appcircle runner or on an Appcircle runner host if you are using VM.

### Creating a Diagnostic Report For Sharing

You can run the `diagnostic.sh` tool and create the diagnostic files, which will help you track the configuration of your runner or host machine.

When you run the tool, there will be a `diagnostic-${datetime}.tar.gz` file under the `diagnostic-reports` directory, which you can share with us.

The `${datetime}` in the file name above is a dynamic variable, which is the date and time you run the script. The date time format is: `yyyymmddHHMMSS` For example: `diagnostic-20240109064747.tar.gz`

:::caution
The diagnostic tool needs `sudo` permission to read some system files.

For better results, you should run the tool with the user that you use to run Appcircle runner.

The diagnostic tool can ask for the sudo password, you can write the password and hit enter to continue.
:::

To use the tool, you should go to the `appcircle-runner` directory on your Appcircle runner machine.

```bash
cd appcircle-runner
```

:::info
If you want to use that script on another machine, like the host machine of the runner VM, you can just copy the `diagnostic.sh` file and see the example commands below.
:::

:::info
The tool will store the diagnostic reports under the `./diagnostic-reports` directory by default. We don't recommend you change the output name or path unless you have a special reason.

When you create a new diagnostic report, the previously created ones are also included in the report file. For this reason, we also don't recommend deleting the `./diagnostic-reports` directory.
:::

#### Create a Diagnostic Report

To create a diagnostic report, you can run the diagnostic tool like in the examples below.

- Run with default settings which will create the files discussed above:

```bash
./scripts/diagnostic.sh
```

- Not recommended but you can change the output file name to `diagnostic-report-${datetime}.txt`:

:::info
This will create a `txt` file instead of a tar ball file. 
:::

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

#### Share the Diagnostic Report

Once you run the the diagnostic tool, the diagnostic reports will be created in the `./diagnostic-reports` directory.

- To list diagnostic files with the one, you can list the current directory.

```bash
ls -l ./diagnostic-reports
```

- As output, you will see some diagnostic reports.

```bash
-rw-r--r--   1 appcircle  staff   1755 Jan 23 12:01 diagnostic-20240123120153.tar.gz
-rw-r--r--   1 appcircle  staff   1755 Jan 25 14:12 diagnostic-20240125141220.tar.gz
```

- You can share the latest diagnostic report with us for analyzing.

### Printing Diagnostic Information to the Terminal

If you want to write the diagnostic output to the terminal instead of a file, you can run the command below:

```bash
./scripts/diagnostic.sh --output "/dev/stdout"
```
