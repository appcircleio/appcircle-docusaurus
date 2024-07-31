---
title: Setting Up Appcircle Distribute Task in Azure DevOps Pipeline
sidebar_label: Testing Distribution
description: Overview of self-hosted Appcircle and related concepts regarding testing distribution
tags:
  [
    testing-distribution,
    ipa distribution,
    apk distribution,
    binary distribution,
  ]
sidebar_position: 1
---

The Appcircle distribute extension allows users to upload their apps and start distribution to test groups or individuals.

import Screenshot from '@site/src/components/Screenshot';

### Discover Extension

You can discover more about this extension and install it by:
https://marketplace.visualstudio.com/items?itemName=Appcircle.build-release-task

### How to Add the Appcircle Distribute Task Extension to Your Pipeline

To install the Appcircle Distribute Task Extension, follow these steps:

1. Go to your pipeline, click "Edit" button on the top right corner
   <Screenshot url='https://cdn.appcircle.io/docs/assets/testing-distribution-azure-pipeline-edit.png' />
2. Search for the “Appcircle distribute” task extension within your `YAML` file.
   <Screenshot url='https://cdn.appcircle.io/docs/assets/testing-distribution-azure-extension-task.png' />
3. Fill out the necessary input fields and click the **Add** button.
   <Screenshot url='https://cdn.appcircle.io/docs/assets/testing-distribution-azure-extension-task-detail.png' />

   3.1. You can learn more about getting your access token [here](/appcircle-api/api-authentication#generatingmanaging-the-personal-api-tokens).

   3.2. Find out how to create a distribution profile [here](/distribute/create-or-select-a-distribution-profile)

:::caution Build Steps Order
You should add this task extension after completing your build steps.
:::

After filling out the required fields, the `AppcircleEnterpriseStore@0` task will appear in your pipeline steps as shown below:

```yaml
- task: AppcircleTestingDistribution@0
  inputs:
    accessToken: "APPCIRCLE_ACCESS_TOKEN" # Your Appcircle Access Token
    profileId: "APPCIRCLE_PROFILE_ID" # ID of your Appcircle Distribution Profile
    appPath: "BUILD_PATH" # Path to your iOS .ipa or .xcarchive, or Android APK or App Bundle
    message: "Sample Message" # Custom message for your testers
```

## Leveraging Environment Variables

Utilize environment variables seamlessly by substituting the parameters with $(VARIABLE_NAME) in your task inputs. The extension automatically retrieves values from the specified environment variables within your pipeline.

## References

- For details on generating an Appcircle Personel API Token, visit [Generating/Managing Personal API Tokens](/appcircle-api/api-authentication#generatingmanaging-the-personal-api-tokens)

- To create or learn more about Appcircle testing and distribution profiles, please refer to [Creating or Selecting a Distribution Profile](/distribute/create-or-select-a-distribution-profile)
