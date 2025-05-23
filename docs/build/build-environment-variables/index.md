---
title: Overview
description: Overview of environment variables in Appcircle
tags: [environment variables, variable groups, text-based variables, file-based variables]
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

# Overview of Environment Variables

### Creating environment variable groups

To create an environment variable group, select Environment Variables from the build module. Click on the orange + icon and enter the name of the group into the input box, press enter to save the group name and create the group.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3108-var2.png' />

### Adding key and text-based value pairs

To add an environment variable to the group, select the "Text" tab from the top and use the inputs below. Enter a key name, then enter the value for the key and press enter.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3108-var3.png' />

You can add as many environment variables as you need.

:::info

Variables that need to be secret can be hidden using the lock icon. Such variables cannot be viewed by the users during the build process.

:::

Please note that some environment variables may need to be duplicated to be used in different groups for different purposes.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3108-var1.png' />

### Adding files as environment variables

You can also add files as environment variables and use them in build workflows in the same way. They can be used for things like API-key based authentication in Firebase or for adding dSYM files.

To add a file, select the "File" tab from the top and enter a key name from the inputs below. Then select a file from the file browser that opens when you click the file field.

Then press add to upload the file.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3108-var4.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3108-var5.png' />

:::info

When you upload a file as an environment variable, file name is not preserved. The reason of this to prevent file name conflicts. You can upload different files with same name and can use their keys to refer them. You need to use your key to find the location of this file and then you can read the contents of this file.

:::

### Downloading environment variables

You can download and view environment variables in **JSON** format. For this, you can use the "Download" button by clicking on the three dots next to one of the variable groups under "Build > Environment Variables > Variable Groups".

In the downloaded file content, you will see a structure with **key-value** pairs.

In addition, if the value part of the environment variable is set to hidden during the text-based environment variable addition process, the "isSecret" value will be `true` and the key, along with the value **will not** be listed in the downloaded file. The same rule is valid for file type variables. If it is not hidden, this value will be `false`, and the value will be visible.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6155-variable1.png' />

:::info
An example of environment variable downloaded as a JSON file:

```json
[
  {
    "key": "API_URL",
    "value": "https://api.example.com",
    "isSecret": false,
    "isFile": false,
    "id": "API_URL"
  }
]
```

As seen in the example above;

- if the **isSecret** value is `false`, it has visible value
- if the **isSecret** value is `true` or **isFile** value is `true` , the key and the value will not be downloaded.
:::

### Uploading environment variables

The Upload feature allows users to bulk-import environment variables into any existing Variable Group (e.g., Staging, Prod, or Dev) within the Build > Environment Variables section.

This feature streamlines the process of configuring variables by enabling users to upload a predefined JSON file instead of manually entering each variable.

The uploadable file must be a `.json` file with an array of variable objects. Each variable object must include the following fields:

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6155-variable2.png' />

```json
[
{
"key": "API_URL",
"value": "https://api.example.com",
"isSecret": false,
"isFile": false,
"id": "API_URL"
},
{
"key": "API_KEY",
"value": "12345-abcde-67890-fghij",
"isSecret": true,
"isFile": false,
"id": "API_KEY"
}
]
```

:::warning
-	File type variables (isFile: `true`) cannot be uploaded using JSON. These must be added manually via the UI.
-	The Download feature does not include secret values or file contents for security reasons.
-	You can edit your own JSON files to update variables in a group. However, duplicated keys are not allowed.
:::

#### Using environment variable groups in builds

Environment variable groups can be used in builds to extend the workflow and add additional actions to workflow steps.

To add an environment variable group to a build, go to the build profile from the build module and select _Build Configuration > Env. Variables_

Here, you can see a list of previously created environment variable groups. Select the groups you want to be included in this specific build profile. Then click Save to save your selection.

Then in workflows, you can specify the environment variable for use.

<Screenshot url='https://cdn.appcircle.io/docs/assets/build-configuration-env-variables.png' />

#### Creating environment variables on the fly

If you want to create environment variables on the fly, you should write those environment variables to a special file called `AC_ENV_FILE_PATH`. For example, if we want to create a build number based on a timestamp and use it in the next steps we can use the following custom script.

```bash
 echo "BUILD_NUMBER=$(date +%s)" >> $AC_ENV_FILE_PATH
```

Any step after this custom script can access the `$BUILD_NUMBER` environment variable.

#### Using Environment Variables For SSH And PAT (Personal Access Token) Connections of the Git Provider

You can use personal access tokens or SSH private keys from the environment variables according to your needs by defining them once.

So you can add environment variables and use them in multiple projects. Also, this usage allows you to update all your projects at once when there is a change to the SSH private key, or PAT.

:::info
You can create an environment variable and enter the key value for the Personal Access Token.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3108-var7.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/repocon-azure.png' />

:::info
If you are going to use an SSH private key, you need to upload it as a file.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3108-var8.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/sshconn-var.png' />

:::caution
There are two use cases for the variable group naming here.

If the variable group nomenclature contains space, the usage will be as follows:

```txt
$"Variable Group:Key"
```

If the variable group nomenclature does not contain any space, it will be used like this:

```txt
$VariableGroup:Key
```

:::

:::caution
If your SSH public key is not defined on the Git provider, Appcircle will not be able to connect to your repository. First, you will need to add your public key to the Git provider.
:::

<ContentRef url="/build/manage-the-connections/adding-a-build-profile/connecting-to-private-repository-via-ssh">Connecting to Repository via SSH</ContentRef>

For platform specific environment variables and more detailed information, please refer to the related [documentation](/environment-variables/platform-specific-usage).