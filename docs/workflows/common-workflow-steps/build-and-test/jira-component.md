---
title: Jira Component
metaTitle: Jira Component
metaDescription: Jira Component
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';

# Jira Component

Jira is a software development tool used for issue tracking, project management, and agile software development. It allows users to plan, track, and release software projects. Jira's core functionality includes the ability to create and assign tasks, track progress and status, and collaborate with team members.

By adding Appcircle's [**Jira Component**](https://github.com/appcircleio/appcircle-jira-component/) component to your workflow, you can add comments or change their status according to your workflow.

<Screenshot url='https://cdn.appcircle.io/docs/assets/jira-component1.png' />

### Prerequisites

There is no mandatory sequence for the use of this component. It depends on your business decision which step to use before or after in your workflow.

:::caution
Please note that once the Jira Component has run successfully, the status of the relevant article in your Jira account will be changed. If the build fails in Appcircle, an incorrect status may appear in your Jira account. Make sure you use it in the correct order in Workflow.
:::

### Configuration of Component

To add a comment, the issue ID must be supplied to the component. We need to get this issue ID dynamically so that our workflow can work for multiple branches. Appcircle components use environment variables to pass the state. We can add a step just before the Jira Component to prepare the necessary environment variables.

For example, you're working on a feature branch called `feature/jiraissue-1`. You may use the below Ruby script to get `jiraissue-1` from the branch name and use this information with the Jira component. Please see the [**Custom Script step documentation**](/workflows/common-workflow-steps/build-and-test/custom-script) for this implementation.

```ruby
branch = ENV['AC_GIT_BRANCH']
feature_name = branch.split('/')[1].upcase
puts feature_name

# Write Environment Variable
open(ENV['AC_ENV_FILE_PATH'], 'a') { |f|
    f.puts "AC_JIRA_ISSUE=#{feature_name}"
}
```

### Input Variables

There are some necessary parameters for this stepper to work properly. These parameters are given in the table below with their explanations.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3049-jiraInput.png' />

:::warning
**Do not hard-code sensitive variables, such as tokens and API keys, directly to the parameters in the step.**

We recommend using [Environment Variables](/environment-variables/) groups for such sensitive variables.
:::

| Variable Name                 | Description                                                                                                                                                                           | Status   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `$AC_JIRA_HOST`               | Your Jira subdomain. For example: `mysubdomain.atlassian.net`                                                                                                                         | Required |
| `$AC_JIRA_EMAIL`              | Email of Jira user. Please use [**Environment Variables**](/environment-variables/).                                                                                                  | Required |
| `$AC_JIRA_TOKEN`              | User's API Token. Please use [**Environment Variables**](/environment-variables/). You can create your token from [here](https://id.atlassian.com/manage-profile/security/api-tokens) | Required |
| `$AC_JIRA_ISSUE`              | The ID or key of the issue.                                                                                                                                                           | Required |
| `$AC_JIRA_FAIL_TRANSITION`    | Transition ID or name for the failed step. If the previous state succeeds, you can optionally change the status of your issue.                                                        | Optional |
| `$AC_JIRA_SUCCESS_TRANSITION` | Transition ID or name for the successful step. If the previous state succeeds, you can optionally change the status of your issue.                                                    | Optional |
| `$AC_JIRA_TEMPLATE`           | This comment template will be used to post a comment. Variables donated with `$` will be replaced during the build.                                                                   | Required |

### Changing Template

Appcircle provides a default template that adds commit id, branch name, time in UTC, and a couple of environment variables. However, this template can be edited and modified according to the Atlassian Document Format (ADF). You can use [ADF Builder](https://developer.atlassian.com/cloud/jira/platform/apis/document/playground/) to create your custom comments.

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-jira-component
