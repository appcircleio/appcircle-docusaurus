---
title: Setting Up Appcircle Enterprise Store in Your Pipeline
sidebar_label: Enterprise Store
description: Overview of Azure DevOps Enterprise Store Extension
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
- task: AppcircleEnterpriseStore@0
  inputs:
    accessToken: "ACCESS_TOKEN" # Appcircle Access Token
    entProfileId: "ENT_PROFILE_ID" # Enterprise Profile Id
    appPath: "APP_PATH" # Your App Path
    summary: "SUMMARY" # Your Summary
    releaseNotes: "RELEASE_NOTE" # Your Release Note
    publishType: "PUBLISH_TYPE" # None, Beta, Live
```

## Leveraging Environment Variables

Utilize environment variables seamlessly by substituting the parameters with $(VARIABLE_NAME) in your task inputs. The extension automatically retrieves values from the specified environment variables within your pipeline.

## References

- For details on generating an Appcircle Personal API Token, visit [Generating/Managing Personal API Tokens](https://docs.appcircle.io/appcircle-api/api-authentication#generatingmanaging-the-personal-api-tokens)

For more detailed instructions and support, visit the [Appcircle Enterprise App Store documentation](https://appcircle.io/enterprise-app-store).
