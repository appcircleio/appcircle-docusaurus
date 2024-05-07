---
title: Jira Comment
description: Explore Jira Comment, a tool for efficient project management and issue tracking. Enhance your workflow with Appcircle's integration.
tags: [jira, workflow, issue tracking, step]
---

import Screenshot from '@site/src/components/Screenshot';

# Jira Comment

Jira is a software development tool used for issue tracking, project management, and agile software development. It allows users to plan, track, and release software projects. Jira's core functionality includes the ability to create and assign tasks, track progress and status, and collaborate with team members.

By adding Appcircle's [**Jira Comment**](https://github.com/appcircleio/appcircle-jira-component/) component to your workflow, you can add comments or change their status according to your workflow.

<Screenshot url='https://cdn.appcircle.io/docs/assets/jira-component1.png' />

## Prerequisites

There is no mandatory sequence for the use of this component. It depends on your business decision which step to use before or after in your workflow.

:::caution

Please note that once the **Jira Comment** has run successfully, the status of the relevant article in your Jira account will be changed. If the build fails in Appcircle, an incorrect status may appear in your Jira account. Make sure you use it in the correct order in Workflow.

:::

:::danger

To ensure that the **Jira Comment** step runs even if your Workflow fails, please enable the `Always run this step even if the previous steps fail` switch.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3199-jiraPrerequisites.png' />

:::

## Configuration of Component

To add a comment, the issue ID must be supplied to the component. We need to get this issue ID dynamically so that our workflow can work for multiple branches. Appcircle components use environment variables to pass the state. We can add a step just before the **Jira Comment** to prepare the necessary environment variables.

For example, you're working on a feature branch called `feature/jiraissue-1`. You may use the below Ruby script to get `jiraissue-1` from the branch name and use this information with the **Jira Comment**. Please see the [**Custom Script step documentation**](/workflows/common-workflow-steps/custom-script) for this implementation.

```ruby
branch = ENV['AC_GIT_BRANCH']
feature_name = branch.split('/')[1].upcase
puts feature_name

# Write Environment Variable
open(ENV['AC_ENV_FILE_PATH'], 'a') { |f|
    f.puts "AC_JIRA_ISSUE=#{feature_name}"
}
```

### Jira REST API Version Reference

Jira comment input types depending on the Jira REST API version. Therefore, you can select the appropriate Jira REST API version from the component version selection list. Here's how:

- For [Jira REST API version 2](https://developer.atlassian.com/cloud/jira/platform/rest/v2/intro/#version): Choose `2.*.*` from the selection list.
- For [Jira REST API version 3](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#version): Choose `3.*.*` from the selection list.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3199-jiraAPIVersion.png' />

## Input Variables

There are some necessary parameters for this stepper to work properly. These parameters are given in the table below with their explanations.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3199-jiraInput.png' />

:::warning

**Do not hard-code sensitive variables, such as tokens and API keys, directly to the parameters in the step.**

We recommend using [Environment Variables](/environment-variables/) groups for such sensitive variables.

:::

| Variable Name                 | Description                                                                                                                                                                           | Status   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `$AC_JIRA_HOST`               | Your Jira subdomain. For example: `mysubdomain.atlassian.net`                                                                                                                         | Required |
| `$AC_JIRA_EMAIL`              | Email of Jira user. This field is required for those using API tokens instead of PAT. Please use [**Environment Variables**](/environment-variables/).        | Optional |
| `$AC_JIRA_TOKEN`              | User's API token. Please use [**Environment Variables**](/environment-variables/). You can create your token from [here](https://id.atlassian.com/manage-profile/security/api-tokens). | Optional |
| `$AC_JIRA_PAT`              | Specify the Personal Access Token (PAT) for Jira authentication. If you have filled in this field for authentication, you do not need to fill in the `AC_JIRA_TOKEN` field. | Optional |
| `$AC_JIRA_REST_API_VERSION`  | Specify the REST API version of Jira. Cloud Jira users generally use the latest version (currently `3`) of the API, but Jira enterprise users can use different API versions. Additional details can be found [here](#jira-rest-api-version-reference). | Required |
| `$AC_JIRA_ISSUE`              | The ID or key of the issue. Please check the [documentation](https://docs.appcircle.io/integrations/jira-integration) to learn how you can get this information from branch names or commit messages. | Required |
| `$AC_JIRA_FAIL_TRANSITION`    | Transition ID or name for the failed step. If the previous state succeeds, you can optionally change the status of your issue.                                                        | Optional |
| `$AC_JIRA_SUCCESS_TRANSITION` | Transition ID or name for the successful step. If the previous state succeeds, you can optionally change the status of your issue.                                                    | Optional |
| `$AC_JIRA_TEMPLATE`           | This comment template will be used to post a comment. Variables donated with `$` will be replaced during the build.                                                                   | Required |

## Changing Template

Appcircle provides a default template that adds commit id, branch name, time in UTC, and a couple of environment variables. However, this template can be edited and modified according to the Atlassian Document Format (ADF). You can use [ADF Builder](https://developer.atlassian.com/cloud/jira/platform/apis/document/playground/) to create your custom comments.

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-jira-component
