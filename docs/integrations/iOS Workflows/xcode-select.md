---
title: Xcode Select
metaTitle: Xcode Select
metaDescription: Xcode Select
sidebar_position: 3
---
import Screenshot from '@site/src/components/Screenshot';

## Xcode Select (Version)


This step is used to specify the Xcode version to be used during the build process. All available versions of Xcode can be seen from configuration tab. 

- For this, open configurations in build profile.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2585-xcode_select_config.png' />

- Create a new configuration set or use existing one

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2585-xcode_select_config_details.png' />

- After open configuration set, you will see **Xcode Version** section. Now you can select a version for Xcode.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2585-xcode_select_list.png' />

:::info
Appcircle provides new versions of Xcode (including Beta versions) within 24 hours after they released. 
:::
:::caution

### Pool-Based Xcode Version Selection

A version other than the Xcode versions on the configuration page should not be entered manually as the Xcode select workflow argument.
Because the Xcode versions on the configuration page are the versions installed on runners.
Entering an unavailable Xcode version may cause the build to fail.
You can review the documentation for detailed information about the Xcode version selection [here](../self-hosted-appcircle/self-hosted-runner/configure-runner/manage-pools.md/#pool-based-xcode-version-selection).
:::

https://github.com/appcircleio/appcircle-xcode-select-component
