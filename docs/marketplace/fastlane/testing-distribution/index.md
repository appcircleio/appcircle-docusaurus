---
title: Setting Up Appcircle Testing Distribution Plugin For Fastlane
sidebar_label: Testing Distribution
description: Enhance powerful action to distribute your builds to appcircle with fastlane
tags:
  [
    testing distribution,
    ipa distribution,
    apk distribution,
    binary distribution,
    fastlane-marketplace,
  ]
sidebar_position: 1
---

# Setting Up Appcircle Testing Distribution Plugin

The Appcircle Testing Distribution plugin allows users to upload their apps and start distribution to test groups or individuals.

### Discover Action

You can discover more about this action and install it from:
https://rubygems.org/gems/fastlane-plugin-appcircle_testing_distribution

### System Requirements

**Compatible Agents:**

- macOS 14 (arm64)
- RHEL 9 (x86_64)
- Ubuntu 22.04 (x86_64)

**Supported Version:**

- Fastlane 2.222.0
- Ruby 3.2.2

:::caution
Currently, plugins are only compatible to use with **Appcircle Cloud**. **Self-hosted** support will be available in future releases.
:::

### User Permission Requirements

To perform operations such as generating a Personal API Token, creating a testing distribution profile, and managing testing groups, your user role must have the necessary permissions in the target organization. For more information about user roles and permissions, please refer to the relevant sections of the Role Management documentation below.

- Access to organization or sub-organization and generating PAT: [Organization Management Permissions](https://docs.appcircle.io/account/my-organization/profile-and-team/role-management#organization-management-permissions).
- Testing distribution operations and profile management: [Testing Distribution Permissions](https://docs.appcircle.io/account/my-organization/profile-and-team/role-management#testing-distribution-permissions).
- Testing group management: [Testing Group Permissions](https://docs.appcircle.io/account/my-organization/profile-and-team/role-management#testing-group-permissions).

### How to Add the Appcircle Testing Distribution Action to Your Pipeline

To use the Appcircle Testing Distribution action, install the plugin and add the following step to your pipeline at the end:

```bash
fastlane add_plugin appcircle_testing_distribution
```

```ruby
  appcircle_testing_distribution(
    personalAPIToken: ENV["AC_PERSONAL_API_TOKEN"],
    subOrganizationName: ENV["AC_SUB_ORGANIZATION_NAME"],
    profileName: ENV["AC_PROFILE_NAME"],
    createProfileIfNotExists: ENV["AC_CREATE_PROFILE_IF_NOT_EXISTS"],
    profileCreationSettings: {
      authType: ENV["AC_PROFILE_AUTH_TYPE"],
      username: ENV["AC_PROFILE_USERNAME"],
      password: ENV["AC_PROFILE_PASSWORD"],
      testingGroupNames: ENV["AC_PROFILE_TESTING_GROUP_NAMES"]
    },
    appPath: ENV["AC_APP_PATH"],
    message: ENV["AC_MESSAGE"]
  )
```

- `personalAPIToken`: The Appcircle Personal API token used to authenticate and authorize access to Appcircle services within this plugin.
- `subOrganizationName` (optional): Required when the Root Organization's `personalAPIToken` is used, and you want to create the profile under a sub-organization. In this case, provide the name of the sub-organization in this field. If you directly used the sub-organization's `personalAPIToken`, this parameter is not needed.
- `profileName`: Specifies the profile that will be used for uploading the app.
- `createProfileIfNotExists` (optional): Ensures that a testing distribution profile is automatically created if it does not already exist; if the profile name already exists, the app will be uploaded to that existing profile instead.
- `profileCreationSettings` (optional): If `createProfileIfNotExists` is `true` and a new profile being created, the profile will be configured with these settings.
  - `authType`: Authentication type of the profile. `none`: None, `static`: Static Username and Password, `ldap`: LDAP Login, `sso`: SSO Login.
  - `username`: The username for the profile if authentication type set to `static` (Static Username and Password).
  - `password`: The password for the profile if authentication type set to `static` (Static Username and Password).
  - `testingGroupNames`: Uploaded versions will be automatically shared with these testing groups. Example format: `group1, group2, group3`.
- `appPath`: Indicates the file path to the application package that will be uploaded to Appcircle Testing Distribution Profile.
- `message`: Your message to testers, ensuring they receive important updates and information regarding the application.

:::tip
Profile creation settings are only used when a new profile is created. If you need to update these settings, please go to the [profile settings](https://docs.appcircle.io/testing-distribution/create-or-select-a-distribution-profile#settings) in the Appcircle dashboard.
:::

:::caution Build Steps Order
Ensure that this action is added after build steps have been completed.
:::

:::caution
If multiple workflows start simultaneously, the order in which versions are shared in the Testing Distribution is determined by the execution order of the publish step. The version that completes its build and triggers the publish plugin first will be shared first, followed by the others in sequence.
:::

### Distributing to Sub-Organizations

To distribute your app to a sub-organization, you can use one of the following methods:

#### 1. Using the Root Organization's Personal API Token

- Obtain the `personalAPIToken` for the Root Organization. This token is used to authenticate and authorize actions within Appcircle.
- Specify the `subOrganizationName` parameter in your configuration. This parameter indicates the target sub-organization where the profile will be created and the app will be distributed.

#### 2. Using the Sub-Organization's Personal API Token

- Invite your user to the sub-organization and obtain the `personalAPIToken` for the sub-organization. This token directly authenticates and authorizes actions within the specific sub-organization.
- Use the sub-organization's `personalAPIToken` in your configuration.

With this configuration, the profile will be created and the app will be distributed within the sub-organization.

### CLI Usage

Recommended method of using the action is adding it to the `Fastfile` as described [above](https://docs.appcircle.io/marketplace/fastlane/testing-distribution#how-to-add-the-appcircle-distribute-action-to-your-pipeline).

If you prefer to use it from the terminal, you can execute the following command and enter the inputs interactively:

```bash
fastlane run appcircle_testing_distribution
```

To pass parameters with the command, you can use the `:symbol` format. For example:

```bash
fastlane run appcircle_testing_distribution parameter1:"value1" parameter2:"value2"
```

:::caution IMPORTANT NOTE
The CLI only supports primitive types such as integers, floats, booleans, and strings. Arrays can be passed as a comma-separated string (e.g., `parameter:"value1,value2,value3"`). Hashes are not currently supported, so to use parameters like `profileCreationSettings`, it is recommended to add the action to the `Fastfile` as described.
:::

### Leveraging Environment Variables

Utilize environment variables seamlessly by substituting the parameters with `ENV["VARIABLE_NAME"]` in your task inputs. The extension automatically retrieves values from the specified environment variables within your pipeline.

## References

- For details on generating an Appcircle Personal API Token, visit [Generating/Managing Personal API Tokens](/appcircle-api-and-cli/api-authentication#generatingmanaging-the-personal-api-tokens).

- To create or learn more about Appcircle testing and distribution profiles, please refer to [Creating or Selecting a Distribution Profile](/testing-distribution/create-or-select-a-distribution-profile).
