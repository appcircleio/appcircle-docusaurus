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

You can discover more about this extension and install it by:
https://marketplace.visualstudio.com/items?itemName=Appcircle.build-release-task

### System Requirements

**Compatible Agents:**

- macOS 14 (arm64)
- Ubuntu 22.04 (x86_64)

### How to Add the Appcircle Testing Distribution Task to Your Pipeline

To install the Appcircle Testing Distribution Task Extension, follow these steps:

1. Go to your pipeline, click "Edit" button on the top right corner
   <Screenshot url='https://cdn.appcircle.io/docs/assets/testing-distribution-azure-pipeline-edit.png' />
2. Search for the “Appcircle Testing Distribution" task extension within your `YAML` file.
   <Screenshot url='https://cdn.appcircle.io/docs/assets/SP-242_azure_testing_distribution.png' />
3. Fill out the necessary input fields and click the **Add** button.
   <Screenshot url='https://cdn.appcircle.io/docs/assets/SP-242_azure_testing_distribution_task_detail.png' />

   3.1. You can learn more about getting your personal api token [here](/appcircle-api-and-cli/api-authentication#generatingmanaging-the-personal-api-tokens).

   3.2. Find out how to create a distribution profile [here](/testing-distribution/create-or-select-a-distribution-profile)

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
- `appPath`: Indicates the file path to the application package that will be uploaded to Appcircle Testing Distribution Profile.
- `message` (optional): Your message to testers, ensuring they receive important updates and information regarding the application.

### Using with Appcircle Self-Hosted

#### Self-signed Certificates

::: caution
Adding custom certificates is **not** currently supported in this extension. If your self-hosted Appcircle server has self-signed certificates, the Azure DevOps agent that runs the pipeline must trust your Appcircle server's certificates.
:::

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
