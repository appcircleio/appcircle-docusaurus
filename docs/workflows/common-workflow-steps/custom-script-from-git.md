---
title: Custom Script from Git
description: Use Script steps for additional functionalities in your builds.
tags: [custom scripts, build, test, workflow, step]
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import Screenshot from '@site/src/components/Screenshot';
import SensitiveVariablesDanger from '@site/docs/\_sensitive-variables-danger.mdx';

# Custom Script from Git

You can use **Custom Script from Git** to clone and run your own scripts directly from a Git repository as part of your Appcircle build. This step supports authenticated cloning (via username and PAT).

Before execution, the step will clone (or reuse) your repository, check out the specified branch, and execute the script based on its file extension (postfix).

:::caution

Keep in mind that the script file has to be under the repository root folder in order to work with the component.

:::

:::info

The step inspects your script file’s postfix (its extension—.sh, .py, .rb, .pl, .js, .java) to choose the execution path. It must match exactly.
Supported script types and their execution commands:

- example-script.sh → bash
- example-script.rb → ruby
- example-script.py → python
- example-script.pl → perl
- example-script.js → nodejs
- example-script.java →
```ruby 
# Script-filename and Class-name within the script must match.
javac example-script.java
java example-script 
```

:::

:::caution

If you are seeing the following error in the build log, please ensure that both the username and the personal access token (PAT) are set correctly. This error is returned by the Git provider when authentication fails due to an incorrect or missing username or PAT:

```bash

fatal: could not read Username for Git provider

```

:::

### Prerequisites

There are no prerequisites required before using the **Custom Script from Git** step.

:::tip

Note that you can put the **Custom Script from Git** component anywhere you want in the workflow. This step is used to add different capabilities to the existing workflow. As well as the [**Custom Script**](/workflows/common-workflow-steps/custom-script).

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6419-csfromgit.png' />

### Input Variables

This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6419-csfromgitinput.png' />

<SensitiveVariablesDanger />

| Variable Name                  | Description                                                                                                                                                                                       | Status   |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| `$AC_SCRIPT_FILENAME`          | Specifies the exact name of the script file to execute within the Git repository (e.g., test.sh, code.rb, python.py).                                                                             | Required |
| `$AC_SCRIPT_EXTRA_PARAMETERS`  | Additional parameters to pass to the relevant script file. Separate multiple parameters with a comma \" , \". If a parameter contains spaces, enclose it in \" \".                                | Optional |
| `$AC_SCRIPT_REPO_DIR`          | If the Git repository has already been cloned in a previous workflow step, set Repository Directory Output here. **Required** if Clone URL, Username, and Personal Access Token are not provided. | Optional |
| `$AC_SCRIPT_REPO_CLONE_URL`    | Git repository clone URL (https). **Required** if the Repository Directory Output is not provided.                                                                                                | Optional |
| `$AC_SCRIPT_GIT_USERNAME`      | Git provider username for authentication. **Required** if the Repository Directory Output is not provided. **Public repository** doesnt require Username.                                         | Optional |
| `$AC_SCRIPT_GIT_PAT`           | Git provider personal access token for authentication. **Required** if the Repository Directory Output is not provided. **Public repository** doesnt require PAT.                                 | Optional |
| `$AC_SCRIPT_GIT_BRANCH`        | Name of the branch to checkout from the script repository. Default branch is **main**.                                                                                                            | Optional |

### Output Variables

The output(s) resulting from the operation of this component are as follows:

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6419-csfromgitoutput.png'/>

| Variable Name                 | Description                                                                                                         |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------| 
| `AC_SCRIPT_REPO_OUTPUT_DIR`   | **Repository Directory Output** of the custom script repository on the build machine for reuse in subsequent steps. |

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-custom-script-from-git-component

---
