---
title: Appcircle CLI
metaTitle: Appcircle CLI
metaDescription: Appcircle CLI
sidebar_position: 14
---

## Overview

Appcircle CLI is a command-line interface designed to use Appcircle from the terminals. The Appcircle CLI tool, which is executed directly from the terminal, provides users with a streamlined command-driven experience for efficient management of Appcircle.

The Appcircle CLI is user-friendly and versatile, offering a range of commands to enhance backend control. You can start builds, download build artifacts, publish applications on the Enterprise App Stor, and do more. For detailed usage, you can head over to the Appcircle CLI documentation.

Additionally, its scriptable nature allows for easy automation through shell scripts, enabling users to automate tasks and integrate the CLI into existing workflows effortlessly.

## Pre-Requirements

To configure Appcircle CLI to use your self-hosted Appcircle, you need a personal access token for authentication. Also, you need the `api` and the `auth` URLs of the Appcircle server.

### Creating a Personal Access Token

For the Appcircle CLI to authenticate to your self-hosted Appcircle, you need to create a personal access token and configure the Appcircle CLI to use it.

You can follow the [Generating Personal Access Tokens](../../appcircle-api/api-authentication.md#generatingmanaging-the-personal-access-tokens) page to create one.

### Getting the Self-Hosted URLs

To find these URLs, you have two ways.

1. Change the subdomain of an Appcircle URL and test if it is working.

2. Get the URLs from the Appcircle server configuration.

#### Change Subdomain to Find `api` and `auth` URL

To find the `api` and the `auth` URL, you can check the URL that you are using to access to the Appcircle web UI and then change its subdomain according to the format.

For example, if you are using `https://my.appcircle.spacetech.com` to access to the Appcircle web UI,

- Change `my` to `api` for the api URL. As a result, the `api` URL should be `https://api.appcircle.spacetech.com`.

- Change `my` to `auth` for the auth URL. As a result, the `auth` URL should be `https://auth.appcircle.spacetech.com`.

You can test the `api` URL access by running `curl -v https://api.appcircle.spacetech.com`. If you are facing an error, there are two possible problems:

1. There is no network access between the computer that runs the `curl` command above and Appcircle server.

2. The `api` URL is not correct. To get the correct URL, you can follow the title below.

#### Get the Subdomain From Appcircle Server Configuration

To get the `api` and the `auth` URL, you can login to the Appcircle server and follow the steps below:

- Change the directory on the Appcircle server.

```bash
cd appcircle-server
```

- Export the required dependencies.

```bash
export PATH=$PATH:$(pwd)/deps/bin
```

- Get the `api` and `auth` URL from the configuration file of your project.

:::info
`spacetech` in the example below is an example project name. To find your projects, list the `./projects` directory:

```bash
ls -l ./projects
```

:::

```bash
yq '.apiGateway.external.url' ./projects/spacetech/export/.global.yaml && \
yq '.keycloak.external.url' ./projects/spacetech/export/.global.yaml
```

As a result, you should see the required URLs.

You can test the `api` url with the `curl -v https://api.appcircle.spacetech.com` command again.

If you are still getting an error, you should check the network access between the machine that runs `curl` and the Appcircle server.

## Configuring Appcircle CLI to Use Your Self-Hosted Appcircle

By default, Appcircle CLI is configured to interact with the Appcircle cloud. But with a few commands, you can change this behavior and use your own self-hosted Appcircle with the CLI.

:::info
We are assuming that you have already installed the Appcircle CLI and that it is ready to use.

To test, you can open a terminal and run `appcircle --version` command in your terminal. If there is an output, you are ready to configure.
:::

To configure the Appcircle CLI to use the self-hosted Appcircle:

- Add a new configuration with any desired name.

```bash
appcircle config add spacetech-appcircle
```

- Set the [required URLs](#getting-the-self-hosted-urls) to communicate with the self-hosted Appcircle:

```bash
appcircle config set API_HOSTNAME 'https://api.appcircle.spacetech.com' && \
appcircle config set AUTH_HOSTNAME 'https://auth.appcircle.spacetech.com'
```

- Set the [personal access token](#creating-a-personal-access-token) to authenticate with the self-hosted Appcircle:

```bash
appcircle login --pat "TTk0YzFwdUVmVHZrZ0FvMnUwcVdGTVZ3eE1lc2JtelEwbnN4dWtjbnFjMAscpCurFTTM4Q2VJNnZkd3Z6SnwxNzM3ODI5SIO3ODc0fGZiOTVkYTE4LWYzMDgtNDY5Yy1iNDUzLTY0MTQ3NzMzNzRhNw=="
```

If you face any self-signed certificate error, check the [Trusting Certificate](#trusting-the-ssl-certificate-recommended) section.

- Check the configuration.

```bash
appcircle config list
```

- To use the Appcircle CLI in interactive mode:

```bash
appcircle -i
```

- To list build profiles:

```bash
appcircle listBuildProfiles
```

- For detailed usage information about the Appcircle CLI, you can refer to the [Appcircle CLI documentation](https://github.com/appcircleio/appcircle-cli#appcircle-command-line-interface).

## Self-Signed Certificate of Appcircle Server

If you are using a self-signed SSL certificate on the self-hosted Appcircle and the certificate is not trusted on your computer, you may face an error like `self-signed certificate in certificate chain undefined` while trying to run `appcircle` CLI tool like in the example below.

```bash
appcircle login --pat "example-pat"

self-signed certificate in certificate chain undefined
```

That error occurs when the root CA certificate or the self signed certificate of the Appcircle server is not trusted on your computer.

You can trust the SSL certificate of the Appcircle server for securing network between the CLI and Appcircle or you can disable certificate verification.

:::danger
Disabling the certificate verification is risky and not recommended. For a secure and reliable communication, you should trust the SSL certificate.
:::

### Trusting the SSL Certificate (recommended)

You can trust the SSL certificate of the Appcircle server with `appcircle` CLI tool itself to make sure all the requests are secured and trusted.

You should already have [configured](#configuring-appcircle-cli-to-use-your-self-hosted-appcircle) the `appcircle` CLI tool for the self-hosted Appcircle server.

:::info
This command is supported on `macOS` and `Linux` operating systems only.

If you are a `Windows` user, you can download the SSL certificate and make it trusted under the `MMC` menu of `Windows`.
:::

To trust the SSL certificate of the configured Appcircle server, follow the steps below:

- Run the `config trust` subcommand of the `appcircle` CLI tool.

```bash
appcircle config trust
```

- The command may ask for the `sudo` password.

- If the script is successfully trusts the certificate, you will see an output like below.

```bash
[+] OS: Darwin
Appcircle URL is valid: https://api.appcircle.spacetech.com
[-] Allowing addition of root certificates
[-] Getting root certificate of 'api.appcircle.spacetech.com'
Found cert that has same subject and issuer
 [+] Certificate written to 'api.appcircle.spacetech.com.crt'
 [+] Subject: Crtforge ROOT CA, emailAddress=contact@spacetech.com
 [+] Expires on: Jan 31 10:12:39 2044 GMT
[-] Adding 'api.appcircle.spacetech.com.crt' to Keychain
Password:
YES (0)
YES (0)
[-] Adding Certs to Nodejs
The line already exists in /Users/spacetech/.zshrc
[-] Verifying connection to 'api.appcircle.spacetech.com'
 [+] Verification successful!
The root cert has been trusted successfully.
You must open a new terminal session for the changes to take effect.
```

- After the command completes, you should open a new terminal for changes to take effect.

- Now you can run the `appcircle` commands securely without any certificate problem.

### Disabling the Certificate Verification (not-recommended)

- To disable the TLS verification just for the `appcircle` CLI tool, you can add a prefix to the `appcircle` cli command.

```bash
alias appcircle="NODE_TLS_REJECT_UNAUTHORIZED=0 appcircle"
```

- After disabling the certificate verification, there will be a warning saying TLS verification is disabled, you can ignore it :

```bash
$ appcircle listBuildProfiles
(node:74065) Warning: Setting the NODE_TLS_REJECT_UNAUTHORIZED environment variable to '0' makes TLS connections and HTTPS requests insecure by disabling certificate verification.
(Use `node --trace-warnings ...` to show where the warning was created)
...
```
