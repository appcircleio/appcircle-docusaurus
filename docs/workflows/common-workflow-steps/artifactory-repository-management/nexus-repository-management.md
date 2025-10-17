---
title: Sonatype Nexus Integration
description: Enhance your development process with Cache Pull to quickly retrieve and reuse stored data, boosting efficiency and performance.
tags: [cache pull, efficiency, dependencies, cache structure]
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';
import NexusHttpsProtocol from '@site/docs/\_nexus-https-protocol.mdx';

# Sonatype Nexus Integration

Integrating Sonatype Nexus into your CI/CD pipeline enables secure, efficient, and automated management of dependencies, artifacts, and container images. By connecting Appcircle with Nexus Repository Manager, teams can centralize artifact storage, enforce security policies, and ensure consistent version control across builds. This integration not only streamlines dependency resolution but also enhances supply chain security through vulnerability scanning and license compliance checks — ultimately improving build reliability and traceability throughout the release process.

### Nexus Integration for iOS

Integrating an Artifactory repository manager into your iOS build process is a robust approach to centralizing dependency management, improving build reliability, and ensuring reproducibility. Below, we’ll demonstrate this process using **Sonatype Nexus Repository Manager** as an example in conjunction with the Appcircle **CocoaPods Install** workflow step. Please ensure your Sonatype Nexus Repository Manager is properly installed and configured. For more information, please visit the [official Sonatype Nexus documentation](https://help.sonatype.com/repomanager3).

:::info Supported Frameworks

Sonatype Sonatype Nexus only supports **CocoaPods** for iOS. There is no support for [**Carthage**](https://github.com/Carthage/Carthage) and [**SPM (Swfit Package Manager)**](https://www.swift.org/documentation/package-manager/).

For more information about supported frameworks, please visit [**Sonatype Sonatype Nexus Repository documentation**](https://help.sonatype.com/en/formats.html).

Please visit to [**Local Repository Integration**](/workflows/common-workflow-steps/artifactory-repository-management/local-repository-integration) documentation to see alternative solution for **SPM (Swfit Package Manager)**.

:::

:::tip Artifactory Management for SPM

Since Sonatype Nexus does not yet support **SPM**, it is **not** possible to manage SPM packages using Nexus.
For users with a Nexus infrastructure, an alternative approach to centralize and fetch SPM packages is to collect all SPM packages in a private Git repository. This way, all SPM packages are pulled only from a repository accessible to the user and included in the build process.

**Note**: With this method, the **SPM** packages collected in a single repository must be regularly checked and updated to ensure they remain up to date.

:::

:::caution Configure Sonatype Nexus Repository Authentication

If [anonymous access option](https://help.sonatype.com/en/anonymous-access.html) is turned off in Sonatype Nexus repository, you need to authenticate to the repository with the [**Authenticate with Netrc**](/workflows/common-workflow-steps/authenticate-with-netrc) step or by using a [**Custom Script**](/workflows/common-workflow-steps/custom-script). If Custom Script is used, you can use the bash script given below.

For more information, please visit the [**Sonatype Nexus Authentication documentations**](https://help.sonatype.com/en/cocoapods-repositories.html#configure-nexus-repository-authentication).

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

For detailed server-side configuration steps, you can refer to [Appcircle’s Sonatype Nexus configuration guide](/self-hosted-appcircle/install-server/linux-package/configure-server/external-image-registry#sonatype-nexus-configuration).


<NexusHttpsProtocol />

:::info SSL Configuration

If you are using a self-signed SSL certificate, ensure that curl can work with it properly. Since the CocoaPods client uses the curl command to download Pod files from Nexus Repository, you can configure curl by adding the `--insecure` option to the .curlrc file in your home directory. If the file does not exist, simply create it. Example:

```bash
$cat ~/.curlrc
--insecure
```

For detailed information, please visit the [**Sonatype Nexus SSL Configuration documentations**](https://help.sonatype.com/en/cocoapods-repositories.html#configure-ssl).

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

### Nexus Integration for Android

Integrating an Artifactory repository manager into your Android build process is a robust approach to centralizing dependency management, improving build reliability, and ensuring reproducibility. Below, we’ll demonstrate this process using [**Nexus Repository Manager**](https://www.sonatype.com/products/sonatype-nexus-repository) as an example in conjunction with the Appcircle **Android Build** workflow step.

For detailed instructions on integrating Nexus Repository Manager with Appcircle, see our [Sonatype Nexus Configuration guide](/self-hosted-appcircle/install-server/linux-package/configure-server/external-image-registry#sonatype-nexus-configuration).


#### 1. Set up Nexus repository

- Ensure your Nexus Repository Manager is properly installed and configured. For hosted installations, follow the [official Nexus documentation](https://help.sonatype.com/repomanager3) to set up your Maven or Gradle repositories.  
- Create a hosted Maven repository (or any repository format compatible with your project). Name the repository, for example, `android-repo`.

#### 2. Integrate Nexus into the Android project

In your Android project’s build.gradle (or settings.gradle if using Gradle Version Catalog), configure Nexus as a repository.

<NexusHttpsProtocol />

To fetch dependencies from a Nexus repository, add the following configuration to your Gradle file.
You can place this block in either the project-level or module-level `build.gradle` file, depending on your project structure.

If all modules in your project will use the same artifacts, it is recommended to place it in the project-level file:

```gradle
repositories {
    maven {
        url 'https://your-nexus-url/repository/android-repo/'
    }
}
```

If the URL requires authentication for access, you can configure it as shown below:

```gradle
repositories {
    maven {
        url 'https://your-nexus-url/repository/android-repo/'
        credentials {
            username = "your-username"
            password = "your-password"
        }
    }
}
```

To update your Gradle distribution URL with a Nexus repository, modify your `gradle-wrapper.properties` file and replace the `distributionUrl` value with the Nexus repository URL. Below is an example:  

```gradle
distributionUrl=https://your-nexus-url/repository/gradle-distributions/gradle-8.8-bin.zip
```

#### 3. Run the build workflow

Trigger your build through Appcircle. The workflow will fetch dependencies from the Nexus repository as configured and compile the project with them. Logs will show dependency resolution status to confirm successful integration with Nexus.