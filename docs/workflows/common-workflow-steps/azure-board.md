---
title: Azure Boards
description: Manage your software development process with Azure Boards. Track work items' progress throughout the development lifecycle.
tags: [workflow, build and test, azure, boards]
---

import Screenshot from '@site/src/components/Screenshot';

# Azure Boards

Azure Boards is a standalone service within the Azure DevOps suite that helps teams plan, track, and discuss work across the entire software development process. It provides a flexible, customizable platform for managing work items, such as user stories, bugs, tasks, and issues, so you can track your work item's progress throughout the development lifecycle.

You can use the [Azure Boards Component](https://github.com/appcircleio/appcircle-azure-boards-component/) to add a comment and change the status of your issues according to the status of your workflow.

<Screenshot url='https://cdn.appcircle.io/docs/assets/azure-component1.png' />

### Prerequisites

There are no prerequisites required before using the **Azure Boards** step. It depends on your business decision which step to use before or after in your workflow.

:::caution

Please note that once the **Azure Boards** component has run successfully, the status of the relevant article in your Azure Board account will be changed. If the build fails in Appcircle, an incorrect status may appear in your Azure Board account. Make sure you use it in the correct order in Workflow.

:::

### Configuration of Component

To add a comment, the issue ID `$AC_AZUREBOARD_WORKITEM` must be supplied to the component. We need to get this issue ID dynamically so that our workflow can work for multiple branches. Appcircle components use environment variables to pass the state. We can add a step just before the Azure Boards component to prepare the necessary environment variables.

Let's say you're working on a feature branch called feature/onboarding-1. You may use the below Ruby script to get issue ID 1 from the branch name and use this information with the Azure Boards component. Please see the [**Custom Script step documentation**](/workflows/common-workflow-steps/upload-files-to-amazon-s3) for this implementation.

```ruby
branch = ENV['AC_GIT_BRANCH']
issue_number = branch.split('-')[1]
puts issue_number

# Write Environment Variable
open(env_var_path, 'a') { |f|
    f.puts "AC_AZUREBOARD_WORKITEM=#{issue_number}"
}
```

### Input Variables

This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3049-azureInput.png' />

:::danger Sensitive Variables

Please do not use sensitive variables such as **Username**, **Password**, **API Key**, or **Personal Access Key** directly within the step.

We recommend using [**Environment Variables**](/environment-variables/managing-variables) groups for such sensitive variables.

:::

| Variable Name                  | Description                                                                                                                                                                                                                                                                                      | Status   |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| `$AC_AZUREBOARD_INSTANCE`      | Your Azure Board subdomain. If you're using a self-hosted instance, write the instance URL. For example: `https://dev.azure.com`                                                                                                                                                                 | Required |
| `$AC_AZUREBOARD_API_VERSION`   | The version of the Azure DevOps Services REST API. The default value is `7.0`                                                                                                                                                                                                                    | Required |
| `$AC_AZUREBOARD_EMAIL`         | Email of Azure user. Please use [**Environment Variables**](/environment-variables/).                                                                                                                                                                                                            | Required |
| `$AC_AZUREBOARD_TOKEN`         | Personal access token of the user. It can be created by visiting User settings. Please use [**Environment Variables**](/environment-variables/).                                                                                                                                                 | Required |
| `$AC_AZUREBOARD_ORG`           | Azure Organization. The organization can be identified by its URL, such as for the `https://dev.azure.com/JohnDoe/MyProject/_boards/board/t/MyTeam/Issues` **JohnDoe** is the organization name.                                                                                                 | Required |
| `$AC_AZUREBOARD_PROJECT`       | Azure Project. The project can be identified by its URL, such as for the `https://dev.azure.com/JohnDoe/MyProject/_boards/board/t/MyTeam/Issues` **MyProject** is the project name.                                                                                                              | Required |
| `$AC_AZUREBOARD_WORKITEM`      | Azure work item ID. The work item ID (integer) is shown next to the issue.                                                                                                                                                                                                                       | Required |
| `$AC_AZUREBOARD_FAIL_STATE`    | The state name for the failed step. If the previous state fails, you can optionally change the state of your issue.                                                                                                                                                                              | Optional |
| `$AC_AZUREBOARD_SUCCESS_STATE` | The state name for the successful step. If the previous state succeeds, you can optionally change the state of your issue.                                                                                                                                                                       | Optional |
| `$AC_AZUREBOARD_TEMPLATE`      | This comment template will be used to post a comment. Variables donated with `$` will be replaced during the build. Please check [this document](https://learn.microsoft.com/en-us/rest/api/azure/devops/wit/work-items/update?view=azure-devops-rest-7.0) to learn more about possible updates. | Required |

:::tip

If you add state names for successful and failed steps (`$AC_AZUREBOARD_FAIL_STATE` and `$AC_AZUREBOARD_SUCCESS_STATE`), the Azure Boards component will automatically change the status of your issue according to the state of your workflow.

:::

### Changing Template

Appcircle provides a default template that adds the commit ID, branch name, and a couple of environment variables. When you're adding a comment, you may use HTML. This template can be edited and modified according to the Azure API. You can check [this document](https://learn.microsoft.com/en-us/rest/api/azure/devops/wit/work-items/update?view=azure-devops-rest-7.0&tabs=HTTP/) to create your custom comments.

Please check the [Azure Boards Component](https://github.com/appcircleio/appcircle-azure-boards-component/) documentation for more information.

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-azure-boards-component/
