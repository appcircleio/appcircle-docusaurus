---
title: Add Badge to Your App Icon
metaTitle: Add Badge to Your App Icon
metaDescription: Add Badge to Your App Icon
sidebar_position: 4
---

import Screenshot from '@site/src/components/Screenshot';

# Add Badge to Your App Icon

With Appcircle's **Add Badge to Your App Icon** component, you can add your badge and version information to your app icon. Also, you can customize them. In this way, testers can easily understand which version they are testing on the application icon.

|Original|Modified|
|--------|------|
|![Original Image](https://github.com/appcircleio/appcircle-badge-component/blob/main/assets/original.png?raw=true)|![Modified Image](https://github.com/appcircleio/appcircle-badge-component/blob/main/assets/badged.png?raw=true)|

### Prerequisites

The workflow steps that need to be executed before running this step, along with their respective reasons, are listed in the table below.

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [Git Clone](https://docs.appcircle.io/workflows/common-workflow-steps/#git-clone) | The repo needs to be cloned in order to start the badge-adding process. After this step works, the variable `AC_REPOSITORY_DIR` will be created.|

:::caution

If you are using the [**Increment Build and Version Number**](/versioning/ios-version) component in your workflow and you want to print the current version information on the icon, this step should be used before the Add Badge to Your App Icon component.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3061-badgeOrder1.png' />


### Input Variables

You can find all the parameters required for this step in the table below, with their descriptions in detail.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3061-badgeInput.png' />

| Variable Name                            | Description                         | Status           |
|-------------------------------|------------------------------------------------|------------------|
| `$AC_ICONS_PATH`         | Specifies the path of icon files. For example: `MyProject/Assets.xcassets/AppIcon.appiconset`. The glob pattern can be used to select multiple image paths. For example: `app/src/main/res/mipmap*` adds badges to all pngs under mipmap in this file path. | Required |
| `$AC_BADGE_TEXT`               | Text that appears in the right corner. | Optional |
| `$AC_BADGE_VERSION`              | Version or build number that will appear at the bottom. | Optional |
| `$AC_BADGE_BGCOLOR`             | You can use a full color name `(orange)`, `hex codes(#FFA500)`, or rgb values `(rgb(255,165,0))`. | Optional |
| `$AC_BADGE_TEXTCOLOR`           | You can use a full color name `(white)`, `hex codes(#FFFFFF)`, or rgb values `(rgb(255,255,255))`. | Optional |

:::info

In order to use this component, the icon path in the project file must be given. Sample path usages for this are listed below.

- iOS Native: `MyProject/Assets.xcassets/AppIcon.appiconset`
- Android Native `app/src/main/res/`
- React Native iOS: `ios//MyProject/Assets.xcassets/AppIcon.appiconset/`
- React Native Android: `android/app/src/main/res/`
- Flutter iOS: `ios/Runner/Assets.xcassets/AppIcon.appiconset`
- Flutter Android: `android/app/src/main/res/`

**Note:** The glob pattern can be used to select multiple image paths. For example: `app/src/main/res/mipmap*` adds badges to all pngs under mipmap in this file path.

:::

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-badge-component
