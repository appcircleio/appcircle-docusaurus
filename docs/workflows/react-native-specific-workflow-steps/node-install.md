---
title: Install Node
description: Ensure the correct Node version for your React Native app with Install Node. A crucial step for building React Native applications.
tags: [react native, mobile, workflow, step]
---

import Screenshot from '@site/src/components/Screenshot';

# Install Node

React Native applications commonly depend on certain Node modules. This workflow step makes sure that you have the required Node version installed in the build agent to build your React Native application.

### Prerequisites

Before running the **Install Node** step, you must complete certain prerequisites, as detailed in the table below:

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [**Git Clone**](/workflows/common-workflow-steps/git-clone) | Clone the selected repository to the build machine. Please use the **Install Node** step after this step. |

:::caution

Please note that this step should be used before steps that need the **npm/yarn Commands** step. To avoid any problems, you can run this step after the **Git Clone** step.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2796-nodeOrder.png' />

### Input Variables

This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2796-nodeDetails.png' />

| Variable Name                 | Description                                    | Status |
|-------------------------------|------------------------------------------------|--------|
| `$AC_SELECTED_NODE_VERSION`   | This step takes only the **node version** variable. You can specify the version directly in the step if you wish. Or you can get it from build [**Configurations**](/build/platform-build-guides/building-react-native-applications#build-configuration-for-react-native-ios-applications). | Optional |

:::caution

If you do not specify any specific version for the **Install Node** step. The latest version will be installed automatically.

:::

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-node-install-component