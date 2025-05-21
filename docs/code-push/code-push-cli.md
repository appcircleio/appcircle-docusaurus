---
title: CodePush CLI
description: Learn how to use Appcircle CodePush CLI and manage your deployments via command line.
tags: [appcircle codepush cli, cli, codepush cli, deployments, command line]
sidebar_position: 3
---


# CodePush CLI

The Appcircle CodePush CLI enables developers to interact with the CodePush service directly from the command line. With this tool, you can create and manage releases, assign deployments, and monitor rollout progress without needing to access the Appcircle UI. This section provides detailed instructions and examples for using the CLI effectively in your update workflows.

https://www.npmjs.com/package/@appcircle/codepush-cli


## Installing

To get started with the **Appcircle CodePush CLI**, you need to install it via `npm`. This CLI tool allows you to perform CodePush-related operations from your terminal environment.

Use the following command to install it globally:

```bash
npm i -g @appcircle/codepush-cli
```

Once installed, you can run `appcircle-code-push --help` to see the list of available commands.


## Login

Before you can use the CLI to manage your CodePush deployments, you need to authenticate your session.

Run the following command to start the login process:

```bash
appcircle-code-push login --accessKey <Your-Personal-Access-Token>
```

This command will prompt you to enter your Appcircle authentication credentials. Once authenticated, you’ll be able to access and manage your CodePush profiles via CLI.

## CLI Experience

This section explains all the necessary details to use Appcircle’s CodePush functionality via the CLI. You’ll find all the required commands and their execution logic below.

### Creating a CodePush Application in Appcircle

To start using CodePush via CLI, you first need to create a CodePush app. This app acts as a container for your deployment channels and releases.

Use the following command to create a new app:

```bash
appcircle-code-push app add <App-Name>
```

Replace `<App-Name>` with a unique name for your app. This name will be used to associate future deployments and manage them accordingly.

In addition, all necessary parameters for aplication can be found in table below;

| Command                            | Description                                                        |
|------------------------------------|--------------------------------------------------------------------|
| `appcircle-code-push app add`      | Creates a new CodePush app with the specified name.                |
| `appcircle-code-push app remove`   | Deletes an existing CodePush app from your account.                |
| `appcircle-code-push app rename`   | Changes the name of an existing CodePush app.                      |
| `appcircle-code-push app list`     | Displays a list of all CodePush apps associated with your account. |
| `appcircle-code-push app transfer` | Transfers ownership of an app to another user or organization.     |


### Adding a Deployment Channel in Appcircle

Deployment channels help organize and separate your release flows; this section explains how to add a new channel using the CLI so you can manage environments like staging and production effectively.

Use the following command to create a new deployment channel:

```bash
appcircle-code-push deployment add <App-Name> <Deployment-Name>
```
Replace `<App-Name>` and `<Deployment-Name>` with a unique names for your app and deployment channel.


In addition, all necessary parameters for aplication can be found in table below;

| Command                                  | Description                                                  |
|------------------------------------------|--------------------------------------------------------------|
| `appcircle-code-push deployment add`     | Creates a new deployment channel under the specified app.    |
| `appcircle-code-push deployment remove`  | Deletes an existing deployment channel from a CodePush app.  |
| `appcircle-code-push deployment rename`  | Renames a deployment channel within a CodePush app.          |
| `appcircle-code-push deployment list`    | Lists all deployment channels for a specific CodePush app.   |
| `appcircle-code-push deployment history` | Shows the release history for a specific deployment channel. |

### Releasing a New Version

To publish a new CodePush update using the CLI, you can use the `release-react` command. This command bundles your React Native app and pushes the update to the specified deployment channel.

Example:

```bash
appcircle-code-push release-react <MyAppName> ios -d <DeploymentChannelName> --targetBinaryVersion <BinaryVersion> [OtherOptions]
```

Replace `MyAppName` with your app name, `<DeploymentChannelName>` with the name of your deployment channel, and `<BinaryVersion>` with the version of the binary that this update targets.

:::caution Target Binary Version

When sending a CodePush release, you must specify the binary version that the release targets. The Appcircle CodePush SDK determines the binary version based on the `version` field in `Info.plist` (for iOS) or `build.gradle` (for Android). The version specified in `package.json` is not considered by the SDK.

:::

The table below summarizes the parameters used in this `release-react` command:

| Parameter                | Description                                                                                |
|--------------------------|--------------------------------------------------------------------------------------------|
| `MyAppName`              | The name of the app you registered via CodePush CLI.                                       |
| `ios` or `android`       | The target platform (`ios` or `android`).                                                  |
| `-d <DeploymentChannel>` | The deployment channel to which the update will be released.                               |
| `--targetBinaryVersion`  | The binary version of the app that this CodePush release is compatible with (e.g `1.0.0`). |
| `--rollout`              | The percentage of users that will receive the update (e.g., `50` for 50%).                 |
| `--mandatory`            | Marks the update as mandatory; users will be forced to update immediately.                 |
| `--disabled`             | Disables the release so it won’t be delivered to any devices.                              |
| `--description`          | A short note describing the content of the release.                                        |