---
title: SwiftLint
metaTitle: SwiftLint
metaDescription: SwiftLint
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';

# SwiftLint
This step installs [SwiftLint](https://github.com/realm/SwiftLint/) and runs swiftlint with given options. Note that if you are using Cocoapods, you should add this step after the **Cocoapods Install** step. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2613-lint_order.png' />

:::caution
If you are using **Swift Package Manager (SPM)**, do not use this step. SPM packages will be compiled in other steps that work with **Xcode**, such as **Xcodebuild for Devices.**
:::
:::warning
If you are using **Cocoapods**, note that this step is dependent on the **Cocoapods Install** step. Otherwise the SwiftLint component will **fail** and the **pipeline will break.**
:::

You can also customize your SwiftLint step with the options in the component.

- With the Range option, you can run SwiftLint on your entire project or only on changes in PR.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2613-lint_range.png' />

- You can change the report type with the Reporter format option. This option supports extensions such as **`html`**, **`json`**, **`junit`** etc.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2613-lint_format.png' />

- If there is a failure in the running lint, you can break the pipeline with the **Strict** option, if you want the logs to be simpler, you can make the report file simpler with the **Quiet Mode** feature.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2613-lint_strict.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2613-lint_quiet.png' />

https://github.com/appcircleio/appcircle-swiftlint-component