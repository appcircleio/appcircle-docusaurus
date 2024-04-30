---
title: Azure Bot for Swiftlint
description: Integrate Azure DevOps Bot with SwiftLint to analyze and report details under PRs. Automate builds with configured triggers.
tags: [ios, build, test, workflow, step]
---

import Screenshot from '@site/src/components/Screenshot';

# Azure Bot for Swiftlint

With the Azure DevOps Bot for Swiftlint integration, you can analyze your [**SwiftLint**](https://github.com/realm/SwiftLint/) and post the report details under the opened PR. You can also modify the PR status.

:::info
This component will work in builds that are automatically triggered by a configured trigger. To achieve this, you need to open a PR and set up the trigger. Further information for **Trigger Build**, please follow the [documantation](/build/build-process-management/build-manually-or-with-triggers/).
:::

:::caution
If there are warnings or errors in the SwiftLint report, this workflow step will fail and stop the build.
:::

:::warning
For this component to work, a PR must be opened, and a trigger must be set up based on this PR. If the build is triggered manually, the component will not function.
:::

### Prerequisites

The workflow steps that need to be executed before running the **Swiftlint** workflow step, along with their respective reasons, are listed in the table below.

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [**Swiftlint**](/workflows/ios-specific-workflow-steps/swiftlint) | This component will check the source code for programmatic as well as stylistic errors. This is helpful in identifying some common and uncommon mistakes that are made during coding. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3049-azureBotOrder.png' />

### Input Variables

This component needs some parameters to operate. You can find the required parameters and their detailed descriptions in the list below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3049-azureBotInput.png' />

:::warning
**Do not hard-code sensitive variables, such as tokens and API keys, directly to the parameters in the step.**

We recommend using [Environment Variables](/environment-variables/) groups for such sensitive variables.
:::

| Variable Name                            | Description                         | Status           |
|-------------------------------|------------------------------------------------|------------------|
| `$AC_LINT_PATH`         | This is the Swiftlint report path, this path will being automatically generated, if Swiftlint step runs. | Required |
| `$AC_AZURE_ORG_NAME`               | Specifies the name of the Azure DevOps organization. You can find it in the Azure DevOps URL:  `https://dev.azure.com/{Your_Organization}`. Check out [this document](https://learn.microsoft.com/en-us/answers/questions/1080972/find-organization-name) to locate the organization name. | Required |
| `$AC_AZURE_PROJECT_NAME`              | Specifies the name of the Azure DevOps project. You can find it in the Azure DevOps URL: `https://dev.azure.com/{Your_Organization}/{Your_Project}`. For more information about Azure DevOps projects, refer to [this document](https://learn.microsoft.com/en-us/azure/devops/user-guide/project-admin-tutorial?toc=%2Fazure%2Fdevops%2Forganizations%2Ftoc.json&view=azure-devops). | Required |
| `$AC_AZURE_REPO_NAME`             | Specifies the name of the Azure DevOps repository. Check out [this document](https://learn.microsoft.com/en-us/azure/devops/repos/git/repository-settings) for more details about Azure DevOps repositories. | Required |
| `$AC_AZURE_BASE_URL`           | Specifies the base URL of Azure DevOps. The default value is `https://dev.azure.com`. | Required |
| `$AC_AZURE_API_KEY`             | Specifies the API key for Azure DevOps. Refer to [this document](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate) for details on how to obtain it. | Required |
| `$AC_DOMAIN_NAME`               | Specifies the domain name of Appcircle. The default value is `my.appcircle.io`, which is the domain for Appcircle Cloud. | Required |
| `$AC_AZURE_API_VERSION`               | Specifies the version of the Azure API, for example: `7.1`. Refer to the [REST API versioning](https://learn.microsoft.com/en-us/azure/devops/integrate/concepts/rest-api-versioning) document for more information. | Required |

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-ios-azure-bot-for-swiftlint-component

