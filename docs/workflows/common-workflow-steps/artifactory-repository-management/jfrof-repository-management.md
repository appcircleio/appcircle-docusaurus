---
title: JFrog Integration
description: Enhance your development process with Cache Pull to quickly retrieve and reuse stored data, boosting efficiency and performance.
tags: [cache pull, efficiency, dependencies, cache structure]
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';

# JFrog Integration

Integrating JFrog into your CI/CD workflows provides a unified and secure approach to managing build artifacts, dependencies, and release packages. By connecting Appcircle with JFrog Artifactory, development teams can automate artifact storage, versioning, and distribution while maintaining end-to-end traceability. This integration enhances software supply chain security through advanced vulnerability analysis and license compliance, ensuring that every artifact promoted through the pipeline meets organizational quality and security standards.

## JFrog Integration for iOS

Integrating JFrog Artifactory into iOS projects allows seamless management of CocoaPods and Swift Package Manager dependencies within a secure and centralized repository. This setup ensures consistent build environments, faster dependency resolution, and improved control over private libraries — all while maintaining compliance and traceability across your CI/CD workflows.

### Cocoapods Dependencies

CocoaPods dependencies can be seamlessly integrated with JFrog Artifactory to manage private and public iOS libraries efficiently, ensuring secure storage, version control, and faster dependency resolution during the build process.

To fetch CocoaPods dependencies from JFrog during the build process, you first need to create a CocoaPods repository in JFrog. For detailed steps, refer to the JFrog [**Create a CocoaPods Repository**](https://jfrog.com/help/r/jfrog-artifactory-documentation/create-a-cocoapods-repository) documentation.

#### Example 1: How can I fetch the all dependencies from JFrog with CocoaPods?

In the **CocoaPods Install** step, in order to pull dependencies from JFrog, you need to make some changes in the `Pods` file. For this, the `source url` value of the `Pods` file in the project must be replaced with the relevant artifactory. A short example is shown in the following bash script.

:::caution Configure JFrog Repository Authentication

If authentication to the repository is required, you need to authenticate to the repository with the [**Authenticate with Netrc**](/workflows/common-workflow-steps/authenticate-with-netrc) step or by using a [**Custom Script**](/workflows/common-workflow-steps/custom-script). If Custom Script is used, you can use the bash script given below.

For more information, please visit the [**JFrog Authentication**](https://jfrog.com/help/r/jfrog-artifactory-documentation/connect-cocoapods-cdn-to-artifactory) documentation.

```bash
$cat ~/.netrc
machine [JFrogPlatformURL]
login admin
password admin123
```

:::

```bash

platform :ios, '13.0'
source "https://[JFrogPlatformURL]/artifactory/api/pods/<REPO_NAME>"
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
source "https://[JFrogPlatformURL]/artifactory/api/pods/<REPO_NAME>"
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

- Trigger your build through Appcircle. The workflow will fetch dependencies from the JFrog CocoaPods repository as configured and compile the project with them.
- Logs will show dependency resolution status to confirm successful integration with JFrog.


### SPM (Swift Package Manager) Dependencies

Swift Package Manager (SPM) dependencies can also be integrated with JFrog Artifactory to manage Swift packages securely and efficiently. By configuring your package sources to point to artifactory, you can centralize package storage, improve dependency resolution speed, and maintain consistent access control and versioning across your iOS build environment.

To fetch SPM dependencies from JFrog during the build process, you first need to create a Swift repository in JFrog. For detailed steps, refer to the JFrog [**Create a Swift Repository**](https://jfrog.com/help/r/jfrog-artifactory-documentation/create-a-swift-repository) documentation.

#### How can I fetch the all dependencies from JFrog with SPM?

In the **Xcodebuild for Devices** step, to fetch SPM dependencies from JFrog, you need to make certain modifications to the `Package.swift` file within your project. For this, the relevant artifactory URL must be specified as the dependency URL in the `Package.swift` file. A short example is shown in the following bash script.

```bash

// swift-tools-version: 5.7
import PackageDescription

let package = Package(
    name: "MyApp",
    platforms: [
        .iOS(.v13)
    ],
    dependencies: [
        // JFrog Swift repository üzerinden gelen bir paket
        .package(url: "https://[JFrogPlatformURL]/artifactory/api/swift/swift-local/MyLibrary.git", from: "1.0.0")
    ],
    targets: [
        .target(
            name: "MyApp",
            dependencies: ["MyLibrary"]
        )
    ]
)

```

- JFrogPlatformURL → Artifactory Domain (For Example: https://company.jfrog.io)
- swift-local → Repository name in JFrog
- MyLibrary.git → Dependency Git Repository URL


## JFrog Integration for Android