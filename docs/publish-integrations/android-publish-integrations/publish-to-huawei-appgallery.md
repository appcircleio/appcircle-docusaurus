---
title: Publish to Huawei AppGallery
description: Publish your Android applications to Huawei AppGallery with Appcircle
tags: [android, android integrations, android publish integrations, huawei appgallery, publish appgallery]
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';
import RunnerUsage from '@site/docs/\_publish-steps-runner-usage-caution.mdx';

# Publish to Huawei AppGallery

Appcircle supports sending [APK](https://developer.huawei.com/consumer/en/doc/app/agc-help-releaseapkrpk-0000001106463276) and [AAB](https://developer.huawei.com/consumer/en/doc/app/agc-help-releasebundle-0000001100316672) binaries to [Huawei AppGallery](https://appgallery.huawei.com/) through the Publish module.

<RunnerUsage />

### Prerequisites

Before uploading a binary to the store, please make sure that an application listing is created in Huawei AppGallery Connect and the initial binary is manually uploaded with the same keystore and the application ID. Otherwise, the store upload process will fail.

You also need to have an AppGallery Connect API and its key as a JSON file. Please refer to the following document for more information on creating your API key.

<ContentRef url="/account/my-organization/security/credentials/adding-huawei-api-key">
  Adding Huawei AppGallery API Key
</ContentRef>

After completing the integration with Huawei AppGallery API Key, go to [Publishing Settings](/publish-to-stores-module/publish-settings). In the [`Store Credential`](/publish-to-stores-module/publish-settings#store-credentials) section, select the Huawei AppGallery API Key you uploaded, from the drop-down list.

If you are using [Publish Variables](/publish-to-stores-module/publish-settings#publish-variables), you should select them in the [Publishing Settings](/publish-to-stores-module/publish-settings) window.

## Input Variables

The parameters required for this step to work as expected are listed below:

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-publishflow-publish-huawei-appgallery-1.png'/>

| Variable Name       | Description                                                                                                                                                                                                                                  | Status    |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| `$AC_HUAWEI_APP_ID` | It is required to publish the app to Huawei AppGallery. You can find the App ID on the [Huawei Developer Console](https://developer.huawei.com/consumer/en/console) by navigating to `App Services` > `AppGallery Connect` > `My Apps` > `your app` > `App Information`. | Required  |
| `$AC_RELEASE_NOTES` | Provides release notes for the submission to Huawei AppGallery. | Optional  |

## Output Variables

**Publish to Huawei AppGallery** step does not produce any output. However, you can check the logs to see whether your app has successfully accessed Huawei AppGallery.

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-publish-send-to-appgallery.git


## FAQ

### App is not visible on Huawei AppGallery after a successful publish

**Question**:

Publishing to Huawei AppGallery completes successfully on Appcircle, but the app does not appear on the Huawei Store. The same build is visible on Google Play without any issues. Why does this happen?

**Answer**:

This issue can occur if there is a previous rollout on Huawei AppGallery that has not been completed or canceled.
We observed that when an incomplete or ongoing rollout exists, Huawei AppGallery may block the new upload even though Appcircle reports the publish step as successful.

**Solution**:

- Cancel the previous incomplete rollout on Huawei AppGallery.
- After canceling the old rollout, you will see that the app you previously submitted has been successfully installed.

### It works on my machine. Why does it fail on Appcircle?

**Question**

The build works successfully on my local machine, but it fails when running on Appcircle. Why does this happen?

**Answer**

This difference is usually caused by **environment cleanliness and caching behavior**.

**Appcircle** provisions a **completely clean machine for every build**. Each run starts from a fresh environment with:

* No cached Gradle files
* No previously downloaded dependencies
* No leftover build artifacts

This is an even **cleaner approach than a local clean build**, which often still relies on cached data.

As a result, issues that are hidden by local caches may surface on Appcircle.


**Why IDE Cache Invalidation Is Not Enough**

Many developers rely on **Invalidate Caches / Restart** in Android Studio.

While this step can be helpful, it is important to understand its limitations:

* It clears **Android Studio IDE caches only**
* It does **not** delete Gradle caches
* The `~/.gradle` directory remains untouched

This means local builds may still succeed due to cached Gradle data, even though the environment is not truly clean.


**Recommended Steps for a True Local Clean Build**

To reproduce Appcircle’s clean environment locally, follow these steps.

#### 1️⃣ Clean and Refresh Dependencies

This removes old build outputs and forces Gradle to re-download dependencies:

```bash
./gradlew clean build --refresh-dependencies
```

#### 2️⃣ Clear Gradle Caches (for Major Gradle Updates)

If you upgraded Gradle significantly (for example, **Gradle 7 → Gradle 8**), you should also remove cached Gradle files:

```bash
# Linux / macOS
rm -rf ~/.gradle/caches/
rm -rf ~/.gradle/wrapper/
```

This ensures no outdated Gradle artifacts remain.


#### 3️⃣ (Optional) Invalidate IDE Caches

You may still run **Invalidate Caches / Restart** in Android Studio as an additional step, but it should not replace the Gradle cleanup steps above.

---

#### 4️⃣ Run a Full Clean Build Locally

From the terminal:

```bash
./gradlew clean
./gradlew build
```

Or from Android Studio:

* **Build > Clean Project**
* **Build > Rebuild Project**

Following the steps above will help you identify issues that only appear in clean CI environments and reduce discrepancies between local and Appcircle builds.
