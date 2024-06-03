---
title: Setting Up Appcircle Enterprise App Store in Your Pipeline
sidebar_label: Enterprise App Store
description: Overview of Azure DevOps Enterprise App Store Extension
tags:
  [
    testing-distribution,
    overview,
    concepts,
    app store,
    internal testing,
    beta testing,
    binary distribution,
    ipa distribution,
    apk distribution,
  ]
sidebar_position: 2
---

Appcircle Enterprise Mobile App Store serves as your private mobile app store, allowing access to in-house apps through a customizable mobile storefront. The Appcircle Enterprise Mobile App Store extension enables you to upload your app to your personalized app store within Appcircle.

import Screenshot from '@site/src/components/Screenshot';

### How to Install the Appcircle Enterprise Store Task in Your Pipeline

In order to install Appcircle Enterprise Store task extension, follow these steps;

1. Go to your pipeline, click "Edit" button on the top right corner
   <Screenshot url='https://cdn.appcircle.io/docs/assets/testing-distribution-azure-pipeline-edit.png' />
2. Inside your YAML file, search for "Appcircle Enterprise Store" task extension
   <Screenshot url='https://cdn.appcircle.io/docs/assets/ac-app-store-azure-extension-task.png' />
3. Complete the necessary input fields and then click the "Add" button.

   3.1. You can learn more about getting your access token [here](https://docs.appcircle.io/appcircle-api/api-authentication#generatingmanaging-the-personal-api-tokens).

:::info
You should add this task extension after completing your build steps.
:::

After filling out the required fields, the `AppcircleEnterpriseStore@0` task will appear in your pipeline steps as shown below:

```yaml
- task: AppcircleDistribute@0
  inputs:
    accessToken: "APPCIRCLE_ACCESS_TOKEN" # Your Appcircle Access Token
    profileId: "APPCIRCLE_PROFILE_ID" # ID of your Appcircle Distribution Profile
    appPath: "BUILD_PATH" # Path to your iOS .ipa or .xcarchive, or Android APK or App Bundle
    message: "Sample Message" # Custom message for your testers
```

## Leveraging Environment Variables

Utilize environment variables seamlessly by substituting the parameters with $(VARIABLE_NAME) in your task inputs. The extension automatically retrieves values from the specified environment variables within your pipeline.

## References

- For details on generating an Appcircle Personal Access Token, visit [Generating/Managing Personal API Tokens](https://docs.appcircle.io/appcircle-api/api-authentication#generatingmanaging-the-personal-api-tokens)

For more detailed instructions and support, visit the [Appcircle Enterprise App Store documentation](https://appcircle.io/enterprise-app-store).
