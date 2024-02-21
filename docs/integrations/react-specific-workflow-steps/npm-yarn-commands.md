---
title: npm/yarn Commands
metaTitle: npm/yarn Commands
metaDescription: npm/yarn Commands
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';

# npm/yarn Commands

React Native applications commonly depend on certain Node modules. This workflow step makes sure that you have the required Node version installed in the build agent to build your React Native application.

:::caution
Note that this step must be used after the Node Install step to work correctly
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2797-npmOrder.png' />

### Input Variables

This step contains different variables. It needs these variables to work. The table below gives explanations of these variables.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2797-nmpDetails.png' />

| Variable Name                 | Description                                    | Required |
|-------------------------------|------------------------------------------------|----------|
| `$AC_REPOSITORY_DIR`          | Specifies the cloned repository directory. | ✅ |
| `$AC_NPM_COMMAND_ARGS`        | The npm command to run. defaults to: npm/yarn install | ➖ |


https://github.com/appcircleio/appcircle-npm-yarn-component