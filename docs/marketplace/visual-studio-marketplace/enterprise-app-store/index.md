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
- ubuntu-22.04

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
    personalAPIToken: $(AC_PERSONAL_API_TOKEN)
    appPath: $(APP_PATH)
    summary: $(SUMMARY)
    releaseNotes: $(RELEASE_NOTES)
    publishType: $(PUBLISH_TYPE) # "0": None, "1": Beta, "2": Live
```

- `personalAPIToken`: The Appcircle Personal API token is utilized to
  authenticate and secure access to Appcircle services, ensuring that only
  authorized users can perform actions within the platform.
- `appPath`: Indicates the file path to the application that will be uploaded to
  Appcircle Testing Distribution Profile.
- `releaseNote`: Contains the details of changes, updates, and improvements made
  in the current version of the app being published.
- `Summary`: Used to provide a brief overview of the version of the app that is
  about to be published.
- `publishType`: Specifies the publishing status as either none, beta, or live,
  and must be assigned the values "0", "1", or "2" accordingly.

### Leveraging Environment Variables

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
