---
title: Local Repository Integration
description: Enhance your development process with Cache Pull to quickly retrieve and reuse stored data, boosting efficiency and performance.
tags: [cache pull, efficiency, dependencies, cache structure]
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';


# Local Repository Integration

In some enterprise environments, outbound internet access is restricted, or external repository managers like **JFrog Artifactory** and **Sonatype Nexus** cannot be fully utilized. For example, Nexus currently lacks support for **Swift Package Manager (SPM)**, making it unsuitable for iOS dependency management in certain cases. To accommodate such scenarios, Appcircle allows integration with a **Local Repository**, enabling teams to host and fetch dependencies from an internal, on-premise source without external network dependency.

This guide explains how to configure and use a Local Repository for both **iOS** and **Android** projects, covering the most common dependency managers: **CocoaPods**, **Swift Package Manager**, **Maven**, and **Gradle**.

## iOS Integration

### CocoaPods Local Repository Setup

For iOS projects using CocoaPods, developers can create and host a local `.podspec` repository within the internal network or on a shared file server.

1. **Create a Local Podspec Repository**  
   Initialize a Git repository or a shared directory to host `.podspec` files:
   ```bash
   mkdir ~/local-pods
   cd ~/local-pods
   git init
   ```

2. **Add Podspecs**  
   Place your custom or mirrored `.podspec` files in this repository. For example:
   ```bash
   cp ~/MyLibrary/MyLibrary.podspec ~/local-pods/
   git add .
   git commit -m "Add local podspecs"
   ```

3. **Reference the Local Source**  
   In your project’s `Podfile`, point to the local repository path:
   ```ruby
   source 'file:///Users/username/local-pods'
   use_frameworks!
   target 'MyApp' do
       pod 'MyLibrary', '~> 1.0'
   end
   ```

4. **Install Dependencies**  
   ```bash
   pod install --verbose
   ```

This setup allows you to fetch dependencies entirely from local sources, without requiring internet access.


### Swift Package Manager (SPM) Local Repository Setup

For projects using **SPM**, dependencies can be hosted in a local Git server or a shared filesystem.

1. **Local Git Hosting**  
   Host your Swift package repository on a local Git server or accessible path.

2. **Add Dependency in Xcode**  
   Open Xcode → *File* → *Add Packages...* and enter the file path instead of a remote URL:
   ```
   file:///Users/username/Projects/MyPackage
   ```

3. **Alternative CLI Integration**  
   In `Package.swift`, add:
   ```swift
   dependencies: [
       .package(path: "../LocalPackages/MyPackage")
   ]
   ```

This approach ensures SPM dependencies are resolved locally, bypassing the need for remote repositories.


## Android Integration

### Maven Local Repository Setup

For Android or Java-based projects, you can publish and consume dependencies from a local Maven repository using Gradle’s built-in capabilities.

1. **Publish to Local Maven Repository**  
   Add the following to your module’s `build.gradle`:
   ```gradle
   publishing {
       publications {
           release(MavenPublication) {
               groupId = 'com.example'
               artifactId = 'mylibrary'
               version = '1.0.0'
               from components.release
           }
       }
       repositories {
           maven {
               url uri('/Users/username/maven-repo')
           }
       }
   }
   ```
   Then execute:
   ```bash
   ./gradlew publish
   ```

2. **Consume from Local Repository**  
   Update your main project’s `build.gradle`:
   ```gradle
   repositories {
       maven {
           url uri('/Users/username/maven-repo')
       }
       google()
       mavenCentral()
   }

   dependencies {
       implementation 'com.example:mylibrary:1.0.0'
   }
   ```


### Gradle Flat Directory Repository

If you prefer to directly include `.aar` or `.jar` files, you can use a **flatDir** repository:

```gradle
repositories {
    flatDir {
        dirs 'libs', '/Users/username/local-libs'
    }
}

dependencies {
    implementation name: 'mylibrary', ext: 'aar'
}
```

This method is ideal for fully offline builds or when artifact versioning is handled manually.