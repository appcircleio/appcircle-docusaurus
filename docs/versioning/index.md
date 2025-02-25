---
title: Versioning
description: Understand and manage versioning for Android and iOS applications
tags: [versioning, android, ios]
---

import ContentRef from '@site/src/components/ContentRef';

# Versioning

Proper versioning is crucial for maintaining and updating mobile applications effectively. It helps in tracking different versions of your app, managing updates, and ensuring compatibility.

## [iOS Versioning](/versioning/ios-version)

iOS apps use `CFBundleShortVersionString` and `CFBundleVersion`:

- `CFBundleShortVersionString`: The release version number displayed to users.
- `CFBundleVersion`: The build number, which identifies an iteration of the app.

## [Android Versioning](/versioning/android-version)

Android apps use a combination of `versionCode` and `versionName` in their build configurations:

- `versionCode`: An integer value that represents the version of the application code, which is incremented with every release.
- `versionName`: A string value that represents the release version to the user.

This section provides resources and guidelines to understand and manage the versioning system for both iOS and Android platforms.