---
title: Setting Up Appcircle Enterprise App Store in Your Pipeline
sidebar_label: Enterprise App Store
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

Appcircle Enterprise App Store serves as your private mobile app store, allowing access to in-house apps through a customizable mobile storefront. The Appcircle Enterprise App Store extension enables you to upload your app to your personalized app store within Appcircle.

import Screenshot from '@site/src/components/Screenshot';

## System Requirements

**Compatible Agents:**

- macos-14 (arm64)

:::caution
Currently, plugins are only compatible to use with **Appcircle Cloud**. **Self-hosted** support will be available in future releases.
:::

### How to Install the Appcircle Enterprise App Store Task in Your Pipeline

In order to install Appcircle Enterprise App Store task extension, follow these steps;

1. Go to your pipeline, click "Edit" button on the top right corner
   <Screenshot url='https://cdn.appcircle.io/docs/assets/testing-distribution-azure-pipeline-edit.png' />
2. Inside your YAML file, search for "Appcircle Enterprise App Store" task extension
   <Screenshot url='https://cdn.appcircle.io/docs/assets/SP-242_azure_ent_store_task.png' />
3. Complete the necessary input fields and then click the "Add" button.

   3.1. You can learn more about getting your personal api token [here](https://docs.appcircle.io/appcircle-api/api-authentication#generatingmanaging-the-personal-api-tokens).

After filling out the required fields, the `AppcircleEnterpriseStore@0` task will appear in your pipeline steps as shown below:

```yaml
- task: AppcircleEnterpriseStore@0
  inputs:
    personalAPIToken: $(AC_PROFLE_API_TOKEN)
    profileName: $(AC_PROFILE_NAME)
    createProfileIfNotExists: $(CREATE_PROFILE_IF_NOT_EXISTS)
    appPath: $(APP_PATH)
    message: $(MESSAGE)
```

- `personalAPIToken`: The Appcircle Personal API token is used to authenticate and secure access to Appcircle services. Add this token to your credentials to enable its use in your pipeline and ensure authorized actions within the platform.
- `profileName`: Specifies the profile that will be used for uploading the app.
- `createProfileIfNotExists`: Ensures that a user profile is automatically created if it does not already exist; if the profile name already exists, the app will be uploaded to that existing profile instead.
- `appPath`: Indicates the file path to the application package that will be uploaded to Appcircle Testing Distribution Profile.
- `message`: Your message to testers, ensuring they receive important updates and information regarding the application.

## Leveraging Environment Variables

Utilize environment variables seamlessly by substituting the parameters with $(VARIABLE_NAME) in your task inputs. The extension automatically retrieves values from the specified environment variables within your pipeline.

:::caution Build Steps Order
Ensure that this action is added after build steps have been completed.
:::

:::caution
If multiple workflows start simultaneously, the order in which versions are shared in the Testing Distribution is determined by the execution order of the publish step. The version that completes its build and triggers the publish plugin first will be shared first, followed by the others in sequence.
:::

## References

- For details on generating an Appcircle Personal API Token, visit [Generating/Managing Personal API Tokens](https://docs.appcircle.io/appcircle-api/api-authentication#generatingmanaging-the-personal-api-tokens)

- For more detailed instructions and support, visit the [Appcircle Enterprise App Store documentation](/enterprise-app-store).
