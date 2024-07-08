---
title: Send to Enterprise App Store
description: Learn how to send Binary to Enterprise App Store in the Publish module of Appcircle
tags: [publish, publish module, enterprise, app store, enterprise app store, review]
sidebar_position: 4
---

import Screenshot from '@site/src/components/Screenshot';

# Send to Enterprise App Store

With Appcircle's Publish module, you can submit your application to external stores such as App Store, Google Play, Huawei AppGallery or Microsoft Intune, as well as to Appcircle's Enterprise App Store module.

Enterprise App Store offers a store structure that you can use and customise for internal application distribution. For detailed information, please see the [**Enterprise App Store document**](/enterprise-appstore).


### Prerequisites

There is no prerequisite required for this step to work. You can use this step anywhere you want in the Flow.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3973-sendEnterprise.png' />


:::caution Send to Enterprise App Store

If the binary you want to send is available in the Enterprise App Store profile, the step will fail due to version conflict.

Make sure that you are not sending a version that exists in the Enterprise App Store profile.

:::

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-publish-send-to-enterprise-store