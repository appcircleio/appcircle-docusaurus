---
title: Installation
metaTitle: Install Self-hosted Appcircle
metaDescription: Install Self-hosted Appcircle
sidebar_position: 3
---

# Installation

Following sections give you detailed information about system requirements, installation and configuration steps. After following directives successfully, you will get a running Appcircle instance on you infrastructure.

## Prerequisites

The following operating systems are supported for the self-hosted runner.

**Linux**

- Ubuntu 20.04
  
Only `x64` processor architecture is supported by now for Linux distributions.

Minimum hardware requirements for self-hosted Appcircle can be:

- 100GB or more free disk space
- 8 or more cores CPU
- 8 or more gigabytes (GB) RAM

These hardware specs are minumum requirements for execution but higher numbers will be better especially for increased number of users.

## Install

First, download the latest self-hosted Appcircle server zip package. After download, extract the package and change current working directory to extracted one for following steps.

Appcircle server's modules are run on Docker Engine as a container application on your system. All containers are run using a `compose.yaml` file which is generated after `ac-self-hosted.sh` is executed in the extracted files on your system.

To install Appcircle Server, you will need to have root access on your system. (`sudoer`) Also you need to have the following tools installed on your system.

- jq
- curl
- gomplate
- docker
- yq
- openssl

The good news is that the ac-self-hosted.sh script installs all the necessary tools if they are not already installed on your system.

To do this, execute the script using the `-i` argument as shown below.

```bash
sudo ./ac-self-hosted.sh -i
```

Make sure the script was executed without any error. Script will print installed and required packages when executed. Some packages may need manual installation on some linux distributions. Check command output for warnings and follow directives given in the output.

## Configure

At this point, `compose.yaml` is not generated yet. The file will be created into the project that you would previously create using the same script. To do this you should create a new project using the following command.

```bash
./ac-self-hosted.sh -n "your-project"
```

The new project folder named “your-project” is created in the `projects` directory after the above command has been successfully executed. The folder contains `global.yaml`, `secret-variable.yaml` files and `export` folder.

At this point, the `compose.yaml` file is generated in `projects/your-project/export` path. But some custom environment variables are not configured for your environments.

`Global.yaml` and `secret-variable.yaml` files are standard yaml files to configure custom variables for your environment and you can use them to update `compose.yaml` file.

For example, `global.yaml`

```yml
external:
  scheme: http
  mainDomain: ".yourcompany.com"
smtpServer:
  password: BNBJ***
  user: AKIA***
  from: noreply@yourcompany.com
```

For example, `secret-variable.yaml`

```yml
postgres:
  password: vUOWv***
```

For more details about yaml keys and values, please refer to online docs.

Note that after changes made to yaml files, you must execute the script again for the changes to take effect as shown below.

```bash
./ac-self-hosted.sh -n "your-project"
```

Now you can run Appcircle Server in the directory that exists `compose.yaml` file.

```bash
cd projects/your-project/export
```

```bash
docker compose up -d
```
