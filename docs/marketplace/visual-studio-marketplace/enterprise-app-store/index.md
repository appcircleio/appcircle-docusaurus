---
title: Setting Up Appcircle Enterprise App Store in Azure DevOps Pipeline
sidebar_label: Enterprise App Store
description: Overview of Azure DevOps Enterprise Store Extension
tags:
  [
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

import Screenshot from '@site/src/components/Screenshot';

<!-- ATTENTION: Documentation at README of this extension's repository
has table of contents that references to the titles in this document. -->

Appcircle Enterprise App Store serves as your private mobile app store, allowing access to in-house apps through a customizable mobile storefront. The Appcircle Enterprise App Store extension enables you to upload your app to your personalized app store within Appcircle.

### System Requirements

**Compatible Azure DevOps Versions:**

- Azure DevOps Services (cloud)
- Azure DevOps Server 2020 (on-premises)
- Azure DevOps Server 2022 (on-premises)

**Compatible Agents:**

Both cloud and self-hosted agents are supported.

- macOS 14 (arm64)
- Ubuntu 22.04 (x86_64)

### Setup Appcircle Enterprise App Store

Refer to our comprehensive [Enterprise App Store Docs](/enterprise-app-store) for detailed information about: Enterprise App Store profiles, portal customization, portal settings, enterprise portal, portal reports, in-app updates and more.

### How to Get the Appcircle Enterprise App Store Extension

#### Permissions

Before installing the extension, ensure you have the necessary permissions in your Azure DevOps organization. If you don't have permission to add extensions, you'll need to [request approval](https://learn.microsoft.com/en-us/azure/devops/marketplace/request-extensions) from your organization administrator.

#### Installation

For details on how to install the extension, visit the Azure [extension installation](https://learn.microsoft.com/en-us/azure/devops/marketplace/install-extension) guide.

**Note:** When visiting the installation guide, ensure you select the correct version of Azure DevOps from the dropdown menu at the top of the page. The available options include "Azure DevOps Services" and "Azure DevOps Server 2022" etc.

You can find the marketplace page for the Appcircle Enterprise App Store extension here:
https://marketplace.visualstudio.com/items?itemName=Appcircle.enterprise-app-store

### How to Add the Appcircle Enterprise App Store Task into Your Pipeline

#### 1. Get a Personal API Token

For this extension to authenticate to your Appcircle, you need to create a Personal API Token, and use it in your task configuration.

You can follow the [Generating and Managing Personal API Tokens](https://docs.appcircle.io/appcircle-api-and-cli/api-authentication#generatingmanaging-the-personal-api-tokens) page to create a PAT.

#### 2. Add Task to Your Pipeline

In order to install Appcircle Enterprise App Store Extension, follow these steps;

1. Go to your pipeline, click "Edit" button on the top right corner.
   <Screenshot url='https://cdn.appcircle.io/docs/assets/testing-distribution-azure-pipeline-edit.png' />
2. Inside your YAML file, search for "Appcircle Enterprise App Store" task.
   <Screenshot url='https://cdn.appcircle.io/docs/assets/SP-242_azure_ent_store_task.png' />
3. Complete the necessary input fields and then click the "Add" button.

#### 3. Configure the Task

After filling out the required fields, the `AppcircleEnterpriseStore@0` task will appear in your pipeline steps as shown below:

```yaml
- task: AppcircleEnterpriseStore@0
  inputs:
    personalAPIToken: $(AC_PERSONAL_API_TOKEN)
    authEndpoint: $(AC_AUTH_ENDPOINT)
    apiEndpoint: $(AC_API_ENDPOINT)
    appPath: $(AC_APP_PATH)
    summary: $(AC_SUMMARY)
    releaseNotes: $(AC_RELEASE_NOTES)
    publishType: $(AC_PUBLISH_TYPE)
```

- `personalAPIToken`: The Appcircle Personal API token used to authenticate and authorize access to Appcircle services within this extension.
- `authEndpoint` (optional): Authentication endpoint URL for self-hosted Appcircle installations. If not specified, uses Appcircle Cloud by default (`auth.appcircle.io`).
- `apiEndpoint` (optional): API endpoint URL for self-hosted Appcircle installations. If not specified, uses Appcircle Cloud by default (`api.appcircle.io`).
- `appPath`: Indicates the file path to the application that will be uploaded to Appcircle Enterprise App Store. The path can be specified in two ways:

  **When Build and Enterprise App Store tasks are in the same pipeline:**
  Assuming you are using Enterprise App Store task after a build step, you can use the output directory of the build step. For example:
  - iOS:
    - `$(Build.SourcesDirectory)/output/app.ipa` or
    - `./output/app.ipa`
  - Android:
    - `$(Build.SourcesDirectory)/app/build/outputs/apk/release/app-release.apk` or
    - `./app/build/outputs/apk/release/app-release.apk`
  
  **When Enterprise App Store task is a separate pipeline:**
  Assuming you have published a build artifact in your build pipeline using `PublishBuildArtifacts` task, you can get the artifact using `DownloadBuildArtifacts` task into a specified directory and use it in the Enterprise App Store pipeline. For example:
  - `$(Build.ArtifactStagingDirectory)/app.ipa`
  - `$(Build.ArtifactStagingDirectory)/app.apk`
  
  Make sure the path points to a valid application package file.

- `releaseNote`: Contains the details of changes, updates, and improvements made in the current version of the app being published.
- `summary`: Used to provide a brief overview of the version of the app that is about to be published.
- `publishType`: Specifies the publishing status as either none, beta, or live, and must be assigned the values "None", "Beta", or "Live" accordingly.

:::caution Build Steps Order
Ensure that this action is added after build steps have been completed.
:::

:::caution
If two workflows start simultaneously, the last workflow to reach the publish step will be the up-to-date version on the Enterprise App Store. If these workflows building the same package version, the first publish will be successful, while later deployments with the same version will fail.
:::

### Using with Appcircle Self-Hosted

#### Self-signed Certificates

Adding custom certificates is **not** currently supported in this extension. 

:::caution
If your self-hosted Appcircle server has self-signed certificates, the Azure DevOps agent that runs the pipeline must trust your Appcircle server's certificates.
:::

### Leveraging Environment Variables

Utilize environment variables seamlessly by substituting the parameters with $(VARIABLE_NAME) in your task inputs. The extension automatically retrieves values from the specified environment variables within your pipeline.

## References

- For details on generating an Appcircle Personal API Token, visit [Generating/Managing Personal API Tokens](/appcircle-api-and-cli/api-authentication#generatingmanaging-the-personal-api-tokens)

- For more detailed instructions and support, visit the [Appcircle Enterprise App Store documentation](/enterprise-app-store).
