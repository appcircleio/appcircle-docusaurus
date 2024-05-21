---
title: Latest Release Notes
description: Appcircle release notes
tags: [release notes]
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

<!-- Note to contributors: You can use the following badges to indicate the availability of the feature for modules.-->

<!-- <BuildBadge/> <APICLIBadge/> <BuildIntegrationsBadge/> <ContinuousTestingBadge/> <EnvironmentVariablesBadge/> <VersioningBadge/> <AccountBadge/> <BestPracticesBadge/> <DistributionBadge/>
<IntegrationsBadge/> <EnterpriseStoreBadge/> <FaqBadge/> <InfrastructureBadge/> <PublishBadge/> <ReportsBadge/> <SigningIdentitiesBadge/> <SelfHostedBadge/> <PublishIntegrationsBadge/> -->

# Latest Release Notes

## 3.17.0 - 2024-05-17 - LDAP Mapping Improvements, Publish Module Bug Fixes, and more

### 🆕 New Features

- Users can now automate [Group](https://docs.appcircle.io/self-hosted-appcircle/configure-server/integrations-and-access/ldap-settings#managing-ldap-groups-and-mappings) and [Role](https://docs.appcircle.io/self-hosted-appcircle/configure-server/integrations-and-access/ldap-settings#ldap-role-mapping) Management using LDAP Authentication for Appcircle Login in Self-Hosted environments. <SelfHostedBadge/>
- We have introduced the [Team Activity Log](https://docs.appcircle.io/account/my-organization/team-activity-log) feature within the Organization settings. This feature enables users to monitor team management actions within their organization if they are the organization owner or have the Organization Management role. <CloudBadge/> <SelfHostedBadge/>
- The self-hosted Appcircle server now has a new configuration at `global.yaml` that helps you [enable or disable](https://docs.appcircle.io/self-hosted-appcircle/configure-server/monitoring#disable-the-monitoring-services) the log monitoring feature on demand. <SelfHostedBadge/>

### :muscle: Improvements

- The "Get Approval via Email" component now allows you to view the statuses of all users in its logs. <PublishBadge/> <CloudBadge/> <SelfHostedBadge/>
- We have added an activity log for updates to Release Notes on the [Metadata Information](https://docs.appcircle.io/publish-module/publish-information/meta-data-information) page within the Publish Module. <PublishBadge/> <CloudBadge/> <SelfHostedBadge/>
- Self-hosted users can now choose to hide the Change Password option in the account settings page by disabling the Forgot Password option in Self-Hosted Settings. <SelfHostedBadge/>
- We have added the ability for Jira Enterprise users to choose the API version.The [Jira Comment](https://docs.appcircle.io/workflows/common-workflow-steps/jira-comment) workflow step now supports both Jira Cloud and On-Prem use cases for both Jira API v2 and v3, which makes the integration more flexible. <BuildIntegrationsBadge/> <CloudBadge/> <SelfHostedBadge/>
- We have updated the documentation links on the workflow steps to enable users to access the most current and detailed documents for integration purposes. <BuildIntegrationsBadge/> <CloudBadge/> <SelfHostedBadge/>

### 🐞 Fixes

- Performance improvements have been made on the [Testing Distribution Portal](https://docs.appcircle.io/distribute/testing-management/downloading-binaries). <DistributionBadge/> <CloudBadge/> <SelfHostedBadge/>
- If the **Auto-Register** feature is disabled on the [Testing Distribution Profile](https://docs.appcircle.io/distribute/create-or-select-a-distribution-profile), the **Register Device** button will now be hidden on the [Testing Distribution Portal](https://docs.appcircle.io/distribute/testing-management/downloading-binaries). Additionally, various typos and UI issues on the [Testing Distribution Portal](https://docs.appcircle.io/distribute/testing-management/downloading-binaries) have been fixed. <DistributionBadge/> <CloudBadge/> <SelfHostedBadge/>
- Deleting a [Release Candidate](https://docs.appcircle.io/publish-module/publish-information/marking-release-candidates) app version is now prevented; users must unmark it from being a [Release Candidate](https://docs.appcircle.io/publish-module/publish-information/marking-release-candidates) before deletion. <PublishBadge/> <CloudBadge/> <SelfHostedBadge/>
- Release Notes can now only be changed for [Release Candidate](https://docs.appcircle.io/publish-module/publish-information/marking-release-candidates) app versions. <PublishBadge/> <CloudBadge/> <SelfHostedBadge/>
- Fixed an issue requiring a refresh for event-based logs in the Get Approval via Email component. <PublishBadge/> <CloudBadge/> <SelfHostedBadge/>
- A bug was fixed where deleting an app version that leaves no app versions in the Publish Profile, resulted in incorrect information being displayed in the header. <PublishBadge/> <CloudBadge/> <SelfHostedBadge/>
- Fixed an issue where a refresh was causing a problem in the Publish Flow log panel. <PublishBadge/> <CloudBadge/> <SelfHostedBadge/>
- A bug was fixed where test submissions with missing compliance did not display a warning message about resolving the compliance issue before test submission to internal or external groups. <PublishBadge/> <CloudBadge/> <SelfHostedBadge/>
- Fixed a bug on UI where an app version name was cut short due to Release Candidate badge , also affected the other app version names within Publish Profile. <PublishBadge/> <CloudBadge/> <SelfHostedBadge/>
- An issue was fixed where, during the resigning of an .IPA binary, the sign button was enabled despite no Provision Profile being selected. <PublishBadge/> <CloudBadge/> <SelfHostedBadge/>
- An issue regarding the positioning of the Provisioning Profile and Read-Only Bundle ID options within Resign Binary feature has been fixed. <PublishBadge/> <CloudBadge/> <SelfHostedBadge/>
- The broken Jira transitions that the [Jira Comment](https://docs.appcircle.io/workflows/common-workflow-steps/jira-comment) step is making are now fixed so that you can update the status of Jira issues in the build pipeline. <BuildIntegrationsBadge/> <CloudBadge/> <SelfHostedBadge/>
- Android apps with special characters in their names now proceed without errors during signing and other steps. <BuildBadge/> <CloudBadge/> <SelfHostedBadge/>
- A bug fix has been applied to the auto distribution and publish features to address issues with non-existing Testing Distribution and Publish Profiles. <BuildBadge/> <CloudBadge/> <SelfHostedBadge/>
- Fixed the incorrect versioning of the [Gradle Runner](https://docs.appcircle.io/workflows/android-specific-workflow-steps/gradle-runner) step, which was breaking current workflows because of incompatible changes. <BuildIntegrationsBadge/> <CloudBadge/> <SelfHostedBadge/>
- [Testinium](https://docs.appcircle.io/workflows/common-workflow-steps/testinium) step dependencies are defined for the workflow editor so that the user can easily include the integration in the correct order. <BuildIntegrationsBadge/> <CloudBadge/> <SelfHostedBadge/>
- [Maestro Cloud Upload](https://docs.appcircle.io/workflows/common-workflow-steps/maestro-cloud-upload) step dependencies are defined for the workflow editor so that the user can easily include the integration in the correct order. <BuildIntegrationsBadge/> <CloudBadge/> <SelfHostedBadge/>
- Fixed a bug that caused the [no-proxy](https://docs.appcircle.io/self-hosted-appcircle/configure-server/integrations-and-access/proxy-configuration#edit-no_proxy-for-internal-container-network) helper tool to throw an error when the CIDR notation was used in the `no_proxy` environment variable. <SelfHostedBadge/>
- Fixed a bug that prevented the self-hosted Appcircle server logging service from being healthy when a proxy is used for network access. <SelfHostedBadge/>
- Fixed a bug that causes the wrong self-hosted server package to [download](https://docs.appcircle.io/self-hosted-appcircle/update#1-download-latest) when a specific version is preferred instead of the latest. <SelfHostedBadge/>

## 3.16.0 - 2024-05-10 - New features in Publish Module, Resigning Binary, Xcode 15.4, and more

### 🆕 New Features

- The [Resign Binary](/publish-module/publish-information/resign-binary) feature is now available for both iOS and Android applications within the Publish module. <PublishBadge/> <CloudBadge/> <SelfHostedBadge/>
- Users can now upload application screenshots and update [Metadata Information](https://docs.appcircle.io/publish-module/publish-information/meta-data-information) within the Publish module, including promotional text and descriptions, via Appcircle, without the need for the App Store Connect interface. <CloudBadge/> <SelfHostedBadge/> <PublishBadge/>
<!-- - LDAP Mapping is now supported in Appcircle, allowing seamless synchronization of user groups and roles from your LDAP directory to your Appcircle environment. This integration streamlines user management and enhances security by aligning your Appcircle roles with your organizational structures. For a detailed setup guide, visit our [LDAP Mapping documentation](/self-hosted-appcircle/configure-server/integrations-and-access/ldap-settings#ldap-mapping) -->
- Within the Publish profile card, App Store Status will be displayed for Enterprise users, while Flow Status will be observed for non-enterprise users. Similarly, in the app version view, Enterprise users will have access to both Flow and App Store Status, whereas non-Enterprise users will only see Flow Status displayed. <CloudBadge/> <SelfHostedBadge/> <PublishBadge/>
- A new component named "Update Metadata on App Store" has been integrated to the Publish Steps section, facilitating the display of metadata information. <CloudBadge/> <SelfHostedBadge/> <PublishIntegrationsBadge/>
- On the Metadata Information page, metadata for profiles designated as Release Candidates is retrieved directly from the store. For more information, refer to the [Metadata Information](/publish-module/publish-information/meta-data-information) documentation. <CloudBadge/> <SelfHostedBadge/> <PublishBadge/>
- Users uploading .AAB files can now share the app version with testers within the [Distribution](https://docs.appcircle.io/distribute) module. <CloudBadge/> <SelfHostedBadge/> <DistributionBadge/>
- The install certificate tool bundled in the runner package now supports proxies when connecting to remote URLs on macOS. <SelfHostedBadge/>
- The [Signing Identities](/signing-identities) module features are now accessible via the command-line interface. Learn more. <CloudBadge/> <SelfHostedBadge/> <APICLIBadge/> <SigningIdentitiesBadge/>
- You can now manage [Testing Groups](/distribute/testing-management/testing-groups) within the [Distribution](/distribute) module via the command-line interface. <CloudBadge/> <SelfHostedBadge/> <APICLIBadge/> <DistributionBadge/>
- Users can configure [Distribution](/distribute) settings to [automatically send builds to testers](/distribute/create-or-select-a-distribution-profile#auto-send-your-build-to-the-testers) using the command-line interface. <CloudBadge/> <SelfHostedBadge/> <APICLIBadge/> <DistributionBadge/>
- The "Default M1 pool" and "macOS VM image" now include [Xcode 15.4](https://docs.appcircle.io/infrastructure/ios-build-infrastructure#available-xcode-versions) installed on runners. We strongly recommend extensive testing of your workflows to ensure compatibility and stability with this release candidate. <CloudBadge/> <SelfHostedBadge/>
- This release introduces [a log viewing and delivery system](https://docs.appcircle.io/self-hosted-appcircle/configure-server/monitoring) for the self-hosted Appcircle server. <SelfHostedBadge/>
- Self-hosted customers can now [download](https://docs.appcircle.io/self-hosted-appcircle/configure-server/auto-updating) the Appcircle server package seamlessly and [update](https://docs.appcircle.io/self-hosted-appcircle/configure-server/auto-updating) the Appcircle server fully automated. <SelfHostedBadge/>

### :muscle: Improvements

- Users now have the capability to download comprehensive data associated with the app version, encompassing publish logs, metadata, screenshots, and build logs. <CloudBadge/> <SelfHostedBadge/>
- Users can now prepare and transmit screenshots and metadata to the App Store through the newly integrated metadata component. <CloudBadge/> <SelfHostedBadge/>
- Users can now seamlessly import metadata and screenshots from App Store Connect to establish the initial state on the Update Metadata screen. <CloudBadge/> <SelfHostedBadge/>
- The Appcircle runner package now includes a diagnostic tool that helps to identify, analyze, and troubleshoot system issues. <SelfHostedBadge/>
- Self-hosted Appcircle clients can now [download and extract](https://docs.appcircle.io/self-hosted-appcircle/self-hosted-runner/runner-vm-setup#download-the-macos-vm-and-xcode-images-automatically) the runner macOS VM in the background more robustly, particularly in cases of network connection faults. <SelfHostedBadge/>
- The install certificate tool included in the runner package, which trusts CA certificates, now extends support to Java 8, 17, and 21. <SelfHostedBadge/>
- We have added an App Store Status field within Publish Profiles and App Versions lists, providing regular updates at 30-minute intervals. For further details, please refer to the [App Store Status](/publish-module/binary-management#store-status) documentation. <CloudBadge/> <SelfHostedBadge/>

:::caution

To ensure the App Store status remains current, the following conditions must be met:

- The current profile necessitates valid store credentials defined within the Signing Identity module and must be selected.
- Alignment of the published app's identifier, version, and build number with the Appcircle app version records is essential.
- Identification of one of the app version records as the designated release candidate is required.
- The service will continue updating the app status until it reaches the 'READY_TO_SALE' or 'READY_TO_DISTRIBUTE' states.
- Initially, the service checks the App Store status; in the event of no matching records, it subsequently conducts a search within TestFlight.

:::

### 🐞 Fixes

- The self-hosted runner macOS installation now detects Homebrew anomalies that can occur after macOS upgrades and reinstalls Homebrew with package upgrades. <SelfHostedBadge/>
- Fixed various bugs that occurred during the installation of the self-hosted runner on GNU/Linux. <SelfHostedBadge/>
- Made improvements and fixed various bugs in the install certificate tool bundled in the runner package. <SelfHostedBadge/>
- Fixed a bug in the self-hosted version that prevented listing the Xcode version for the selected pool. <SelfHostedBadge/>
- Fixed a bug that caused errors during the parsing of large AAB files. <CloudBadge/> <SelfHostedBadge/>
- Fixed a bug that caused the last build time within the build profile appearing as null when a user deleted old builds. <CloudBadge/> <SelfHostedBadge/>

## 3.15.0 - 2024-04-24 - AAB to APK, Improved Testing Distribution, Publish Event Enhancement

### 🆕 New Features

- [The public link](https://docs.appcircle.io/distribute/create-or-select-a-distribution-profile#using-public-link-for-distribution) in the distribution settings has been transformed into a QR code to simplify access and sharing. <CloudBadge/> <SelfHostedBadge/>
- Users can now filter the app version list on [the testing portal](https://docs.appcircle.io/distribute/testing-management/downloading-binaries) by app name, version, release notes, or build number for enhanced navigation and search capabilities. <CloudBadge/> <SelfHostedBadge/>
- The system now automatically converts uploaded or built AAB files to a universal format. It also discreetly saves the newly created APK file with the second app's resource id. <CloudBadge/> <SelfHostedBadge/>
- A new command, ["build active-list"](https://docs.appcircle.io/appcircle-api/) has been added, allowing users to view active builds in the queue directly from their command line interface. <CloudBadge/> <SelfHostedBadge/>
- A new command, ["build view"](https://docs.appcircle.io/appcircle-api/) has been added, enabling users to access and view detailed information about builds directly from the command line interface. <CloudBadge/> <SelfHostedBadge/>
- The "Default M1 pool" now includes [Xcode 15.4 beta-1](https://docs.appcircle.io/infrastructure/ios-build-infrastructure#available-xcode-versions) installed on runners. As this is a beta release, we strongly recommend testing your workflows extensively to ensure compatibility and stability. <CloudBadge/> <SelfHostedBadge/>

### :muscle: Improvements

- We have introduced new [Publish Events](https://docs.appcircle.io/publish-module/) like Publish Profile Created, Publish Profile Deleted, App Version Uploaded, App Version Created, and App Version Deleted to enrich the activity report. <CloudBadge/> <SelfHostedBadge/>
- We have fine-tuned branch search and filter operations for faster performance and smoother functionality. <CloudBadge/> <SelfHostedBadge/>
- We have introduced the capability for active users to store profile pins (Enterprise store profile, Distribution profile, Build Profile, and Publish Profile) individually. Previously, profile pins were stored solely on an organization-wide level. Now, each active user can set and manage their own pin independently, providing greater flexibility and customization options. <CloudBadge/> <SelfHostedBadge/>
- Added [Okta](https://docs.appcircle.io/account/my-organization/sso-providers-configuration/okta-saml) tile based login so users can log in to the Appcircle dashboard by clicking the Appcircle app icon on Okta side. <CloudBadge/> <SelfHostedBadge/>

### 🐞 Fixes

- We have fixed a bug that caused the report to update only once due to discrepancies between canceling after the build starts and canceling before it starts. <CloudBadge/> <SelfHostedBadge/>
- Fixed an issue where manual distribution resulted in errors when attempting to install an already existing version. Now, a pop-up warning is displayed in such cases. <CloudBadge/> <SelfHostedBadge/>
- Fixed the issue of undefined workflow name in the 'listBuildProfileWorkflows' command. <CloudBadge/> <SelfHostedBadge/>
- Fixed "workflowName" parameter in the "build start" command. <CloudBadge/> <SelfHostedBadge/>
- Fixed a bug that caused fullchain certificates installed by users to not work properly. <CloudBadge/> <SelfHostedBadge/>

## 3.14.0 - 2024-04-04 - Improved Workflow Editor, Publish Module Enhancement, Deprecated Store Submit Module

### 🆕 New Features

- In the [Publish module](https://docs.appcircle.io/publish-module), within the app information section, users can now redirect to the relevant build and profile if the publish originated from a build. <CloudBadge/> <SelfHostedBadge/>
- Release notes are now displayed in the [app information](https://docs.appcircle.io/publish-integrations/ios-publish-integrations/app-information-app-store) section within the Publish module. <CloudBadge/> <SelfHostedBadge/>
- The ["Get approval from Test Flight"](https://docs.appcircle.io/publish-integrations/ios-publish-integrations/approval-test-flight) step has been enhanced to provide additional information and actions, such as managing beta testers and addressing compliance errors. <CloudBadge/> <SelfHostedBadge/>
- Added the ability to distribute to both internal and external groups within the ["Get approval from Test Flight"](https://docs.appcircle.io/publish-integrations/ios-publish-integrations/approval-test-flight) section. <CloudBadge/> <SelfHostedBadge/>
- The compliance status is now displayed in the ["Get approval from Test Flight"](https://docs.appcircle.io/publish-integrations/ios-publish-integrations/approval-test-flight) component on the new UI page.<CloudBadge/> <SelfHostedBadge/>
- Support for obtaining multiple email approvals, with required/optional options and a minimum approval count, has been added to the [Publish Flow](https://docs.appcircle.io/publish-module/publish-flow/). <CloudBadge/> <SelfHostedBadge/>
- Added filtering support for Publish Profile list based on latest statuses. <CloudBadge/> <SelfHostedBadge/>
- You can now update the default release note of the app version provided by the Build Module. This will be sent as the "What to Test" area in [TestFlight](https://docs.appcircle.io/publish-integrations/ios-publish-integrations/sent-to-testflight). <CloudBadge/> <SelfHostedBadge/>
- Submit Store redirects have been eliminated from the site. <CloudBadge/> <SelfHostedBadge/>
- Incorporated a "Type" field into the data table within the [Environment Variable](https://docs.appcircle.io/environment-variables) sections, offering additional context regarding the type of each variable. <CloudBadge/> <SelfHostedBadge/>
- [PAT (Personal Access Token) connections](https://docs.appcircle.io/build/manage-the-connections/#managing-pat-connections) listed on the build connection page are now deletable, providing users with the flexibility to manage their connections more efficiently. <CloudBadge/> <SelfHostedBadge/>
- Branches are now filtered based on their status, enabling users to easily identify and navigate through branches based on their current state. <CloudBadge/> <SelfHostedBadge/>
- Users now have the capability to be redirected to their desired locations upon clicking on [Okta applications](https://docs.appcircle.io/account/my-organization/sso-providers-configuration/okta-saml), enhancing navigation efficiency and user experience within the system. <CloudBadge/> <SelfHostedBadge/>
- When a build is [manually initiated](https://docs.appcircle.io/build/build-process-management/build-manually-or-with-triggers#manual-build), the system retrieves information about the user from the initiating organization. Conversely, if the build is [not initiated manually](https://docs.appcircle.io/build/build-process-management/build-manually-or-with-triggers#automatic-build), it displays the details of the user who made the commit, ensuring accurate attribution of actions within the system. <CloudBadge/> <SelfHostedBadge/>
- The self-hosted Appcircle server now supports using a custom domain for the [Testing Distribution Portal](/distribute/testing-management/downloading-binaries). Follow the instructions in the [Testing Distribution](/self-hosted-appcircle/configure-server/integrations-and-access/ssl-configuration#testing-distribution) section of the SSL configuration. <SelfHostedBadge/>
- The self-hosted Appcircle server now adopts single-node single drive MinIO instead of multi-node single drive MinIO in the default configuration, which decreases disk consumption significantly. <SelfHostedBadge/>

:::caution

Upgrading from older versions to `v3.14.0` or later, requires MinIO migration that should be done interactively while upgrading.

In order to migrate to single-node single drive MinIO configuration or stay with the deprecated multi-node single drive MinIO configuration, **you must follow the instructions** that are defined in the [MinIO Migration](/self-hosted-appcircle/configure-server/minio-migration) document.

:::

:::tip

Fresh self-hosted server installations do not require any manual intervention for the MinIO configuration.

The single-node single drive [MinIO configuration](/self-hosted-appcircle/configure-server/minio-migration) is applied by default on fresh installations.

:::

### :muscle: Improvements

- Users can now update the default release notes for app versions directly on the [Binary Information](https://docs.appcircle.io/publish-module/publish-information/binary-information) page. <CloudBadge/> <SelfHostedBadge/>
- In the [Publish module](https://docs.appcircle.io/publish-module), the names "App Info" and "Details" have been updated to prevent misunderstanding. "App Information" has been changed to "Binary Information," and "Details" has been changed to "Publish Details" for clarity. <CloudBadge/> <SelfHostedBadge/>
- In the Publish module, the [Release Candidate](https://docs.appcircle.io/publish-module/publish-information/marking-release-candidates) version is now the exclusive source for the Profile App Version, Build Number, and Icon.<CloudBadge/> <SelfHostedBadge/>
- Post-upload control for [Google Play](https://docs.appcircle.io/publish-integrations/android-publish-integrations/send-to-googleplay#adding-a-google-play-developer-api-key) and [Huawei AppGallery](https://docs.appcircle.io/publish-integrations/android-publish-integrations/send-to-huawei#adding-a-huawei-appgallery-api-key) Credential Validation against API files has been implemented. <CloudBadge/> <SelfHostedBadge/>
- Improvements have been made to the text on the download and install buttons in the Enterprise app store. <CloudBadge/> <SelfHostedBadge/>
- The user interface has been updated for disabled states, with the opacity of the corresponding switch object being reduced to improve visual clarity and indicate its disabled status more effectively. <CloudBadge/> <SelfHostedBadge/>
- The invitation link has been updated to be a clickable link instead of plain text, allowing users to easily access the invitation page with a single click for a smoother onboarding experience. <CloudBadge/> <SelfHostedBadge/>

### 🐞 Fixes

- Fixed a bug that allowed app versions with different bundle IDs to be uploaded. <CloudBadge/> <SelfHostedBadge/>
- Fixed a bug where self-hosted runners, when the only available runner systems were present, were unable to detect changes or default values of Xcode versions for App Store steps. <SelfHostedBadge/>
- Fixed a bug where the data was not updated when an app version Release Candidate (RC) was selected. <CloudBadge/> <SelfHostedBadge/>
- Fixed a bug in the pool table where, if agent information was missing, the pool was erroneously reset as if no records were present. <CloudBadge/> <SelfHostedBadge/>
- Fixed a bug that occurred when re-uploading a file with the same name. <CloudBadge/> <SelfHostedBadge/>
- Fixed a crash that occurred on the add new user screen when encountering an invited user. <CloudBadge/> <SelfHostedBadge/>
- Resolved a 404 issue that users encountered when attempting to connect to PAT (Personal Access Token). <CloudBadge/> <SelfHostedBadge/>
- Fixed a problem where versioning was being reset erroneously. <CloudBadge/> <SelfHostedBadge/>
- Fixed a bug where form validation was broken after uploading YAML files. <CloudBadge/> <SelfHostedBadge/>
- Fixed an issue where there was a problem with keystore selection on the Resign binary page <CloudBadge/> <SelfHostedBadge/>

## 3.13.0 - 2024-03-04 - Improved Publish Module, Xcode 15.3, Build Infrastructure Updates

### 🆕 New Feature

- The new "App Information" tab has been added into the Publish Detail page for the new "App Information from App Store" step. <CloudBadge/> <SelfHostedBadge/>
- Within the new "App Information" section, users can now find the Publish icon displayed for both TestFlight and App Store, offering convenient access to essential information regarding the app's publication status across these platforms. <CloudBadge/> <SelfHostedBadge/>
- The pool selection feature has been added to the [Publish Module Settings](https://docs.appcircle.io/publish-module/#publish-settings). <CloudBadge/> <SelfHostedBadge/>
- In the Publish Module, users now have the capability to upload YAML files for their flows, enabling easier management and customization. Additionally, they can download their existing flows for offline reference or modification. <CloudBadge/> <SelfHostedBadge/>
- Within the Publish Module, customers now have the capability to designate their desired app version as a Release Candidate, streamlining the process of identifying and managing versions prior to official release. <CloudBadge/> <SelfHostedBadge/>
- The "Default M1 Pool" and [self-hosted macOS VM image](https://docs.appcircle.io/self-hosted-appcircle/self-hosted-runner/runner-vm-setup/) have been updated to include the latest [Xcode 15.3](https://developer.apple.com/documentation/xcode-release-notes/xcode-15_3-release-notes) release. <CloudBadge/> <SelfHostedBadge/>
- The "Default M1 Pool" has been transitioned to [macOS Sonoma](https://docs.appcircle.io/infrastructure/ios-build-infrastructure), now featuring the latest Xcode and stack updates. <CloudBadge/> <SelfHostedBadge/>
- The "Default M1 Pool" and the self-hosted runner environment now feature the latest [JDK 21](https://docs.appcircle.io/workflows/common-workflow-steps/custom-script#how-to-change-java-version), along with patch version upgrades for JDK 8, 11, and 17, ensuring compatibility and providing users with access to the most up-to-date Java development environment. <CloudBadge/> <SelfHostedBadge/>

### :muscle: Improvement

- Certain email templates have been upgraded to incorporate icons in build notifications, enhancing visual clarity and the user experience. <CloudBadge/> <SelfHostedBadge/>
- Self-hosted installations now have the ability to customize the "distribution not found" logo by specifying a custom SVG logo path within the tester web container. <SelfHostedBadge/>
- A scheduled task has been implemented to enhance performance by optimizing the cleaning process of outdated information-level job and job log records. <CloudBadge/> <SelfHostedBadge/>
- The login, registration, forgot password, and single sign-on (SSO) login pages have all been updated with a fresh new user interface. <CloudBadge/> <SelfHostedBadge/>
- Registration now restricts the use of common and disposable email domains for user sign-up. <CloudBadge/> <SelfHostedBadge/>
- Social login functionality is deprecated. Users attempting to log in via social platforms will now be redirected to the registration page for initial setup. However, those who have previously utilized social logins can still access this feature without interruption. <CloudBadge/> <SelfHostedBadge/>
- After logging into the application, users now have the ability to provide onboarding information. <SelfHostedBadge/>
- Dynamic title changes based on the selected language have been implemented to elevate the user experience, ensuring that users receive content in their preferred language seamlessly. <CloudBadge/> <SelfHostedBadge/>
- A new "Provision Profile Type" section has been incorporated into the "App Information" section within the App version, providing users with essential details regarding provisioning profile types associated with the application. <CloudBadge/> <SelfHostedBadge/>
- A validation has been introduced to the Email field within the "Approval via Email" section, ensuring that accurate and properly formatted email addresses are provided for submission. <CloudBadge/> <SelfHostedBadge/>
- In the "select repository" section while connecting to [Bitbucket](https://docs.appcircle.io/build/adding-a-build-profile/connecting-to-bitbucket), [GitLab](https://docs.appcircle.io/build/adding-a-build-profile/connecting-to-gitlab), [GitHub](https://docs.appcircle.io/build/adding-a-build-profile/connecting-to-github), or [Azure DevOps](https://docs.appcircle.io/build/adding-a-build-profile/connecting-to-azure), teams are now listed in alphabetical order, streamlining the process of selecting repositories and enhancing user navigation within the system. <CloudBadge/> <SelfHostedBadge/>
- A new "Connection Pool" field has been introduced in the LDAP Configuration settings, providing users with the ability to configure connection pooling for LDAP connections. <CloudBadge/> <SelfHostedBadge/>
- An "Order" field has been incorporated into the LDAP Configuration settings, enabling users to specify the order of LDAP configurations. <CloudBadge/> <SelfHostedBadge/>
- Sub-organizations can now access and manage the connection settings, allowing for more comprehensive control and customization within the system. <CloudBadge/> <SelfHostedBadge/>
- A new status has been introduced for builds. Moving forward, the "running" status will also be displayed, providing users with real-time updates on the progress of ongoing builds. <CloudBadge/> <SelfHostedBadge/>
- During self-hosted runner installation, the system now conducts checks on the host configuration. If nested virtualization is supported, the installation process includes the setup of the [Android emulator](https://docs.appcircle.io/self-hosted-appcircle/self-hosted-runner/configure-runner/android-emulator/), enhancing compatibility and enabling seamless Android development workflows. <SelfHostedBadge/>
- The "Default M1 Pool" and the self-hosted runner environment have been updated to include Node.js 18 LTS as the default version, providing users with the latest features and improvements in Node.js for [Android](https://docs.appcircle.io/infrastructure/android-build-infrastructure) and [iOS](https://docs.appcircle.io/infrastructure/ios-build-infrastructure). <CloudBadge/> <SelfHostedBadge/>

### 🐞 Fixed

- Fixed a bug that prevented the display of the active publish status in the App version table field. <CloudBadge/> <SelfHostedBadge/>
- Fixed a bug that caused errors when attempting to download app versions during the publish process. <CloudBadge/> <SelfHostedBadge/>
- Fixed a bug that retained the behavior of the export build artifact step for problematic metadata exports. <CloudBadge/> <SelfHostedBadge/>
- Fixed a bug where, if the commit message was empty and there was no custom release note component, the release note wasn't being transmitted to the distribution server. <CloudBadge/> <SelfHostedBadge/>
- Fixed a bug in the Appcircle CLI config trust command that caused it to fail to locate the script. <SelfHostedBadge/>
- Fixed a bug causing multiple requests to be sent erroneously. <CloudBadge/> <SelfHostedBadge/>
- Fixed a bug where validation problems in the form were occurring. <CloudBadge/> <SelfHostedBadge/>

## 3.12.0 - 2024-01-25 - Comprehensive Revision on Permissions, Improvements for Notifications, Migrating to the Publish Module, and Appcircle CLI Updates

### 🆕 New Feature

- Permission (role) naming has been changed in [advanced role management](https://docs.appcircle.io/account/my-organization#advanced-role-management). Also, there are some new roles added for better scope management in your organization. <CloudBadge/> <SelfHostedBadge/>
- [Share with Testers](https://docs.appcircle.io/distribute/create-or-select-a-distribution-profile#share-your-application-with-the-test-groups-manually) in Testing Distribution now has a new toggle option that enables you to display only the shared app version instead of all app versions. <CloudBadge/> <SelfHostedBadge/>
- Appcircle Notifications now has improvements on [Slack](https://docs.appcircle.io/account/slack/slack-notifications), [Microsoft Teams](https://docs.appcircle.io/account/teams-notifications), [Email](https://docs.appcircle.io/account/email-connection), and [Webhook](https://docs.appcircle.io/account/webhooks) channels that allows you to share release notes, build logs, and test reports via notifications. <CloudBadge/> <SelfHostedBadge/>
- The Store Submit module has been deprecated and it will be replaced by the brand-new [Publish](https://docs.appcircle.io/publish-module) module. You should transfer your apps to the [Publish](https://docs.appcircle.io/publish-module) module in order to submit your apps to the stores. <CloudBadge/> <SelfHostedBadge/>
- The Appcircle CLI has undergone a complete revision to make it compatible with the latest Appcircle API. Now it also supports self-hosted Appcircle servers. You can see all the recent changes made in the [changelog](https://github.com/appcircleio/appcircle-cli/blob/main/CHANGELOG.md) and follow [configuration instructions](https://docs.appcircle.io/self-hosted-appcircle/configure-server/appcircle-cli) to use the CLI with a self-hosted Appcircle server. <CloudBadge/> <SelfHostedBadge/>

### :muscle: Improvement

- You can now [download](https://docs.appcircle.io/publish-module/#version-download) app version artifacts (`ipa`, `aab`, or `apk`) in the Publish module. <CloudBadge/> <SelfHostedBadge/>
- The blue status bar at the bottom has been changed to **Active Processes**. Now, not only the builds but also the active store submit and publish jobs will be seen there. <CloudBadge/> <SelfHostedBadge/>
- Enterprise users can customize their [publish flows](https://docs.appcircle.io/publish-module/#publish-flow) using the **Manage Flow** button so that they can deploy their apps to multiple targets, get approvals from different stakeholders, execute custom scripts, and even more. <CloudBadge/> <SelfHostedBadge/>
- Administrators can now enable or disable the "Edit Username" feature from **Login Settings** on the self-hosted Appcircle server. <SelfHostedBadge/>
- `Manager`, `Operator`, and `Viewer` build profile roles have view permission for the [self-hosted runners](https://docs.appcircle.io/self-hosted-appcircle/self-hosted-runner/configure-runner/manage-runners) list but cannot enable or disable any runner on the list. <CloudBadge/> <SelfHostedBadge/>
- License limits for monthly tester emails and artifact storage size were removed from "Organization > Billing > Usages". Keep in mind that for fair usage, the limits exist but are higher when compared to previous plan limits. <CloudBadge/> <SelfHostedBadge/>
- Now only the underscore character ("\_") can be used in [environment variable](https://docs.appcircle.io/environment-variables/managing-variables) group naming. Appcircle will not allow other special characters in group names. <CloudBadge/> <SelfHostedBadge/>
- [Enterprise App Store](https://docs.appcircle.io/account/my-organization#enterprise-app-store-permissions) permissions have undergone revision with new roles that enable users to configure authorization in detail. <CloudBadge/> <SelfHostedBadge/>
- [User invitation](https://docs.appcircle.io/account/my-organization#managing-team-members) and membership update notification emails have been improved and now include additional information, such as sub-organizations. <CloudBadge/> <SelfHostedBadge/>
- User redirection when invited to the organization was improved according to several different cases, like registered, not registered, or SSO login. <CloudBadge/> <SelfHostedBadge/>
- Now you can enhance the SSO login experience by eliminating the "SSO Alias" requirement on the login screen. For this, you should create an Appcircle-compatible login URL so that users can pass through the "SSO Alias" step when they access Appcircle using your custom login URL. <CloudBadge/> <SelfHostedBadge/>
- Publish flow step statuses, and the last step status in the [version list](https://docs.appcircle.io/publish-module/#publish-versions) will be in `waiting` status unless the runner executes them. <CloudBadge/> <SelfHostedBadge/>
- The contact button at the bottom right of the page has been removed. You can reach us through the [Contact](https://appcircle.io/contact) or [Slack](https://slack.appcircle.io/) channels. <CloudBadge/>
- The duration and results of internal scheduled tasks can now be tracked by the schedule manager in the infrastructure. <CloudBadge/> <SelfHostedBadge/>
- You can see the Git URL under the repository name while selecting the repository on a new connection, which avoids confusion when the team has the same repository name in different locations. <CloudBadge/> <SelfHostedBadge/>
- Queue waiting records with a waiting time of 0 min will no longer appear in the queue waiting reports for better experience. <SelfHostedBadge/>
- Supported Xcode versions that you see in the "starting workflow" step in build logs are ordered descending (latest first) for better readability. <CloudBadge/> <SelfHostedBadge/>
- Testing Distribution [distribution profile](https://docs.appcircle.io/account/my-organization#distribution-profile-permissions) permissions have undergone revision with new `Operator` role and other role naming changes. <CloudBadge/> <SelfHostedBadge/>
- The self-hosted runner macOS image is the same VM image as in the cloud Appcircle, which will keep you always up-to-date with the latest without waiting for special self-hosted updates. <SelfHostedBadge/>

### 🐞 Fixed

- The time to check the active status of self-hosted runners has been increased from 2 hours to 3 days, which also fixes self-hosted pool availability in the build profile configuration. <SelfHostedBadge/>
- Fixed a typo and a broken re-login redirection when an invalid OTP attempt was made in custom authentication. <SelfHostedBadge/>
- Fixed a bug that prevents sub-organizations from seeing their own enterprise app store download reports. <CloudBadge/> <SelfHostedBadge/>
- Fixed a bug that throws an "branch and commit are not active" toast error when a new branch is added to the repository and not refreshed on the Appcircle side. <CloudBadge/> <SelfHostedBadge/>
- Fixed cache invalidation issues on the login screen. <CloudBadge/> <SelfHostedBadge/>
- Fixed a bug that prevents users from manually uploading `aab` files in the Publish module. <CloudBadge/> <SelfHostedBadge/>
- Fixed a bug for correct step listing in Build module workflow and Publish module flow steps. <CloudBadge/> <SelfHostedBadge/>
- Fixed a bug that prevents user to click on "disconnect" but at Slack integration. <CloudBadge/> <SelfHostedBadge/>
- Fixed bugs that occur while deleting the store API keys in integrations. <CloudBadge/> <SelfHostedBadge/>
- Fixed a bug that enables users to distribute apps to the Enterprise App Store, although they do not have sufficient permission in the Enterprise App Store. <CloudBadge/> <SelfHostedBadge/>
- Fixed unnecessary toast errors when the user has relevant permission in Distribution Profile and opens the build profile configuration. <CloudBadge/> <SelfHostedBadge/>
- Fixed a bug that throws toast errors messages when the user opens the build configuration signing tab. <CloudBadge/> <SelfHostedBadge/>
- Fixed a bug that prevents the correct display of the "Published At" in Enterprise App Store profiles. <CloudBadge/> <SelfHostedBadge/>
- Fixed a bug where the user can enter invalid values into license limits at license details. <CloudBadge/> <SelfHostedBadge/>
- Fixed a bug that prevents manage profiles and app versions in the Enterprise App Store when they have the `Uploader` role. <CloudBadge/> <SelfHostedBadge/>
- Fixed a bug that makes browser crash while viewing build logs. <CloudBadge/> <SelfHostedBadge/>
- Fixed a bug that prints the incorrect remaining limit when the license is expired. <CloudBadge/> <SelfHostedBadge/>
- Fixed a bug that threw an error while renaming the publish profile. <CloudBadge/> <SelfHostedBadge/>
- Fixed the missing default values for [Appdome Build-2Secure for Android](https://docs.appcircle.io/integrations/appdome-integration) workflow step output. <CloudBadge/> <SelfHostedBadge/>
- Fixed the [JaCoCo](https://www.eclemma.org/jacoco/) code coverage "NilObject" error by improving the parser algorithm at the [test report](https://docs.appcircle.io/continuous-testing/android-testing/running-android-unit-tests#generating-test-report) workflow step. <CloudBadge/> <SelfHostedBadge/>
- Fixed the format of values in the publish flow step settings so that they're more user-friendly instead of "key|value" style. <CloudBadge/> <SelfHostedBadge/>
- Fixed the value of the `AC_PULL_NUMBER` environment variable in the build pipeline, which should be the merge request `iid` value for the GitLab connection. <CloudBadge/> <SelfHostedBadge/>

## 3.11.0 - 2023-12-27 - Publish Module, Change Build Profile Owner, Custom Authentication Integration

### 🆕 New Feature

- A new module called [Publish](/publish-module) is introduced in beta, which helps manage App Store, Google Play, and Huawei AppGallery deployments with more efficiency. You can now modify publishing flows, add custom scripts, and control flow logic. <CloudBadge/> <SelfHostedBadge/>
- Members in the same [organization](/account/my-organization) can take ownership of previously added build profiles. <CloudBadge/> <SelfHostedBadge/>
- The user can now add a new PAT (Personal Access Token) via the [Connections](/build/manage-the-connections#managing-pat-connections) page without creating a new build profile. <CloudBadge/> <SelfHostedBadge/>
- Enterprise customers can integrate their own authentication and OTP services and use them in conjunction with LDAP configuration on self-hosted installations. <SelfHostedBadge/>
- The configuration file [global.yaml](../self-hosted-appcircle/install-server/docker#3-configure) now has a validator that helps users configure the settings correctly on export and prevents them from starting the server with broken settings. <SelfHostedBadge/>
- The [certificate installer](../self-hosted-appcircle/install-server/docker#3-configure) tool now supports extracting proxy server certificates, which enable the runner to connect through a proxy without any SSL certificate error. <SelfHostedBadge/>

### :muscle: Improvement

- The starting workflow step in the build log shows the email address of the user who triggered the current build. <CloudBadge/> <SelfHostedBadge/>
- Users who have reached the build limit on their licenses will no longer be able to use Autofill while adding a new profile. <CloudBadge/> <SelfHostedBadge/>
- The motto on the login and sign-up pages has been changed to reflect our up-to-date vision. <CloudBadge/> <SelfHostedBadge/>
- The "Default M1 Pool" has the latest stable [Xcode 15.1](https://developer.apple.com/documentation/xcode-release-notes/xcode-15_1-release-notes) update available on runners and can be used for iOS builds. <CloudBadge/> <SelfHostedBadge/>
- The "Default M1 Pool" has [Xcode 15.2](https://developer.apple.com/documentation/xcode-release-notes/xcode-15_2-release-notes) beta-1 installed on runners. Since this is a beta release, please test your workflows extensively. <CloudBadge/> <SelfHostedBadge/>
- The LDAP configuration section in settings has a help button that redirects to the relevant documentation page for configuration details. <SelfHostedBadge/>
- A new type of role **Operator** has been added to the build profile roles that can also trigger builds. <CloudBadge/> <SelfHostedBadge/>
- You can change the [Enterprise App Store](/self-hosted-appcircle/configure-server/integrations-and-access/ssl-configuration#enterprise-app-store) settings (domain, etc.) after installation without any `reset` action. <SelfHostedBadge/>

### 🐞 Fixed

- Fixed an issue where a connected build profile would appear as if it had not been connected before. <CloudBadge/> <SelfHostedBadge/>
- Fixed an issue that caused the user to completely restrict their own [privileges](/account/my-organization#managing-the-team-under-an-organization) when alone in an organization. <CloudBadge/> <SelfHostedBadge/>
- Fixed the case where the build pipeline was executed on a non-selected wrong pool, which was affecting the default Intel and M1 pools. <CloudBadge/>
- Fixed an issue that was affecting the first-time [connections to the GitLab](/build/manage-the-connections/adding-a-build-profile/connecting-to-gitlab) provider. <CloudBadge/> <SelfHostedBadge/>
- The bug was fixed in the re-creation of a connection that had been disconnected and had its [token revoked](/build/manage-the-connections#revoke-oauth-connections). <CloudBadge/> <SelfHostedBadge/>
- Fixed a redirect issue when the user tried to connect to any Git provider without an active connection. <CloudBadge/> <SelfHostedBadge/>
- Fixed an issue with the [Unit and UI test](/continuous-testing/ios-testing/running-ios-unit-and-ui-tests) screenshots in the test reports. <CloudBadge/> <SelfHostedBadge/>
- Fixed an issue that occurred in the branch list and commits after [changing the git provider](/build/manage-the-connections/reconnect-change-provider#change-git-provider-and-reconnect) connection at the build profile. <CloudBadge/> <SelfHostedBadge/>
- Fixed an issue that caused environment variables to be created with the same name in the same [environment variable](/environment-variables/managing-variables) group on the API. <CloudBadge/> <SelfHostedBadge/>
- An error that occurred after closing the repository list while trying to change the Git provider of a build profile connected to a repository has been fixed. <CloudBadge/> <SelfHostedBadge/>
- Fixed an issue that caused the [invited user](/account/my-organization#managing-team-members) not to be redirected to the sign up page if they were not registered. <CloudBadge/> <SelfHostedBadge/>
- Fixed an issue where the authentication logs section was not visible. <CloudBadge/>
- The error with the email hint text falling into the email field on the login and sign up pages has been fixed. <CloudBadge/> <SelfHostedBadge/>
- Fixed the [Xcodebuild for Unit and UI Tests](/workflows/ios-specific-workflow-steps/#xcodebuild-for-unit-and-ui-tests) workflow step, which was stuck in the build pipeline until timeout in some cases. <CloudBadge/> <SelfHostedBadge/>
- Fixed the crash in the [Export Build Artifacts](/workflows/common-workflow-steps#export-build-artifacts) workflow step that occurs while uploading files in the artifacts that have 0 bytes of length or no content. <CloudBadge/> <SelfHostedBadge/>
- The bundler version bug has been fixed in the [Fastlane](/workflows/common-workflow-steps/fastlane) workflow step by pinning the last bundler version compatible with the ruby version that's included in build runners. <CloudBadge/> <SelfHostedBadge/>
- The permission error that occurred while using the [Authenticate with Netrc](/workflows/common-workflow-steps#authenticate-with-netrc) workflow step was fixed. <CloudBadge/> <SelfHostedBadge/>
- The command line parameter order has been changed to fetch provisioning profiles for signing first, which fixes the broken auto-sign feature in the [Xcodebuild for Devices](/workflows/ios-specific-workflow-steps#xcodebuild-for-devices-archive--export) workflow step. <CloudBadge/> <SelfHostedBadge/>
- Fixed the errors thrown while using the [Bitbucket](/build/manage-the-connections/adding-a-build-profile/connecting-to-bitbucket) connection in build profiles. <CloudBadge/> <SelfHostedBadge/>
- In the [Azure DevOps Server 2020](/build/manage-the-connections/adding-a-build-profile/connecting-to-azure#connecting-to-azure-devops-server-repository) version, the trigger was malfunctioning due to the different JSON format received after a merge operation following a PR (Pull Request). It was fixed. <CloudBadge/> <SelfHostedBadge/>
- The bug that prevents users from [changing their emails](/account/my-account/account-management/my-details) was fixed. <CloudBadge/> <SelfHostedBadge/>
- Fixed a bug about [`no_proxy`](/self-hosted-appcircle/configure-server/integrations-and-access/proxy-configuration#2-configure-proxy-for-the-server) environment variables that broke the network connection of the self-hosted Appcircle server. <SelfHostedBadge/>
- Fixed bug that causes version output to be incorrect when [artifact registry](../self-hosted-appcircle/install-server/docker#using-3rd-party-or-self-hosted-artifact-registry) has port in URL. <SelfHostedBadge/>
- Fixed corrupted `check` command output in Ubuntu-based Linux [distributions](../self-hosted-appcircle/install-server/docker#supported-linux-distributions). <SelfHostedBadge/>

## 3.10.0 - 2023-12-01 - Connections Page, Disconnect Profile and Change Provider

### 🆕 New Feature

- Added [Connections](/build/manage-the-connections) to the Build module, where all connections (OAuth, PAT) can be viewed and edited. From here, you can disconnect, reconnect, and view the build profiles affected by the connections. <CloudBadge/> <SelfHostedBadge/>
- You can now [disconnect and reconnect](/build/manage-the-connections/reconnect-change-provider#change-git-provider-and-reconnect) to another repository or Git provider without deleting the link to an added profile. You can also change PATs for connections made with PAT. <CloudBadge/> <SelfHostedBadge/>
- The [Testinium](/workflows/common-workflow-steps/#testinium) workflow component now tries several times in case of an error from the Testinium APIs. <CloudBadge/> <SelfHostedBadge/>
- The [Appdome-Build-2Secure](/workflows/ios-specific-workflow-steps/#appdome-build-2secure-for-ios) for iOS component was added, which is the integration that allows activating security and app protection features. <CloudBadge/> <SelfHostedBadge/>

### :muscle: Improvement

- Now builds that result in a [warning](/workflows/#build-warning-status) will also appear as a warning in the branch list. <CloudBadge/> <SelfHostedBadge/>
- Appcircle builds can now be displayed as “Appcircle/BuildProfileId” in pipelines on Git providers. <CloudBadge/> <SelfHostedBadge/>
- The URL format validation used when adding Git provider [instances](/build/manage-the-connections/adding-a-build-profile/connecting-multiple-instance) has been removed for self-hosted environments. <SelfHostedBadge/>
- The [Testinium](/workflows/common-workflow-steps/#testinium) workflow component parses result summary and outputs in seperate environment variables. <CloudBadge/> <SelfHostedBadge/>
- A user-friendly format has been introduced in the [testing distribution](/distribute/create-or-select-a-distribution-profile) emails. <CloudBadge/> <SelfHostedBadge/>
- [Brute-force protection](/self-hosted-appcircle/configure-server/advanced-configuration/ldap-brutefore) and the ability to configure it have been added when logging into the Enterprise App Store and Testing Distribution via the LDAP method in self-hosted use. <SelfHostedBadge/>
- The caching mechanism used when choosing between Testing Distribution [authentication](/distribute/create-or-select-a-distribution-profile#using-authentication-for-distribution) options has been disabled for the sake of quick response. <CloudBadge/> <SelfHostedBadge/>
- You can no longer add or build Smartface projects to Appcircle. Smartface support has been removed. <CloudBadge/> <SelfHostedBadge/>
- Appcircle no longer supports purchases via Appsumo, and there is no Appsumo featured license supported on Appcircle. <CloudBadge/>
- Appcircle online documentation got several updates and improvements, including search, screenshots, and content that provides a better user experience. <CloudBadge/>

### 🐞 Fixed

- The loader did not appear when loading the [Enterprise App Store](/enterprise-appstore/enterprise-app-store-setup/add-ent-profile) page, the confusion caused by this has been fixed by adding the loader. <CloudBadge/> <SelfHostedBadge/>
- Fixed a bug when adding profiles using the [SSH connection](/build/manage-the-connections/adding-a-build-profile/connecting-to-private-repository-via-ssh) method. <CloudBadge/> <SelfHostedBadge/>
- Fixed a bug during the [configuration cloning](/build/build-process-management/build-profile-configuration#clone-configuration) process. <CloudBadge/> <SelfHostedBadge/>
- Page redirection issues were occurring on plan upgrade, this problem has been fixed. <CloudBadge/>
- Fixed an issue with the [Xcodebuild for Devices](../build/platform-build-guides/building-ios-applications) workflow step getting stuck in the build pipeline until timing out in some cases. <CloudBadge/> <SelfHostedBadge/>
- Fixed an issue that caused a build to be started in Appcircle when one of the _Approve_, _Approve with Recommendations_, _Wait for Author_, or _Reject_ activities was selected on pull requests when using the [Azure DevOps](/build/build-process-management/build-manually-or-with-triggers#managing-triggers-for-builds) Git provider. <CloudBadge/> <SelfHostedBadge/>
- Fixed a bug that prevented screenshots from being displayed as a result of the [Unit and UI Tests](/continuous-testing/ios-testing/running-ios-unit-and-ui-tests) in the test results section. <CloudBadge/> <SelfHostedBadge/>
- Fixed the issue that caused multiple builds to be launched when only one trigger was set on Appcircle and a trigger was triggered. <CloudBadge/> <SelfHostedBadge/>
- The incorrect "Configuration" information in the [e-mail notification](/account/my-organization/notifications-and-communication/email-connection) sent as a result of the build in simultaneous build triggers has been corrected. <CloudBadge/> <SelfHostedBadge/>
- When the [Environment Variables](/environment-variables/managing-variables) file was created from scratch and values were entered and downloaded, the downloaded file appeared empty. This error has been fixed. <CloudBadge/> <SelfHostedBadge/>

## 3.9.0 - 2023-11-01 - LDAP Support for User Authentication, Change the PAT by Build Profile, Download Environment Variables

### 🆕 New Feature

- "Self-hosted Settings" has been introduced on the admin page for self-hosted Appcircle server. It includes [LDAP Login](/self-hosted-appcircle/configure-server/integrations-and-access/ldap-settings#appcircle-login-with-ldap) for configuring LDAP user authentication and [Login Settings](/self-hosted-appcircle/configure-server/integrations-and-access/login-configuration#login-settings) for other login configuration options. <SelfHostedBadge/>
- Users are now allowed to manage their connections to private repositories after connecting their profiles. <CloudBadge/> <SelfHostedBadge/>
- Now users are able to download the [environment variables](/environment-variables/managing-variables#download-environment-variables) in JSON format. <CloudBadge/> <SelfHostedBadge/>
- Added a new environment variable called [AC_TRIGGER_REASON](/environment-variables/appcircle-specific-environment-variables#ios--android-common-environment-variables) that specifies the trigger that causes the build to start. <CloudBadge/> <SelfHostedBadge/>
- The "Default M1 Pool" runners have [Xcode 15.1 beta-1](../build/platform-build-guides/building-ios-applications) installed. As this is a beta release, please test your workflows thoroughly. <CloudBadge/> <SelfHostedBadge/>
- A new filter has been added for filtering reports. Users will now be able to filter by organization and sub organization. <CloudBadge/> <SelfHostedBadge/>
- New commands `download` and `load` were introduced to the self-hosted Appcircle server in order to support [offline installation and upgrade](../self-hosted-appcircle/configure-server/offline-installation) scenarios. <SelfHostedBadge/>
- The self-hosted Appcircle server now supports Secure LDAP, aka LDAPS, that encrypts the authentication process for enhanced security. <SelfHostedBadge/>

### :muscle: Improvement

- A parent organization can access its children's "Build History", "Signing History", "App Sharing Report", "Enterprise App Store Reports", and "Queue Waiting Reports". <CloudBadge/> <SelfHostedBadge/>
- Improvements have been made to the [email notification](/account/my-organization/notifications-and-communication/email-connection) format for build events. <CloudBadge/> <SelfHostedBadge/>
- The "Default M1 Pool" has the latest stable [Xcode 15.0.1](https://developer.apple.com/documentation/xcode-release-notes/xcode-15_0_1-release-notes) update available on runners. <CloudBadge/> <SelfHostedBadge/>
- We now support Azure DevOps Server 2020 connection while adding a [build profile](/build/manage-the-connections/adding-a-build-profile/connecting-to-azure). <CloudBadge/> <SelfHostedBadge/>
- The [public link](/distribute/create-or-select-a-distribution-profile#using-public-link-for-distribution) in the test deployment area will now be available regardless of authentication type. <CloudBadge/> <SelfHostedBadge/>
- A bug that prevented failed builds from sending notifications to the MS Teams application has been fixed. <CloudBadge/> <SelfHostedBadge/>
- Previously, you could only select one profile for test deployment. Now you can select [multiple profiles in the distribution](/build/build-process-management/build-profile-configuration#distribution-configuration) profile settings. <CloudBadge/> <SelfHostedBadge/>
- Removed the obsolete icon from the Commit ID redirect link in the build profile details. <CloudBadge/> <SelfHostedBadge/>
- The cache size was bumped to 4 GB while using the [cache push](/workflows/common-workflow-steps/#cache-push) in the build pipeline. <SelfHostedBadge/>
- We made improvements to the self-hosted server [SSL configuration](/self-hosted-appcircle/configure-server/integrations-and-access/ssl-configuration) for enhanced security. <SelfHostedBadge/>
- The [Testinium](/workflows/common-workflow-steps/#testinium) workflow step has the latest improvements from customer feedback and enhanced stability. <CloudBadge/> <SelfHostedBadge/>

### 🐞 Fixed

- Builds that took longer than an hour showed the wrong time on the left side of the screen. This has been fixed. <CloudBadge/> <SelfHostedBadge/>
- While reviewing the build logs in the admin panel, if there is no build log, we were not showing the user an error. Now it is shown as a toast message. <CloudBadge/> <SelfHostedBadge/>
- The bug that occurred if there were no screenshots in the test project has been fixed. <CloudBadge/> <SelfHostedBadge/>
- A problem related to component caching in the runner has been resolved. <CloudBadge/> <SelfHostedBadge/>
- Without user [permission](/account/my-organization#advanced-role-management), requests on the relevant screens are no longer sent to the service, so no warnings are displayed. <CloudBadge/> <SelfHostedBadge/>
- We were not showing the status of the request with the loader when a request was sent for workflows; this problem has been fixed. <CloudBadge/> <SelfHostedBadge/>
- Some spelling errors at the beginning of the workflow have been fixed, and a user-friendly appearance has been provided. <CloudBadge/> <SelfHostedBadge/>
- Fixed a bug that prevented logging in to the Enterprise App Store. <CloudBadge/> <SelfHostedBadge/>
- Fixed the error that occurred when test users emails were written in capital letters. <CloudBadge/> <SelfHostedBadge/>
- In the general profile tab in the [distribution profile](/distribute/create-or-select-a-distribution-profile), the incorrect screen movement that occurred when the switch was disabled and reactivated was fixed. <CloudBadge/> <SelfHostedBadge/>
- Fixed unnecessary requests that go on report screens in the case of being a [sub organization](/account/my-organization#working-with-multiple-organizations). <CloudBadge/> <SelfHostedBadge/>
- Fixed missing versioning for the [HashiCorp Vault](https://blog.appcircle.io/article/security-in-appcircle) container image on the self-hosted server. <SelfHostedBadge/>

## 3.8.0 - 2023-10-02 - Multiple Git Providers Support, Config Clone, Pool-Based Xcode Version Selection

### 🆕 New Feature

- The user can add [multiple instances](/build/manage-the-connections/adding-a-build-profile/connecting-multiple-instance) of the Git providers and select any of them to connect to. So the user can bind and build the repositories. <CloudBadge/> <SelfHostedBadge/>
- The [Xcode version](/self-hosted-appcircle/self-hosted-runner/configure-runner/manage-pools/#pool-based-xcode-version-selection) list of runners is integrated into the custom pool selection. It can be displayed dynamically in the build configuration, and the user can choose which Xcode version to build with. <CloudBadge/> <SelfHostedBadge/>
- You can now quickly [copy a configuration](/build/build-process-management/build-profile-configuration#clone-configuration) and create a new one from that configuration. <CloudBadge/> <SelfHostedBadge/>

### :muscle: Improvement

- Waiting times in Queue Waiting Reports are now shown in minutes instead of seconds. <SelfHostedBadge/>
- If the user selects any step that has the "Continue with the next step even if this step fails" option and gets a failure during the build on that step, this build's status is displayed as [Warning](/workflows/#build-warning-status). <CloudBadge/> <SelfHostedBadge/>
- Fixed the case that users belonging to more than one organization on [Azure DevOps](/build/manage-the-connections/adding-a-build-profile/connecting-to-azure) could not bind repository. <CloudBadge/> <SelfHostedBadge/>
- Improved suborganization experience in the Enterprise App Store by hiding the "Customize" and "Settings" sections, providing a more focused interface for suborganization administrators. <CloudBadge/> <SelfHostedBadge/>
- The latest stable version of [Xcode 15.0](../build/platform-build-guides/building-ios-applications) is available on both cloud and self-hosted runners. <SelfHostedBadge/> <CloudBadge/>
- The self-hosted Appcircle server now supports proxies with a [self-signed certificate.](/self-hosted-appcircle/configure-server/integrations-and-access/proxy-configuration) <SelfHostedBadge/>
- Users can more easily switch to the self-hosted version of their choice by only [downloading](../self-hosted-appcircle/update#1-download-latest) the server package. <SelfHostedBadge/>
- Added the [NTP configuration](../self-hosted-appcircle/self-hosted-runner/runner-vm-setup#2-configure-base-runners-ntp-settings) helper tool to the self-hosted runner package. <SelfHostedBadge/>
- Added self-signed certificate management for Node.JS to the [certificate installer](../self-hosted-appcircle/self-hosted-runner/configure-runner/custom-certificates#adding-certificates) tool. <SelfHostedBadge/>
- Now you can analyze your [SwiftLint](/workflows/ios-specific-workflow-steps/azure-bot-for-swiftlint) and [Detekt](/workflows/android-specific-workflow-steps/) reports and post the report details under the opened PR on Azure DevOps. <CloudBadge/> <SelfHostedBadge/>

### 🐞 Fixed

- Fixed the "Waiting Duration" title in the Queue Waiting Reports header. <SelfHostedBadge/>
- The role management error in the [Apple Devices](/distribute/platform-specific-guidance/ios/apple-devices) section in the Testing Distribution module has been fixed. <CloudBadge/> <SelfHostedBadge/>
- Fixed the issue of not being able to distribute to the selected configuration in the [Testing Distribution](/distribute/create-or-select-a-distribution-profile) module. <CloudBadge/> <SelfHostedBadge/>
- Fixed the issue where the branch list could not be refreshed when the user [permission](/account/my-organization) for the Build module was set to "Read Only Access". <CloudBadge/> <SelfHostedBadge/>
- Fixed the issue where the build does not appear in the list when the build starts. <CloudBadge/> <SelfHostedBadge/>
- Fixed the bug that users without permission were sending requests to the service when browsing pages. <CloudBadge/> <SelfHostedBadge/>
- In the Store Submit module, the "Huawei App ID" field in the Huawei AppGallery section was disabled. It's been fixed. <CloudBadge/> <SelfHostedBadge/>
- Flickering on the screen due to line overlap in the build module has been fixed. <CloudBadge/> <SelfHostedBadge/>
- When an invalid email was entered in the [email integration](/account/my-organization/notifications-and-communication/email-connection) module, other options were reset. It's been fixed. <CloudBadge/> <SelfHostedBadge/>
- The wrong dialog modal was opening in the "never delete" option selected for the deletion of an artifact. It's been fixed, and an extra description has been added. <CloudBadge/> <SelfHostedBadge/>
- When there was a workflow step of the same name, there was a confusion of names. It's has been fixed. <CloudBadge/> <SelfHostedBadge/>
- An error message is now displayed to the user when an invalid workflow name is entered. <CloudBadge/> <SelfHostedBadge/>
- Fixed the data refresh error when the version is deleted in the [Apple Devices](/distribute/platform-specific-guidance/ios/apple-devices) section of the Testing Distribution module. <CloudBadge/> <SelfHostedBadge/>
- Fixed the page crash problem when the user clicks on the [Triggers](/build/build-process-management/build-manually-or-with-triggers). <CloudBadge/> <SelfHostedBadge/>
- Added a toast message that is shown when the user tries to download the deleted configuration in the admin panel. <CloudBadge/> <SelfHostedBadge/>
- The case that selection of the adhoc [auto device register](/distribute/platform-specific-guidance/ios/apple-devices#automatically-adding-registered-devices-to-the-provisioning-profile) on the distribution profile settings has been fixed. <CloudBadge/> <SelfHostedBadge/>

## 3.7.0 - 2023-09-05 - Email Notification, Queue Waiting Reports

### 🆕 New Feature

- We added a new admin report for the queue waiting report. Now self-hosted enterprise customers can see the queue status and waiting durations of each build, fetch, store submit, and resign process. <SelfHostedBadge/>
- You can now send [email notifications](/account/my-organization/notifications-and-communication/email-connection) for most actions taken within Appcircle (build start, store submit, etc.). <CloudBadge/> <SelfHostedBadge/>
- Self-hosted [runner](/self-hosted-appcircle/self-hosted-runner/installation) now supports installation of the latest [Xcode 15.0](/infrastructure/ios-build-infrastructure) release with all its simulator runtimes. Since this is a beta release, please test your workflows extensively. <SelfHostedBadge/>

### :muscle: Improvement

- Removed profile names will now appear as "Deleted" in corporate store reports. <CloudBadge/> <SelfHostedBadge/>
- The active build section now shows the email address that started the build, not the email address of the user who created the profile. <CloudBadge/> <SelfHostedBadge/>
- If there is a space character in the [variable group](/environment-variables/managing-variables#using-environment-variables-for-ssh-and-pat-personal-access-token-connections-of-the-git-provider) name, it can be used within double quotes while connecting the repository. <CloudBadge/> <SelfHostedBadge/>
  - `$"Variable Group:Key"`
- Self-hosted enterprise customers can download the [configurations](/build/build-process-management/build-profile-configuration) of previous builds with the `.yaml` extension in "Build Details" section of the admin panel. <SelfHostedBadge/>
- Unsubscribe and resubscribe features are enabled for email notifications, distribution, and the enterprise app store. <CloudBadge/> <SelfHostedBadge/>

### 🐞 Fixed

- The confusion regarding the use of Turkish characters when creating [workflows](/workflows) and [configurations](/build/build-process-management/build-profile-configuration) has been resolved. Turkish characters and some special characters can no longer be used in this section. <CloudBadge/> <SelfHostedBadge/>
- The error in [permission management](/account/my-organization) in the environment variables section has been fixed. <CloudBadge/> <SelfHostedBadge/>
- The problem with the build transaction texts above the branch name in the "Branch" section being mixed up has been fixed. <CloudBadge/> <SelfHostedBadge/>
- The error in permission management in the [Enterprise App Store](/enterprise-appstore/enterprise-app-store-setup/add-ent-profile) section has been fixed. <CloudBadge/> <SelfHostedBadge/>
- The incorrect display of the inactive steps at the beginning of the build pipeline has been fixed. It was affecting the workflow steps section in the build logs while the build was running. <CloudBadge/> <SelfHostedBadge/>
- The problem of creating groups without a group name and with an existing name on the API's side has been fixed. <CloudBadge/> <SelfHostedBadge/>
- Optional steps won't affect build status anymore. If "Continue with the next step even if this step fails" is selected, your build status will not turn failed. <CloudBadge/> <SelfHostedBadge/>

## 3.6.0 - 2023-08-03 - Azure DevOps Integration, Using Environment Variables On Git Integrations

### 🆕 New Feature

- Now you can connect repositories from [Azure DevOps Services](/build/manage-the-connections/adding-a-build-profile/connecting-to-azure) and Azure DevOps Server for your builds. <CloudBadge/> <SelfHostedBadge/>
- Added support for using [webhook](/account/my-organization/webhooks) with OAuth 2.0 and the Personal Access Token on Azure DevOps. <CloudBadge/> <SelfHostedBadge/>
- The quick add feature has been added to the new project screen for both Azure DevOps Services and Azure DevOps Server. <CloudBadge/> <SelfHostedBadge/>
- LDAP, user lookup decision strategy can be configured in global.yaml. See [LDAP settings](/self-hosted-appcircle/configure-server/integrations-and-access/ldap-settings) for details. <SelfHostedBadge/>

### :muscle: Improvement

- The ability to use information such as [SSH and PAT](/build/manage-the-connections/adding-a-build-profile/connecting-to-private-repository-via-ssh), that is required for adding new projects with SSH has been added with environment variables. <CloudBadge/> <SelfHostedBadge/>
- The [Tag Model](/build/build-process-management/build-manually-or-with-triggers) now includes the name and email of the user who created the tag. <CloudBadge/> <SelfHostedBadge/>
- The self-hosted script can now be called from anywhere in the OS. <SelfHostedBadge/>

### 🐞 Fixed

- Fixed a bug that users were experiencing when adding to the provisioning profile. <CloudBadge/> <SelfHostedBadge/>
- Fixed a bug that caused [endpoints](/appcircle-api/api-authentication) to not appear in the webhook module on Swagger. <CloudBadge/> <SelfHostedBadge/>
- When an event matches the trigger rules, all satisfied triggers will be executed. <CloudBadge/> <SelfHostedBadge/>
- The user is redirected to the "invitation expired" page when the [invitation](/account/my-organization) link is timed out. <CloudBadge/> <SelfHostedBadge/>
- The health check command was fixed, and it now reports the correct state both for Podman and Docker. <SelfHostedBadge/>
- The missing service on the Podman installation was fixed. <SelfHostedBadge/>

## 3.5.0 - 2023-07-13 - Configuration, Workflow Improvements, New Autofill Feature

### 🆕 New Feature

- Added the "Autofill" option when creating a new build profile and connecting it with the service. <CloudBadge/> <SelfHostedBadge/>
- [Xcode 15.0 Beta-4](/infrastructure/ios-build-infrastructure) added to build agents. Since this is a beta release, please test your workflows extensively. <CloudBadge/>

### :muscle: Improvement

- Added the feature that [LDAP](/account/my-organization/ldap-login) and [SSO](/account/my-organization/sso-providers-configuration/single-sign-on) settings can be made once and all sub-organizations can use this setting. <CloudBadge/> <SelfHostedBadge/>
- Previous [Configuration and Workflow](/build/manage-the-connections/adding-a-build-profile) files can be downloaded in the Configuration and Workflow sections. The ability to create configuration and workflow by re-uploading downloaded `.yaml` files has been improved. <CloudBadge/> <SelfHostedBadge/>
- On the [self-hosted](../self-hosted-appcircle/self-hosted-runner) side, the feature of adding priority has been developed for online and offline runners. <CloudBadge/> <SelfHostedBadge/>
- Sequential numbering improvement was made in the naming while creating the new configuration and workflow. <CloudBadge/> <SelfHostedBadge/>
- The ability to send files from the Testing Distribution module to the Enterprise App Store added. <CloudBadge/> <SelfHostedBadge/>
- Made an improvement to prevent the subordinate from accessing the details on the 'corporate settings' page. <CloudBadge/> <SelfHostedBadge/>
- Default M1 Pool is automatically selected in case of [Xcode](/infrastructure/ios-build-infrastructure) version 14.3.x and above. <CloudBadge/>
- Improved the display of device name if there is an available device on the [IOS provisioning](/distribute/platform-specific-guidance/ios/apple-devices) profile side. <CloudBadge/> <SelfHostedBadge/>
- Subtitle would also have to be searched for components. This development has been done. <CloudBadge/> <SelfHostedBadge/>

### 🐞 Fixed

- Fixed an issue where the user could not create a [sub-organization](/account/my-organization) even though they had the required permission. <CloudBadge/> <SelfHostedBadge/>
- Fixed issue with file permissions when exporting a project for self-hosted uses. <SelfHostedBadge/>
- Fixed the problem of adding the same name while uploading the [configuration](/build/manage-the-connections/adding-a-build-profile). <CloudBadge/> <SelfHostedBadge/>
- The permissions of the applications in the Huawei App Gallery that depend on the permission to view the applications in the store submit section has been fixed. <CloudBadge/> <SelfHostedBadge/>
- The problem that the save button is not active after the changes made in the organization pool has been fixed. <CloudBadge/> <SelfHostedBadge/>
- Fixed a double slash (`//`) bug on the webhook link that caused the triggers to not work. <CloudBadge/> <SelfHostedBadge/>
- The error that the change indicator appears even though there is no change in some tabs in the config modal has been fixed. <CloudBadge/> <SelfHostedBadge/>
- Apple Devices improved, not sending device enrollment link if auto enrollment is disabled. <CloudBadge/> <SelfHostedBadge/>
- Fixed configuration creation error without giving any name. <CloudBadge/> <SelfHostedBadge/>
- Fixing UI bugs in search field in [Testing Distribution](/distribute/create-or-select-a-distribution-profile) module. <CloudBadge/> <SelfHostedBadge/>
- Fixed a bug that caused triggers to be deleted. <CloudBadge/> <SelfHostedBadge/>
- The error that the save button is not active when I change the [offset](../versioning/ios-version) part of the build number has been fixed. <CloudBadge/> <SelfHostedBadge/>
- Fixed unsigned owners error on files that are not resigned in test deployment part. <CloudBadge/> <SelfHostedBadge/>
- Fixed some icons appearing properly in dark mode. <CloudBadge/> <SelfHostedBadge/>

## 3.4.0 - 2023-06-09 - Build Profile Improvements, Azure Boards

### 🆕 New Feature

- [Xcode 15.0 Beta](/infrastructure/ios-build-infrastructure) added to build agents. Since this is a beta release, please test your workflows extensively. <CloudBadge/> <SelfHostedBadge/>
- [Java 17](../infrastructure/android-build-infrastructure) added to build agents. <CloudBadge/> <SelfHostedBadge/>
- [Build Profile](/build/manage-the-connections/adding-a-build-profile) configurations are separated from branchs. It is now easier to see and manage configs from a single location. <CloudBadge/> <SelfHostedBadge/>
- [SSO](/account/my-organization/sso-providers-configuration/single-sign-on) and [LDAP](/account/my-organization/ldap-login) Login added to Testing Distribution. <CloudBadge/> <SelfHostedBadge/>
- [Azure Boards](/workflows/common-workflow-steps/azure-board) workflow step added. <CloudBadge/> <SelfHostedBadge/>
- [Repeato](/workflows/common-workflow-steps/#repeato-mobile-test-automation) workflow step added. <CloudBadge/> <SelfHostedBadge/>
- [Snyk Secure Scan](/workflows/common-workflow-steps/#snyk-scan-security) workflow step added. <CloudBadge/> <SelfHostedBadge/>

### :muscle: Improvement

- [Xcode Build for Simulator](/workflows/ios-specific-workflow-steps/#xcodebuild-for-ios-simulator) workflow step updated. The new version allows you to create both x86_64 and arm64 simulator builds. This step can optionally install the simulator builds to run UI tests on the simulator. <CloudBadge/> <SelfHostedBadge/>
- [Test Report](/continuous-testing/ios-testing/running-ios-unit-and-ui-tests) step tries to parse JUnit files if it can't find .xctestresult files. This can be useful if your testing framework(BrowserStack, Repeato, etc.) is producing JUnit reports. <CloudBadge/> <SelfHostedBadge/>
- [Wait for Android Emulator](/workflows/android-specific-workflow-steps/#wait-for-android-emulator) step updated to install optional APK after the emulator boots. <CloudBadge/> <SelfHostedBadge/>
- The default Xcode version is bumped to 14.2 for new projects. <CloudBadge/> <SelfHostedBadge/>
- Sub-organizations can see their download reports. <CloudBadge/> <SelfHostedBadge/>
- Build configuration screen is improved. Changing the tabs no longer resets the configuration. <CloudBadge/> <SelfHostedBadge/>
- Build trigger screen is improved. <CloudBadge/> <SelfHostedBadge/>
- [Self-hosted Runer](/self-hosted-appcircle/self-hosted-runner/installation) installation script updated for new Xcode versions and other tools. <SelfHostedBadge/>
- The default configuration file that contains [Self-hosted Server](../self-hosted-appcircle/install-server/docker) settings is simplified. <SelfHostedBadge/>
- The [Self-hosted Server](../self-hosted-appcircle/install-server/docker) package has a text file that contains a list of container services. <SelfHostedBadge/>
- [Self-hosted Server](../self-hosted-appcircle/install-server/docker) Podman support added. <SelfHostedBadge/>
- [Self-hosted Server](../self-hosted-appcircle/install-server/docker) installation script `version` command updated to fix Podman compatibility. <SelfHostedBadge/>
- New script added [Self-hosted Server](../self-hosted-appcircle/install-server/docker) installation package. This script allows users to add and trust their custom self-signed certificates. <SelfHostedBadge/>
- New script added [Self-hosted Server](../self-hosted-appcircle/install-server/docker) installation package. This script allows users to add and trust their custom self-signed certificates. <SelfHostedBadge/>

### 🐞 Fixed

- Strict URL check is removed when users try to add Azure repositories. <CloudBadge/> <SelfHostedBadge/>
- An error that was occurring when you tried to add a sub-org on self-hosted Appcircle is fixed. <SelfHostedBadge/>
- Some minor cases that were occurring on the [Self-hosted Server](../self-hosted-appcircle/install-server/docker) boot process are fixed. <SelfHostedBadge/>

## 3.3.2 - 2023-05-10 - Xcode 14.3,FTP Upload

### 🆕 New Feature

- [Xcode 14.3](/infrastructure/ios-build-infrastructure) added to build agents. Since Xcode 14.3 only runs on Ventura, M1 infrastructure is also updated. Please test your workflows extensively. <CloudBadge/> <SelfHostedBadge/>
- [FTP Upload](/workflows/common-workflow-steps/#ftp-upload) workflow step added. <CloudBadge/> <SelfHostedBadge/>

### :muscle: Improvement

- [Data Theorem Mobile Secure](/workflows/common-workflow-steps/#data-theorem-mobile-secure) workflow step updated. <CloudBadge/> <SelfHostedBadge/>
- New options added to [Android Resign](/distribute/platform-specific-guidance/android/resigning-android-binaries). <CloudBadge/> <SelfHostedBadge/>
- Sub-organizations can see their download reports. <CloudBadge/> <SelfHostedBadge/>
- Build configuration screen is improved. Changing the tabs no longer resets the configuration. <CloudBadge/> <SelfHostedBadge/>
- Build trigger screen is improved. <CloudBadge/> <SelfHostedBadge/>

### 🐞 Fixed

- Fixed a bug that makes users unable to add their GitHub repositories. <CloudBadge/> <SelfHostedBadge/>

## 3.3.0 - 2023-04-27 - Data Theorem Mobile Secure, App Center CodePush

### 🆕 New Feature

- [Data Theorem Mobile Secure](/workflows/common-workflow-steps/#data-theorem-mobile-secure) workflow step added. <CloudBadge/> <SelfHostedBadge/>
- [App Center CodePush](/workflows/react-native-specific-workflow-steps/#app-center-codepush) workflow step added. <CloudBadge/> <SelfHostedBadge/>
- Latest five build status added to build profile. <CloudBadge/> <SelfHostedBadge/>
- [Slack Bot](/account/my-organization/notifications-and-communication/slack/appcircle-bot-for-slack) added. <CloudBadge/>

### :muscle: Improvement

- SVG images are updated <CloudBadge/> <SelfHostedBadge/>
- Build profile card design is improved. <CloudBadge/> <SelfHostedBadge/>
- Color scheme and icons are updated for dark themes. <CloudBadge/> <SelfHostedBadge/>
- Lots of UI and text improvements were made for better UX. <CloudBadge/> <SelfHostedBadge/>

### 🐞 Fixed

- Huawei AppGallery submission bug fixed. <SelfHostedBadge/>
- [Enterprise App Store](/enterprise-appstore/enterprise-app-store-setup/customize-ent-store) The background image bug was fixed on the login page. <SelfHostedBadge/>
- Fixed a bug that makes users unable to login to the enterprise app store in some cases. <CloudBadge/>
- Fixed a bug that gives an unexpected error on project `export` on self-hosted server installations. <SelfHostedBadge/>
- Fixed a bug that gives an unexpected error on project `up` when there is no vault image in the system. <SelfHostedBadge/>
- The default license duration for the self-hosted package is updated to 3 months for demo use cases. <SelfHostedBadge/>
- Fixed broken tag triggers which was missing to start build on some cases. <CloudBadge/> <SelfHostedBadge/>
- Store submit workflows are updated for the latest Fastlane version. <CloudBadge/> <SelfHostedBadge/>

## 3.2.0 - 2023-04-07 - Resign, Sub Organizations

### 🆕 New Feature

- [Resigning](/distribute/platform-specific-guidance/ios/resigning-ios-binaries) iOS and Android binaries added to Test Distribution module. <CloudBadge/> <SelfHostedBadge/>
- Enterprise customers can create [sub organizations](/account/my-organization) to manage their users. <CloudBadge/> <SelfHostedBadge/>
- [App Center iOS Distribution](/workflows/ios-specific-workflow-steps/#app-center-ios-distribution) workflow step added. <CloudBadge/> <SelfHostedBadge/>
- [App Center Android Distribution](/workflows/android-specific-workflow-steps/#app-center-android-distribution) workflow step added. <CloudBadge/> <SelfHostedBadge/>

### :muscle: Improvement

- Build profile list UI is improved <CloudBadge/> <SelfHostedBadge/>
- Extra notes added to [SSH](/build/manage-the-connections/adding-a-build-profile/connecting-to-private-repository-via-ssh) key generation for Windows users. <CloudBadge/> <SelfHostedBadge/>
- User's default branch is listed at the top. <CloudBadge/> <SelfHostedBadge/>

### 🐞 Fixed

- GitLab double trigger bug fixed. <CloudBadge/> <SelfHostedBadge/>
- GitLab Self-Hosted access token now longer shows inside build logs. <CloudBadge/> <SelfHostedBadge/>
- [Enterprise App Store](/enterprise-appstore/enterprise-app-store-setup/customize-ent-store) 2FA Safari bug fixed. <SelfHostedBadge/>
- [Enterprise App Store](/enterprise-appstore/enterprise-app-store-setup/customize-ent-store) localization bug fixed. <CloudBadge/> <SelfHostedBadge/>
- [Enterprise App Store](/enterprise-appstore/enterprise-app-store-setup/customize-ent-store) Download bug is fixed for slow networks. <SelfHostedBadge/>

## 3.1.0 - 2023-03-17 - StoreSubmit, Self-hosted Improvements

### 🆕 New Feature

- Submissions to Google Play Console and Huawei AppGallery will now begin from the build agents. <CloudBadge/> <SelfHostedBadge/>
- It is now possible to localize some login form texts on the [Enterprise App Store](/enterprise-appstore/enterprise-app-store-setup/customize-ent-store) when LDAP login is activated. <SelfHostedBadge/>

### :muscle: Improvement

- [Enterprise App Store](/enterprise-appstore/enterprise-app-store-setup/customize-ent-store) language selection page is improved. <CloudBadge/> <SelfHostedBadge/>
- `AC_COMMIT_AUTHOR_EMAIL`, `AC_COMMIT_SUBJECT`, and `AC_COMMIT_MESSAGE` [Environment Variables](/environment-variables/appcircle-specific-environment-variables) added to build agents. <CloudBadge/> <SelfHostedBadge/>
- Unauthenticated internal SMTP server support added for Self-Hosted Appcircle. <SelfHostedBadge/>
- `global.yaml` content is improved with new configuration options. <SelfHostedBadge/>
- Confusing initial `user-secret` file generation is removed. <SelfHostedBadge/>
- New command line parameters added for Self-Hosted Appcircle CLI. <SelfHostedBadge/>

### 🐞 Fixed

- Huawei AppGallery App ID saving bug fixed. <CloudBadge/> <SelfHostedBadge/>
- [Enterprise App Store](/enterprise-appstore/enterprise-app-store-setup/customize-ent-store) 2FA login bug fixed. <CloudBadge/> <SelfHostedBadge/>
- Appcircle now shows a warning if it can't reach your repository due to network problems. <CloudBadge/> <SelfHostedBadge/>
- Fixed broken downloads on Enterprise App Store when an app has a name in non-ASCII characters. <CloudBadge/> <SelfHostedBadge/>
- Minor localization fixes were done on Enterprise App Store for the Turkish language. <CloudBadge/> <SelfHostedBadge/>
- Minor fixes were done on SSH key format and SSH repo connections. <CloudBadge/> <SelfHostedBadge/>
- Enterprise App Store settings' broken UI fixed when the custom domain is disabled. <SelfHostedBadge/>
- Dashboard no longer shows builds started for store submission. <CloudBadge/> <SelfHostedBadge/>
- Dashboard no longer shows builds from deleted build profiles. <CloudBadge/> <SelfHostedBadge/>

## 3.0.1 - 2023-02-28 - AppSweep, Self-hosted Improvements

### 🆕 New Feature

- [AppSweep Mobile Security Testing](/workflows/android-specific-workflow-steps/#appsweep-mobile-security-testing) component added. <CloudBadge/> <SelfHostedBadge/>
- [Self-signed certificate](/self-hosted-appcircle/configure-server/integrations-and-access/ssl-configuration) support added for Testing Distribution. <SelfHostedBadge/>
- [Enterprise App Store](/enterprise-appstore/enterprise-app-store-setup/customize-ent-store) is now available in German and Turkish languages in addition to English. To switch to your preferred language, simply navigate to the language settings on your store homepage and select either German or Turkish. <CloudBadge/> <SelfHostedBadge/>
- [New APIs](https://api.appcircle.io/openapi/index.html?urls.primaryName=enterprisestore) are added to directly download IPA or APK files from Enterprise App Store by using a PAT. <CloudBadge/> <SelfHostedBadge/>

### :muscle: Improvement

- New line is added to SSH private key if it doesn't exist. <CloudBadge/> <SelfHostedBadge/>
- API key selection is now mandatory for all app submissions on Google Play. <CloudBadge/> <SelfHostedBadge/>
- Autofill button respects the selected pool. <CloudBadge/> <SelfHostedBadge/>
- Self-hosted GitLab onboarding screen is improved. <CloudBadge/> <SelfHostedBadge/>
- Default pools are removed from Self-hosted instances. <SelfHostedBadge/>

### 🐞 Fixed

- Email address parse error fixed for Distribution profiles. <CloudBadge/> <SelfHostedBadge/>
- Test reports are correctly created for branches even if they don't have any configuration. <CloudBadge/> <SelfHostedBadge/>
- Dashboard no longer shows builds started with autofill. <CloudBadge/> <SelfHostedBadge/>
- Cache pull and Cache Pull components are fixed. <SelfHostedBadge/>
- [Enterprise App Store](/enterprise-appstore/enterprise-app-store-setup/customize-ent-store) live and beta channels access managament bug fixed <CloudBadge/> <SelfHostedBadge/>
- Store Submit permission bug fixed. <SelfHostedBadge/>

## 3.0.0 - 2023-02-14 - LDAP, Self-hosted Improvements

### 🆕 New Feature

- [Multiple LDAP](/enterprise-appstore/enterprise-app-store-setup/customize-ent-store#ldap-login) support added for Enterprise App Store. <CloudBadge/> <SelfHostedBadge/>
- [Self-signed certificate](/self-hosted-appcircle/configure-server/integrations-and-access/ssl-configuration) support added for Appcircle server. <SelfHostedBadge/>
- [Self-signed certificate](/self-hosted-appcircle/configure-server/integrations-and-access/ssl-configuration) support added for external services such as Git providers (GitLab, Bitbucket etc.) <SelfHostedBadge/>

### :muscle: Improvement

- Onboarding of React Native Android project is improved. <CloudBadge/> <SelfHostedBadge/>
- Flutter iOS build component improved. <CloudBadge/> <SelfHostedBadge/>
- [Feedback form](https://my.appcircle.io/help) added to help section. <CloudBadge/> <SelfHostedBadge/>
- CSS and icon handling is updated to improve the performance of the Enterprise App Store. <CloudBadge/> <SelfHostedBadge/>
- Self-hosted instances can be installed from a single Docker registry. <SelfHostedBadge/>
- Self-hosted instances can start without an active internet connection. <SelfHostedBadge/>
- Public and SSH repository options are added to default profile options. <SelfHostedBadge/>
- Improvements were made to the logging system to prevent big log files. <SelfHostedBadge/>

### 🐞 Fixed

- Enterprise app store cache related bugs were fixed. <CloudBadge/> <SelfHostedBadge/>
- SMTP bugs were fixed for server notifications. <SelfHostedBadge/>

## 2.9.23 - 2023-02-02 - LDAP, Jira, Microsoft Teams

### 🆕 New Feature

- [LDAP Login](/enterprise-appstore/enterprise-app-store-setup/customize-ent-store#ldap-login) added to Enterprise App Store.
- [Jira](/workflows/common-workflow-steps/jira-comment) component added.
- [Microsoft Teams](/account/my-organization/notifications-and-communication/teams-notifications) integration added.
- [Gradle Runner](/workflows/android-specific-workflow-steps/#gradle-runner) component added.
- [Maestro Cloud Upload](/workflows/common-workflow-steps/#maestro-cloud-upload) component added.

### :muscle: Improvement

- UI improvements for the
- Build profile based device registration added to Ad Hoc provisioning profiles.

### 🐞 Fixed

- [iOS Version and Build Number Increment](../versioning/ios-version) component gracefully exits if it can't update the project.

## 2.9.22 - 2023-01-16 - Adhoc Improvements

### 🆕 New Feature

- [Apple Devices](/distribute/platform-specific-guidance/ios/apple-devices) section will allow you to easily register new devices and add them to Ad Hoc provisioning profiles.
- [Firebase Deployment ]/workflows/flutter-specific-workflow-steps/firebase-deployment) component added.

### :muscle: Improvement

- [Firebase App Distribution](/workflows/common-workflow-steps/#firebase-app-distribution) component support service account.
- UI improvements for the custom script editor.

### 🐞 Fixed

- If you revert a commit and force push it, Appcircle will correctly handle this situation.

## 2.9.21 - 2022-12-28 - BrowserStack App Automate

### 🆕 New Feature

- [BrowserStack App Automate - Espresso](/workflows/android-specific-workflow-steps/#browserstack-app-automate---espresso) component added
- [BrowserStack App Automate - XCUI](/workflows/ios-specific-workflow-steps/#browserstack-app-automate---xcui) component added

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

- [Testinium](/workflows/common-workflow-steps/#testinium) component added. This component allows you to run your test plans on [Testinium](https://testinium.com)
- [Firebase dSYM Upload](/workflows/ios-specific-workflow-steps/firebase-upload-dsym) component added. You may use this component to upload Debug Symbols to Firebase.

### :muscle: Improvement

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

<ContentRef url="/build/manage-the-connections/accessing-repositories-in-internal-networks-firewalls/">
Accessing Repositories in Internal Networks (Firewalls)
</ContentRef>

**Intel Pool**:

If your builds fail on M1 pool or if you’re not ready for the M1 migration, please go to your branch’s config screen and choose Default Intel Pool from the dropdown menu.

## 2.9.17 - 2022-12-01 - Test Reports

### 🆕 New Feature

- Test Reports added for [iOS](/continuous-testing/ios-testing/running-ios-unit-and-ui-tests) and [Android](/continuous-testing/android-testing/running-android-unit-tests). Please check their documentation to learn how to set up your workflows.
- [Danger](/workflows/common-workflow-steps/#code-reviews-with-danger) component added. Danger runs during your CI process and gives teams the chance to automate common code review chores
- The emulator feature is removed.

### :muscle: Improvement

- Performance improvements for the Dashboard
- Announcement button ⚡️ added to Dashboard. You can check that section for product announcements.
- Wildcard Provisioning Profile support for manual code signing
- Setting environment variables via the `AC_ENV_FILE_PATH` environment variable now works on failed steps as well.
- Xcode versions older than 12.5 removed.

## 2.9.16 - 2022-10-07 - Triggers fallback config, Netrc, Bundlletool and Detekt components

### 🆕 New Feature

- [Fallback config](/build/build-process-management/build-manually-or-with-triggers) added for Pull/Merge Requests and Tag triggers.
- [Netrc component](/workflows/common-workflow-steps) You can use this component to add credentials for hosts such as your repositories or external hosts.
- [Bundletool Component](/workflows/android-specific-workflow-steps) You can use this component to create universal apk from the aab.
- [Detekt](/workflows/android-specific-workflow-steps) You can use this component to run your detekt gradle task.

### :muscle: Improvement

- [Added FAQs](/troubleshooting-faq/common-issues) related to Xcode 14 and code signing errors.

## 2.9.15 - 2022-09-30 - Fortify On Demand and Firebase App Distribution components

### 🆕 New Feature

- [Fortify On Demand Component](/workflows/common-workflow-steps) You can use Fortify On Demand uploader for all your projects.
- [Firebase App Distribution Component](/workflows/common-workflow-steps) You can use Firebase App Distribution to distribute your builds.
- [Wait for Android Emulator](/workflows/android-specific-workflow-steps) You must use this step before your UI tests to wait for the Android emulator to start.

### :muscle: Improvement

- Navigation and repository refresh speed improved.,
- Linux agents are more powerful now. They also support nested virtualizations therefore you may use Android emulators.
- Xcode default version number is changed to 13.4.x
- Android Emulator added to agents. The added emulator is based on Android 9.0 image. You may install additional emulators by using `sdkmanager`. Please check [Android Infrastructure](../infrastructure/android-build-infrastructure) to learn more. In order to use the emulator, you need to add the Wait for Android Emulator step to your workflow.

### 🐞 Fixed

- Bitbucket commit messages now show properly.
- `AC_PULL_NUMBER` environment variable added for Pull/Merge Requests.
- Changing assignee no longer triggers a build for GitLab Merge Request.
- Build statuses correctly shows on the main dashboard.

## 2.9.14 - 2022-08-18 - New Dashboard, Appium Server and SwiftLint components

### 🆕 New Feature

- [New Dashboard](https://my.appcircle.io) Appcircle has a brand new dashboard that shows an overview of your account.
- [Artifacts Management](/account/my-organization/artifacts) You can set the retention period for your build artifacts.
- [Appium Server Component](/workflows/common-workflow-steps) You can use Appium Server for iOS and Android projects.
- [SwiftLint Component](/workflows/ios-specific-workflow-steps) You can use Swiftlint for iOS projects.

### :muscle: Improvement

- Empty states are added for all modules.
- [Self-Hosted Runners](../self-hosted-appcircle/self-hosted-runner) Self hosted documentation updated.
- Docs updated to Docusaurus v2.0.1

### 🐞 Fixed

- Sharing Simulator URL fixed.

## 2.9.13 - 2022-07-27 - Self-hosted Runners, Artifacts Management, Automatic iOS Code Signing

### 🆕 New Feature

- [Self-Hosted Runners](../self-hosted-appcircle/self-hosted-runner) Self-hosted runner enables you to use your own systems and infrastructure for running Appcircle build pipelines.
- [Automatic iOS Code Signing](/signing-identities/ios-certificates-and-provisioning-profiles) If you're using Xcode 13 or later, you can now use the automatic code signing option to automatically sign your iOS apps.
- [Artifacts Management](/account/my-organization/artifacts) You can set the retention period for your build artifacts.
- [SonarQube Component](/workflows/common-workflow-steps) You can use SonarQube for iOS and Android projects.

### :muscle: Improvement

- Slack messages updated to include store name and distribution links.
- Android v2 signing support improved.

### 🐞 Fixed

- `Get help with build errors` link fixed.
- Renaming build profiles fixed.

## 2.9.12 - 2022-07-07 - Android Version Management, Enterprise App Store Improvements

### 🆕 New Feature

- [Android Versioning](../versioning/android-version) You can manage version code and version name directly with UI.
- [Enterprise App Store](/enterprise-appstore/enterprise-app-store-setup/customize-ent-store) You can change the display picture of your apps.

### :muscle: Improvement

- Added Open menu to actions list on build profiles.
- [Enterprise App Store](../enterprise-appstore/enterprise-reports) App usage reports update more frequently.
- [My Organization](/account/my-organization) Access Management document updated.

### 🐞 Fixed

- Creating a new branch without a commit was not triggering a build. This is fixed.
- SSO UI issues fixed
- Android Build Tools 31.0.0 corrupted error message fixed.

## 2.9.11 - 2022-06-20 - Release Notes Component, Enterprise App Store Improvements

### 🆕 New Feature

- [Release Notes Component](/workflows/common-workflow-steps/publish-release-notes) You can create release notes with Publish Release Notes component.
- [Enterprise App Store](/enterprise-appstore/enterprise-app-store-setup/customize-ent-store) Certificate Details added to Enterprise App Store.
- [Enterprise App Store](../enterprise-appstore/enterprise-reports) Detailed reports are added to Enterprise App Store.
- [Open API](https://api.appcircle.io/openapi/index.html?urls.primaryName=signing-identity) New API endpoints added to Certificate and Provisioning profiles upload.
- [Open API](https://api.appcircle.io/openapi/index.html?urls.primaryName=build) New API endpoint added to start a build with provided environment variables.

### :muscle: Improvement

- [iOS Stack](/infrastructure/ios-build-infrastructure) Monterey is upgraded to 12.4 for macOS agents.
- Log window is improved. It is more performant and stable.
- Added [FAQ section](/troubleshooting-faq/common-issues#issues-in-connecting-to-the-repositories-with-ssh) for multiple SSH keys.

### 🐞 Fixed

- Store Submit logs show properly.

## 2.9.10 - 2022-05-31 - iOS Version Management, Enterprise App Store Customizations

### 🆕 New Feature

- [Enterprise App Store Customizations](https://docs.appcircle.io/enterprise-appstore/customize-ent-store). You can connect your subdomain as Enterprise App Store.
- [NodeJS Version Selection](https://docs.appcircle.io/build/building-react-native-applications#build-configuration-for-react-native-ios-applications) You can now directly set the NodeJS version on config screen.
- [Flutter Version Selection](https://docs.appcircle.io/build/building-flutter-applications#how-to-set-a-specific-flutter-version-for-the-build) You can now directly set the Flutter version on the config screen.
- [iOS Versioning](https://docs.appcircle.io/versioning/ios-version) You can manage build and version numbers directly with UI.

### :muscle: Improvement

- [Android Stack](https://docs.appcircle.io/infrastructure/android-build-infrastructure) Android Build Infrastructure updated. Now the default JAVA version is 11.
- [iOS Stack](https://docs.appcircle.io/infrastructure/ios-build-infrastructure) iOS Build Infrastructure updated. Xcode 13.4 added to iOS agents.
- [Workflow Management](https://docs.appcircle.io/workflows/#setting-up-workflows) You can now import or export your workflows as a YAML file.
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

- Huawei App Gallery support added. You can submit your apk or aab files to Huawei AppGallery.
- Java 11 added to iOS agents
- [Slather](https://docs.appcircle.io/workflows/ios-specific-workflow-steps#slather),[Tuist](https://docs.appcircle.io/workflows/ios-specific-workflow-steps#tuist) and Badge components added
- You can now see all your running builds from the status bar and cancel them.
- [Skip the Workflow](https://docs.appcircle.io/build/build-process-management/build-manually-or-with-triggers/#skipping-a-workflow) if the commit message includes `[skip ci]` or `[ci skip]`
- [Retry Merge/Pull Request workflow](https://docs.appcircle.io/build/build-process-management/build-manually-or-with-triggers/#retrying-a-workflow) if the comment includes `[retry]`

### :muscle: Improvement

- [Triggers updated](https://docs.appcircle.io/build/build-process-management/build-manually-or-with-triggers/#auto-build-on-every-push). You can use a default config for new branches. You no longer need to configure every branch.
- [New environment variables](https://docs.appcircle.io/environment-variables/appcircle-specific-environment-variables/) added for commit message, build number, PR number, time stamp.
- You can now download build logs directly from the menu.
- [Node Install](https://docs.appcircle.io/workflows/react-native-specific-workflow-steps#install-node) step uses `lts` version as default.
- Error messages are clarified for build permissions.

### 🐞 Fixed

- GitLab Merge Request Webhook fixed
- Browser UI issues fixed
- Sometimes progress bar was showing on the wrong branch. Fixed.

### 📑 Documentation

- Added Huawei App Gallery section for sending your apps to Huawei App Gallery.
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

<ContentRef url="/account/my-organization/api-integrations/adding-an-app-store-connect-api-key">Adding an App Store Connect API Key</ContentRef>

After adding an API Key, you can add new signing identities from the Signing Identities section. For more information on how to add identities and use them, check out [Signing Identities guide](https://docs.appcircle.io/signing-identities/ios-certificates-and-provisioning-profiles#1-get-ios-certificates-and-provisioning-profiles-from-apple).

### 🆕 New Feature

- Flutter version `2.5.0` is released in their stable channel. You can now use this latest stable version on Appcircle.

## 2.5.0 - 2021-08-27 - Two Factor Authentication, Self Hosted GitLab and Bitbucket, Xcode 13 Beta 5

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

Within this release as prior to the previous release, Appcircle also supports [Xcode 13 Beta 4](https://developer.apple.com/documentation/xcode-release-notes/xcode-13-release-notes). When 13.0.x from the Xcode Version is selected, the Xcode version will be Xcode 13 Beta 4.

### 🆕 New Feature

- iOS builds will be using Xcode 13 Beta 4 if 13.0.x is selected as Xcode version.
- Added metadata (Organization ID, OS version etc.) at the beginning of the Build Logs
- While manually building the workflow, Appcircle now lets you choose which workflow to trigger:

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (215).png' />

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

Within this release, Appcircle now supports [Xcode 13 Beta 2](https://developer.apple.com/documentation/xcode-release-notes/xcode-13-release-notes). When 13.0.x from the Xcode Version is selected, it will be using Xcode 13 Beta 2.

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

<ContentRef url="/build/manage-the-connections/accessing-repositories-in-internal-networks-firewalls">
  Accessing Repositories in Internal Networks (Firewalls)
</ContentRef>

### 🐞 Fixed

- Fixed a bug that **Config **section appearing disabled when connected to the repository for the first time
- Fixed a bug that causes Store Submit modules to not show correct progress while the upload is in progress.

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
- Whitelist IPs are under update process, you can follow the process under [Accessing Repositories in Internal Networks](https://docs.appcircle.io/build/manage-the-connections/accessing-repositories-in-internal-networks-firewalls/) document.

### 🐞 Fixed

- Fixed a bug that the same commit not appearing on multiple branches.
- Fixed a bug that new SSH connections being unable to fetch config.;

## 2.1.5 - 2021-05-10 - GitHub App for Repository Connections

This release includes the release of Appcircle GitHub app and the share app previews along with feature improvements.

### 🆕 New Feature

- [Appcircle GitHub App](/build/manage-the-connections/adding-a-build-profile/connecting-to-github) - You can now connect to GitHub with the Appcircle GitHub app as an alternative to the oAuth connection.
- [Share App Preview Links](/distribute/create-or-select-a-distribution-profile#auto-send-your-build-to-the-testers) - You can now share in-browser app preview links automatically with the testers as an alternative to app binaries. No physical device needed for testing.

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

- [Repository-level workflows](/workflows) - You can now define multiple workflows in a build profile and assign them to multiple branches or assign multiple workflows to the same branch. You can also clone workflows for easier management.
- [Repository-level triggers](/build/build-process-management/build-manually-or-with-triggers) - You can now specify triggers in the build profile level with wildcards for branch names and workflow selection for each trigger for higher flexibility and manageability of the build profiles.
- [Pull request/merge request triggers](/build/build-process-management/build-manually-or-with-triggers#auto-build-pullmerge-requests) - You can now trigger builds whenever you initiate a pull request or merge request from a source branch to the target branch. The build will be done with the pull/merge result. This allows testing the PR/MR result before the actual approval of the request.

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
- Appcircle Distribute API - On top of the previously released build APIs, the Testing Distribution APIs are now available for programmatic access.
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
- Personal API Token - You can generate a token to access the Appcircle API
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
