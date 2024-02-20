---
title: Git Clone
metaTitle: Git Clone
metaDescription: Git Clone
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';

# Git Clone

Appcircle Build Profiles require the corresponding project for users to run build operations. This step clones the repository of the related project on the currently running Runner VM.

:::info
We recommend using this step at the beginning of the workflow to avoid any problems in the workflow.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2794-gitOrder.png' />

### Input Variables

- Some necessary parameters for this step to work are listed below with explanations.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2794-gitDetails.png' />

:::warning
Variables that come with Default Steps are usually taken from **Reserved Environment Variables**. Make sure that the variable you provide has a **value**, in case you want to make a possible change. **Required variables cannot be left blank**.
:::

| Variable Name                 | Description                                    | Required |
|-------------------------------|------------------------------------------------|----------|
| `$AC_GIT_URL`                 | Url of the repository. | ✅ |
| `$AC_GIT_COMMIT`              | Commit of the repository | ➖ |
| `$AC_GIT_BRANCH`              | Branch of the repository | ➖ |
| `$AC_GIT_TAG`                 | Tag of the repository | ➖ |
| `$AC_GIT_LFS`                 | Used to specify whether large files will be downloaded. | ➖ |
| `$AC_GIT_SUBMODULE`           | Used to specify whether the submodule should be cloned. | ➖ |
| `$AC_GIT_CACHE_CREDENTIALS`   | If this set to true, the credentials will be cached. This can be useful if the same credentials are used for multiple repositories. | ➖ |
| `$AC_GIT_EXTRA_PARAMS`        | If this set, sends extra parameter for git requests. | ➖ |
