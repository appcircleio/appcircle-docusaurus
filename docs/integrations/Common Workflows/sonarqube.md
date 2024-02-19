---
title: SonarQube
metaTitle: SonarQube
metaDescription: SonarQube
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';

# SonarQube

This step allows you to analyze your code quality with the SonarQube CLI. Whichever workflow you are doing your code analysis after, please run the SonarQube step after that step is completed.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2583-sonarOrder.png' />

### Input Variables

- You can change the SonarQube CLI version as you wish with the version parameter. Default will be latest.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2583-sonarVersion.png' />

- With the Scanner Parameters input, you can start your code quality analysis by entering the required SonarQube information.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2583-sonarParam.png' />

:::caution
Please note that SonarQube is a commercial code quality analysis tool. The parameters required for the scanner to work should be used as **Enviroment Variables** as they may create security vulnerabilities. You can obtain these parameters by contacting your DevOps team.
:::

- You can use this input variable to add an extra parameter to the CLI Tool.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2583-sonarExtra.png' />

# Including Tests

You can also include your Unit/UI test results in the SonarQube analysis.

:::caution
If you want to include your test results in the SonarQube analysis, always run the SonarQube step after test step.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2583-sonarTestOrder.png' />

:::warning
SonarQube accepts `.xml` format files to analyze test results. In order to analyze your test results, do not forget to convert your test results to `.xml` format by running the **Convert Xcresult to HTML/XML** step after the **Xcodebuild for Unit and UI testing** step.
:::

