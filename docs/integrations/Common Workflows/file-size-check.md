---
title: File Size Check
metaTitle: File Size Check
metaDescription: File Size Check
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';

# File Size Check

The File Size Check component checks the size of your generated .ipa, .apk or .aab file. It compares it against the size you have given and if the size is exceeded, it either breaks the pipeline or shows it as a warning.

:::caution
Please note that you should use this step after **Xcodebuild for Devices** and **Android Build**.
:::
### For iOS
<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2582-size_order.png' />

### For Android
<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2582-size_order_android.png' />

When you enter this component detail, you need to specify **file size** and **check action**. The file size parameter here is the **maximum possible** **`.ipa`**, **`.apk`** and **`.aab`** size. If the archived application size exceeds this size, the pipeline will be **broken** or **warned** according to the warn or fail option you specify in the check action parameter.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2582-size_action.png' />

If you select Warn, this is how it will appear in your build list.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2582-size_warn.png' />


:::caution
Note that this step only controls the size of the application generated according to the size variable you specify. 
:::

https://github.com/appcircleio/appcircle-filesize-component