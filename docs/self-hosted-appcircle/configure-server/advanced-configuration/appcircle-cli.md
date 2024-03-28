---
title: Command-Line Interface (CLI) Configuration
metaTitle: Command-Line Interface (CLI) Configuration
metaDescription: Command-Line Interface (CLI) Configuration
sidebar_position: 12
---

Appcircle CLI is a command-line interface designed to use Appcircle from the terminals. The Appcircle CLI tool, which is executed directly from the terminal, provides users with a streamlined command-driven experience for efficient management of Appcircle.

The Appcircle CLI is user-friendly and versatile, offering a range of commands to enhance backend control. You can start builds, download build artifacts, publish applications on the Enterprise App Store, and do more.

Additionally, its scriptable nature allows for easy automation through shell scripts, enabling users to automate tasks and integrate the CLI into existing workflows effortlessly.

For detailed usage, you can head over to the [Appcircle CLI](https://github.com/appcircleio/appcircle-cli#appcircle-command-line-interface) documentation.

## Pre-Requirements

To configure Appcircle CLI to use your self-hosted Appcircle, you need a **Personal API Token** for authentication. Also, you need the `api` and the `auth` URLs of the Appcircle server.

### 1. Create a Personal API Token

For the Appcircle CLI to authenticate to your self-hosted Appcircle, you need to create a **Personal API Token** and configure the Appcircle CLI to use it.

You can follow the [Generating and Managing Personal API Tokens](/appcircle-api/api-authentication.md#generatingmanaging-the-personal-api-tokens) page to create one.

### 2. Find out the Appcircle server URLs

To find these URLs, you have two ways.

1. Change the subdomain of an Appcircle URL and test if it is working.
2. Get the URLs from the Appcircle server configuration.

#### Change the subdomain with `api` and `auth` for the default configuration

To find out the `api` and the `auth` URL, you can check the URL that you are using to access the Appcircle web UI (dashboard) and then change its subdomain according to the format.

For example, if you are using `https://my.appcircle.spacetech.com` to access the Appcircle web UI,

- Change `my` to `api` for the **API_HOSTNAME**.
  - It should be `https://api.appcircle.spacetech.com`.
- Change `my` to `auth` for the **AUTH_HOSTNAME**.
  - It should be `https://auth.appcircle.spacetech.com`.

You can test the **API** URL access by running the command below.

```bash
curl -v https://api.appcircle.spacetech.com
```

If you are facing a connectivity error, there are two possible problems:

1. There is no network access between the computer that runs the `curl` command above and the Appcircle server.
2. Or the **API** URL is not correct. In order to get the correct URL, you can follow the title below.

#### Get the subdomains from the Appcircle server for any type of configuration

To get the `api` and the `auth` URL, you should login to the Appcircle server and follow the steps below:

- Change the directory on the Appcircle server.

```bash
cd appcircle-server
```

- Update the environment variable `PATH` with the required dependencies.

```bash
export PATH=$PATH:$(pwd)/deps/bin
```

- Get the `api` and `auth` URL from the configuration file of your project.

:::info
`spacetech` in the example below is an example project name.

To find out your projects, list the content of the `./projects` directory.

```bash
ls -l ./projects
```

:::

```bash
yq '.apiGateway.external.url' ./projects/spacetech/export/.global.yaml && \
yq '.keycloak.external.url' ./projects/spacetech/export/.global.yaml
```

You can test the **API** URL access by running the command below.

```bash
curl -v https://api.appcircle.spacetech.com
```

If you are still getting a connectivity error, you should check the network access between the host that runs `curl` and the Appcircle server.

## Configure CLI to Use Your Self-Hosted Server

By default, Appcircle CLI is configured to interact with the Appcircle cloud. But with a few commands, you can change this behavior and use your own self-hosted Appcircle server with the CLI.

:::info
We are assuming that you have already installed the Appcircle CLI and that it is ready to use.

Follow the installation instructions [here](https://github.com/appcircleio/appcircle-cli?tab=readme-ov-file#installation) to install Appcircle CLI if it's not ready to use.

To test, you can open a terminal and run the command below in your terminal.

```bash
appcircle --version
```

If you see the Appcircle CLI version without any errors, you are ready to configure the tool.
:::

To configure the Appcircle CLI to use with the self-hosted Appcircle server follow the steps below.

**1.** Add a new configuration with any desired name.

```bash
appcircle config add "${CONFIGURATION_NAME}"
```

For example;

```bash
appcircle config add "spacetech"
```

**2.** Set the [required URLs](#2-find-out-the-appcircle-server-urls) to communicate with the self-hosted Appcircle server.

```bash
appcircle config set API_HOSTNAME 'https://api.appcircle.spacetech.com'
```

```bash
appcircle config set AUTH_HOSTNAME 'https://auth.appcircle.spacetech.com'
```

**3.** Set the [Personal API Token](#1-create-a-personal-api-token) for authentication on the server.

```bash
appcircle login --pat "${PERSONAL_API_TOKEN}"
```

For example;

```bash
appcircle login --pat "TTk0...RhNw=="
```

:::caution
If you face any self-signed certificate error, for example, "self-signed certificate in certificate chain", check the [Trusting Certificate](#trusting-the-ssl-certificate-recommended) section for troubleshooting.
:::

You can check the configuration with the command below.

```bash
appcircle config list
```

You should see the current (active) configuration, the path of the `config.json` file, and server URLs per configuration.

You can also configure the Appcircle CLI in interactive mode.

```bash
appcircle -i
```

You should use the relevant menu item and follow the instructions there that are similar to the steps above.

When you successfully log in with the Appcircle CLI, you can list the build profiles with the command below.

```bash
appcircle listBuildProfiles
```

For detailed usage information about the Appcircle CLI, you can refer to the [Appcircle CLI](https://github.com/appcircleio/appcircle-cli#appcircle-command-line-interface) documentation.

## Self-Signed Certificates

If you are using a self-signed SSL certificate on the self-hosted Appcircle server and the certificate is not trusted on your host, you may face an error like below while trying to run the Appcircle CLI tool.

```bash
$ appcircle login --pat "TTk0...RhNw=="

self-signed certificate in certificate chain undefined
```

That error occurs when the root CA certificate or the self-signed certificate of the Appcircle server is not trusted on your host.

You can trust the SSL certificate of the Appcircle server to secure the network between the CLI and the server, or you can disable certificate verification.

:::danger
Disabling certificate verification is risky and not recommended.

For secure and reliable communication, you should trust the SSL certificate.
:::

### Trusting the SSL Certificate (recommended)

You can trust the SSL certificate of the Appcircle server with the Appcircle CLI tool itself to make sure all the requests are secured and trusted.

You should already have [configured](#configure-cli-to-use-your-self-hosted-server) the Appcircle CLI tool for the self-hosted Appcircle server.

:::info
This command is supported on **MacOS** and **Linux** operating systems only.

If you are a **Windows** user, you can download the SSL certificate and make it trusted under the `MMC` menu in Windows.
:::

:::caution
Trusting the SSL certificate is supported for Appcircle CLI version `1.1.1` or later.

For older versions, you should upgrade the Appcircle CLI, or although it's not recommended, you can [disable the SSL verification](#disabling-the-ssl-certificate-verification-not-recommended).
:::

To trust the SSL certificate of the configured Appcircle server, run the `config trust` subcommand of the Appcircle CLI.

```bash
appcircle config trust
```

:::info
The command may ask for the `sudo` password for some system-wide operations. You should be sudoer.
:::

When the script successfully trusts the certificate, you will see an output like below.

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

Now you should open a new terminal for the changes to take effect.

In a new terminal session, you can run the `appcircle` commands securely without any certificate problems.

### Disabling the SSL Certificate Verification (not-recommended)

Disabling SSL certificate verification removes a critical layer of security, leaving the communication vulnerable to a variety of threats, including those associated with man-in-the-middle attacks, data integrity issues, and trustworthiness concerns.

Proper SSL certificate validation is essential for ensuring the authenticity and security of the communication between the Appcircle CLI and the Appcircle server.

It's crucial to prioritize security measures to protect sensitive data and maintain the integrity of your system.

:::danger
While we do not recommend it, you have the choice to accept the mentioned risk by selectively disabling certificate verification specifically for the Appcircle CLI.

It can be used when you have problems [trusting the SSL certificates](#trusting-the-ssl-certificate-recommended).
:::

To disable the SSL certificate verification just for the Appcircle CLI tool, you should add a prefix to the `appcircle` command.

:::info
SSL and TLS are the same concepts for this document. So, TLS certificates are also known as SSL certificates.
:::

```bash
alias appcircle="NODE_TLS_REJECT_UNAUTHORIZED=0 appcircle"
```

After disabling SSL certificate verification, there will be a warning saying SSL verification is disabled.

```bash
$ appcircle listBuildProfiles

(node:74065) Warning: Setting the NODE_TLS_REJECT_UNAUTHORIZED environment variable to '0' makes TLS connections and HTTPS requests insecure by disabling certificate verification.
(Use `node --trace-warnings ...` to show where the warning was created)
...
```

You can ignore it. All the subcommands will work as they should.

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />
