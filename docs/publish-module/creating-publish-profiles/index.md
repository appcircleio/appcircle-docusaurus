---
title: Creating Publish Profiles
description: Learn how to create publish profiles in Appcircle
tags: [publish, publish profiles, distribution]
sidebar_position: 1
---

# Creating Publish Profiles

import Screenshot from '@site/src/components/Screenshot';

After building the application, we can start the publishing process by sending it to the Publish module.

For this, it is necessary to first create a publish profile within the Publish module. Afterwards, the relevant publish profile must be selected from the **Distribution** tab in the configuration of the relevant profile in the Build module.

In order to create a publish profile, click on the "Add New" button in the Publish module.

### Create Profile Manually

There are two different ways to create a Publish profile. One of them is to create it manually.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3923-publishCreateModal.png' />

When manual creation is selected, the name and bundleID fields required for the Publish profile must be filled in.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3923-publishCreateManual.png' />

- **Publish Profile Name**: The name Publish profile is the name given to distinguish your profile from other profiles and appears on the profile card.
- **BundleID**: BundleID is the unique identifier of your application. It is hard-coded when the profile is created and cannot be changed afterwards.

:::danger

Please note that once the BundleID value of your profile has been set, it cannot be changed. Therefore, make sure that it is entered correctly. 

:::

After manually creating your profile, you will see your profile card on the Publish screen.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3923-publishManualCard.png' />

### Create from App Store Connect

Another way to create a Publish profile is to use your existing apps on **App Store Connect**. This feature of Appcircle allows you to automatically create profiles with your existing **App Store Connect** apps.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3923-publishCreateASCimport.png' />

When you create a Publish profile via App Store Connect, your existing apps are listed on Appcircle. You can create your profiles by making multiple selections. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3923-publishImportASC.png' />

Based on the apps you select from the list, Appcircle will automatically create a profile card with your app name and BundleID value.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3923-publishASCCard.png' />