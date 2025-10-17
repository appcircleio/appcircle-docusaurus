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

Integrating JFrog Artifactory into Android projects centralizes the management of Maven and Gradle dependencies and build artifacts. By configuring a module’s `build.gradle` or `settings.gradle` files to point to artifactory repositories, engineers enable reliable retrieval, caching, versioning, and distribution of libraries and modules. This integration accelerates build times, enforces consistent build environments, and enhances traceability across CI/CD workflows. Artifactory’s vulnerability scanning and license‑compliance checks further help maintain the integrity and security of the Android supply chain.


### Gradle Dependencies

Integrating JFrog Artifactory with Gradle enables centralized dependency management, artifact publishing, and version control within your Android build system. This setup helps development teams ensure reproducible builds, optimize caching, and maintain full traceability of artifacts across CI/CD pipelines.

#### 1. Configure Repositories in `build.gradle`
To integrate JFrog Artifactory into an Android project, you need to define your repository endpoints inside the project’s `build.gradle` or `settings.gradle` file.

**Example (Project-level `build.gradle`):**
```gradle
buildscript {
    repositories {
        maven {
            url "https://[JFrogPlatformURL]/artifactory/[REPO_NAME]"
            credentials {
                username = project.findProperty("artifactory_user") ?: System.getenv("ARTIFACTORY_USER")
                password = project.findProperty("artifactory_password") ?: System.getenv("ARTIFACTORY_PASSWORD")
            }
        }
        google()
        mavenCentral()
    }

    dependencies {
        classpath "com.android.tools.build:gradle:8.1.0"
    }
}
```

**Example (Module-level `build.gradle`):**
```gradle
repositories {
    maven {
        url "https://[JFrogPlatformURL]/artifactory/[REPO_NAME]"
        credentials {
            username = project.findProperty("artifactory_user") ?: System.getenv("ARTIFACTORY_USER")
            password = project.findProperty("artifactory_password") ?: System.getenv("ARTIFACTORY_PASSWORD")
        }
    }
    google()
    mavenCentral()
}

dependencies {
    implementation "com.squareup.retrofit2:retrofit:2.9.0"
    implementation "org.jetbrains.kotlinx:kotlinx-coroutines-android:1.7.3"
}
```

**Key Parameters:**
- `JFrogPlatformURL` → Your Artifactory domain (e.g. `https://company.jfrog.io`)
- `[REPO_NAME]` → The target repository (e.g. `gradle-release-local`)
- `credentials` → Authentication credentials from environment variables or Gradle properties

#### 2. Authentication with Artifactory
If authentication is required, use either:
- The **Authenticate with Netrc** step in Appcircle *(recommended for security and automation)*, or
- Store credentials in environment variables or encrypted Gradle properties (`gradle.properties`):

```properties
artifactory_user=yourUsername
artifactory_password=yourPassword
```

#### 3. Publishing Artifacts to Artifactory
You can also publish your own libraries or build outputs to Artifactory using the official **Gradle Artifactory Plugin**.

Add the plugin to your root `build.gradle`:
```gradle
plugins {
    id "com.jfrog.artifactory" version "4.33.2"
}
```

Configure publishing settings:
```gradle
artifactory {
    contextUrl = "https://[JFrogPlatformURL]/artifactory"
    publish {
        repository {
            repoKey = "gradle-release-local"
            username = project.findProperty("artifactory_user")
            password = project.findProperty("artifactory_password")
        }
        defaults {
            publications("release")
            publishArtifacts = true
        }
    }
}
```

This allows the CI/CD pipeline (e.g. Appcircle) to automatically push your `.aar` or `.apk` artifacts to JFrog Artifactory after successful builds.


### Maven Dependencies

Integrating JFrog Artifactory with Maven allows you to manage dependencies, plugins, and project artifacts through a secure, centralized repository. This integration ensures reproducible builds, consistent dependency resolution, and full control over versioning and artifact promotion within your Android CI/CD workflows.

#### 1. Configure Repositories in `pom.xml`
To use Artifactory with Maven, define your repository endpoints inside your project’s `pom.xml` file under the `<repositories>` and `<pluginRepositories>` sections:

```xml
<repositories>
  <repository>
    <id>jfrog-release</id>
    <name>JFrog Release Repository</name>
    <url>https://[JFrogPlatformURL]/artifactory/[REPO_NAME]</url>
  </repository>
</repositories>

<pluginRepositories>
  <pluginRepository>
    <id>jfrog-plugins</id>
    <url>https://[JFrogPlatformURL]/artifactory/[PLUGIN_REPO_NAME]</url>
  </pluginRepository>
</pluginRepositories>
```

#### 2. Authentication Configuration
To authenticate with Artifactory, add your credentials to the global Maven configuration file (`~/.m2/settings.xml`):

```xml
<servers>
  <server>
    <id>jfrog-release</id>
    <username>${env.ARTIFACTORY_USER}</username>
    <password>${env.ARTIFACTORY_PASSWORD}</password>
  </server>
</servers>
```

- `JFrogPlatformURL` → Artifactory domain (e.g. `https://company.jfrog.io`)
- `[REPO_NAME]` → Target Maven repository (e.g. `libs-release-local`)
- `[PLUGIN_REPO_NAME]` → Repository for Maven plugins

This approach allows secure integration within Appcircle pipelines using environment variables or the **Authenticate with Netrc** step.

#### 3. Deploy Artifacts to Artifactory
To publish build artifacts (e.g., `.jar`, `.aar`) to Artifactory, use the Maven Deploy plugin or the **Artifactory Maven Plugin**.

**Example `distributionManagement` configuration:**
```xml
<distributionManagement>
  <repository>
    <id>jfrog-release</id>
    <url>https://[JFrogPlatformURL]/artifactory/libs-release-local</url>
  </repository>
  <snapshotRepository>
    <id>jfrog-snapshot</id>
    <url>https://[JFrogPlatformURL]/artifactory/libs-snapshot-local</url>
  </snapshotRepository>
</distributionManagement>
```

#### 4. Using the JFrog Maven Plugin
Add the plugin to your `pom.xml` to automate uploads:

```xml
<build>
  <plugins>
    <plugin>
      <groupId>org.jfrog.buildinfo</groupId>
      <artifactId>artifactory-maven-plugin</artifactId>
      <version>3.5.4</version>
      <executions>
        <execution>
          <id>build-info</id>
          <goals>
            <goal>publish</goal>
          </goals>
        </execution>
      </executions>
      <configuration>
        <url>https://[JFrogPlatformURL]/artifactory</url>
        <username>${env.ARTIFACTORY_USER}</username>
        <password>${env.ARTIFACTORY_PASSWORD}</password>
        <repoKey>libs-release-local</repoKey>
      </configuration>
    </plugin>
  </plugins>
</build>
```
