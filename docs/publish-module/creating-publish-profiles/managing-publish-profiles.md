---
title: Managing Publish Profiles
metaTitle: Managing Publish Profiles
metaDescription: Managing Publish Profiles
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';

# Managing Publish Profiles

Publish profiles are used to define the target platforms and configurations for the application distribution. You can create multiple publish profiles for different target platforms and configurations and select the relevant publish profile for each build profile.

### Rename Publish Profile

Appcircle allows previously created Publish profiles to be renamed.

To do this, click on the three dots at the top right of the relevant publish profile in the profiles list and select **Rename**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-rename.png' />

:::caution
Publish profile names must be unique for both **`iOS`** and **`Android`**.

For example, if you have a Publish profile named **`My Great App`** for iOS Publish, Appcircle will not allow you to create a profile named **`My Great App`** again for Android Publish or iOS Publish.

Also, you cannot rename a Publish profile to an existing name on the same platform.
:::

### Delete Publish Profile

To delete the Publish profile, click on the three dots at the top right of the relevant Publish profile in the profiles list and select **Delete**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-remove.png' />

:::caution
Appcircle **does not delete** the application that has been submitted to the stores.

By deleting the Publish profile, all the application versions and Publish action logs related to that publish profile will be removed on the Appcircle side.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-remove-confirm.png' />
