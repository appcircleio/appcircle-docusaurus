---
title: Export Build Artifacts
description: Exports the specified build artifacts from the build agent to the Appcircle dashboard.
tags: [export, artifact, build, workflow, step]
---

import Screenshot from '@site/src/components/Screenshot';


# Export Build Artifact

Exports the specified build artifacts from the build agent to the Appcircle dashboard. The exported files will be available for download in the artifacts section of the completed build.

:::danger

Sending applications to **Publish**, **Enterprise App Store**, or **Testing Distribution** will not work without this step.

:::

### Prerequisites

There are no prerequisites required before using the **Export Build Artifact** step.

:::note

We **recommend** using it as the **last** step in your workflow.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2584-exportOrder.png' />

:::danger

Remember, if you set a step to run after this step, artifacts generated after this step **will not be exported**. This step only exports the artifacts produced before it.

:::

### Download Exported Artifacts

You can access and download the exported artifacts by clicking on the three dots (**⋮**) in the Build list and selecting download artifact. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2584-exportDownload.png' />

:::caution

If you use the **Default Workflow** templates, the option "**Always run this step even if the previous steps fail**" is already enabled for the **Export Build Artifacts** step by default. However, **if you want to ensure that the build log and any extracted artifacts are available even if the pipeline fails, you need to turn on this option.**

<Screenshot url='https://cdn.appcircle.io/docs/assets/exportToggle.png' />

:::

### Input Variables

This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2584-exportInput.png' />


| Variable Name                 | Description                                    | Status |
|-------------------------------|------------------------------------------------|--------|
| `$AC_UPLOAD_DIR`              | If a folder path is specified, the files in this folder will be exported as artifacts. If a file path is specified, that file will be exported as an artifact. Uploading files with a 0 byte size in the specified path will be skipped. The default folder path is **`$AC_OUTPUT_DIR`**. | Required |
| `$AC_DISABLE_UPLOAD_ON_FAIL`  | The Delete Artifact for failed build variable is **false** by default. This variable allows you to export artifacts if a build succeeds, so that they do not take up disk space.  | Optional |

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-export-build-artifacts