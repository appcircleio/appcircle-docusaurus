---
title: BrowserStack App Automate
metaTitle: BrowserStack App Automate
metaDescription: BrowserStack App Automate
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';


## BrowserStack App Automate - XCUI

Run your XCUI tests on BrowserStack App Automate. You need to add **Xcodebuild Build for Testing** before this step to create the required `$AC_TEST_IPA_PATH` and `$AC_UITESTS_RUNNER_PATH` files. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2587-bs_order.png' />

:::info
After **Xcodebuild Build for Testing** step runs, `$AC_TEST_IPA_PATH` and `$AC_UITESTS_RUNNER_PATH` paths will be created automatically. The BrowserStack component depends on these paths.
:::

:::warning
When the build step order is not like this, **BrowserStack** will throw an **error** and **break the pipeline** because it cannot find the paths that your step depends on. 
- **Note that this step is dependent on Xcodebuild Build for Testing**
:::

#### Configuration of BrowserStack

You need to enter your BrowserStack **Username** and **Access Key** to use this step. This step will send the ipa created for the test to the BrowserStack dashboard with the credentials you provide. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2587-bs_name.png' />

:::warning
**Do not specify the Access Key directly in a hard coded format in steps. Please use Environment Variables when using potentially sensitive variables like this.**
:::

At the same time, if you have custom configuration when you use BrowserStack, you can send a payload. If you have not a custom payload, this step comes with a default payload.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2587-bs_payload.png' />

In addition, you can specify a timeout period for the running time of the step. The duration is in seconds.

[https://github.com/appcircleio/appcircle-browserstack-xcui-component](https://github.com/appcircleio/appcircle-browserstack-xcui-component)