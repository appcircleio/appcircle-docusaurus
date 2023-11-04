---
title: Latest Release Notes
metaTitle: Latest Release Notes
metaDescription: Latest Release Notes
sidebar_position: 1
---

import ContentRef from '@site/src/components/ContentRef';
import SelfHostedBadge from '@site/src/components/SelfHostedBadge';
import CloudBadge from '@site/src/components/CloudBadge';

# Latest Release Notes

## 3.9.0 - 2023-11-01 - LDAP Support for User Authentication, Change the PAT by Build Profile, Download Environment Variables

### 🆕 New Feature

- "Self-hosted Settings" has been introduced on the admin page for self-hosted Appcircle server. It includes "LDAP login" for configuring LDAP user authentication and other "Login Settings". <SelfHostedBadge/>
- Users are now allowed to manage their connections to private repositories after connecting their profiles. <CloudBadge/> <SelfHostedBadge/>
- Now users are able to download the [environment variables](../environment-variables/managing-variables.md) in JSON format. <CloudBadge/> <SelfHostedBadge/>
- Added a new environment variable called [AC_TRIGGER_REASON](../environment-variables/appcircle-specific-environment-variables.md#ios--android-common-environment-variables) that specifies the trigger that causes the build to start. <CloudBadge/> <SelfHostedBadge/>
- The "Default M1 Pool" runners have [Xcode 15.1 beta-1](../build/building-ios-applications.md) installed. As this is a beta release, please test your workflows thoroughly. <CloudBadge/> <SelfHostedBadge/>
- A new filter has been added for filtering reports. Users will now be able to filter by organization and sub organization. <CloudBadge/> <SelfHostedBadge/>
- New commands "download" and "load" were introduced to the self-hosted Appcircle server in order to support offline installation scenarios <SelfHostedBadge/>
- The self-hosted Appcircle server now supports Secure LDAP, aka LDAPS, that encrypts the authentication process for enhanced security. <SelfHostedBadge/>

### :muscle: Improvement

- A parent organization can access its children's "Build History", "Signing History", "App Sharing Report", "Enterprise App Store Reports", and "Queue Waiting Reports". <CloudBadge/> <SelfHostedBadge/>
- Improvements have been made to the [email notification](../account/email-connection) format for build events. <CloudBadge/> <SelfHostedBadge/>
- The "Default M1 Pool" has the latest stable [Xcode 15.0.1](https://developer.apple.com/documentation/xcode-release-notes/xcode-15_0_1-release-notes) update available on runners. <CloudBadge/> <SelfHostedBadge/>
- We now support Azure DevOps Server 2020 connection while adding a [build profile](../build/adding-a-build-profile/connecting-to-azure.md). <CloudBadge/> <SelfHostedBadge/>
- The [public link](../distribute/create-or-select-a-distribution-profile.md#using-public-link-for-distribution) in the test deployment area will now be available regardless of authentication type. <CloudBadge/> <SelfHostedBadge/>
- A bug that prevented failed builds from sending notifications to the MS Teams application has been fixed. <CloudBadge/> <SelfHostedBadge/>
- Previously, you could only select one profile for test deployment. Now you can select multiple profiles in the [distribution](../distribute/create-or-select-a-distribution-profile.md) profile settings. <CloudBadge/> <SelfHostedBadge/>
- Removed the obsolete icon from the Commit ID redirect link in the build profile details. <CloudBadge/> <SelfHostedBadge/>
- The cache size was bumped to 4 GB while using the [cache push](../workflows/common-workflow-steps.md#cache-push) in the build pipeline. <SelfHostedBadge/>
- We made improvements to the self-hosted server [SSL configuration](../self-hosted-appcircle/configure-server/ssl-configuration.md) for enhanced security. <SelfHostedBadge/>

### 🐞 Fixed

- Builds that took longer than an hour showed the wrong time on the left side of the screen. This has been fixed. <CloudBadge/> <SelfHostedBadge/>
- While reviewing the build logs in the admin panel, if there is no build log, we were not showing the user an error. Now it is shown as a toast message. <CloudBadge/> <SelfHostedBadge/>
- The bug that occurred if there were no screenshots in the test project has been fixed. <CloudBadge/> <SelfHostedBadge/>
- A problem related to component caching in the runner has been resolved. <CloudBadge/> <SelfHostedBadge/>
- Without user [permission](../account/my-organization#special-permissions), requests on the relevant screens are no longer sent to the service, so no warnings are displayed. <CloudBadge/> <SelfHostedBadge/>
- We were not showing the status of the request with the loader when a request was sent for workflows; this problem has been fixed. <CloudBadge/> <SelfHostedBadge/>
- Some spelling errors at the beginning of the workflow have been fixed, and a user-friendly appearance has been provided. <CloudBadge/> <SelfHostedBadge/>
- Fixed a bug that prevented logging in to the Enterprise App Store. <CloudBadge/> <SelfHostedBadge/>
- Fixed the error that occurred when test users emails were written in capital letters. <CloudBadge/> <SelfHostedBadge/>
- In the general profile tab in the [distribution profile](../distribute/create-or-select-a-distribution-profile.md), the incorrect screen movement that occurred when the switch was disabled and reactivated was fixed. <CloudBadge/> <SelfHostedBadge/>
- Fixed unnecessary requests that go on report screens in the case of being a [sub organization](../account/my-organization#working-with-multiple-organizations). <CloudBadge/> <SelfHostedBadge/>
- Fixed missing versioning for the [HashiCorp Vault](https://blog.appcircle.io/article/security-in-appcircle) container image on the self-hosted server. <SelfHostedBadge/>

## 3.8.0 - 2023-10-02 - Multiple Git Providers Support, Config Clone, Pool-Based Xcode Version Selection

### 🆕 New Feature

- The user can add [multiple instances](../build/adding-a-build-profile/connecting-multiple-instance) of the Git providers and select any of them to connect to. So the user can bind and build the repositories. <CloudBadge/> <SelfHostedBadge/>
- The [Xcode version](../self-hosted-appcircle/self-hosted-runner/configure-runner/manage-pools/#pool-based-xcode-version-selection) list of runners is integrated into the custom pool selection. It can be displayed dynamically in the build configuration, and the user can choose which Xcode version to build with. <CloudBadge/> <SelfHostedBadge/>
- You can now quickly [copy a configuration](../build/build-profile-configuration#clone-configuration) and create a new one from that configuration. <CloudBadge/> <SelfHostedBadge/>

### :muscle: Improvement

- Waiting times in Queue Waiting Reports are now shown in minutes instead of seconds. <SelfHostedBadge/>
- If the user selects any step that has the "Continue with the next step even if this step fails" option and gets a failure during the build on that step, this build's status is displayed as [Warning](../workflows/why-to-use-workflows/#build-warning-status). <CloudBadge/> <SelfHostedBadge/>
- Fixed the case that users belonging to more than one organization on [Azure DevOps](/build/adding-a-build-profile/connecting-to-azure) could not bind repository. <CloudBadge/> <SelfHostedBadge/>
- Improved suborganization experience in the Enterprise App Store by hiding the "Customize" and "Settings" sections, providing a more focused interface for suborganization administrators. <CloudBadge/> <SelfHostedBadge/>
- The latest stable version of [Xcode 15.0](../build/building-ios-applications.md) is available on both cloud and self-hosted runners. <SelfHostedBadge/> <CloudBadge/>
- The self-hosted Appcircle server now supports proxies with a [self-signed certificate.](../self-hosted-appcircle/configure-server/proxy-configuration.md) <SelfHostedBadge/>
- Users can more easily switch to the self-hosted version of their choice by only [downloading](../self-hosted-appcircle/update.md#1-download-latest) the server package. <SelfHostedBadge/>
- Added the [NTP configuration](../self-hosted-appcircle/self-hosted-runner/runner-vm-setup.md#1-configure-base-runners-ntp-settings) helper tool to the self-hosted runner package. <SelfHostedBadge/>
- Added self-signed certificate management for Node.JS to the [certificate installer](../self-hosted-appcircle/self-hosted-runner/configure-runner/custom-certificates.md#adding-certificates) tool. <SelfHostedBadge/>
- Now you can analyze your [SwiftLint](../integrations/azure-bot-for-swiftlint-and-detekt.md#azure-devops-bot-for-swiftlint) and [Detekt](../integrations/azure-bot-for-swiftlint-and-detekt.md#azure-devops-bot-for-detekt) reports and post the report details under the opened PR on Azure DevOps. <CloudBadge/> <SelfHostedBadge/>

### 🐞 Fixed

- Fixed the "Waiting Duration" title in the Queue Waiting Reports header. <SelfHostedBadge/>
- The role management error in the [Apple Devices](../distribute/apple-devices.md) section in the Testing Distribution module has been fixed. <CloudBadge/> <SelfHostedBadge/>
- Fixed the issue of not being able to distribute to the selected configuration in the [Testing Distribution](../distribute/create-or-select-a-distribution-profile.md) module. <CloudBadge/> <SelfHostedBadge/>
- Fixed the issue where the branch list could not be refreshed when the user [permission](../account/my-organization.md) for the Build module was set to "Read Only Access". <CloudBadge/> <SelfHostedBadge/>
- Fixed the issue where the build does not appear in the list when the build starts. <CloudBadge/> <SelfHostedBadge/>
- Fixed the bug that users without permission were sending requests to the service when browsing pages. <CloudBadge/> <SelfHostedBadge/>
- In the Store Submit module, the "Huawei App ID" field in the [Huawei AppGallery](../store-submit/huawei-app-gallery.md) section was disabled. It's been fixed. <CloudBadge/> <SelfHostedBadge/>
- Flickering on the screen due to line overlap in the build module has been fixed. <CloudBadge/> <SelfHostedBadge/>
- When an invalid email was entered in the [email integration](../account/email-connection) module, other options were reset. It's been fixed. <CloudBadge/> <SelfHostedBadge/>
- The wrong dialog modal was opening in the "never delete" option selected for the deletion of an artifact. It's been fixed, and an extra description has been added. <CloudBadge/> <SelfHostedBadge/>
- When there was a workflow step of the same name, there was a confusion of names. It's has been fixed. <CloudBadge/> <SelfHostedBadge/>
- An error message is now displayed to the user when an invalid workflow name is entered. <CloudBadge/> <SelfHostedBadge/>
- Fixed the data refresh error when the version is deleted in the [Apple Devices](../distribute/apple-devices.md) section of the Testing Distribution module. <CloudBadge/> <SelfHostedBadge/>
- Fixed the page crash problem when the user clicks on the [Triggers](../build/build-manually-or-with-triggers.md). <CloudBadge/> <SelfHostedBadge/>
- Added a toast message that is shown when the user tries to download the deleted configuration in the admin panel. <CloudBadge/> <SelfHostedBadge/>
- The case that selection of the adhoc [auto device register](../distribute/apple-devices.md#automatically-adding-registered-devices-to-the-provisioning-profile) on the distribution profile settings has been fixed. <CloudBadge/> <SelfHostedBadge/>

## 3.7.0 - 2023-09-05 - Email Notification, Queue Waiting Reports

### 🆕 New Feature

- We added a new admin report for the queue waiting report. Now self-hosted enterprise customers can see the queue status and waiting durations of each build, fetch, store submit, and resign process. <SelfHostedBadge/>
- You can now send [email notifications](../account/email-connection.md) for most actions taken within Appcircle (build start, store submit, etc.). <CloudBadge/> <SelfHostedBadge/>
- Self-hosted [runner](../self-hosted-appcircle/self-hosted-runner/installation.md) now supports installation of the latest [Xcode 15.0](../infrastructure/ios-build-infrastructure.md) release with all its simulator runtimes. Since this is a beta release, please test your workflows extensively. <SelfHostedBadge/>

### :muscle: Improvement

- Removed profile names will now appear as "Deleted" in corporate store reports. <CloudBadge/> <SelfHostedBadge/>
- The active build section now shows the email address that started the build, not the email address of the user who created the profile. <CloudBadge/> <SelfHostedBadge/>
- If there is a space character in the [variable group](../environment-variables/managing-variables.md#using-environment-variables-for-ssh-and-pat-personal-access-token-connections-of-the-git-provider) name, it can be used within double quotes while connecting the repository. <CloudBadge/> <SelfHostedBadge/>
  - `$"Variable Group:Key"`
- Self-hosted enterprise customers can download the [configurations](../build/build-profile-configuration.md) of previous builds with the `.yaml` extension in "Build Details" section of the admin panel. <SelfHostedBadge/>
- Unsubscribe and resubscribe features are enabled for email notifications, distribution, and the enterprise store. <CloudBadge/> <SelfHostedBadge/>

### 🐞 Fixed

- The confusion regarding the use of Turkish characters when creating [workflows](../workflows/why-to-use-workflows.md)  and [configurations](../build/build-profile-configuration.md) has been resolved. Turkish characters and some special characters can no longer be used in this section. <CloudBadge/> <SelfHostedBadge/>
- The error in [permission management](../account/my-organization.md) in the environment variables section has been fixed. <CloudBadge/> <SelfHostedBadge/>
- The problem with the build transaction texts above the branch name in the "Branch" section being mixed up has been fixed. <CloudBadge/> <SelfHostedBadge/>
- The error in permission management in the [Enterprise Store](../enterprise-appstore/add-ent-profile.md) section has been fixed. <CloudBadge/> <SelfHostedBadge/>
- The incorrect display of the inactive steps at the beginning of the build pipeline has been fixed. It was affecting the workflow steps section in the build logs while the build was running. <CloudBadge/> <SelfHostedBadge/>
- The problem of creating groups without a group name and with an existing name on the API's side has been fixed. <CloudBadge/> <SelfHostedBadge/>
- Optional steps won't affect build status anymore. If "Continue with the next step even if this step fails" is selected, your build status will not turn failed. <CloudBadge/> <SelfHostedBadge/>

## 3.6.0 - 2023-08-03 - Azure DevOps Integration, Using Environment Variables On Git Integrations

### 🆕 New Feature
- Now you can connect repositories from [Azure DevOps Services](../build/adding-a-build-profile/connecting-to-azure.md) and Azure DevOps Server for your builds. <CloudBadge/> <SelfHostedBadge/>
- Added support for using [webhook](../account/webhooks.md) with OAuth 2.0 and the Personal Access Token on Azure DevOps. <CloudBadge/> <SelfHostedBadge/>
- The quick add feature has been added to the new project screen for both Azure DevOps Services and Azure DevOps Server. <CloudBadge/> <SelfHostedBadge/>
- LDAP, user lookup decision strategy can be configured in global.yaml. See [LDAP settings](../self-hosted-appcircle/configure-server/ldap-settings.md) for details. <SelfHostedBadge/>

### :muscle: Improvement
- The ability to use information such as [SSH and PAT](../build/adding-a-build-profile/connecting-to-private-repository-via-ssh.md), that is required for adding new projects with SSH has been added with environment variables. <CloudBadge/> <SelfHostedBadge/>
- The [Tag Model](../build/build-manually-or-with-triggers.md) now includes the name and email of the user who created the tag. <CloudBadge/> <SelfHostedBadge/>
- The self-hosted script can now be called from anywhere in the OS. <SelfHostedBadge/>

### 🐞 Fixed
- Fixed a bug that users were experiencing when adding to the provisioning profile. <CloudBadge/> <SelfHostedBadge/>
- Fixed a bug that caused [endpoints](../appcircle-api/api-authentication.md) to not appear in the webhook module on Swagger. <CloudBadge/> <SelfHostedBadge/>
- When an event matches the trigger rules, all satisfied triggers will be executed. <CloudBadge/> <SelfHostedBadge/>
- The user is redirected to the "invitation expired" page when the [invitation](../account/my-organization.md) link is timed out. <CloudBadge/> <SelfHostedBadge/>
- The health check command was fixed, and it now reports the correct state both for Podman and Docker. <SelfHostedBadge/>
- The missing service on the Podman installation was fixed. <SelfHostedBadge/>

## 3.5.0 - 2023-07-13 - Configuration, Workflow Improvements, New Autofill Feature

### 🆕 New Feature
- Added the "Autofill" option when creating a new build profile and connecting it with the service. <CloudBadge/> <SelfHostedBadge/>
- [Xcode 15.0 Beta-4](../infrastructure/ios-build-infrastructure.md) added to build agents. Since this is a beta release, please test your workflows extensively. <CloudBadge/>

### :muscle: Improvement
- Added the feature that [LDAP and SSO](../account/sso-ldap-login.md) settings  can be made once and all sub-organizations can use this setting. <CloudBadge/> <SelfHostedBadge/>
- Previous [Configuration and Workflow](../build/adding-a-build-profile) files can be downloaded in the Configuration and Workflow sections. The ability to create configuration and workflow by re-uploading downloaded `.yaml` files has been improved. <CloudBadge/> <SelfHostedBadge/>
- On the [self-hosted](../self-hosted-appcircle/self-hosted-runner/overview.md) side, the feature of adding priority has been developed for online and offline runners. <CloudBadge/> <SelfHostedBadge/>
- Sequential numbering improvement was made in the naming while creating the new configuration and workflow. <CloudBadge/> <SelfHostedBadge/>
- The ability to send files from the Testing Distribution module to the Enterprise App Store added. <CloudBadge/> <SelfHostedBadge/>
- Made an improvement to prevent the subordinate from accessing the details on the 'corporate settings' page. <CloudBadge/> <SelfHostedBadge/>
- Default M1 Pool is automatically selected in case of [Xcode](../infrastructure/ios-build-infrastructure.md) version 14.3.x and above. <CloudBadge/>
- Improved the display of device name if there is an available device on the [IOS provisioning](../distribute/apple-devices.md) profile side. <CloudBadge/> <SelfHostedBadge/>
- Subtitle would also have to be searched for components. This development has been done. <CloudBadge/> <SelfHostedBadge/>

### 🐞 Fixed
- Fixed an issue where the user could not create a [sub-organization](../account/my-organization.md) even though they had the required permission. <CloudBadge/> <SelfHostedBadge/>
- Fixed issue with file permissions when exporting a project for self-hosted uses. <SelfHostedBadge/>
- Fixed the problem of adding the same name while uploading the [configuration](../build/adding-a-build-profile). <CloudBadge/> <SelfHostedBadge/>
- The permissions of the applications in the Huawei App Gallery that depend on the permission to view the applications in the [store submit](../store-submit/huawei-app-gallery.md) section has been fixed. <CloudBadge/> <SelfHostedBadge/>
- The problem that the save button is not active after the changes made in the organization pool has been fixed. <CloudBadge/> <SelfHostedBadge/>
- Fixed a double slash (`//`) bug on the webhook link that caused the triggers to not work. <CloudBadge/> <SelfHostedBadge/>
- The error that the change indicator appears even though there is no change in some tabs in the config modal has been fixed. <CloudBadge/> <SelfHostedBadge/>
- Apple Devices improved, not sending device enrollment link if auto enrollment is disabled. <CloudBadge/> <SelfHostedBadge/>
- Fixed configuration creation error without giving any name. <CloudBadge/> <SelfHostedBadge/>
- Fixing UI bugs in search field in [Testing Distribution](../distribute/create-or-select-a-distribution-profile.md) module. <CloudBadge/> <SelfHostedBadge/>
- Fixed a bug that caused triggers to be deleted. <CloudBadge/> <SelfHostedBadge/>
- The error that the save button is not active when I change the [offset](../versioning/ios-version.md) part of the build number has been fixed. <CloudBadge/> <SelfHostedBadge/>
- Fixed unsigned owners error on files that are not resigned in test deployment part. <CloudBadge/> <SelfHostedBadge/>
- Fixed some icons appearing properly in dark mode. <CloudBadge/> <SelfHostedBadge/>

## 3.4.0 - 2023-06-09 - Build Profile Improvements, Azure Boards 

### 🆕 New Feature
- [Xcode 15.0 Beta](../infrastructure/ios-build-infrastructure.md) added to build agents. Since this is a beta release, please test your workflows extensively. <CloudBadge/> <SelfHostedBadge/>
- [Java 17](../infrastructure/android-build-infrastructure.md) added to build agents. <CloudBadge/> <SelfHostedBadge/>
- [Build Profile](../build/adding-a-build-profile/README.md) configurations are separated from branchs. It is now easier to see and manage configs from a single location. <CloudBadge/> <SelfHostedBadge/>
- [SSO and LDAP Login](../account/sso-ldap-login.md) added to Testing Distribution. <CloudBadge/> <SelfHostedBadge/>
- [Azure Boards](../integrations/azure-board.md) workflow step added. <CloudBadge/> <SelfHostedBadge/>
- [Repeato](../workflows/common-workflow-steps.md#repeato-mobile-test-automation) workflow step added. <CloudBadge/> <SelfHostedBadge/>
- [Snyk Secure Scan](../workflows/common-workflow-steps.md#snyk-scan-security) workflow step added. <CloudBadge/> <SelfHostedBadge/>

### :muscle: Improvement
- [Xcode Build for Simulator](../workflows/ios-specific-workflow-steps.md#xcodebuild-for-ios-simulator) workflow step updated. The new version allows you to create both x86_64 and arm64 simulator builds. This step can optionally install the simulator builds to run UI tests on the simulator. <CloudBadge/> <SelfHostedBadge/>
- [Test Report](../continuous-testing/running-ios-unit-and-ui-tests.md) step tries to parse JUnit files if it can't find .xctestresult files. This can be useful if your testing framework(BrowserStack, Repeato, etc.) is producing JUnit reports. <CloudBadge/> <SelfHostedBadge/>
- [Wait for Android Emulator](../workflows/android-specific-workflow-steps.md#wait-for-android-emulator) step updated to install optional APK after the emulator boots.  <CloudBadge/> <SelfHostedBadge/>
- The default Xcode version is bumped to 14.2 for new projects.  <CloudBadge/> <SelfHostedBadge/>
- Sub-organizations can see their download reports. <CloudBadge/> <SelfHostedBadge/>
- Build configuration screen is improved. Changing the tabs no longer resets the configuration. <CloudBadge/> <SelfHostedBadge/>
- Build trigger screen is improved. <CloudBadge/> <SelfHostedBadge/>
- [Self-hosted Runer](../self-hosted-appcircle/self-hosted-runner/installation.md) installation script updated for new Xcode versions and other tools. <SelfHostedBadge/>
- The default configuration file that contains [Self-hosted Server](../self-hosted-appcircle/install-server/docker.md) settings is simplified. <SelfHostedBadge/>
- The [Self-hosted Server](../self-hosted-appcircle/install-server/docker.md) package has a text file that contains a list of container services. <SelfHostedBadge/>
- [Self-hosted Server](../self-hosted-appcircle/install-server/docker.md) Podman support added. <SelfHostedBadge/>
- [Self-hosted Server](../self-hosted-appcircle/install-server/docker.md) installation script `version` command updated to fix Podman compatibility. <SelfHostedBadge/>
- New script added [Self-hosted Server](../self-hosted-appcircle/install-server/docker.md) installation package. This script allows users to add and trust their custom self-signed certificates. <SelfHostedBadge/>
- New script added [Self-hosted Server](../self-hosted-appcircle/install-server/docker.md) installation package. This script allows users to add and trust their custom self-signed certificates. <SelfHostedBadge/>

### 🐞 Fixed
- Strict URL check is removed when users try to add Azure repositories. <CloudBadge/> <SelfHostedBadge/>
- An error that was occurring when you tried to add a sub-org on self-hosted Appcircle is fixed. <SelfHostedBadge/>
- Some minor cases that were occurring on the [Self-hosted Server](../self-hosted-appcircle/install-server/docker.md)   boot process are fixed. <SelfHostedBadge/>

## 3.3.2 - 2023-05-10 - Xcode 14.3,FTP Upload 

### 🆕 New Feature
- [Xcode 14.3](../infrastructure/ios-build-infrastructure.md) added to build agents. Since Xcode 14.3 only runs on Ventura, M1 infrastructure is also updated. Please test your workflows extensively. <CloudBadge/> <SelfHostedBadge/>
- [FTP Upload](../workflows/common-workflow-steps.md#ftp-upload) workflow step added. <CloudBadge/> <SelfHostedBadge/>

### :muscle: Improvement
- [Data Theorem Mobile Secure](../workflows/common-workflow-steps.md#data-theorem-mobile-secure) workflow step updated. <CloudBadge/> <SelfHostedBadge/>
- New options added to [Android Resign](../distribute/resign.md). <CloudBadge/> <SelfHostedBadge/>
- Sub-organizations can see their download reports. <CloudBadge/> <SelfHostedBadge/>
- Build configuration screen is improved. Changing the tabs no longer resets the configuration. <CloudBadge/> <SelfHostedBadge/>
- Build trigger screen is improved. <CloudBadge/> <SelfHostedBadge/>

### 🐞 Fixed
- Fixed a bug that makes users unable to add their GitHub repositories. <CloudBadge/> <SelfHostedBadge/>

## 3.3.0 - 2023-04-27 - Data Theorem Mobile Secure, App Center CodePush

### 🆕 New Feature
- [Data Theorem Mobile Secure](../workflows/common-workflow-steps.md#data-theorem-mobile-secure) workflow step added. <CloudBadge/> <SelfHostedBadge/>
- [App Center CodePush](../workflows/react-native-specific-workflow-steps.md#app-center-codepush) workflow step added. <CloudBadge/> <SelfHostedBadge/>
- Latest five build status added to build profile. <CloudBadge/> <SelfHostedBadge/>
- [Slack Bot](../account/slack/appcircle-bot-for-slack.md) added. <CloudBadge/>

### :muscle: Improvement
- SVG images are updated <CloudBadge/> <SelfHostedBadge/>
- Build profile card design is improved. <CloudBadge/> <SelfHostedBadge/>
- Color scheme and icons are updated for dark themes. <CloudBadge/> <SelfHostedBadge/>
- Lots of UI and text improvements were made for better UX. <CloudBadge/> <SelfHostedBadge/>

### 🐞 Fixed
- [Huawei AppGallery](../store-submit/huawei-app-gallery.md) submission bug fixed.  <SelfHostedBadge/>
- [Enterprise Store](../enterprise-appstore/customize-ent-store.md) The background image bug was fixed on the login page. <SelfHostedBadge/>
- Fixed a bug that makes users unable to login to the enterprise app store in some cases. <CloudBadge/>
- Fixed a bug that gives an unexpected error on project `export` on self-hosted server installations. <SelfHostedBadge/>
- Fixed a bug that gives an unexpected error on project `up` when there is no vault image in the system. <SelfHostedBadge/>
- The default license duration for the self-hosted package is updated to 3 months for demo use cases. <SelfHostedBadge/>
- Fixed broken tag triggers which was missing to start build on some cases.  <CloudBadge/> <SelfHostedBadge/>
- Store submit workflows are updated for the latest Fastlane version. <CloudBadge/> <SelfHostedBadge/>

## 3.2.0 - 2023-04-07 - Resign, Sub Organizations

### 🆕 New Feature
- [Resigning](../distribute/resign.md) iOS and Android binaries added to Test Distribution module. <CloudBadge/> <SelfHostedBadge/>
- Enterprise customers can create [sub organizations](../account/my-organization.md) to manage their users. <CloudBadge/> <SelfHostedBadge/>
- [App Center iOS Distribution](../workflows/ios-specific-workflow-steps.md#app-center-ios-distribution) workflow step added. <CloudBadge/> <SelfHostedBadge/>
- [App Center Android Distribution](../workflows/android-specific-workflow-steps.md#app-center-android-distribution) workflow step added. <CloudBadge/> <SelfHostedBadge/>

### :muscle: Improvement
- Build profile list UI is improved <CloudBadge/> <SelfHostedBadge/>
- Extra notes added to [SSH](../build/adding-a-build-profile/connecting-to-private-repository-via-ssh.md) key generation for Windows users. <CloudBadge/> <SelfHostedBadge/>
- User's default branch is listed at the top. <CloudBadge/> <SelfHostedBadge/>

### 🐞 Fixed
- Gitlab double trigger bug fixed. <CloudBadge/> <SelfHostedBadge/>
- Gitlab Self-Hosted access token now longer shows inside build logs. <CloudBadge/> <SelfHostedBadge/>
- [Enterprise Store](../enterprise-appstore/customize-ent-store.md) 2FA Safari bug fixed. <SelfHostedBadge/>
- [Enterprise Store](../enterprise-appstore/customize-ent-store.md) localization bug fixed. <CloudBadge/> <SelfHostedBadge/>
- [Enterprise Store](../enterprise-appstore/customize-ent-store.md) Download bug is fixed for slow networks. <SelfHostedBadge/>


## 3.1.0 - 2023-03-17 - StoreSubmit, Self-hosted Improvements

### 🆕 New Feature
- Submissions to [Google Play Console](../store-submit/google-play.md) and [Huawei AppGallery](../store-submit/huawei-app-gallery.md) will now begin from the build agents. <CloudBadge/> <SelfHostedBadge/>
- It is now possible to localize some login form texts on the [Enterprise Store](../enterprise-appstore/customize-ent-store.md) when LDAP login is activated. <SelfHostedBadge/>

### :muscle: Improvement
- [Enterprise Store](../enterprise-appstore/customize-ent-store.md) language selection page is improved. <CloudBadge/> <SelfHostedBadge/>
- `AC_COMMIT_AUTHOR_EMAIL`, `AC_COMMIT_SUBJECT`, and `AC_COMMIT_MESSAGE` [Environment Variables](../environment-variables/appcircle-specific-environment-variables.md) added to build agents. <CloudBadge/> <SelfHostedBadge/>
- Unauthenticated internal SMTP server support added for Self-Hosted Appcircle. <SelfHostedBadge/>
- `global.yaml` content is improved with new configuration options. <SelfHostedBadge/> 
- Confusing initial `user-secret` file generation is removed. <SelfHostedBadge/> 
- New command line parameters added for Self-Hosted Appcircle CLI. <SelfHostedBadge/> 

### 🐞 Fixed
- Huawei AppGallery App ID saving bug fixed. <CloudBadge/> <SelfHostedBadge/>
- [Enterprise Store](../enterprise-appstore/customize-ent-store.md) 2FA login bug fixed. <CloudBadge/> <SelfHostedBadge/>
- Appcircle now shows a warning if it can't reach your repository due to network problems. <CloudBadge/> <SelfHostedBadge/> 
- Fixed broken downloads on Enterprise Store when an app has a name in non-ASCII characters. <CloudBadge/> <SelfHostedBadge/>
- Minor localization fixes were done on Enterprise Store for the Turkish language. <CloudBadge/> <SelfHostedBadge/>
- Minor fixes were done on SSH key format and SSH repo connections.  <CloudBadge/> <SelfHostedBadge/>
- Enterprise Store settings' broken UI fixed when the custom domain is disabled. <SelfHostedBadge/>
- Dashboard no longer shows builds started for store submission. <CloudBadge/> <SelfHostedBadge/>
- Dashboard no longer shows builds from deleted build profiles. <CloudBadge/> <SelfHostedBadge/>

## 3.0.1 - 2023-02-28 - AppSweep, Self-hosted Improvements

### 🆕 New Feature
- [AppSweep Mobile Security Testing](../workflows/android-specific-workflow-steps.md#appsweep-mobile-security-testing) component added. <CloudBadge/> <SelfHostedBadge/>
- [Self-signed certificate](../self-hosted-appcircle/configure-server/ssl-configuration.md) support added for Testing Distribution. <SelfHostedBadge/>
- [Enterprise Store](../enterprise-appstore/customize-ent-store.md) is now available in German and Turkish languages in addition to English. To switch to your preferred language, simply navigate to the language settings on your store homepage and select either German or Turkish. <CloudBadge/> <SelfHostedBadge/>
- [New APIs](https://api.appcircle.io/openapi/index.html?urls.primaryName=enterprisestore) are added to directly download IPA or APK files from Enterprise Store by using a PAT. <CloudBadge/> <SelfHostedBadge/>

### :muscle: Improvement
- New line is added to SSH private key if it doesn't exist. <CloudBadge/> <SelfHostedBadge/>
- API key selection is now mandatory for all app submissions on Google Play. <CloudBadge/> <SelfHostedBadge/> 
- Autofill button respects the selected pool. <CloudBadge/> <SelfHostedBadge/> 
- Self-hosted Gitlab onboarding screen is improved. <CloudBadge/> <SelfHostedBadge/> 
- Default pools are removed from Self-hosted instances. <SelfHostedBadge/> 

### 🐞 Fixed
- Email address parse error fixed for Distribution profiles. <CloudBadge/> <SelfHostedBadge/> 
- Test reports are correctly created for branches even if they don't have any configuration. <CloudBadge/> <SelfHostedBadge/> 
- Dashboard no longer shows builds started with autofill. <CloudBadge/> <SelfHostedBadge/>  
- Cache pull and Cache Pull components are fixed. <SelfHostedBadge/> 
- [Enterprise Store](../enterprise-appstore/customize-ent-store.md) live and beta channels access managament bug fixed <CloudBadge/> <SelfHostedBadge/>
- Store Submit permission bug fixed. <SelfHostedBadge/> 

## 3.0.0 - 2023-02-14 - LDAP, Self-hosted Improvements

### 🆕 New Feature
- [Multiple LDAP](../enterprise-appstore/customize-ent-store.md#ldap-login) support added for Enterprise Store. <CloudBadge/> <SelfHostedBadge/>
- [Self-signed certificate](../self-hosted-appcircle/configure-server/ssl-configuration.md) support added for Appcircle server. <SelfHostedBadge/>
- [Self-signed certificate](../self-hosted-appcircle/configure-server/ssl-configuration.md) support added for external services such as Git providers (Gitlab, Bitbucket etc.) <SelfHostedBadge/>

### :muscle: Improvement
- Onboarding of React Native Android project is improved.  <CloudBadge/> <SelfHostedBadge/>
- Flutter iOS build component improved. <CloudBadge/> <SelfHostedBadge/> 
- [Feedback form](https://my.appcircle.io/help) added to help section. <CloudBadge/> <SelfHostedBadge/> 
- CSS and icon handling is updated to improve the performance of the Enterprise Store. <CloudBadge/> <SelfHostedBadge/> 
- Self-hosted instances can be installed from a single Docker registry. <SelfHostedBadge/>
- Self-hosted instances can start without an active internet connection. <SelfHostedBadge/>
- Public and SSH repository options are added to default profile options. <SelfHostedBadge/>
- Improvements were made to the logging system to prevent big log files.  <SelfHostedBadge/>

### 🐞 Fixed
- Enterprise store cache related bugs were fixed. <CloudBadge/> <SelfHostedBadge/> 
- SMTP bugs were fixed for server notifications. <SelfHostedBadge/>

## 2.9.23 - 2023-02-02 - LDAP, Jira, Microsoft Teams

### 🆕 New Feature
- [LDAP Login](../enterprise-appstore/customize-ent-store.md#ldap-login) added to Enterprise Store.
- [Jira](../integrations/jira-integration.md) component added.
- [Microsoft Teams](../account/teams-notifications.md) integration added.
- [Gradle Runner](../workflows/android-specific-workflow-steps.md#gradle-runner) component added.
- [Maestro Cloud Upload](../workflows/common-workflow-steps.md#maestro-cloud-upload) component added.

### :muscle: Improvement
- UI improvements for the Enterprise Store login options.
- Build profile based device registration added to Ad Hoc provisioning profiles.

### 🐞 Fixed
- [iOS Version and Build Number Increment](../versioning/ios-version.md) component gracefully exits if it can't update the project.

## 2.9.22 - 2023-01-16 - Adhoc Improvements

### 🆕 New Feature
- [Apple Devices](../distribute/apple-devices.md) section will allow you to easily register new devices and add them to Ad Hoc provisioning profiles.
- [Firebase Deployment ](../workflows/common-workflow-steps.md#firebase-deployment) component added.

### :muscle: Improvement
- [Firebase App Distribution](../workflows/common-workflow-steps.md#firebase-app-distribution) component support service account.
- UI improvements for the custom script editor.

### 🐞 Fixed
- If you revert a commit and force push it, Appcircle will correctly handle this situation.

## 2.9.21 - 2022-12-28 - BrowserStack App Automate

### 🆕 New Feature
- [BrowserStack App Automate - Espresso](../workflows/android-specific-workflow-steps.md#browserstack-app-automate---espresso) component added
- [BrowserStack App Automate - XCUI](../workflows/ios-specific-workflow-steps.md#browserstack-app-automate---xcui) component added

### :muscle: Improvement
- Component YAML structure is improved. YAML files support markdown.
- UI improvements for the custom script editor.

### 🐞 Fixed
- `[retry]` comment now works on BitBucket. If your workflow failed, writing `[retry]` as a comment will start your workflow again.
- If the owner of the repository changes, you will see a new authentication dialog. After authentication, Appcircle will correctly refresh the token on behalf of the new user.
- Slack connection bug fixed.

## 2.9.20 - 2022-12-22 - Xcode 14.2, Google Play Draft Submission

### 🆕 New Feature
- Xcode 14.2 added to both Intel and M1 machines
- Submit Release as Draft. If your app has no presence on Google Play you may send it as a draft.

### :muscle: Improvement
- Repository connection errors are shown properly.
- UI improvements for Environment Variables and Testing groups.
- [Flutter Test Component](https://github.com/appcircleio/appcircle-flutter-test-component) creates a JUnit report which can be consumed by the [Test Report Component](https://github.com/appcircleio/appcircle-test-report-component).

### 🐞 Fixed
- `[skip ci]` commit message also works on Pull/Merge Requests. If you have open PR, sending a commit with `[ci skip]` or `[ci skip]` message will not trigger a workflow.
- [Test Report Component](https://github.com/appcircleio/appcircle-test-report-component) now handles multiple reports in the same folder.

## 2.9.19 - 2022-12-14 - Testinium and Firebase dSYM Upload components

### 🆕 New Feature
- [Testinium](../workflows/common-workflow-steps.md#testinium) component added. This component allows you to run your test plans on [Testinium](https://testinium.com)
- [Firebase dSYM Upload](../workflows/common-workflow-steps.md#firebase-upload-dsym) component added. You may use this component to upload Debug Symbols to Firebase.

### :muscle: Improvement
- Xcode and NodeJS version selection added to Smartface projects
- Help document links added to SSO section.

### 🐞 Fixed
- Github authentication issue is solved.
- Account delete bug fixed.
- Refresh button refreshes correctly and shows forced pushes as well.

## 2.9.18 - 2022-12-06 - M1 Machines

### 🆕 New Feature
- We have a big announcement today :tada: We have added an M1 Mac mini machines to our infrastructure and enabled them for every account. Both Android and iOS builds will benefit from the blazing fast M1 machines. We expect this change to be smooth for most of the users. Please be aware of the following issues.

**Firewall**:

If you’re using self hosted services and allowed Appcircle IPs in your firewall, you need to update your allowed IP list. Please check the following document.

<ContentRef url="/infrastructure/accessing-repositories-in-internal-networks-firewalls/">
Accessing Repositories in Internal Networks (Firewalls)
</ContentRef>

**Intel Pool**:

If your builds fail on M1 pool or if you’re not ready for the M1 migration, please go to your branch’s config screen and choose Default Intel Pool from the dropdown menu.

## 2.9.17 - 2022-12-01 - Test Reports

### 🆕 New Feature
- Test Reports added for [iOS](../continuous-testing/running-ios-unit-and-ui-tests.md) and [Android](../continuous-testing/running-android-unit-tests.md). Please check their documentation to learn how to set up your workflows.
- [Danger](../workflows/common-workflow-steps.md#code-reviews-with-danger) component added. Danger runs during your CI process and gives teams the chance to automate common code review chores 
- The emulator feature is removed.

### :muscle: Improvement
- Performance improvements for the Dashboard
- Announcement button ⚡️ added to Dashboard. You can check that section for product announcements.
- Wildcard Provisioning Profile support for manual code signing
- Setting environment variables via the `AC_ENV_FILE_PATH` environment variable now works on failed steps as well.
- Xcode versions older than 12.5 removed.

## 2.9.16 - 2022-10-07 - Triggers fallback config, Netrc, Bundlletool and Detekt components

### 🆕 New Feature
- [Fallback config](../build/build-manually-or-with-triggers.md) added for Pull/Merge Requests and Tag triggers.
- [Netrc component](../workflows/common-workflow-steps.md) You can use this component to add credentials for hosts such as your repositories or external hosts.
- [Bundletool Component](../workflows/android-specific-workflow-steps.md) You can use this component to create universal apk from the aab.
- [Detekt](../workflows/android-specific-workflow-steps.md) You can use this component to run your detekt gradle task.

### :muscle: Improvement
- [Added FAQs](../troubleshooting-faq/common-issues.md) related to Xcode 14 and code signing errors.

## 2.9.15 - 2022-09-30 - Fortify On Demand and Firebase App Distribution components

### 🆕 New Feature
- [Fortify On Demand Component](../workflows/common-workflow-steps.md) You can use Fortify On Demand uploader for all your projects.
- [Firebase App Distribution Component](../workflows/common-workflow-steps.md) You can use Firebase App Distribution to distribute your builds.
- [Wait for Android Emulator](../workflows/android-specific-workflow-steps.md) You must use this step before your UI tests to wait for the Android emulator to start.

### :muscle: Improvement
- Navigation and repository refresh speed improved.,
- Linux agents are more powerful now. They also support nested virtualizations therefore you may use Android emulators.
- Xcode default version number is changed to 13.4.x
- Android Emulator added to agents. The added emulator is based on Android 9.0 image. You may install additional emulators by using `sdkmanager`. Please check [Android Infrastructure](../infrastructure/android-build-infrastructure.md) to learn more. In order to use the emulator, you need to add the Wait for Android Emulator step to your workflow.

### 🐞 Fixed
- Bitbucket commit messages now show properly.
- `AC_PULL_NUMBER` environment variable added for Pull/Merge Requests.
- Changing assignee no longer triggers a build for Gitlab Merge Request.
- Build statuses correctly shows on the main dashboard.

## 2.9.14 - 2022-08-18 - New Dashboard, Appium Server and SwiftLint components

### 🆕 New Feature
- [New Dashboard](https://my.appcircle.io) Appcircle has a brand new dashboard that shows an overview of your account.
- [Artifacts Management](../account/artifacts.md) You can set the retention period for your build artifacts.
- [Appium Server Component](../workflows/common-workflow-steps.md) You can use Appium Server for iOS and Android projects.
- [SwiftLint Component](../workflows/ios-specific-workflow-steps.md) You can use Swiftlint for iOS projects.

### :muscle: Improvement
- Empty states are added for all modules.
- [Self-Hosted Runners](../self-hosted-appcircle/self-hosted-runner/overview.md) Self hosted documentation updated.
- Docs updated to Docusaurus v2.0.1

### 🐞 Fixed
- Sharing Simulator URL fixed.

## 2.9.13 - 2022-07-27 - Self-hosted Runners, Artifacts Management, Automatic iOS Code Signing

### 🆕 New Feature
- [Self-Hosted Runners](../self-hosted-appcircle/self-hosted-runner/overview.md) Self-hosted runner enables you to use your own systems and infrastructure for running Appcircle build pipelines. 
- [Automatic iOS Code Signing](../signing-identities/ios-certificates-and-provisioning-profiles.md) If you're using Xcode 13 or later, you can now use the automatic code signing option to automatically sign your iOS apps.
- [Artifacts Management](../account/artifacts.md) You can set the retention period for your build artifacts.
- [SonarQube Component](../workflows/common-workflow-steps.md) You can use SonarQube for iOS and Android projects.

### :muscle: Improvement
- Slack messages updated to include store name and distribution links.
- Android v2 signing support improved.

### 🐞 Fixed

- `Get help with build errors` link fixed.
- Renaming build profiles fixed.

## 2.9.12 - 2022-07-07 - Android Version Management, Enterprise Store Improvements

### 🆕 New Feature

- [Android Versioning](../versioning/android-version.md) You can manage version code and version name directly with UI.
- [Enterprise Store](../enterprise-appstore/customize-ent-store.md) You can change the display picture of your apps.

### :muscle: Improvement
- Added Open menu to actions list on build profiles.
- [Enterprise Store](../enterprise-appstore/enterprise-reports.md) App usage reports update more frequently.
- [My Organization](../account/my-organization.md) Access Management document updated.

### 🐞 Fixed

- Creating a new branch without a commit was not triggering a build. This is fixed.
- SSO UI issues fixed
- Android Build Tools 31.0.0 corrupted error message fixed.

## 2.9.11 - 2022-06-20 - Release Notes Component, Enterprise Store Improvements

### 🆕 New Feature

- [Release Notes Component](../integrations/managing-release-notes.md) You can create release notes with Publish Release Notes component.
- [Enterprise Store](../enterprise-appstore/customize-ent-store.md) Certificate Details added to Enterprise Store.
- [Enterprise Store](../enterprise-appstore/enterprise-reports.md) Detailed reports are added to Enterprise Store.
- [Open API](https://api.appcircle.io/openapi/index.html?urls.primaryName=signing-identity) New API endpoints added to Certificate and Provisioning profiles upload.
- [Open API](https://api.appcircle.io/openapi/index.html?urls.primaryName=build) New API endpoint added to start a build with provided environment variables.

### :muscle: Improvement
- [iOS Stack](../infrastructure/ios-build-infrastructure.md) Monterey is upgraded to 12.4 for macOS agents.
- Log window is improved. It is more performant and stable.
- Added [FAQ section](../troubleshooting-faq/common-issues.md#issues-in-connecting-to-the-repositories-with-ssh) for multiple SSH keys.

### 🐞 Fixed

- Store Submit logs show properly.

## 2.9.10 - 2022-05-31 - iOS Version Management, Enterprise Store Customizations

### 🆕 New Feature

- [Enterprise Store Customizations](https://docs.appcircle.io/enterprise-appstore/customize-ent-store). You can connect your subdomain as Enterprise Store.
- [NodeJS Version Selection](https://docs.appcircle.io/build/building-react-native-applications#build-configuration-for-react-native-ios-applications) You can now directly set the NodeJS version on config screen.
- [Flutter Version Selection](https://docs.appcircle.io/build/building-flutter-applications#how-to-set-a-specific-flutter-version-for-the-build) You can now directly set the Flutter version on the config screen.
- [iOS Versioning](https://docs.appcircle.io/versioning/ios-version) You can manage build and version numbers directly with UI.

### :muscle: Improvement
- [Android Stack](https://docs.appcircle.io/infrastructure/android-build-infrastructure) Android Build Infrastructure updated. Now the default JAVA version is 11.
- [iOS Stack](https://docs.appcircle.io/infrastructure/ios-build-infrastructure) iOS Build Infrastructure updated. Xcode 13.4 added to iOS agents.
- [Workflow Management](https://docs.appcircle.io/workflows/why-to-use-workflows#setting-up-workflows) You can now import or export your workflows as a YAML file.
- [Appcircle CLI Update](https://www.npmjs.com/package/@appcircle/cli) Getting Live and Beta versions added to CLI.
- When you download the logs, the profile and branch names will be added to the file name.

### 🐞 Fixed

- Browser UI issues fixed

## 2.9.2 - 2022-03-16 - SSO Login for Enterprise, Cached Builds

### 🆕 New Feature

- [SSO Login](https://docs.appcircle.io/account/sso/single-sign-on) is now available for all Enterprise accounts. You can connect your SAML and OpenID Provider right now!
- [Cached Builds](https://docs.appcircle.io/workflows/common-workflow-steps/#cache-push) are available to all. You can now use the Cache Push and Cache Pull components on your workflows to cache your dependencies and speed up your builds.

### 🐞 Fixed

- Browser UI issues fixed


## 2.9.1 - 2022-02-07 - Huawei AppGallery, New Components, Improved Triggers

### 🆕 New Feature

- [Huawei App Gallery](https://docs.appcircle.io/store-submit/huawei-app-gallery) support added. You can submit your apk or aab files to Huawei AppGallery.
- Java 11 added to iOS agents
- [Slather](https://docs.appcircle.io/workflows/ios-specific-workflow-steps#slather),[Tuist](https://docs.appcircle.io/workflows/ios-specific-workflow-steps#tuist) and Badge components added
- You can now see all your running builds from the status bar and cancel them.
- [Skip the Workflow](https://docs.appcircle.io/build/build-manually-or-with-triggers/#skipping-a-workflow) if the commit message includes `[skip ci]` or `[ci skip]`
- [Retry Merge/Pull Request workflow](https://docs.appcircle.io/build/build-manually-or-with-triggers/#retrying-a-workflow) if the comment includes `[retry]`

### :muscle: Improvement

- [Triggers updated](https://docs.appcircle.io/build/build-manually-or-with-triggers/#auto-build-on-every-push). You can use a default config for new branches. You no longer need to configure every branch. 
- [New environment variables](https://docs.appcircle.io/environment-variables/appcircle-specific-environment-variables/) added for commit message, build number, PR number, time stamp. 
- You can now download build logs directly from the menu.
- [Node Install](https://docs.appcircle.io/workflows/react-native-specific-workflow-steps#install-node) step uses `lts` version as default. 
- Error messages are clarified for build permissions. 

### 🐞 Fixed

- Gitlab Merge Request Webhook fixed
- Browser UI issues fixed
- Sometimes progress bar was showing on the wrong branch. Fixed.

### 📑 Documentation

- Added [Huawei App Gallery](https://docs.appcircle.io/store-submit/huawei-app-gallery) section for sending your apps to Huawei App Gallery.
- Added [Huawei App Gallery](https://docs.appcircle.io/account/adding-huawei-api-key) section for creating Huawei App Gallery API Key.
- Added [FAQ section](https://docs.appcircle.io/troubleshooting-faq/common-issues#cocoapods-errros-due-to-version-mismatch) for Cocoapods version.
- Added [FAQ section](https://docs.appcircle.io/troubleshooting-faq/common-issues#provisioning-profile-error) for Provisioning Profiles.
- Added [FAQ section](https://docs.appcircle.io/troubleshooting-faq/common-issues#missing-entitlements) for Missing Entitlements​
- Added [FAQ section](https://docs.appcircle.io/troubleshooting-faq/common-issues#gradle-build-after-bintray-shutdown) for Bintray deprecation
- Added [FAQ section](https://docs.appcircle.io/troubleshooting-faq/common-issues#no-pubspecyaml-file-found-error) for Flutter build errors
- Added [FAQ section](https://docs.appcircle.io/troubleshooting-faq/common-issues#file-not-found-error) for Flutter file naming errors
- Added [FAQ section](https://docs.appcircle.io/troubleshooting-faq/common-issues#firebase-version) for Flutter Firebase version
- Added [FAQ section](https://docs.appcircle.io/troubleshooting-faq/common-issues#err_ossl_evp_unsupported) for React native apps

## 2.9.0 - New Build Profile Detail UI, Better Artifact Upload Times

### 🆕 New Feature

- We have a brand new build profile detail UI! This new UI aims ease the access to workflows and triggers. It also has some improvements on onboarding.

### :muscle: Improvement

- Improved typography throughout the app. Working on more improvements and UI changes.
- We've improved artifact upload times drastically.

### 🐞 Fixed

- Fixed an issue where build logs were cut in half when multiple browser tabs were displaying the same build logs.

## 2.8.0 - 2021-10-25 - Improved Build Logging, Refresh Repository Connection, Persistent Notifications

### 🆕 New Feature

- A branch or a commit is missing? You can refresh repository connections for GitLab, GitHub, and Bitbucket repositories. Just look for the refresh icon on top of the branch list.

### :muscle: Improvement

- Build Notifications will sync between browsers and devices now.
- Removed unnecessary version texts from build steps on log panels.
- Build logging is improved for larger projects that have half a million lines of build logs.

### 🐞 Fixed

- Sometimes recent build logs were not displaying properly. Fixed.
- Branch pinning was not syncing between browsers.
- Some users weren't able to display the build artifacts after a successful build. It happened on way old builds too. Now they are accessible.
- Slack Distribution notifications didn't include platform info. Now they do and they won't look like double notifications for builds that have multiple distribution configs.
- Some large builds were uploading their artifacts very slowly. Now they are much faster.

## 2.7.0 - 2021-09-29 - Xcode 13.0 Support, Carthage on Workflows, Renaming Workflow Steps

### 🆕 New Feature

- You can now rename workflow steps.
- Carthage Dependency Manager for iOS is available as a workflow step
- Xcode 13.0 Public release is available.

### :muscle: Improvement

- We've added build number next to version number on artifacts distributed to testers.
- Improved commit and build listing for very large projects.
- Added iPhone 12 to emulator module.
- Improved iOS certificate and provisioning profile matching algorithm.
- Workflow name added as the title of the build logs detail screen.
- Small UI improvements

### 🐞 Fixed

- Fixed a bug where pasting SSH private key would add newlines to the key.;
- Fetch details on branch config defaults to Xcode 12.5.x instead of 12.0.
- Custom script workflow step didn't select any language initially. It selects bash now.
- Fixed some merge commits not triggering auto-build issue.
- Fixed an issue where workflow starting time was different from the user's local time.

## 2.6.0 - 2021-09-14 - Easier iOS Certificate and Provisioning Profile Management, Flutter 2.5.0 Support

With this release, we're adding the ability to connect to Apple for easier iOS Certificate and Provisioning Profile management. You can now add an App Store Connect API Key to your account and with it, Appcircle will list all the certificates and provisioning profiles you have on your Apple Developer account.

To set up an API Key, check this guide:

<ContentRef url="/account/adding-an-app-store-connect-api-key">Adding an App Store Connect API Key</ContentRef>

After adding an API Key, you can add new signing identities from the Signing Identities section. For more information on how to add identities and use them, check out [Signing Identities guide](https://docs.appcircle.io/signing-identities/ios-certificates-and-provisioning-profiles#1-get-ios-certificates-and-provisioning-profiles-from-apple).

### 🆕 New Feature

- Flutter version `2.5.0` is released in their stable channel. You can now use this latest stable version on Appcircle.

## 2.5.0 - 2021-08-27 - Two Factor Authentication, Self Hosted Gitlab and Bitbucket, Xcode 13 Beta 5

Within this release, we bring fully built-in Appcircle support for your Self Hosted (Enterprise) for:

- [Bitbucket Self Hosted](https://docs.appcircle.io/build/adding-a-build-profile/connecting-to-bitbucket#connecting-to-bitbucket-self-hosted-repository)
- [GitLab Self Hosted](https://docs.appcircle.io/build/adding-a-build-profile/connecting-to-gitlab#connecting-to-gitlab-self-hosted-repository)

solutions. Click on them to see how to connect your self hosted repository within Appcircle!

:::info

### Notice about GitHub OAuth

Appcircle removed GitHub OAuth connection support in the new connections. Starting from this release, the new connections will only be using GitHub App.

Your current GitHub OAuth connection will stay as is. However, Appcircle recommends you to switch to GitHub app for better support.

:::

:::caution

### Disclaimer for React Native Users

The default Node version which Appcircle uses to build React Native apps are upgraded from v13 to v16. If your app relies on v13 or another specific version of Node, [refer to this documentation](https://docs.appcircle.io/workflows/react-native-specific-workflow-steps#install-node) to configure your node version. You can change your node version on your workflow settings at **Install Node** step.

:::

If your app targets Android 11, please read the following documentation to enable V2 Signing in your Build Profile:

https://docs.appcircle.io/build/building-android-applications/android-signing-for-google-play#enable-v2-sign-in-appcircle

### 🆕 New Feature

- iOS builds will be using Xcode 13 Beta 5 if 13.0.x is selected as Xcode version.
- Appcircle is now more secure with Two Factor Authentication 🔒 Refer to [this documentation](https://docs.appcircle.io/account/my-account/authenticator-two-factor-authentication) to secure your account 🔑
- Appcircle now supports Android V2 Signature Scheme out of the box.;

### :muscle:Improvement

- Repository Connection now has a new look and feel! Refer to [this documentation](https://docs.appcircle.io/build/adding-a-build-profile#connect-your-repository) to see the new connection screens or dive right into the connection module to check our new simplified experience!

### 📑 Documentation

- If you use a single profile to produce multiple apps, we have written a [new documentation](https://docs.appcircle.io/building-multiple-apps-in-one-profile) about how to utilize your Product Variants(Android) or Multiple Targets(iOS) within Appcircle!

## 2.4.0 - 2021-07-30 - Xcode 13 Beta 4 & Manual Build Workflow Select;

This release focuses on stability with optimizing the logging of the builds.

Within this release as prior to the previous release, Appcircle also supports [Xcode 13 Beta 4](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-13-beta-release-notes). When 13.0.x from the Xcode Version is selected, the Xcode version will be Xcode 13 Beta 4.

### 🆕 New Feature

- iOS builds will be using Xcode 13 Beta 4 if 13.0.x is selected as Xcode version.
- Added metadata (Organization ID, OS version etc.) at the beginning of the Build Logs
- While manually building the workflow, Appcircle now lets you choose which workflow to trigger:

![](<https://cdn.appcircle.io/docs/assets/image (215).png>)

### :muscle:Improvement

- Commit Status on PR/CR is more detailed than before, you can track your progress(not only fail/success) as well, integrated with CI/CD progresses of the repository providers. More info is located at [Sending the build status to repository providers](https://docs.appcircle.io/build/building-ios-applications#sending-the-build-status-to-the-repository-providers) documentation

### 🐞 Fixed

- Fixed a bug that on **Save **button not being activated while chaning config values on Store Submit;
- Fixed a bug that the build tab was showing an empty column when the branch is deleted
- \[UI] Fixed the style of Delete button on the version list of Testing Distribution

### ; 📑 Documentation

- Added [FAQ section](https://docs.appcircle.io/troubleshooting-faq/common-issues#artifact-storage-is-full) of how to delete old artifacts.
- Improved [Sending the build status to repository providers](https://docs.appcircle.io/build/building-ios-applications#sending-the-build-status-to-the-repository-providers) section for better CI/CD pipeline tracking.

## 2.3.0 - 2021-06-28 - Xcode Version Updates

Within this release, Appcircle now supports [Xcode 13 Beta 2](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-13-beta-release-notes). When 13.0.x from the Xcode Version is selected, it will be using Xcode 13 Beta 2.

### 🆕 New Feature

- iOS builds will be using Xcode 13 Beta 2 if 13.0.x is selected as Xcode version.
- iOS builds will be using Xcode 12.5.1 if 12.5.x is selected as Xcode version.
- Google Play Store submit now supports internal channel uploads.

### :muscle:Improvement

- New profiles with Flutter iOS will have `--no-codesign`\*\* \*\*and `--verbose` parameters as default for easier debugging.;
- Increased allocated size over each build, now you can build bigger projects on Appcircle 🎉
- Further optimizations towards Android side of builds. Build times are considerably faster on Android 🎉
- The Date\&Time which Appcircle uses on their logs now will show the local time instead of the server time.
- Code gloss-over for [Appcircle CLI](https://www.npmjs.com/package/@appcircle/cli).
- If you are using an internal network, check the IP addresses you need whitelist through the document below:

<ContentRef url="/infrastructure/accessing-repositories-in-internal-networks-firewalls">
  Accessing Repositories in Internal Networks (Firewalls)
</ContentRef>

### 🐞 Fixed

- Fixed a bug that **Config **section appearing disabled when connected to the repository for the first time
- Fixed a bug that causes Store Submit modules to not show correct progress while the upload is in progress.
- Fixed a bug that Copy\&Set Configurations not working properly on **Smartface Android **profiles**.**

### 📑 Documentation

- Added [React Native Specific FAQ](https://docs.appcircle.io/troubleshooting-faq/common-issues#react-native-specific-issues) section

## 2.2.0 - 2021-06-16 - Xcode Version and CLI Improvements

This release includes the new Xcode 13.0, a new CLI look\&feel and marketplace to peek workflows as a bulk.

:::caution

### Important Update for iOS Developers

Since April 26, Apple removed the support of Store Submission for pre Xcode 12.0 and iOS SDK 14.0 compiled apps. Make sure that your Xcode version is greater or equal to Xcode 12.0 under your repository config.

More info is located under: [https://developer.apple.com/news/?id=ib31uj1j](https://developer.apple.com/news/?id=ib31uj1j);

:::

### 🆕 New Feature

- You can specify which Xcode version to use on your builds. This can also be specified on the repository and will be seamlessly fetched from the relevant repository during the **Fetch Details** Process. Available versions: 13.0, 12.5, 12.4, 12.3, 12.2, 12.1, 12.0, 11.7, 11.6, 11.5, 11.4, 11.3, 11.2, 11.1 and 11.0
  - Latest Xcode 13 beta is used on 13.0.x
- [Appcircle CLI ](https://www.npmjs.com/package/@appcircle/cli)has a fresh look\&feel and lots of new features along with it.
- [Export Build Artifacts](https://docs.appcircle.io/workflows/common-workflow-steps#export-build-artifacts) has been added for a separate step. You can remove this step and upload your files elsewhere if your artifacts have a need to be on-premise.
- [Setting build status](https://docs.appcircle.io/build/building-ios-applications#sending-the-build-status-to-the-repository-providers) updates to the repository providers - You can now send updates about a commit to the repository providers for a complete CI/CD experience.
- A new workflow setting, **Always run this step even if the previous steps fail** has been added. The steps which have this enabled will always run.
- [Appcircle Marketplace](https://www.appcircle.io/integrations/) has been released. Checking which features are supported built-in has never been easier!

### :muscle:Improvement

- iOS Build Servers are optimized to reduce the queue time & better performance.
- Added better icons for Git providers when connecting to the repository.
- Whitelist IPs are under update process, you can follow the process under [Accessing Repositories in Internal Networks](https://docs.appcircle.io/infrastructure/accessing-repositories-in-internal-networks-firewalls/) document.

### 🐞 Fixed

- Fixed a bug that the same commit not appearing on multiple branches.
- Fixed a bug that new SSH connections being unable to fetch config.;

## 2.1.5 - 2021-05-10 - GitHub App for Repository Connections

This release includes the release of Appcircle GitHub app and the share app previews along with feature improvements.

### 🆕 New Feature

- [Appcircle GitHub App](../build/adding-a-build-profile/connecting-to-github.md)  - You can now connect to GitHub with the Appcircle GitHub app as an alternative to the oAuth connection.
- [Share App Preview Links](../distribute/create-or-select-a-distribution-profile.md#auto-send-your-build-to-the-testers) - You can now share in-browser app preview links automatically with the testers as an alternative to app binaries. No physical device needed for testing.

### :muscle:Improvement

- Improved new workflow addition;
- New status bar for live build tracking and quick team switching
- Workflow and trigger user interface improvements

### 🐞 Fixed

- Workflow and trigger fixes
- User interface fixes
- Entity deletion fixes

## 2.1.0 - 2021-04-23 - Repo-Level Workflows and PR/MR Triggers

This is a major release with the complete revamp of the build workflows and autobuild triggers for repository-level workflows and triggers along with the new PR/MR trigger option.

### 🆕 New Feature

- [Repository-level workflows](../workflows/why-to-use-workflows.md) - You can now define multiple workflows in a build profile and assign them to multiple branches or assign multiple workflows to the same branch. You can also clone workflows for easier management.
- [Repository-level triggers](../build/build-manually-or-with-triggers.md) - You can now specify triggers in the build profile level with wildcards for branch names and workflow selection for each trigger for higher flexibility and manageability of the build profiles.
- [Pull request/merge request triggers](../build/build-manually-or-with-triggers.md#auto-build-pullmerge-requests) - You can now trigger builds whenever you initiate a pull request or merge request from a source branch to the target branch. The build will be done with the pull/merge result. This allows testing the PR/MR result before the actual approval of the request.

### :muscle:Improvement

- Under-the-hood improvements for logging and user authentication
- User interface improvements
- Performance improvements

### 🐞 Fixed

- License management fixes
- User interface fixes

## 2.0.0 - 2021-03-21 - Appcircle CLI and the New Customer Portal

This major release introduces the Appcircle CLI and a new customer portal for billing and plan management along with the Appcircle distribute API.

### 🆕 New Feature

- Appcircle CLI - You can now access the Appcircle platform from the command line for custom pipelines or advanced automation use cases. [Appcircle CLI is available on npm](https://www.npmjs.com/package/@appcircle/cli).
- Appcircle Distribute API - On top of the previously released build APIs, the distribute module APIs are now available for programmatic access.
- New Customer Portal - Billing and plan management is now easier and more flexible with the new customer portal.

### :muscle:Improvement

- Account and organization deletion improvements
- Plan upgrade and downgrade improvements

### 🐞 Fixed

- Webhook trigger fixes
- Emulator/simulator issue reporting fixes
- API and API portal fixes

## 1.7.0 - 2021-03-07 - Appcircle Build API and Experience Improvements

This release introduces the Appcircle API with the build module and all around experience features in various areas.

### 🆕 New Feature

- Appcircle API - You can now utilize the Appcircle API for programmatic access to the platform features. This release includes the build module APIs.
- Personal Access Token - You can generate a token to access the Appcircle API
- Webhook support for AWS CodeCommit and Azure DevOps git repositories
- In-browser emulator/simulator rotation and restart features
- In-browser emulator/simulator issue reporting - You can now share screenshots and notes over email while running an app preview.
- System message trace ID - You can now get the trace ID for each system message for easier troubleshooting.;

### :muscle:Improvement

- Flutter 2.0 support
- Organization ID management improvements
- Webhook URL management improvements
- Logging and reporting optimizations

### 🐞 Fixed

- Webhook support fixes
- SSH connection fixes
- Failed plan upgrade payment fix

## 1.6.0 - 2021-02-09 - Replicate Configuration, Git Webhooks and Advanced Role Management

This release introduces the two most requested features along with the enterprise-grade role management.

### 🆕 New Feature

- Copy/Set Branch Configuration - You can now copy the configuration from a branch to other branches in the same build profile for easy replication of the same configuration.;
- Webhooks for Git - With the webhook support for the compatible git providers, you can enable build triggers through SSH connections without the need for app authorization
- Advanced Role Management - You can now set submodule based access;

### :muscle:Improvement

- Branch list viewing improvements
- SSH connection improvements
- User interface optimizations

### 🐞 Fixed

- Slack notification fixes
- Environment variable management fixes
- User interface fixes
- License limit and access fixes

## 1.5.0 - 2021-01-22 - Slack Notifications for All Modules

This release includes support for Slack notifications for the major events in all modules along with minor features and fixes.

### 🆕 New Feature

- Slack Notifications for All Modules - You can now get notified for Signing Identity, Distribute and Store Submit module events through Slack (in addition to the Build module).;
- Storage Management - You can now delete build artifacts and app versions in select plans.
- Branch Pinning in Build Profiles - You can pin the primarily used branches in build profiles for easy access.

### :muscle:Improvement

- Artifact and binary management improvements
- Slack notification improvements
- Third-party connections management improvements
- Improved FAQ and troubleshooting
- User interface improvements towards better guidance

### 🐞 Fixed

- User interface issues in Safari
- Repository connection issues
- App preview sharing fixes

## 1.4.0 - 2020-12-08 - Auto Store Deployments and Emulator Starter Plan;

This release includes the automatic public store deployment feature and the introduction of a new Starter-based upgrade plan for higher Emulator/Simulator minutes.

### 🆕 New Feature

- Auto deployment to the Store Submit Module - You can now deploy your builds automatically to the Store Submit Module by enabling the setting in the build configuration
- Auto upload to Public Stores - You can now upload deployed apps automatically to Google Play Console and App Store Connect
- New Emulator Plan - This plan provides additional emulator minutes over the Starter plan, mainly for the standalone emulator/simulator users.

### :muscle:Improvement

- Store Submit Module improvements
- Configuration tab in Smartface projects
- Under-the-hood Standalone Emulator/Simulator improvements
- Billing and plan info view improvements

### 🐞 Fixed

- Public store credential management fixes
- Various user interface fixes
- Standalone Emulator/Simulator fixes

## 1.3.0 - 2020-11-16 - Maintenance Update

This release is a maintenance update with all around improvements.

### 🆕 New Feature

- Direct signing identity uploads in the build module - You can add signing identities directly from the build configuration if the signing identities module is empty.

### :muscle:Improvement

- Reporting improvements
- Standalone Emulator interface improvements
- App sharing interface improvements
- File size display and upload dialog improvements
- Various user interface improvements

### 🐞 Fixed

- Repository connection fixes
- Preview on device report update period fix
- Emulator share link error state fix
- Emulator share expiry duration fix
- Plan limit update fixes
- Various user interface fixes

## 1.2.0 - 2020-10-27 - Standalone Emulator/Simulator

This release includes the new in-Browser Emulator/Simulator module and Amazon Device Farm Support.

### ;🆕 New Feature

- Standalone Emulator for web sites and app uploads - You can now use the "Preview on Device" feature as a standalone module with support for direct uploads and web site previews.
- Device preview share - Just like sending apps to the testers, you can now share in-browser app preview links with the testers.
- AWS Device Farm Support - AWS Device Farm is now available as a workflow step. You can deploy apps to AWS Device Farm and run tests as a part of your pipeline.

### :muscle:Improvement

- Billing-related improvements
- Preview on device fixes in line with the Standalone Emulator
- Android 11 and iOS 14 support in device previews

### 🐞 Fixed

- GitLab branch listing fix
- Large file upload fix
- Further environment variables module fixes

## 1.1.0 - 2020-10-12

This release includes experience improvements along with support for Flutter Web builds.

### ;🆕 New Feature

- Flutter Web Support - You can now build your Flutter Web apps along with Flutter iOS and Android apps.
- Centralized Credentials for Store Uploads - for Google Play and App Store Connect uploads, the credentials can now be saved for reuse.
- Apple ID with App-specific password support for App Store Connect uploads.;

### :muscle:Improvement

- Improved multi-provisioning profile support (e.g. for Apple Watch builds) in iOS builds
- User experience improvements in the Store Submit module
- User experience improvements in the Environment Variables Module

### 🐞 Fixed

- Theme-related UI fixes
- Store upload fixes
- Environment variables module fixes
- Further state preservation fixes

## 1.0.0 - 2020-09-23 - Initial Release

We are excited to announce that Appcircle beta is complete and it is fully released with version 1.0. You can now use Appcircle with full set of features.

This is of course just a start of a long journey. Follow us on Twitter [@appcircleio](https://twitter.com/appcircleio) for updates.

For any questions, feedback or feature requests, just drop us a message using the in-app messaging or raise an issue in Appcircle GitHub: [https://github.com/appcircleio](https://github.com/appcircleio)

### ;🆕 New Feature

- Send apps to Public Stores - You can now send your apps to App Store Connect through the App Store Connect API.;
- Theme support with Dark Mode - There is an Appcircle for everyone. You can now select between Light, Dark and the Darker modes.
- Upload to Amazon S3 step - You can now deploy any file or folder to an Amazon S3 bucket with the new workflow step.

### :muscle:Improvement

- Xcode 12 GM support;
- User experience improvements in line with the theme support

### 🐞 Fixed

- Multimodule support fix
- Billing plan fixes
- State preservation fixes
