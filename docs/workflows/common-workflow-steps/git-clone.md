---
title: Git Clone
description: The Git Clone step is used to fetch the source code repository from a Git provider and clone it into the runner where the build and deployment processes take place.
tags: [git, clone, workflow, step]
---

import Screenshot from '@site/src/components/Screenshot';

# Git Clone

The **Git Clone** step is used to fetch the source code repository from a Git provider, such as [**GitHub**](https://docs.appcircle.io/build/adding-a-build-profile/connecting-to-github), [**GitLab**](https://docs.appcircle.io/build/adding-a-build-profile/connecting-to-gitlab), [**Bitbucket**](https://docs.appcircle.io/build/adding-a-build-profile/connecting-to-bitbucket), or [**Azure DevOps**](https://docs.appcircle.io/build/adding-a-build-profile/connecting-to-azure), and clone it into the runner where the build and deployment processes take place. This step ensures that the latest version of the codebase is available for subsequent build and deployment steps.

### Prerequisites

Below is a list of workflow steps that must be completed before executing the **Git Clone** workflow step, along with their respective descriptions:

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [**Activate SSH Private Key**](https://docs.appcircle.io/workflows/common-workflow-steps/#activate-ssh-key) | This step sets up your SSH key on the build machine **if you used one to connect your repository with SSH**. |

:::caution
If you have not connected your repo via SSH, the **Git Clone** does not have any dependency on the **Activate SSH Private Key** step.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2794-gitOrder.png' />

:::info
We recommend using this step at the beginning of the workflow to avoid any problems in the workflow.
:::

### Input Variables

You can find all the parameters required for this step in the table below, with their descriptions in detail.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2794-gitDetails.png' />

:::danger
After connecting the repository, the following [**Reserved Environment Variables**](https://docs.appcircle.io/environment-variables/appcircle-specific-environment-variables), which **Git Clone** uses as input, will be automatically populated. Ensure that the variable you provide has a value if you intend to make any changes. **The required variables must not be left empty**.
:::

| Variable Name                 | Description                                    | Status           | 
|-------------------------------|------------------------------------------------|------------------|
| `$AC_GIT_URL`                 | URL of the repository. After the [**provider connection**](https://docs.appcircle.io/build/adding-a-build-profile/) is completed with the Git provider, these values will be set automatically. | Required |
| `$AC_GIT_COMMIT`              | Commit of the repository. This value will come from the Git provider. When a new commit is pushed, Appcircle fetches the details of the latest commit. | Optional |
| `$AC_GIT_BRANCH`              | Branch of the repository. You can find more details about [**branch management**](https://docs.appcircle.io/build/build-profile-branch-operations). The branch information selected before starting manual build on the interface is automatically included here.  | Optional |
| `$AC_GIT_TAG`                 | Tag of the repository. If you have tags in your repository, Appcircle can start a build according to the tags. | Optional |
| `$AC_GIT_LFS`                 | Used to specify whether large files will be downloaded. The default value is `false`. | Optional |
| `$AC_GIT_SUBMODULE`           | Used to specify whether the submodule should be cloned. | Optional |
| `$AC_GIT_CACHE_CREDENTIALS`   | If this variable is set to `true`, the credentials will be cached. This can be useful if the same credentials are used for multiple repositories. The default value is `true`. | Optional |
| `$AC_GIT_EXTRA_PARAMS`        | If this variable is set, it sends additional parameters for Git requests. | Optional |

### Output Variables

| Variable Name                 | Description                                    |
|-------------------------------|------------------------------------------------|
| `$AC_REPOSITORY_DIR`          | Specifies the root directory of the cloned repository. This path is automatically generated after the repository is cloned. |

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-git-clone-component