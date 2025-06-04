---
title: Snyk Scan Security
description: The Snyk Security Scan step enables developers to seamlessly incorporate vulnerability scanning into their CI/CD workflows.
tags: [snyk scan, security, mobile]
---

import Screenshot from '@site/src/components/Screenshot';

# Snyk Scan Security

[Snyk Security Scan](https://snyk.io/learn/vulnerability-scanner/) is a powerful tool designed to identify and resolve vulnerabilities within your project's dependencies. Leveraging Snyk's extensive vulnerability database, this tool thoroughly analyzes libraries and frameworks used in your project, offering actionable insights to mitigate potential risks.

The **Snyk Security Scan** step integrates directly into Appcircle’s CI/CD workflows, allowing developers to automatically scan project dependencies for vulnerabilities with each build.

### Prerequisites

Before running the **Snyk Scan Security** step, you must complete certain prerequisites, as detailed in the table below:

| Prerequisite Workflow Step | Description                                                                                   |
| -------------------------- | --------------------------------------------------------------------------------------------- |
| [**Git Clone**](/workflows/common-workflow-steps/#git-clone) | Fetches the repository to be built from the specified branch, ensuring that the [Snyk CLI](https://docs.snyk.io/snyk-cli) can run on the repository path. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/common-workflow-components-snyk-scan-cloud-upload_1.png'/>

### Input Variables

This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/common-workflow-components-snyk-scan-cloud-upload_2.png'/>

:::danger Sensitive Variables

Please do not use sensitive variables such as **Username**, **Password**, **API Key**, or **Personal Access Key** directly within the step.

We recommend using [**Environment Variables**](/build/build-environment-variables) groups for such sensitive variables.

:::

| Variable Name                 | Description                                                                                               | Status    |
|-------------------------------|-----------------------------------------------------------------------------------------------------------|-----------|
| `$AC_REPOSITORY_DIR`          | Specifies the directory where the repository is cloned.                                                   | Required  |
| `$AC_SNYK_ORGANIZATION`       | The name of the [Snyk organization](https://docs.snyk.io/snyk-admin/groups-and-organizations/organizations) under which this project should be tested and monitored.                | Required  |
| `$AC_SNYK_AUTH_TOKEN`         | Your [Snyk authentication token](https://docs.snyk.io/snyk-api/authentication-for-api).                                                                           | Required  |
| `$AC_SYK_CLI_COMMAND`         | The [Snyk CLI command](https://docs.snyk.io/snyk-cli/cli-commands-and-options-summary) to execute. The default value is `test`.                                             | Optional  |
| `$AC_SNYK_SEVERITY_THRESHOLD` | Specifies the minimum [severity level of vulnerabilities](https://docs.snyk.io/manage-risk/prioritize-your-issues/severity-levels) to report. Options: `low`, `medium`, `high`.      | Optional  |
| `$AC_SNYK_FAIL_ON_ISSUES`     | Specifies whether the build should fail based on the Snyk test results. Options: `yes`, `no`.             | Optional  |
| `$AC_SNYK_CREATE_REPORT`      | Specifies whether to generate an [HTML report](https://docs.snyk.io/manage-risk/reporting/getting-started-with-snyk-reports). Options: `yes`, `no`.                                       | Optional  |
| `$AC_SNYK_MONITOR`            | If enabled, imports the snapshot of dependencies to [Snyk for continuous monitoring](https://docs.snyk.io/snyk-cli/commands/monitor). Options: `yes`, `no`. | Optional  |
| `$AC_SNYK_ADD_ARG`            | Additional arguments for the Snyk CLI command.                                                             | Optional  |                                                         | Optional  |


### Output Variables

The output(s) resulting from the operation of this component are as follows:

| Output Variable                | Description                                                                                                              |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| `AC_SNYK_REPORT`              | The [Snyk report](https://docs.snyk.io/manage-risk/reporting/) file containing the results of executed tests.            |
| `AC_SNYK_MONITOR_EXPLORE_LINK`| The [link to explore and monitor](https://docs.snyk.io/snyk-cli/commands/monitor) the project's security status on Snyk. |

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-snyk-scan-secure-component
