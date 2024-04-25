---
title: Appcircle Onboarding
description: To add your iOS or Android project to Appcircle, you need to complete the following checklist. The list is divided into sub-sections.
tags: [onboarding, best practices]
sidebar_position: 2
---

import ContentRef from '@site/src/components/ContentRef';

# Appcircle Onboarding

To add your iOS or Android project to Appcircle, you need to complete the following checklist The list is divided into sub-sections.

# Prerequisite

Before building the project on Appcircle, it should be checked whether it builds properly on your local computer. Frequently, the developers do not send the changes on their local computer, or their changes may not end up on the repo because of .gitignore file. The following steps should be followed to check that the project can be built without errors. If possible, these steps should be tried in a virtual machine, if not, with a different user or folder.

- Clone the repo to another folder
- If it's an iOS project and using Cocoapods or Carthage, run pod install or carthage bootsrap.
- Build the project.

If you get any errors, correct them and push them to your repo. Since Appcircle always starts a machine from scratch. Appcircle should have access to all files required to build your project.

If your projects builds without an error, you need to complete the following sections.

1. Repository
2. Dependencies
3. Signing
4. Integrations
5. Extra suggestions

# Repository

## Firewall

<ContentRef url="/build/manage-the-connections/accessing-repositories-in-internal-networks-firewalls/">
Accessing Repositories in Internal Networks (Firewalls)
</ContentRef>

## Repository Owner

The person who will add the repository to Appcircle must be the owner of the repository. If the owner of the repository has too many repositories, a bot user can be created just for Appcircle so that only the required repositories can be accessed.

## Repository Type

### Cloud

Repo access is achieved for GitHub and GitLab by installing an app to the repository. The user who added the repo must have the required access to add the application

### Self Hosted

If your repo is Self Hosted with GitLab or Bitbucket, your repo will be added with an Access Token.

**GitLab**

You will need to generate Personal Access Token or Project Access Token for GitLab. Personal Access Token allows to access all the repositories of that person. Project Access Token allows to access all the repositories under the specified project.

https://docs.appcircle.io/build/adding-a-build-profile/connecting-to-gitlab/

**Bitbucket**

Bitbucket also allows using repository tokens to access a single repository.
Personal Access Token allows to access all the repositories of that person. Project Access Token allows to access all the repositories under the specified project.

https://docs.appcircle.io/build/adding-a-build-profile/connecting-to-bitbucket

Appcircle needs admin permission to function properly. The admin permission is needed to create relevant WebHooks automatically.

**NOTE:**

If the dependencies used by the repo are in a different project or that person does not have access to that repo, the project will throw an error while building. So the added token must have access to all the dependencies needed to build the project.

## Dependencies

If the extra libraries you use are in a private repo, these repositories must be accessible with the tokens we mentioned above. If this is not possible, these libraries should be accessed in one of the following ways.

- SSH Private Key
- .netrc file

### SSH Private Key

You will need to create a new SSH key and upload the public key to your Repo and the private key to Appcircle. These files can be created easily by following the document below.

https://docs.appcircle.io/build/manage-the-connections/adding-a-build-profile/connecting-to-private-repository-via-ssh

### Netrc File

The .netrc file contains login and initialization information used by the auto-login process. You can use this component to add credentials for hosts such as your repositories or external hosts. Git automatically recognizes the .netrc file

https://docs.appcircle.io/workflows/common-workflow-steps/#authenticate-with-netrc

## Signing

To upload artifacts to the App Store or GooglePlay, the files must be signed. The files listed below must be uploaded to Appcircle's Signing Module

### iOS

There are 2 types of signing for iOS, Manual and Automatic.

Manual Signing requires you to upload the provisioning profile for each bundle id. For Automatic code signing, only 2 certificates and App Store Connect Key must be added.

**Manual Sign**

- Distribution Certificate. The certificate must be uploaded as .p12 file. It would be better to create a distribution certificate from scratch for Appcircle.
- Provisioning profiles created with the above certificates. After uploading the Provisioning profile files, a green checkmark image will appear next to the entry. If it does not appear, you may need to refresh the page. If the error persists, it means that the certificate file is missing on Appcircle.

**Automatic Sign**

Automatic signing can be used for projects that can be built with Xcode 13 and later. This requires the following

- 1 Distribution Certificate
- 1 Development Certificate
- App Store Connect API Key

When the above credentials are provided, Xcode automatically creates provisioning profiles and signs the application. It is important to add both development and distribution certificates. If you do not provide the required certificates, Xcode will constantly create new certificates in your account.

### Android

The only thing that needs to be installed for Android is the keystore file you used to sign the project. Simply uploading this file will often not be sufficient for signing. You will also need to make changes to the build.gradle file and sign it with the keystore installed on the Appcircle environment. Please check the following document for this process.

https://docs.appcircle.io/build/building-android-applications/android-signing-for-google-play/#enable-v2-sign-through-the-android-project-buildgradle

## Integrations

App Store, Google Play, or Huawei App Gallery keys must be added to Appcircle to upload IPA or APK files. To create these files, the following documents can be followed.

https://docs.appcircle.io/publish-integrations/android-publish-integrations/send-to-googleplay

https://docs.appcircle.io/publish-integrations/ios-publish-integrations/send-to-app-store

https://docs.appcircle.io/publish-integrations/android-publish-integrations/send-to-huawei

## Extra suggestions

**General**

- It will be better to manage confidential or constantly changing information with Environment Variables. This will allow you to get different outputs by selecting different variable groups without changing your code.

https://docs.appcircle.io/environment-variables/managing-variables/#creating-environment-variable-groups

https://docs.appcircle.io/environment-variables/using-environment-variables-in-ios-projects/#using-different-values-for-different-stages

https://docs.appcircle.io/environment-variables/using-environment-variables-in-android-projects

- It is important that the versions you use for React Native and Flutter are written on the config screen. If you don't set a version, it will be built with the latest version.
- If you are using React Native, you can turn off Flipper with the following change in the Podfile. This will shorten your build times.

```
if !ENV['AC_APPCIRCLE']
    use_flipper!
    post_install do |installer|
      flipper_post_install(installer)
    end
  end
```

**iOS**

- If you are using CocoaPods, SwiftPM or Carthage, you need to commit Podfile.lock Package.resolved and Cartfile.resolved files. When these files are not available, the wrong versions may be installed.
- You should not make any local changes to your pods. If you are going to make a change, you must fork the original pod and make the changes in that fork. Appcircle must have the access to the same code as you have on your local machine.

**Android**

- Don't forget to add your gradle folder to your repo. Appcircle uses ./gradlew command to build your poject. Therefore, if that file does not exist, the build will fail
- You may experience Gradle build errors if your project uses Bintray resources. Since JFrog has shutdowned Bintray on May 1, 2021. You should update your `build.gradle` file and move it to Maven Central. Replace `jcenter()` with `mavenCentral()` in all your `build.gradle` files. Please be aware that some of your dependencies may not exist on Maven.
- If you are using jitpack in your project, it will be useful to upload these dependencies to `mavenCentral()`. It is recommended to create your Maven repo to host your dependencies. Jitpack has reliability issues and you may not experience those issues on your local computer since your builds use cache. However, Appcircle will download your dependencies each time you start a build and Jitpack may create a problem in the long run.
