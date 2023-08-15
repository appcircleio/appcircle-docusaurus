---
title: Creating and Using Environment Variables
metaTitle: Creating and Using Environment Variables
metaDescription: Creating and Using Environment Variables
sidebar_position: 2
---

# Creating and Using Environment Variables

### Creating environment variable groups

To create an environment variable group, select Environment Variables from the build module. Click on the orange + icon and enter the name of the group into the input box, press enter to save the group name and create the group.

![](<https://cdn.appcircle.io/docs/assets/image (76).png>)

### Adding key and text-based value pairs

To add an environment variable to the group, select the "Text" tab from the top and use the inputs below. Enter a key name, then enter the value for the key and press enter.

![](<https://cdn.appcircle.io/docs/assets/image (77).png>)

You can add as many environment variables as you need.

:::info

Variables that need to be secret can be hidden using the lock icon. Such variables cannot be viewed by the users during the build process.

:::

Please note that some environment variables may need to be duplicated to be used in different groups for different purposes.

![](<https://cdn.appcircle.io/docs/assets/image (78).png>)

### Adding files as environment variables

You can also add files as environment variables and use them in build workflows in the same way. They can be used for things like API-key based authentication in Firebase or for adding dSYM files.

To add a file, select the "File" tab from the top and enter a key name from the inputs below. Then select a file from the file browser that opens when you click the file field.

Then press add to upload the file.

![](<https://cdn.appcircle.io/docs/assets/image (79).png>)

![](<https://cdn.appcircle.io/docs/assets/image (80).png>)

:::info

When you upload a file as an environment variable, file name is not preserved. The reason of this to prevent file name conflicts. You can upload different files with same name and can use their keys to refer them. You need to use your key to find the location of this file and then you can read the contents of this file.

:::


### Using environment variable groups in builds

Environment variable groups can be used in builds to extend the workflow and add additional actions to workflow steps.

To add an environment variable group to a build, go to the build profile from the build module and select _Build Configuration > Env. Variables_

Here, you can see a list of previously created environment variable groups. Select the groups you want to be included in this specific build profile. Then click Save to save your selection.

Then in workflows, you can specify the environment variable for use.

![](<https://cdn.appcircle.io/docs/assets/image (172).png>)

### Creating environment variables on the fly 

If you want to create environment variables on the fly, you should write those environment variables to a special file called `AC_ENV_FILE_PATH`. For example, if we want to create a build number based on a timestamp and use it in the next steps we can use the following custom script.

```bash
 echo "BUILD_NUMBER=$(date +%s)" >> $AC_ENV_FILE_PATH
```

Any step after this custom script can access the `$BUILD_NUMBER` environment variable. 

### Using Environment Variables in Project Creation

You can use environment variables when creating your project with SSH. You can use personal access tokens or SSH Public key variables in environment variables according to your needs by defining them once.

You can create an environment variable and enter the key value for the Personal Access Token.

![](<https://cdn.appcircle.io/docs/assets/variable-group-PAT.png>)

![](<https://cdn.appcircle.io/docs/assets/vg-repo-pat.png>)

:::info
If you are going to use a Private SSH key, you need to upload it as a file.
:::

![](<https://cdn.appcircle.io/docs/assets/varible-group-SSH.png>)

![](<https://cdn.appcircle.io/docs/assets/vg-repo-ssh.png>)