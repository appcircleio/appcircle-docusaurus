---
title: Carthage
description: Appcircle supports Carthage for dependency management in iOS projects.
tags: [carthage, ios, management, workflow, step]
---

import Screenshot from '@site/src/components/Screenshot';

# Carthage

[Carthage](https://github.com/Carthage/Carthage) is a dependency manager for Swift and Objective-C applications. [Carthage](https://github.com/Carthage/Carthage) handles the installation of external libraries your application depends on during a build.

[Carthage](https://github.com/Carthage/Carthage) is widely used among iOS developers for dependency management, and it's very easy to include it in your iOS projects with Appcircle.

### Prerequisites

Before running the **Carthage** step, you must complete certain prerequisites, as detailed in the table below:


| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [**Git Clone**](https://docs.appcircle.io/workflows/common-workflow-steps#git-clone) | This step clones your git repo on the runner where the build process will take place so that the necessary workflow operations can be performed. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2828-cartOrder.png' />

:::caution

Appcircle will look for a [`Cartfile`](https://github.com/Carthage/Carthage/blob/master/Documentation/Artifacts.md) file in your repository and use it to install the dependencies. For this reason, **it should be used after the Git Clone step**.

:::

### Input Variables

The output(s) resulting from the operation of this component are as follows:

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2828-cartInput.png' />

| Variable Name                 | Description                                    | Status 			|
|-------------------------------|------------------------------------------------|------------------|
| `$AC_CARTHAGE_COMMAND`        | Specifies the Carthage command to run. Defaults to `bootstrap`. **Possible values:** `bootstrap`, `update` | Required |
| `$AC_REPOSITORY_DIR`          | Specifies the cloned repository directory. This path will be generated after [Git Clone](https://docs.appcircle.io/workflows/common-workflow-steps#git-clone).| Optional |
| `$AC_CARTFILE_PATH`           | Specifies the path where the Cartfile resides. Defaults to the repository directory. **DO NOT** include Cartfile, this is only the path. **This value will be appended** to `$AC_REPOSITORY_DIR`. **Example:** `./` or `./subpath-to-cartfile/` | Optional |
| `$AC_CARTHAGE_FLAGS`          | Specifies additional flags after the Carthage command. The default value is empty. **For Xcode 12 and above, make sure to include** `--use-xcframeworks` **here**. To shorten the build time, make sure to specify the platform: `--platform iOS`. Example usage: `--platform iOS --use-xcframeworks` | Optional |

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-carthage-component