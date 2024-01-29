---
title: Appcircle CLI
metaTitle: Appcircle CLI
metaDescription: Appcircle CLI
sidebar_position: 14
---

## Overview

Appcircle CLI is a command-line interface designed to use Appcircle from the terminals. The Appcircle CLI tool is executed directly from the terminal, provides users with a streamlined command-driven experience for efficient management of Appcircle.

The Appcircle CLI is user-friendly and versatile, offering a range of commands to enhance backend control. You can start builds, download build artifacts, publish applications on the Enterprise App Store and do more. For detailed usage, you can head over to the Appcircle CLI documentation.

Additionally, its scriptable nature allows for easy automation through shell scripts, enabling users to automate tasks and integrate the CLI into existing workflows effortlessly.

## Pre-Requirements

To configure Appcircle CLI to use your self-hosted Appcircle, you need a personal access token for authentication. Also you need the `api` and the `auth` URLs of the Appcircle server.

### Creating a Personal Access Token

For the Appcircle CLI to authenticate to your self-hosted Appcircle, you need to create a Personal access token and configure Appcircle CLI to use it.

You can follow [Generating Personal Access Tokens](../../appcircle-api/api-authentication.md#generatingmanaging-the-personal-access-tokens) page to create.

### Getting the Self-Hosted URLs

To find these URLs, you have 2 ways.

1- Change the subdomain of an Appcircle URL and test if it is working.

2- Get the URLs from the Appcircle server configuration.

#### Change Subdomain to Find `api` and `auth` URL

To find the `api` and the `auth` URL, you can check the URL that you are using to access to the Appcircle web UI and then change it's subdomain according to the format.

For example if you are using `https://my.appcircle.spacetech.com` to access to the Appcircle web UI:

- Change `my` to `api` for the api URL. As the result the `api` URL should be `https://api.appcircle.spacetech.com`.

- Change `my` to `auth` for the auth URL. As the result the `auth` URL should be `https://auth.appcircle.spacetech.com`.

You can test the `api` URL access by running `curl -v https://api.appcircle.spacetech.com`. If you are facing an error, there is 2 possible problem:

1- There is no network access between the computer which runs the `curl` command above.

2- The `api` URL is not correct. To get the correct URL, you can follow the title below.

#### Get the Subdomain From Appcircle Server Configuration

To get the `api` and the `auth` URL, you can login to the Appcircle server and run follow the steps below:

- Change directory to the Appcircle server.

```bash
cd appcircle-server
```

- Export the required dependencies..

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

By default, Appcircle CLI is configured to interact with Appcircle cloud. But with a few commands, you can change this behavior and use your own self-hosted Appcircle with the CLI.

:::info
We are assuming that you have already installed the Appcircle CLI and it is ready to use.

To test, you can open a terminal and run `appcircle --version` command. If there is an output, you are ready to configure.
:::

To configure the Appcircle CLI to use self-hosted Appcircle:

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

- Check the configuration

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

- For detailed usage about the Appcircle CLI, you can refer to the [Appcircle CLI documentation](https://github.com/appcircleio/appcircle-cli#appcircle-command-line-interface).
