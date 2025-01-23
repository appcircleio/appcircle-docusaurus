---
title: Setting Up Appcircle Testing Distribution Task in Azure DevOps Pipeline
sidebar_label: Testing Distribution
description: Overview of self-hosted Appcircle and related concepts regarding testing distribution
tags:
  [
    testing distribution,
    ipa distribution,
    apk distribution,
    binary distribution,
  ]
sidebar_position: 1
---

<!-- ATTENTION: Documentation at README of this extension's repository
has table of contents that references to the titles in this document. -->

The Appcircle distribute extension allows users to upload their apps and start distribution to test groups or individuals.

import Screenshot from '@site/src/components/Screenshot';

### Discover Extension

Before installing the extension, ensure you have the necessary permissions in your Azure DevOps organization. If you don't have permission to add extensions, you'll need to request approval from your organization administrator.

You can discover more about this extension and install it from here:
https://marketplace.visualstudio.com/items?itemName=Appcircle.build-release-task

### System Requirements

The extension can be used on cloud and self-hosted Azure DevOps installations. Supported Azure DevOps Server versions are `2020` and `2022`.

**Compatible Agents:**

Both cloud and self-hosted agents are supported.

- macOS 14 (arm64)
- Ubuntu 22.04 (x86_64)

### How to Add the Appcircle Testing Distribution Task to Your Pipeline

#### 1. Get a Personal API Token

For this extension to authenticate to your Appcircle, you need to create a Personal API Token, and use it in your task configuration.

You can follow the [Generating and Managing Personal API Tokens](https://docs.appcircle.io/appcircle-api-and-cli/api-authentication#generatingmanaging-the-personal-api-tokens) page to create a PAT.

#### 2. Add Task to Your Pipeline

To install the Appcircle Testing Distribution Task Extension, follow these steps:

1. Go to your pipeline, click "Edit" button on the top right corner
   <Screenshot url='https://cdn.appcircle.io/docs/assets/testing-distribution-azure-pipeline-edit.png' />
2. Search for the “Appcircle Testing Distribution" task extension within your `YAML` file.
   <Screenshot url='https://cdn.appcircle.io/docs/assets/SP-242_azure_testing_distribution.png' />
3. Fill out the necessary input fields and click the **Add** button.
   <Screenshot url='https://cdn.appcircle.io/docs/assets/SP-242_azure_testing_distribution_task_detail.png' />

   3.1. You can learn more about getting your personal api token [here](/appcircle-api-and-cli/api-authentication#generatingmanaging-the-personal-api-tokens).

   3.2. Find out how to create a distribution profile [here](/testing-distribution/create-or-select-a-distribution-profile)

#### 3. Usage

After filling out the required fields, the `AppcircleTestingDistribution@0` task will appear in your pipeline steps as shown below:

```yaml
- task: AppcircleTestingDistribution@0
  inputs:
    personalAPIToken: $(AC_PROFILE_API_TOKEN)
    authEndpoint: $(AC_AUTH_ENDPOINT)
    apiEndpoint: $(AC_API_ENDPOINT)
    profileName: $(AC_PROFILE_NAME)
    createProfileIfNotExists: $(AC_CREATE_PROFILE_IF_NOT_EXISTS)
    appPath: $(AC_APP_PATH)
    message: $(AC_MESSAGE)
```

- `personalAPIToken`: The Appcircle Personal API token used to authenticate and authorize access to Appcircle services within this extension.
- `authEndpoint` (optional): Authentication endpoint URL for self-hosted Appcircle installations. Defaults to https://auth.appcircle.io.
- `apiEndpoint` (optional): API endpoint URL for self-hosted Appcircle installations. Defaults to https://api.appcircle.io.
- `profileName`: Specifies the profile that will be used for uploading the app.
- `createProfileIfNotExists` (optional): Ensures that a testing distribution profile is automatically created if it does not already exist; if the profile name already exists, the app will be uploaded to that existing profile instead.
- `appPath`: Indicates the file path to the application package that will be uploaded to Appcircle Testing Distribution Profile. Using absolute paths is recommended with the help of predefined environment variables in Azure DevOps. The path can be specified in two ways:

  **When build and distribution are in the same pipeline:**
  Assuming you are using Testing Distribution task after a build step, you can use the output directory of the build step, for example:
  - For iOS: `$(Build.SourcesDirectory)/output/app.ipa`
  - For Android: `$(Build.SourcesDirectory)/app/build/outputs/apk/release/app-release.apk`
  
  **When distribution is a separate pipeline:**
  Assuming you have published a build artifact in your build pipeline using `PublishBuildArtifacts` task, you can get the artifact using `DownloadBuildArtifacts` task into a specified directory and use it in the distribution pipeline.
  - For example: `$(Build.ArtifactStagingDirectory)/app.ipa` or `$(Build.ArtifactStagingDirectory)/app.apk`
  
  Make sure the path points to a valid application package file.
- `message` (optional): Your message to testers, ensuring they receive important updates and information regarding the application.

### Using with Appcircle Self-Hosted

#### Self-signed Certificates

::: caution
Adding custom certificates is **not** currently supported in this extension. If your self-hosted Appcircle server has self-signed certificates, the Azure DevOps agent that runs the pipeline must trust your Appcircle server's certificates.
:::

### Testing Distribution Integration

Refer to our comprehensive [Testing Distribution Docs](/testing-distribution) for detailed information about: Distribution profiles, Testing groups, Binary re-signing, Testing portal, Reporting and more.

<!-- ### Enterprise App Store Integration

When using the Enterprise App Store plugin, refer to our comprehensive [Enterprise App Store Guide](/enterprise-appstore/overview) for detailed information about:
- Setting release notes
- Creating summaries
- Configuring publish types
- Managing app visibility and distribution -->

### Leveraging Environment Variables

Utilize environment variables seamlessly by substituting the parameters with $(VARIABLE_NAME) in your task inputs. The extension automatically retrieves values from the specified environment variables within your pipeline.

:::caution Build Steps Order
Ensure that this action is added after build steps have been completed.
:::

:::caution
If multiple workflows start simultaneously, the order in which versions are shared in the Testing Distribution is determined by the execution order of the publish step. The version that completes its build and triggers the publish plugin first will be shared first, followed by the others in sequence.
:::

## References

- For details on generating an Appcircle Personel API Token, visit [Generating/Managing Personal API Tokens](/appcircle-api-and-cli/api-authentication#generatingmanaging-the-personal-api-tokens)

- To create or learn more about Appcircle testing and distribution profiles, please refer to [Creating or Selecting a Distribution Profile](/testing-distribution/create-or-select-a-distribution-profile)
