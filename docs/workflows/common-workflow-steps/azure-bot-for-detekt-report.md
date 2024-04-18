---
title: Azure DevOps Bot for Detekt Report
description: The Azure DevOps Bot for Detekt Report step analyze your Detekt report and post the report details within the opened pull request in Azure DevOps.
tags: [Azure-DevOps, Detekt-Report, analysis]
sidebar_position: 5
---

import Screenshot from '@site/src/components/Screenshot';

# Azure DevOps Bot for Detekt Report

The **Azure DevOps Bot for Detekt Report** step allows you to analyse your [Detekt report](https://detekt.dev/docs/introduction/reporting/) and post the report details under the opened pull request in [Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/). Additionally, you can modify the [pull request status](https://learn.microsoft.com/en-us/rest/api/azure/devops/git/pull-request-statuses). Integration requires following some necessary steps.

:::caution
[Danger](https://danger.systems) works on a similar logic to this step, allowing you to utilise the [Danger step](https://docs.appcircle.io/workflows/common-workflow-steps/#code-reviews-with-danger) for other providers like [GitHub](https://github.com), [GitLab](https://about.gitlab.com), or [Bitbucket](https://bitbucket.org/product/guides/getting-started/overview#a-brief-overview-of-bitbucket). Nonetheless, it's worth noting that Danger does not offer support for Azure DevOps at this time.

For more information, refer to the Appcircle blog post about Danger:
- [**Danger in CI: Automate Your Mobile Code Reviews**](https://appcircle.io/blog/danger-in-ci-automate-your-mobile-code-reviews).
:::

### Prerequisites

The workflow steps that need to be executed before running the **Azure DevOps Bot for Detekt Report** workflow step, along with their respective reasons, are listed in the table below.

| Prerequisite Workflow Step                       | Description                                      |
 |-------------------------------------------------|--------------------------------------------------|
 | [Detekt](https://docs.appcircle.io/workflows/android-specific-workflow-steps/#detekt) | In order to generate the [Detekt report](https://detekt.dev/docs/introduction/reporting/), the **Detekt** step must be executed beforehand.  |

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-azure-bot-for-detekt-report_1.png'/>

### Input Variables
For each step, specific input variables are required for its operation on your system. The input variables necessary for the **Azure DevOps Bot for Detekt Report** are as follows:

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-azure-bot-for-detekt-report_2.png'/>

:::caution
Confidential information should be entered as a [**secret environment variable**](https://docs.appcircle.io/environment-variables/managing-variables#adding-key-and-text-based-value-pairs). Also, ensure that the [**environment variable group**](https://docs.appcircle.io/environment-variables/managing-variables#using-environment-variable-groups-in-builds) is selected in the [Configuration](https://docs.appcircle.io/build/build-profile-configuration/).
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