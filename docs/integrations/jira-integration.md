---
title: Jira Integration
metaTitle: Jira Integration
metaDescription: Jira Integration
sidebar_position: 8
---

# Jira Integration

Jira is a software development tool used for issue tracking, project management, and agile software development. It allows users to plan, track, and release software projects. Jira's core functionality includes the ability to create and assign tasks, track progress and status, and collaborate with team members

You can use [Jira Component](https://github.com/appcircleio/appcircle-jira-component/) to add a comment and change the status of your issues according to the status of your workflow. 

![](<https://cdn.appcircle.io/docs/assets/jira-component1.png>)

## Credentials

In order to use Jira Component, you need to configure the component and add the necessary credentials. It is strongly advised to add the credentials of your Jira instance with locked environment variables.

- `AC_JIRA_HOST`: Jira Host. Your Jira subdomain. Example: `mysubdomain.atlassian.net`
- `AC_JIRA_EMAIL`: Jira Email. Email of Jira user. 
- `AC_JIRA_TOKEN`: API Token. User's API Token. You can create your token from [here](https://id.atlassian.com/manage-profile/security/api-tokens)

![](<https://cdn.appcircle.io/docs/assets/jira-component2.png>)

## Configuring Component

To add a comment, the issue id must be supplied to the component. We need to get this issue id dynamically so that our workflow can work for multiple branches. Appcircle components use environment variables to pass the state. We can add a step just before the Jira Component to prepare the necessary environment variables. 

Let's say, you're working on a feature branch called `feature/jiraissue-1`. You may use the below Ruby script to get `jiraissue-1` from the branch name and use this information with the Jira component.

```ruby
branch = ENV['AC_GIT_BRANCH']
feature_name = branch.split('/')[1].upcase
puts feature_name

# Write Environment Variable
open(env_var_path, 'a') { |f|
    f.puts "AC_JIRA_ISSUE=#{feature_name}"
}
```

## Transitioning Issue

If you add a transition id or transition name for successful and failed steps, the Jira component will automatically change the status of your issue. 

## Changing Template

Appcircle provides a default template that adds commit id, branch name, time in UTC, and a couple of environment variables. However, this template can be edited and modified according to  Atlassian Document Format (ADF). You can use [ADF builder](https://developer.atlassian.com/cloud/jira/platform/apis/document/playground/) to create your custom comments.

Please check [Jira Component](https://github.com/appcircleio/appcircle-jira-component/) documentation for more information.