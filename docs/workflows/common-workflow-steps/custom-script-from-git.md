---
title: Custom Script from Git
description: Use Custom Script from Git to run your own scripts during the build. Easily add custom steps by cloning scripts from any Git repository, with support for authentication.
tags: [custom script, custom scripts, data protection, build, git, git scripts, reuse]
---

import Screenshot from '@site/src/components/Screenshot';
import SensitiveVariablesDanger from '@site/docs/\_sensitive-variables-danger.mdx';

# Custom Script from Git

You can use **Custom Script from Git** to clone and run your own scripts directly from a Git repository as part of your Appcircle build. This step supports authenticated cloning (via username and PAT).

Before execution, the step will clone (or reuse) your repository, check out the specified branch, and execute the script based on its file extension (postfix).

If the `AC_SCRIPT_FILENAME` value includes a relative path (for example, `folder/test.sh`), the script will be located and executed from that path within the repository structure.

:::info

The step inspects your script file’s postfix (its extension—`.sh`, `.py`, `.rb`, `.pl`, `.js`, `.java`) to choose the execution path. It must match exactly.
Supported script types and their execution commands:

- `example-script.sh` → bash
- `example_script.rb` → ruby
- `example_script.py` → python
- `example-script.pl` → perl
- `example-script.js` → nodejs
- `ExampleScript.java` → java

:::

:::danger 

When executing a `Java` file, the `script filename` and the `class name` within the script must match.

```ruby 
javac ExampleScript.java
java ExampleScript 
```
:::

:::caution

If you are seeing the following error in the build log, please ensure that both the `username` and the `personal access token` (PAT) are set correctly. This error is returned by the Git provider when authentication fails due to an `incorrect or missing username or PAT`:

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

<SensitiveVariablesDanger />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6419-csfromgitinput.png' />


| Variable Name                  | Description                                                                                                                                                                                            | Status   |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| `$AC_SCRIPT_FILENAME`          | Specifies the exact name of the script file to execute within the Git repository (e.g., test.sh, code.rb or relative_path/python.py).                                                                  | Required |
| `$AC_SCRIPT_EXTRA_PARAMETERS`  | Additional parameters to pass to the script (comma "," separated; if a parameter has an empty character, define it with " "; e.g. param1,param2,"param3 with spaces",param4).                          | Optional |
| `$AC_SCRIPT_REPO_DIR`          | If the Git repository has already been cloned in a previous step of the same workflow, set the Repository Directory Output here. This input is required if `AC_SCRIPT_REPO_CLONE_URL` is not provided. | Optional |
| `$AC_SCRIPT_REPO_CLONE_URL`    | Git repository clone URL. Required if the Repository Directory Output is not provided. (e.g. exampleGit.exampleRepo.git). This input is required if `AC_SCRIPT_REPO_DIR` is not provided.      | Optional |
| `$AC_SCRIPT_GIT_USERNAME`      | Git provider username for authentication. This is required if the AC_SCRIPT_REPO_DIR input is not provided and the Git repository is private.                                                          | Optional |
| `$AC_SCRIPT_GIT_PAT`           | Git provider personal access token for authentication. This is required if the AC_SCRIPT_REPO_DIR input is not provided and the Git repository is private.                                             | Optional |
| `$AC_SCRIPT_GIT_BRANCH`        | Name of the branch to check out from the script repository. If not specified, the repository's default branch will be used.                                                                            | Optional |

### Output Variables

The output(s) resulting from the operation of this component are as follows:

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6419-csfromgitoutput.png'/>

| Variable Name                 | Description                                                                                                                              |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------| 
| `AC_SCRIPT_REPO_OUTPUT_DIR`   | The directory path where the custom script repository is located on the runner. This output can be reused in subsequent workflow steps.  |

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-custom-script-from-git-component

---
