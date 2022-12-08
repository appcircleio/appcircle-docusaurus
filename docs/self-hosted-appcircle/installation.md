---
title: Installation
metaTitle: Install Self-hosted Appcircle
metaDescription: Install Self-hosted Appcircle
sidebar_position: 2
---

# Overview

Following sections give you detailed information about system requirements, installation and configuration steps. After following directives successfully, you will get a running Appcircle instance on your infrastructure.

## Prerequisites

The following operating systems are supported for the self-hosted appcircle.

**Linux**

- Ubuntu 20.04 or later
- Debian 11 or later
- CentOS 8 or later
- RHEL 8 or later
  
Only `x64` processor architecture is supported by now for Linux distributions.

Minimum hardware requirements for self-hosted appcircle can be:

- 100GB or more free disk space
- 4 or more cores CPU
- 8 or more gigabytes (GB) RAM

These hardware specs are minumum requirements for execution but higher numbers will be better especially for increased number of users.

## Installation

### 1. Download

You need to have the following tools installed on your system:

- curl
- unzip

Download the latest self-hosted appcircle package.

```bash
curl -o appcircle-server-linux-x64-1.0.0.zip -L https://cdn.appcircle.io/self-hosted/appcircle/appcircle-server-linux-x64-1.0.0.zip
```

Extract self-hosted appcircle package into folder.

```bash
unzip -o -u appcircle-server-linux-x64-1.0.0.zip -d appcircle-server
```

Change directory into extracted `appcircle-server` folder for following steps.

```bash
cd appcircle-server
```

### 2. Packages

You need to have the following tools installed on your system.

- jq
- curl
- openssl
- gomplate
- yq
- docker

The good news is that the ac-self-hosted.sh script installs all the necessary tools if they are not already installed on your system.

:::caution

You need to have root access on your system for this step. Being able to run `sudo` is sufficient for the following step. (sudoer)

:::

To do this, execute the script using the `-i` argument as shown below.

```bash
sudo ./ac-self-hosted.sh -i
```

You can also use the long option `--install-package` for the same purpose.

Make sure the script was executed without any error. Script will print installed and required packages when executed. Some packages may need manual installation on some linux distributions. Check command output for warnings and follow directives given in the output.

### 3. Configure

First we need to find a name to our self-hosted appcircle installation. It will be the unique project name.

```bash
./ac-self-hosted.sh -n "your-project"
```

The new project folder named “your-project” will be created in the `projects` folder after the above command has been successfully executed.

Let's assume we have company named as Space Tech. Then our project name can be "spacetech". For following steps, we will give examples based on this fictive company for better understanding.

Then our command to execute will be:

```bash
./ac-self-hosted.sh -n "spacetech"
```

The folder contains `global.yaml`, `user-secret` files and `export` folder.

```txt
projects
└── spacetech
    ├── export
    ├── generated-secret.yaml
    ├── global.yaml
    └── user-secret
```

At this point, the `compose.yaml` file is generated in `projects/your-project/export` path. But some custom environment variables are not configured for your environment. So we need to configure them.

`global.yaml` and `user-secret` files are standard yaml files to configure custom variables for your environment. `global.yaml` file is in human-readable form but `user-secret` is in base64 encoded form. `user-secret` is a complementary file for `global.yaml`. You can keep all your environment variables in `global.yml` but if you don't want to keep some secrets visible in `global.yml`, you can keep them in `user-secret`. Following sections will have examples for both use cases.

`global.yaml` has some initial and example values preset when it's generated.

```yaml
---
environment: Production
enableErrorHandling: "true"
external:
  scheme: https
  mainDomain: ".example.com"

smtpServer:
  user:
  from:
  host:
  fromDisplayName:
  port:
  ssl:
  auth:
  starttls:
recaptcha:
  requirement: DISABLED # REQUIRED vs DISABLED
bruteForce:
  bruteForceProtected: 'true'
  permanentLockout: 'false'
  maxFailureWaitSeconds: '900'
  minimumQuickLoginWaitSeconds: '60'
  waitIncrementSeconds: '60'
  quickLoginCheckMilliSeconds: '1000'
  maxDeltaTimeSeconds: '43200'
  failureFactor: '30'
keycloak:
  initialUsername: admin@example.com
  enabledRegistration: true
storeWeb:
  external:
    subdomain: store
  customDomain:
    enabled: true
    domain: store.example.com
```

As an example, we can change some variables like below according to our fictive company setup.

```yaml
---
environment: Production
enableErrorHandling: "true"
external:
  scheme: http
  mainDomain: ".appcircle.spacetech.com"
  
smtpServer:
  user: o***y*****@v******.net
  from: o***y*****@v******.net
  host: smtp.v******.net
  fromDisplayName: Space Tech
  port: '587'
  ssl: 'false'
  auth: 'true'
  starttls: 'true'
recaptcha:
  requirement: DISABLED # REQUIRED vs DISABLED
bruteForce:
  bruteForceProtected: 'true'
  permanentLockout: 'false'
  maxFailureWaitSeconds: '900'
  minimumQuickLoginWaitSeconds: '60'
  waitIncrementSeconds: '60'
  quickLoginCheckMilliSeconds: '1000'
  maxDeltaTimeSeconds: '43200'
  failureFactor: '30'
keycloak:
  initialUsername: admin@spacetech.com
  enabledRegistration: true
storeWeb:
  external:
    subdomain: store
  customDomain:
    enabled: true
    domain: store.spacetech.com
```

For our example, we configured below values:

- `external.scheme` is configured as `http` for our case. When we set as `https` we also need to configure other SSL options. See related section in online docs for SSL configuration details.
- `external.mainDomain` is set as a subdomain of our example company's main domain.
- `smtpServer` settings are set for e-mail notifications. We choose not to set SMTP password as plain text in here. We will put it to `user-secret` on next steps. But if it's acceptable for you, then you can set `smtpServer.password` variable in here.
- `keycloak.initialUsername` will be appcircle's default organization's admin user. Its username is set to `initialUsername`.  We choose not to set its password as plain text in here. We will put it to `user-secret` on next steps. But if it's acceptable for you, then you can set `keycloak.initialPassword` variable in here.
- `storeWeb.customDomain.domain` is set with our example company's store domain. It's used for enterprise app store URL.

As seen in above items, we choose to set some secrets in `user-secret` file. So we need to take additional steps to complete configuration. If you set them as plain text in `global.yaml` then you don't need to take `user-secret` steps.

First create your secret yaml configuration as plain text like below.

```yaml
smtpServer:
  password: 4NZ**********
keycloak:
  initialPassword: ZP6***********
```

For example, let's assume our secret yaml file is located in `projects/spacetech/secret.yaml` path.

In order to convert it to base64 encoded `user-secret` run following command.

```bash
base64 projects/spacetech/secret.yaml > projects/spacetech/user-secret
```

You can check `user-secret` file content in human-readable form with below command if required.

```bash
base64 -d projects/spacetech/user-secret
```

We have `user-secret` filled in successfully and don't need `projects/spacetech/secret.yaml` anymore. So we should delete it.

```bash
rm projects/spacetech/secret.yaml
```

For more details about yaml keys and values, please refer to online docs.

Note that after changes made to yaml files, you must execute the script again for the changes to take effect as shown below.

```bash
./ac-self-hosted.sh -n "spacetech"
```

### 4. Run Server

Appcircle server's modules are run on Docker Engine as a container application on your system. All containers are run using a `compose.yaml` file which is generated after `ac-self-hosted.sh` is executed successfully explained in above steps.

`projects/your-project/export` path will have all exported envrionment for self-hosted appcircle services along with `compose.yaml`.

```text
projects/
└── spacetech
    ├── export
    │   ├── agent-cache
    │   ├── api-gateway
    │   ├── build
    │   ├── common.env
    │   ├── compose.yaml
    │   ├── distribution
    │   ├── keycloak
    │   ├── keycloak-migration
    │   ├── license
    │   ├── minio
    │   ├── mongo
    │   ├── nginx
    │   ├── notification
    │   ├── postgres
    │   ├── report
    │   ├── rijndael
    │   ├── signing-identity
    │   ├── store
    │   ├── store-submit
    │   ├── tester-web
    │   ├── vault
    │   ├── webApp
    │   └── webhook
    ├── generated-secret.yaml
    ├── global.yaml
    └── user-secret
```

Before we run self-hosted appcircle, we need to set artifact registry credentials in order to pull docker images for services. When you buy an enterprise license for self-hosted appcircle, you will get a credentials JSON file which enables you to login our artifact registry. For example, assume for our fictive company we got `space-tech-cred.json` and dowloaded it into `~/Downloads` folder.

Copy credentials file into self-hosted appcircle root directory.

```bash
cp ~/Downloads/space-tech-cred.json cred.json
```

Using that JSON file you need to execute below command.

```bash
./ac-self-hosted.sh -n "spacetech"
```

You should see "Docker login cred not found. Trying to login now..." in command output and then "Login Succeeded" which shows us successful artifact registry login.

If you get any error for some reason at this step, you can remove `~/.docker/config` file to reset and execute same command again to retake same steps.

Now you are ready to run self-hosted appcircle.

Change into the directory that exists `compose.yaml` file.

```bash
cd projects/spacetech/export
```

Run appcircle server services.

```bash
docker compose up -d
```

:::info

At first run, it will pull once all docker images needed from artifact registry. Also there are some migration steps taken for once which prepares system for other operations.

So it may need up to ~20 min to system be up according to your internet connection speed and CPU power. But recurrent boots will take a couple of minutes and will have shorter durations.

:::

If everything is okay, then you should see service statuses as "running", "running (healthy)" or "exited (0)".

![](https://cdn.appcircle.io/docs/assets/self-hosted-appcircle-container-health.png)

Open your browser and go to URL `https://my.appcircle.spacetech.com`. You should see login page.

![](https://cdn.appcircle.io/docs/assets/self-hosted-appcircle-login-page.png)

Login to self-hosted appcircle with `initialUsername` and `initialPassword` that we have configured in above steps. For our example, user name is `admin@spacetech.com`.

![](https://cdn.appcircle.io/docs/assets/self-hosted-appcircle-dashboard-page.png)

You can also login to enterprise app store with configured custom URL `store.spacetech.com`.

![](https://cdn.appcircle.io/docs/assets/self-hosted-appcircle-enterprise-app-store.png)
