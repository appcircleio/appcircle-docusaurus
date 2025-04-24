---
title: Portal Customization
description: Customize the appearance and authentication settings of your Enterprise App Store in Appcircle
tags: [enterprise app store, customize, appearance]
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

You can customize the appearance of your portal by navigating to the Customize section.

The Customization feature allows you to tailor the login page of your Enterprise Portal to align with your organization's branding. This feature enables you to modify key elements to create a consistent and professional appearance that reflects your corporate identity.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5909-eas1.png' />

- **Logo**: Replace the default logo with your company’s logo to reinforce brand recognition.
- **App Store Header**: Choose from three options to customize the positions of your store title and logo on your App Store header: Default, Title Left, or Title Center.
- **App Store Title**: Personalize the title displayed on the login page. You can update it to include your company name or any other relevant text that suits your brand.
- **Colors**: Customize the color scheme of your login page, including the background, text, and button, to reflect your brand’s unique palette.

The preview screen allows you to view changes in real time before saving them. The preview screen displays the Login screen, App Details screen, and App List screen as you customize your Enterprise Portal.

<Tabs
defaultValue="login"
values={[
{ label: 'Login', value: 'login' },
{ label: 'App List', value: 'list' },
{ label: 'App Detail', value: 'detail' },
]}
>
  <TabItem value="login">
<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5909-eas1.png' />
  </TabItem>
  <TabItem value="list">
<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5909-eas2.png' />
  </TabItem>
  <TabItem value="detail">
<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5909-eas3.png' />
  </TabItem>
</Tabs>

:::caution
If you are working on a sub organization, you will not have access to Customize and Settings sections on Enterprise App Store module.
Only the root organization has the privilege to Set up, Configure and Customize the Enterprise Portal.
:::