---
title: Archived Release Notes (v0.x)
metaTitle: Archived Release Notes (v0.x)
metaDescription: Archived Release Notes (v0.x)
sidebar_position: 2
---
# Archived Release Notes (v0.x)

## 1.0.0 - 2020-09-23 - Initial Release

We are excited to announce that Appcircle beta is complete and it is fully released with version 1.0. You can now use Appcircle with full set of features.

This is of course just a start of a long journey. Follow us on Twitter [@appcircleio](https://twitter.com/appcircleio) for updates.

For any questions, feedback or feature requests, just drop us a message using the in-app messaging or raise an issue in Appcircle GitHub: [https://github.com/appcircleio](https://github.com/appcircleio)

### ;🆕 New Feature

* Send apps to Public Stores - You can now send your apps to App Store Connect through the App Store Connect API.;
* Theme support with Dark Mode - There is an Appcircle for everyone. You can now select between Light, Dark and the Darker modes.
* Upload to Amazon S3 step - You can now deploy any file or folder to an Amazon S3 bucket with the new workflow step.

### :muscle:Improvement

* Xcode 12 GM support;
* User experience improvements in line with the theme support

### 🐞 Fixed

* Multimodule support fix
* Billing plan fixes
* State preservation fixes

## 0.9.9 - 2020-09-07 - Last Mile Update

This release includes the last mile changes in the platform.

### ;🆕 New Feature

* GitLab Support - You can now connect to your GitLab repositories just like GitHub and BitBucket.
* Plan Upgrades - The plan upgrades are now available. You can upgrade to a higher [Appcircle plan](https://appcircle.io/pricing) of your choosing for larger workloads and organizations. (The free tier is being preserved as is.)
* Dashboard - The platform is now accessed with a dashboard
* Flutter iOS simulator support - Flutter iOS builds can now be run on the Appcircle iOS simulator (preview on device).

### :muscle:Improvement

* Enriched Slack message format
* AAB file support in the Testing Distribution for Google Play uploads;

### 🐞 Fixed

* Google Play upload fixes
* iOS simulator build fixes
* Further log viewer fixes
* Billing interface fixes

## 0.9.5 - 2020-08-22 - Upload to Public Stores, Slack Notifications and Billing Interface

This release brings in the initial versions of some of the long-awaited features.

### ;🆕 New Feature

* Send apps to Public Stores - You can now send your apps to Google Play Dashboard (App Store Connect support coming in the next release)
* Slack notifications - You can now send build start and end status to a selected Slack channel
* Billing and plan interface - The plan features and the limits and consumption amounts are now visible in the Billing dashboard under the organization
* Fastlane step - Fastlane is added as an optional workflow step. You can now opt in to use Fastlane in your builds

### :muscle:Improvement

* Selective downloads for build artifacts
* Reports interface improvements
* Improved help texts and guidance across the product

### 🐞 Fixed

* App download issues related with the CDN
* Log viewer fixes

## 0.9 - 2020-07-28 - Firebase Test Lab, Log Viewer and Files as Environment Variables

This is a feature release along with a specific focus on storage-related improvements.

### ;🆕 New Feature

* New log viewer - The log viewer is redesigned with a new viewer engine. It's now faster and less resource-consuming and provides an improved viewing experience with
  * Step-based outline
  * Log Map
  * Multi-colored text
  * Inline text finder
* Files as environment variables - You can now add any type of file as an environment variable. (e.g. for keys in JSON format.)
* Firebase Test Lab support for Android - You can add Firebase Test Lab as a workflow step in Android apps to run continuous tests

### :muscle:Improvement

* Increased performance for artifact and app downloads with a new CDN
* Increased security for signing identity and secret storage with Vault

### 🐞 Fixed

* An issue where certain types of keystores caused a signing error
* Flutter build configuration saving issue
* Issues in environment variable creation

## 0.8.5 - 2020-07-20 - Maintenance Release

This is a maintenance release with under-the-hood experience and performance improvements.

### ;🆕 New Feature

* File support in environment variables - You can now add files as environment variables and use them in the build workflows (e.g. key files in JSON format or scripts)
* Build status in the branch list - You can now see the last build status of each branch in the branch list;

:::info


**Known Issue: **Branch-based build statuses are only updated for the builds initiated after this release. If you had past builds under a branch, you will see "No Builds" for that branch until a new build is initiated for that branch.

:::

### :muscle:Improvement

* Increased log viewer performance, especially in logs with large sizes
* Additional option fields in Flutter build configuration

### 🐞 Fixed

* Log viewer fixes
* Organization management fixes

## 0.8.0 - 2020-07-09 - Pre-Release Version with the High-Performance Cloud Infrastructure Powered by AWS

We are thrilled to announce our pre-release version. In this version, the platform has been fully redeployed on a high performance AWS instance in preparations for the final release.

This update also introduces new ways to manage workflow steps and user experience improvements.

:::caution

**Breaking change:** The new infrastructure requires reregistration of all user accounts currently registered. Please get in touch with us through the in-app messaging for any issues.

:::

### 🆕 New Feature

* New infrastructure - The platform is moved to the final release environment. You will be getting all around higher performance and responsiveness.;
* Organization and team management - In our last release, this feature was in the preview stage and now it is widely available with fixes and polishes. You can now create or join organizations and collaborate on the same workspace with multiple members.;
* Build step skipping controls - To avoid complete build failures in case of optional steps, you can now set each step individually to "skip to the next step if it fails".

### ;:muscle:Improvement

* User interface improvements - we made small changes to improve your experience further
* Improvements in the workflow steps to minimize potential failures

### 🐞 Fixed

* Reports fixes
* Minor user interface fixes

## 0.7.0 - 2020-06-29 - Xcode 12 Beta and Organization & Team Management

This update comes with the Xcode 12 Beta support right after its announcement and the new organization and team management features. This update also includes under-the-hood improvements in performance and user experience.

### 🆕 New Feature

* Xcode 12 beta support - You can select Xcode 12 beta in the build configuration for iOS 14 readiness.
* Smart build queue management - We are introducing a new way to manage the build queues for an improved build experience.
* Organization and team management (early access feature) - You can now create or join organizations and collaborate on the same workspace with multiple members. This feature is still in early access mode, so you may encounter issues with certain use cases.
* Sample projects in the build module - When connecting to a repository, you can directly select a  sample Appcircle project if you want to test drive the platform or if you don't have a repository in hand.

### ;:muscle:Improvement

* User interface improvements - we made small changes to improve your experience further
* Framework updates and the related under-the-hood improvements

### 🐞 Fixed

* We fixed a few issues regarding the account management feature released last week.
* Minor user interface fixes

## v0.6.0 - 2020-06-22 - Account Management and Build Status

In this update, we are introducing the account management interface.

### 🆕 New Feature

* Account Management Interface - You can now manage your details, change your password, connect to identity providers, access the list of current sessions, and view the identity logs in the My Account section.
* New Identity Providers - No need for email and password to register and login. You can use GitHub, Bitbucket, Google or Microsoft to login to your dashboard. If you already have an account with email, you can link an identity provider from the My Account section.
* Setting build status updates to the repository providers - You can now send updates about a commit to the repository providers for a complete CI/CD experience

### :muscle: Improvement

* Updates in the Flutter workflow steps.
* iOS build agent performance improvements. (You may see its effects later this week as we roll out the new build agents.)

### 🐞 Fixed

* We fixed a few issues regarding the reporting feature released last week.

## v0.5.0 - 2020-06-12 - Flutter Support and the New Reports

This is a major update, with the highlight being the Flutter build support.

### 🆕 New Feature

* Flutter Support - You can now build Flutter projects for iOS and Android. It also works with the workflows, so you can configure your Flutter builds in a powerful way just like the other frameworks supported by the Appcircle Build Module.
* New Reports - After the previous update bringing in the reporting feature, we now added new reports to the Distribute and Signing Identities module. These enterprise-grade reports are aimed to increase your visibility over the distribution processes.

### :muscle: Improvement

* Updates in the workflow steps and sample applications.
* iOS build agent updates - as the new major version Xcode is drawing near, we updated our primary iOS build agents to Catalina to ensure future Xcode compatibility.

### 🐞 Fixed

* We squashed a number of UI issues.

## v0.4.0 - 2020-06-03 - Open Beta Launch

This is a major update as we are gearing up for the final public release.

Invite codes are removed from registration with the platform and everyone can register for the public beta. During the beta, the product will be accessible with full features.

### :new: New Feature

* Reporting Feature - you can now view the reports for the Preview on Device feature in the dashboard. Other reports will also be released soon.
* Open Source Workflow Components - All the workflow components in the [Workflow Marketplace](https://docs.appcircle.io/workflows/index#workflow-marketplace) are now available at GitHub: [https://github.com/appcircleio/appcircle-workflow-components](https://github.com/appcircleio/appcircle-workflow-components). Feel free to contribute with your own workflow steps. Default workflow definitions are also available on GitHub
* Direct Documentation Access - The fields in the workflow and the build configuration screens are now linked with the documentation. You can directly view the related help document by clicking on the info button next to the specific fields.

### :muscle: Improvement

* Production-ready registration and login system with a major rehaul.

:::caution

**Breaking change:** The new authentication system requires reregistration of all user accounts currently registered. Please get in touch with us through the in-app messaging for any issues.

:::

* Improved iOS build agent performance.
* Improved build artifact downloads.

## v0.3.27 - 2020-05-10

### :new: New Feature

* Authentication with an SSH Key - You can now use your private SSH keys to connect your private repositories to Appcircle. Appcircle will use your SSH key to create a secure connection to your Git repository. :link: [**Connecting Your Git Repository**](https://docs.appcircle.io/build/adding-a-build-profile#connect-your-repository)****
* Workflow Marketplace - Appcircle's improved workflow window now includes Workflow Marketplace that allows you to add and remove additional workflow steps. We will be improving the marketplace steps constantly and adding new functionalities you can add to your build workflow. :link: [**Workflow Marketplace**](https://docs.appcircle.io/workflows/index#workflow-marketplace)****

## v0.3.26 - 2020-04-26

### :new: New Feature

* React Native support - You can now build iOS and Android applications developed with React Native. React Native build workflows allow you to select your Node version and run additional NPM/Yarn commands. :link: [**Building React Native Applications**](../build/building-react-native-applications.md)****

### :muscle: Improvement

* New Workflow Marketplace Steps - We are improving our Workflow Marketplace with more workflow steps that will help you perform more tasks in less time. Workflow steps are organized better for each platform and new workflow steps like Android Unit Tests and Android Lint are now available. :link: [**Workflow Marketplace**](https://docs.appcircle.io/workflows/index#workflow-marketplace)****
* Run Unit & UI Tests - You can now run Android unit tests and iOS unit & UI tests with corresponding workflow steps. Test results will be gathered and included in the downloadable artifacts archive.

## v0.3.25 - 2020-04-17

### :new: New Feature

* Appcircle now supports any public Git repository without needing to authenticate using your Github, BitBucket, or GitLab account. Simply enter the URL of your repository and Appcircle will connect your project from there. \
  \
  For further information please see: :link: [**Connecting a repository**](https://docs.appcircle.io/build/adding-a-build-profile#connect-your-repository)****

### :muscle: Improvement

* Xcode version 11.3.1 is now available for your iOS builds.
* UI improvements were made to improve usability and provide a better Appcircle experience.

## v0.3.24 - 2020-04-11

### :new: New Feature

* Appcircle Slack workspace is now open for your support request. Appcircle team will answer your questions 9 am to 6 pm EST. :link: [**Appcircle Slack Workspace**](https://slack.appcircle.io)****

### :muscle: Improvement

* If a build has multiple APK file outputs, each APK file will be included in the distribution module and can be downloaded separately. :link: [**Testing Portal**](../distribute/downloading-binaries.md)****
* Distribution emails and distribution portal is now showing application name with version.
* Notifications window is improved and now shows better information including color codes and more details about events.
* Environment variables in Git Clone workflow step are updated.
* Help page is updated with links to [**Appcircle Documentation**](https://docs.appcircle.io), Appcircle Contact Form and [**Appcircle Slack Workspace**](https://slack.appcircle.io).
* Miscellaneous UI improvements.

### :lady\_beetle: Fixed

* Information displayed on Distribution Module cards is fixed. The last updated field shows the latest file date in the profile and the Last shared field shows the last time the distribution was performed. :link: [**Distribution Profiles**](../distribute/create-or-select-a-distribution-profile.md)****

## v0.3.23 - 2020-04-03

### :muscle: Improvement

* A proper OS related icon will be displayed on distribution emails if there is no application icon present.
* Android Keystores can now be downloaded.
* Expired signing certificates now indicate the expiration date in red.
* When manual distribution selected for a completed build, if there are no distribution profiles set in build configuration, Appcircle will ask you to define one.
* Miscellaneous UI improvements.

### :lady\_beetle: Fixed

* When an Android Keystore was removed from Signing Identities module, it still appeared on build configuration. This bug was fixed.

## v0.3.22 - 2020-03-28

### :new: New Feature

* Appcircle now will automatically update the branch list when a branch is added, renamed or removed from Git repository in Github or BitBucket.
* Live support service is now active. You can click on the chat icon and connect with us weekdays 9 am - 6 pm EST.

### :muscle: Improvement

* When a build is canceled, related working agents are killed immediately to improve performance.
* Ruby version is updated to 2.6.5 on iOS virtual machines and 2.5.5 for Android virtual machines.
* New parameters are added to iOS native specific Build, Sign and Simulator workflow steps.
* Exit codes are now shown on the log window.

### :lady\_beetle: Fixed

* Error logs for custom scripts in workflow steps are now displaying properly.
* Safari related issues are fixed.
* Log window is improved for performance and stability.
* Minor UI and UX issues are fixed.
* iOS virtual machine date & time is synchronized with Apple NTP Server before starting the build.

## v0.3.21 - 2020-03-21

### :new: New Feature

* Auto-send Feature added.
* Resolved or closed issues on Github or Bitbucket are now included in the message to testers.

### :muscle: Improvement

* Build processed can be tracked realtime on build profiles dashboard.
* Custom script editor UI is updated.

### :lady\_beetle: Fixed

* There was a bug which prevented authenticating a new VCS account after the old one being revoked. RIP dear bug.

