---
title: Latest Release Notes
metaTitle: Latest Release Notes
metaDescription: Latest Release Notes
sidebar_position: 1
---

import ContentRef from '@site/src/components/ContentRef';

# Latest Release Notes

## 2.9.13 - 2022-07-27 - Self-hosted Runners, Artifacts Management, Automatic iOS Code Signing

### 🆕 New Feature
- [Self-Hosted Runners](../self-hosted-runner/overview.md) Self-hosted runner enables you to use your own systems and infrastructure for running Appcircle build pipelines. 
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

- [Appcircle GitHub App](../build/adding-a-build-profile/#connecting-to-a-cloud-git-provider-github-bitbucket-and-gitlab) - You can now connect to GitHub with the Appcircle GitHub app as an alternative to the oAuth connection.
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
