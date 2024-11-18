---
title: Azure DevOps Bot for Detekt Report
description: The Azure DevOps Bot for Detekt Report step analyze your Detekt report and post the report details within the opened pull request in Azure DevOps.
tags: [detekt report, analysis]
---

import Screenshot from '@site/src/components/Screenshot';

# Azure DevOps Bot for Detekt Report

The **Azure DevOps Bot for Detekt Report** step analyzes your [Detekt report](https://detekt.dev/docs/introduction/reporting/) and posts the details to an open pull request in [Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/). It also allows you to modify the [pull request status](https://learn.microsoft.com/en-us/rest/api/azure/devops/git/pull-request-statuses).

:::caution

[Danger](https://danger.systems/) operates on a similar principle, allowing use of the [Danger step](/workflows/common-workflow-steps/danger) with platforms such as [GitHub](https://github.com/), [GitLab](https://about.gitlab.com/), and [Bitbucket](https://bitbucket.org/product/guides/getting-started/overview#a-brief-overview-of-bitbucket). However, Danger currently does not support Azure DevOps.

For more information, refer to the Appcircle blog post about Danger:
- [**Danger in CI: Automate Your Mobile Code Reviews**](https://appcircle.io/blog/danger-in-ci-automate-your-mobile-code-reviews).

:::

### Prerequisites

Before running the **Azure DevOps Bot for Detekt Report** step, you must complete certain prerequisites, as detailed in the table below:

| Prerequisite Workflow Step                       | Description                                      |
 |-------------------------------------------------|--------------------------------------------------|
 | [**Detekt**](/workflows/android-specific-workflow-steps/detekt) | In order to generate the [Detekt report](https://detekt.dev/docs/introduction/reporting/), the **Detekt** step must be executed beforehand.  |

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-azure-bot-for-detekt-report_1.png'/>

### Input Variables

This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-azure-bot-for-detekt-report_2.png'/>

:::danger Sensitive Variables

Please do not use sensitive variables such as **Username**, **Password**, **API Key**, or **Personal Access Key** directly within the step.

We recommend using [**Environment Variables**](/environment-variables/managing-variables) groups for such sensitive variables.

:::

| Variable Name              | Description                                    | Status |
|----------------------------|------------------------------------------------|--------|
| `$AC_AZURE_ORG_NAME`       | Specifies the name of the Azure DevOps organization. You can find it in the Azure DevOps URL:  `https://dev.azure.com/{Your_Organization}`. Check out [this document](https://learn.microsoft.com/en-us/answers/questions/1080972/find-organization-name) to locate the organization name. | Required |
| `$AC_AZURE_PROJECT_NAME`   | Specifies the name of the Azure DevOps project. You can find it in the Azure DevOps URL: `https://dev.azure.com/{Your_Organization}/{Your_Project}`. For more information about Azure DevOps projects, refer to [this document](https://learn.microsoft.com/en-us/azure/devops/user-guide/project-admin-tutorial?toc=%2Fazure%2Fdevops%2Forganizations%2Ftoc.json&view=azure-devops). | Required |
| `$AC_AZURE_REPO_NAME`      | Specifies the name of the Azure DevOps repository. Check out [this document](https://learn.microsoft.com/en-us/azure/devops/repos/git/repository-settings) for more details about Azure DevOps repositories. | Required |
| `$AC_AZURE_BASE_URL`       | Specifies the base URL of Azure DevOps. The default value is `https://dev.azure.com`. | Required |
| `$AC_AZURE_API_KEY`        | Specifies the API key for Azure DevOps. Refer to [this document](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate) for details on how to obtain it. | Required |
| `$AC_DETEKT_FILE_PATH`     | Specifies the file path of the Detekt report. If you used the **Detekt** step in the previous stage, this section will be automatically filled. The default value is `$AC_DETEKT_OUTPUT_PATH`, which represents the output of the **Detekt** step. | Required |
| `$AC_DOMAIN_NAME`          | Specifies the domain name of Appcircle. The default value is `my.appcircle.io`, which is the domain for Appcircle Cloud. | Required |
| `$AC_AZURE_API_VERSION`    | Specifies the version of the Azure API, for example: `7.1`. Refer to the [REST API versioning](https://learn.microsoft.com/en-us/azure/devops/integrate/concepts/rest-api-versioning) document for more information. | Required |

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-android-azure-bot-for-detekt-component.git