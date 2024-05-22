---
title: Appcircle Onboarding
description: To add your iOS or Android project to Appcircle, you need to complete the following checklist. The list is divided into sub-sections.
tags: [onboarding, best practices]
sidebar_position: 2
---

import ContentRef from '@site/src/components/ContentRef';

# Appcircle Onboarding

To add your iOS or Android project to Appcircle, you must complete the following checklist, divided into sub-sections.

# Prerequisite

Before building the project on Appcircle, ensure it builds properly on your local computer. Developers often do not commit changes, or their changes may not end up in the repo due to the `.gitignore` file. Follow these steps to ensure that the project builds without errors:

- Clone the repo to another folder.
- If it's an iOS project using Cocoapods or Carthage, run pod install or carthage bootstrap.
- Build the project.

If you encounter any errors, correct them and push the changes to your repo. Appcircle always starts a machine from scratch, so it must have access to all files required to build your project.

For detailed information on how Appcircle configures its build machines and manages dependencies, refer to our Infrastructure Documentation. This guide will help you understand the environments in which your applications are built, ensuring you have all necessary files and settings in place

<ContentRef url="/infrastructure">
Infrastructure
</ContentRef>

Once your project builds without error, complete the following sections:

1. Repository
2. Dependencies
3. Signing
4. Integrations
5. Extra suggestions

# Repository

## Firewall

- **Internal Networks:** If your repositories are hosted internally, you must configure firewall settings to allow the runners to clone them. This setup is essential to prevent access issues during the build process.

<ContentRef url="/build/manage-the-connections/accessing-repositories-in-internal-networks-firewalls/">
Accessing Repositories in Internal Networks (Firewalls)
</ContentRef>

- **External Hosts (e.g., GitHub.com):** If your repositories are hosted on external platforms like GitHub, no additional firewall configuration is necessary.

## Repository Owner

The person adding the repository to Appcircle must own the repository. If the owner has too many repositories, consider creating a bot user specifically for Appcircle to access only the required repositories.

## Repository Type

### Cloud

Access to repositories on GitHub and GitLab is managed by installing an app to the repository. The user who adds the repo must have the necessary access to install the application.

### Self Hosted

If your repository is Self Hosted with GitLab or Bitbucket, add your repo using an Access Token.

**Azure DevOps**

Azure DevOps requires a Personal Access Token to access the repository. The token must have access to the necessary repositories.

<ContentRef url="/build/manage-the-connections/adding-a-build-profile/connecting-to-azure">
Connecting to Azure DevOps
</ContentRef>

**GitLab**

Generate a Personal Access Token or Project Access Token for GitLab. A Personal Access Token allows access to all the repositories of that person. A Project Access Token allows access to all the repositories under the specified project.

<ContentRef url="/build/manage-the-connections/adding-a-build-profile/connecting-to-gitlab">
Connecting to GitLab
</ContentRef>

**Bitbucket**

Bitbucket also supports using repository tokens to access a single repository.

Personal Access Token allows to access all the repositories of that person. Project Access Token allows to access all the repositories under the specified project.

<ContentRef url="/build/manage-the-connections/adding-a-build-profile/connecting-to-bitbucket">
Connecting to Bitbucket
</ContentRef>

Appcircle requires admin permission to function properly, which is necessary to create relevant WebHooks automatically.

:::note

If dependencies used by the repo are in a different project or inaccessible to the person, the build will throw an error. Therefore, the added token must have access to all necessary dependencies.

:::

## Dependencies

If you use libraries in a private repo, these must be accessible with the tokens mentioned above. If this is not possible, access these libraries using one of the following methods:

- SSH Private Key
- .netrc file

### SSH Private Key

Create a new SSH key, upload the public key to your Repo, and the private key to Appcircle. Follow the steps in this guide.

<ContentRef url="/build/manage-the-connections/adding-a-build-profile/connecting-to-private-repository-via-ssh">
Connecting to Private Repository via SSH
</ContentRef>

### Netrc File

The .netrc file contains login and initialization information used by the auto-login process. You can use this component to add credentials for hosts such as your repositories or external hosts. Git automatically recognizes the .netrc file.\

<ContentRef url="/workflows/common-workflow-steps/authenticate-with-netrc">
Authenticate with .netrc
</ContentRef>

## Signing

To upload artifacts to the App Store or GooglePlay, the files must be signed. Upload the following files to Appcircle's Signing Module:

### iOS

There are two types of signing for iOS, Manual and Automatic.

Manual Signing requires you to upload the provisioning profile for each bundle id. For Automatic code signing, only 2 certificates and App Store Connect Key must be added.

**Manual Signing:**

- Upload the Distribution Certificate as a `.p12` file. It is better to create a new distribution certificate specifically for Appcircle.
- Upload Provisioning profiles created with the above certificates. A green checkmark will appear next to the entry if successful. If not, refresh the page or check for missing certificate files.

**Automatic Sign**

Automatic signing works with Xcode 13 and later. It requires:

- One Distribution Certificate
- One Development Certificate
- App Store Connect API Key

Provide both development and distribution certificates to prevent Xcode from continuously creating new certificates in your account.

### Android

For Android, upload the keystore file used to sign the project. Simply uploading this file may not suffice for signing; adjustments to the `build.gradle` file might also be necessary. Consult this document for further guidance.

<ContentRef url="/build/platform-build-guides/building-android-applications/android-signing-for-google-play#enable-v2-sign-through-the-android-project-buildgradle">
Android Signing for Google Play
</ContentRef>

## Integrations

Add App Store, Google Play, or Huawei AppGallery keys to Appcircle to upload IPA or APK-AAB files. Follow these guides for detailed instructions:

<ContentRef url="/publish-integrations/ios-publish-integrations/send-to-app-store">
Send to App Store
</ContentRef>

<ContentRef url="/publish-integrations/android-publish-integrations/send-to-googleplay">
Send to Google Play
</ContentRef>

<ContentRef url="/publish-integrations/android-publish-integrations/send-to-huawei">
Send to Huawei
</ContentRef>

## Extra suggestions

**General**

- Manage confidential or frequently changing information with Environment Variables to achieve different outputs by selecting different variable groups without altering your code.

<ContentRef url="/environment-variables/managing-variables#creating-environment-variable-groups">
Creating Environment Variable Groups
</ContentRef>

<ContentRef url="/environment-variables/platform-specific-usage/using-environment-variables-in-ios-projects#using-different-values-for-different-stages">
Using Different Values for Different Stages
</ContentRef>

<ContentRef url="/environment-variables/platform-specific-usage/using-environment-variables-in-android-projects">
Using Environment Variables in Android Projects
</ContentRef>

- Specify versions for React Native and Flutter on the config screen to avoid building with the latest version by default.
- Disable Flipper in React Native to shorten build times by modifying the Podfile as follows:

```
if !ENV['AC_APPCIRCLE']
    use_flipper!
    post_install do |installer|
      flipper_post_install(installer)
    end
  end
```

**iOS**

- If you are using CocoaPods, SwiftPM or Carthage, you need to commit `Podfile.lock` `Package.resolved` and `Cartfile.resolved` files. When these files are not available, the wrong versions may be installed.
- Avoid making local changes to your pods. If necessary, fork the original pod and make changes in that fork. Appcircle must have access to the same code as your local machine.

**Android**

- Include your Gradle folder in your repo. Appcircle uses the `./gradlew` command to build your project. If this file is missing, the build will fail.
- Update your build.gradle file to replace `jcenter()` with `mavenCentral()` if your project uses Bintray resources, as JFrog shut down Bintray on May 1, 2021. Some dependencies may not be available on Maven.
- Consider uploading dependencies used from jitpack to `mavenCentral()`. Jitpack has reliability issues, and while your local builds may use cached versions, Appcircle downloads your dependencies for each build, which can lead to problems.\

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />

Need more help? Check out our FAQ section:

<ContentRef url="/troubleshooting-faq">
FAQ
</ContentRef>
