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

To ensure that the **Jira Comment** step runs even if your workflow fails, please enable the `Always run this step even if the previous steps fail` switch.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3199-jiraPrerequisites.png' />

:::

## Configuration of Jira Comment

To add a comment, the issue ID must be supplied to the component. We need to get this issue ID dynamically so that our workflow can work for multiple branches. Appcircle components use environment variables to pass the state. We can add a step just before the **Jira Comment** to prepare the necessary environment variables.

For example, you're working on a feature branch called `feature/jiraissue-1`. You may use the below Ruby script to get `jiraissue-1` from the branch name and use this information with the **Jira Comment**. Please see the [**Custom Script documentation**](/workflows/common-workflow-steps/custom-script) for this implementation.

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

**Jira Comment** input types depend on the [Jira REST API version](https://developer.atlassian.com/server/jira/platform/rest-apis/#uri-structure). Therefore, you can select the appropriate Jira REST API version from the component version selection list. Here's how:

- For [Jira REST API version 2](https://developer.atlassian.com/cloud/jira/platform/rest/v2/intro/#version): This version can be used by both Jira On-Prem and Jira Cloud users. Choose `2.*.*` from the selection list.
- For [Jira REST API version 3](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#version): This version can only be used by Jira Cloud users. Choose `3.*.*` from the selection list.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3199-jiraAPIVersion.png' />

### Changing Template

Appcircle provides a default template that adds commit id, branch name, time in UTC, and a couple of environment variables. The structure of the Jira comment template depends on the version of the Jira REST API you're utilizing.

If you're utilizing [API version 2](https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-issue-comments/#api-rest-api-2-issue-issueidorkey-comment-post), commenting is limited to string type only. On the other hand, for [Jira API version 3](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-comments/#api-rest-api-3-issue-issueidorkey-comment-post), you have the flexibility to send comments in any format using the Atlassian Document Format (ADF). To create custom comments for version 3, you can leverage tools like the [ADF Builder](https://developer.atlassian.com/cloud/jira/platform/apis/document/playground/).

## Input Variables

There are some necessary parameters for this stepper to work properly. These parameters are given in the table below with their descriptions.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3199-jiraInput.png' />

:::danger

Confidential information should be entered as a [secret environment variable](/environment-variables/managing-variables#adding-key-and-text-based-value-pairs). Also, ensure that the [environment variable group](/environment-variables/managing-variables#using-environment-variable-groups-in-builds) is selected in the [configuration](/build/build-process-management/build-profile-configuration/).

:::

:::info

The required inputs for authorization vary based on the type of Jira instance (On-Prem or Cloud). Below is a summary of the required inputs:

**For [Jira On-Prem](https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html) Users:**
- `AC_JIRA_EMAIL`: Not required
- `AC_JIRA_TOKEN`: Not required
- `AC_JIRA_PAT`: Required

**For [Jira Cloud](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/) Users:**
- `AC_JIRA_EMAIL`: Required
- `AC_JIRA_TOKEN`: Required
- `AC_JIRA_PAT`: Not required

:::

| Variable Name                 | Description                                                                                                                                                                           | Status   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `$AC_JIRA_HOST`               | Your Jira subdomain. For example: `mysubdomain.atlassian.net`                                                                                                                         | Required |
| `$AC_JIRA_EMAIL`              | The email associated with your Jira account. This field is required for using API tokens instead of PAT.         | Optional |
| `$AC_JIRA_TOKEN`              | User's API Token. If this value is fill, the Jira e-mail field must be filled. Only Jira Cloud users can use API Token. You can create token from [here](https://id.atlassian.com/manage-profile/security/api-tokens) | Optional |
| `$AC_JIRA_PAT`              | Specify the Personal Access Token for Jira authentication. Only Jira On-Prem users can use PAT.  | Optional |
| `$AC_JIRA_ISSUE`              | The ID or key of the issue. Refer to the [documentation](https://docs.appcircle.io/integrations/jira-integration) for instructions on extracting this information from branch names or commit messages. | Required |
| `$AC_JIRA_FAIL_TRANSITION`    | Transition ID or name for the failed step. Optionally change the status of your issue if the previous state fails. Ensure that the `Always run this step even if the previous steps fail` switch is enabled for this feature to work.  | Optional |
| `$AC_JIRA_SUCCESS_TRANSITION` | Transition ID or name for the successful step. Optionally change the status of your issue if the previous state succeeds.                                                    | Optional |
| `$AC_JIRA_TEMPLATE_V2`           | The comment template used to post a comment if [Jira REST API Version 2](#jira-rest-api-version-reference) is selected. Variables prefixed with `$` will be replaced during the build process. Refer to [this header](#changing-template) to modify the template. | Required |
| `$AC_JIRA_TEMPLATE_V3`           | The comment template used to post a comment if [Jira REST API Version 3](#jira-rest-api-version-reference) is selected. Variables prefixed with `$` will be replaced during the build process. Refer to [this header](#changing-template) to modify the template. | Required |

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-jira-component
