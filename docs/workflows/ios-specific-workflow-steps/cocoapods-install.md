---
title: Cocoapods Install
description: Master Cocoapods Install for managing dependencies in your project. Learn how to use the 'pod install' command effectively.
tags: [cocoapods, install, workflow, step]
---

import Screenshot from '@site/src/components/Screenshot';

# Cocoapods Install

Runs the [CocoaPods](https://cocoapods.org) install command for dependency management. This step installs all pod dependencies. Appcircle uses the `pod install` command to install pods in the project. This command comes from the CocoaPods tool installed on the system. If a version is not specified for CocoaPods, this step will use the version of [**CocoaPods installed**](/infrastructure/ios-build-infrastructure#ios-build-agent-stacks) on the system.

### Prerequisites

Before running the **Cocoapods Install** step, you must complete certain prerequisites, as detailed in the table below:

| Prerequisite Workflow Step                                                        | Description                                                                                                                                                                                              |
| --------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [**Git Clone**](/workflows/common-workflow-steps/git-clone) | The repo needs to be cloned in order to start the CocoaPods installation process. After the clone, CocoaPods will be installed. After this step works, the variable `$AC_REPOSITORY_DIR` will be created. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2588-pod_order.png' />

### Input Variables

This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2588-pod_version.png' />

| Variable Name           | Description                                                                                                                                                                                                                                                     | Status   |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `$AC_PROJECT_PATH`      | Specifies the project path. For example: `./appcircle.xcodeproj`. If you filled in **`Configuration => Project or Workspace`**, this variable comes from [Configuration](/build/build-process-management/build-profile-configuration). | Required |
| `$AC_REPOSITORY_DIR`    | Specifies the cloned repository directory. This path will be generated after the [**Git Clone**](/workflows/common-workflow-steps/git-clone) step.                                                                                         | Required |
| `$AC_COCOAPODS_VERSION` | Specifies the CocoaPods version. If there is a specific version you want to use, give it here as hardcoded, and the system will automatically install the given version.                                                                                        | Optional |

:::info

Please note that the **CocoaPods Install** step uses the default system [**CocoaPods version**](/infrastructure/ios-build-infrastructure#ios-build-agent-stacks). If you want to use a specific version, please enter it hardcoded in the CocoaPods Version parameter in the step.

:::

:::danger

Remember, if the project extension is not **.xcworkpace**, the pod install step will not work as expected. In the Configuration tab, make sure that the extension in the project path is **.xcworkspace**.

:::

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-cocoapods-component

---

## FAQ

### How do I manage iOS dependencies with artifactory repository manager?

Integrating an Artifactory repository manager into your iOS build process is a robust approach to centralizing dependency management, improving build reliability, and ensuring reproducibility. Below, we’ll demonstrate this process using **Sonatype Nexus Repository Manager** as an example in conjunction with the Appcircle **CocoaPods Install** workflow step. Please ensure your Sonatype Nexus Repository Manager is properly installed and configured. For more information, please visit the [official Sonatype Sonatype Nexus documentation](https://help.sonatype.com/repomanager3).

:::info Supported Frameworks

Sonatype Sonatype Nexus only supports **CocoaPods** for iOS. There is no support for [**Carthage**](https://github.com/Carthage/Carthage) and [**SPM (Swfit Package Manager)**](https://www.swift.org/documentation/package-manager/).

For more information about supported frameworks, please visit [**Sonatype Sonatype Nexus Repository documentation**](https://help.sonatype.com/en/sonatype-Sonatype Nexus-repository.html).

:::

:::caution Configure Sonatype Nexus Repository Authentication

If [anonymous access option](https://help.sonatype.com/en/anonymous-access.html) is turned off in Sonatype Nexus repository, you need to authenticate to the repository with the [**Authenticate with Netrc**](/workflows/common-workflow-steps/authenticate-with-netrc) step or by using a [**Custom Script**](/workflows/common-workflow-steps/custom-script). If Custom Script is used, you can use the bash scirpt given below.

For more information, please visit the [**Sonatype Nexus Authentication documentations**](https://help.sonatype.com/en/cocoapods-repositories.html).

```bash
$cat ~/.netrc
machine https://Sonatype Nexus.example.com/repository/cocoapods-specs.git
login admin
password admin123
```

:::

For more information about Sonatype Nexus integration with CocoaPods, please visit the [Sonatype Nexus CocoaPods documentations](https://help.sonatype.com/en/cocoapods-repositories.html).

#### Example 1: How can I fetch the all dependencies from Sonatype Nexus with CocoaPods?

In the **CocoaPods Install** step, in order to pull dependencies from Sonatype Nexus or another artifactory, you need to make some changes in the `Pods` file. For this, the `source url` value of the `Pods` file in the project must be replaced with the relevant artifactory. A short example is shown in the following bash script.

:::danger HTTPS Protocol

When configuring Sonatype Sonatype Nexus, you should pay attention to the `https` protocol. Sonatype Nexus **does not support** **`http`** protocol. Therefore, the source URL must be in `https` protocol.

:::

:::info SSL Configuration

If you are using a Self-Signed https protocol, this certificate must be secure. If the certificate is not secure, some action should be taken. 

For detailed information, please visit the [**Sonatype Nexus SSL Configuration documentations**](https://help.sonatype.com/en/cocoapods-repositories.html).

:::

```bash

platform :ios, '13.0'
source 'https://Sonatype Nexus.example.com/repository/cocoapods-specs.git'
target 'MyApp' do

use_frameworks!
  
  pod 'AFNetworking', '~> 4.0'
  pod 'Alamofire', '~> 5.4'

end

.
.
. #Other Pod file codes

```

#### Example 2: How can I fetch some dependencies from different repositories?

If you want to fetch a dependency from a source other than this artifactory, you can set up your `Pod` file as shown below. This `Pod` file will pull any pods that are explicitly referenced from the specified URL, while all other dependencies will be retrieved directly from the default `source URL`.

```bash

platform :ios, '13.0'
source 'https://Sonatype Nexus.example.com/repository/cocoapods-specs.git'
target 'MyApp' do

use_frameworks!

  pod 'AFNetworking', '~> 4.0'
  pod 'Alamofire', '~> 5.4'
  pod 'MyPrivatePod', :git => 'https://git.mycompany.com/MyPrivatePod.git', :branch => 'main'

end

.
.
. #Other Pod file codes

```

After these changes;

- Trigger your build through Appcircle. The workflow will fetch dependencies from the Sonatype Nexus repository as configured and compile the project with them.
- Logs will show dependency resolution status to confirm successful integration with Sonatype Nexus.