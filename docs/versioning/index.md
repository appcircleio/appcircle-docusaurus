---
title: Versioning
description: Understand and manage versioning for Android and iOS applications
tags: [versioning, android, ios]
---

import ContentRef from '@site/src/components/ContentRef';

# Versioning

Proper versioning is crucial for maintaining and updating mobile applications effectively. It helps in tracking different versions of your app, managing updates, and ensuring compatibility.

## Understanding Android Versioning

Android apps use a combination of `versionCode` and `versionName` in their build configurations:

- `versionCode`: An integer value that represents the version of the application code, which is incremented with every release.
- `versionName`: A string value that represents the release version to the user.

For a detailed guide on Android versioning, please refer to:

<ContentRef url="/versioning/android-version">
  Understanding Android Versioning
</ContentRef>

## Understanding iOS Versioning

iOS apps use `CFBundleShortVersionString` and `CFBundleVersion`:

- `CFBundleShortVersionString`: The release version number displayed to users.
- `CFBundleVersion`: The build number, which identifies an iteration of the app.

For a detailed guide on iOS versioning, please refer to:

<ContentRef url="/versioning/ios-version">
  Understanding iOS Versioning
</ContentRef>

This section provides resources and guidelines to understand and manage the versioning system for both Android and iOS platforms.
