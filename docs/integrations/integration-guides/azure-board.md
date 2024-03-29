---
title: Azure Boards Integration
metaTitle: Azure Boards Integration
metaDescription: Azure Boards Integration
sidebar_position: 9
---

import Screenshot from '@site/src/components/Screenshot';

# Azure Boards Integration

Azure Boards is a standalone service within the Azure DevOps suite that helps teams plan, track, and discuss work across the entire software development process. It provides a flexible, customizable platform for managing work items, such as user stories, bugs, tasks, and issues, so you can track your work item's progress throughout the development lifecycle.

You can use [Azure Boards Component](https://github.com/appcircleio/appcircle-azure-boards-component/) to add a comment and change the status of your issues according to the status of your workflow. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/azure-component1.png' />

## Credentials

In order to use Azure Boards Component, you need to configure the component and add the necessary credentials. It is strongly advised to add the credentials of your Azure instance with locked environment variables.

<Screenshot url='https://cdn.appcircle.io/docs/assets/azure-component2.png' />


- `AC_AZUREBOARD_INSTANCE`: Instance. If you're using a self-hosted instance, write the instance URL.
- `AC_AZUREBOARD_API_VERSION`: API Version. The version of the Azure DevOps Services REST API
- `AC_AZUREBOARD_EMAIL`: Email. Email of Azure user. Please add this using **locked** environment variables.
- `AC_AZUREBOARD_TOKEN`: Personal Access Token. Personal access token of the user. It can be created by visiting User settings. Please add this using **locked** environment variables.
- `AC_AZUREBOARD_ORG`: Organization. Azure Organization. The organization can be identified by its URL, such as for the `https://dev.azure.com/JohnDoe/MyProject/_boards/board/t/MyTeam/Issues` **JohnDoe** is the organization name.
- `AC_AZUREBOARD_PROJECT`: Project. Azure Project. The project can be identified by its URL, such as for the `https://dev.azure.com/JohnDoe/MyProject/_boards/board/t/MyTeam/Issues` **MyProject** is the project name.

After creating the above environment variables, please don't forget to select and save them.

<Screenshot url='https://cdn.appcircle.io/docs/assets/azure-component3.png' />


## Configuring Component

To add a comment, the issue id(`AC_AZUREBOARD_WORKITEM`) must be supplied to the component. We need to get this issue id dynamically so that our workflow can work for multiple branches. Appcircle components use environment variables to pass the state. We can add a step just before the Azure Boards Component to prepare the necessary environment variables. 

Let's say, you're working on a feature branch called `feature/onboarding-1`. You may use the below Ruby script to get the issue id `1` from the branch name and use this information with the Azure Boards component.

```ruby
branch = ENV['AC_GIT_BRANCH']
issue_number = branch.split('-')[1]
puts issue_number

# Write Environment Variable
open(env_var_path, 'a') { |f|
    f.puts "AC_AZUREBOARD_WORKITEM=#{issue_number}"
}
```

## Changing State

If you add state names for successful and failed steps(`AC_AZUREBOARD_FAIL_STATE`, `AC_AZUREBOARD_SUCCESS_STATE`), the Azure Boards component will automatically change the status of your issue according to the state of your workflow.

## Changing Template

Appcircle provides a default template that adds the commit id, branch name, and a couple of environment variables. When you're adding comment, you may use HTML. This template can be edited and modified according to Azure API. You can check [this document](https://learn.microsoft.com/en-us/rest/api/azure/devops/wit/work-items/update?view=azure-devops-rest-7.0&tabs=HTTP/) to create your custom comments.

Please check [Azure Boards Component](https://github.com/appcircleio/appcircle-azure-boards-component/) documentation for more information.