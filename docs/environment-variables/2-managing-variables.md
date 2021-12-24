---
title: "Creating and Using Environment Variables"
metaTitle: "Creating and Using Environment Variables"
metaDescription: "Creating and Using Environment Variables"
---
# Creating and Using Environment Variables

### Creating environment variable groups

To create an environment variable group, select Environment Variables from the build module. Click on the orange + icon and enter the name of the group into the input box, press enter to save the group name and create the group.

![](<../assets/image (76).png>)



### &#x20;Adding key and text-based value pairs

To add an environment variable to the group, select the "Text" tab from the top and use the inputs below. Enter a key name, then enter the value for the key and press enter.

![](<../assets/image (77).png>)



You can add as many environment variables as you need.&#x20;

:::info


Variables that need to be secret can be hidden using the lock icon. Such variables cannot be viewed by the users during the build process.

:::

Please note that some environment variables may need to be duplicated to be used in different groups for different purposes.

![](<../assets/image (78).png>)



### Adding files as environment variables

You can also add files as environment variables and use them in build workflows in the same way. They can be used for things like API-key based authentication in Firebase or for adding dSYM files.

To add a file, select the "File" tab from the top and enter a key name from the inputs below. Then select a file from the file browser that opens when you click the file field.

Then press add to upload the file.

![](<../assets/image (79).png>)

![](<../assets/image (80).png>)

###

### Using environment variable groups in builds

Environment variable groups can be used in builds to extend the workflow and add additional actions to workflow steps.

To add an environment variable group to a build, go to the build profile from the build module and select _Build Configuration > Env. Variables_

Here, you can see a list of previously created environment variable groups. Select the groups you want to be included in this specific build profile. Then click Save to save your selection.

Then in workflows, you can specify the environment variable for use.

![](<../assets/09-12-EnvVars (1).jpg>)
