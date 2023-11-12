---
title: Creating and Using Environment Variables
metaTitle: Creating and Using Environment Variables
metaDescription: Creating and Using Environment Variables
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

# Creating and Using Environment Variables

### Creating environment variable groups

To create an environment variable group, select Environment Variables from the build module. Click on the orange + icon and enter the name of the group into the input box, press enter to save the group name and create the group.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (76).png' />

### Adding key and text-based value pairs

To add an environment variable to the group, select the "Text" tab from the top and use the inputs below. Enter a key name, then enter the value for the key and press enter.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (77).png' />

You can add as many environment variables as you need.

:::info

Variables that need to be secret can be hidden using the lock icon. Such variables cannot be viewed by the users during the build process.

:::

Please note that some environment variables may need to be duplicated to be used in different groups for different purposes.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (78).png' />

### Adding files as environment variables

You can also add files as environment variables and use them in build workflows in the same way. They can be used for things like API-key based authentication in Firebase or for adding dSYM files.

To add a file, select the "File" tab from the top and enter a key name from the inputs below. Then select a file from the file browser that opens when you click the file field.

Then press add to upload the file.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (79).png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (80).png' />

:::info

When you upload a file as an environment variable, file name is not preserved. The reason of this to prevent file name conflicts. You can upload different files with same name and can use their keys to refer them. You need to use your key to find the location of this file and then you can read the contents of this file.

:::

### Download Environment Variables

You can now download and view environment variables in <b>JSON</b> format. For this, you can use the "Download" button by clicking on the three dots next to one of the variable groups under Build -> Environment Variables -> Variable Groups.

In the downloaded file content, you will see a structure as <b>Key -> Value</b>. Here you can view text and file-based variables. However, only the name of the environment variables you added as a file will appear. The related file will not be downloaded. In addition, if the value part of the environment variable is set to hidden during the text-based environment variable addition process, the isSecret value will be true and the value value will be empty in the downloaded file. If it is not hidden, this value will be false, and the value will appear full.

![](<https://cdn.appcircle.io/docs/assets/down-variables.png>)

:::info
An example of environment variables in a JSON file:
```txt
[{"key": "API_URL", "value": "https://api.example. com", "isSecret":false, "id": "API_URL"},{"anahtar": "API_KEY", "value":"", "isSecret":true, "id": "API_KEY"},{"key": "API_SECRET", "value":"", "isSecret":true, "id": "API_SECRET"},{"key": "myFile", "value": "mykeys. json", "isSecret":false, "id": "myFile"}]
```
As seen in the example above, if the isSecret value is true, the value part is empty; if the isSecret value is false, it is filled.
:::


### Using environment variable groups in builds

Environment variable groups can be used in builds to extend the workflow and add additional actions to workflow steps.

To add an environment variable group to a build, go to the build profile from the build module and select _Build Configuration > Env. Variables_

Here, you can see a list of previously created environment variable groups. Select the groups you want to be included in this specific build profile. Then click Save to save your selection.

Then in workflows, you can specify the environment variable for use.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (172).png' />

### Creating environment variables on the fly 

If you want to create environment variables on the fly, you should write those environment variables to a special file called `AC_ENV_FILE_PATH`. For example, if we want to create a build number based on a timestamp and use it in the next steps we can use the following custom script.

```bash
 echo "BUILD_NUMBER=$(date +%s)" >> $AC_ENV_FILE_PATH
```

Any step after this custom script can access the `$BUILD_NUMBER` environment variable. 

### Using Environment Variables For SSH And PAT (Personal Access Token) Connections of the Git Provider

You can use personal access tokens or SSH private keys from the environment variables according to your needs by defining them once.

So you can add environment variables and use them in multiple projects. Also, this usage allows you to update all your projects at once when there is a change to the SSH private key, or PAT.

:::info
You can create an environment variable and enter the key value for the Personal Access Token.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/variable-group-SSH-2.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/repocon-azure.png' />

:::info
If you are going to use an SSH private key, you need to upload it as a file.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/variable-group-ssh-main.png' />

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

<ContentRef url="/build/adding-a-build-profile/connecting-to-private-repository-via-ssh">Connecting to Repository via SSH</ContentRef>
