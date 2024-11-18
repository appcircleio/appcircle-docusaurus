---
title: Add a Badge to Your App Icon
description: Learn how to add a badge to your app icon with Appcircle's badge component.
tags: [badge, app icon, version, build, appcircle, mobile ci/cd]
---


import Screenshot from '@site/src/components/Screenshot';

# Add a Badge to Your App Icon

With Appcircle's **Add Badge to Your App Icon** component, you can add badges and version information to your app icon, which you can also customize. This helps testers easily identify the version they are testing directly on the application icon.

|Original|Modified|
|--------|------|
|![Original Image](https://cdn.appcircle.io/docs/assets/be-3069-original-icon.png)|![Modified Image](https://cdn.appcircle.io/docs/assets/be-3069-badge-icon.png)|

### Prerequisites

Before running the **Add a Badge to Your App Icon** step, you must complete certain prerequisites, as detailed in the table below:

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [**Git Clone**](/workflows/common-workflow-steps#git-clone) | The repository needs to be cloned to begin the badge-adding process. After this step, the variable `AC_REPOSITORY_DIR` will be set. |

:::caution

If you are using the [**Increment Build and Version Number**](/versioning/ios-version) component in your workflow and you want to print the current version information on the icon, this step should be used before the **Add Badge to Your App Icon** component.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3061-badgeOrder1.png' />


### Input Variables

This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3061-badgeInput.png' />

| Variable Name                            | Description                         | Status           |
|-------------------------------|------------------------------------------------|------------------|
| `$AC_ICONS_PATH`         | Specifies the path of icon files. For example: `MyProject/Assets.xcassets/AppIcon.appiconset`. The glob pattern can be used to select multiple image paths, for example, `app/src/main/res/mipmap*` to add badges to all PNGs under mipmap in this file path. | Required |
| `$AC_BADGE_TEXT`               | The text to appear in the badge on the top right corner. | Optional |
| `$AC_BADGE_VERSION`              | The version or build number to display at the bottom of the badge. | Optional |
| `$AC_BADGE_BGCOLOR`             | You can specify a full color name (e.g., `orange`), hex codes (e.g., `#FFA500`), or RGB values (e.g., `rgb(255,165,0)`). | Optional |
| `$AC_BADGE_TEXTCOLOR`           | You can specify a full color name (e.g., `white`), hex codes (e.g., `#FFFFFF`), or RGB values (e.g., `rgb(255,255,255)`). | Optional |

:::info

To use this component, you must provide the icon path from your project file. Here are some sample path usages:

- iOS Native: `MyProject/Assets.xcassets/AppIcon.appiconset`
- Android Native `app/src/main/res/`
- React Native iOS: `ios//MyProject/Assets.xcassets/AppIcon.appiconset/`
- React Native Android: `android/app/src/main/res/`
- Flutter iOS: `ios/Runner/Assets.xcassets/AppIcon.appiconset`
- Flutter Android: `android/app/src/main/res/`

**Note:** The glob pattern can be used to select multiple image paths. For example: `app/src/main/res/mipmap*` adds badges to all pngs under the mipmap in this file path.

:::

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-badge-component
