---
title: Publish Information Overview
description: Overview of the Publish module in Appcircle
tags: [publish, publish module, publish information]
sidebar_position: 1
---

import ContentRef from '@site/src/components/ContentRef';
import Screenshot from '@site/src/components/Screenshot';

# Publish Information Overview

The Publish module provides users with several key actions to manage their application versions effectively. Below is an overview of each menu item and its function within the system:

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3857-pub1.png' />

## [App Store Connect Information](/publish-module/publish-information/app-information)

For a binary to be successfully sent for review, certain information must be completed. By using Appcircle's App Information feature, you can update the required information for binary submission.

## [Check Release Status](/publish-module/publish-information/check-release-status)

With the Check Release Status function, you can instantly update the status information of the version marked as Release Candidate. Make sure that one of the versions is marked as Release Candidate so that you can do a status check.

## [Publish Details](/publish-module/publish-information/publish-details)

This option provides an in-depth view of the selected version's publish process. Users can review the steps taken, configurations used, and outcomes of the publish sequence. It's an essential resource for understanding the specific details of a version's journey through the publish workflow.

## [Google Play Console Information](/publish-module/publish-information/google-play-information)

For Android binaries, by using Appcircle's Google Play Console Information feature, you can update the required information for binary submission.

## [Marking Release Candidates](/publish-module/publish-information/marking-release-candidates)

This action is used to change the status of a build that has been previously marked as a Release Candidate (RC). This might be necessary if the build is found to have issues that require it to be retracted from the release candidate status, indicating it's not yet ready for production release.

## [Binary Information](/publish-module/publish-information/binary-information)

Selecting this menu item displays detailed information about the application binary. This includes metadata such as the build version, creation date, binary size, and any relevant identifiers. It's particularly useful for developers and release managers who need to verify binary specifics before distribution.

## [Metadata Details](/publish-module/publish-information/meta-data-information)

The Meta Data Information option provides a comprehensive overview of the version's metadata. This includes details such as the application name, version, build number, and other relevant information. Users can review and edit metadata to ensure accurate and consistent versioning across the application.

## [Resign Binary](/publish-module/publish-information/resign-binary)

The Resign Binary feature allows users to resign both iOS and Android application binaries. For iOS applications, users can change provisioning profiles or app entitlements, while for Android applications, users can resign binaries with a new keystore. This feature is essential for updating app distribution settings and security credentials without requiring a new build.

## [History](/publish-module/publish-information/history)

The History has two sections: The Publish History and The Resign History.

The Publish History gives users a chronological log of all publish actions taken for a specific version. It allows users to track and audit the deployment process over time, which can be crucial for compliance, troubleshooting, and historical analysis.

The Resign History gives users a chronological log of all resign actions that was done within the Publish Module for a specific app version.

## [Downloading Binaries](/publish-module/publish-information/download)

This functionality enables users to download the binary directly from the Publish module. This is useful for offline review, storage, or distribution purposes. The download feature ensures that users can access and disseminate the application's build even outside the publish platform.

## [Cancel Submission](/publish-module/publish-information/cancel-submission)

Canceling a submission on the App Store can be crucial for developers who need to make last-minute changes or corrections. Learn how to efficiently cancel your app submission, understand common pitfalls, and ensure a smoother app review process.

## [Reject Binary](/publish-module/publish-information/reject-binary)

Binary rejection on Appcircle can delay your app's launch. Discover the top reasons for binary rejection, how to address them effectively, and ensure your app meets guidelines for a successful approval process. Optimize your app's chances today!

## [Delete](/publish-module/publish-information/delete)

The Delete option provides a way to remove a version from the system. It should be used with caution as it will permanently eliminate the selected version and all associated data from the Publish module. This feature helps in maintaining a clean and organized workspace by removing obsolete or unnecessary versions.

---

Each menu item is an integral part of the Publish module, providing comprehensive tools for managing application versions from creation to deployment. Users should familiarize themselves with these options to fully leverage the capabilities of the Publish system.

For further details on each menu item, refer to the corresponding section in this documentation.